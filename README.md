# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.0739，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 314 个入图，36 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3.1 Pro | 0.9566 | 2.8T | — | large | ❌ | ✅ |
| 2 | Qwen3.8 2.4T A95B | 0.7969 | 2.4T | 95B | large | ✅ | ✅ |
| 3 | Kimi K3 (max) | 0.7935 | 2.8T | 104B | large | ✅ | ✅ |
| 4 | DeepSeek V4.1 Flash 1017 (max) | 0.7697 | 552B | 16B | large | ✅ | ✅ |
| 5 | Qwen3.8-Flash-Next | 0.7522 | 180B | 6B | large | ✅ | ✅ |
| 6 | MiMo-V2.6-Pro | 0.7436 | 1T | 42B | large | ✅ | ✅ |
| 7 | Step 5 Preview | 0.7359 | 600B | — | large | ✅ | ✅ |
| 8 | GLM-5.3 (max) | 0.7200 | 753B | 40B | large | ✅ | ✅ |
| 9 | GLM-5.2 (max) | 0.7194 | 753B | 40B | large | ✅ | ✅ |
| 10 | Ling 3.1 Flash | 0.6968 | 560B | — | large | ✅ | ✅ |
| 11 | DeepSeek V4 Pro 0813 (max) | 0.6936 | 1.6T | 49B | large | ✅ | ✅ |
| 12 | DeepSeek V4 Flash Vision (max) | 0.6904 | 284B | — | large | ❌ | ✅ |
| 13 | Muse Spark Open (xhigh) | 0.6895 | 816B | 42B | large | ✅ | ✅ |
| 14 | GLM-5.3-Flash | 0.6831 | 320B | 18B | large | ✅ | ✅ |
| 15 | DeepSeek V4 Pro (high) | 0.6813 | 1.6T | 49B | large | ✅ | ✅ |
| 16 | DeepSeek V4 Flash 0731 (max) | 0.6721 | 284B | 13B | large | ✅ | ✅ |
| 17 | Motif 3 | 0.6581 | 314B | 13.2B | large | ✅ | ✅ |
| 18 | Qwen3.8 27B (xhigh) | 0.6558 | 27B | — | small | ✅ | ✅ |
| 19 | DeepSeek V4.1 Flash (max) | 0.6549 | 552B | 16B | large | ✅ | ✅ |
| 20 | GLM-5 | 0.6511 | 744B | 40B | large | ✅ | ✅ |
| 21 | Kimi K2 Thinking | 0.6502 | 1T | 32B | large | ✅ | ✅ |
| 22 | Motif 3 (Beta) | 0.6416 | 314B | — | large | ❌ | ✅ |
| 23 | DeepSeek V4 Pro (max) | 0.6376 | 1.6T | 49B | large | ✅ | ✅ |
| 24 | JT-4.1 Flash 236B A21B | 0.6342 | 236B | — | large | ❌ | ✅ |
| 25 | Kimi K2.6 | 0.6324 | 1T | 32B | large | ✅ | ✅ |
| 26 | MiMo-V2.6-Flash | 0.6157 | 309B | 15B | large | ✅ | ✅ |
| 27 | Mistral Large 4 Preview | 0.6069 | 1T | — | large | ❌ | ✅ |
| 28 | DeepSeek V3.2 | 0.6061 | 685B | 37B | large | ✅ | ✅ |
| 29 | MiMo-V2-Flash | 0.6052 | 309B | 15B | large | ✅ | ✅ |
| 30 | GLM-4.7 | 0.6046 | 357B | 32B | large | ✅ | ✅ |
| 31 | Kimi K2.5 | 0.6034 | 1T | 32B | large | ✅ | ✅ |
| 32 | Kimi K3 (low) | 0.5991 | 2.8T | 104B | large | ✅ | ✅ |
| 33 | GLM-5.1 | 0.5988 | 744B | 40B | large | ✅ | ✅ |
| 34 | MiniMax-M2.1 | 0.5976 | 230B | 10B | large | ✅ | ✅ |
| 35 | Solar Open2 250B | 0.5934 | 250B | 15B | large | ✅ | ✅ |
| 36 | Qwen3.5 27B | 0.5929 | 27.8B | — | small | ✅ | ✅ |
| 37 | MiMo-V2-Flash (Feb 2026) | 0.5924 | 309B | 15B | large | ✅ | ✅ |
| 38 | Nex-N2-Pro | 0.5833 | 397B | 17B | large | ✅ | ✅ |
| 39 | Kimi K2.7 Code | 0.5808 | 1T | 32B | large | ✅ | ✅ |
| 40 | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5798 | 236B | — | large | ❌ | ❌ |
| 41 | DeepSeek V3.2 Speciale | 0.5787 | 685B | 37B | large | ✅ | ✅ |
| 42 | DeepSeek V4 Flash (max) | 0.5772 | 284B | 13B | large | ✅ | ✅ |
| 43 | Kimi K2.6 (non-reasoning) | 0.5670 | 1T | 32B | large | ✅ | ❌ |
| 44 | GLM-5.3 (low) | 0.5564 | 753B | 40B | large | ✅ | ✅ |
| 45 | DeepSeek V4 Flash (high) | 0.5547 | 284B | 13B | large | ✅ | ✅ |
| 46 | Hy3-preview | 0.5524 | 295B | 21B | large | ✅ | ✅ |
| 47 | K2 Horizon 375B A23B | 0.5501 | 375B | 23B | large | ✅ | ✅ |
| 48 | MiniMax-M2.5 | 0.5469 | 230B | 10B | large | ✅ | ✅ |
| 49 | GLM-5.1 (non-reasoning) | 0.5458 | 744B | 40B | large | ✅ | ❌ |
| 50 | MiMo-V2.5 | 0.5427 | 310B | 15B | large | ✅ | ✅ |
| 51 | MiniMax-M2 | 0.5420 | 230B | 10B | large | ✅ | ✅ |
| 52 | MiMo-V2.5-Pro | 0.5347 | 1T | 42B | large | ✅ | ✅ |
| 53 | Step 3.7 Flash | 0.5293 | 198B | 11B | large | ✅ | ✅ |
| 54 | Ling-3.0-flash-VL | 0.5273 | 124B | 5.5B | medium | ✅ | ✅ |
| 55 | G9v3-39A5B | 0.5262 | 39B | 5B | small | ✅ | ✅ |
| 56 | Qwen3.5 35B A3B | 0.5251 | 36B | 3B | small | ✅ | ✅ |
| 57 | Quasar 438B (max) | 0.5214 | 438B | — | large | ❌ | ✅ |
| 58 | Qwen3.6 27B | 0.5202 | 27.8B | — | small | ✅ | ✅ |
| 59 | Kimi K2.5 (non-reasoning) | 0.5193 | 1T | 32B | large | ✅ | ❌ |
| 60 | DeepSeek V3.2 Exp | 0.5182 | 685B | 37B | large | ✅ | ✅ |
| 61 | MiniMax-M3 | 0.5172 | 428B | 23B | large | ✅ | ✅ |
| 62 | Hy3 | 0.5170 | 299B | 21B | large | ✅ | ✅ |
| 63 | Qwen3.8 27B (medium) | 0.5147 | 27B | — | small | ✅ | ✅ |
| 64 | Beam 1.0 | 0.5101 | 501B | 23B | large | ✅ | ✅ |
| 65 | GLM-5 (non-reasoning) | 0.5075 | 744B | 40B | large | ✅ | ❌ |
| 66 | K2 Horizon MoVA 36B A4B | 0.5050 | 36B | 4B | small | ✅ | ✅ |
| 67 | Qwen3.5 397B A17B (non-reasoning) | 0.5003 | 397B | 17B | large | ✅ | ❌ |
| 68 | Qwen3.5 397B A17B | 0.4964 | 397B | 17B | large | ✅ | ✅ |
| 69 | Qwen3.8 27B (low) | 0.4882 | 27B | — | small | ✅ | ✅ |
| 70 | K-EXAONE 2.0 | 0.4864 | 750B | 37B | large | ✅ | ✅ |
| 71 | Qwen3.5 27B (non-reasoning) | 0.4845 | 27.8B | — | small | ✅ | ❌ |
| 72 | JT-35B-Flash | 0.4822 | 35B | — | small | ❌ | ❌ |
| 73 | Step 3.5 Flash | 0.4811 | 196B | 11B | large | ✅ | ✅ |
| 74 | MiniMax-M2.7 | 0.4804 | 230B | 10B | large | ✅ | ✅ |
| 75 | K-EXAONE | 0.4766 | 236B | 23B | large | ✅ | ✅ |
| 76 | DeepSeek V3.1 | 0.4765 | 685B | 37B | large | ✅ | ✅ |
| 77 | Qwen3 VL 235B A22B | 0.4758 | 235B | 22B | large | ✅ | ✅ |
| 78 | GLM-4.6 | 0.4754 | 357B | 32B | large | ✅ | ✅ |
| 79 | GLM-5.2 (non-reasoning) | 0.4746 | 753B | 40B | large | ✅ | ❌ |
| 80 | Qwen3.6 27B (non-reasoning) | 0.4703 | 27.8B | — | small | ✅ | ❌ |
| 81 | Qwen3.6 35B A3B | 0.4578 | 36B | 3B | small | ✅ | ✅ |
| 82 | GLM-4.5 | 0.4564 | 355B | 32B | large | ✅ | ✅ |
| 83 | Qwen3.5 122B A10B (non-reasoning) | 0.4551 | 125B | 10B | medium | ✅ | ❌ |
| 84 | Inkling Small | 0.4523 | 266B | 12B | large | ✅ | ✅ |
| 85 | DeepSeek V4 Pro (non-reasoning) | 0.4520 | 1.6T | 49B | large | ✅ | ❌ |
| 86 | DeepSeek R1 0528 | 0.4519 | 685B | 37B | large | ✅ | ✅ |
| 87 | Kimi K2 0905 | 0.4499 | 1T | 32B | large | ✅ | ❌ |
| 88 | A.X-K2 | 0.4479 | 692B | 33B | large | ✅ | ✅ |
| 89 | Apriel-v1.6-15B-Thinker | 0.4474 | 15B | — | small | ✅ | ✅ |
| 90 | Qwen3.5 122B A10B | 0.4432 | 125B | 10B | medium | ✅ | ✅ |
| 91 | Nemotron 3.5 Super VL | 0.4427 | 120B | 12B | medium | ✅ | ✅ |
| 92 | Qwen3 VL 32B | 0.4421 | 33.4B | — | small | ✅ | ✅ |
| 93 | DeepSeek V4.1 Flash (non-reasoning) | 0.4413 | 552B | 16B | large | ✅ | ❌ |
| 94 | DeepSeek V3.2 (non-reasoning) | 0.4408 | 685B | 37B | large | ✅ | ❌ |
| 95 | DeepSeek V3.1 Terminus | 0.4397 | 685B | 37B | large | ✅ | ✅ |
| 96 | Gemma 4 31B | 0.4350 | 30.7B | — | small | ✅ | ✅ |
| 97 | Apriel-v1.5-15B-Thinker | 0.4332 | 15B | — | small | ✅ | ✅ |
| 98 | Ling-3.0-flash-Fin | 0.4320 | 124B | 5.1B | medium | ✅ | ✅ |
| 99 | Cogito v2.1 | 0.4298 | 671B | 37B | large | ✅ | ✅ |
| 100 | Inkling (xhigh) | 0.4268 | 975B | 41B | large | ✅ | ✅ |
| 101 | Solar Mini 4 | 0.4243 | 35B | — | small | ❌ | ✅ |
| 102 | GLM-4.7 (non-reasoning) | 0.4232 | 357B | 32B | large | ✅ | ❌ |
| 103 | K2 Horizon 7B | 0.4213 | 7B | — | small | ✅ | ✅ |
| 104 | Ling 3.0 Flash | 0.4208 | 124B | 5.1B | medium | ✅ | ✅ |
| 105 | MiMo-V2-Flash (non-reasoning) | 0.4204 | 309B | 15B | large | ✅ | ❌ |
| 106 | EXAONE 4.5 33B | 0.4163 | 34.4B | — | small | ✅ | ✅ |
| 107 | Qwen3.6 35B A3B (non-reasoning) | 0.4146 | 36B | 3B | small | ✅ | ❌ |
| 108 | Kimi K2 | 0.4139 | 1T | 32B | large | ✅ | ❌ |
| 109 | MiMo-V2.5-Pro (non-reasoning) | 0.4109 | 1T | 42B | large | ✅ | ❌ |
| 110 | Mistral Medium 3.5 | 0.4096 | 128B | — | medium | ✅ | ✅ |
| 111 | Gemma 4 12B | 0.4091 | 12B | — | small | ✅ | ✅ |
| 112 | Nemotron 3 Ultra | 0.4068 | 550B | 55B | large | ✅ | ✅ |
| 113 | Seed-OSS-36B-Instruct | 0.4066 | 36.2B | — | small | ✅ | ✅ |
| 114 | DeepSeek V4 Flash (non-reasoning) | 0.4065 | 284B | 13B | large | ✅ | ❌ |
| 115 | Muse Glimmer (high) | 0.4037 | 30B | — | small | ✅ | ✅ |
| 116 | Ling-2.6-1T | 0.4034 | 1T | 63B | large | ✅ | ❌ |
| 117 | Qwen3.8 27B (non-reasoning) | 0.3970 | 27B | — | small | ✅ | ❌ |
| 118 | Hy3-preview (non-reasoning) | 0.3954 | 295B | 21B | large | ✅ | ❌ |
| 119 | Gemma 4 26B A4B | 0.3951 | 25.2B | 3.8B | small | ✅ | ✅ |
| 120 | Gemma 4 31B (non-reasoning) | 0.3947 | 30.7B | — | small | ✅ | ❌ |
| 121 | LongCat 2.0 | 0.3941 | 1.6T | 48B | large | ✅ | ✅ |
| 122 | Ring-2.6-1T | 0.3941 | 1T | 63B | large | ✅ | ✅ |
| 123 | Qwen3.5 35B A3B (non-reasoning) | 0.3904 | 36B | 3B | small | ✅ | ❌ |
| 124 | Nemotron 3.5 Bolt 74B-A9B | 0.3896 | 74B | 9B | medium | ✅ | ✅ |
| 125 | Qwen3.5 4B | 0.3868 | 4.66B | — | small | ✅ | ✅ |
| 126 | GLM-4.6 (non-reasoning) | 0.3861 | 357B | 32B | large | ✅ | ❌ |
| 127 | Ring-1T | 0.3813 | 1T | 50B | large | ✅ | ✅ |
| 128 | Qwen3 Next 80B A3B | 0.3769 | 80B | 3B | medium | ✅ | ✅ |
| 129 | DeepSeek V3.1 Terminus (non-reasoning) | 0.3762 | 685B | 37B | large | ✅ | ❌ |
| 130 | Qwen3 Coder 480B | 0.3760 | 480B | 35B | large | ✅ | ❌ |
| 131 | GLM-4.5-Air | 0.3699 | 106B | 12B | medium | ✅ | ✅ |
| 132 | INTELLECT-3 | 0.3688 | 107B | 12B | medium | ✅ | ✅ |
| 133 | GLM-4.6V | 0.3667 | 108B | 12B | medium | ✅ | ✅ |
| 134 | DeepSeek V3.2 Exp (non-reasoning) | 0.3665 | 685B | 37B | large | ✅ | ❌ |
| 135 | Qwen3 235B 2507 | 0.3635 | 235B | 22B | large | ✅ | ❌ |
| 136 | K2-V2 (high) | 0.3603 | 70B | — | medium | ✅ | ✅ |
| 137 | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3593 | 1.6T | 49B | large | ✅ | ❌ |
| 138 | Nemotron Cascade 2 30B A3B | 0.3589 | 31.6B | 3B | small | ✅ | ✅ |
| 139 | DeepSeek V3.1 (non-reasoning) | 0.3585 | 685B | 37B | large | ✅ | ❌ |
| 140 | Qwen3.5 9B | 0.3567 | 9.65B | — | small | ✅ | ✅ |
| 141 | Qwen3 VL 235B A22B | 0.3565 | 235B | — | large | ✅ | ❌ |
| 142 | GLM-4.7-Flash | 0.3564 | 31.2B | 3B | small | ✅ | ✅ |
| 143 | QwQ-32B | 0.3558 | 32.8B | — | small | ✅ | ✅ |
| 144 | MiniMax M1 80k | 0.3542 | 456B | 45.9B | large | ✅ | ✅ |
| 145 | Qwen3 VL 30B A3B | 0.3531 | 30B | 3B | small | ✅ | ✅ |
| 146 | Qwen3.5 9B (non-reasoning) | 0.3457 | 9.65B | — | small | ✅ | ❌ |
| 147 | Qwen3 235B A22B 2507 | 0.3449 | 235B | 22B | large | ✅ | ✅ |
| 148 | Llama Nemotron Super 49B v1.5 | 0.3380 | 49B | — | medium | ✅ | ✅ |
| 149 | HyperCLOVA X SEED Think (32B) | 0.3377 | 32B | — | small | ✅ | ✅ |
| 150 | Command A+ | 0.3377 | 218B | 25B | large | ✅ | ✅ |
| 151 | Gemma 4 26B A4B (non-reasoning) | 0.3364 | 25.2B | 3.8B | small | ✅ | ❌ |
| 152 | Motif-2-12.7B | 0.3308 | 12.7B | — | small | ❌ | ✅ |
| 153 | gpt-oss-20b (low) | 0.3295 | 21B | 3.6B | small | ✅ | ✅ |
| 154 | Hermes 4 405B | 0.3278 | 406B | — | large | ✅ | ✅ |
| 155 | K2 Horizon 3.7B | 0.3274 | 3.7B | — | tiny | ✅ | ✅ |
| 156 | Qwen3 Next 80B A3B | 0.3263 | 80B | 3B | medium | ✅ | ❌ |
| 157 | Ling-1T | 0.3255 | 1T | 50B | large | ✅ | ❌ |
| 158 | Qwen3 4B 2507 | 0.3201 | 4.02B | — | tiny | ✅ | ✅ |
| 159 | gpt-oss-120b (low) | 0.3189 | 117B | 5.1B | medium | ✅ | ✅ |
| 160 | MiniMax M1 40k | 0.3155 | 456B | 45.9B | large | ✅ | ✅ |
| 161 | Qwen3 VL 32B | 0.3109 | 33.4B | — | small | ✅ | ❌ |
| 162 | EXAONE 4.0 32B | 0.3107 | 32B | — | small | ✅ | ✅ |
| 163 | Falcon-H1R-7B | 0.3105 | 7B | — | small | ✅ | ✅ |
| 164 | K2-V2 (medium) | 0.3064 | 70B | — | medium | ✅ | ✅ |
| 165 | Qwen3 235B | 0.3057 | 235B | 22B | large | ✅ | ✅ |
| 166 | Nemotron 3 Super | 0.3046 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 167 | gpt-oss-120b (high) | 0.3034 | 117B | 5.1B | medium | ✅ | ✅ |
| 168 | Qwen3 Omni 30B A3B | 0.3009 | 35.3B | 3B | small | ✅ | ✅ |
| 169 | G9v3-3B | 0.3006 | 3B | — | tiny | ✅ | ✅ |
| 170 | NVIDIA Nemotron Nano 12B v2 VL | 0.2981 | 13.2B | — | small | ✅ | ✅ |
| 171 | Nemotron 3 Nano | 0.2966 | 31.6B | 3.6B | small | ✅ | ✅ |
| 172 | Granite 4.2 30B | 0.2961 | 30B | — | small | ✅ | ✅ |
| 173 | HyperNova 60B 2605 (high) | 0.2956 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 174 | Olmo 3.1 32B Think | 0.2955 | 32.2B | — | small | ✅ | ✅ |
| 175 | Trinity Large Thinking | 0.2952 | 399B | 13B | large | ✅ | ✅ |
| 176 | MiniCPM5-2B | 0.2934 | 2.6B | — | tiny | ✅ | ✅ |
| 177 | Llama Nemotron Ultra | 0.2930 | 253B | — | large | ✅ | ✅ |
| 178 | Gemma 4 12B (non-reasoning) | 0.2913 | 12B | — | small | ✅ | ❌ |
| 179 | DiffusionGemma 26B A4B | 0.2904 | 25.2B | 3.8B | small | ✅ | ✅ |
| 180 | Ring-flash-2.0 | 0.2888 | 103B | 6.1B | medium | ✅ | ✅ |
| 181 | GLM-4.5V | 0.2886 | 108B | 12B | medium | ✅ | ✅ |
| 182 | Ling 3.0 Tiny | 0.2881 | 7.9B | 1.3B | small | ✅ | ✅ |
| 183 | Qwen3 VL 30B A3B | 0.2879 | 30B | 3B | small | ✅ | ❌ |
| 184 | NVIDIA Nemotron Nano 9B V2 | 0.2877 | 9B | — | small | ✅ | ✅ |
| 185 | MiniCPM5-1B | 0.2875 | 1B | — | tiny | ✅ | ✅ |
| 186 | MiniCPM5-1B (non-reasoning) | 0.2874 | 1B | — | tiny | ✅ | ❌ |
| 187 | K-EXAONE (non-reasoning) | 0.2853 | 236B | 23B | large | ✅ | ❌ |
| 188 | Solar Open 100B | 0.2825 | 102B | 12B | medium | ✅ | ✅ |
| 189 | K2 Think V2 | 0.2822 | 70B | — | medium | ✅ | ✅ |
| 190 | Ling 2.6 Flash | 0.2799 | 107B | 7.4B | medium | ✅ | ❌ |
| 191 | Qwen3.5 4B (non-reasoning) | 0.2756 | 4.66B | — | small | ✅ | ❌ |
| 192 | Hermes 4 70B | 0.2741 | 70.6B | — | medium | ✅ | ✅ |
| 193 | DeepSeek R1 (Jan) | 0.2706 | 685B | 37B | large | ✅ | ✅ |
| 194 | ERNIE 4.5 300B A47B | 0.2702 | 300B | 47B | large | ✅ | ❌ |
| 195 | gpt-oss-20b (high) | 0.2677 | 21B | 3.6B | small | ✅ | ✅ |
| 196 | DeepSeek R1 Distill Qwen 32B | 0.2673 | 32B | — | small | ✅ | ✅ |
| 197 | Nemotron 3 Nano Omni 30B A3B | 0.2653 | 30B | 3B | small | ✅ | ✅ |
| 198 | Nemotron 3.5 Lightning | 0.2615 | 31.6B | 3.6B | small | ✅ | ✅ |
| 199 | Qwen3 Coder Next | 0.2610 | 79.7B | 3B | medium | ✅ | ❌ |
| 200 | Ling-flash-2.0 | 0.2587 | 103B | 6.1B | medium | ✅ | ❌ |
| 201 | North Mini Code | 0.2579 | 30B | 3B | small | ✅ | ✅ |
| 202 | Tri-21B-think Preview | 0.2575 | 21B | — | small | ✅ | ✅ |
| 203 | Mistral Small 4 | 0.2560 | 119B | 6.5B | medium | ✅ | ✅ |
| 204 | Magistral Small 1.2 | 0.2560 | 24B | — | small | ✅ | ✅ |
| 205 | LongCat Flash Lite | 0.2558 | 68.5B | 3B | medium | ✅ | ❌ |
| 206 | Qwen3 30B | 0.2549 | 30.5B | 3.3B | small | ✅ | ✅ |
| 207 | Gemma 4 E4B (non-reasoning) | 0.2517 | 8B | 4.5B | small | ✅ | ❌ |
| 208 | Tri-21B-Think | 0.2514 | 21B | — | small | ✅ | ✅ |
| 209 | Qwen3 VL 8B | 0.2505 | 8.77B | — | small | ✅ | ✅ |
| 210 | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.2503 | 9B | — | small | ✅ | ❌ |
| 211 | Granite 4.2 8B | 0.2483 | 8B | — | small | ✅ | ✅ |
| 212 | DeepSeek R1 Distill Qwen 14B | 0.2467 | 14B | — | small | ✅ | ✅ |
| 213 | Hermes 4 405B (non-reasoning) | 0.2458 | 406B | — | large | ✅ | ❌ |
| 214 | Pixtral Large | 0.2447 | 124B | — | medium | ✅ | ❌ |
| 215 | Olmo 3 32B Think | 0.2444 | 32.2B | — | small | ✅ | ✅ |
| 216 | Qwen3 Coder 30B A3B | 0.2430 | 30.5B | 3.3B | small | ✅ | ❌ |
| 217 | Devstral 2 | 0.2422 | 125B | — | medium | ✅ | ❌ |
| 218 | Llama 3.1 405B | 0.2383 | 405B | — | large | ✅ | ❌ |
| 219 | Qwen3 30B A3B 2507 (non-reasoning) | 0.2373 | 30.5B | 3.3B | small | ✅ | ❌ |
| 220 | GLM-4.6V (non-reasoning) | 0.2363 | 108B | 12B | medium | ✅ | ❌ |
| 221 | Mistral Large 3 | 0.2329 | 675B | 41B | large | ✅ | ❌ |
| 222 | Step3 VL 10B | 0.2317 | 10.2B | — | small | ✅ | ✅ |
| 223 | DeepSeek V3 0324 | 0.2315 | 671B | 37B | large | ✅ | ❌ |
| 224 | GLM-4.7-Flash (non-reasoning) | 0.2290 | 31.2B | 3B | small | ✅ | ❌ |
| 225 | Qwen3 30B A3B 2507 | 0.2288 | 30.5B | 3.3B | small | ✅ | ✅ |
| 226 | Magistral Small 1 | 0.2265 | 23.6B | — | small | ✅ | ✅ |
| 227 | Solar Pro 3 | 0.2247 | 102B | — | medium | ❌ | ✅ |
| 228 | K2-V2 (low) | 0.2229 | 70B | — | medium | ✅ | ✅ |
| 229 | Mistral Small 4 (non-reasoning) | 0.2216 | 119B | 6.5B | medium | ✅ | ❌ |
| 230 | Llama 3.3 Nemotron Super 49B | 0.2190 | 49B | — | medium | ✅ | ✅ |
| 231 | LFM2.5-8B-A1B | 0.2166 | 8.3B | 1.5B | small | ✅ | ✅ |
| 232 | Devstral Small 2 | 0.2152 | 24B | — | small | ✅ | ❌ |
| 233 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.2140 | 4.51B | — | small | ✅ | ✅ |
| 234 | LFM2.5-2.6B | 0.2110 | 2.7B | — | tiny | ✅ | ✅ |
| 235 | Qwen3 4B | 0.2109 | 4.02B | — | tiny | ✅ | ✅ |
| 236 | Mistral Large 2 (Nov) | 0.2071 | 123B | — | medium | ✅ | ❌ |
| 237 | Gemma 4 E2B | 0.2025 | 5.1B | 2.3B | small | ✅ | ✅ |
| 238 | Gemma 4 E4B | 0.2022 | 8B | 4.5B | small | ✅ | ✅ |
| 239 | Llama 4 Maverick | 0.2015 | 402B | 17B | large | ✅ | ❌ |
| 240 | Qwen3 Omni 30B A3B | 0.2005 | 35.3B | 3B | small | ✅ | ❌ |
| 241 | Qwen3 4B 2507 (non-reasoning) | 0.1986 | 4.02B | — | tiny | ✅ | ❌ |
| 242 | Kimi Linear 48B A3B Instruct | 0.1967 | 49.1B | 3B | medium | ✅ | ❌ |
| 243 | Qwen3 VL 8B | 0.1953 | 8.77B | — | small | ✅ | ❌ |
| 244 | Llama 3.2 90B (Vision) | 0.1947 | 90B | — | medium | ✅ | ❌ |
| 245 | Sarvam 105B (high) | 0.1922 | 106B | 10.3B | medium | ✅ | ✅ |
| 246 | Qwen3 32B | 0.1917 | 32.8B | — | small | ✅ | ✅ |
| 247 | Olmo 3 7B Think | 0.1912 | 7B | — | small | ✅ | ✅ |
| 248 | DeepSeek R1 0528 Qwen3 8B | 0.1909 | 8.19B | — | small | ✅ | ✅ |
| 249 | EXAONE 4.0 32B (non-reasoning) | 0.1891 | 32B | — | small | ✅ | ❌ |
| 250 | Devstral Small (May) | 0.1889 | 23.6B | — | small | ✅ | ❌ |
| 251 | Qwen3 235B (non-reasoning) | 0.1877 | 235B | 22B | large | ✅ | ❌ |
| 252 | Qwen3.5 2B | 0.1875 | 2.27B | — | tiny | ✅ | ✅ |
| 253 | Granite 4.2 3B | 0.1856 | 3B | — | tiny | ✅ | ✅ |
| 254 | Devstral Small | 0.1842 | 24B | — | small | ✅ | ❌ |
| 255 | DeepSeek R1 Distill Llama 70B | 0.1841 | 70B | — | medium | ✅ | ✅ |
| 256 | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1829 | 49B | — | medium | ✅ | ❌ |
| 257 | Qwen3 VL 4B | 0.1822 | 4.44B | — | tiny | ✅ | ✅ |
| 258 | Qwen2.5 72B | 0.1804 | 72B | — | medium | ✅ | ❌ |
| 259 | Qwen3 32B (non-reasoning) | 0.1793 | 32.8B | — | small | ✅ | ❌ |
| 260 | Nanbeige4.1-3B | 0.1754 | 3.93B | — | tiny | ✅ | ✅ |
| 261 | Qwen3 14B | 0.1734 | 14.8B | — | small | ✅ | ✅ |
| 262 | Command A | 0.1729 | 111B | — | medium | ✅ | ❌ |
| 263 | DeepSeek V3 (Dec) | 0.1705 | 671B | 37B | large | ✅ | ❌ |
| 264 | GLM-4.5V (non-reasoning) | 0.1686 | 108B | 12B | medium | ✅ | ❌ |
| 265 | Gemini 1.5 Flash-8B | 0.1652 | 8B | — | small | ❌ | ❌ |
| 266 | Granite 4.1 30B | 0.1614 | 30B | — | small | ✅ | ❌ |
| 267 | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1607 | 49B | — | medium | ✅ | ❌ |
| 268 | Qwen3 14B (non-reasoning) | 0.1606 | 14.8B | — | small | ✅ | ❌ |
| 269 | Llama 3.1 Nemotron 70B | 0.1572 | 70B | — | medium | ✅ | ❌ |
| 270 | Mistral Large 2 (Jul) | 0.1539 | 123B | — | medium | ✅ | ❌ |
| 271 | Gemma 4 E2B (non-reasoning) | 0.1535 | 5.1B | 2.3B | small | ✅ | ❌ |
| 272 | Ministral 3 14B | 0.1524 | 14B | — | small | ✅ | ❌ |
| 273 | Ling-mini-2.0 | 0.1512 | 16.3B | 1.4B | small | ✅ | ❌ |
| 274 | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1505 | 13.2B | — | small | ✅ | ❌ |
| 275 | Mistral Small 3.2 | 0.1496 | 24B | — | small | ✅ | ❌ |
| 276 | Llama 3.1 70B | 0.1484 | 70B | — | medium | ✅ | ❌ |
| 277 | Olmo 3.1 32B Instruct | 0.1478 | 32.2B | — | small | ✅ | ❌ |
| 278 | DeepSeek R1 Distill Llama 8B | 0.1452 | 8B | — | small | ✅ | ✅ |
| 279 | Qwen3 VL 4B | 0.1445 | 4.44B | — | tiny | ✅ | ❌ |
| 280 | Qwen3 30B (non-reasoning) | 0.1417 | 30.5B | 3.3B | small | ✅ | ❌ |
| 281 | Llama 3.3 70B | 0.1415 | 70B | — | medium | ✅ | ❌ |
| 282 | Exaone 4.0 1.2B | 0.1406 | 1.28B | — | tiny | ✅ | ✅ |
| 283 | Hermes 4 70B (non-reasoning) | 0.1403 | 70.6B | — | medium | ✅ | ❌ |
| 284 | Qwen3.5 2B (non-reasoning) | 0.1379 | 2.27B | — | tiny | ✅ | ❌ |
| 285 | Llama 4 Scout | 0.1370 | 109B | 17B | medium | ✅ | ❌ |
| 286 | Nemotron 3 Nano (non-reasoning) | 0.1359 | 31.6B | 3.6B | small | ✅ | ❌ |
| 287 | Jamba Reasoning 3B | 0.1334 | 3B | — | tiny | ✅ | ✅ |
| 288 | Reka Flash 3 | 0.1321 | 21B | — | small | ✅ | ✅ |
| 289 | LFM2 24B A2B | 0.1269 | 23.8B | 2.3B | small | ✅ | ❌ |
| 290 | Sarvam 30B (high) | 0.1237 | 32.2B | 2.4B | small | ✅ | ✅ |
| 291 | Mistral Small 3 | 0.1232 | 24B | — | small | ✅ | ❌ |
| 292 | Granite 4.0 H Small | 0.1219 | 32B | 9B | small | ✅ | ❌ |
| 293 | Ministral 3 8B | 0.1211 | 8B | — | small | ✅ | ❌ |
| 294 | Granite 4.1 8B | 0.1179 | 8B | — | small | ✅ | ❌ |
| 295 | Jamba 1.7 Large | 0.1168 | 398B | 94B | large | ✅ | ❌ |
| 296 | Llama 3.1 8B | 0.1165 | 8B | — | small | ✅ | ❌ |
| 297 | Phi-4 | 0.1141 | 14B | — | small | ✅ | ❌ |
| 298 | MiniCPM-V 4.6 1.3B | 0.1100 | 1.3B | — | tiny | ✅ | ❌ |
| 299 | Qwen3 8B | 0.1091 | 8.19B | — | small | ✅ | ✅ |
| 300 | Olmo 3 7B | 0.1079 | 7B | — | small | ✅ | ❌ |
| 301 | Qwen3 1.7B | 0.1062 | 2.03B | — | tiny | ✅ | ✅ |
| 302 | Llama 3 70B | 0.0993 | 70B | — | medium | ✅ | ❌ |
| 303 | Qwen3 8B (non-reasoning) | 0.0987 | 8.19B | — | small | ✅ | ❌ |
| 304 | Sarvam M | 0.0943 | 23.6B | — | small | ✅ | ✅ |
| 305 | Nemotron 3 Nano 4B | 0.0918 | 3.97B | — | tiny | ✅ | ✅ |
| 306 | Exaone 4.0 1.2B (non-reasoning) | 0.0873 | 1.28B | — | tiny | ✅ | ❌ |
| 307 | Ministral 3 3B | 0.0820 | 3B | — | tiny | ✅ | ❌ |
| 308 | Llama 3.2 11B (Vision) | 0.0798 | 11B | — | small | ✅ | ❌ |
| 309 | LFM2.5-1.2B-Instruct | 0.0796 | 1.17B | — | tiny | ✅ | ❌ |
| 310 | Qwen3.5 0.8B | 0.0772 | 0.873B | — | tiny | ✅ | ✅ |
| 311 | Gemma 3 27B | 0.0761 | 27.4B | — | small | ✅ | ❌ |
| 312 | LFM2 8B A1B | 0.0744 | 8.34B | 1.5B | small | ✅ | ❌ |
| 313 | Molmo2-8B | 0.0740 | 8.66B | — | small | ✅ | ❌ |
| 314 | Gemma 3 270M | 0.0739 | 0.268B | — | tiny | ✅ | ❌ |
| 315 | LFM2 2.6B | 0.0725 | 2.57B | — | tiny | ✅ | ❌ |
| 316 | LFM2.5-1.2B-Thinking | 0.0710 | 1.17B | — | tiny | ✅ | ✅ |
| 317 | Llama 3.2 3B | 0.0685 | 3B | — | tiny | ✅ | ❌ |
| 318 | Apertus 70B Instruct | 0.0636 | 70B | — | medium | ✅ | ❌ |
| 319 | Granite 4.1 3B | 0.0589 | 3B | — | tiny | ✅ | ❌ |
| 320 | Granite 4.0 H 1B | 0.0587 | 1.5B | — | tiny | ✅ | ❌ |
| 321 | Phi-4 Mini | 0.0586 | 3.84B | — | tiny | ✅ | ❌ |
| 322 | Phi-4 Multimodal | 0.0583 | 5.6B | — | small | ✅ | ❌ |
| 323 | Jamba 1.7 Mini | 0.0579 | 52B | 12B | medium | ✅ | ❌ |
| 324 | Qwen3.5 0.8B (non-reasoning) | 0.0561 | 0.873B | — | tiny | ✅ | ❌ |
| 325 | Granite 4.0 Micro | 0.0551 | 3B | — | tiny | ✅ | ❌ |
| 326 | OLMo 2 32B | 0.0473 | 32.2B | — | small | ✅ | ❌ |
| 327 | Qwen3 0.6B | 0.0467 | 0.752B | — | tiny | ✅ | ✅ |
| 328 | Gemma 3 12B | 0.0461 | 12.2B | — | small | ✅ | ❌ |
| 329 | Granite 3.3 8B (non-reasoning) | 0.0432 | 8.17B | — | small | ✅ | ❌ |
| 330 | Llama 3.2 1B | 0.0421 | 1B | — | tiny | ✅ | ❌ |
| 331 | LFM2.5-VL-1.6B | 0.0373 | 1.6B | — | tiny | ✅ | ❌ |
| 332 | Phi-3 Mini | 0.0361 | 3.8B | — | tiny | ✅ | ❌ |
| 333 | Gemma 3 4B | 0.0351 | 4.3B | — | tiny | ✅ | ❌ |
| 334 | Llama 3 8B | 0.0348 | 8B | — | small | ✅ | ❌ |
| 335 | Gemma 3n E4B | 0.0324 | 8.39B | 4B | small | ✅ | ❌ |
| 336 | Granite 4.0 1B | 0.0315 | 1.6B | — | tiny | ✅ | ❌ |
| 337 | Qwen3 1.7B (non-reasoning) | 0.0299 | 2.03B | — | tiny | ✅ | ❌ |
| 338 | Mistral 7B | 0.0266 | 7B | — | small | ✅ | ❌ |
| 339 | LFM2 1.2B | 0.0235 | 1.17B | — | tiny | ✅ | ❌ |
| 340 | Apertus 8B Instruct | 0.0225 | 8B | — | small | ✅ | ❌ |
| 341 | Granite 4.0 350M | 0.0225 | 0.35B | — | tiny | ✅ | ❌ |
| 342 | Qwen3 0.6B (non-reasoning) | 0.0157 | 0.752B | — | tiny | ✅ | ❌ |
| 343 | Gemma 3 1B | 0.0147 | 1B | — | tiny | ✅ | ❌ |
| 344 | OLMo 2 7B | 0.0111 | 7.3B | — | small | ✅ | ❌ |
| 345 | Gemma 3n E2B | 0.0110 | 5.98B | 2B | small | ✅ | ❌ |
| 346 | Granite 4.0 H 350M | 0.0084 | 0.34B | — | tiny | ✅ | ❌ |
| 347 | DeepSeek R1 Distill Qwen 1.5B | 0.0065 | 1.5B | — | tiny | ✅ | ✅ |
| 348 | Molmo 7B-D | 0.0038 | 8.02B | — | small | ✅ | ❌ |
| 349 | Tiny Aya Global | 0.0017 | 3.35B | — | tiny | ✅ | ❌ |
| 350 | K2 Horizon 0.9B | 0.0000 | 0.9B | — | tiny | ✅ | ✅ |

## 品牌帕累托前沿连线（仅体现在图中）

以下 11 个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 8 |
| <img src="https://artificialanalysis.ai/img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 6 |
| <img src="https://artificialanalysis.ai/img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | `#80B6A1` | 1 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | `#795BCF` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | `#3B62EC` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | `#00F5E7` | 4 |
| <img src="https://artificialanalysis.ai/img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 4 |

## 基准测试动态标定（Leave-One-Out Calibration）

不同基准测试的参测模型群体能力分布存在差异（例如部分高难度或专业领域基准测试仅覆盖头部高能力模型）。系统在标准归一化之后执行了**留一交叉动态映射标定流程**：

1. **排除单项基准**：暂时排除某项基准测试，计算各模型在其余测试项上的平均能力；
2. **全域归一化评估**：将排除后的平均能力归一化至 `[0, 1]`；
3. **锁定参测区间**：提取实际参测该基准测试的所有模型，以它们排除该项后的能力最高值和最低值分别作为该项的新映射上界和下界；
4. **并行同步迭代**：所有基准测试以 `[0, 1]` 为初值同步更新，完成一轮后以新上下界作为输入进入下一轮，重复迭代直至收敛。

> 标定状态：已完成 **17** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）。标定得到的数据作为新指标独立保存，不覆盖原始基准测试归一化与综合能力。

| 基准测试项 | 英文标识 | 参测模型数 | 标定映射下界 | 标定映射上界 | 映射跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 617 | `0.0000` | `1.0000` | `1.0000` |
| GPQA Diamond | `gpqa` | 551 | `0.0000` | `0.9951` | `0.9951` |
| Humanity's Last Exam | `hle` | 616 | `0.0000` | `1.0000` | `1.0000` |
| MMMU Pro | `mmmuPro` | 297 | `0.0021` | `1.0000` | `0.9979` |
| IFBench Instruction Following | `ifbench` | 450 | `0.0000` | `0.9092` | `0.9092` |
| SciCode Coding | `scicode` | 243 | `0.0348` | `1.0000` | `0.9652` |
| CritPt Physics | `critpt` | 588 | `0.0236` | `1.0000` | `0.9764` |
| AA-LCR Long Context | `lcr` | 586 | `0.0000` | `1.0000` | `1.0000` |
| AA Omniscience Index | `omniscience` | 588 | `0.0195` | `1.0000` | `0.9805` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 588 | `0.0143` | `1.0000` | `0.9857` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 588 | `0.0159` | `1.0000` | `0.9841` |
| GDPval-AA Normalized | `gdpvalNormalized` | 307 | `0.0348` | `1.0000` | `0.9652` |
| AA Analyst Agent | `analystAgent` | 51 | `0.2879` | `1.0000` | `0.7121` |
| APEX-Agents-AA | `apexAgents` | 33 | `0.2717` | `0.8286` | `0.5569` |
| ITBench-AA | `itbenchSre` | 45 | `0.1549` | `1.0000` | `0.8451` |
| τ²-Bench Telecom | `tau2` | 439 | `0.0141` | `0.8965` | `0.8823` |
| τ³-Bench Banking | `tauBanking` | 209 | `0.0282` | `1.0000` | `0.9718` |
| Terminal-Bench Hard | `terminalbenchHard` | 432 | `0.0178` | `0.8983` | `0.8805` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 242 | `0.0340` | `0.9965` | `0.9625` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 232 | `0.0348` | `1.0000` | `0.9652` |
| LiveCodeBench | `livecodebench` | 285 | `0.0000` | `0.7183` | `0.7183` |
| AIME 2025 | `aime2025` | 269 | `0.0000` | `0.7256` | `0.7256` |
| AA-Briefcase Knowledge Work | `briefcase` | 243 | `0.0348` | `1.0000` | `0.9652` |
| AutomationBench-AA SaaS Workflows | `automationbench` | 235 | `0.0348` | `1.0000` | `0.9652` |
| GDP.pdf Long Document | `gdpPdf` | 234 | `0.0330` | `1.0000` | `0.9670` |
| MLCR-AA Medical Reasoning | `mlcr` | 174 | `0.1019` | `1.0000` | `0.8981` |
| Terminal-Bench-Science | `terminalbenchScience` | 97 | `0.1261` | `1.0000` | `0.8739` |
| FrontierCode SWE | `frontiercode` | 77 | `0.1263` | `1.0000` | `0.8737` |
| EnterpriseOps-Gym-AA | `enterpriseOps` | 50 | `0.3059` | `0.8962` | `0.5903` |
| Harvey LAB-AA Legal Agent | `harveyLab` | 28 | `0.5021` | `1.0000` | `0.4979` |
| Code2Video-AA Animation | `code2video` | 27 | `0.4822` | `1.0000` | `0.5178` |
| AA-3D Interactive Experience | `aa3d` | 23 | `0.4825` | `1.0000` | `0.5175` |


## 评分方法

1. **32项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-AA、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0、LiveCodeBench、AIME 2025、AA-Briefcase Knowledge Work、AutomationBench-AA SaaS Workflows、GDP.pdf Long Document、MLCR-AA Medical Reasoning、Terminal-Bench-Science、FrontierCode SWE、EnterpriseOps-Gym-AA、Harvey LAB-AA Legal Agent、Code2Video-AA Animation、AA-3D Interactive Experience）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且总参数量 ≤，且至少一项严格更优；缺少参数量数据的模型不在图表和表格中）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.0739，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 0.56，r = B/C = 1.79644），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002984，maxdev = 0.1052。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 51，10B–100B: 111，100B–1T: 138，1T–2.8T: 10
- 中位数位置 0.568；左 141 个，右 173 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.121，10^1→ 0.345，10^2→ 0.610，10^3→ 0.879

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
**模型数（有参数量数据）**: 350（总体帕累托前沿 14 个；图表入图 314 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 11 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.0739，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 36 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
