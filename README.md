# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.1245，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 286 个入图，52 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | GLM-5.3 (max) | 0.8541 | 753B | 40B | large | ✅ | ✅ |
| 2 | Kimi K3 (max) | 0.8415 | 2.8T | 104B | large | ✅ | ✅ |
| 3 | MiMo-V2.6-Pro | 0.8226 | 1T | 42B | large | ✅ | ✅ |
| 4 | Step 5 Preview | 0.8178 | 600B | — | large | ❌ | ✅ |
| 5 | GLM-5.3-Flash | 0.8084 | 320B | 18B | large | ✅ | ✅ |
| 6 | Qwen3.8 2.4T A95B | 0.7741 | 2.4T | 95B | large | ✅ | ✅ |
| 7 | GLM-5.2 (max) | 0.7543 | 753B | 40B | large | ✅ | ✅ |
| 8 | Qwen3.8-Flash-Next | 0.7493 | 180B | 6B | large | ✅ | ✅ |
| 9 | DeepSeek V4 Pro 0813 (max) | 0.7018 | 1.6T | 49B | large | ✅ | ✅ |
| 10 | DeepSeek V4.1 Flash (max) | 0.6953 | 552B | 16B | large | ✅ | ✅ |
| 11 | Motif 3 | 0.6789 | 314B | 13.2B | large | ✅ | ✅ |
| 12 | Qwen3.8 27B (xhigh) | 0.6752 | 27B | — | small | ✅ | ✅ |
| 13 | Kimi K2.6 | 0.6729 | 1T | 32B | large | ✅ | ✅ |
| 14 | DeepSeek V4 Flash Vision (max) | 0.6660 | 284B | — | large | ❌ | ✅ |
| 15 | DeepSeek V4 Flash 0731 (max) | 0.6659 | 284B | 13B | large | ✅ | ✅ |
| 16 | DeepSeek V4 Pro (high) | 0.6571 | 1.6T | 49B | large | ✅ | ✅ |
| 17 | GLM-5 | 0.6453 | 744B | 40B | large | ✅ | ✅ |
| 18 | JT-4.1 Flash 236B A21B | 0.6448 | 236B | — | large | ❌ | ✅ |
| 19 | Kimi K3 (low) | 0.6441 | 2.8T | 104B | large | ✅ | ✅ |
| 20 | DeepSeek V4 Pro (max) | 0.6437 | 1.6T | 49B | large | ✅ | ✅ |
| 21 | MiMo-V2.6-Flash | 0.6432 | 309B | 15B | large | ✅ | ✅ |
| 22 | MiniMax-M3 | 0.6415 | 428B | 23B | large | ✅ | ✅ |
| 23 | GLM-5.1 | 0.6218 | 744B | 40B | large | ✅ | ✅ |
| 24 | Motif 3 (Beta) | 0.6110 | 314B | — | large | ❌ | ✅ |
| 25 | K2 Horizon 375B A23B | 0.6069 | 375B | 23B | large | ✅ | ✅ |
| 26 | GLM-5.3 (low) | 0.6058 | 753B | 40B | large | ✅ | ✅ |
| 27 | Kimi K2.7 Code | 0.6043 | 1T | 32B | large | ✅ | ✅ |
| 28 | Nex-N2-Pro | 0.6031 | 397B | 17B | large | ✅ | ✅ |
| 29 | Qwen3.5 27B | 0.5905 | 27.8B | — | small | ✅ | ✅ |
| 30 | MiMo-V2-Flash (Feb 2026) | 0.5902 | 309B | 15B | large | ✅ | ✅ |
| 31 | MiMo-V2.5-Pro | 0.5867 | 1T | 42B | large | ✅ | ✅ |
| 32 | Solar Open2 250B | 0.5854 | 250B | 15B | large | ✅ | ✅ |
| 33 | DeepSeek V4 Flash (max) | 0.5820 | 284B | 13B | large | ✅ | ✅ |
| 34 | Ling-3.0-flash-VL | 0.5807 | 124B | 5.5B | medium | ✅ | ✅ |
| 35 | MiMo-V2.5 | 0.5798 | 310B | 15B | large | ✅ | ✅ |
| 36 | Kimi K2.5 | 0.5788 | 1T | 32B | large | ✅ | ✅ |
| 37 | Kimi K2 Thinking | 0.5734 | 1T | 32B | large | ✅ | ✅ |
| 38 | Inkling (xhigh) | 0.5676 | 975B | 41B | large | ✅ | ✅ |
| 39 | Kimi K2.6 (non-reasoning) | 0.5663 | 1T | 32B | large | ✅ | ❌ |
| 40 | Inkling Small | 0.5618 | 266B | 12B | large | ✅ | ✅ |
| 41 | Quasar 438B (max) | 0.5608 | 438B | — | large | ❌ | ✅ |
| 42 | DeepSeek V4 Flash (high) | 0.5576 | 284B | 13B | large | ✅ | ✅ |
| 43 | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5562 | 236B | — | large | ❌ | ❌ |
| 44 | Qwen3.6 27B | 0.5559 | 27.8B | — | small | ✅ | ✅ |
| 45 | Hy3-preview | 0.5528 | 295B | 21B | large | ✅ | ✅ |
| 46 | MiniMax-M2.5 | 0.5475 | 230B | 10B | large | ✅ | ✅ |
| 47 | Qwen3.8 27B (medium) | 0.5468 | 27B | — | small | ✅ | ✅ |
| 48 | GLM-5.1 (non-reasoning) | 0.5463 | 744B | 40B | large | ✅ | ❌ |
| 49 | Nemotron 3 Ultra | 0.5462 | 550B | 55B | large | ✅ | ✅ |
| 50 | Qwen3.5 397B A17B | 0.5384 | 397B | 17B | large | ✅ | ✅ |
| 51 | A.X-K2 | 0.5328 | 692B | 33B | large | ✅ | ✅ |
| 52 | Qwen3.8 27B (low) | 0.5324 | 27B | — | small | ✅ | ✅ |
| 53 | MiniMax-M2.1 | 0.5323 | 230B | 10B | large | ✅ | ✅ |
| 54 | MiniMax-M2.7 | 0.5320 | 230B | 10B | large | ✅ | ✅ |
| 55 | Hy3 | 0.5291 | 299B | 21B | large | ✅ | ✅ |
| 56 | Qwen3.5 35B A3B | 0.5269 | 36B | 3B | small | ✅ | ✅ |
| 57 | Step 3.7 Flash | 0.5227 | 198B | 11B | large | ✅ | ✅ |
| 58 | Kimi K2.5 (non-reasoning) | 0.5216 | 1T | 32B | large | ✅ | ❌ |
| 59 | MiMo-V2-Flash | 0.5203 | 309B | 15B | large | ✅ | ✅ |
| 60 | K2 Horizon MoVA 36B A4B | 0.5184 | 36B | 4B | small | ✅ | ✅ |
| 61 | GLM-4.7 | 0.5154 | 357B | 32B | large | ✅ | ✅ |
| 62 | DeepSeek V3.2 | 0.5146 | 685B | 37B | large | ✅ | ✅ |
| 63 | GLM-5 (non-reasoning) | 0.5104 | 744B | 40B | large | ✅ | ❌ |
| 64 | G9v3-39A5B | 0.5104 | 39B | 5B | small | ✅ | ✅ |
| 65 | Qwen3.6 35B A3B | 0.5080 | 36B | 3B | small | ✅ | ✅ |
| 66 | Qwen3.5 397B A17B (non-reasoning) | 0.5037 | 397B | 17B | large | ✅ | ❌ |
| 67 | Qwen3.5 122B A10B | 0.4993 | 125B | 10B | medium | ✅ | ✅ |
| 68 | Qwen3.5 27B (non-reasoning) | 0.4888 | 27.8B | — | small | ✅ | ❌ |
| 69 | DeepSeek V3.2 Speciale | 0.4876 | 685B | 37B | large | ✅ | ✅ |
| 70 | JT-35B-Flash | 0.4866 | 35B | — | small | ❌ | ❌ |
| 71 | Step 3.5 Flash | 0.4858 | 196B | 11B | large | ✅ | ✅ |
| 72 | Ling-3.0-flash-Fin | 0.4839 | 124B | 5.1B | medium | ✅ | ✅ |
| 73 | K-EXAONE 2.0 | 0.4828 | 750B | 37B | large | ✅ | ✅ |
| 74 | Ling 3.0 Flash | 0.4795 | 124B | 5.1B | medium | ✅ | ✅ |
| 75 | Qwen3.8 27B (non-reasoning) | 0.4765 | 27B | — | small | ✅ | ❌ |
| 76 | Gemma 4 31B | 0.4764 | 30.7B | — | small | ✅ | ✅ |
| 77 | MiniMax-M2 | 0.4732 | 230B | 10B | large | ✅ | ✅ |
| 78 | Muse Glimmer (high) | 0.4685 | 30B | — | small | ✅ | ✅ |
| 79 | Solar Mini 4 | 0.4680 | 35B | — | small | ❌ | ✅ |
| 80 | GLM-5.2 (non-reasoning) | 0.4611 | 753B | 40B | large | ✅ | ❌ |
| 81 | DeepSeek V4 Pro (non-reasoning) | 0.4584 | 1.6T | 49B | large | ✅ | ❌ |
| 82 | Qwen3.6 27B (non-reasoning) | 0.4555 | 27.8B | — | small | ✅ | ❌ |
| 83 | Mistral Medium 3.5 | 0.4483 | 128B | — | medium | ✅ | ✅ |
| 84 | Ring-2.6-1T | 0.4471 | 1T | 63B | large | ✅ | ✅ |
| 85 | DeepSeek V3.2 Exp | 0.4414 | 685B | 37B | large | ✅ | ✅ |
| 86 | DeepSeek V4.1 Flash (non-reasoning) | 0.4373 | 552B | 16B | large | ✅ | ❌ |
| 87 | Command A+ | 0.4364 | 218B | 25B | large | ✅ | ✅ |
| 88 | Qwen3.5 122B A10B (non-reasoning) | 0.4353 | 125B | 10B | medium | ✅ | ❌ |
| 89 | K2 Horizon 7B | 0.4333 | 7B | — | small | ✅ | ✅ |
| 90 | LongCat 2.0 | 0.4204 | 1.6T | 48B | large | ✅ | ✅ |
| 91 | MiMo-V2.5-Pro (non-reasoning) | 0.4198 | 1T | 42B | large | ✅ | ❌ |
| 92 | Kimi K2 0905 | 0.4169 | 1T | 32B | large | ✅ | ❌ |
| 93 | Gemma 4 26B A4B | 0.4168 | 25.2B | 3.8B | small | ✅ | ✅ |
| 94 | DeepSeek V4 Flash (non-reasoning) | 0.4157 | 284B | 13B | large | ✅ | ❌ |
| 95 | Qwen3 VL 235B A22B | 0.4156 | 235B | 22B | large | ✅ | ✅ |
| 96 | DeepSeek V3.1 Terminus | 0.4137 | 685B | 37B | large | ✅ | ✅ |
| 97 | Ling-2.6-1T | 0.4128 | 1T | 63B | large | ✅ | ❌ |
| 98 | DeepSeek V3.2 (non-reasoning) | 0.4070 | 685B | 37B | large | ✅ | ❌ |
| 99 | Hy3-preview (non-reasoning) | 0.4052 | 295B | 21B | large | ✅ | ❌ |
| 100 | GLM-4.7 (non-reasoning) | 0.4022 | 357B | 32B | large | ✅ | ❌ |
| 101 | Qwen3.6 35B A3B (non-reasoning) | 0.4007 | 36B | 3B | small | ✅ | ❌ |
| 102 | Qwen3.5 4B | 0.3972 | 4.66B | — | small | ✅ | ✅ |
| 103 | GLM-4.6 | 0.3955 | 357B | 32B | large | ✅ | ✅ |
| 104 | EXAONE 4.5 33B | 0.3939 | 34.4B | — | small | ✅ | ✅ |
| 105 | DeepSeek V3.1 | 0.3936 | 685B | 37B | large | ✅ | ✅ |
| 106 | GLM-4.5 | 0.3930 | 355B | 32B | large | ✅ | ✅ |
| 107 | Gemma 4 12B | 0.3886 | 12B | — | small | ✅ | ✅ |
| 108 | Qwen3.5 9B | 0.3879 | 9.65B | — | small | ✅ | ✅ |
| 109 | Kimi K2 | 0.3834 | 1T | 32B | large | ✅ | ❌ |
| 110 | DeepSeek R1 0528 | 0.3820 | 685B | 37B | large | ✅ | ✅ |
| 111 | K-EXAONE | 0.3787 | 236B | 23B | large | ✅ | ✅ |
| 112 | Gemma 4 31B (non-reasoning) | 0.3750 | 30.7B | — | small | ✅ | ❌ |
| 113 | Qwen3 VL 32B | 0.3727 | 33.4B | — | small | ✅ | ✅ |
| 114 | Qwen3.5 35B A3B (non-reasoning) | 0.3723 | 36B | 3B | small | ✅ | ❌ |
| 115 | MiMo-V2-Flash (non-reasoning) | 0.3696 | 309B | 15B | large | ✅ | ❌ |
| 116 | GLM-4.7-Flash | 0.3686 | 31.2B | 3B | small | ✅ | ✅ |
| 117 | GLM-4.6 (non-reasoning) | 0.3651 | 357B | 32B | large | ✅ | ❌ |
| 118 | Granite 4.2 30B | 0.3649 | 30B | — | small | ✅ | ✅ |
| 119 | Apriel-v1.5-15B-Thinker | 0.3613 | 15B | — | small | ✅ | ✅ |
| 120 | Qwen3.5 9B (non-reasoning) | 0.3586 | 9.65B | — | small | ✅ | ❌ |
| 121 | Qwen3 Coder 480B | 0.3563 | 480B | 35B | large | ✅ | ❌ |
| 122 | Cogito v2.1 | 0.3550 | 671B | 37B | large | ✅ | ✅ |
| 123 | Nemotron 3 Super | 0.3544 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 124 | Apriel-v1.6-15B-Thinker | 0.3510 | 15B | — | small | ✅ | ✅ |
| 125 | Gemma 4 26B A4B (non-reasoning) | 0.3499 | 25.2B | 3.8B | small | ✅ | ❌ |
| 126 | GLM-4.6V | 0.3486 | 108B | 12B | medium | ✅ | ✅ |
| 127 | DeepSeek V3.1 Terminus (non-reasoning) | 0.3480 | 685B | 37B | large | ✅ | ❌ |
| 128 | Nemotron Cascade 2 30B A3B | 0.3454 | 31.6B | 3B | small | ✅ | ✅ |
| 129 | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3432 | 1.6T | 49B | large | ✅ | ❌ |
| 130 | K2 Horizon 3.7B | 0.3379 | 3.7B | — | tiny | ✅ | ✅ |
| 131 | Trinity Large Thinking | 0.3378 | 399B | 13B | large | ✅ | ✅ |
| 132 | MiniCPM5-2B | 0.3312 | 2.6B | — | tiny | ✅ | ✅ |
| 133 | DeepSeek V3.2 Exp (non-reasoning) | 0.3304 | 685B | 37B | large | ✅ | ❌ |
| 134 | Nemotron 3.5 Lightning | 0.3277 | 31.6B | 3.6B | small | ✅ | ✅ |
| 135 | DeepSeek V3.1 (non-reasoning) | 0.3272 | 685B | 37B | large | ✅ | ❌ |
| 136 | Ling 3.0 Tiny | 0.3267 | 7.9B | 1.3B | small | ✅ | ✅ |
| 137 | gpt-oss-120b (high) | 0.3236 | 117B | 5.1B | medium | ✅ | ✅ |
| 138 | Seed-OSS-36B-Instruct | 0.3234 | 36.2B | — | small | ✅ | ✅ |
| 139 | Qwen3 235B A22B 2507 | 0.3206 | 235B | 22B | large | ✅ | ✅ |
| 140 | G9v3-3B | 0.3163 | 3B | — | tiny | ✅ | ✅ |
| 141 | Qwen3 235B 2507 | 0.3160 | 235B | 22B | large | ✅ | ❌ |
| 142 | North Mini Code | 0.3086 | 30B | 3B | small | ✅ | ✅ |
| 143 | Mistral Small 4 | 0.3082 | 119B | 6.5B | medium | ✅ | ✅ |
| 144 | Gemma 4 12B (non-reasoning) | 0.3076 | 12B | — | small | ✅ | ❌ |
| 145 | Qwen3 VL 235B A22B | 0.3069 | 235B | — | large | ✅ | ❌ |
| 146 | QwQ-32B | 0.3051 | 32.8B | — | small | ✅ | ✅ |
| 147 | Ring-1T | 0.3041 | 1T | 50B | large | ✅ | ✅ |
| 148 | MiniCPM5-1B | 0.3040 | 1B | — | tiny | ✅ | ✅ |
| 149 | MiniCPM5-1B (non-reasoning) | 0.3039 | 1B | — | tiny | ✅ | ❌ |
| 150 | K2 Think V2 | 0.3032 | 70B | — | medium | ✅ | ✅ |
| 151 | Pixtral Large | 0.3027 | 124B | — | medium | ✅ | ❌ |
| 152 | Solar Open 100B | 0.2993 | 102B | 12B | medium | ✅ | ✅ |
| 153 | HyperNova 60B 2605 (high) | 0.2965 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 154 | GLM-4.5-Air | 0.2959 | 106B | 12B | medium | ✅ | ✅ |
| 155 | MiniMax M1 80k | 0.2957 | 456B | 45.9B | large | ✅ | ✅ |
| 156 | Qwen3.5 4B (non-reasoning) | 0.2928 | 4.66B | — | small | ✅ | ❌ |
| 157 | Qwen3 Next 80B A3B | 0.2909 | 80B | 3B | medium | ✅ | ✅ |
| 158 | MiniMax M1 40k | 0.2888 | 456B | 45.9B | large | ✅ | ✅ |
| 159 | HyperCLOVA X SEED Think (32B) | 0.2887 | 32B | — | small | ✅ | ✅ |
| 160 | K2-V2 (high) | 0.2865 | 70B | — | medium | ✅ | ✅ |
| 161 | K-EXAONE (non-reasoning) | 0.2862 | 236B | 23B | large | ✅ | ❌ |
| 162 | Qwen3 Coder Next | 0.2857 | 79.7B | 3B | medium | ✅ | ❌ |
| 163 | Solar Pro 3 | 0.2831 | 102B | — | medium | ❌ | ✅ |
| 164 | Granite 4.2 8B | 0.2821 | 8B | — | small | ✅ | ✅ |
| 165 | INTELLECT-3 | 0.2767 | 107B | 12B | medium | ✅ | ✅ |
| 166 | DiffusionGemma 26B A4B | 0.2766 | 25.2B | 3.8B | small | ✅ | ✅ |
| 167 | Tri-21B-think Preview | 0.2759 | 21B | — | small | ✅ | ✅ |
| 168 | LongCat Flash Lite | 0.2743 | 68.5B | 3B | medium | ✅ | ❌ |
| 169 | Qwen3 VL 30B A3B | 0.2739 | 30B | 3B | small | ✅ | ✅ |
| 170 | gpt-oss-20b (low) | 0.2735 | 21B | 3.6B | small | ✅ | ✅ |
| 171 | Llama 3.1 405B | 0.2724 | 405B | — | large | ✅ | ❌ |
| 172 | Ling 2.6 Flash | 0.2711 | 107B | 7.4B | medium | ✅ | ❌ |
| 173 | Nemotron 3 Nano | 0.2705 | 31.6B | 3.6B | small | ✅ | ✅ |
| 174 | Gemma 4 E4B (non-reasoning) | 0.2704 | 8B | 4.5B | small | ✅ | ❌ |
| 175 | Tri-21B-Think | 0.2702 | 21B | — | small | ✅ | ✅ |
| 176 | Qwen3 Next 80B A3B | 0.2623 | 80B | 3B | medium | ✅ | ❌ |
| 177 | Qwen3 VL 32B | 0.2620 | 33.4B | — | small | ✅ | ❌ |
| 178 | Nemotron 3 Nano Omni 30B A3B | 0.2606 | 30B | 3B | small | ✅ | ✅ |
| 179 | Hermes 4 405B | 0.2604 | 406B | — | large | ✅ | ✅ |
| 180 | DeepSeek R1 (Jan) | 0.2587 | 685B | 37B | large | ✅ | ✅ |
| 181 | K2-V2 (medium) | 0.2579 | 70B | — | medium | ✅ | ✅ |
| 182 | Ling-1T | 0.2570 | 1T | 50B | large | ✅ | ❌ |
| 183 | DeepSeek V3 0324 | 0.2569 | 671B | 37B | large | ✅ | ❌ |
| 184 | Motif-2-12.7B | 0.2565 | 12.7B | — | small | ❌ | ✅ |
| 185 | Mistral Large 3 | 0.2544 | 675B | 41B | large | ✅ | ❌ |
| 186 | Gemma 4 E4B | 0.2537 | 8B | 4.5B | small | ✅ | ✅ |
| 187 | Qwen3 VL 8B | 0.2534 | 8.77B | — | small | ✅ | ✅ |
| 188 | gpt-oss-20b (high) | 0.2519 | 21B | 3.6B | small | ✅ | ✅ |
| 189 | Step3 VL 10B | 0.2516 | 10.2B | — | small | ✅ | ✅ |
| 190 | Llama 4 Maverick | 0.2502 | 402B | 17B | large | ✅ | ❌ |
| 191 | Llama Nemotron Super 49B v1.5 | 0.2495 | 49B | — | medium | ✅ | ✅ |
| 192 | GLM-4.7-Flash (non-reasoning) | 0.2491 | 31.2B | 3B | small | ✅ | ❌ |
| 193 | gpt-oss-120b (low) | 0.2483 | 117B | 5.1B | medium | ✅ | ✅ |
| 194 | ERNIE 4.5 300B A47B | 0.2464 | 300B | 47B | large | ✅ | ❌ |
| 195 | Qwen3 4B 2507 | 0.2433 | 4.02B | — | tiny | ✅ | ✅ |
| 196 | Mistral Small 4 (non-reasoning) | 0.2422 | 119B | 6.5B | medium | ✅ | ❌ |
| 197 | Hermes 4 405B (non-reasoning) | 0.2411 | 406B | — | large | ✅ | ❌ |
| 198 | Qwen3 Coder 30B A3B | 0.2398 | 30.5B | 3.3B | small | ✅ | ❌ |
| 199 | Qwen3 30B A3B 2507 | 0.2377 | 30.5B | 3.3B | small | ✅ | ✅ |
| 200 | LFM2.5-8B-A1B | 0.2375 | 8.3B | 1.5B | small | ✅ | ✅ |
| 201 | Qwen3 VL 30B A3B | 0.2367 | 30B | 3B | small | ✅ | ❌ |
| 202 | Devstral 2 | 0.2365 | 125B | — | medium | ✅ | ❌ |
| 203 | GLM-4.6V (non-reasoning) | 0.2361 | 108B | 12B | medium | ✅ | ❌ |
| 204 | Qwen3 Omni 30B A3B | 0.2342 | 35.3B | 3B | small | ✅ | ✅ |
| 205 | Granite 4.2 3B | 0.2337 | 3B | — | tiny | ✅ | ✅ |
| 206 | Qwen3 235B | 0.2301 | 235B | 22B | large | ✅ | ✅ |
| 207 | GLM-4.5V | 0.2294 | 108B | 12B | medium | ✅ | ✅ |
| 208 | NVIDIA Nemotron Nano 12B v2 VL | 0.2287 | 13.2B | — | small | ✅ | ✅ |
| 209 | Mistral Large 2 (Nov) | 0.2277 | 123B | — | medium | ✅ | ❌ |
| 210 | Falcon-H1R-7B | 0.2262 | 7B | — | small | ✅ | ✅ |
| 211 | Llama Nemotron Ultra | 0.2253 | 253B | — | large | ✅ | ✅ |
| 212 | Gemma 4 E2B | 0.2164 | 5.1B | 2.3B | small | ✅ | ✅ |
| 213 | Devstral Small 2 | 0.2161 | 24B | — | small | ✅ | ❌ |
| 214 | LFM2.5-2.6B | 0.2157 | 2.7B | — | tiny | ✅ | ✅ |
| 215 | Olmo 3.1 32B Think | 0.2155 | 32.2B | — | small | ✅ | ✅ |
| 216 | Sarvam 105B (high) | 0.2146 | 106B | 10.3B | medium | ✅ | ✅ |
| 217 | EXAONE 4.0 32B | 0.2136 | 32B | — | small | ✅ | ✅ |
| 218 | K2-V2 (low) | 0.2122 | 70B | — | medium | ✅ | ✅ |
| 219 | NVIDIA Nemotron Nano 9B V2 | 0.2116 | 9B | — | small | ✅ | ✅ |
| 220 | Ring-flash-2.0 | 0.2091 | 103B | 6.1B | medium | ✅ | ✅ |
| 221 | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.2074 | 49B | — | medium | ✅ | ❌ |
| 222 | Hermes 4 70B | 0.2054 | 70.6B | — | medium | ✅ | ✅ |
| 223 | Devstral Small (May) | 0.2044 | 23.6B | — | small | ✅ | ❌ |
| 224 | Magistral Small 1.2 | 0.2009 | 24B | — | small | ✅ | ✅ |
| 225 | Llama 3.3 Nemotron Super 49B | 0.2007 | 49B | — | medium | ✅ | ✅ |
| 226 | DeepSeek R1 Distill Qwen 32B | 0.2004 | 32B | — | small | ✅ | ✅ |
| 227 | DeepSeek V3 (Dec) | 0.2001 | 671B | 37B | large | ✅ | ❌ |
| 228 | Qwen2.5 72B | 0.1997 | 72B | — | medium | ✅ | ❌ |
| 229 | Ling-flash-2.0 | 0.1989 | 103B | 6.1B | medium | ✅ | ❌ |
| 230 | Nanbeige4.1-3B | 0.1986 | 3.93B | — | tiny | ✅ | ✅ |
| 231 | Qwen3 VL 8B | 0.1983 | 8.77B | — | small | ✅ | ❌ |
| 232 | Qwen3.5 2B | 0.1973 | 2.27B | — | tiny | ✅ | ✅ |
| 233 | Qwen3 30B | 0.1968 | 30.5B | 3.3B | small | ✅ | ✅ |
| 234 | Magistral Small 1 | 0.1964 | 23.6B | — | small | ✅ | ✅ |
| 235 | Mistral Large 2 (Jul) | 0.1925 | 123B | — | medium | ✅ | ❌ |
| 236 | Command A | 0.1916 | 111B | — | medium | ✅ | ❌ |
| 237 | Devstral Small | 0.1910 | 24B | — | small | ✅ | ❌ |
| 238 | Mistral Small 3.2 | 0.1909 | 24B | — | small | ✅ | ❌ |
| 239 | Qwen3 235B (non-reasoning) | 0.1907 | 235B | 22B | large | ✅ | ❌ |
| 240 | Llama 3.1 Nemotron 70B | 0.1894 | 70B | — | medium | ✅ | ❌ |
| 241 | Qwen3 VL 4B | 0.1868 | 4.44B | — | tiny | ✅ | ✅ |
| 242 | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1842 | 49B | — | medium | ✅ | ❌ |
| 243 | Qwen3 30B A3B 2507 (non-reasoning) | 0.1824 | 30.5B | 3.3B | small | ✅ | ❌ |
| 244 | Llama 4 Scout | 0.1820 | 109B | 17B | medium | ✅ | ❌ |
| 245 | Qwen3 4B | 0.1810 | 4.02B | — | tiny | ✅ | ✅ |
| 246 | Llama 3.1 70B | 0.1805 | 70B | — | medium | ✅ | ❌ |
| 247 | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1803 | 9B | — | small | ✅ | ❌ |
| 248 | Qwen3 32B | 0.1794 | 32.8B | — | small | ✅ | ✅ |
| 249 | Qwen3 32B (non-reasoning) | 0.1788 | 32.8B | — | small | ✅ | ❌ |
| 250 | GLM-4.5V (non-reasoning) | 0.1784 | 108B | 12B | medium | ✅ | ❌ |
| 251 | Gemma 4 E2B (non-reasoning) | 0.1783 | 5.1B | 2.3B | small | ✅ | ❌ |
| 252 | Qwen3 14B | 0.1747 | 14.8B | — | small | ✅ | ✅ |
| 253 | Ministral 3 14B | 0.1734 | 14B | — | small | ✅ | ❌ |
| 254 | Olmo 3.1 32B Instruct | 0.1729 | 32.2B | — | small | ✅ | ❌ |
| 255 | Qwen3 Omni 30B A3B | 0.1712 | 35.3B | 3B | small | ✅ | ❌ |
| 256 | Qwen3 4B 2507 (non-reasoning) | 0.1694 | 4.02B | — | tiny | ✅ | ❌ |
| 257 | Olmo 3 32B Think | 0.1652 | 32.2B | — | small | ✅ | ✅ |
| 258 | DeepSeek R1 Distill Llama 70B | 0.1644 | 70B | — | medium | ✅ | ✅ |
| 259 | DeepSeek R1 Distill Qwen 14B | 0.1640 | 14B | — | small | ✅ | ✅ |
| 260 | Kimi Linear 48B A3B Instruct | 0.1637 | 49.1B | 3B | medium | ✅ | ❌ |
| 261 | Granite 4.1 30B | 0.1630 | 30B | — | small | ✅ | ❌ |
| 262 | Qwen3.5 2B (non-reasoning) | 0.1621 | 2.27B | — | tiny | ✅ | ❌ |
| 263 | Nemotron 3 Nano 4B | 0.1608 | 3.97B | — | tiny | ✅ | ✅ |
| 264 | Hermes 4 70B (non-reasoning) | 0.1591 | 70.6B | — | medium | ✅ | ❌ |
| 265 | Jamba Reasoning 3B | 0.1588 | 3B | — | tiny | ✅ | ✅ |
| 266 | EXAONE 4.0 32B (non-reasoning) | 0.1567 | 32B | — | small | ✅ | ❌ |
| 267 | Llama 3.3 70B | 0.1549 | 70B | — | medium | ✅ | ❌ |
| 268 | Llama 3.1 8B | 0.1541 | 8B | — | small | ✅ | ❌ |
| 269 | LFM2 24B A2B | 0.1534 | 23.8B | 2.3B | small | ✅ | ❌ |
| 270 | Jamba 1.7 Large | 0.1523 | 398B | 94B | large | ✅ | ❌ |
| 271 | Sarvam 30B (high) | 0.1503 | 32.2B | 2.4B | small | ✅ | ✅ |
| 272 | Mistral Small 3 | 0.1489 | 24B | — | small | ✅ | ❌ |
| 273 | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1486 | 13.2B | — | small | ✅ | ❌ |
| 274 | Granite 4.1 8B | 0.1449 | 8B | — | small | ✅ | ❌ |
| 275 | Qwen3 30B (non-reasoning) | 0.1441 | 30.5B | 3.3B | small | ✅ | ❌ |
| 276 | Ministral 3 8B | 0.1432 | 8B | — | small | ✅ | ❌ |
| 277 | Nemotron 3 Nano (non-reasoning) | 0.1415 | 31.6B | 3.6B | small | ✅ | ❌ |
| 278 | Granite 4.0 H Small | 0.1383 | 32B | 9B | small | ✅ | ❌ |
| 279 | Qwen3 VL 4B | 0.1379 | 4.44B | — | tiny | ✅ | ❌ |
| 280 | MiniCPM-V 4.6 1.3B | 0.1360 | 1.3B | — | tiny | ✅ | ❌ |
| 281 | DeepSeek R1 0528 Qwen3 8B | 0.1339 | 8.19B | — | small | ✅ | ✅ |
| 282 | Qwen3 14B (non-reasoning) | 0.1322 | 14.8B | — | small | ✅ | ❌ |
| 283 | Qwen3 8B | 0.1312 | 8.19B | — | small | ✅ | ✅ |
| 284 | Phi-4 | 0.1275 | 14B | — | small | ✅ | ❌ |
| 285 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1267 | 4.51B | — | small | ✅ | ✅ |
| 286 | Gemma 3 270M | 0.1245 | 0.268B | — | tiny | ✅ | ❌ |
| 287 | Gemma 3 27B | 0.1202 | 27.4B | — | small | ✅ | ❌ |
| 288 | Llama 3 70B | 0.1194 | 70B | — | medium | ✅ | ❌ |
| 289 | Llama 3.2 11B (Vision) | 0.1189 | 11B | — | small | ✅ | ❌ |
| 290 | Llama 3.2 3B | 0.1170 | 3B | — | tiny | ✅ | ❌ |
| 291 | Olmo 3 7B Think | 0.1155 | 7B | — | small | ✅ | ✅ |
| 292 | Ministral 3 3B | 0.1139 | 3B | — | tiny | ✅ | ❌ |
| 293 | LFM2.5-1.2B-Instruct | 0.1090 | 1.17B | — | tiny | ✅ | ❌ |
| 294 | Reka Flash 3 | 0.1085 | 21B | — | small | ✅ | ✅ |
| 295 | Ling-mini-2.0 | 0.1080 | 16.3B | 1.4B | small | ✅ | ❌ |
| 296 | LFM2 2.6B | 0.1080 | 2.57B | — | tiny | ✅ | ❌ |
| 297 | Qwen3 8B (non-reasoning) | 0.1070 | 8.19B | — | small | ✅ | ❌ |
| 298 | Qwen3.5 0.8B | 0.1060 | 0.873B | — | tiny | ✅ | ✅ |
| 299 | Molmo2-8B | 0.1037 | 8.66B | — | small | ✅ | ❌ |
| 300 | Sarvam M | 0.1035 | 23.6B | — | small | ✅ | ✅ |
| 301 | Jamba 1.7 Mini | 0.1023 | 52B | 12B | medium | ✅ | ❌ |
| 302 | LFM2.5-1.2B-Thinking | 0.1008 | 1.17B | — | tiny | ✅ | ✅ |
| 303 | Apertus 70B Instruct | 0.0940 | 70B | — | medium | ✅ | ❌ |
| 304 | Olmo 3 7B | 0.0926 | 7B | — | small | ✅ | ❌ |
| 305 | Exaone 4.0 1.2B | 0.0916 | 1.28B | — | tiny | ✅ | ✅ |
| 306 | OLMo 2 32B | 0.0914 | 32.2B | — | small | ✅ | ❌ |
| 307 | Granite 4.0 H 1B | 0.0910 | 1.5B | — | tiny | ✅ | ❌ |
| 308 | Llama 3.2 1B | 0.0899 | 1B | — | tiny | ✅ | ❌ |
| 309 | Phi-4 Mini | 0.0893 | 3.84B | — | tiny | ✅ | ❌ |
| 310 | Qwen3 1.7B | 0.0888 | 2.03B | — | tiny | ✅ | ✅ |
| 311 | Qwen3.5 0.8B (non-reasoning) | 0.0855 | 0.873B | — | tiny | ✅ | ❌ |
| 312 | Exaone 4.0 1.2B (non-reasoning) | 0.0846 | 1.28B | — | tiny | ✅ | ❌ |
| 313 | Gemma 3 12B | 0.0838 | 12.2B | — | small | ✅ | ❌ |
| 314 | LFM2 8B A1B | 0.0828 | 8.34B | 1.5B | small | ✅ | ❌ |
| 315 | Granite 4.0 Micro | 0.0802 | 3B | — | tiny | ✅ | ❌ |
| 316 | Granite 4.1 3B | 0.0795 | 3B | — | tiny | ✅ | ❌ |
| 317 | Phi-3 Mini | 0.0752 | 3.8B | — | tiny | ✅ | ❌ |
| 318 | Granite 3.3 8B (non-reasoning) | 0.0718 | 8.17B | — | small | ✅ | ❌ |
| 319 | LFM2.5-VL-1.6B | 0.0692 | 1.6B | — | tiny | ✅ | ❌ |
| 320 | Granite 4.0 1B | 0.0685 | 1.6B | — | tiny | ✅ | ❌ |
| 321 | Granite 4.0 350M | 0.0675 | 0.35B | — | tiny | ✅ | ❌ |
| 322 | LFM2 1.2B | 0.0657 | 1.17B | — | tiny | ✅ | ❌ |
| 323 | Qwen3 0.6B | 0.0651 | 0.752B | — | tiny | ✅ | ✅ |
| 324 | Llama 3 8B | 0.0648 | 8B | — | small | ✅ | ❌ |
| 325 | Mistral 7B | 0.0623 | 7B | — | small | ✅ | ❌ |
| 326 | Gemma 3 4B | 0.0604 | 4.3B | — | tiny | ✅ | ❌ |
| 327 | Qwen3 1.7B (non-reasoning) | 0.0569 | 2.03B | — | tiny | ✅ | ❌ |
| 328 | OLMo 2 7B | 0.0566 | 7.3B | — | small | ✅ | ❌ |
| 329 | Gemma 3 1B | 0.0563 | 1B | — | tiny | ✅ | ❌ |
| 330 | Apertus 8B Instruct | 0.0553 | 8B | — | small | ✅ | ❌ |
| 331 | Gemma 3n E4B | 0.0533 | 8.39B | 4B | small | ✅ | ❌ |
| 332 | Granite 4.0 H 350M | 0.0511 | 0.34B | — | tiny | ✅ | ❌ |
| 333 | Molmo 7B-D | 0.0479 | 8.02B | — | small | ✅ | ❌ |
| 334 | K2 Horizon 0.9B | 0.0458 | 0.9B | — | tiny | ✅ | ✅ |
| 335 | Qwen3 0.6B (non-reasoning) | 0.0439 | 0.752B | — | tiny | ✅ | ❌ |
| 336 | Gemma 3n E2B | 0.0362 | 5.98B | 2B | small | ✅ | ❌ |
| 337 | Tiny Aya Global | 0.0358 | 3.35B | — | tiny | ✅ | ❌ |
| 338 | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 1.5B | — | tiny | ✅ | ✅ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且总参数量 ≤，且至少一项严格更优；缺少参数量数据的模型不在图表和表格中）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.1245，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 1.84，r = B/C = 0.54343），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002233，maxdev = 0.1188。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 39，10B–100B: 103，100B–1T: 132，1T–2.8T: 9
- 中位数位置 0.518；左 131 个，右 155 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.059，10^1→ 0.254，10^2→ 0.548，10^3→ 0.860

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
**模型数（有参数量数据）**: 338（总体帕累托前沿 11 个；图表入图 286 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.1245，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 52 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
