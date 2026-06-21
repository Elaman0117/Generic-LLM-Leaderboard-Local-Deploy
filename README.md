# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## Pareto 前沿模型（综合能力从高到低）

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | GLM-5.2 (max) | 0.8030 | 753B | 40B | large | Y | Y |
| 2 | MiniMax-M3 | 0.7180 | 428B | 23B | large | Y | Y |
| 3 | MiMo-V2.5 | 0.6534 | 310B | 15B | large | Y | Y |
| 4 | DeepSeek V4 Flash (Reasoning, Max Effort) | 0.6354 | 284B | 13B | large | Y | Y |
| 5 | MiniMax-M2.7 | 0.6115 | 230B | 10B | large | Y | Y |
| 6 | Qwen3.6 27B (Reasoning) | 0.6080 | 28B | 28B | small | Y | Y |
| 7 | Qwen3.5 9B (Reasoning) | 0.4741 | 10B | 10B | small | Y | Y |
| 8 | Qwen3.5 4B (Reasoning) | 0.4078 | 5B | 5B | small | Y | Y |
| 9 | MiniCPM5-1B (Non-reasoning) | 0.2801 | 1B | 1B | tiny | Y | N |
| 10 | Qwen3.5 0.8B (Reasoning) | 0.1550 | 873M | 873M | tiny | Y | Y |
| 11 | Gemma 3 270M | 0.1204 | 268M | 268M | tiny | Y | N |

## 综合性能排行榜（抛开参数量）

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) | 0.9348 | -- | -- | -- | N | Y |
| 2 | GPT-5.5 (xhigh) | 0.8664 | -- | -- | -- | N | Y |
| 3 | Claude Opus 4.8 (Adaptive Reasoning, Max Effort) | 0.8571 | -- | -- | -- | N | Y |
| 4 | GPT-5.5 (high) | 0.8437 | -- | -- | -- | N | Y |
| 5 | Claude Opus 4.7 (Adaptive Reasoning, Max Effort) | 0.8232 | -- | -- | -- | N | Y |
| 6 | Gemini 3.5 Flash (high) | 0.8102 | -- | -- | -- | N | Y |
| 7 | GPT-5.5 (medium) | 0.8032 | -- | -- | -- | N | Y |
| 8 | GLM-5.2 (max) | 0.8030 | 753B | 40B | large | Y | Y |
| 9 | Gemini 3.1 Pro Preview | 0.7874 | -- | -- | -- | N | Y |
| 10 | Gemini 3.5 Flash (medium) | 0.7852 | -- | -- | -- | N | Y |
| 11 | GPT-5.3 Codex (xhigh) | 0.7788 | -- | -- | -- | N | Y |
| 12 | Qwen3.7 Max | 0.7732 | -- | -- | -- | N | Y |
| 13 | Muse Spark | 0.7225 | -- | -- | -- | N | Y |
| 14 | MiniMax-M3 | 0.7180 | 428B | 23B | large | Y | Y |
| 15 | Kimi K2.6 | 0.7169 | 1000B | 32B | large | Y | Y |
| 16 | Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort) | 0.7147 | -- | -- | -- | N | Y |
| 17 | GPT-5.5 (low) | 0.7125 | -- | -- | -- | N | Y |
| 18 | Grok 4.3 (medium) | 0.7102 | -- | -- | -- | N | Y |
| 19 | DeepSeek V4 Pro (Reasoning, Max Effort) | 0.6985 | 1600B | 49B | large | Y | Y |
| 20 | Claude Opus 4.7 (Non-reasoning, High Effort) | 0.6960 | -- | -- | -- | N | N |
| 21 | GLM-5.1 (Reasoning) | 0.6830 | 744B | 40B | large | Y | Y |
| 22 | Grok 4.3 (high) | 0.6811 | -- | -- | -- | N | Y |
| 23 | Qwen3.6 Plus | 0.6745 | -- | -- | -- | N | Y |
| 24 | DeepSeek V4 Pro (Reasoning, High Effort) | 0.6723 | 1600B | 49B | large | Y | Y |
| 25 | MiMo-V2.5-Pro | 0.6707 | 1023B | 42B | large | Y | Y |
| 26 | GPT-5.4 mini (xhigh) | 0.6636 | -- | -- | -- | N | Y |
| 27 | Kimi K2.7 Code | 0.6601 | 1000B | 32B | large | Y | Y |
| 28 | Grok 4.3 (low) | 0.6561 | -- | -- | -- | N | Y |
| 29 | MiMo-V2.5 | 0.6534 | 310B | 15B | large | Y | Y |
| 30 | Qwen3.7 Plus | 0.6426 | -- | -- | -- | N | Y |
| 31 | DeepSeek V4 Flash (Reasoning, Max Effort) | 0.6354 | 284B | 13B | large | Y | Y |
| 32 | Nemotron 3 Ultra 550B A55B (Reasoning) | 0.6336 | 550B | 55B | large | Y | Y |
| 33 | MiMo-V2-Omni-0327 | 0.6131 | -- | -- | -- | N | Y |
| 34 | GPT-5.5 Instant (May 2026) | 0.6118 | -- | -- | -- | N | Y |
| 35 | MiniMax-M2.7 | 0.6115 | 230B | 10B | large | Y | Y |
| 36 | GLM-5-Turbo | 0.6110 | -- | -- | -- | N | Y |
| 37 | DeepSeek V4 Flash (Reasoning, High Effort) | 0.6099 | 284B | 13B | large | Y | Y |
| 38 | Qwen3.6 27B (Reasoning) | 0.6080 | 28B | 28B | small | Y | Y |
| 39 | GPT-5.4 nano (xhigh) | 0.6050 | -- | -- | -- | N | Y |
| 40 | Gemini 3.5 Flash (minimal) | 0.6045 | -- | -- | -- | N | N |
| 41 | o3 | 0.5941 | -- | -- | -- | N | Y |
| 42 | MiMo-V2-Flash (Feb 2026) | 0.5865 | 309B | 15B | large | Y | Y |
| 43 | GLM 5V Turbo (Reasoning) | 0.5861 | -- | -- | -- | N | Y |
| 44 | Qwen3.5 397B A17B (Reasoning) | 0.5858 | 397B | 17B | large | Y | Y |
| 45 | MiMo-V2-Omni | 0.5852 | -- | -- | -- | N | Y |
| 46 | Claude Sonnet 4.6 (Non-reasoning, High Effort) | 0.5848 | -- | -- | -- | N | N |
| 47 | Claude Sonnet 4.6 (Non-reasoning, Low Effort) | 0.5746 | -- | -- | -- | N | N |
| 48 | GPT-5.5 (Non-reasoning) | 0.5699 | -- | -- | -- | N | N |
| 49 | Qwen3.6 35B A3B (Reasoning) | 0.5649 | 36B | 3B | small | Y | Y |
| 50 | Kimi K2.6 (Non-reasoning) | 0.5623 | 1000B | 32B | large | Y | N |
| 51 | Qwen3.5 122B A10B (Reasoning) | 0.5585 | 125B | 10B | medium | Y | Y |
| 52 | Hy3-preview (Reasoning) | 0.5576 | 295B | 21B | large | Y | Y |
| 53 | Command A+ | 0.5507 | 218B | 25B | large | Y | Y |
| 54 | Qwen3.5 Omni Plus | 0.5466 | -- | -- | -- | N | N |
| 55 | GLM-5.1 (Non-reasoning) | 0.5445 | 744B | 40B | large | Y | N |
| 56 | Gemini 2.5 Pro | 0.5436 | -- | -- | -- | N | Y |
| 57 | Step 3.7 Flash | 0.5381 | 198B | 11B | large | Y | Y |
| 58 | GPT-5.4 mini (medium) | 0.5379 | -- | -- | -- | N | Y |
| 59 | GPT-5.4 nano (medium) | 0.5335 | -- | -- | -- | N | Y |
| 60 | Gemma 4 31B (Reasoning) | 0.5287 | 31B | 31B | small | Y | Y |
| 61 | Qwen3.5 397B A17B (Non-reasoning) | 0.5208 | 397B | 17B | large | Y | N |
| 62 | Mistral Medium 3.5 | 0.5145 | 128B | 128B | medium | Y | Y |
| 63 | Step 3.5 Flash 2603 | 0.5114 | -- | -- | -- | N | Y |
| 64 | Claude 4.5 Haiku (Reasoning) | 0.5079 | -- | -- | -- | N | Y |
| 65 | Ring-2.6-1T | 0.4963 | 1000B | 63B | large | Y | Y |
| 66 | Nova 2.0 Lite (high) | 0.4929 | -- | -- | -- | N | Y |
| 67 | Doubao Seed Code | 0.4895 | -- | -- | -- | N | Y |
| 68 | Qwen3.5 122B A10B (Non-reasoning) | 0.4844 | 125B | 10B | medium | Y | N |
| 69 | JT-35B-Flash | 0.4833 | 35B | 35B | small | N | N |
| 70 | Nova 2.0 Pro Preview (low) | 0.4828 | -- | -- | -- | N | Y |
| 71 | Qwen3.6 27B (Non-reasoning) | 0.4808 | 28B | 28B | small | Y | N |
| 72 | DeepSeek V4 Pro (Non-reasoning) | 0.4788 | 1600B | 49B | large | Y | N |
| 73 | Qwen3.5 9B (Reasoning) | 0.4741 | 10B | 10B | small | Y | Y |
| 74 | Gemini 3.1 Flash-Lite | 0.4627 | -- | -- | -- | N | Y |
| 75 | Gemma 4 31B (Non-reasoning) | 0.4473 | 31B | 31B | small | Y | N |
| 76 | Nova 2.0 Pro Preview (medium) | 0.4472 | -- | -- | -- | N | Y |
| 77 | Gemma 4 12B (Reasoning) | 0.4467 | 12B | 12B | small | Y | Y |
| 78 | Nova 2.0 Lite (medium) | 0.4460 | -- | -- | -- | N | Y |
| 79 | EXAONE 4.5 33B | 0.4451 | 34B | 34B | small | Y | Y |
| 80 | MiMo-V2.5-Pro (Non-reasoning) | 0.4404 | 1023B | 42B | large | Y | N |
| 81 | Mercury 2 | 0.4398 | -- | -- | -- | N | Y |
| 82 | K-EXAONE (Reasoning) | 0.4394 | 236B | 23B | large | Y | Y |
| 83 | Gemma 4 26B A4B (Reasoning) | 0.4372 | 25B | 4B | small | Y | Y |
| 84 | Trinity Large Thinking | 0.4360 | 399B | 13B | large | Y | Y |
| 85 | Magistral Medium 1.2 | 0.4332 | -- | -- | -- | N | Y |
| 86 | Claude 4.5 Haiku (Non-reasoning) | 0.4323 | -- | -- | -- | N | N |
| 87 | DeepSeek V4 Flash (Non-reasoning) | 0.4320 | 284B | 13B | large | Y | N |
| 88 | Ling-2.6-1T | 0.4301 | 1026B | 63B | large | Y | N |
| 89 | Qwen3.5 35B A3B (Non-reasoning) | 0.4242 | 36B | 3B | small | Y | N |
| 90 | Hy3-preview (Non-reasoning) | 0.4239 | 295B | 21B | large | Y | N |
| 91 | Mistral Small 4 (Reasoning) | 0.4213 | 119B | 6B | medium | Y | Y |
| 92 | Nova 2.0 Omni (medium) | 0.4209 | -- | -- | -- | N | Y |
| 93 | Grok 4.3 (Non-reasoning) | 0.4203 | -- | -- | -- | N | N |
| 94 | ERNIE 5.0 Thinking Preview | 0.4121 | -- | -- | -- | N | Y |
| 95 | Nemotron Cascade 2 30B A3B | 0.4096 | 32B | 3B | small | Y | Y |
| 96 | Qwen3.5 4B (Reasoning) | 0.4078 | 5B | 5B | small | Y | Y |
| 97 | Qwen3.6 35B A3B (Non-reasoning) | 0.4020 | 36B | 3B | small | Y | N |
| 98 | HyperNova 60B 2605 | 0.4002 | 59B | 5B | medium | Y | Y |
| 99 | NVIDIA Nemotron 3 Super 120B A12B (Reasoning) | 0.3969 | 121B | 13B | medium | Y | Y |
| 100 | Qwen3 Next 80B A3B (Reasoning) | 0.3968 | 80B | 3B | medium | Y | Y |
| 101 | Nova 2.0 Lite (low) | 0.3962 | -- | -- | -- | N | Y |
| 102 | Nova 2.0 Omni (low) | 0.3944 | -- | -- | -- | N | Y |
| 103 | North Mini Code | 0.3864 | 30B | 3B | small | Y | Y |
| 104 | gpt-oss-120b (high) | 0.3799 | 117B | 5B | medium | Y | Y |
| 105 | Gemma 4 26B A4B (Non-reasoning) | 0.3797 | 25B | 4B | small | Y | N |
| 106 | MiMo-V2-Flash (Non-reasoning) | 0.3719 | 309B | 15B | large | Y | N |
| 107 | Qwen3.5 9B (Non-reasoning) | 0.3715 | 10B | 10B | small | Y | N |
| 108 | NVIDIA Nemotron 3 Nano 30B A3B (Reasoning) | 0.3660 | 32B | 4B | small | Y | Y |
| 109 | Qwen3.5 Omni Flash | 0.3639 | -- | -- | -- | N | N |
| 110 | Qwen3 Coder Next | 0.3583 | 80B | 3B | medium | Y | N |
| 111 | gpt-oss-120b (low) | 0.3480 | 117B | 5B | medium | Y | Y |
| 112 | Nova 2.0 Pro Preview (Non-reasoning) | 0.3458 | -- | -- | -- | N | N |
| 113 | Mistral Large 3 | 0.3404 | 675B | 41B | large | Y | N |
| 114 | Ling 2.6 Flash | 0.3395 | 107B | 7B | medium | Y | N |
| 115 | Gemma 4 E4B (Reasoning) | 0.3325 | 8B | 4B | small | Y | Y |
| 116 | Gemma 4 12B (Non-reasoning) | 0.3270 | 12B | 12B | small | Y | N |
| 117 | GPT-5.4 mini (Non-Reasoning) | 0.3269 | -- | -- | -- | N | N |
| 118 | Nemotron 3 Nano Omni 30B A3B Reasoning | 0.3234 | 30B | 3B | small | Y | Y |
| 119 | Mi:dm K 2.5 Pro | 0.3183 | 32B | 32B | small | N | Y |
| 120 | Solar Open 100B (Reasoning) | 0.3180 | 102B | 12B | medium | Y | Y |
| 121 | K-EXAONE (Non-reasoning) | 0.3158 | 236B | 23B | large | Y | N |
| 122 | INTELLECT-3 | 0.3151 | 107B | 12B | medium | Y | Y |
| 123 | GPT-5.4 nano (Non-Reasoning) | 0.3149 | -- | -- | -- | N | N |
| 124 | Qwen3.5 4B (Non-reasoning) | 0.3142 | 5B | 5B | small | Y | N |
| 125 | JT-MINI | 0.3129 | -- | -- | -- | N | N |
| 126 | Solar Pro 3 | 0.3094 | 102B | 12B | medium | N | Y |
| 127 | gpt-oss-20B (low) | 0.3071 | 21B | 4B | small | Y | Y |
| 128 | Llama Nemotron Super 49B v1.5 (Reasoning) | 0.3058 | 49B | 49B | medium | Y | Y |
| 129 | LongCat Flash Lite | 0.3011 | 68B | 3B | medium | Y | N |
| 130 | Qwen3 Next 80B A3B Instruct | 0.2991 | 80B | 3B | medium | Y | N |
| 131 | Llama 3.1 Instruct 405B | 0.2984 | 405B | 405B | large | Y | N |
| 132 | Devstral 2 | 0.2964 | 125B | 125B | medium | Y | N |
| 133 | Nova Premier | 0.2955 | -- | -- | -- | N | N |
| 134 | Llama 4 Maverick | 0.2893 | 402B | 17B | large | Y | N |
| 135 | Nova 2.0 Lite (Non-reasoning) | 0.2828 | -- | -- | -- | N | N |
| 136 | Motif-2-12.7B-Reasoning | 0.2826 | 13B | 13B | small | N | Y |
| 137 | MiniCPM5-1B (Non-reasoning) | 0.2801 | 1B | 1B | tiny | Y | N |
| 138 | Magistral Small 1.2 | 0.2798 | 24B | 24B | small | Y | Y |
| 139 | MiniCPM5-1B (Reasoning) | 0.2797 | 1B | 1B | tiny | Y | Y |
| 140 | Step3 VL 10B | 0.2792 | 10B | 10B | small | Y | Y |
| 141 | Mi:dm K 2.5 Pro Preview | 0.2790 | -- | -- | -- | N | Y |
| 142 | gpt-oss-20B (high) | 0.2790 | 21B | 4B | small | Y | Y |
| 143 | Nova 2.0 Omni (Non-reasoning) | 0.2681 | -- | -- | -- | N | N |
| 144 | Gemma 4 E2B (Reasoning) | 0.2680 | 5B | 2B | small | Y | Y |
| 145 | Mistral Small 4 (Non-reasoning) | 0.2662 | 119B | 6B | medium | Y | N |
| 146 | Qwen3 Omni 30B A3B (Reasoning) | 0.2650 | 35B | 3B | small | Y | Y |
| 147 | Nanbeige4.1-3B | 0.2622 | 4B | 4B | tiny | Y | Y |
| 148 | Devstral Small 2 | 0.2613 | 24B | 24B | small | Y | N |
| 149 | Llama 3.2 Instruct 90B (Vision) | 0.2606 | 90B | 90B | medium | Y | N |
| 150 | NVIDIA Nemotron Nano 12B v2 VL (Reasoning) | 0.2580 | 13B | 13B | small | Y | Y |
| 151 | ERNIE 4.5 300B A47B | 0.2577 | 300B | 47B | large | Y | N |
| 152 | Gemma 4 E4B (Non-reasoning) | 0.2547 | 8B | 4B | small | Y | N |
| 153 | Llama 3.1 Nemotron Ultra 253B v1 (Reasoning) | 0.2533 | 253B | 253B | large | Y | Y |
| 154 | EXAONE 4.0 32B (Reasoning) | 0.2501 | 32B | 32B | small | Y | Y |
| 155 | Qwen3.5 2B (Reasoning) | 0.2491 | 2B | 2B | tiny | Y | Y |
| 156 | Falcon-H1R-7B | 0.2488 | 7B | 7B | small | Y | Y |
| 157 | Sarvam 105B (high) | 0.2439 | 106B | 10B | medium | Y | Y |
| 158 | LFM2.5-8B-A1B | 0.2337 | -- | -- | -- | Y | Y |
| 159 | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2336 | 49B | 49B | medium | Y | N |
| 160 | NVIDIA Nemotron Nano 9B V2 (Reasoning) | 0.2323 | 9B | 9B | small | Y | Y |
| 161 | Ministral 3 14B | 0.2312 | 14B | 14B | small | Y | N |
| 162 | Solar Pro 2 (Reasoning) | 0.2279 | -- | -- | -- | N | Y |
| 163 | Ring-flash-2.0 | 0.2277 | 103B | 6B | medium | Y | Y |
| 164 | Command A | 0.2247 | 111B | 111B | medium | Y | N |
| 165 | NVIDIA Nemotron 3 Nano 4B | 0.2171 | 4B | 4B | tiny | Y | Y |
| 166 | Llama 3.1 Nemotron Instruct 70B | 0.2164 | 70B | 70B | medium | Y | N |
| 167 | Llama 3.3 Instruct 70B | 0.2160 | 70B | 70B | medium | Y | N |
| 168 | Llama 4 Scout | 0.2100 | 109B | 17B | medium | Y | N |
| 169 | Ministral 3 8B | 0.2081 | 8B | 8B | small | Y | N |
| 170 | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.2058 | 9B | 9B | small | Y | N |
| 171 | Qwen3.5 2B (Non-reasoning) | 0.2018 | 2B | 2B | tiny | Y | N |
| 172 | Kimi Linear 48B A3B Instruct | 0.2001 | 49B | 3B | medium | Y | N |
| 173 | Gemma 4 E2B (Non-reasoning) | 0.1988 | 5B | 2B | small | Y | N |
| 174 | Solar Pro 2 (Non-reasoning) | 0.1962 | -- | -- | -- | N | N |
| 175 | Qwen3 Omni 30B A3B Instruct | 0.1931 | 35B | 3B | small | Y | N |
| 176 | Granite 4.1 30B | 0.1861 | 30B | 30B | small | Y | N |
| 177 | EXAONE 4.0 32B (Non-reasoning) | 0.1855 | 32B | 32B | small | Y | N |
| 178 | NVIDIA Nemotron 3 Nano 30B A3B (Non-reasoning) | 0.1847 | 32B | 4B | small | Y | N |
| 179 | Granite 4.1 8B | 0.1792 | 8B | 8B | small | Y | N |
| 180 | Jamba 1.7 Large | 0.1775 | 398B | 94B | large | Y | N |
| 181 | Sarvam 30B (high) | 0.1755 | 32B | 2B | small | Y | Y |
| 182 | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1698 | 13B | 13B | small | Y | N |
| 183 | Granite 4.0 H Small | 0.1667 | 32B | 9B | small | Y | N |
| 184 | Phi-4 | 0.1652 | 14B | 14B | small | Y | N |
| 185 | LFM2 24B A2B | 0.1635 | 24B | 2B | small | Y | N |
| 186 | Nova Micro | 0.1615 | -- | -- | -- | N | N |
| 187 | Ministral 3 3B | 0.1594 | 3B | 3B | tiny | Y | N |
| 188 | Qwen3.5 0.8B (Reasoning) | 0.1550 | 873M | 873M | tiny | Y | Y |
| 189 | Reka Flash 3 | 0.1520 | 21B | 21B | small | Y | Y |
| 190 | Jamba Reasoning 3B | 0.1393 | 3B | 3B | tiny | Y | Y |
| 191 | Llama 3.2 Instruct 11B (Vision) | 0.1355 | 11B | 11B | small | Y | N |
| 192 | MiniCPM-V 4.6 1.3B | 0.1290 | 1B | 1B | tiny | Y | N |
| 193 | Ling-mini-2.0 | 0.1278 | 16B | 1B | small | Y | N |
| 194 | Phi-4 Mini Instruct | 0.1263 | 4B | 4B | tiny | Y | N |
| 195 | Qwen3.5 0.8B (Non-reasoning) | 0.1234 | 873M | 873M | tiny | Y | N |
| 196 | Gemma 3 270M | 0.1204 | 268M | 268M | tiny | Y | N |
| 197 | Apertus 70B Instruct | 0.1165 | 70B | 70B | medium | Y | N |
| 198 | LFM2 2.6B | 0.1164 | 3B | 3B | tiny | Y | N |
| 199 | Jamba 1.7 Mini | 0.1157 | 52B | 12B | medium | Y | N |
| 200 | Granite 4.1 3B | 0.1143 | 3B | 3B | tiny | Y | N |
| 201 | LFM2.5-1.2B-Instruct | 0.1120 | 1B | 1B | tiny | Y | N |
| 202 | Phi-4 Multimodal Instruct | 0.1098 | 6B | 6B | small | Y | N |
| 203 | Exaone 4.0 1.2B (Reasoning) | 0.1062 | 1B | 1B | tiny | Y | Y |
| 204 | Granite 4.0 H 1B | 0.1052 | 2B | 2B | tiny | Y | N |
| 205 | LFM2.5-1.2B-Thinking | 0.1040 | 1B | 1B | tiny | Y | Y |
| 206 | Granite 4.0 Micro | 0.1012 | 3B | 3B | tiny | Y | N |
| 207 | Exaone 4.0 1.2B (Non-reasoning) | 0.1008 | 1B | 1B | tiny | Y | N |
| 208 | LFM2 8B A1B | 0.0926 | 8B | 2B | small | Y | N |
| 209 | Granite 4.0 1B | 0.0876 | 2B | 2B | tiny | Y | N |
| 210 | LFM2.5-VL-1.6B | 0.0820 | 2B | 2B | tiny | Y | N |
| 211 | Apertus 8B Instruct | 0.0743 | 8B | 8B | small | Y | N |
| 212 | Granite 4.0 350M | 0.0720 | 350M | 350M | tiny | Y | N |
| 213 | Granite 4.0 H 350M | 0.0537 | 340M | 340M | tiny | Y | N |
| 214 | Tiny Aya Global | 0.0532 | 3B | 3B | tiny | Y | N |

### 评分方法

1. **18项评估指标**各自线性归一化到 [0,1]
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **Pareto前沿** = 不被任何其他模型支配的模型（参数更少且能力更高）

### 横轴说明

**X轴 = 模型总参数量 (totalParameters)**

参数数据来自 Artificial Analysis 的模型元数据 (`totalParameters`)，
即模型的总参数量（单位：十亿/B）。对于 MoE 模型，总参数量包含所有专家参数。
线性刻度展示，按实际参数量1:1排布。

Pareto 前沿上的模型代表了**最高训练效率**——用更少的参数实现更高的能力。

### 数据来源

**数据来源**: [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)  
**方法论**: [AA Methodology](https://artificialanalysis.ai/methodology)  
**模型总数**: 214  