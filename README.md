# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.0000，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 344 个入图，0 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3.1 Pro | 0.8793 | 2.8T | — | large | ❌ | ✅ |
| 2 | Kimi K3 (max) | 0.8521 | 2.8T | 104B | large | ✅ | ✅ |
| 3 | GLM-5.3 (max) | 0.7745 | 753B | 40B | large | ✅ | ✅ |
| 4 | GLM-5.2 (max) | 0.7733 | 753B | 40B | large | ✅ | ✅ |
| 5 | Step 5 Preview | 0.7655 | 600B | — | large | ✅ | ✅ |
| 6 | Ling 3.1 Flash | 0.7540 | 560B | — | large | ✅ | ✅ |
| 7 | Qwen3.8 2.4T A95B | 0.7493 | 2.4T | 95B | large | ✅ | ✅ |
| 8 | DeepSeek V4.1 Flash (max) | 0.7369 | 552B | 16B | large | ✅ | ✅ |
| 9 | DeepSeek V4 Flash 0731 (max) | 0.7367 | 284B | 13B | large | ✅ | ✅ |
| 10 | DeepSeek V4 Flash Vision (max) | 0.7287 | 284B | — | large | ❌ | ✅ |
| 11 | DeepSeek V4 Pro (high) | 0.7267 | 1.6T | 49B | large | ✅ | ✅ |
| 12 | Muse Spark Open (xhigh) | 0.7232 | 816B | 42B | large | ✅ | ✅ |
| 13 | DeepSeek V4.1 Flash 1017 (max) | 0.7163 | 552B | 16B | large | ✅ | ✅ |
| 14 | GLM-5.3-Flash | 0.7158 | 320B | 18B | large | ✅ | ✅ |
| 15 | Qwen3.8-Flash-Next | 0.7083 | 180B | 6B | large | ✅ | ✅ |
| 16 | MiMo-V2.6-Pro | 0.7041 | 1T | 42B | large | ✅ | ✅ |
| 17 | Motif 3 (Beta) | 0.7005 | 314B | — | large | ❌ | ✅ |
| 18 | Qwen3.5 27B | 0.6923 | 27.8B | — | small | ✅ | ✅ |
| 19 | Motif 3 | 0.6905 | 314B | 13.2B | large | ✅ | ✅ |
| 20 | Nex-N2-Pro | 0.6890 | 397B | 17B | large | ✅ | ✅ |
| 21 | Kimi K2.6 | 0.6863 | 1T | 32B | large | ✅ | ✅ |
| 22 | DeepSeek V4 Pro (max) | 0.6794 | 1.6T | 49B | large | ✅ | ✅ |
| 23 | GLM-5 | 0.6532 | 744B | 40B | large | ✅ | ✅ |
| 24 | MiniMax-M2.5 | 0.6531 | 230B | 10B | large | ✅ | ✅ |
| 25 | Hy3-preview | 0.6515 | 295B | 21B | large | ✅ | ✅ |
| 26 | Kimi K2.7 Code | 0.6480 | 1T | 32B | large | ✅ | ✅ |
| 27 | MiMo-V2-Flash (Feb 2026) | 0.6475 | 309B | 15B | large | ✅ | ✅ |
| 28 | Kimi K2 Thinking | 0.6436 | 1T | 32B | large | ✅ | ✅ |
| 29 | DeepSeek V4 Pro 0813 (max) | 0.6407 | 1.6T | 49B | large | ✅ | ✅ |
| 30 | MiMo-V2-Flash | 0.6357 | 309B | 15B | large | ✅ | ✅ |
| 31 | DeepSeek V4 Flash (max) | 0.6349 | 284B | 13B | large | ✅ | ✅ |
| 32 | Qwen3.8 27B (xhigh) | 0.6310 | 27B | — | small | ✅ | ✅ |
| 33 | GLM-5.1 | 0.6305 | 744B | 40B | large | ✅ | ✅ |
| 34 | JT-4.1 Flash 236B A21B | 0.6202 | 236B | — | large | ❌ | ✅ |
| 35 | Qwen3.5 35B A3B | 0.6190 | 36B | 3B | small | ✅ | ✅ |
| 36 | Kimi K2.5 | 0.6126 | 1T | 32B | large | ✅ | ✅ |
| 37 | DeepSeek V4 Flash (high) | 0.6110 | 284B | 13B | large | ✅ | ✅ |
| 38 | MiniMax-M2.1 | 0.6078 | 230B | 10B | large | ✅ | ✅ |
| 39 | Mistral Large 4 Preview | 0.6049 | 1T | — | large | ❌ | ✅ |
| 40 | MiMo-V2.5 | 0.5979 | 310B | 15B | large | ✅ | ✅ |
| 41 | GLM-4.7 | 0.5978 | 357B | 32B | large | ✅ | ✅ |
| 42 | Kimi K3 (low) | 0.5976 | 2.8T | 104B | large | ✅ | ✅ |
| 43 | Ling-3.0-flash-VL | 0.5960 | 124B | 5.5B | medium | ✅ | ✅ |
| 44 | Qwen3.5 397B A17B | 0.5936 | 397B | 17B | large | ✅ | ✅ |
| 45 | Qwen3.6 27B | 0.5912 | 27.8B | — | small | ✅ | ✅ |
| 46 | GLM-5.1 (non-reasoning) | 0.5902 | 744B | 40B | large | ✅ | ❌ |
| 47 | MiMo-V2.6-Flash | 0.5871 | 309B | 15B | large | ✅ | ✅ |
| 48 | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5848 | 236B | — | large | ❌ | ❌ |
| 49 | Solar Open2 250B | 0.5844 | 250B | 15B | large | ✅ | ✅ |
| 50 | Step 3.7 Flash | 0.5825 | 198B | 11B | large | ✅ | ✅ |
| 51 | MiniMax-M3 | 0.5814 | 428B | 23B | large | ✅ | ✅ |
| 52 | Step 3.5 Flash | 0.5804 | 196B | 11B | large | ✅ | ✅ |
| 53 | DeepSeek V3.2 | 0.5793 | 685B | 37B | large | ✅ | ✅ |
| 54 | MiMo-V2.5-Pro | 0.5782 | 1T | 42B | large | ✅ | ✅ |
| 55 | Kimi K2.6 (non-reasoning) | 0.5779 | 1T | 32B | large | ✅ | ❌ |
| 56 | Hy3 | 0.5751 | 299B | 21B | large | ✅ | ✅ |
| 57 | Qwen3.5 122B A10B | 0.5723 | 125B | 10B | medium | ✅ | ✅ |
| 58 | Qwen3.5 27B (non-reasoning) | 0.5708 | 27.8B | — | small | ✅ | ❌ |
| 59 | MiniMax-M2 | 0.5701 | 230B | 10B | large | ✅ | ✅ |
| 60 | Qwen3.5 397B A17B (non-reasoning) | 0.5699 | 397B | 17B | large | ✅ | ❌ |
| 61 | Quasar 438B (max) | 0.5617 | 438B | — | large | ❌ | ✅ |
| 62 | K2 Horizon 375B A23B | 0.5561 | 375B | 23B | large | ✅ | ✅ |
| 63 | GLM-5.3 (low) | 0.5476 | 753B | 40B | large | ✅ | ✅ |
| 64 | Qwen3.6 35B A3B | 0.5402 | 36B | 3B | small | ✅ | ✅ |
| 65 | Qwen3.6 27B (non-reasoning) | 0.5352 | 27.8B | — | small | ✅ | ❌ |
| 66 | DeepSeek V3.2 Speciale | 0.5328 | 685B | 37B | large | ✅ | ✅ |
| 67 | Kimi K2.5 (non-reasoning) | 0.5308 | 1T | 32B | large | ✅ | ❌ |
| 68 | Inkling (xhigh) | 0.5279 | 975B | 41B | large | ✅ | ✅ |
| 69 | Qwen3.5 122B A10B (non-reasoning) | 0.5253 | 125B | 10B | medium | ✅ | ❌ |
| 70 | Beam 1.0 | 0.5242 | 501B | 23B | large | ✅ | ✅ |
| 71 | Inkling Small | 0.5240 | 266B | 12B | large | ✅ | ✅ |
| 72 | K2 Horizon MoVA 36B A4B | 0.5234 | 36B | 4B | small | ✅ | ✅ |
| 73 | MiniMax-M2.7 | 0.5211 | 230B | 10B | large | ✅ | ✅ |
| 74 | Nemotron 3 Ultra | 0.5204 | 550B | 55B | large | ✅ | ✅ |
| 75 | JT-35B-Flash | 0.5182 | 35B | — | small | ❌ | ❌ |
| 76 | Ling 3.0 Flash | 0.5062 | 124B | 5.1B | medium | ✅ | ✅ |
| 77 | GLM-5 (non-reasoning) | 0.5039 | 744B | 40B | large | ✅ | ❌ |
| 78 | Qwen3.8 27B (medium) | 0.5022 | 27B | — | small | ✅ | ✅ |
| 79 | DeepSeek V4 Pro (non-reasoning) | 0.4977 | 1.6T | 49B | large | ✅ | ❌ |
| 80 | Qwen3.8 27B (low) | 0.4974 | 27B | — | small | ✅ | ✅ |
| 81 | Ling-2.6-1T | 0.4918 | 1T | 63B | large | ✅ | ❌ |
| 82 | A.X-K2 | 0.4904 | 692B | 33B | large | ✅ | ✅ |
| 83 | Ling-3.0-flash-Fin | 0.4895 | 124B | 5.1B | medium | ✅ | ✅ |
| 84 | Qwen3.6 35B A3B (non-reasoning) | 0.4867 | 36B | 3B | small | ✅ | ❌ |
| 85 | G9v3-39A5B | 0.4829 | 39B | 5B | small | ✅ | ✅ |
| 86 | Gemma 4 26B A4B | 0.4822 | 25.2B | 3.8B | small | ✅ | ✅ |
| 87 | DeepSeek V3.2 Exp | 0.4813 | 685B | 37B | large | ✅ | ✅ |
| 88 | EXAONE 4.5 33B | 0.4807 | 34.4B | — | small | ✅ | ✅ |
| 89 | K-EXAONE | 0.4806 | 236B | 23B | large | ✅ | ✅ |
| 90 | Qwen3 VL 235B A22B | 0.4794 | 235B | 22B | large | ✅ | ✅ |
| 91 | DeepSeek V3.2 (non-reasoning) | 0.4770 | 685B | 37B | large | ✅ | ❌ |
| 92 | DeepSeek V4 Flash (non-reasoning) | 0.4761 | 284B | 13B | large | ✅ | ❌ |
| 93 | Gemma 4 31B | 0.4754 | 30.7B | — | small | ✅ | ✅ |
| 94 | Gemma 4 12B | 0.4732 | 12B | — | small | ✅ | ✅ |
| 95 | Nemotron 3.5 Super VL | 0.4720 | 120B | 12B | medium | ✅ | ✅ |
| 96 | GLM-4.7 (non-reasoning) | 0.4665 | 357B | 32B | large | ✅ | ❌ |
| 97 | MiMo-V2.5-Pro (non-reasoning) | 0.4655 | 1T | 42B | large | ✅ | ❌ |
| 98 | Mistral Large 4 (high) | 0.4625 | 1T | — | large | ✅ | ✅ |
| 99 | Qwen3.5 35B A3B (non-reasoning) | 0.4612 | 36B | 3B | small | ✅ | ❌ |
| 100 | K-EXAONE 2.0 | 0.4608 | 750B | 37B | large | ✅ | ✅ |
| 101 | GLM-4.7-Flash | 0.4588 | 31.2B | 3B | small | ✅ | ✅ |
| 102 | Qwen3.5 4B | 0.4581 | 4.66B | — | small | ✅ | ✅ |
| 103 | GLM-4.6 | 0.4570 | 357B | 32B | large | ✅ | ✅ |
| 104 | Solar Mini 4 | 0.4539 | 35B | — | small | ❌ | ✅ |
| 105 | Qwen3.5 9B | 0.4537 | 9.65B | — | small | ✅ | ✅ |
| 106 | LongCat 2.0 | 0.4509 | 1.6T | 48B | large | ✅ | ✅ |
| 107 | Mistral Large 4 (medium) | 0.4484 | 1.1T | 52B | large | ✅ | ✅ |
| 108 | Gemma 4 31B (non-reasoning) | 0.4470 | 30.7B | — | small | ✅ | ❌ |
| 109 | Ring-2.6-1T | 0.4467 | 1T | 63B | large | ✅ | ✅ |
| 110 | DeepSeek V3.1 Terminus | 0.4448 | 685B | 37B | large | ✅ | ✅ |
| 111 | Mistral Medium 3.5 | 0.4444 | 128B | — | medium | ✅ | ✅ |
| 112 | Qwen3.8 27B (non-reasoning) | 0.4442 | 27B | — | small | ✅ | ❌ |
| 113 | MiMo-V2-Flash (non-reasoning) | 0.4438 | 309B | 15B | large | ✅ | ❌ |
| 114 | Apriel-v1.6-15B-Thinker | 0.4429 | 15B | — | small | ✅ | ✅ |
| 115 | Qwen3.5 9B (non-reasoning) | 0.4402 | 9.65B | — | small | ✅ | ❌ |
| 116 | GLM-5.2 (non-reasoning) | 0.4357 | 753B | 40B | large | ✅ | ❌ |
| 117 | Qwen3 VL 32B | 0.4317 | 33.4B | — | small | ✅ | ✅ |
| 118 | K2 Horizon 7B | 0.4317 | 7B | — | small | ✅ | ✅ |
| 119 | Hy3-preview (non-reasoning) | 0.4304 | 295B | 21B | large | ✅ | ❌ |
| 120 | Muse Glimmer (high) | 0.4301 | 30B | — | small | ✅ | ✅ |
| 121 | Kimi K2 0905 | 0.4289 | 1T | 32B | large | ✅ | ❌ |
| 122 | Command A+ | 0.4222 | 218B | 25B | large | ✅ | ✅ |
| 123 | Gemma 4 26B A4B (non-reasoning) | 0.4197 | 25.2B | 3.8B | small | ✅ | ❌ |
| 124 | Nemotron Cascade 2 30B A3B | 0.4196 | 31.6B | 3B | small | ✅ | ✅ |
| 125 | Apriel-v1.5-15B-Thinker | 0.4154 | 15B | — | small | ✅ | ✅ |
| 126 | DeepSeek V3.1 | 0.4136 | 685B | 37B | large | ✅ | ✅ |
| 127 | Nemotron 3.5 Bolt 74B-A9B | 0.4132 | 74B | 9B | medium | ✅ | ✅ |
| 128 | DeepSeek V4.1 Flash 1017 (non-reasoning) | 0.4128 | 552B | 16B | large | ✅ | ❌ |
| 129 | DeepSeek V4.1 Flash (non-reasoning) | 0.4053 | 552B | 16B | large | ✅ | ❌ |
| 130 | GLM-4.5 | 0.4012 | 355B | 32B | large | ✅ | ✅ |
| 131 | Kimi K2 | 0.3929 | 1T | 32B | large | ✅ | ❌ |
| 132 | DeepSeek R1 0528 | 0.3919 | 685B | 37B | large | ✅ | ✅ |
| 133 | Nemotron 3 Super | 0.3911 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 134 | Trinity Large Thinking | 0.3793 | 399B | 13B | large | ✅ | ✅ |
| 135 | DeepSeek V3.1 Terminus (non-reasoning) | 0.3789 | 685B | 37B | large | ✅ | ❌ |
| 136 | Seed-OSS-36B-Instruct | 0.3672 | 36.2B | — | small | ✅ | ✅ |
| 137 | DeepSeek V3.2 Exp (non-reasoning) | 0.3660 | 685B | 37B | large | ✅ | ❌ |
| 138 | gpt-oss-120b (high) | 0.3628 | 117B | 5.1B | medium | ✅ | ✅ |
| 139 | GLM-4.6 (non-reasoning) | 0.3611 | 357B | 32B | large | ✅ | ❌ |
| 140 | DiffusionGemma 26B A4B | 0.3577 | 25.2B | 3.8B | small | ✅ | ✅ |
| 141 | Qwen3 235B A22B 2507 | 0.3574 | 235B | 22B | large | ✅ | ✅ |
| 142 | GLM-4.5-Air | 0.3532 | 106B | 12B | medium | ✅ | ✅ |
| 143 | Qwen3.5 4B (non-reasoning) | 0.3496 | 4.66B | — | small | ✅ | ❌ |
| 144 | Qwen3 Coder Next | 0.3493 | 79.7B | 3B | medium | ✅ | ❌ |
| 145 | HyperNova 60B 2605 (high) | 0.3474 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 146 | North Mini Code | 0.3468 | 30B | 3B | small | ✅ | ✅ |
| 147 | K-EXAONE (non-reasoning) | 0.3464 | 236B | 23B | large | ✅ | ❌ |
| 148 | DeepSeek V3.1 (non-reasoning) | 0.3442 | 685B | 37B | large | ✅ | ❌ |
| 149 | Qwen3 VL 235B A22B | 0.3433 | 235B | — | large | ✅ | ❌ |
| 150 | Ling 2.6 Flash | 0.3432 | 107B | 7.4B | medium | ✅ | ❌ |
| 151 | Solar Open 100B | 0.3418 | 102B | 12B | medium | ✅ | ✅ |
| 152 | LongCat Flash Lite | 0.3409 | 68.5B | 3B | medium | ✅ | ❌ |
| 153 | K2 Horizon 3.7B | 0.3406 | 3.7B | — | tiny | ✅ | ✅ |
| 154 | Granite 4.2 30B | 0.3403 | 30B | — | small | ✅ | ✅ |
| 155 | Ring-1T | 0.3389 | 1T | 50B | large | ✅ | ✅ |
| 156 | Gemma 4 12B (non-reasoning) | 0.3374 | 12B | — | small | ✅ | ❌ |
| 157 | Qwen3 235B 2507 | 0.3297 | 235B | 22B | large | ✅ | ❌ |
| 158 | Pixtral Large | 0.3291 | 124B | — | medium | ✅ | ❌ |
| 159 | Qwen3 Next 80B A3B | 0.3291 | 80B | 3B | medium | ✅ | ✅ |
| 160 | Ling 3.0 Tiny | 0.3275 | 7.9B | 1.3B | small | ✅ | ✅ |
| 161 | GLM-4.6V | 0.3268 | 108B | 12B | medium | ✅ | ✅ |
| 162 | K2-V2 (high) | 0.3266 | 70B | — | medium | ✅ | ✅ |
| 163 | K2 Think V2 | 0.3244 | 70B | — | medium | ✅ | ✅ |
| 164 | Qwen3 Coder 480B | 0.3218 | 480B | 35B | large | ✅ | ❌ |
| 165 | Tri-21B-think Preview | 0.3218 | 21B | — | small | ✅ | ✅ |
| 166 | MiniMax M1 80k | 0.3188 | 456B | 45.9B | large | ✅ | ✅ |
| 167 | Tri-21B-Think | 0.3176 | 21B | — | small | ✅ | ✅ |
| 168 | Cogito v2.1 | 0.3167 | 671B | 37B | large | ✅ | ✅ |
| 169 | HyperCLOVA X SEED Think (32B) | 0.3144 | 32B | — | small | ✅ | ✅ |
| 170 | Nemotron 3.5 Lightning | 0.3131 | 31.6B | 3.6B | small | ✅ | ✅ |
| 171 | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3127 | 1.6T | 49B | large | ✅ | ❌ |
| 172 | Qwen3 VL 30B A3B | 0.3125 | 30B | 3B | small | ✅ | ✅ |
| 173 | Qwen3 VL 32B | 0.3122 | 33.4B | — | small | ✅ | ❌ |
| 174 | gpt-oss-20b (low) | 0.3109 | 21B | 3.6B | small | ✅ | ✅ |
| 175 | MiniCPM5-2B | 0.3048 | 2.6B | — | tiny | ✅ | ✅ |
| 176 | Nemotron 3 Nano Omni 30B A3B | 0.3037 | 30B | 3B | small | ✅ | ✅ |
| 177 | MiniMax M1 40k | 0.3010 | 456B | 45.9B | large | ✅ | ✅ |
| 178 | GLM-4.7-Flash (non-reasoning) | 0.3005 | 31.2B | 3B | small | ✅ | ❌ |
| 179 | Qwen3 Next 80B A3B | 0.3002 | 80B | 3B | medium | ✅ | ❌ |
| 180 | Nemotron 3 Nano | 0.3001 | 31.6B | 3.6B | small | ✅ | ✅ |
| 181 | Motif-2-12.7B | 0.2964 | 12.7B | — | small | ❌ | ✅ |
| 182 | INTELLECT-3 | 0.2956 | 107B | 12B | medium | ✅ | ✅ |
| 183 | gpt-oss-20b (high) | 0.2936 | 21B | 3.6B | small | ✅ | ✅ |
| 184 | Granite 4.2 8B | 0.2904 | 8B | — | small | ✅ | ✅ |
| 185 | Mistral Small 4 | 0.2862 | 119B | 6.5B | medium | ✅ | ✅ |
| 186 | Ling-1T | 0.2840 | 1T | 50B | large | ✅ | ❌ |
| 187 | gpt-oss-120b (low) | 0.2795 | 117B | 5.1B | medium | ✅ | ✅ |
| 188 | Solar Pro 3 | 0.2783 | 102B | — | medium | ❌ | ✅ |
| 189 | Step3 VL 10B | 0.2761 | 10.2B | — | small | ✅ | ✅ |
| 190 | Qwen3 VL 30B A3B | 0.2752 | 30B | 3B | small | ✅ | ❌ |
| 191 | Qwen3 4B 2507 | 0.2696 | 4.02B | — | tiny | ✅ | ✅ |
| 192 | Qwen3 VL 8B | 0.2673 | 8.77B | — | small | ✅ | ✅ |
| 193 | Mistral Large 3 | 0.2660 | 675B | 41B | large | ✅ | ❌ |
| 194 | K2-V2 (medium) | 0.2628 | 70B | — | medium | ✅ | ✅ |
| 195 | Devstral 2 | 0.2591 | 125B | — | medium | ✅ | ❌ |
| 196 | DeepSeek V3 0324 | 0.2584 | 671B | 37B | large | ✅ | ❌ |
| 197 | NVIDIA Nemotron Nano 12B v2 VL | 0.2581 | 13.2B | — | small | ✅ | ✅ |
| 198 | Qwen3 Omni 30B A3B | 0.2579 | 35.3B | 3B | small | ✅ | ✅ |
| 199 | DeepSeek R1 (Jan) | 0.2570 | 685B | 37B | large | ✅ | ✅ |
| 200 | Qwen3 30B A3B 2507 | 0.2551 | 30.5B | 3.3B | small | ✅ | ✅ |
| 201 | Gemma 4 E4B (non-reasoning) | 0.2541 | 8B | 4.5B | small | ✅ | ❌ |
| 202 | Falcon-H1R-7B | 0.2512 | 7B | — | small | ✅ | ✅ |
| 203 | Hermes 4 405B | 0.2482 | 406B | — | large | ✅ | ✅ |
| 204 | Llama Nemotron Super 49B v1.5 | 0.2471 | 49B | — | medium | ✅ | ✅ |
| 205 | Devstral Small 2 | 0.2465 | 24B | — | small | ✅ | ❌ |
| 206 | Llama 4 Maverick | 0.2372 | 402B | 17B | large | ✅ | ❌ |
| 207 | Qwen3 Coder 30B A3B | 0.2366 | 30.5B | 3.3B | small | ✅ | ❌ |
| 208 | Mistral Small 4 (non-reasoning) | 0.2334 | 119B | 6.5B | medium | ✅ | ❌ |
| 209 | EXAONE 4.0 32B | 0.2315 | 32B | — | small | ✅ | ✅ |
| 210 | Sarvam 105B (high) | 0.2284 | 106B | 10.3B | medium | ✅ | ✅ |
| 211 | MiniCPM5-1B | 0.2271 | 1B | — | tiny | ✅ | ✅ |
| 212 | Magistral Small 1.2 | 0.2238 | 24B | — | small | ✅ | ✅ |
| 213 | Ring-flash-2.0 | 0.2208 | 103B | 6.1B | medium | ✅ | ✅ |
| 214 | GLM-4.5V | 0.2166 | 108B | 12B | medium | ✅ | ✅ |
| 215 | Ling-flash-2.0 | 0.2125 | 103B | 6.1B | medium | ✅ | ❌ |
| 216 | Gemma 4 E4B | 0.2103 | 8B | 4.5B | small | ✅ | ✅ |
| 217 | Qwen3.5 2B | 0.2102 | 2.27B | — | tiny | ✅ | ✅ |
| 218 | Granite 4.2 3B | 0.2062 | 3B | — | tiny | ✅ | ✅ |
| 219 | Llama Nemotron Ultra | 0.2062 | 253B | — | large | ✅ | ✅ |
| 220 | Qwen3 VL 4B | 0.2054 | 4.44B | — | tiny | ✅ | ✅ |
| 221 | Qwen3 235B | 0.2052 | 235B | 22B | large | ✅ | ✅ |
| 222 | ERNIE 4.5 300B A47B | 0.2033 | 300B | 47B | large | ✅ | ❌ |
| 223 | Llama 3.3 Nemotron Super 49B | 0.2023 | 49B | — | medium | ✅ | ✅ |
| 224 | Devstral Small (May) | 0.2022 | 23.6B | — | small | ✅ | ❌ |
| 225 | Hermes 4 405B (non-reasoning) | 0.2013 | 406B | — | large | ✅ | ❌ |
| 226 | Qwen3 30B A3B 2507 (non-reasoning) | 0.1994 | 30.5B | 3.3B | small | ✅ | ❌ |
| 227 | Mistral Large 2 (Jul) | 0.1993 | 123B | — | medium | ✅ | ❌ |
| 228 | Granite 4.1 30B | 0.1989 | 30B | — | small | ✅ | ❌ |
| 229 | GLM-4.6V (non-reasoning) | 0.1968 | 108B | 12B | medium | ✅ | ❌ |
| 230 | Ministral 3 14B | 0.1967 | 14B | — | small | ✅ | ❌ |
| 231 | Qwen3.5 2B (non-reasoning) | 0.1940 | 2.27B | — | tiny | ✅ | ❌ |
| 232 | Hermes 4 70B | 0.1940 | 70.6B | — | medium | ✅ | ✅ |
| 233 | Llama 3.1 405B | 0.1928 | 405B | — | large | ✅ | ❌ |
| 234 | Qwen2.5 72B | 0.1897 | 72B | — | medium | ✅ | ❌ |
| 235 | Qwen3 Omni 30B A3B | 0.1895 | 35.3B | 3B | small | ✅ | ❌ |
| 236 | K2-V2 (low) | 0.1893 | 70B | — | medium | ✅ | ✅ |
| 237 | MiniCPM5-1B (non-reasoning) | 0.1892 | 1B | — | tiny | ✅ | ❌ |
| 238 | Qwen3 VL 8B | 0.1865 | 8.77B | — | small | ✅ | ❌ |
| 239 | DeepSeek V3 (Dec) | 0.1845 | 671B | 37B | large | ✅ | ❌ |
| 240 | Qwen3 4B | 0.1840 | 4.02B | — | tiny | ✅ | ✅ |
| 241 | LFM2.5-8B-A1B | 0.1815 | 8.3B | 1.5B | small | ✅ | ✅ |
| 242 | Olmo 3.1 32B Think | 0.1805 | 32.2B | — | small | ✅ | ✅ |
| 243 | Qwen3 30B | 0.1774 | 30.5B | 3.3B | small | ✅ | ✅ |
| 244 | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1750 | 49B | — | medium | ✅ | ❌ |
| 245 | G9v3-3B | 0.1745 | 3B | — | tiny | ✅ | ✅ |
| 246 | Mistral Small 3.2 | 0.1739 | 24B | — | small | ✅ | ❌ |
| 247 | Qwen3 235B (non-reasoning) | 0.1717 | 235B | 22B | large | ✅ | ❌ |
| 248 | Mistral Large 2 (Nov) | 0.1704 | 123B | — | medium | ✅ | ❌ |
| 249 | Gemma 4 E2B (non-reasoning) | 0.1692 | 5.1B | 2.3B | small | ✅ | ❌ |
| 250 | Qwen3 32B | 0.1690 | 32.8B | — | small | ✅ | ✅ |
| 251 | NVIDIA Nemotron Nano 9B V2 | 0.1667 | 9B | — | small | ✅ | ✅ |
| 252 | Llama 4 Scout | 0.1666 | 109B | 17B | medium | ✅ | ❌ |
| 253 | GLM-4.5V (non-reasoning) | 0.1657 | 108B | 12B | medium | ✅ | ❌ |
| 254 | Sarvam 30B (high) | 0.1655 | 32.2B | 2.4B | small | ✅ | ✅ |
| 255 | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1654 | 9B | — | small | ✅ | ❌ |
| 256 | Devstral Small | 0.1648 | 24B | — | small | ✅ | ❌ |
| 257 | Qwen3 4B 2507 (non-reasoning) | 0.1638 | 4.02B | — | tiny | ✅ | ❌ |
| 258 | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1615 | 13.2B | — | small | ✅ | ❌ |
| 259 | Command A | 0.1614 | 111B | — | medium | ✅ | ❌ |
| 260 | Ministral 3 8B | 0.1611 | 8B | — | small | ✅ | ❌ |
| 261 | Kimi Linear 48B A3B Instruct | 0.1597 | 49.1B | 3B | medium | ✅ | ❌ |
| 262 | MiniCPM-V 4.6 1.3B | 0.1575 | 1.3B | — | tiny | ✅ | ❌ |
| 263 | Qwen3 14B | 0.1572 | 14.8B | — | small | ✅ | ✅ |
| 264 | Magistral Small 1 | 0.1548 | 23.6B | — | small | ✅ | ✅ |
| 265 | Qwen3 VL 4B | 0.1548 | 4.44B | — | tiny | ✅ | ❌ |
| 266 | Nanbeige4.1-3B | 0.1528 | 3.93B | — | tiny | ✅ | ✅ |
| 267 | Gemma 4 E2B | 0.1523 | 5.1B | 2.3B | small | ✅ | ✅ |
| 268 | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1505 | 49B | — | medium | ✅ | ❌ |
| 269 | Olmo 3 32B Think | 0.1504 | 32.2B | — | small | ✅ | ✅ |
| 270 | EXAONE 4.0 32B (non-reasoning) | 0.1493 | 32B | — | small | ✅ | ❌ |
| 271 | Mistral Small 3 | 0.1480 | 24B | — | small | ✅ | ❌ |
| 272 | Nemotron 3 Nano (non-reasoning) | 0.1432 | 31.6B | 3.6B | small | ✅ | ❌ |
| 273 | Olmo 3.1 32B Instruct | 0.1420 | 32.2B | — | small | ✅ | ❌ |
| 274 | Llama 3.3 70B | 0.1387 | 70B | — | medium | ✅ | ❌ |
| 275 | Qwen3 30B (non-reasoning) | 0.1381 | 30.5B | 3.3B | small | ✅ | ❌ |
| 276 | Llama 3.1 Nemotron 70B | 0.1360 | 70B | — | medium | ✅ | ❌ |
| 277 | Jamba Reasoning 3B | 0.1347 | 3B | — | tiny | ✅ | ✅ |
| 278 | Granite 4.1 8B | 0.1329 | 8B | — | small | ✅ | ❌ |
| 279 | Jamba 1.7 Large | 0.1295 | 398B | 94B | large | ✅ | ❌ |
| 280 | Llama 3.1 70B | 0.1281 | 70B | — | medium | ✅ | ❌ |
| 281 | Qwen3 8B | 0.1275 | 8.19B | — | small | ✅ | ✅ |
| 282 | LFM2 24B A2B | 0.1263 | 23.8B | 2.3B | small | ✅ | ❌ |
| 283 | Ling-mini-2.0 | 0.1242 | 16.3B | 1.4B | small | ✅ | ❌ |
| 284 | Qwen3 14B (non-reasoning) | 0.1229 | 14.8B | — | small | ✅ | ❌ |
| 285 | Nemotron 3 Nano 4B | 0.1226 | 3.97B | — | tiny | ✅ | ✅ |
| 286 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1190 | 4.51B | — | small | ✅ | ✅ |
| 287 | Granite 4.0 H Small | 0.1182 | 32B | 9B | small | ✅ | ❌ |
| 288 | LFM2.5-2.6B | 0.1182 | 2.7B | — | tiny | ✅ | ✅ |
| 289 | Hermes 4 70B (non-reasoning) | 0.1153 | 70.6B | — | medium | ✅ | ❌ |
| 290 | Llama 3.2 3B | 0.1140 | 3B | — | tiny | ✅ | ❌ |
| 291 | DeepSeek R1 Distill Llama 70B | 0.1136 | 70B | — | medium | ✅ | ✅ |
| 292 | Olmo 3 7B Think | 0.1130 | 7B | — | small | ✅ | ✅ |
| 293 | LFM2.5-1.2B-Thinking | 0.1115 | 1.17B | — | tiny | ✅ | ✅ |
| 294 | DeepSeek R1 0528 Qwen3 8B | 0.1110 | 8.19B | — | small | ✅ | ✅ |
| 295 | Ministral 3 3B | 0.1068 | 3B | — | tiny | ✅ | ❌ |
| 296 | Gemma 3 27B | 0.1058 | 27.4B | — | small | ✅ | ❌ |
| 297 | Qwen3 8B (non-reasoning) | 0.1052 | 8.19B | — | small | ✅ | ❌ |
| 298 | LFM2.5-1.2B-Instruct | 0.1007 | 1.17B | — | tiny | ✅ | ❌ |
| 299 | Qwen3.5 0.8B (non-reasoning) | 0.0984 | 0.873B | — | tiny | ✅ | ❌ |
| 300 | Jamba 1.7 Mini | 0.0977 | 52B | 12B | medium | ✅ | ❌ |
| 301 | Exaone 4.0 1.2B | 0.0959 | 1.28B | — | tiny | ✅ | ✅ |
| 302 | Llama 3.2 11B (Vision) | 0.0917 | 11B | — | small | ✅ | ❌ |
| 303 | Exaone 4.0 1.2B (non-reasoning) | 0.0902 | 1.28B | — | tiny | ✅ | ❌ |
| 304 | Olmo 3 7B | 0.0900 | 7B | — | small | ✅ | ❌ |
| 305 | Molmo2-8B | 0.0883 | 8.66B | — | small | ✅ | ❌ |
| 306 | Qwen3 1.7B | 0.0872 | 2.03B | — | tiny | ✅ | ✅ |
| 307 | Phi-4 | 0.0851 | 14B | — | small | ✅ | ❌ |
| 308 | Reka Flash 3 | 0.0848 | 21B | — | small | ✅ | ✅ |
| 309 | Granite 4.1 3B | 0.0819 | 3B | — | tiny | ✅ | ❌ |
| 310 | OLMo 2 32B | 0.0806 | 32.2B | — | small | ✅ | ❌ |
| 311 | LFM2 8B A1B | 0.0769 | 8.34B | 1.5B | small | ✅ | ❌ |
| 312 | Gemma 3 12B | 0.0746 | 12.2B | — | small | ✅ | ❌ |
| 313 | Granite 4.0 Micro | 0.0745 | 3B | — | tiny | ✅ | ❌ |
| 314 | Llama 3 70B | 0.0740 | 70B | — | medium | ✅ | ❌ |
| 315 | Granite 4.0 H 1B | 0.0717 | 1.5B | — | tiny | ✅ | ❌ |
| 316 | LFM2.5-VL-1.6B | 0.0715 | 1.6B | — | tiny | ✅ | ❌ |
| 317 | Sarvam M | 0.0691 | 23.6B | — | small | ✅ | ✅ |
| 318 | Llama 3.1 8B | 0.0661 | 8B | — | small | ✅ | ❌ |
| 319 | Granite 4.0 1B | 0.0653 | 1.6B | — | tiny | ✅ | ❌ |
| 320 | Phi-3 Mini | 0.0638 | 3.8B | — | tiny | ✅ | ❌ |
| 321 | Granite 3.3 8B (non-reasoning) | 0.0634 | 8.17B | — | small | ✅ | ❌ |
| 322 | Qwen3 1.7B (non-reasoning) | 0.0556 | 2.03B | — | tiny | ✅ | ❌ |
| 323 | Qwen3.5 0.8B | 0.0551 | 0.873B | — | tiny | ✅ | ✅ |
| 324 | Gemma 3 4B | 0.0532 | 4.3B | — | tiny | ✅ | ❌ |
| 325 | Qwen3 0.6B | 0.0525 | 0.752B | — | tiny | ✅ | ✅ |
| 326 | Apertus 70B Instruct | 0.0505 | 70B | — | medium | ✅ | ❌ |
| 327 | LFM2 2.6B | 0.0454 | 2.57B | — | tiny | ✅ | ❌ |
| 328 | Phi-4 Mini | 0.0437 | 3.84B | — | tiny | ✅ | ❌ |
| 329 | OLMo 2 7B | 0.0417 | 7.3B | — | small | ✅ | ❌ |
| 330 | Gemma 3n E4B | 0.0403 | 8.39B | 4B | small | ✅ | ❌ |
| 331 | Apertus 8B Instruct | 0.0361 | 8B | — | small | ✅ | ❌ |
| 332 | Qwen3 0.6B (non-reasoning) | 0.0356 | 0.752B | — | tiny | ✅ | ❌ |
| 333 | Granite 4.0 H 350M | 0.0345 | 0.34B | — | tiny | ✅ | ❌ |
| 334 | LFM2 1.2B | 0.0336 | 1.17B | — | tiny | ✅ | ❌ |
| 335 | Molmo 7B-D | 0.0311 | 8.02B | — | small | ✅ | ❌ |
| 336 | Llama 3 8B | 0.0303 | 8B | — | small | ✅ | ❌ |
| 337 | Granite 4.0 350M | 0.0268 | 0.35B | — | tiny | ✅ | ❌ |
| 338 | Gemma 3 1B | 0.0268 | 1B | — | tiny | ✅ | ❌ |
| 339 | Tiny Aya Global | 0.0226 | 3.35B | — | tiny | ✅ | ❌ |
| 340 | Llama 3.2 1B | 0.0210 | 1B | — | tiny | ✅ | ❌ |
| 341 | K2 Horizon 0.9B | 0.0141 | 0.9B | — | tiny | ✅ | ✅ |
| 342 | Gemma 3n E2B | 0.0119 | 5.98B | 2B | small | ✅ | ❌ |
| 343 | Mistral 7B | 0.0035 | 7B | — | small | ✅ | ❌ |
| 344 | Gemma 3 270M | 0.0000 | 0.268B | — | tiny | ✅ | ❌ |

## 品牌帕累托前沿连线（仅体现在图中）

以下 10 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | `#00F5E7` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | `#4fb5ff` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 9 |
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 7 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | `#3B62EC` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | `#0f62fe` | 5 |

## 基准测试动态标定（Leave-One-Out Calibration）

不同基准测试的参测模型群体能力分布存在差异（例如部分高难度或专业领域基准测试仅覆盖头部高能力模型）。系统在标准归一化之后执行了**留一交叉动态映射标定流程**：

1. **排除单项基准**：暂时排除某项基准测试，计算各模型在其余测试项上的平均能力；
2. **全域归一化评估**：将排除后的平均能力归一化至 `[0, 1]`；
3. **锁定参测区间**：提取实际参测该基准测试的所有模型，以它们排除该项后的能力最高值和最低值分别作为该项的新映射上界和下界；
4. **并行同步迭代**：所有基准测试以 `[0, 1]` 为初值同步更新，完成一轮后以新上下界作为输入进入下一轮，重复迭代直至收敛。

> 标定状态：已完成 **14** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）。标定得到的数据作为新指标独立保存，不覆盖原始基准测试归一化与综合能力。

| 基准测试项 | 英文标识 | 参测模型数 | 标定映射下界 | 标定映射上界 | 映射跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 89 | `0.1772` | `1.0000` | `0.8228` |
| GPQA Diamond | `gpqa` | 535 | `0.0000` | `0.9180` | `0.9180` |
| Humanity's Last Exam | `hle` | 603 | `0.0000` | `0.9506` | `0.9506` |
| MMMU Pro | `mmmuPro` | 292 | `0.0168` | `0.9506` | `0.9337` |
| IFBench Instruction Following | `ifbench` | 442 | `0.0000` | `0.8963` | `0.8963` |
| SciCode Coding | `scicode` | 244 | `0.0406` | `0.9506` | `0.9099` |
| CritPt Physics | `critpt` | 591 | `0.0000` | `0.9531` | `0.9531` |
| AA-LCR Long Context | `lcr` | 582 | `0.0000` | `1.0000` | `1.0000` |
| AA Omniscience Index | `omniscience` | 107 | `0.1772` | `1.0000` | `0.8228` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 107 | `0.1726` | `1.0000` | `0.8274` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 107 | `0.1709` | `1.0000` | `0.8291` |
| GDPval-AA Normalized | `gdpvalNormalized` | 307 | `0.0406` | `1.0000` | `0.9594` |
| AA Analyst Agent | `analystAgent` | 51 | `0.3328` | `0.9539` | `0.6211` |
| APEX-Agents-AA | `apexAgents` | 33 | `0.3100` | `0.8189` | `0.5088` |
| ITBench-SRE | `itbenchSre` | 45 | `0.1542` | `0.9728` | `0.8186` |
| τ²-Bench Telecom | `tau2` | 438 | `0.0000` | `0.8956` | `0.8956` |
| τ³-Bench Banking | `tauBanking` | 209 | `0.0306` | `0.9229` | `0.8923` |
| Terminal-Bench Hard | `terminalbenchHard` | 431 | `0.0035` | `0.8852` | `0.8817` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 242 | `0.0393` | `0.9146` | `0.8753` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 236 | `0.0408` | `1.0000` | `0.9592` |


## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且总参数量 ≤，且至少一项严格更优；缺少参数量数据的模型不在图表和表格中）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.0000，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 0.25，r = B/C = 4.0008），用 11 品牌前沿入图模型的总参数量定出；mse = 0.003229，maxdev = 0.1045。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 71，10B–100B: 110，100B–1T: 140，1T–2.8T: 11
- 中位数位置 0.567；左 115 个，右 229 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.173，10^1→ 0.398，10^2→ 0.643，10^3→ 0.890

## 图中标注规则

品牌帕累托前沿模型全部标注。V13/V15/V16 规则：

1. **品牌公共前缀剔除（最长有效切点）**：品牌全部前沿模型共享的前导块被剔除 —— 切点须止于分界符（空格/连字符/下划线，如 'Claude '、'GPT-'、'GLM-'、'Grok '、'DeepSeek V4 '），或止于字母且每个名称在切点后紧跟数字（品牌/系列字母 + 版本号，如 'Kimi K|2.6'、'Qwen|3.8'、'MiMo-V|2.5'、'MiniMax-M|2.1'）—— 实例：Claude Opus 5 (high) → Opus 5 (high)、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5-Pro → 2.5-Pro；剔除后任一名称为空或产生重复标签则该切点作废，顺次尝试更短切点；
2. **(non-reasoning) → (non)**：思考程度中的 Non-reasoning 简写为 non（含组合式：Non-reasoning, high → non, high）；
3. **相邻同名 run 短标签（每次重新计算）**：品牌连线上连续 2 个以上顶点属于同一模型时，仅性能最低者（run 首位）保留全名，其后相邻的较高者只标思考程度（如 Opus 5 的 (low) (medium) (high) (xhigh) 序列仅首项带族名）；同名模型不相邻的重复出现不合并、保留全名 —— A-B(high)-B(xhigh)-C-B(max) 标注为 A-B(high)-(xhigh)-C-B(max)，因此交错家族（Gemini 3.7 / 3.8 Flash、Claude Fable 5.1 / Opus 5）始终可分辨。

4. **标签位置与序列同向（V15）**：品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上 —— 对前沿相邻对 A→B（B 更靠右上），标签位移的两个分量须同时 >= 0（至少是 (0,0)），既不得更左、也不得更低（只要有一个分量非负不算合格；V14 的投影规则会放过「更右但更低」，V15 起视为违反；等参数堆叠即：上方模型的标签既在上方、也不更左）；初始放置违反时就近重摆（不产生新的重叠、不破坏与前后邻居的同向关系，最多 6 轮；单标签重摆无解——标签被前后邻居夹死、局部约束盒为空——时，自动升级为以违规对为中心逐级扩大的窗口级联重排，整段相邻标签作为一个阶梯整体重排，修不好的配对在日志中报告）。

5. **标签摆放四级优先（V16）**：① 尽量多的标签骑在连线段上——点的右侧（去路段）或左侧（来路段）皆可，同一条线段允许容纳两个标签（各贴各的点）；目标骑线位仅被其他标签占据时触发「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线。② 骑不上线的标签在「假设线能放下该标签」的离点最近位置的上方或下方、与线平行摆放（右/左侧 × 上/下方四组合；互相掣肘的标签自然错开成对角组合）。③ 仍放不下时放在点的两条连线延长线上的最近点。④ 最后在两条连线夹角形成的扇区（连线前上方空白区）内就近放置，文字保持与邻近连线平行。

标注文字与连线平行且中轴线重合；文字下方不绘制连线，仅在文字两侧绘制（若两侧仍有区域）；文字使用品牌颜色，无边框、无背景。

## X：模型总参数量

**X = 模型总参数量（单位B；MoE 用总数）**

总参数量是详情页 FAQ 数据；缺少参数量数据的模型不在图表和表格中。

### 数据来源

**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)（Status: All）  
**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  
**模型数（有参数量数据）**: 344（总体帕累托前沿 19 个；图表入图 344 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 10 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.0000，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 0 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
