#!/usr/bin/env python3
"""
Scoring system and Pareto analysis for Artificial Analysis LLM Leaderboard.

**Version 9**: X-axis = Model Parameter Count (totalParameters from AA).

Key change from v8: Instead of cost, we use AA's reported model parameter count
as the X-axis. This lets us analyze which models achieve the best intelligence
per parameter — a measure of training efficiency.

The X-axis represents totalParameters (in billions), the total number of
parameters in the model as reported by the model provider via AA.

Data source: AA's Next.js RSC payload (500 models × 88 fields)
"""

import json
import os
import sys
from collections import Counter
from fractions import Fraction

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ══════════════════════════════════════════════════════════════════════
# Font setup
# ══════════════════════════════════════════════════════════════════════
_HEITI_FONTS = [
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Bold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-SemiBold.ttf",
    "/usr/share/fonts/truetype/chinese/SarasaMonoSC-Regular.ttf",
]
_LATIN = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
for fp in _HEITI_FONTS:
    if os.path.exists(fp):
        fm.fontManager.addfont(fp)
        break
for fp in _LATIN:
    if os.path.exists(fp):
        fm.fontManager.addfont(fp)
        break
plt.rcParams["font.sans-serif"] = ["Sarasa Mono SC", "Noto Serif SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# ── Paths ──
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
RAW_DATA_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")

# ── Metrics (from AA's evaluation data) ──
# Maps our internal key → AA's field name in the RSC payload
METRIC_FIELDS = {
    "intelligenceIndex": "intelligenceIndex",
    "agenticIndex": "agenticIndex",
    "codingIndex": "codingIndex",
    "gpqa": "gpqa",
    "hle": "hle",
    "mmmuPro": "mmmuPro",
    "ifbench": "ifbench",
    "scicode": "scicode",
    "critpt": "critpt",
    "lcr": "lcr",
    "tau2": "tau2",
    "terminalbenchHard": "terminalbenchHard",
    "omniscience": "omniscience",
    "omniscienceAccuracy": "omniscienceAccuracy",
    "omniscienceNonHallucination": "omniscienceNonHallucination",
    "apexAgents": "apexAgents",
    "itbenchSre": "itbenchSre",
    "gdpvalNormalized": "gdpvalNormalized",
}

METRIC_LABELS = {
    "intelligenceIndex": "AA Intelligence Index",
    "agenticIndex": "AA Agentic Index",
    "codingIndex": "AA Coding Index",
    "gpqa": "GPQA Diamond",
    "hle": "Humanity's Last Exam",
    "mmmuPro": "MMMU Pro",
    "ifbench": "IFBench Instruction Following",
    "scicode": "SciCode Coding",
    "critpt": "CritPt Physics",
    "lcr": "AA-LCR Long Context",
    "tau2": "τ²-Bench Telecom",
    "terminalbenchHard": "Terminal-Bench Hard",
    "omniscience": "AA Omniscience Index",
    "omniscienceAccuracy": "AA-Omniscience Accuracy",
    "omniscienceNonHallucination": "AA-Omniscience Non-Hallucination",
    "apexAgents": "APEX-Agents-AA",
    "itbenchSre": "ITBench-SRE",
    "gdpvalNormalized": "GDPval-AA Normalized",
}

MIN_VALID_METRICS = 5


# ══════════════════════════════════════════════════════════════════════
# Data Loading & Computation
# ══════════════════════════════════════════════════════════════════════

def load_data():
    with open(RAW_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def compute_scores(data):
    """Compute composite ability and extract parameter count."""
    models = []
    for d in data:
        # Skip deprecated models
        if d.get("deprecated", False):
            continue

        m = {
            "model": d.get("name", "Unknown"),
            "slug": d.get("slug", ""),
            "is_reasoning": bool(d.get("reasoningModel", False)),
            "creator": d.get("modelCreatorName", ""),
            "context_window": d.get("contextWindowTokens"),
            "is_open_weights": d.get("isOpenWeights", False),
            # Parameter counts (from AA)
            "total_parameters": _to_frac(d.get("totalParameters")),
            "active_parameters": _to_frac(d.get("activeParameters")),
            "size_class": d.get("sizeClass"),
            # Pricing (direct from AA)
            "input_price": _to_frac(d.get("price1mInputTokens")),
            "output_price": _to_frac(d.get("price1mOutputTokens")),
            "cache_hit_price": _to_frac(d.get("cacheHitPrice")),
            "blended_price_721": _to_frac(d.get("price1mBlended7To2To1")),
            # AA's measured Intelligence Index cost
            "intelligence_index_cost_total": _to_frac(d.get("intelligenceIndexCostTotal")),
            "intelligence_index_cost_input": _to_frac(d.get("intelligenceIndexCostInput")),
            "intelligence_index_cost_output": _to_frac(d.get("intelligenceIndexCostOutput")),
            "intelligence_index_cost_reasoning": _to_frac(d.get("intelligenceIndexCostReasoning")),
            "intelligence_index_cost_answer": _to_frac(d.get("intelligenceIndexCostAnswer")),
            # Speed data
            "speed": _to_frac(d.get("medianOutputTokensPerSecond")),
            "ttft": _to_frac(d.get("medianTimeToFirstTokenSeconds")),
            "total_response": _to_frac(d.get("medianEndToEndResponseTimeSeconds")),
            "reasoning_time": _to_frac(d.get("medianReasoningTimeSeconds")),
            # Intelligence Index
            "intelligence_index": _to_frac(d.get("intelligenceIndex")),
            # Token counts
            "token_counts": d.get("intelligenceIndexTokenCounts"),
            "_parsed": {},
        }

        # Parse evaluation metrics
        for key, aa_field in METRIC_FIELDS.items():
            val = d.get(aa_field)
            m["_parsed"][key] = _to_frac(val)

        models.append(m)

    print(f"Models loaded (excluding deprecated): {len(models)}")
    print(f"  Reasoning models: {sum(1 for m in models if m['is_reasoning'])}")
    print(f"  Non-reasoning models: {sum(1 for m in models if not m['is_reasoning'])}")
    print(f"  With total_parameters: {sum(1 for m in models if m['total_parameters'] is not None)}")
    print(f"  With active_parameters: {sum(1 for m in models if m['active_parameters'] is not None)}")

    # ── Metric ranges (Fraction) ──
    metric_ranges = {}
    for key in METRIC_FIELDS:
        vals = [m["_parsed"][key] for m in models if m["_parsed"][key] is not None]
        if len(vals) >= 2:
            metric_ranges[key] = {"min": min(vals), "max": max(vals), "count": len(vals)}
        else:
            metric_ranges[key] = None

    # ── Normalize metrics ──
    for m in models:
        m["_norm"] = {}
        for key in METRIC_FIELDS:
            val = m["_parsed"][key]
            rng = metric_ranges.get(key)
            if val is None or rng is None:
                m["_norm"][key] = None
            elif rng["max"] == rng["min"]:
                m["_norm"][key] = Fraction(1, 2)
            else:
                m["_norm"][key] = (val - rng["min"]) / (rng["max"] - rng["min"])

    # ── Composite ability = exact Fraction mean ──
    for m in models:
        nv = [v for v in m["_norm"].values() if v is not None]
        m["composite_ability"] = sum(nv) / len(nv) if nv else None
        m["valid_metrics"] = len(nv)

    # Quality filter
    valid = [m for m in models
             if m["composite_ability"] is not None and m["valid_metrics"] >= MIN_VALID_METRICS]
    print(f"Models with ≥{MIN_VALID_METRICS} metrics: {len(valid)}")

    # ── Use totalParameters as the X-axis ──
    # totalParameters is in billions (e.g., 175 = 175B parameters)
    # For MoE models, totalParameters includes all expert parameters
    for m in valid:
        m["param_count"] = m["total_parameters"]

    # ── Normalize parameter count (linear, Pareto max = 1) ──
    paramed = [m for m in valid if m.get("param_count") is not None and m["param_count"] > 0]
    if paramed:
        # Compute a preliminary Pareto to find the max param on the frontier
        sorted_paramed = sorted(paramed, key=lambda m: (m["param_count"], -m["composite_ability"]))
        prelim_frontier = []
        for m in sorted_paramed:
            if any(_dominates(o, m) for o in prelim_frontier):
                continue
            prelim_frontier = [p for p in prelim_frontier if not _dominates(m, p)]
            prelim_frontier.append(m)

        # Max parameter count on the Pareto frontier is the normalization ceiling
        if prelim_frontier:
            max_pareto_param = max(m["param_count"] for m in prelim_frontier)
        else:
            max_pareto_param = max(m["param_count"] for m in paramed)

        print(f"Parameter count range: {float(min(m['param_count'] for m in paramed)):.1f}B – {float(max(m['param_count'] for m in paramed)):.1f}B")
        print(f"Max Pareto frontier params (normalization ceiling): {float(max_pareto_param):.1f}B")

        for m in paramed:
            if max_pareto_param > 0:
                m["normalized_param"] = m["param_count"] / max_pareto_param
            else:
                m["normalized_param"] = Fraction(1, 2)
    for m in valid:
        if "normalized_param" not in m:
            m["normalized_param"] = None

    return valid, metric_ranges


def _to_frac(val):
    """Convert a numeric value to Fraction, or None if null/invalid."""
    if val is None:
        return None
    try:
        return Fraction(val).limit_denominator(10**12)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


# ══════════════════════════════════════════════════════════════════════
# Plot Models Filter
# ══════════════════════════════════════════════════════════════════════

def get_plot_models(models):
    """Filter models that have valid normalized_param for plotting."""
    plot_models = [m for m in models if m.get("normalized_param") is not None]
    print(f"\n  {len(plot_models)} models with valid parameter data for plotting")
    return plot_models


# ══════════════════════════════════════════════════════════════════════
# Pareto frontier computation
# ══════════════════════════════════════════════════════════════════════

def compute_pareto(models):
    """Pareto frontier based on parameter count vs composite ability.
    
    A model is on the Pareto frontier if no other model has BOTH
    fewer parameters AND equal or higher composite ability.
    (We prefer models that achieve more with less.)
    """
    paramed = [m for m in models if m.get("param_count") is not None and m["param_count"] > 0]
    sorted_m = sorted(paramed, key=lambda m: (m["param_count"], -m["composite_ability"]))
    frontier = []
    for m in sorted_m:
        if any(_dominates(o, m) for o in frontier):
            continue
        frontier = [p for p in frontier if not _dominates(m, p)]
        frontier.append(m)
    frontier.sort(key=lambda m: m["composite_ability"], reverse=True)
    return frontier


def _dominates(a, b):
    """a dominates b if a has >= ability with <= parameters (and strictly better on one)."""
    return (a["composite_ability"] >= b["composite_ability"]
            and a["param_count"] <= b["param_count"]
            and (a["composite_ability"] > b["composite_ability"]
                 or a["param_count"] < b["param_count"]))


# ══════════════════════════════════════════════════════════════════════
# Visualization
# ══════════════════════════════════════════════════════════════════════

def plot_analysis(models, pareto):
    """Generate the Pareto scatter plot: Composite Ability vs Parameter Count."""
    try:
        from adjustText import adjust_text
        has_adj = True
    except ImportError:
        has_adj = False

    plot_models = [m for m in models if m.get("param_count") is not None]
    pareto_names = {m["model"] for m in pareto}
    others = [m for m in plot_models if m["model"] not in pareto_names]

    fig, ax = plt.subplots(figsize=(14, 14))
    fig.patch.set_facecolor("#000000")
    ax.set_facecolor("#000000")

    # Use log scale for parameter axis (ranges from <1B to >1000B)
    ax.set_xscale('log')

    # Grid
    ax.grid(True, which='major', color='#333333', alpha=0.5, linewidth=0.4, zorder=0)
    ax.grid(True, which='minor', color='#1A1A1A', alpha=0.3, linewidth=0.2, zorder=0)

    # Scatter: other models — color by size class
    size_colors = {
        "tiny": "#666666",
        "small": "#4A90D9",
        "medium": "#D4A017",
        "large": "#D94A4A",
    }
    for sc, color in size_colors.items():
        group = [m for m in others if m.get("size_class") == sc]
        if group:
            ax.scatter(
                [float(m["param_count"]) for m in group],
                [float(m["composite_ability"]) for m in group],
                c=color, s=25, alpha=0.5, zorder=2,
                label=f"{sc.capitalize()} ({len(group)})",
            )
    uncategorized = [m for m in others if m.get("size_class") not in size_colors]
    if uncategorized:
        ax.scatter(
            [float(m["param_count"]) for m in uncategorized],
            [float(m["composite_ability"]) for m in uncategorized],
            c="#4A4A4A", s=20, alpha=0.35, zorder=2,
            label=f"未知大小 ({len(uncategorized)})",
        )

    # Scatter: Pareto frontier
    ax.scatter(
        [float(m["param_count"]) for m in pareto],
        [float(m["composite_ability"]) for m in pareto],
        c="#00E5FF", s=100, alpha=0.95, zorder=4,
        edgecolors="#FFFFFF", linewidth=1.2,
        label=f"Pareto前沿 ({len(pareto)})",
    )

    # Pareto frontier line
    pf = sorted(pareto, key=lambda m: m["param_count"])
    ax.plot(
        [float(m["param_count"]) for m in pf],
        [float(m["composite_ability"]) for m in pf],
        c="#00E5FF", linewidth=2.0, alpha=0.35, zorder=3, linestyle="--",
    )

    # Pareto model labels
    texts = []
    for i, m in enumerate(pf):
        param_b = float(m["param_count"])
        if param_b >= 1000:
            param_str = f"{param_b/1000:.1f}T"
        elif param_b >= 1:
            param_str = f"{param_b:.0f}B"
        else:
            param_str = f"{param_b*1000:.0f}M"
        label = f"{i+1}. {m['model']} ({param_str})"
        t = ax.text(
            float(m["param_count"]),
            float(m["composite_ability"]),
            label,
            fontsize=8, ha="left", va="bottom",
            color="#FFFFFF", fontweight="bold", zorder=5,
            bbox=dict(boxstyle="round,pad=0.12",
                      facecolor="#1A1A1A", alpha=0.85,
                      edgecolor="#00E5FF", linewidth=0.5),
        )
        texts.append(t)

    if has_adj:
        adjust_text(texts,
                    arrowprops=dict(arrowstyle="->", color="#888888", lw=0.5),
                    expand_points=(1.8, 1.8),
                    force_text=(0.3, 0.5),
                    force_points=(0.1, 0.1),
                    lim=200)

    ax.set_xlabel("模型参数量 (B = 十亿参数, 对数刻度)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_ylabel("综合能力 (0=最低, 1=最高)",
                  fontsize=13, color="#FFFFFF", labelpad=10, fontweight="bold")
    ax.set_title(
        f"LLM 综合能力 vs 模型参数量 — Pareto前沿\n"
        f"（参数数据来自AA | 18项指标综合评分）",
        fontsize=15, color="#FFFFFF", fontweight="bold", pad=16,
    )

    # Custom x-axis ticks for parameter counts
    import matplotlib.ticker as ticker
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(
        lambda x, p: f"{x:.0f}B" if x >= 1 else f"{x*1000:.0f}M"
    ))

    # Set reasonable x-axis limits
    all_params = [float(m["param_count"]) for m in plot_models]
    if all_params:
        ax.set_xlim(min(all_params) * 0.5, max(all_params) * 2)

    for spine in ax.spines.values():
        spine.set_color('#444444')
    ax.tick_params(axis='both', colors='#FFFFFF', length=5, width=1.2)
    ax.tick_params(axis='x', which='minor', colors='#666666', length=3, width=0.5)

    legend = ax.legend(loc="lower right", fontsize=10.5,
                       framealpha=0.85, edgecolor="#FFFFFF",
                       facecolor="#1A1A1A", labelcolor="#FFFFFF")

    method = (
        f"X轴: 模型总参数量totalParameters (对数刻度) | Y轴: 综合能力(18指标均值)\n"
        f"★ 参数越小能力越高 → 训练效率越高 | 共{len(plot_models)}模型"
    )
    ax.text(0.98, 0.02, method, transform=ax.transAxes, fontsize=6,
            va="bottom", ha="right", color="#AAAAAA", style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#111111", alpha=0.85,
                      edgecolor="#444444", linewidth=0.5))

    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, "pareto_analysis.png")
    plt.savefig(out, dpi=200, bbox_inches="tight", facecolor="#000000")
    plt.close()
    print(f"Plot saved to {out}")


# ══════════════════════════════════════════════════════════════════════
# Helper: Fraction → JSON
# ══════════════════════════════════════════════════════════════════════

def _frac_to_json(v):
    if v is None:
        return None
    if isinstance(v, Fraction):
        return float(v)
    return v


# ══════════════════════════════════════════════════════════════════════
# Output: JSON + README
# ══════════════════════════════════════════════════════════════════════

def save_results(models, pareto, metric_ranges):
    output = {
        "metadata": {
            "source": "https://artificialanalysis.ai/leaderboards/models",
            "methodology": (
                "18 evaluation metrics normalized [0,1], averaged → composite ability; "
                "Pareto = non-dominated by parameter count; "
                "X-axis: totalParameters (log scale); "
                "Y-axis: composite ability (linear, direct average); "
                "Parameter count from AA's model metadata"
            ),
            "param_source": "totalParameters from AA RSC payload — total model parameters in billions",
            "total_models": len(models),
            "pareto_count": len(pareto),
        },
        "metric_ranges": {
            METRIC_LABELS[k]: {
                "min": float(v["min"]),
                "max": float(v["max"]),
                "count": v["count"],
            } if isinstance(v, dict) else v
            for k, v in metric_ranges.items()
        },
        "pareto_frontier": [_export_model(m, i + 1) for i, m in enumerate(pareto)],
        "all_models": [
            {
                "model": m["model"],
                "creator": m["creator"],
                "composite_ability": float(m["composite_ability"]),
                "normalized_param": _frac_to_json(m.get("normalized_param")),
                "total_parameters_B": _frac_to_json(m.get("param_count")),
                "active_parameters_B": _frac_to_json(m.get("active_parameters")),
                "size_class": m.get("size_class"),
                "is_reasoning": m["is_reasoning"],
                "is_open_weights": m["is_open_weights"],
                "is_pareto": m["model"] in {p["model"] for p in pareto},
            }
            for m in sorted(models, key=lambda x: x["composite_ability"], reverse=True)
        ],
    }

    json_path = os.path.join(OUTPUT_DIR, "analysis_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"JSON saved to {json_path}")

    generate_readme(pareto, models)


def _export_model(m, rank):
    return {
        "rank": rank,
        "model": m["model"],
        "creator": m["creator"],
        "is_reasoning": m["is_reasoning"],
        "is_open_weights": m["is_open_weights"],
        "composite_ability": float(m["composite_ability"]),
        "total_parameters_B": _frac_to_json(m.get("param_count")),
        "active_parameters_B": _frac_to_json(m.get("active_parameters")),
        "size_class": m.get("size_class"),
        "normalized_param": _frac_to_json(m.get("normalized_param")),
        "intelligence_index_cost_usd": _frac_to_json(m.get("intelligence_index_cost_total")),
        "input_price": _frac_to_json(m.get("input_price")),
        "output_price": _frac_to_json(m.get("output_price")),
        "speed": _frac_to_json(m["speed"]),
        "ttft": _frac_to_json(m["ttft"]),
        "total_response": _frac_to_json(m["total_response"]),
        "reasoning_time": _frac_to_json(m["reasoning_time"]),
        "valid_metrics": m["valid_metrics"],
    }


def generate_readme(pareto, models):
    lines = []
    lines.append("# LLM Leaderboard — 综合能力 vs 模型参数量\n")
    lines.append("![Pareto Analysis](output/pareto_analysis.png)\n")
    lines.append("## Pareto 前沿模型（综合能力从高到低）\n")
    lines.append("| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |")
    lines.append("|---|------|---------|---------|-----------|--------|------|------|")

    for i, m in enumerate(pareto):
        param = m.get("param_count")
        if param is not None:
            pb = float(param)
            param_str = f"{pb:.0f}B" if pb >= 1 else f"{pb*1000:.0f}M"
        else:
            param_str = "--"

        active = m.get("active_parameters")
        if active is not None:
            ab = float(active)
            active_str = f"{ab:.0f}B" if ab >= 1 else f"{ab*1000:.0f}M"
        else:
            active_str = "--"

        sc = m.get("size_class", "--") or "--"
        ow = "Y" if m.get("is_open_weights") else "N"
        reas = "Y" if m["is_reasoning"] else "N"
        lines.append(
            f"| {i+1} | {m['model']} | {float(m['composite_ability']):.4f} "
            f"| {param_str} | {active_str} | {sc} | {ow} | {reas} |"
        )

    lines.append("")
    lines.append("### 评分方法")
    lines.append("")
    lines.append("1. **18项评估指标**各自线性归一化到 [0,1]")
    lines.append("2. **综合能力值** = 所有有效归一化分数的算术平均")
    lines.append("3. **Pareto前沿** = 不被任何其他模型支配的模型（参数更少且能力更高）")
    lines.append("")
    lines.append("### 横轴说明")
    lines.append("")
    lines.append("**X轴 = 模型总参数量 (totalParameters)**")
    lines.append("")
    lines.append("参数数据来自 Artificial Analysis 的模型元数据 (`totalParameters`)，")
    lines.append("即模型的总参数量（单位：十亿/B）。对于 MoE 模型，总参数量包含所有专家参数。")
    lines.append("对数刻度展示，因为参数量跨越多个数量级（0.3B 到 1600B+）。")
    lines.append("")
    lines.append("Pareto 前沿上的模型代表了**最高训练效率**——用更少的参数实现更高的能力。")
    lines.append("")
    lines.append("### 数据来源")
    lines.append("")
    lines.append(f"**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  ")
    lines.append(f"**方法论**: [AA Methodology](https://artificialanalysis.ai/methodology)  ")
    lines.append(f"**模型总数**: {len(models)}  ")

    readme_path = os.path.join(BASE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"README saved to {readme_path}")


# ══════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(RAW_DATA_FILE):
        print(f"ERROR: {RAW_DATA_FILE} not found. Run scrape.py first.")
        sys.exit(1)

    print("Loading data...")
    data = load_data()
    print(f"  {len(data)} models loaded")

    print("\nComputing scores & parameters...")
    models, metric_ranges = compute_scores(data)

    with_param = [m for m in models if m.get("param_count") is not None and m["param_count"] > 0]
    if with_param:
        params = [m["param_count"] for m in with_param]
        print(f"  Models with param data: {len(with_param)}/{len(models)}")
        print(f"  Param range: {float(min(params)):.1f}B – {float(max(params)):.1f}B")

    print("\nComputing Pareto frontier...")
    pareto = compute_pareto(models)
    print(f"  Pareto frontier: {len(pareto)} models")

    print("\nGenerating visualization...")
    plot_models = get_plot_models(models)
    plot_analysis(plot_models, pareto)

    print("\nSaving results...")
    save_results(models, pareto, metric_ranges)

    # Print Pareto table
    print(f"\n{'='*120}")
    print(f"PARETO FRONTIER ({len(pareto)} models) — ranked by composite ability")
    print(f"{'='*120}")
    print(f"{'#':<3} {'Model':<36} {'Ability':>8} {'Params':>10} {'Active':>10} {'Size':>6} {'Open':>4} {'Reas':>4}")
    print(f"{'-'*3} {'-'*36} {'-'*8} {'-'*10} {'-'*10} {'-'*6} {'-'*4} {'-'*4}")
    for i, m in enumerate(pareto):
        param = m.get("param_count")
        if param is not None:
            pb = float(param)
            p_str = f"{pb:.0f}B" if pb >= 1 else f"{pb*1000:.0f}M"
        else:
            p_str = "--"
        active = m.get("active_parameters")
        if active is not None:
            ab = float(active)
            a_str = f"{ab:.0f}B" if ab >= 1 else f"{ab*1000:.0f}M"
        else:
            a_str = "--"
        sc = m.get("size_class", "--") or "--"
        ow = "Y" if m.get("is_open_weights") else "N"
        reas = "Y" if m["is_reasoning"] else "N"
        print(f"{i+1:<3} {m['model']:<36} {float(m['composite_ability']):>8.4f} "
              f"{p_str:>10} {a_str:>10} {sc:>6} {ow:>4} {reas:>4}")

    print("\nDone!")


if __name__ == "__main__":
    main()
