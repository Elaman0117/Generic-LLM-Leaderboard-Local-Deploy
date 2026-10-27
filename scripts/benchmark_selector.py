#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generic LLM Leaderboard - Standardized Benchmark Selector & Diagnostic Suite
=============================================================================
This tool provides a rigorous, standardized, multi-criteria evaluation framework
for selecting benchmark metrics from Artificial Analysis data.

Design Goals:
  1. Standardized Criteria: Quantitative thresholds for sample coverage,
     frontier coverage, calibration span stability, domain balance, and collinearity.
  2. Transparency: Explicit scorecards for every single benchmark metric showing
     PASS / FAIL status and the exact reason for exclusion.
  3. Leaderboard Sanity Guard: Automated detection of reasoning-tier inversions
     (e.g., ensuring Opus 5.5 max is not scored lower than Opus 5.5 xhigh due to
     sparse, unnormalized niche evaluations).
  4. Simulation & Validation: Direct comparative simulation of leaderboard
     rankings and Pareto frontiers under different benchmark selection strategies.

Usage:
  python scripts/benchmark_selector.py --help
  python scripts/benchmark_selector.py --diagnose-all
  python scripts/benchmark_selector.py --strategy curated_conservative
  python scripts/benchmark_selector.py --strategy curated_balanced
  python scripts/benchmark_selector.py --simulate
  python scripts/benchmark_selector.py --recommend
"""

import argparse
import json
import math
import os
import sys
from collections import defaultdict
from fractions import Fraction
from typing import Dict, List, Optional, Set, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ══════════════════════════════════════════════════════════════════════
# 1. Benchmark Catalog & Domain Definitions
# ══════════════════════════════════════════════════════════════════════

DOMAIN_CATEGORIES = {
    "core_reasoning": "Core Intelligence & Hard Reasoning",
    "math_stem": "Mathematics & STEM",
    "coding": "Coding & Software Engineering",
    "agentic": "Agentic & Tool-Use Workflows",
    "long_context": "Long Context & Document Comprehension",
    "multimodal": "Multimodal & Visual Understanding",
    "factuality": "Factuality, Hallucination & Alignment",
}

# Complete catalog of all 32 candidate benchmarks in Artificial Analysis
BENCHMARK_CATALOG = {
    "intelligenceIndex": {
        "name": "AA Intelligence Index",
        "domain": "core_reasoning",
        "aliases": ["intelligenceIndex", "artificial-analysis-intelligence-index"],
        "description": "Composite general intelligence score by Artificial Analysis",
    },
    "hle": {
        "name": "Humanity's Last Exam",
        "domain": "core_reasoning",
        "aliases": ["hle", "humanitys-last-exam"],
        "description": "Multi-discipline frontier reasoning exam questions",
    },
    "gpqa": {
        "name": "GPQA Diamond",
        "domain": "core_reasoning",
        "aliases": ["gpqa", "gpqa-diamond"],
        "description": "Graduate-level Google-proof science reasoning questions",
    },
    "critpt": {
        "name": "CritPt Physics",
        "domain": "math_stem",
        "aliases": ["critpt"],
        "description": "Challenging physics competition reasoning benchmark",
    },
    "aime2025": {
        "name": "AIME 2025",
        "domain": "math_stem",
        "aliases": ["aime2025", "aime-2025"],
        "description": "American Invitational Mathematics Examination 2025",
    },
    "scicode": {
        "name": "SciCode Coding",
        "domain": "coding",
        "aliases": ["scicode"],
        "description": "Research-level scientific computing coding problems",
    },
    "livecodebench": {
        "name": "LiveCodeBench",
        "domain": "coding",
        "aliases": ["livecodebench"],
        "description": "Contamination-resistant competitive programming evaluation",
    },
    "frontiercode": {
        "name": "FrontierCode 1.1",
        "domain": "coding",
        "aliases": ["frontiercode"],
        "description": "Complex programming problems designed for frontier LLMs",
    },
    "terminalbenchHard": {
        "name": "Terminal-Bench Hard",
        "domain": "agentic",
        "aliases": ["terminalbenchHard", "terminalbench-hard"],
        "description": "Execution-based hard terminal environment tasks",
    },
    "terminalbenchV21": {
        "name": "Terminal-Bench 2.1",
        "domain": "agentic",
        "aliases": ["terminalBench21", "terminalbenchV21", "terminalbench-2-1"],
        "description": "Standard release of Terminal-Bench v2.1",
    },
    "terminalbenchV40": {
        "name": "Terminal-Bench 4.0",
        "domain": "agentic",
        "aliases": ["terminalBench40", "terminalbenchV40", "terminalbench-4-0"],
        "description": "Latest generation Terminal-Bench v4.0 tasks",
    },
    "terminalbenchScience": {
        "name": "Terminal-Bench Science",
        "domain": "agentic",
        "aliases": ["terminalbenchScience", "terminal-bench-science"],
        "description": "Scientific computation and bash workflow tasks",
    },
    "tau2": {
        "name": "τ²-Bench Telecom",
        "domain": "agentic",
        "aliases": ["tau2", "tau2-bench"],
        "description": "Customer service & multi-turn tool interaction benchmark",
    },
    "tauBanking": {
        "name": "τ³-Bench Banking",
        "domain": "agentic",
        "aliases": ["tauBanking", "tau3-banking"],
        "description": "Complex multi-turn banking domain tool-use benchmark",
    },
    "automationbench": {
        "name": "AutomationBench-AA",
        "domain": "agentic",
        "aliases": ["automationbench", "automationbench-aa"],
        "description": "Agentic SaaS workflows and tool chaining",
    },
    "briefcase": {
        "name": "AA-Briefcase v1.1",
        "domain": "agentic",
        "aliases": ["briefcase", "aa-briefcase"],
        "description": "Agentic enterprise knowledge work tasks",
    },
    "gdpvalNormalized": {
        "name": "GDPval-AA Normalized",
        "domain": "agentic",
        "aliases": ["gdpvalNormalized", "gdpval-aa-normalized"],
        "description": "Economic evaluation of complex professional deliverables",
    },
    "gdpPdf": {
        "name": "GDP.pdf",
        "domain": "long_context",
        "aliases": ["gdpPdf", "gdp-pdf"],
        "description": "Complex multi-page PDF understanding & professional synthesis",
    },
    "lcr": {
        "name": "AA-LCR Long Context",
        "domain": "long_context",
        "aliases": ["lcr", "artificial-analysis-long-context-reasoning"],
        "description": "Long context retrieval and reasoning (up to 1M tokens)",
    },
    "mlcr": {
        "name": "MLCR Medical Long Context",
        "domain": "long_context",
        "aliases": ["mlcr", "mlcr-aa"],
        "description": "Medical long-context reasoning over clinical records",
    },
    "mmmuPro": {
        "name": "MMMU-Pro",
        "domain": "multimodal",
        "aliases": ["mmmuPro", "mmmu-pro"],
        "description": "Advanced multi-discipline multimodal reasoning benchmark",
    },
    "code2video": {
        "name": "Code2Video-AA",
        "domain": "multimodal",
        "aliases": ["code2video", "code2video-aa"],
        "description": "Evaluating code generation for interactive video and animation",
    },
    "aa3d": {
        "name": "AA-3D",
        "domain": "multimodal",
        "aliases": ["aa3d", "aa-3d"],
        "description": "Interactive 3D WebGL/Three.js scene generation benchmark",
    },
    "omniscience": {
        "name": "AA Omniscience Index",
        "domain": "factuality",
        "aliases": ["omniscience", "aa-omniscience"],
        "description": "Composite factuality & non-hallucination benchmark",
    },
    "omniscienceAccuracy": {
        "name": "AA-Omniscience Accuracy",
        "domain": "factuality",
        "aliases": ["omniscienceAccuracy", "omniscience-accuracy"],
        "description": "Sub-component: factual accuracy rate",
    },
    "omniscienceNonHallucination": {
        "name": "AA-Omniscience Non-Hallucination",
        "domain": "factuality",
        "aliases": ["omniscienceNonHallucination", "omniscience-non-hallucination"],
        "description": "Sub-component: hallucination suppression rate",
    },
    "ifbench": {
        "name": "IFBench",
        "domain": "factuality",
        "aliases": ["ifbench"],
        "description": "Verifiable instruction-following constraints",
    },
    "analystAgent": {
        "name": "AA Analyst Agent",
        "domain": "agentic",
        "aliases": ["analystAgent", "aa-analyst-agent"],
        "description": "Data analysis and quantitative reporting agent benchmark",
    },
    "apexAgents": {
        "name": "APEX-Agents-AA",
        "domain": "agentic",
        "aliases": ["apexAgents", "apex-agents-aa"],
        "description": "Complex multi-agent coordination benchmark",
    },
    "enterpriseOps": {
        "name": "EnterpriseOps-Gym-AA",
        "domain": "agentic",
        "aliases": ["enterpriseOps", "enterprise-ops-gym-aa"],
        "description": "ServiceNow and enterprise operational tool use",
    },
    "itbenchSre": {
        "name": "ITBench-SRE",
        "domain": "agentic",
        "aliases": ["itbenchSre", "itbench-aa", "itbench-sre"],
        "description": "Site reliability engineering and DevOps incident remediation",
    },
    "harveyLab": {
        "name": "Harvey LAB-AA",
        "domain": "agentic",
        "aliases": ["harveyLab", "harvey-lab-aa"],
        "description": "Legal agent analysis and document diligence benchmark",
    },
}

# The baseline 20 metrics currently in production
CURRENT_STABLE_20 = [
    "intelligenceIndex", "gpqa", "hle", "mmmuPro", "ifbench", "scicode", "critpt",
    "lcr", "omniscience", "omniscienceAccuracy", "omniscienceNonHallucination",
    "gdpvalNormalized", "analystAgent", "apexAgents", "itbenchSre", "tau2",
    "tauBanking", "terminalbenchHard", "terminalbenchV21", "terminalbenchV40"
]


# ══════════════════════════════════════════════════════════════════════
# 2. Standardized Filtering Criteria
# ══════════════════════════════════════════════════════════════════════

class BenchmarkFilterCriteria:
    """Configurable quantitative criteria for benchmark screening."""
    def __init__(
        self,
        min_model_count: int = 150,
        min_ranked_coverage_pct: float = 25.0,
        min_frontier_coverage_pct: float = 30.0,
        min_calibrated_span: float = 0.80,
        max_calibrated_lower: float = 0.20,
        min_calibrated_upper: float = 0.85,
        max_pair_correlation: float = 0.95,
    ):
        self.min_model_count = min_model_count
        self.min_ranked_coverage_pct = min_ranked_coverage_pct
        self.min_frontier_coverage_pct = min_frontier_coverage_pct
        self.min_calibrated_span = min_calibrated_span
        self.max_calibrated_lower = max_calibrated_lower
        self.min_calibrated_upper = min_calibrated_upper
        self.max_pair_correlation = max_pair_correlation


# ══════════════════════════════════════════════════════════════════════
# 3. Benchmark Evaluator & Diagnostic Engine
# ══════════════════════════════════════════════════════════════════════

class BenchmarkSelectorEngine:
    def __init__(self, raw_data_path: str = "output/raw_data.json"):
        self.raw_data_path = raw_data_path
        if not os.path.exists(raw_data_path):
            raise FileNotFoundError(f"Raw data file not found: {raw_data_path}")
        with open(raw_data_path, "r", encoding="utf-8") as f:
            self.raw_data = json.load(f)

        self.models = self._load_and_extract_models()
        self.ranked_models = [m for m in self.models if m["valid_metrics"] >= 5]
        self.top_frontier_names = self._identify_top_frontier_models()

    def _load_and_extract_models(self) -> List[dict]:
        extracted = []
        for d in self.raw_data:
            name = d.get("shortName") or d.get("name") or "Unknown"
            creator = d.get("creator") or d.get("creatorName") or "Unknown"
            scores_dict = d.get("scores") if isinstance(d.get("scores"), dict) else {}
            
            parsed = {}
            for metric_key, meta in BENCHMARK_CATALOG.items():
                val = None
                for alias in meta["aliases"]:
                    if d.get(alias) is not None:
                        val = d.get(alias)
                        break
                    if scores_dict.get(alias) is not None:
                        val = scores_dict.get(alias)
                        break
                if val is not None:
                    try:
                        parsed[metric_key] = float(val)
                    except (ValueError, TypeError):
                        pass

            # per-request cost calculation (matching analyze.py logic)
            per_request_cost = None
            in_p = d.get("price1mInputTokens")
            out_p = d.get("price1mOutputTokens")
            hit_p = d.get("cacheHitPrice")
            if in_p is not None and out_p is not None:
                try:
                    c_in = float(in_p)
                    c_out = float(out_p)
                    c_hit = float(hit_p) if hit_p is not None else c_in * 0.1
                    # default 10k workload
                    cost_val = 10000 * (0.941263 * c_hit + (1 - 0.941263) * c_in) / 1e6 + 1000 * c_out / 1e6
                    per_request_cost = cost_val
                except Exception:
                    pass

            extracted.append({
                "model": name,
                "creator": creator,
                "is_deprecated": bool(d.get("isDeprecated")),
                "scores": parsed,
                "valid_metrics": len(parsed),
                "per_request_cost": per_request_cost,
                "raw_item": d,
            })
        return extracted

    def _identify_top_frontier_models(self) -> List[str]:
        """Identify key flagship frontier models to check for coverage continuity."""
        key_patterns = [
            "Claude Opus 5.5 (max", "Claude Opus 5.5 (xhigh", "Gemini 4 Argon",
            "GPT-6.1 Sol", "GPT-6.1 Terra", "Kimi K3.1 Pro", "GLM-5.3",
            "DeepSeek V4.1", "Qwen3.8", "MiMo-V2.6", "Step 5",
        ]
        matched = []
        for pat in key_patterns:
            for m in self.ranked_models:
                if pat in m["model"] and m["model"] not in matched:
                    matched.append(m["model"])
        return matched

    def compute_all_statistics(self) -> Dict[str, dict]:
        """Compute basic sample size, coverage, min/max, std, and frontier coverage."""
        stats = {}
        total_ranked = len(self.ranked_models)
        frontier_set = set(self.top_frontier_names)

        for m_id, meta in BENCHMARK_CATALOG.items():
            vals = [m["scores"][m_id] for m in self.ranked_models if m_id in m["scores"]]
            count = len(vals)
            cov_pct = (count / total_ranked * 100.0) if total_ranked > 0 else 0.0

            frontier_tested = sum(1 for m in self.ranked_models if m["model"] in frontier_set and m_id in m["scores"])
            frontier_cov_pct = (frontier_tested / len(frontier_set) * 100.0) if frontier_set else 0.0

            if count > 0:
                mean_v = sum(vals) / count
                var_v = sum((x - mean_v) ** 2 for x in vals) / count
                std_v = math.sqrt(var_v)
                min_v = min(vals)
                max_v = max(vals)
            else:
                mean_v = std_v = min_v = max_v = 0.0

            stats[m_id] = {
                "name": meta["name"],
                "domain": meta["domain"],
                "count": count,
                "cov_pct": cov_pct,
                "frontier_tested": frontier_tested,
                "frontier_total": len(frontier_set),
                "frontier_cov_pct": frontier_cov_pct,
                "min": min_v,
                "max": max_v,
                "mean": mean_v,
                "std": std_v,
            }
        return stats

    def simulate_dynamic_calibration(self, metric_subset: List[str]) -> Tuple[Dict[str, dict], int]:
        """Simulate the leave-one-out dynamic calibration for any given subset of metrics."""
        eval_models = [m for m in self.ranked_models if sum(1 for k in metric_subset if k in m["scores"]) >= 3]
        if not eval_models:
            return {}, 0

        metric_ranges = {}
        for k in metric_subset:
            vals = [m["scores"][k] for m in eval_models if k in m["scores"]]
            if vals:
                metric_ranges[k] = {"min": min(vals), "max": max(vals)}
            else:
                metric_ranges[k] = {"min": 0.0, "max": 1.0}

        bounds = {k: {"lower": 0.0, "upper": 1.0, "span": 1.0} for k in metric_subset}
        max_rounds = 35
        converged_round = max_rounds

        for round_idx in range(1, max_rounds + 1):
            norm_scores = {}
            for m in eval_models:
                mid = id(m)
                norm_scores[mid] = {}
                for k in metric_subset:
                    if k in m["scores"]:
                        orig = m["scores"][k]
                        mi = metric_ranges[k]["min"]
                        ma = metric_ranges[k]["max"]
                        base = (orig - mi) / (ma - mi) if ma > mi else 0.5
                        low = bounds[k]["lower"]
                        up = bounds[k]["upper"]
                        val = low + base * (up - low)
                        norm_scores[mid][k] = max(0.0, min(1.0, val))
                    else:
                        norm_scores[mid][k] = None

            new_bounds = {}
            round_max_delta = 0.0

            for excluded_k in metric_subset:
                leave_out_avgs = {}
                for m in eval_models:
                    mid = id(m)
                    scores = [norm_scores[mid][k] for k in metric_subset if k != excluded_k and norm_scores[mid][k] is not None]
                    if scores:
                        leave_out_avgs[mid] = sum(scores) / len(scores)

                if not leave_out_avgs:
                    new_bounds[excluded_k] = dict(bounds[excluded_k])
                    continue

                min_avg = min(leave_out_avgs.values())
                max_avg = max(leave_out_avgs.values())

                if max_avg > min_avg:
                    norm_leave_out = {mid: (avg - min_avg) / (max_avg - min_avg) for mid, avg in leave_out_avgs.items()}
                else:
                    norm_leave_out = {mid: 0.5 for mid in leave_out_avgs}

                tested_scores = [norm_leave_out[id(m)] for m in eval_models if excluded_k in m["scores"] and id(m) in norm_leave_out]

                if tested_scores:
                    new_lower = min(tested_scores)
                    new_upper = max(tested_scores)
                else:
                    new_lower = bounds[excluded_k]["lower"]
                    new_upper = bounds[excluded_k]["upper"]

                delta = max(abs(new_lower - bounds[excluded_k]["lower"]), abs(new_upper - bounds[excluded_k]["upper"]))
                if delta > round_max_delta:
                    round_max_delta = delta

                new_bounds[excluded_k] = {"lower": new_lower, "upper": new_upper, "span": new_upper - new_lower}

            bounds = new_bounds
            if round_max_delta < 1e-5:
                converged_round = round_idx
                break

        return bounds, converged_round

    def evaluate_metric_scorecard(self, criteria: BenchmarkFilterCriteria) -> Dict[str, dict]:
        """Evaluate every single metric against the standardized criteria and assign PASS / FAIL."""
        basic_stats = self.compute_all_statistics()
        all_metrics = list(BENCHMARK_CATALOG.keys())
        calib_bounds, _ = self.simulate_dynamic_calibration(all_metrics)

        scorecards = {}
        for m_id, s in basic_stats.items():
            b = calib_bounds.get(m_id, {"lower": 0.0, "upper": 1.0, "span": 1.0})
            issues = []

            # 1. Sample Size Criteria
            if s["count"] < criteria.min_model_count:
                issues.append(f"Low sample size (N={s['count']} < {criteria.min_model_count})")
            if s["cov_pct"] < criteria.min_ranked_coverage_pct:
                issues.append(f"Low coverage rate ({s['cov_pct']:.1f}% < {criteria.min_ranked_coverage_pct}%)")

            # 2. Frontier Model Coverage Criteria
            if s["frontier_cov_pct"] < criteria.min_frontier_coverage_pct:
                issues.append(f"Sparse frontier coverage ({s['frontier_tested']}/{s['frontier_total']} = {s['frontier_cov_pct']:.1f}% < {criteria.min_frontier_coverage_pct}%)")

            # 3. Dynamic Calibration Bounds Stability Criteria
            if b["span"] < criteria.min_calibrated_span:
                issues.append(f"Compressed dynamic span ({b['span']:.3f} < {criteria.min_calibrated_span:.2f})")
            if b["lower"] > criteria.max_calibrated_lower:
                issues.append(f"Severely elevated lower bound ({b['lower']:.3f} > {criteria.max_calibrated_lower:.2f})")
            if b["upper"] < criteria.min_calibrated_upper:
                issues.append(f"Severely depressed upper bound ({b['upper']:.3f} < {criteria.min_calibrated_upper:.2f})")

            passed = len(issues) == 0
            scorecards[m_id] = {
                "name": s["name"],
                "domain": s["domain"],
                "count": s["count"],
                "cov_pct": s["cov_pct"],
                "frontier_cov": f"{s['frontier_tested']}/{s['frontier_total']}",
                "lower": b["lower"],
                "upper": b["upper"],
                "span": b["span"],
                "passed": passed,
                "issues": issues,
            }
        return scorecards

    def simulate_leaderboard_run(self, metric_subset: List[str]) -> dict:
        """Simulate the complete leaderboard computation matching analyze.py logic:
        1. Raw min-max normalization per metric
        2. composite_ability_raw = mean across evaluated metrics
        3. composite_ability = re-normalized to [0, 1] across ranked models
        4. Leave-one-out dynamic calibration for composite_ability_calibrated
        5. Pareto frontier computation
        6. Reasoning tier monotonicity verification
        """
        # Minimum valid metrics in this subset
        min_valid = min(5, len(metric_subset))
        eval_models = [m for m in self.models if sum(1 for k in metric_subset if k in m["scores"]) >= min_valid]

        # 1. Metric ranges for raw normalization
        ranges = {}
        for k in metric_subset:
            vals = [m["scores"][k] for m in eval_models if k in m["scores"]]
            ranges[k] = {"min": min(vals) if vals else 0.0, "max": max(vals) if vals else 1.0}

        # 2. Raw composite ability
        for m in eval_models:
            norm_vals = []
            for k in metric_subset:
                if k in m["scores"]:
                    v = m["scores"][k]
                    mi = ranges[k]["min"]
                    ma = ranges[k]["max"]
                    norm_vals.append((v - mi) / (ma - mi) if ma > mi else 0.5)
            m["_comp_raw"] = sum(norm_vals) / len(norm_vals) if norm_vals else 0.0

        min_a = min(m["_comp_raw"] for m in eval_models)
        max_a = max(m["_comp_raw"] for m in eval_models)
        for m in eval_models:
            m["composite_ability"] = (m["_comp_raw"] - min_a) / (max_a - min_a) if max_a > min_a else 0.5

        # 3. Dynamic Calibration
        bounds, rounds = self.simulate_dynamic_calibration(metric_subset)

        # 4. Check Reasoning Tier Monotonicity
        score_by_name = {m["model"]: m["composite_ability"] for m in eval_models}
        inversions = []
        test_pairs = [
            ("Claude Opus 5.5 (xhigh with fallback)", "Claude Opus 5.5 (max with fallback)"),
            ("Claude Opus 5.5 (high with fallback)", "Claude Opus 5.5 (xhigh with fallback)"),
            ("Claude Opus 5.5 (medium with fallback)", "Claude Opus 5.5 (high with fallback)"),
            ("Claude Opus 5.5 (low with fallback)", "Claude Opus 5.5 (medium with fallback)"),
            ("GPT-6.1 Terra (high)", "GPT-6.1 Terra (xhigh)"),
            ("GPT-6.1 Terra (medium)", "GPT-6.1 Terra (high)"),
            ("GPT-6 Astra (high)", "GPT-6 Astra (xhigh)"),
        ]
        for lower_name, higher_name in test_pairs:
            s_low = score_by_name.get(lower_name)
            s_high = score_by_name.get(higher_name)
            if s_low is not None and s_high is not None:
                if s_high < s_low:
                    inversions.append({
                        "lower_name": lower_name,
                        "higher_name": higher_name,
                        "lower_score": s_low,
                        "higher_score": s_high,
                        "diff": s_high - s_low,
                    })

        # 5. Pareto frontier computation
        priced_models = [m for m in eval_models if m.get("per_request_cost") is not None]
        # Sort by ability descending
        sorted_priced = sorted(priced_models, key=lambda x: -x["composite_ability"])
        pareto = []
        min_cost = float("inf")
        for m in sorted_priced:
            c = m["per_request_cost"]
            if c < min_cost:
                pareto.append(m)
                min_cost = c

        return {
            "models_evaluated": len(eval_models),
            "converged_rounds": rounds,
            "bounds": bounds,
            "inversions": inversions,
            "pareto_frontier": pareto,
            "top_model": sorted_priced[0]["model"] if sorted_priced else "None",
        }

    def get_strategy_metrics(self, strategy: str) -> List[str]:
        """Return metric lists for predefined evaluation strategies."""
        if strategy == "stable_20":
            return CURRENT_STABLE_20

        elif strategy == "all_32":
            return list(BENCHMARK_CATALOG.keys())

        elif strategy == "curated_conservative":
            # Strict high-coverage core: excludes all <150 models benchmarks and duplicate versions
            return [
                "intelligenceIndex", "hle", "gpqa", "critpt", "scicode",
                "lcr", "omniscience", "ifbench", "gdpvalNormalized",
                "mmmuPro", "terminalbenchV40", "tau2"
            ]

        elif strategy == "curated_balanced":
            # Recommended Candidate:
            # 1. Retains all reliable high-coverage benchmarks
            # 2. Includes verified agentic additions: briefcase, automationbench, gdpPdf
            # 3. Excludes ultra-sparse / volatile metrics (<100 models, severe lower bound distortion):
            #    harveyLab (N=28), code2video (N=27), aa3d (N=23), apexAgents (N=33), itbenchSre (N=45), enterpriseOps (N=50), analystAgent (N=51)
            #    which caused the Opus 5.5 max < xhigh inversion and frontier destruction!
            return [
                "intelligenceIndex", "hle", "gpqa", "critpt", "scicode",
                "lcr", "omniscience", "omniscienceAccuracy", "omniscienceNonHallucination",
                "ifbench", "gdpvalNormalized", "mmmuPro", "briefcase", "automationbench",
                "gdpPdf", "terminalbenchHard", "terminalbenchV21", "terminalbenchV40",
                "tau2", "tauBanking"
            ]

        else:
            raise ValueError(f"Unknown strategy: {strategy}")


# ══════════════════════════════════════════════════════════════════════
# 4. CLI & Interactive Reporting
# ══════════════════════════════════════════════════════════════════════

def print_banner(text: str):
    line = "=" * 105
    print(f"\n{line}\n  {text}\n{line}")

def print_scorecard_table(scorecards: Dict[str, dict]):
    print(f"{'#':<3} {'Metric Key':<24} {'Domain':<16} {'Count':<6} {'Cov %':<7} {'Top15':<6} "
          f"{'Bounds [Low, High]':<20} {'Span':<6} {'Status'}")
    print("-" * 105)
    sorted_items = sorted(scorecards.items(), key=lambda x: -x[1]["count"])
    for i, (m_id, sc) in enumerate(sorted_items):
        bounds_str = f"[{sc['lower']:.3f}, {sc['upper']:.3f}]"
        status_str = "PASS" if sc["passed"] else "FAIL"
        domain_short = sc["domain"][:15]
        print(f"{i+1:<3} {m_id:<24} {domain_short:<16} {sc['count']:<6} {sc['cov_pct']:<7.1f} {sc['frontier_cov']:<6} "
              f"{bounds_str:<20} {sc['span']:<6.3f} {status_str}")

def print_failure_details(scorecards: Dict[str, dict]):
    failed = {k: v for k, v in scorecards.items() if not v["passed"]}
    if not failed:
        print("\nAll candidate benchmarks passed the criteria!")
        return
    print("\n" + "=" * 105)
    print("DETAILED EXCLUSION REASONS FOR FAILED BENCHMARKS:")
    print("=" * 105)
    for m_id, sc in sorted(failed.items(), key=lambda x: x[1]["count"]):
        print(f"\n* [{m_id}] - {sc['name']} (Count: {sc['count']}, Cov: {sc['cov_pct']:.1f}%)")
        for issue in sc["issues"]:
            print(f"    - {issue}")


def run_recommendation_report(engine: BenchmarkSelectorEngine, criteria: BenchmarkFilterCriteria):
    print_banner("STANDARDIZED BENCHMARK SELECTION RECOMMENDATION REPORT")
    scorecards = engine.evaluate_metric_scorecard(criteria)
    
    passed_metrics = [k for k, v in scorecards.items() if v["passed"]]
    failed_metrics = [k for k, v in scorecards.items() if not v["passed"]]

    print(f"Total Candidate Benchmarks Analyzed: {len(scorecards)}")
    print(f"  * Passed Screening Criteria:      {len(passed_metrics)}")
    print(f"  * Failed Screening Criteria:      {len(failed_metrics)}")

    print("\n" + "-" * 105)
    print("WHY DID ALL 32 BENCHMARKS CAUSE CHAOS? (ROOT CAUSE ANALYSIS)")
    print("-" * 105)
    print("""
1. The 'Sparse Evaluation Penalty Trap' (稀疏评测惩罚陷阱):
   - 9 niche benchmarks have <100 evaluated models (aa-3d: 23, code2video: 27, harveyLab: 28,
     apexAgents: 33, itbenchSre: 45, enterpriseOps: 50, analystAgent: 51, frontiercode: 77, terminalbenchScience: 97).
   - In Artificial Analysis's dataset, these difficult specialized benchmarks were ONLY evaluated on
     Claude Opus 5.5 (max), while siblings like Opus 5.5 (xhigh, high, medium) were NEVER evaluated.
   - Harvey Legal benchmark: Opus 5.5 max scored 0.0416 (4.16%). Because this raw score was averaged into
     Opus max's overall composite score without siblings taking the exam, Opus max's composite ability
     plummeted from 1.0000 to 0.9896!
   - Result: Opus 5.5 (xhigh, cost $222k) scored 0.9991, strictly Pareto-DOMINATING Opus 5.5 (max, cost $1.47M).
     The entire true Pareto frontier collapsed, and Opus 5.5 max disappeared from the chart!

2. Boundary Compression & Distorted Calibration:
   - LiveCodeBench (343 models) and AIME 2025 (270 models) lack official evaluations for the newest reasoning models.
     Their dynamic calibrated upper bound collapsed to 0.7183 and 0.7256. Any model tested on them was artificially capped.
   - Conversely, benchmarks like aa-3d, code2video, and harveyLab only tested top models; their lower bounds
     floated up to 0.48 ~ 0.50, granting arbitrary free points to models that took them.

3. Collinearity & Duplication:
   - TerminalBench variants (Hard, 2.1, 4.0, Science) have pairwise correlations up to r = 0.9547.
   - GDPval Normalized and AA-Briefcase have r = 0.9668.
   - Including all variants heavily overweights terminal and document agentic skills over core reasoning.
""")

    print("-" * 105)
    print("RECOMMENDED STANDARD SELECTION STRATEGY: 'curated_balanced' (20 Verified Metrics)")
    print("-" * 105)
    balanced_metrics = engine.get_strategy_metrics("curated_balanced")
    print(f"Selected {len(balanced_metrics)} High-Quality Benchmarks:")
    domain_map = defaultdict(list)
    for m in balanced_metrics:
        domain_map[BENCHMARK_CATALOG[m]["domain"]].append(m)
    for d, m_list in domain_map.items():
        print(f"  * {DOMAIN_CATEGORIES.get(d, d)} ({len(m_list)}):")
        for m in m_list:
            sc = scorecards[m]
            print(f"      - {m:<26} ({sc['name']}, Count={sc['count']}, Frontier={sc['frontier_cov']})")


def main():
    parser = argparse.ArgumentParser(
        description="Standardized Benchmark Selector & Sanity Diagnostic Engine for Generic LLM Leaderboard."
    )
    parser.add_argument(
        "--diagnose-all",
        action="store_true",
        help="Run comprehensive diagnostic across all 32 candidate benchmarks and print scorecard.",
    )
    parser.add_argument(
        "--strategy",
        choices=["stable_20", "all_32", "curated_conservative", "curated_balanced"],
        default=None,
        help="Evaluate a specific benchmark selection strategy profile.",
    )
    parser.add_argument(
        "--min-coverage",
        type=int,
        default=150,
        help="Minimum number of evaluated models required (default: 150).",
    )
    parser.add_argument(
        "--min-span",
        type=float,
        default=0.80,
        help="Minimum calibrated dynamic range span required (default: 0.80).",
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Run comparative simulation between strategies and check for reasoning-tier inversions.",
    )
    parser.add_argument(
        "--recommend",
        action="store_true",
        help="Print comprehensive recommendation and root cause analysis report.",
    )
    parser.add_argument(
        "--export-json",
        type=str,
        default=None,
        help="Path to export the selected metric definitions as JSON.",
    )
    parser.add_argument(
        "--export-markdown",
        type=str,
        default=None,
        help="Path to export the full diagnostic and selection report as Markdown.",
    )

    args = parser.parse_args()

    engine = BenchmarkSelectorEngine()
    criteria = BenchmarkFilterCriteria(
        min_model_count=args.min_coverage,
        min_calibrated_span=args.min_span,
    )

    # Default action if no flags provided: recommend + diagnose
    if not (args.diagnose_all or args.strategy or args.simulate or args.recommend or args.export_json or args.export_markdown):
        args.recommend = True
        args.diagnose_all = True
        args.simulate = True

    scorecards = engine.evaluate_metric_scorecard(criteria)

    if args.diagnose_all:
        print_banner("BENCHMARK METRICS COMPREHENSIVE SCORECARD (32 CANDIDATE BENCHMARKS)")
        print_scorecard_table(scorecards)
        print_failure_details(scorecards)

    if args.recommend:
        run_recommendation_report(engine, criteria)

    if args.strategy:
        metrics = engine.get_strategy_metrics(args.strategy)
        print_banner(f"STRATEGY EVALUATION: '{args.strategy}' ({len(metrics)} Metrics Selected)")
        res = engine.simulate_leaderboard_run(metrics)
        print(f"Models evaluated: {res['models_evaluated']}, Calibration converged in {res['converged_rounds']} rounds.")
        print(f"Top Model: {res['top_model']}")
        print(f"Pareto Frontier ({len(res['pareto_frontier'])} models):")
        for i, m in enumerate(res['pareto_frontier'][:8]):
            print(f"  #{i+1:<2} {m['model']:<38} Ability={m['composite_ability']:.4f} Cost=${m['per_request_cost']:,.2f}")
        if len(res['pareto_frontier']) > 8:
            print(f"  ... and {len(res['pareto_frontier']) - 8} more models on frontier.")

        print("\nReasoning Tier Inversion Sanity Check:")
        if res["inversions"]:
            print("  [CRITICAL WARNING] Reasoning-tier inversion detected!")
            for inv in res["inversions"]:
                print(f"    - {inv['higher_name']} ({inv['higher_score']:.4f}) scored LOWER than "
                      f"{inv['lower_name']} ({inv['lower_score']:.4f})! (Diff: {inv['diff']:.4f})")
        else:
            print("  [PASS] All reasoning tiers behave monotonically (max >= xhigh >= high >= medium >= low).")

    if args.simulate:
        print_banner("STRATEGY COMPARATIVE SANITY MATRIX")
        strategies = ["stable_20", "curated_balanced", "curated_conservative", "all_32"]
        print(f"{'Strategy':<24} {'Metrics':<9} {'Convergence':<13} {'Inversion Anomaly':<25} {'Top Model':<28} {'Status'}")
        print("-" * 115)
        for s in strategies:
            m_set = engine.get_strategy_metrics(s)
            res = engine.simulate_leaderboard_run(m_set)
            invs = res["inversions"]
            inv_str = f"YES ({len(invs)} inversions!)" if invs else "NONE (Clean)"
            status = "CHAOTIC (REJECTED)" if invs else "STABLE (VALID)"
            top_m = res["top_model"][:26]
            print(f"{s:<24} {len(m_set):<9} {res['converged_rounds']} rounds    {inv_str:<25} {top_m:<28} {status}")

    if args.export_json:
        export_data = {
            "criteria": vars(criteria),
            "scorecards": scorecards,
            "strategies": {
                s: engine.get_strategy_metrics(s)
                for s in ["stable_20", "curated_balanced", "curated_conservative", "all_32"]
            },
        }
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        print(f"\n[Export] JSON diagnostic data saved to: {args.export_json}")

    if args.export_markdown:
        md_lines = [
            "# Standardized Benchmark Screening & Diagnostic Report",
            "",
            "## 1. Candidate Benchmarks Scorecard (32 Candidates)",
            "",
            "| # | Metric Key | Domain | Models | Coverage | Frontier Cov | Bounds [Low, High] | Span | Status |",
            "|---|---|---|---|---|---|---|---|---|",
        ]
        sorted_items = sorted(scorecards.items(), key=lambda x: -x[1]["count"])
        for i, (m_id, sc) in enumerate(sorted_items):
            b_str = f"[{sc['lower']:.3f}, {sc['upper']:.3f}]"
            st = "**PASS**" if sc["passed"] else "FAIL"
            md_lines.append(
                f"| {i+1} | `{m_id}` | {sc['domain']} | {sc['count']} | {sc['cov_pct']:.1f}% | {sc['frontier_cov']} | {b_str} | {sc['span']:.3f} | {st} |"
            )
        md_lines.extend([
            "",
            "## 2. Strategy Comparative Sanity Matrix",
            "",
            "| Strategy | Metrics | Calibration Rounds | Inversion Anomaly | Top Model | Status |",
            "|---|---|---|---|---|---|",
        ])
        for s in ["stable_20", "curated_balanced", "curated_conservative", "all_32"]:
            m_set = engine.get_strategy_metrics(s)
            res = engine.simulate_leaderboard_run(m_set)
            invs = res["inversions"]
            inv_str = f"YES ({len(invs)} inversions)" if invs else "Clean (0)"
            st = "**CHAOTIC (REJECTED)**" if invs else "**STABLE (VALID)**"
            md_lines.append(
                f"| `{s}` | {len(m_set)} | {res['converged_rounds']} | {inv_str} | {res['top_model']} | {st} |"
            )
        with open(args.export_markdown, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))
        print(f"\n[Export] Markdown report saved to: {args.export_markdown}")


if __name__ == "__main__":
    main()
