#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.

Extracts the full model dataset from the Next.js RSC payload embedded in the page.

V18 (2026-09-12): the RSC payload no longer carries the old 96-field array —
AA now splits the data across TWO `models` arrays:
  * the main benchmark array (~50 fields: all evaluation scores, pricing,
    speed/latency, creator color/logo/name, paramClass, …)
  * a display-metadata array (8 fields: slug, name, releaseDate, deprecated,
    isReasoning, effort, release, creator{id,name,logo})
The scraper picks the richest array as `main` and merges the metadata
fields (name, releaseDate) into it by `slug`, restoring the old `name` field.

Fields AA removed from the models payload since v17: agenticIndex,
codingIndex (AA Agentic / Coding Index), intelligenceIndexCostTotal, blended
prices, modelCreatorSlug, cweBench, mlcrOverall, … New benchmark columns
now carried: analystAgent, tauBanking (τ³-Bench Banking),
terminalbenchV21 / terminalbenchV40 ("Intelligence Index v4.3: … 𝜏³-Banking
is removed, and Terminal-Bench moves to v4.0").

The RSC payload contains EVERY model regardless of the page's Status filter
(Current / All) — including deprecated ones (`deprecated: true`), which
analyze.py keeps (Status: All) as of Version 10.
"""

import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "https://artificialanalysis.ai/leaderboards/models"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
MIN_MODELS_EXPECTED = 100

# JavaScript code shared across extraction approaches
_SEARCH_MODELS_JS = """
function _findBestModels(obj, maxDepth) {
  let best = null;
  let bestFC = 0;
  function search(o, d) {
    if (d > maxDepth || !o || typeof o !== 'object') return;
    if (!Array.isArray(o) && o.models && Array.isArray(o.models) && o.models.length > 0) {
      const fc = Object.keys(o.models[0]).length;
      if (fc > bestFC) { bestFC = fc; best = o.models; }
    }
    if (Array.isArray(o)) for (const v of o) search(v, d + 1);
    else for (const v of Object.values(o)) search(v, d + 1);
  }
  search(obj, 0);
  return best;
}
"""

# Primary extraction: parse RSC script tags directly.
# V18: collect ALL `models` arrays (main benchmark array + metadata arrays),
# so the Python side can merge them by slug.
EXTRACT_JS = """
(() => {
  ${SEARCH}
  const scripts = document.querySelectorAll('script');
  const found = [];

  for (let i = 0; i < scripts.length; i++) {
    const text = scripts[i].textContent || '';
    if (!text.includes('__next_f') || !text.includes('models')) continue;

    const match = text.match(/^self\\.__next_f\\.push\\((.+)\\)$/s);
    if (!match) continue;

    try {
      const arr = eval(match[1]);
      const content = arr[1];
      const colonIdx = content.indexOf(':');
      const data = JSON.parse(content.substring(colonIdx + 1));
      const m = _findBestModels(data, 25);
      if (m) found.push(m);
    } catch(e) { /* skip */ }
  }
  return JSON.stringify(found);
})()
""".replace("${SEARCH}", _SEARCH_MODELS_JS)


def scrape_leaderboard():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        print(f"[1/3] Navigating to {URL} ...")
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(8000)  # Wait for RSC stream to complete

        print("[2/3] Extracting model data from RSC payload ...")
        raw_json = page.evaluate(EXTRACT_JS)

        arrays = json.loads(raw_json)
        print(f"  models arrays found: {len(arrays)} "
              f"({[len(a) for a in arrays]} models, "
              f"{[len(a[0].keys()) if a else 0 for a in arrays]} fields each)")

        # V18: main = the array whose models carry the most fields (the
        # benchmark/pricing array). Every other array is treated as a
        # metadata source: fields absent from main are merged in by slug
        # (restores `name`, `releaseDate`, …).
        models = max(arrays, key=lambda a: len(a[0].keys())) if arrays else []
        if len(arrays) > 1:
            main_slugs = {m.get("slug") for m in models}
            meta_by_slug = {}
            for arr in arrays:
                if arr is models:
                    continue
                for m in arr:
                    sl = m.get("slug")
                    if sl and sl in main_slugs and sl not in meta_by_slug:
                        meta_by_slug[sl] = m
            n_merged = 0
            for m in models:
                meta = meta_by_slug.get(m.get("slug"))
                if not meta:
                    continue
                for k, v in meta.items():
                    if k not in m and v is not None:
                        m[k] = v
                        n_merged += 1
            print(f"  Merged metadata fields into {len(meta_by_slug)} models "
                  f"({n_merged} field values, e.g. name/releaseDate)")

        print(f"  Extracted {len(models)} models")

        if models and len(models) > 0:
            print(f"  Fields per model: {len(models[0].keys())}")
        if models and len(models) > 0:
            print(f"  Fields per model: {len(models[0].keys())}")
            
            # Print sample (安全格式化，防止 '?' 或 '--' 导致 ValueError)
            m = models[0]
            
            raw_cost = m.get('intelligenceIndexCostTotal')
            try:
                # 如果是 None、空字符串或 '--'，则降级为 '?'，否则转为浮点数格式化
                if raw_cost in (None, "", "--", "?"):
                    cost_str = "$?"
                else:
                    cost_str = f"${float(raw_cost):.2f}"
            except (ValueError, TypeError):
                cost_str = "$?"

            print(f"  Sample: {m.get('name', '?')}, "
                  f"reasoning={m.get('reasoningModel', '?')}, "
                  f"intelIndex={m.get('intelligenceIndex', '?')}, "
                  f"costTotal={cost_str}, "
                  f"inputPrice=${m.get('price1mInputTokens', '?')}, "
                  f"outputPrice=${m.get('price1mOutputTokens', '?')}")

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
            print(f"WARNING: Only {len(data) if data else 0} models scraped (expected {MIN_MODELS_EXPECTED})")
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
