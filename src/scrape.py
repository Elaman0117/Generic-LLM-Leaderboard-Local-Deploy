#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.

Extracts the full model dataset from the Next.js RSC payload embedded in the page.
This gives us ~500 models with 88 fields including:
  - totalParameters / activeParameters: model parameter counts (in billions)
  - All pricing (input, output, cache_hit, cache_write, blended at various ratios)
  - All intelligence evaluation scores (gpqa, hle, scicode, etc.)
  - Speed, latency, and timing data
  - Token counts for the Intelligence Index evaluations
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

# Primary extraction: parse RSC script tags directly
EXTRACT_JS = """
(() => {
  ${SEARCH}
  const scripts = document.querySelectorAll('script');
  let bestModels = null;
  let bestFieldCount = 0;

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
      const found = _findBestModels(data, 25);
      if (found) {
        const fc = Object.keys(found[0]).length;
        if (fc > bestFieldCount) { bestFieldCount = fc; bestModels = found; }
      }
    } catch(e) { /* skip */ }
  }
  return JSON.stringify(bestModels || []);
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

        models = json.loads(raw_json)
        print(f"  Extracted {len(models)} models")

        if models and len(models) > 0:
            print(f"  Fields per model: {len(models[0].keys())}")
            # Print sample
            m = models[0]
            print(f"  Sample: {m.get('name', '?')}, "
                  f"reasoning={m.get('reasoningModel', '?')}, "
                  f"intelIndex={m.get('intelligenceIndex', '?')}, "
                  f"totalParams={m.get('totalParameters', '?')}B, "
                  f"activeParams={m.get('activeParameters', '?')}B, "
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
