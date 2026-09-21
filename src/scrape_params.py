#!/usr/bin/env python3
"""Scrape per-model total/active parameter counts from AA model detail pages.

Source: https://artificialanalysis.ai/models/<slug> — the FAQ JSON-LD /
rendered text states e.g. "MiMo-V2.5-Pro has 1.0 trillion parameters
(42 billion active)." while closed models say "has not disclosed the
model size or parameter count" (recorded as unknown and excluded
downstream).

V1 (params board): plain-HTTP fetch with gzip (no browser needed — the
probe verified the FAQ text is in the static HTML). Incremental:
output/param_cache.json keyed by slug is committed to the repo, so CI
only fetches new slugs. Units: billions (B); trillion=1000B,
million=0.001B. MoE keeps TOTAL. Name fallback ("32B" in model name)
applies only when the detail page yields nothing, flagged separately.

Usage:
  python src/scrape_params.py [--limit N] [--sleep S] [--force] [--only slug]
"""

import argparse
import datetime
import gzip
import json
import os
import re
import sys
import time
import urllib.request

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
CACHE_FILE = os.path.join(OUTPUT_DIR, "param_cache.json")

UNIT_TO_B = {"trillion": 1000.0, "billion": 1.0, "million": 0.001}

HAS_RE = re.compile(
    r"has\s+(\d[\d.,]*)\s*(trillion|billion|million)\s*parameters?"
    r"(?:\s*\(\s*(\d[\d.,]*)\s*(trillion|billion|million)\s*active\s*\))?",
    re.IGNORECASE,
)
UNDISCLOSED_RE = re.compile(
    r"has not disclosed the model size or parameter count", re.IGNORECASE
)
NAME_RE = re.compile(r"(\d+(?:\.\d+)?)\s*B\b")


def _num(s):
    return float(s.replace(",", ""))


def fetch_page(slug, timeout=60):
    req = urllib.request.Request(
        "https://artificialanalysis.ai/models/" + slug,
        headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "gzip"},
    )
    raw = urllib.request.urlopen(req, timeout=timeout).read()
    try:
        return gzip.decompress(raw).decode("utf-8", "replace")
    except OSError:
        return raw.decode("utf-8", "replace")


def parse_params(html, name):
    """Return (total_B, active_B, source)."""
    m = HAS_RE.search(html)
    if m:
        total = _num(m.group(1)) * UNIT_TO_B[m.group(2).lower()]
        active = None
        if m.group(3):
            active = _num(m.group(3)) * UNIT_TO_B[m.group(4).lower()]
        return total, active, "faq"
    if UNDISCLOSED_RE.search(html):
        return None, None, "undisclosed"
    nm = NAME_RE.search(name or "")
    if nm:
        return _num(nm.group(1)), None, "name"
    return None, None, "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sleep", type=float, default=0.3)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        models = json.load(f)
    cache = {}
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, encoding="utf-8") as f:
            cache = json.load(f)
    print(f"models={len(models)} cached={len(cache)}")

    targets = []
    for m in models:
        slug = m.get("slug")
        if not slug:
            continue
        if args.only and slug != args.only:
            continue
        if not args.force and slug in cache:
            continue
        targets.append(m)
    if args.limit:
        targets = targets[: args.limit]
    print(f"to_fetch={len(targets)}")

    done = 0
    for m in targets:
        slug = m["slug"]
        try:
            html = fetch_page(slug)
            total, active, source = parse_params(html, m.get("name", ""))
        except Exception as e:  # noqa: BLE001 — network flakiness; name fallback still applies
            nm = NAME_RE.search(m.get("name", "") or "")
            if nm:
                total, active, source = _num(nm.group(1)), None, "name-after-error"
            else:
                total, active, source = None, None, f"fetch_error: {type(e).__name__}"
        cache[slug] = {
            "slug": slug,
            "name": m.get("name"),
            "total_B": total,
            "active_B": active,
            "source": source,
            "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        }
        done += 1
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=1)
        if done % 25 == 0 or done == len(targets):
            print(f"  {done}/{len(targets)} ...", flush=True)
        time.sleep(args.sleep)

    by_source = {}
    for v in cache.values():
        by_source[v.get("source", "?").split(":")[0]] = by_source.get(v.get("source", "?").split(":")[0], 0) + 1
    n_known = sum(1 for v in cache.values() if v.get("total_B") is not None)
    print(f"Done. cache={len(cache)} known_total={n_known} by_source={by_source}")


if __name__ == "__main__":
    sys.exit(main())
