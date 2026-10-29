# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.0000，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 341 个入图，0 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3.1 Pro | 0.8603 | 2.8T | — | large | ❌ | ✅ |
| 2 | Kimi K3 (max) | 0.8347 | 2.8T | 104B | large | ✅ | ✅ |
| 3 | GLM-5.3 (max) | 0.7598 | 753B | 40B | large | ✅ | ✅ |
| 4 | GLM-5.2 (max) | 0.7580 | 753B | 40B | large | ✅ | ✅ |
| 5 | Step 5 Preview | 0.7502 | 600B | — | large | ✅ | ✅ |
| 6 | Ling 3.1 Flash | 0.7345 | 560B | — | large | ✅ | ✅ |
| 7 | Qwen3.8 2.4T A95B | 0.7338 | 2.4T | 95B | large | ✅ | ✅ |
| 8 | DeepSeek V4.1 Flash (max) | 0.7218 | 552B | 16B | large | ✅ | ✅ |
| 9 | DeepSeek V4 Flash 0731 (max) | 0.7209 | 284B | 13B | large | ✅ | ✅ |
| 10 | GLM-5.3-Flash | 0.7205 | 320B | 18B | large | ✅ | ✅ |
| 11 | DeepSeek V4 Flash Vision (max) | 0.7152 | 284B | — | large | ❌ | ✅ |
| 12 | DeepSeek V4 Pro (high) | 0.7135 | 1.6T | 49B | large | ✅ | ✅ |
| 13 | Muse Spark Open (xhigh) | 0.7096 | 816B | 42B | large | ✅ | ✅ |
| 14 | DeepSeek V4.1 Flash 1017 (max) | 0.6997 | 552B | 16B | large | ✅ | ✅ |
| 15 | Qwen3.8-Flash-Next | 0.6957 | 180B | 6B | large | ✅ | ✅ |
| 16 | Motif 3 (Beta) | 0.6877 | 314B | — | large | ❌ | ✅ |
| 17 | MiMo-V2.6-Pro | 0.6870 | 1T | 42B | large | ✅ | ✅ |
| 18 | Qwen3.5 27B | 0.6821 | 27.8B | — | small | ✅ | ✅ |
| 19 | Motif 3 | 0.6782 | 314B | 13.2B | large | ✅ | ✅ |
| 20 | Nex-N2-Pro | 0.6767 | 397B | 17B | large | ✅ | ✅ |
| 21 | Kimi K2.6 | 0.6750 | 1T | 32B | large | ✅ | ✅ |
| 22 | DeepSeek V4 Pro (max) | 0.6673 | 1.6T | 49B | large | ✅ | ✅ |
| 23 | MiniMax-M2.5 | 0.6433 | 230B | 10B | large | ✅ | ✅ |
| 24 | GLM-5 | 0.6432 | 744B | 40B | large | ✅ | ✅ |
| 25 | Hy3-preview | 0.6403 | 295B | 21B | large | ✅ | ✅ |
| 26 | MiMo-V2-Flash (Feb 2026) | 0.6371 | 309B | 15B | large | ✅ | ✅ |
| 27 | Kimi K2.7 Code | 0.6363 | 1T | 32B | large | ✅ | ✅ |
| 28 | Kimi K2 Thinking | 0.6333 | 1T | 32B | large | ✅ | ✅ |
| 29 | DeepSeek V4 Pro 0813 (max) | 0.6275 | 1.6T | 49B | large | ✅ | ✅ |
| 30 | MiMo-V2-Flash | 0.6249 | 309B | 15B | large | ✅ | ✅ |
| 31 | DeepSeek V4 Flash (max) | 0.6244 | 284B | 13B | large | ✅ | ✅ |
| 32 | Qwen3.8 27B (xhigh) | 0.6209 | 27B | — | small | ✅ | ✅ |
| 33 | GLM-5.1 | 0.6204 | 744B | 40B | large | ✅ | ✅ |
| 34 | Kimi K3 (low) | 0.6142 | 2.8T | 104B | large | ✅ | ✅ |
| 35 | Qwen3.5 35B A3B | 0.6099 | 36B | 3B | small | ✅ | ✅ |
| 36 | JT-4.1 Flash 236B A21B | 0.6046 | 236B | — | large | ❌ | ✅ |
| 37 | Kimi K2.5 | 0.6031 | 1T | 32B | large | ✅ | ✅ |
| 38 | DeepSeek V4 Flash (high) | 0.6015 | 284B | 13B | large | ✅ | ✅ |
| 39 | MiniMax-M2.1 | 0.5990 | 230B | 10B | large | ✅ | ✅ |
| 40 | Mistral Large 4 Preview | 0.5935 | 1T | — | large | ❌ | ✅ |
| 41 | GLM-4.7 | 0.5888 | 357B | 32B | large | ✅ | ✅ |
| 42 | MiMo-V2.5 | 0.5885 | 310B | 15B | large | ✅ | ✅ |
| 43 | Ling-3.0-flash-VL | 0.5869 | 124B | 5.5B | medium | ✅ | ✅ |
| 44 | Qwen3.5 397B A17B | 0.5849 | 397B | 17B | large | ✅ | ✅ |
| 45 | Qwen3.6 27B | 0.5826 | 27.8B | — | small | ✅ | ✅ |
| 46 | GLM-5.1 (non-reasoning) | 0.5818 | 744B | 40B | large | ✅ | ❌ |
| 47 | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5765 | 236B | — | large | ❌ | ❌ |
| 48 | MiMo-V2.6-Flash | 0.5756 | 309B | 15B | large | ✅ | ✅ |
| 49 | Solar Open2 250B | 0.5740 | 250B | 15B | large | ✅ | ✅ |
| 50 | Step 3.7 Flash | 0.5737 | 198B | 11B | large | ✅ | ✅ |
| 51 | MiniMax-M3 | 0.5725 | 428B | 23B | large | ✅ | ✅ |
| 52 | Step 3.5 Flash | 0.5711 | 196B | 11B | large | ✅ | ✅ |
| 53 | DeepSeek V3.2 | 0.5703 | 685B | 37B | large | ✅ | ✅ |
| 54 | MiMo-V2.5-Pro | 0.5692 | 1T | 42B | large | ✅ | ✅ |
| 55 | Kimi K2.6 (non-reasoning) | 0.5691 | 1T | 32B | large | ✅ | ❌ |
| 56 | Hy3 | 0.5653 | 299B | 21B | large | ✅ | ✅ |
| 57 | Qwen3.5 122B A10B | 0.5641 | 125B | 10B | medium | ✅ | ✅ |
| 58 | Qwen3.5 27B (non-reasoning) | 0.5626 | 27.8B | — | small | ✅ | ❌ |
| 59 | MiniMax-M2 | 0.5616 | 230B | 10B | large | ✅ | ✅ |
| 60 | Qwen3.5 397B A17B (non-reasoning) | 0.5615 | 397B | 17B | large | ✅ | ❌ |
| 61 | Quasar 438B (max) | 0.5506 | 438B | — | large | ❌ | ✅ |
| 62 | K2 Horizon 375B A23B | 0.5471 | 375B | 23B | large | ✅ | ✅ |
| 63 | Gemma 4 31B | 0.5409 | 30.7B | — | small | ✅ | ✅ |
| 64 | GLM-5.3 (low) | 0.5355 | 753B | 40B | large | ✅ | ✅ |
| 65 | Qwen3.6 35B A3B | 0.5324 | 36B | 3B | small | ✅ | ✅ |
| 66 | Qwen3.6 27B (non-reasoning) | 0.5274 | 27.8B | — | small | ✅ | ❌ |
| 67 | Kimi K2.5 (non-reasoning) | 0.5230 | 1T | 32B | large | ✅ | ❌ |
| 68 | DeepSeek V3.2 Speciale | 0.5221 | 685B | 37B | large | ✅ | ✅ |
| 69 | Inkling (xhigh) | 0.5193 | 975B | 41B | large | ✅ | ✅ |
| 70 | Qwen3.5 122B A10B (non-reasoning) | 0.5176 | 125B | 10B | medium | ✅ | ❌ |
| 71 | K2 Horizon MoVA 36B A4B | 0.5152 | 36B | 4B | small | ✅ | ✅ |
| 72 | Inkling Small | 0.5149 | 266B | 12B | large | ✅ | ✅ |
| 73 | MiniMax-M2.7 | 0.5135 | 230B | 10B | large | ✅ | ✅ |
| 74 | Qwen3.8 27B (medium) | 0.5135 | 27B | — | small | ✅ | ✅ |
| 75 | Beam 1.0 | 0.5129 | 501B | 23B | large | ✅ | ✅ |
| 76 | Nemotron 3 Ultra | 0.5125 | 550B | 55B | large | ✅ | ✅ |
| 77 | Qwen3.8 27B (low) | 0.5111 | 27B | — | small | ✅ | ✅ |
| 78 | JT-35B-Flash | 0.5108 | 35B | — | small | ❌ | ❌ |
| 79 | Ling 3.0 Flash | 0.4984 | 124B | 5.1B | medium | ✅ | ✅ |
| 80 | GLM-5 (non-reasoning) | 0.4967 | 744B | 40B | large | ✅ | ❌ |
| 81 | DeepSeek V4 Pro (non-reasoning) | 0.4903 | 1.6T | 49B | large | ✅ | ❌ |
| 82 | Ling-2.6-1T | 0.4847 | 1T | 63B | large | ✅ | ❌ |
| 83 | Ling-3.0-flash-Fin | 0.4818 | 124B | 5.1B | medium | ✅ | ✅ |
| 84 | A.X-K2 | 0.4806 | 692B | 33B | large | ✅ | ✅ |
| 85 | Qwen3.6 35B A3B (non-reasoning) | 0.4797 | 36B | 3B | small | ✅ | ❌ |
| 86 | G9v3-39A5B | 0.4759 | 39B | 5B | small | ✅ | ✅ |
| 87 | Gemma 4 26B A4B | 0.4753 | 25.2B | 3.8B | small | ✅ | ✅ |
| 88 | DeepSeek V3.2 Exp | 0.4738 | 685B | 37B | large | ✅ | ✅ |
| 89 | EXAONE 4.5 33B | 0.4738 | 34.4B | — | small | ✅ | ✅ |
| 90 | K-EXAONE | 0.4734 | 236B | 23B | large | ✅ | ✅ |
| 91 | Qwen3 VL 235B A22B | 0.4726 | 235B | 22B | large | ✅ | ✅ |
| 92 | DeepSeek V3.2 (non-reasoning) | 0.4698 | 685B | 37B | large | ✅ | ❌ |
| 93 | DeepSeek V4 Flash (non-reasoning) | 0.4692 | 284B | 13B | large | ✅ | ❌ |
| 94 | Gemma 4 12B | 0.4665 | 12B | — | small | ✅ | ✅ |
| 95 | Qwen3.8 27B (non-reasoning) | 0.4629 | 27B | — | small | ✅ | ❌ |
| 96 | Nemotron 3.5 Super VL | 0.4622 | 120B | 12B | medium | ✅ | ✅ |
| 97 | GLM-4.7 (non-reasoning) | 0.4598 | 357B | 32B | large | ✅ | ❌ |
| 98 | MiMo-V2.5-Pro (non-reasoning) | 0.4584 | 1T | 42B | large | ✅ | ❌ |
| 99 | Qwen3.5 35B A3B (non-reasoning) | 0.4545 | 36B | 3B | small | ✅ | ❌ |
| 100 | K-EXAONE 2.0 | 0.4540 | 750B | 37B | large | ✅ | ✅ |
| 101 | GLM-4.7-Flash | 0.4522 | 31.2B | 3B | small | ✅ | ✅ |
| 102 | Qwen3.5 4B | 0.4515 | 4.66B | — | small | ✅ | ✅ |
| 103 | GLM-4.6 | 0.4501 | 357B | 32B | large | ✅ | ✅ |
| 104 | Qwen3.5 9B | 0.4471 | 9.65B | — | small | ✅ | ✅ |
| 105 | Solar Mini 4 | 0.4470 | 35B | — | small | ❌ | ✅ |
| 106 | LongCat 2.0 | 0.4436 | 1.6T | 48B | large | ✅ | ✅ |
| 107 | Gemma 4 31B (non-reasoning) | 0.4406 | 30.7B | — | small | ✅ | ❌ |
| 108 | Ring-2.6-1T | 0.4396 | 1T | 63B | large | ✅ | ✅ |
| 109 | Mistral Medium 3.5 | 0.4381 | 128B | — | medium | ✅ | ✅ |
| 110 | DeepSeek V3.1 Terminus | 0.4380 | 685B | 37B | large | ✅ | ✅ |
| 111 | MiMo-V2-Flash (non-reasoning) | 0.4375 | 309B | 15B | large | ✅ | ❌ |
| 112 | Apriel-v1.6-15B-Thinker | 0.4365 | 15B | — | small | ✅ | ✅ |
| 113 | Qwen3.5 9B (non-reasoning) | 0.4338 | 9.65B | — | small | ✅ | ❌ |
| 114 | GLM-5.2 (non-reasoning) | 0.4282 | 753B | 40B | large | ✅ | ❌ |
| 115 | Qwen3 VL 32B | 0.4256 | 33.4B | — | small | ✅ | ✅ |
| 116 | K2 Horizon 7B | 0.4254 | 7B | — | small | ✅ | ✅ |
| 117 | Hy3-preview (non-reasoning) | 0.4241 | 295B | 21B | large | ✅ | ❌ |
| 118 | Muse Glimmer (high) | 0.4234 | 30B | — | small | ✅ | ✅ |
| 119 | Kimi K2 0905 | 0.4228 | 1T | 32B | large | ✅ | ❌ |
| 120 | Command A+ | 0.4162 | 218B | 25B | large | ✅ | ✅ |
| 121 | Gemma 4 26B A4B (non-reasoning) | 0.4138 | 25.2B | 3.8B | small | ✅ | ❌ |
| 122 | Nemotron Cascade 2 30B A3B | 0.4134 | 31.6B | 3B | small | ✅ | ✅ |
| 123 | Apriel-v1.5-15B-Thinker | 0.4090 | 15B | — | small | ✅ | ✅ |
| 124 | DeepSeek V3.1 | 0.4069 | 685B | 37B | large | ✅ | ✅ |
| 125 | Nemotron 3.5 Bolt 74B-A9B | 0.4052 | 74B | 9B | medium | ✅ | ✅ |
| 126 | DeepSeek V4.1 Flash (non-reasoning) | 0.3995 | 552B | 16B | large | ✅ | ❌ |
| 127 | GLM-4.5 | 0.3955 | 355B | 32B | large | ✅ | ✅ |
| 128 | Kimi K2 | 0.3873 | 1T | 32B | large | ✅ | ❌ |
| 129 | DeepSeek R1 0528 | 0.3857 | 685B | 37B | large | ✅ | ✅ |
| 130 | Nemotron 3 Super | 0.3848 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 131 | Trinity Large Thinking | 0.3737 | 399B | 13B | large | ✅ | ✅ |
| 132 | DeepSeek V3.1 Terminus (non-reasoning) | 0.3735 | 685B | 37B | large | ✅ | ❌ |
| 133 | Seed-OSS-36B-Instruct | 0.3620 | 36.2B | — | small | ✅ | ✅ |
| 134 | DeepSeek V3.2 Exp (non-reasoning) | 0.3602 | 685B | 37B | large | ✅ | ❌ |
| 135 | gpt-oss-120b (high) | 0.3574 | 117B | 5.1B | medium | ✅ | ✅ |
| 136 | GLM-4.6 (non-reasoning) | 0.3560 | 357B | 32B | large | ✅ | ❌ |
| 137 | DiffusionGemma 26B A4B | 0.3525 | 25.2B | 3.8B | small | ✅ | ✅ |
| 138 | Qwen3 235B A22B 2507 | 0.3523 | 235B | 22B | large | ✅ | ✅ |
| 139 | GLM-4.5-Air | 0.3482 | 106B | 12B | medium | ✅ | ✅ |
| 140 | Qwen3.5 4B (non-reasoning) | 0.3446 | 4.66B | — | small | ✅ | ❌ |
| 141 | Qwen3 Coder Next | 0.3443 | 79.7B | 3B | medium | ✅ | ❌ |
| 142 | HyperNova 60B 2605 (high) | 0.3422 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 143 | North Mini Code | 0.3418 | 30B | 3B | small | ✅ | ✅ |
| 144 | K-EXAONE (non-reasoning) | 0.3415 | 236B | 23B | large | ✅ | ❌ |
| 145 | DeepSeek V3.1 (non-reasoning) | 0.3393 | 685B | 37B | large | ✅ | ❌ |
| 146 | Qwen3 VL 235B A22B | 0.3384 | 235B | — | large | ✅ | ❌ |
| 147 | Ling 2.6 Flash | 0.3383 | 107B | 7.4B | medium | ✅ | ❌ |
| 148 | Solar Open 100B | 0.3369 | 102B | 12B | medium | ✅ | ✅ |
| 149 | LongCat Flash Lite | 0.3360 | 68.5B | 3B | medium | ✅ | ❌ |
| 150 | K2 Horizon 3.7B | 0.3358 | 3.7B | — | tiny | ✅ | ✅ |
| 151 | Ring-1T | 0.3338 | 1T | 50B | large | ✅ | ✅ |
| 152 | Gemma 4 12B (non-reasoning) | 0.3325 | 12B | — | small | ✅ | ❌ |
| 153 | Qwen3 235B 2507 | 0.3250 | 235B | 22B | large | ✅ | ❌ |
| 154 | Pixtral Large | 0.3244 | 124B | — | medium | ✅ | ❌ |
| 155 | Qwen3 Next 80B A3B | 0.3244 | 80B | 3B | medium | ✅ | ✅ |
| 156 | Ling 3.0 Tiny | 0.3228 | 7.9B | 1.3B | small | ✅ | ✅ |
| 157 | GLM-4.6V | 0.3221 | 108B | 12B | medium | ✅ | ✅ |
| 158 | K2-V2 (high) | 0.3219 | 70B | — | medium | ✅ | ✅ |
| 159 | K2 Think V2 | 0.3198 | 70B | — | medium | ✅ | ✅ |
| 160 | Qwen3 Coder 480B | 0.3172 | 480B | 35B | large | ✅ | ❌ |
| 161 | Tri-21B-think Preview | 0.3172 | 21B | — | small | ✅ | ✅ |
| 162 | MiniMax M1 80k | 0.3142 | 456B | 45.9B | large | ✅ | ✅ |
| 163 | Tri-21B-Think | 0.3130 | 21B | — | small | ✅ | ✅ |
| 164 | Cogito v2.1 | 0.3122 | 671B | 37B | large | ✅ | ✅ |
| 165 | Nemotron 3.5 Lightning | 0.3113 | 31.6B | 3.6B | small | ✅ | ✅ |
| 166 | HyperCLOVA X SEED Think (32B) | 0.3099 | 32B | — | small | ✅ | ✅ |
| 167 | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3083 | 1.6T | 49B | large | ✅ | ❌ |
| 168 | Qwen3 VL 30B A3B | 0.3081 | 30B | 3B | small | ✅ | ✅ |
| 169 | Qwen3 VL 32B | 0.3077 | 33.4B | — | small | ✅ | ❌ |
| 170 | Granite 4.2 30B | 0.3077 | 30B | — | small | ✅ | ✅ |
| 171 | gpt-oss-20b (low) | 0.3065 | 21B | 3.6B | small | ✅ | ✅ |
| 172 | MiniCPM5-2B | 0.3004 | 2.6B | — | tiny | ✅ | ✅ |
| 173 | Nemotron 3 Nano Omni 30B A3B | 0.2994 | 30B | 3B | small | ✅ | ✅ |
| 174 | Mistral Small 4 | 0.2985 | 119B | 6.5B | medium | ✅ | ✅ |
| 175 | MiniMax M1 40k | 0.2967 | 456B | 45.9B | large | ✅ | ✅ |
| 176 | GLM-4.7-Flash (non-reasoning) | 0.2962 | 31.2B | 3B | small | ✅ | ❌ |
| 177 | Qwen3 Next 80B A3B | 0.2959 | 80B | 3B | medium | ✅ | ❌ |
| 178 | Nemotron 3 Nano | 0.2957 | 31.6B | 3.6B | small | ✅ | ✅ |
| 179 | Motif-2-12.7B | 0.2922 | 12.7B | — | small | ❌ | ✅ |
| 180 | INTELLECT-3 | 0.2913 | 107B | 12B | medium | ✅ | ✅ |
| 181 | gpt-oss-20b (high) | 0.2891 | 21B | 3.6B | small | ✅ | ✅ |
| 182 | Ling-1T | 0.2797 | 1T | 50B | large | ✅ | ❌ |
| 183 | gpt-oss-120b (low) | 0.2755 | 117B | 5.1B | medium | ✅ | ✅ |
| 184 | Solar Pro 3 | 0.2744 | 102B | — | medium | ❌ | ✅ |
| 185 | Step3 VL 10B | 0.2722 | 10.2B | — | small | ✅ | ✅ |
| 186 | Qwen3 VL 30B A3B | 0.2713 | 30B | 3B | small | ✅ | ❌ |
| 187 | Qwen3 4B 2507 | 0.2658 | 4.02B | — | tiny | ✅ | ✅ |
| 188 | Qwen3 VL 8B | 0.2634 | 8.77B | — | small | ✅ | ✅ |
| 189 | Mistral Large 3 | 0.2622 | 675B | 41B | large | ✅ | ❌ |
| 190 | K2-V2 (medium) | 0.2591 | 70B | — | medium | ✅ | ✅ |
| 191 | Devstral 2 | 0.2554 | 125B | — | medium | ✅ | ❌ |
| 192 | DeepSeek V3 0324 | 0.2547 | 671B | 37B | large | ✅ | ❌ |
| 193 | NVIDIA Nemotron Nano 12B v2 VL | 0.2544 | 13.2B | — | small | ✅ | ✅ |
| 194 | Qwen3 Omni 30B A3B | 0.2542 | 35.3B | 3B | small | ✅ | ✅ |
| 195 | DeepSeek R1 (Jan) | 0.2532 | 685B | 37B | large | ✅ | ✅ |
| 196 | Granite 4.2 8B | 0.2526 | 8B | — | small | ✅ | ✅ |
| 197 | Qwen3 30B A3B 2507 | 0.2514 | 30.5B | 3.3B | small | ✅ | ✅ |
| 198 | Gemma 4 E4B (non-reasoning) | 0.2503 | 8B | 4.5B | small | ✅ | ❌ |
| 199 | Falcon-H1R-7B | 0.2475 | 7B | — | small | ✅ | ✅ |
| 200 | Hermes 4 405B | 0.2445 | 406B | — | large | ✅ | ✅ |
| 201 | Llama Nemotron Super 49B v1.5 | 0.2436 | 49B | — | medium | ✅ | ✅ |
| 202 | Devstral Small 2 | 0.2430 | 24B | — | small | ✅ | ❌ |
| 203 | Llama 4 Maverick | 0.2339 | 402B | 17B | large | ✅ | ❌ |
| 204 | Qwen3 Coder 30B A3B | 0.2332 | 30.5B | 3.3B | small | ✅ | ❌ |
| 205 | Mistral Small 4 (non-reasoning) | 0.2300 | 119B | 6.5B | medium | ✅ | ❌ |
| 206 | EXAONE 4.0 32B | 0.2282 | 32B | — | small | ✅ | ✅ |
| 207 | Sarvam 105B (high) | 0.2251 | 106B | 10.3B | medium | ✅ | ✅ |
| 208 | MiniCPM5-1B | 0.2238 | 1B | — | tiny | ✅ | ✅ |
| 209 | Magistral Small 1.2 | 0.2205 | 24B | — | small | ✅ | ✅ |
| 210 | Ring-flash-2.0 | 0.2175 | 103B | 6.1B | medium | ✅ | ✅ |
| 211 | GLM-4.5V | 0.2135 | 108B | 12B | medium | ✅ | ✅ |
| 212 | Ling-flash-2.0 | 0.2094 | 103B | 6.1B | medium | ✅ | ❌ |
| 213 | Gemma 4 E4B | 0.2072 | 8B | 4.5B | small | ✅ | ✅ |
| 214 | Qwen3.5 2B | 0.2072 | 2.27B | — | tiny | ✅ | ✅ |
| 215 | Llama Nemotron Ultra | 0.2032 | 253B | — | large | ✅ | ✅ |
| 216 | Qwen3 VL 4B | 0.2024 | 4.44B | — | tiny | ✅ | ✅ |
| 217 | Qwen3 235B | 0.2023 | 235B | 22B | large | ✅ | ✅ |
| 218 | ERNIE 4.5 300B A47B | 0.2004 | 300B | 47B | large | ✅ | ❌ |
| 219 | Llama 3.3 Nemotron Super 49B | 0.1994 | 49B | — | medium | ✅ | ✅ |
| 220 | Devstral Small (May) | 0.1993 | 23.6B | — | small | ✅ | ❌ |
| 221 | Hermes 4 405B (non-reasoning) | 0.1984 | 406B | — | large | ✅ | ❌ |
| 222 | Qwen3 30B A3B 2507 (non-reasoning) | 0.1966 | 30.5B | 3.3B | small | ✅ | ❌ |
| 223 | Mistral Large 2 (Jul) | 0.1965 | 123B | — | medium | ✅ | ❌ |
| 224 | Granite 4.1 30B | 0.1960 | 30B | — | small | ✅ | ❌ |
| 225 | GLM-4.6V (non-reasoning) | 0.1940 | 108B | 12B | medium | ✅ | ❌ |
| 226 | Ministral 3 14B | 0.1939 | 14B | — | small | ✅ | ❌ |
| 227 | Qwen3.5 2B (non-reasoning) | 0.1912 | 2.27B | — | tiny | ✅ | ❌ |
| 228 | Hermes 4 70B | 0.1912 | 70.6B | — | medium | ✅ | ✅ |
| 229 | Llama 3.1 405B | 0.1901 | 405B | — | large | ✅ | ❌ |
| 230 | Qwen2.5 72B | 0.1870 | 72B | — | medium | ✅ | ❌ |
| 231 | Qwen3 Omni 30B A3B | 0.1868 | 35.3B | 3B | small | ✅ | ❌ |
| 232 | K2-V2 (low) | 0.1866 | 70B | — | medium | ✅ | ✅ |
| 233 | MiniCPM5-1B (non-reasoning) | 0.1865 | 1B | — | tiny | ✅ | ❌ |
| 234 | Qwen3 VL 8B | 0.1838 | 8.77B | — | small | ✅ | ❌ |
| 235 | DeepSeek V3 (Dec) | 0.1819 | 671B | 37B | large | ✅ | ❌ |
| 236 | Qwen3 4B | 0.1813 | 4.02B | — | tiny | ✅ | ✅ |
| 237 | LFM2.5-8B-A1B | 0.1789 | 8.3B | 1.5B | small | ✅ | ✅ |
| 238 | Olmo 3.1 32B Think | 0.1779 | 32.2B | — | small | ✅ | ✅ |
| 239 | Qwen3 30B | 0.1749 | 30.5B | 3.3B | small | ✅ | ✅ |
| 240 | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.1725 | 49B | — | medium | ✅ | ❌ |
| 241 | G9v3-3B | 0.1720 | 3B | — | tiny | ✅ | ✅ |
| 242 | Mistral Small 3.2 | 0.1714 | 24B | — | small | ✅ | ❌ |
| 243 | Qwen3 235B (non-reasoning) | 0.1693 | 235B | 22B | large | ✅ | ❌ |
| 244 | Mistral Large 2 (Nov) | 0.1679 | 123B | — | medium | ✅ | ❌ |
| 245 | Granite 4.2 3B | 0.1677 | 3B | — | tiny | ✅ | ✅ |
| 246 | Gemma 4 E2B (non-reasoning) | 0.1668 | 5.1B | 2.3B | small | ✅ | ❌ |
| 247 | Qwen3 32B | 0.1665 | 32.8B | — | small | ✅ | ✅ |
| 248 | NVIDIA Nemotron Nano 9B V2 | 0.1643 | 9B | — | small | ✅ | ✅ |
| 249 | Llama 4 Scout | 0.1642 | 109B | 17B | medium | ✅ | ❌ |
| 250 | GLM-4.5V (non-reasoning) | 0.1634 | 108B | 12B | medium | ✅ | ❌ |
| 251 | Sarvam 30B (high) | 0.1631 | 32.2B | 2.4B | small | ✅ | ✅ |
| 252 | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1631 | 9B | — | small | ✅ | ❌ |
| 253 | Devstral Small | 0.1624 | 24B | — | small | ✅ | ❌ |
| 254 | Qwen3 4B 2507 (non-reasoning) | 0.1614 | 4.02B | — | tiny | ✅ | ❌ |
| 255 | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1592 | 13.2B | — | small | ✅ | ❌ |
| 256 | Command A | 0.1591 | 111B | — | medium | ✅ | ❌ |
| 257 | Ministral 3 8B | 0.1588 | 8B | — | small | ✅ | ❌ |
| 258 | Kimi Linear 48B A3B Instruct | 0.1574 | 49.1B | 3B | medium | ✅ | ❌ |
| 259 | MiniCPM-V 4.6 1.3B | 0.1553 | 1.3B | — | tiny | ✅ | ❌ |
| 260 | Qwen3 14B | 0.1550 | 14.8B | — | small | ✅ | ✅ |
| 261 | Magistral Small 1 | 0.1526 | 23.6B | — | small | ✅ | ✅ |
| 262 | Qwen3 VL 4B | 0.1525 | 4.44B | — | tiny | ✅ | ❌ |
| 263 | Nanbeige4.1-3B | 0.1506 | 3.93B | — | tiny | ✅ | ✅ |
| 264 | Gemma 4 E2B | 0.1501 | 5.1B | 2.3B | small | ✅ | ✅ |
| 265 | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1484 | 49B | — | medium | ✅ | ❌ |
| 266 | Olmo 3 32B Think | 0.1483 | 32.2B | — | small | ✅ | ✅ |
| 267 | EXAONE 4.0 32B (non-reasoning) | 0.1471 | 32B | — | small | ✅ | ❌ |
| 268 | Mistral Small 3 | 0.1459 | 24B | — | small | ✅ | ❌ |
| 269 | Nemotron 3 Nano (non-reasoning) | 0.1412 | 31.6B | 3.6B | small | ✅ | ❌ |
| 270 | Olmo 3.1 32B Instruct | 0.1400 | 32.2B | — | small | ✅ | ❌ |
| 271 | Llama 3.3 70B | 0.1367 | 70B | — | medium | ✅ | ❌ |
| 272 | Qwen3 30B (non-reasoning) | 0.1361 | 30.5B | 3.3B | small | ✅ | ❌ |
| 273 | Llama 3.1 Nemotron 70B | 0.1341 | 70B | — | medium | ✅ | ❌ |
| 274 | Jamba Reasoning 3B | 0.1328 | 3B | — | tiny | ✅ | ✅ |
| 275 | Granite 4.1 8B | 0.1310 | 8B | — | small | ✅ | ❌ |
| 276 | Jamba 1.7 Large | 0.1277 | 398B | 94B | large | ✅ | ❌ |
| 277 | Llama 3.1 70B | 0.1263 | 70B | — | medium | ✅ | ❌ |
| 278 | Qwen3 8B | 0.1256 | 8.19B | — | small | ✅ | ✅ |
| 279 | LFM2 24B A2B | 0.1245 | 23.8B | 2.3B | small | ✅ | ❌ |
| 280 | Ling-mini-2.0 | 0.1224 | 16.3B | 1.4B | small | ✅ | ❌ |
| 281 | Qwen3 14B (non-reasoning) | 0.1212 | 14.8B | — | small | ✅ | ❌ |
| 282 | Nemotron 3 Nano 4B | 0.1208 | 3.97B | — | tiny | ✅ | ✅ |
| 283 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1173 | 4.51B | — | small | ✅ | ✅ |
| 284 | Granite 4.0 H Small | 0.1166 | 32B | 9B | small | ✅ | ❌ |
| 285 | LFM2.5-2.6B | 0.1165 | 2.7B | — | tiny | ✅ | ✅ |
| 286 | Hermes 4 70B (non-reasoning) | 0.1137 | 70.6B | — | medium | ✅ | ❌ |
| 287 | Llama 3.2 3B | 0.1124 | 3B | — | tiny | ✅ | ❌ |
| 288 | DeepSeek R1 Distill Llama 70B | 0.1120 | 70B | — | medium | ✅ | ✅ |
| 289 | Olmo 3 7B Think | 0.1114 | 7B | — | small | ✅ | ✅ |
| 290 | LFM2.5-1.2B-Thinking | 0.1099 | 1.17B | — | tiny | ✅ | ✅ |
| 291 | DeepSeek R1 0528 Qwen3 8B | 0.1094 | 8.19B | — | small | ✅ | ✅ |
| 292 | Ministral 3 3B | 0.1052 | 3B | — | tiny | ✅ | ❌ |
| 293 | Gemma 3 27B | 0.1043 | 27.4B | — | small | ✅ | ❌ |
| 294 | Qwen3 8B (non-reasoning) | 0.1037 | 8.19B | — | small | ✅ | ❌ |
| 295 | LFM2.5-1.2B-Instruct | 0.0993 | 1.17B | — | tiny | ✅ | ❌ |
| 296 | Qwen3.5 0.8B (non-reasoning) | 0.0970 | 0.873B | — | tiny | ✅ | ❌ |
| 297 | Jamba 1.7 Mini | 0.0963 | 52B | 12B | medium | ✅ | ❌ |
| 298 | Exaone 4.0 1.2B | 0.0946 | 1.28B | — | tiny | ✅ | ✅ |
| 299 | Llama 3.2 11B (Vision) | 0.0904 | 11B | — | small | ✅ | ❌ |
| 300 | Exaone 4.0 1.2B (non-reasoning) | 0.0889 | 1.28B | — | tiny | ✅ | ❌ |
| 301 | Olmo 3 7B | 0.0888 | 7B | — | small | ✅ | ❌ |
| 302 | Molmo2-8B | 0.0871 | 8.66B | — | small | ✅ | ❌ |
| 303 | Qwen3 1.7B | 0.0859 | 2.03B | — | tiny | ✅ | ✅ |
| 304 | Phi-4 | 0.0839 | 14B | — | small | ✅ | ❌ |
| 305 | Reka Flash 3 | 0.0835 | 21B | — | small | ✅ | ✅ |
| 306 | Granite 4.1 3B | 0.0807 | 3B | — | tiny | ✅ | ❌ |
| 307 | OLMo 2 32B | 0.0795 | 32.2B | — | small | ✅ | ❌ |
| 308 | LFM2 8B A1B | 0.0758 | 8.34B | 1.5B | small | ✅ | ❌ |
| 309 | Gemma 3 12B | 0.0735 | 12.2B | — | small | ✅ | ❌ |
| 310 | Granite 4.0 Micro | 0.0735 | 3B | — | tiny | ✅ | ❌ |
| 311 | Llama 3 70B | 0.0729 | 70B | — | medium | ✅ | ❌ |
| 312 | Granite 4.0 H 1B | 0.0707 | 1.5B | — | tiny | ✅ | ❌ |
| 313 | LFM2.5-VL-1.6B | 0.0705 | 1.6B | — | tiny | ✅ | ❌ |
| 314 | Sarvam M | 0.0681 | 23.6B | — | small | ✅ | ✅ |
| 315 | Llama 3.1 8B | 0.0651 | 8B | — | small | ✅ | ❌ |
| 316 | Granite 4.0 1B | 0.0644 | 1.6B | — | tiny | ✅ | ❌ |
| 317 | Phi-3 Mini | 0.0628 | 3.8B | — | tiny | ✅ | ❌ |
| 318 | Granite 3.3 8B (non-reasoning) | 0.0625 | 8.17B | — | small | ✅ | ❌ |
| 319 | Qwen3 1.7B (non-reasoning) | 0.0548 | 2.03B | — | tiny | ✅ | ❌ |
| 320 | Qwen3.5 0.8B | 0.0543 | 0.873B | — | tiny | ✅ | ✅ |
| 321 | Gemma 3 4B | 0.0524 | 4.3B | — | tiny | ✅ | ❌ |
| 322 | Qwen3 0.6B | 0.0518 | 0.752B | — | tiny | ✅ | ✅ |
| 323 | Apertus 70B Instruct | 0.0498 | 70B | — | medium | ✅ | ❌ |
| 324 | LFM2 2.6B | 0.0448 | 2.57B | — | tiny | ✅ | ❌ |
| 325 | Phi-4 Mini | 0.0430 | 3.84B | — | tiny | ✅ | ❌ |
| 326 | OLMo 2 7B | 0.0411 | 7.3B | — | small | ✅ | ❌ |
| 327 | Gemma 3n E4B | 0.0397 | 8.39B | 4B | small | ✅ | ❌ |
| 328 | Apertus 8B Instruct | 0.0355 | 8B | — | small | ✅ | ❌ |
| 329 | Qwen3 0.6B (non-reasoning) | 0.0351 | 0.752B | — | tiny | ✅ | ❌ |
| 330 | Granite 4.0 H 350M | 0.0340 | 0.34B | — | tiny | ✅ | ❌ |
| 331 | LFM2 1.2B | 0.0331 | 1.17B | — | tiny | ✅ | ❌ |
| 332 | Molmo 7B-D | 0.0307 | 8.02B | — | small | ✅ | ❌ |
| 333 | Llama 3 8B | 0.0299 | 8B | — | small | ✅ | ❌ |
| 334 | Granite 4.0 350M | 0.0264 | 0.35B | — | tiny | ✅ | ❌ |
| 335 | Gemma 3 1B | 0.0264 | 1B | — | tiny | ✅ | ❌ |
| 336 | Tiny Aya Global | 0.0222 | 3.35B | — | tiny | ✅ | ❌ |
| 337 | Llama 3.2 1B | 0.0207 | 1B | — | tiny | ✅ | ❌ |
| 338 | K2 Horizon 0.9B | 0.0139 | 0.9B | — | tiny | ✅ | ✅ |
| 339 | Gemma 3n E2B | 0.0117 | 5.98B | 2B | small | ✅ | ❌ |
| 340 | Mistral 7B | 0.0035 | 7B | — | small | ✅ | ❌ |
| 341 | Gemma 3 270M | 0.0000 | 0.268B | — | tiny | ✅ | ❌ |

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
| <img src="https://artificialanalysis.ai/img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 8 |
| <img src="https://artificialanalysis.ai/img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | `#1521a9` | 5 |
| <img src="https://artificialanalysis.ai/img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | `#3B62EC` | 2 |
| <img src="https://artificialanalysis.ai/img/logos/ibm.svg" width="18" alt="IBM" /> IBM | `#0f62fe` | 5 |

## 基准测试动态标定（Leave-One-Out Calibration）

不同基准测试的参测模型群体能力分布存在差异（例如部分高难度或专业领域基准测试仅覆盖头部高能力模型）。系统在标准归一化之后执行了**留一交叉动态映射标定流程**：

1. **排除单项基准**：暂时排除某项基准测试，计算各模型在其余测试项上的平均能力；
2. **全域归一化评估**：将排除后的平均能力归一化至 `[0, 1]`；
3. **锁定参测区间**：提取实际参测该基准测试的所有模型，以它们排除该项后的能力最高值和最低值分别作为该项的新映射上界和下界；
4. **并行同步迭代**：所有基准测试以 `[0, 1]` 为初值同步更新，完成一轮后以新上下界作为输入进入下一轮，重复迭代直至收敛。

> 标定状态：已完成 **13** 轮并行迭代收敛（容差阈值 $\Delta < 1e-05$）。标定得到的数据作为新指标独立保存，不覆盖原始基准测试归一化与综合能力。

| 基准测试项 | 英文标识 | 参测模型数 | 标定映射下界 | 标定映射上界 | 映射跨度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| AA Intelligence Index | `intelligenceIndex` | 78 | `0.1726` | `1.0000` | `0.8274` |
| GPQA Diamond | `gpqa` | 535 | `0.0000` | `0.9087` | `0.9087` |
| Humanity's Last Exam | `hle` | 603 | `0.0000` | `1.0000` | `1.0000` |
| MMMU Pro | `mmmuPro` | 291 | `0.0168` | `0.9431` | `0.9263` |
| IFBench Instruction Following | `ifbench` | 442 | `0.0000` | `0.8833` | `0.8833` |
| SciCode Coding | `scicode` | 244 | `0.0399` | `1.0000` | `0.9601` |
| CritPt Physics | `critpt` | 589 | `0.0000` | `1.0000` | `1.0000` |
| AA-LCR Long Context | `lcr` | 581 | `0.0000` | `1.0000` | `1.0000` |
| AA Omniscience Index | `omniscience` | 99 | `0.1726` | `1.0000` | `0.8274` |
| AA-Omniscience Accuracy | `omniscienceAccuracy` | 99 | `0.1695` | `1.0000` | `0.8305` |
| AA-Omniscience Non-Hallucination | `omniscienceNonHallucination` | 99 | `0.1670` | `1.0000` | `0.8330` |
| GDPval-AA Normalized | `gdpvalNormalized` | 307 | `0.0399` | `1.0000` | `0.9601` |
| AA Analyst Agent | `analystAgent` | 51 | `0.3369` | `0.9464` | `0.6094` |
| APEX-Agents-AA | `apexAgents` | 33 | `0.3065` | `0.8081` | `0.5016` |
| ITBench-SRE | `itbenchSre` | 45 | `0.1506` | `0.9650` | `0.8144` |
| τ²-Bench Telecom | `tau2` | 438 | `0.0000` | `0.8826` | `0.8826` |
| τ³-Bench Banking | `tauBanking` | 209 | `0.0301` | `0.9132` | `0.8831` |
| Terminal-Bench Hard | `terminalbenchHard` | 431 | `0.0033` | `0.8723` | `0.8690` |
| Terminal-Bench 2.1 | `terminalbenchV21` | 242 | `0.0386` | `0.9053` | `0.8666` |
| Terminal-Bench 4.0 | `terminalbenchV40` | 233 | `0.0400` | `1.0000` | `0.9600` |


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

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 0.26，r = B/C = 3.87386），用 11 品牌前沿入图模型的总参数量定出；mse = 0.003414，maxdev = 0.1034。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 71，10B–100B: 110，100B–1T: 138，1T–2.8T: 10
- 中位数位置 0.565；左 115 个，右 226 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.170，10^1→ 0.396，10^2→ 0.642，10^3→ 0.889

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
**模型数（有参数量数据）**: 341（总体帕累托前沿 19 个；图表入图 341 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 选定品牌的单独帕累托前沿（共 10 个品牌，（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.0000，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 0 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
