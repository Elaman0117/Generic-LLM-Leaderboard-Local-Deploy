#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.

Extracts the full model dataset (Status: All, including deprecated models)
from the Next.js page at https://artificialanalysis.ai/leaderboards/models?status=all.

V21 (2026-10-20): AA defaults the /leaderboards/models page to 'Status: Current' (273 models)
and carries initial data under `initialModels`. To extract ALL models (~706 models, including
430+ deprecated models), the scraper queries `?status=all`, retrieves the complete model dataset
from the rendered table instance (TanStack table state on the React fiber), traverses RSC payloads
for auxiliary metadata (releases, etc.), merges missing fields across arrays by slug, and resolves
release dates.
"""

import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "https://artificialanalysis.ai/leaderboards/models?status=all"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
MIN_MODELS_EXPECTED = 100

EXTRACT_FULL_JS = """
(() => {
  // 1. Try to get complete model array from TanStack table instance on the React fiber
  let tableModels = null;
  const table = document.querySelector('table');
  if (table) {
    const fiberKey = Object.keys(table).find(k => k.startsWith('__reactFiber$'));
    if (fiberKey) {
      let f = table[fiberKey];
      while (f) {
        if (f.memoizedProps && f.memoizedProps.table && f.memoizedProps.table.options && f.memoizedProps.table.options.data) {
          const d = f.memoizedProps.table.options.data;
          if (Array.isArray(d) && d.length > 0) {
            tableModels = d;
            break;
          }
        }
        f = f.return;
      }
    }
  }

  // 2. Also extract all model/release arrays from RSC scripts
  function _findAllModelArrays(obj, maxDepth) {
    const found = [];
    const seen = new Set();
    function search(o, d) {
      if (d > maxDepth || !o || typeof o !== 'object') return;
      if (Array.isArray(o)) {
        if (o.length > 0 && typeof o[0] === 'object' && o[0] !== null && 'slug' in o[0]) {
          if (!seen.has(o)) {
            seen.add(o);
            found.push(o);
          }
        }
        for (const v of o) search(v, d + 1);
      } else {
        for (const v of Object.values(o)) {
          search(v, d + 1);
        }
      }
    }
    search(obj, 0);
    return found;
  }

  const scripts = document.querySelectorAll('script');
  const rscArrays = [];
  const seenSigs = new Set();

  for (let i = 0; i < scripts.length; i++) {
    const text = scripts[i].textContent || '';
    if (!text.includes('__next_f')) continue;
    if (!text.toLowerCase().includes('model') && !text.includes('slug') && !text.includes('release')) continue;

    const pushPattern = /self\\.__next_f\\.push\\(\\s*(\\[.*?\\])\\s*\\)\\s*;?/gs;
    let m;
    let matchedAny = false;
    while ((m = pushPattern.exec(text)) !== null) {
      matchedAny = true;
      try {
        const arr = eval(m[1]);
        if (!arr || arr.length < 2 || typeof arr[1] !== 'string') continue;
        const content = arr[1];
        const colonIdx = content.indexOf(':');
        if (colonIdx === -1) continue;
        const data = JSON.parse(content.substring(colonIdx + 1));
        const modelArrays = _findAllModelArrays(data, 25);
        for (const a of modelArrays) {
          const sig = a.length + ':' + (a[0] ? a[0].slug : '');
          if (!seenSigs.has(sig)) {
            seenSigs.add(sig);
            rscArrays.push(a);
          }
        }
      } catch(e) { /* skip */ }
    }
    if (!matchedAny) {
      const match = text.match(/^self\\.__next_f\\.push\\((.+)\\)$/s);
      if (match) {
        try {
          const arr = eval(match[1]);
          if (arr && arr.length >= 2 && typeof arr[1] === 'string') {
            const content = arr[1];
            const colonIdx = content.indexOf(':');
            if (colonIdx !== -1) {
              const data = JSON.parse(content.substring(colonIdx + 1));
              const modelArrays = _findAllModelArrays(data, 25);
              for (const a of modelArrays) {
                const sig = a.length + ':' + (a[0] ? a[0].slug : '');
                if (!seenSigs.has(sig)) {
                  seenSigs.add(sig);
                  rscArrays.push(a);
                }
              }
            }
          }
        } catch(e) { /* skip */ }
      }
    }
  }

  return JSON.stringify({
    tableModels: tableModels,
    rscArrays: rscArrays
  });
})()
"""


def scrape_leaderboard():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"[1/3] Navigating to {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(8000)  # Wait for full table and data to settle

        print("[2/3] Extracting model data (Status: All) ...")
        raw_json = page.evaluate(EXTRACT_FULL_JS)
        payload = json.loads(raw_json)

        table_models = payload.get("tableModels")
        rsc_arrays = payload.get("rscArrays", [])

        candidate_arrays = list(rsc_arrays)
        if table_models and isinstance(table_models, list):
            candidate_arrays.append(table_models)

        print(f"  Arrays found: {len(candidate_arrays)} "
              f"(tableModels: {len(table_models) if table_models else 0}, "
              f"rscArrays: {len(rsc_arrays)})")

        # Select the primary dataset: the array with highest benchmark metric coverage and model count
        def array_score(a):
            if not a:
                return (0, 0, 0)
            intel_count = sum(1 for m in a if m.get("intelligenceIndex") is not None)
            total_fields = sum(len(m.keys()) for m in a)
            return (intel_count, len(a), total_fields)

        models = max(candidate_arrays, key=array_score) if candidate_arrays else []

        # Build release date map from all candidate arrays (releases, etc.)
        release_map = {}
        for arr in candidate_arrays:
            for r in arr:
                sl = r.get("slug")
                rd = r.get("releaseDate")
                if sl and rd and sl not in release_map:
                    release_map[sl] = rd

        if len(candidate_arrays) > 1 and models:
            models_by_slug = {m["slug"]: m for m in models if m.get("slug")}
            n_merged = 0
            for arr in candidate_arrays:
                if arr is models:
                    continue
                for item in arr:
                    slug = item.get("slug")
                    if slug and slug in models_by_slug:
                        target = models_by_slug[slug]
                        for k, v in item.items():
                            if k not in target and v is not None:
                                target[k] = v
                                n_merged += 1
            print(f"  Merged {n_merged} missing field values across {len(models_by_slug)} models "
                  f"(e.g. name/releaseDate/releaseSlug)")

        # Join releaseSlug -> release_map for any models missing releaseDate
        n_dated = 0
        for m in models:
            if m.get("releaseDate"):
                n_dated += 1
                continue
            rs = m.get("releaseSlug")
            if rs and rs in release_map:
                m["releaseDate"] = release_map[rs]
                n_dated += 1

        models_with_intel = sum(1 for m in models if m.get("intelligenceIndex") is not None)
        deprecated_count = sum(1 for m in models if m.get("deprecated"))

        if len(models) < MIN_MODELS_EXPECTED or models_with_intel < 50:
            raise RuntimeError(
                f"Extraction validation failed: {len(models)} models extracted "
                f"(expected >= {MIN_MODELS_EXPECTED}), {models_with_intel} models with "
                f"intelligenceIndex (expected >= 50). Available fields: "
                f"{list(models[0].keys()) if models else []}"
            )

        print(f"  Extracted {len(models)} models ({models_with_intel} with intelligenceIndex, "
              f"{deprecated_count} deprecated, {n_dated} with releaseDate)")

        if models and len(models) > 0:
            sample_model = next((x for x in models if x.get("intelligenceIndex") is not None and x.get("price1mInputTokens") is not None), models[0])
            print(f"  Fields per model: {len(sample_model.keys())}")
            
            raw_cost = sample_model.get('intelligenceIndexCostTotal')
            try:
                if raw_cost in (None, "", "--", "?"):
                    cost_str = "$?"
                else:
                    cost_str = f"${float(raw_cost):.2f}"
            except (ValueError, TypeError):
                cost_str = "$?"

            print(f"  Sample: {sample_model.get('name', '?')}, "
                  f"reasoning={sample_model.get('reasoningModel', '?')}, "
                  f"intelIndex={sample_model.get('intelligenceIndex', '?')}, "
                  f"costTotal={cost_str}, "
                  f"inputPrice=${sample_model.get('price1mInputTokens', '?')}, "
                  f"outputPrice=${sample_model.get('price1mOutputTokens', '?')}")

        print(f"[3/3] Saving to {OUTPUT_FILE} ...")
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(models, f, ensure_ascii=False, indent=2)

        browser.close()

    print(f"Done! {len(models)} models saved.")
    return models


if __name__ == "__main__":
    try:
        data = scrape_leaderboard()
        if not data or len(data) < MIN_MODELS_EXPECTED:
            raise RuntimeError(f"Scraping returned insufficient models: {len(data) if data else 0} (expected >= {MIN_MODELS_EXPECTED})")
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
