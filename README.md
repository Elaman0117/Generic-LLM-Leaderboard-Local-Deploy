# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.1216，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 283 个入图，50 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3 (max) | 0.8514 | 2.8T | 104B | large | ✅ | ✅ |
| 2 | GLM-5.3 (max) | 0.8297 | 753B | 40B | large | ✅ | ✅ |
| 3 | MiMo-V2.6-Pro | 0.8283 | 1T | 42B | large | ✅ | ✅ |
| 4 | Step 5 Preview | 0.8108 | 600B | — | large | ❌ | ✅ |
| 5 | Qwen3.8 2.4T A95B | 0.7911 | 2.4T | 95B | large | ✅ | ✅ |
| 6 | GLM-5.3-Flash | 0.7773 | 320B | 18B | large | ✅ | ✅ |
| 7 | GLM-5.2 (max) | 0.7724 | 753B | 40B | large | ✅ | ✅ |
| 8 | Qwen3.8-Flash-Next | 0.7355 | 180B | 6B | large | ✅ | ✅ |
| 9 | DeepSeek V4 Pro 0813 (max) | 0.7066 | 1.6T | 49B | large | ✅ | ✅ |
| 10 | Kimi K2.6 | 0.6904 | 1T | 32B | large | ✅ | ✅ |
| 11 | Qwen3.8 27B (xhigh) | 0.6856 | 27B | — | small | ✅ | ✅ |
| 12 | DeepSeek V4.1 Flash (max) | 0.6823 | 552B | 16B | large | ✅ | ✅ |
| 13 | DeepSeek V4 Flash Vision (max) | 0.6714 | 284B | — | large | ❌ | ✅ |
| 14 | DeepSeek V4 Flash 0731 (max) | 0.6684 | 284B | 13B | large | ✅ | ✅ |
| 15 | Motif 3 | 0.6603 | 314B | 13.2B | large | ✅ | ✅ |
| 16 | Kimi K3 (low) | 0.6598 | 2.8T | 104B | large | ✅ | ✅ |
| 17 | MiniMax-M3 | 0.6561 | 428B | 23B | large | ✅ | ✅ |
| 18 | DeepSeek V4 Pro (max) | 0.6455 | 1.6T | 49B | large | ✅ | ✅ |
| 19 | GLM-5.1 | 0.6399 | 744B | 40B | large | ✅ | ✅ |
| 20 | DeepSeek V4 Pro (high) | 0.6333 | 1.6T | 49B | large | ✅ | ✅ |
| 21 | GLM-5 | 0.6303 | 744B | 40B | large | ✅ | ✅ |
| 22 | K2 Horizon 375B A23B | 0.6242 | 375B | 23B | large | ✅ | ✅ |
| 23 | Kimi K2.7 Code | 0.6191 | 1T | 32B | large | ✅ | ✅ |
| 24 | Ling-3.0-flash-VL | 0.6015 | 124B | 5.5B | medium | ✅ | ✅ |
| 25 | Inkling Small | 0.5978 | 266B | 12B | large | ✅ | ✅ |
| 26 | MiMo-V2.5-Pro | 0.5974 | 1T | 42B | large | ✅ | ✅ |
| 27 | MiMo-V2.5 | 0.5942 | 310B | 15B | large | ✅ | ✅ |
| 28 | DeepSeek V4 Flash (max) | 0.5935 | 284B | 13B | large | ✅ | ✅ |
| 29 | Inkling | 0.5913 | 975B | 41B | large | ✅ | ✅ |
| 30 | DeepSeek V4 Flash (high) | 0.5909 | 284B | 13B | large | ✅ | ✅ |
| 31 | Solar Open2 250B | 0.5784 | 250B | 15B | large | ✅ | ✅ |
| 32 | Qwen3.5 27B | 0.5769 | 27.8B | — | small | ✅ | ✅ |
| 33 | MiMo-V2-Flash (Feb 2026) | 0.5765 | 309B | 15B | large | ✅ | ✅ |
| 34 | Quasar 438B (max) | 0.5747 | 438B | — | large | ❌ | ✅ |
| 35 | Nex-N2-Pro | 0.5737 | 397B | 17B | large | ✅ | ✅ |
| 36 | Motif 3 (Beta) | 0.5714 | 314B | — | large | ❌ | ✅ |
| 37 | Qwen3.6 27B | 0.5701 | 27.8B | — | small | ✅ | ✅ |
| 38 | Kimi K2.5 | 0.5682 | 1T | 32B | large | ✅ | ✅ |
| 39 | Nemotron 3 Ultra | 0.5642 | 550B | 55B | large | ✅ | ✅ |
| 40 | Kimi K2 Thinking | 0.5602 | 1T | 32B | large | ✅ | ✅ |
| 41 | Qwen3.8 27B (medium) | 0.5548 | 27B | — | small | ✅ | ✅ |
| 42 | Qwen3.5 397B A17B | 0.5545 | 397B | 17B | large | ✅ | ✅ |
| 43 | Kimi K2.6 (Non-reasoning) | 0.5532 | 1T | 32B | large | ✅ | ❌ |
| 44 | A.X-K2 | 0.5457 | 692B | 33B | large | ✅ | ✅ |
| 45 | MiniMax-M2.7 | 0.5446 | 230B | 10B | large | ✅ | ✅ |
| 46 | Hy3 | 0.5441 | 299B | 21B | large | ✅ | ✅ |
| 47 | K2 Horizon MoVA 36B A4B | 0.5412 | 36B | 4B | small | ✅ | ✅ |
| 48 | Hy3-preview | 0.5400 | 295B | 21B | large | ✅ | ✅ |
| 49 | Qwen3.8 27B (low) | 0.5398 | 27B | — | small | ✅ | ✅ |
| 50 | MiniMax-M2.5 | 0.5348 | 230B | 10B | large | ✅ | ✅ |
| 51 | GLM-5.1 (Non-reasoning) | 0.5337 | 744B | 40B | large | ✅ | ❌ |
| 52 | Qwen3.6 35B A3B | 0.5297 | 36B | 3B | small | ✅ | ✅ |
| 53 | JT-4.1 Flash 236B A21B | 0.5285 | 236B | — | large | ❌ | ❌ |
| 54 | Ling 3.0 Flash | 0.5234 | 124B | 5.1B | medium | ✅ | ✅ |
| 55 | Agnes 2.5 Pro Alpha | 0.5217 | 397B | 17B | large | ✅ | ✅ |
| 56 | MiniMax-M2.1 | 0.5200 | 230B | 10B | large | ✅ | ✅ |
| 57 | Qwen3.5 122B A10B | 0.5180 | 125B | 10B | medium | ✅ | ✅ |
| 58 | Qwen3.5 35B A3B | 0.5147 | 36B | 3B | small | ✅ | ✅ |
| 59 | Step 3.7 Flash | 0.5143 | 198B | 11B | large | ✅ | ✅ |
| 60 | G9v3-39A5B | 0.5117 | 39B | 5B | small | ✅ | ✅ |
| 61 | Kimi K2.5 (Non-reasoning) | 0.5095 | 1T | 32B | large | ✅ | ❌ |
| 62 | MiMo-V2-Flash | 0.5083 | 309B | 15B | large | ✅ | ✅ |
| 63 | GLM-4.7 | 0.5022 | 357B | 32B | large | ✅ | ✅ |
| 64 | DeepSeek V3.2 | 0.5000 | 685B | 37B | large | ✅ | ✅ |
| 65 | Gemma 4 31B | 0.4990 | 30.7B | — | small | ✅ | ✅ |
| 66 | GLM-5 (Non-reasoning) | 0.4986 | 744B | 40B | large | ✅ | ❌ |
| 67 | Qwen3.8 27B | 0.4980 | 27B | — | small | ✅ | ❌ |
| 68 | Ling-3.0-flash-Fin | 0.4929 | 124B | 5.1B | medium | ✅ | ✅ |
| 69 | Qwen3.5 397B A17B (Non-reasoning) | 0.4920 | 397B | 17B | large | ✅ | ❌ |
| 70 | Muse Glimmer (high) | 0.4856 | 30B | — | small | ✅ | ✅ |
| 71 | Qwen3.5 27B (Non-reasoning) | 0.4775 | 27.8B | — | small | ✅ | ❌ |
| 72 | DeepSeek V3.2 Speciale | 0.4763 | 685B | 37B | large | ✅ | ✅ |
| 73 | JT-35B-Flash | 0.4754 | 35B | — | small | ❌ | ❌ |
| 74 | Step 3.5 Flash | 0.4746 | 196B | 11B | large | ✅ | ✅ |
| 75 | K-EXAONE 2.0 | 0.4727 | 750B | 37B | large | ✅ | ✅ |
| 76 | Command A+ | 0.4675 | 218B | 25B | large | ✅ | ✅ |
| 77 | Ring-2.6-1T | 0.4651 | 1T | 63B | large | ✅ | ✅ |
| 78 | MiniMax-M2 | 0.4622 | 230B | 10B | large | ✅ | ✅ |
| 79 | Mistral Medium 3.5 | 0.4578 | 128B | — | medium | ✅ | ✅ |
| 80 | K2 Horizon 7B | 0.4549 | 7B | — | small | ✅ | ✅ |
| 81 | DeepSeek V4 Pro (Non-reasoning) | 0.4478 | 1.6T | 49B | large | ✅ | ❌ |
| 82 | GLM-5.2 (Non-reasoning) | 0.4358 | 753B | 40B | large | ✅ | ❌ |
| 83 | LongCat 2.0 | 0.4350 | 1.6T | 48B | large | ✅ | ✅ |
| 84 | Qwen3.6 27B (Non-reasoning) | 0.4345 | 27.8B | — | small | ✅ | ❌ |
| 85 | DeepSeek V3.2 Exp | 0.4312 | 685B | 37B | large | ✅ | ✅ |
| 86 | DeepSeek V3.1 Terminus | 0.4269 | 685B | 37B | large | ✅ | ✅ |
| 87 | Qwen3.5 122B A10B (Non-reasoning) | 0.4169 | 125B | 10B | medium | ✅ | ❌ |
| 88 | Qwen3.5 9B | 0.4137 | 9.65B | — | small | ✅ | ✅ |
| 89 | MiMo-V2.5-Pro (Non-reasoning) | 0.4101 | 1T | 42B | large | ✅ | ❌ |
| 90 | Kimi K2 0905 | 0.4073 | 1T | 32B | large | ✅ | ❌ |
| 91 | DeepSeek V4 Flash (Non-reasoning) | 0.4060 | 284B | 13B | large | ✅ | ❌ |
| 92 | Qwen3 VL 235B A22B (Reasoning) | 0.4060 | 235B | 22B | large | ✅ | ✅ |
| 93 | Gemma 4 26B A4B | 0.4049 | 25.2B | 3.8B | small | ✅ | ✅ |
| 94 | Ling-2.6-1T | 0.4032 | 1T | 63B | large | ✅ | ❌ |
| 95 | DeepSeek V3.2 (Non-reasoning) | 0.3976 | 685B | 37B | large | ✅ | ❌ |
| 96 | EXAONE 4.5 33B | 0.3966 | 34.4B | — | small | ✅ | ✅ |
| 97 | Qwen3.5 4B | 0.3959 | 4.66B | — | small | ✅ | ✅ |
| 98 | Hy3-preview (Non-reasoning) | 0.3958 | 295B | 21B | large | ✅ | ❌ |
| 99 | Ling 3.0 Tiny | 0.3930 | 7.9B | 1.3B | small | ✅ | ✅ |
| 100 | GLM-4.7 (Non-reasoning) | 0.3929 | 357B | 32B | large | ✅ | ❌ |
| 101 | Qwen3.6 35B A3B (Non-reasoning) | 0.3854 | 36B | 3B | small | ✅ | ❌ |
| 102 | Gemma 4 12B | 0.3854 | 12B | — | small | ✅ | ✅ |
| 103 | DeepSeek V3.1 | 0.3845 | 685B | 37B | large | ✅ | ✅ |
| 104 | GLM-4.5 | 0.3839 | 355B | 32B | large | ✅ | ✅ |
| 105 | MiniCPM5-2B | 0.3774 | 2.6B | — | tiny | ✅ | ✅ |
| 106 | Kimi K2 | 0.3745 | 1T | 32B | large | ✅ | ❌ |
| 107 | DeepSeek R1 0528 | 0.3732 | 685B | 37B | large | ✅ | ✅ |
| 108 | K-EXAONE | 0.3724 | 236B | 23B | large | ✅ | ✅ |
| 109 | GLM-4.6 | 0.3723 | 357B | 32B | large | ✅ | ✅ |
| 110 | Gemma 4 31B (Non-reasoning) | 0.3692 | 30.7B | — | small | ✅ | ❌ |
| 111 | Qwen3 VL 32B (Reasoning) | 0.3641 | 33.4B | — | small | ✅ | ✅ |
| 112 | K2 Horizon 3.7B | 0.3640 | 3.7B | — | tiny | ✅ | ✅ |
| 113 | Nemotron 3 Super | 0.3636 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 114 | Trinity Large Thinking | 0.3624 | 399B | 13B | large | ✅ | ✅ |
| 115 | Granite 4.2 30B | 0.3621 | 30B | — | small | ✅ | ✅ |
| 116 | Qwen3.5 9B (Non-reasoning) | 0.3602 | 9.65B | — | small | ✅ | ❌ |
| 117 | GLM-4.7-Flash | 0.3601 | 31.2B | 3B | small | ✅ | ✅ |
| 118 | GLM-4.6 (Non-reasoning) | 0.3566 | 357B | 32B | large | ✅ | ❌ |
| 119 | Qwen3.5 35B A3B (Non-reasoning) | 0.3564 | 36B | 3B | small | ✅ | ❌ |
| 120 | Nemotron 3.5 Lightning | 0.3554 | 31.6B | 3.6B | small | ✅ | ✅ |
| 121 | Apriel-v1.5-15B-Thinker | 0.3529 | 15B | — | small | ✅ | ✅ |
| 122 | Qwen3 235B A22B 2507 | 0.3511 | 235B | 22B | large | ✅ | ✅ |
| 123 | Qwen3 Coder 480B | 0.3481 | 480B | 35B | large | ✅ | ❌ |
| 124 | Nemotron Cascade 2 30B A3B | 0.3470 | 31.6B | 3B | small | ✅ | ✅ |
| 125 | Cogito v2.1 | 0.3468 | 671B | 37B | large | ✅ | ✅ |
| 126 | Apriel-v1.6-15B-Thinker | 0.3429 | 15B | — | small | ✅ | ✅ |
| 127 | Gemma 4 26B A4B (Non-reasoning) | 0.3418 | 25.2B | 3.8B | small | ✅ | ❌ |
| 128 | G9v3-3B | 0.3417 | 3B | — | tiny | ✅ | ✅ |
| 129 | GLM-4.6V | 0.3406 | 108B | 12B | medium | ✅ | ✅ |
| 130 | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3399 | 685B | 37B | large | ✅ | ❌ |
| 131 | gpt-oss-120b (high) | 0.3390 | 117B | 5.1B | medium | ✅ | ✅ |
| 132 | MiMo-V2-Flash (Non-reasoning) | 0.3313 | 309B | 15B | large | ✅ | ❌ |
| 133 | Mistral Small 4 | 0.3260 | 119B | 6.5B | medium | ✅ | ✅ |
| 134 | DeepSeek V3.2 Exp (Non-reasoning) | 0.3227 | 685B | 37B | large | ✅ | ❌ |
| 135 | HyperNova 60B 2605 (high) | 0.3210 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 136 | DeepSeek V3.1 (Non-reasoning) | 0.3196 | 685B | 37B | large | ✅ | ❌ |
| 137 | North Mini Code | 0.3169 | 30B | 3B | small | ✅ | ✅ |
| 138 | Seed-OSS-36B-Instruct | 0.3159 | 36.2B | — | small | ✅ | ✅ |
| 139 | Granite 4.2 8B | 0.3101 | 8B | — | small | ✅ | ✅ |
| 140 | Solar Pro 3 | 0.3093 | 102B | — | medium | ❌ | ✅ |
| 141 | Qwen3 235B 2507 | 0.3086 | 235B | 22B | large | ✅ | ❌ |
| 142 | K2 Think V2 | 0.3079 | 70B | — | medium | ✅ | ✅ |
| 143 | Qwen3 Next 80B A3B (Reasoning) | 0.3017 | 80B | 3B | medium | ✅ | ✅ |
| 144 | Gemma 4 12B (Non-reasoning) | 0.3005 | 12B | — | small | ✅ | ❌ |
| 145 | Qwen3 VL 235B A22B | 0.2998 | 235B | — | large | ✅ | ❌ |
| 146 | Nemotron 3 Nano | 0.2997 | 31.6B | 3.6B | small | ✅ | ✅ |
| 147 | QwQ-32B | 0.2980 | 32.8B | — | small | ✅ | ✅ |
| 148 | Ring-1T | 0.2970 | 1T | 50B | large | ✅ | ✅ |
| 149 | MiniCPM5-1B | 0.2970 | 1B | — | tiny | ✅ | ✅ |
| 150 | MiniCPM5-1B (Non-reasoning) | 0.2968 | 1B | — | tiny | ✅ | ❌ |
| 151 | Pixtral Large | 0.2957 | 124B | — | medium | ✅ | ❌ |
| 152 | Solar Open 100B | 0.2924 | 102B | 12B | medium | ✅ | ✅ |
| 153 | Qwen3.5 4B (Non-reasoning) | 0.2902 | 4.66B | — | small | ✅ | ❌ |
| 154 | Qwen3 Coder Next | 0.2897 | 79.7B | 3B | medium | ✅ | ❌ |
| 155 | GLM-4.5-Air | 0.2890 | 106B | 12B | medium | ✅ | ✅ |
| 156 | MiniMax M1 80k | 0.2888 | 456B | 45.9B | large | ✅ | ✅ |
| 157 | Gemma 4 E4B | 0.2881 | 8B | 4.5B | small | ✅ | ✅ |
| 158 | DiffusionGemma 26B A4B | 0.2835 | 25.2B | 3.8B | small | ✅ | ✅ |
| 159 | MiniMax M1 40k | 0.2821 | 456B | 45.9B | large | ✅ | ✅ |
| 160 | HyperCLOVA X SEED Think (32B) | 0.2820 | 32B | — | small | ✅ | ✅ |
| 161 | K2-V2 (high) | 0.2798 | 70B | — | medium | ✅ | ✅ |
| 162 | K-EXAONE (Non-reasoning) | 0.2796 | 236B | 23B | large | ✅ | ❌ |
| 163 | DeepSeek V3 0324 | 0.2784 | 671B | 37B | large | ✅ | ❌ |
| 164 | DeepSeek R1 (Jan) | 0.2760 | 685B | 37B | large | ✅ | ✅ |
| 165 | Mistral Large 3 | 0.2753 | 675B | 41B | large | ✅ | ❌ |
| 166 | Llama 4 Maverick | 0.2740 | 402B | 17B | large | ✅ | ❌ |
| 167 | gpt-oss-20b (high) | 0.2710 | 21B | 3.6B | small | ✅ | ✅ |
| 168 | INTELLECT-3 | 0.2703 | 107B | 12B | medium | ✅ | ✅ |
| 169 | Nemotron 3 Nano Omni 30B A3B | 0.2698 | 30B | 3B | small | ✅ | ✅ |
| 170 | Tri-21B-think Preview | 0.2695 | 21B | — | small | ✅ | ✅ |
| 171 | LongCat Flash Lite | 0.2679 | 68.5B | 3B | medium | ✅ | ❌ |
| 172 | Qwen3 VL 30B A3B (Reasoning) | 0.2676 | 30B | 3B | small | ✅ | ✅ |
| 173 | Qwen3 30B A3B 2507 | 0.2676 | 30.5B | 3.3B | small | ✅ | ✅ |
| 174 | gpt-oss-20b (low) | 0.2672 | 21B | 3.6B | small | ✅ | ✅ |
| 175 | Llama 3.1 405B | 0.2661 | 405B | — | large | ✅ | ❌ |
| 176 | Ling 2.6 Flash | 0.2646 | 107B | 7.4B | medium | ✅ | ❌ |
| 177 | Gemma 4 E4B (Non-reasoning) | 0.2641 | 8B | 4.5B | small | ✅ | ❌ |
| 178 | Tri-21B-Think | 0.2639 | 21B | — | small | ✅ | ✅ |
| 179 | Granite 4.2 3B | 0.2591 | 3B | — | tiny | ✅ | ✅ |
| 180 | Qwen3 Next 80B A3B | 0.2562 | 80B | 3B | medium | ✅ | ❌ |
| 181 | Qwen3 VL 32B | 0.2560 | 33.4B | — | small | ✅ | ❌ |
| 182 | Hermes 4 405B | 0.2543 | 406B | — | large | ✅ | ✅ |
| 183 | K2-V2 (medium) | 0.2519 | 70B | — | medium | ✅ | ✅ |
| 184 | Ling-1T | 0.2511 | 1T | 50B | large | ✅ | ❌ |
| 185 | Motif-2-12.7B | 0.2506 | 12.7B | — | small | ❌ | ✅ |
| 186 | gpt-oss-120b (low) | 0.2503 | 117B | 5.1B | medium | ✅ | ✅ |
| 187 | Qwen3 VL 8B (Reasoning) | 0.2475 | 8.77B | — | small | ✅ | ✅ |
| 188 | Step3 VL 10B | 0.2458 | 10.2B | — | small | ✅ | ✅ |
| 189 | Llama Nemotron Super 49B v1.5 | 0.2437 | 49B | — | medium | ✅ | ✅ |
| 190 | GLM-4.7-Flash (Non-reasoning) | 0.2433 | 31.2B | 3B | small | ✅ | ❌ |
| 191 | Devstral 2 | 0.2415 | 125B | — | medium | ✅ | ❌ |
| 192 | ERNIE 4.5 300B A47B | 0.2407 | 300B | 47B | large | ✅ | ❌ |
| 193 | Qwen3 4B 2507 | 0.2377 | 4.02B | — | tiny | ✅ | ✅ |
| 194 | Mistral Small 4 (Non-reasoning) | 0.2366 | 119B | 6.5B | medium | ✅ | ❌ |
| 195 | Hermes 4 405B (Non-reasoning) | 0.2355 | 406B | — | large | ✅ | ❌ |
| 196 | Qwen3 Coder 30B A3B | 0.2342 | 30.5B | 3.3B | small | ✅ | ❌ |
| 197 | LFM2.5-8B-A1B | 0.2320 | 8.3B | 1.5B | small | ✅ | ✅ |
| 198 | Qwen3 VL 30B A3B | 0.2312 | 30B | 3B | small | ✅ | ❌ |
| 199 | GLM-4.6V (Non-reasoning) | 0.2306 | 108B | 12B | medium | ✅ | ❌ |
| 200 | Gemma 4 E2B | 0.2293 | 5.1B | 2.3B | small | ✅ | ✅ |
| 201 | Qwen3 Omni 30B A3B (Reasoning) | 0.2288 | 35.3B | 3B | small | ✅ | ✅ |
| 202 | LFM2.5-2.6B | 0.2272 | 2.7B | — | tiny | ✅ | ✅ |
| 203 | Qwen3 235B | 0.2248 | 235B | 22B | large | ✅ | ✅ |
| 204 | GLM-4.5V | 0.2241 | 108B | 12B | medium | ✅ | ✅ |
| 205 | NVIDIA Nemotron Nano 12B v2 VL | 0.2234 | 13.2B | — | small | ✅ | ✅ |
| 206 | Mistral Large 2 (Nov) | 0.2224 | 123B | — | medium | ✅ | ❌ |
| 207 | Falcon-H1R-7B | 0.2210 | 7B | — | small | ✅ | ✅ |
| 208 | Llama Nemotron Ultra | 0.2201 | 253B | — | large | ✅ | ✅ |
| 209 | Devstral Small 2 | 0.2189 | 24B | — | small | ✅ | ❌ |
| 210 | DeepSeek V3 (Dec) | 0.2125 | 671B | 37B | large | ✅ | ❌ |
| 211 | Nanbeige4.1-3B | 0.2111 | 3.93B | — | tiny | ✅ | ✅ |
| 212 | Olmo 3.1 32B Think | 0.2105 | 32.2B | — | small | ✅ | ✅ |
| 213 | Mistral Small 3.2 | 0.2102 | 24B | — | small | ✅ | ❌ |
| 214 | Sarvam 105B (high) | 0.2096 | 106B | 10.3B | medium | ✅ | ✅ |
| 215 | EXAONE 4.0 32B | 0.2087 | 32B | — | small | ✅ | ✅ |
| 216 | Magistral Small 1.2 | 0.2082 | 24B | — | small | ✅ | ✅ |
| 217 | K2-V2 (low) | 0.2073 | 70B | — | medium | ✅ | ✅ |
| 218 | NVIDIA Nemotron Nano 9B V2 | 0.2067 | 9B | — | small | ✅ | ✅ |
| 219 | Qwen3.5 2B | 0.2067 | 2.27B | — | tiny | ✅ | ✅ |
| 220 | Ring-flash-2.0 | 0.2043 | 103B | 6.1B | medium | ✅ | ✅ |
| 221 | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2026 | 49B | — | medium | ✅ | ❌ |
| 222 | Llama 4 Scout | 0.2018 | 109B | 17B | medium | ✅ | ❌ |
| 223 | Hermes 4 70B | 0.2007 | 70.6B | — | medium | ✅ | ✅ |
| 224 | Devstral Small (May) | 0.1997 | 23.6B | — | small | ✅ | ❌ |
| 225 | Qwen3 32B | 0.1993 | 32.8B | — | small | ✅ | ✅ |
| 226 | Llama 3.3 Nemotron Super 49B | 0.1961 | 49B | — | medium | ✅ | ✅ |
| 227 | DeepSeek R1 Distill Qwen 32B | 0.1957 | 32B | — | small | ✅ | ✅ |
| 228 | Qwen2.5 72B | 0.1951 | 72B | — | medium | ✅ | ❌ |
| 229 | Qwen3 14B | 0.1944 | 14.8B | — | small | ✅ | ✅ |
| 230 | Ling-flash-2.0 | 0.1943 | 103B | 6.1B | medium | ✅ | ❌ |
| 231 | Qwen3 VL 8B | 0.1937 | 8.77B | — | small | ✅ | ❌ |
| 232 | Qwen3 30B | 0.1923 | 30.5B | 3.3B | small | ✅ | ✅ |
| 233 | Magistral Small 1 | 0.1918 | 23.6B | — | small | ✅ | ✅ |
| 234 | Mistral Large 2 (Jul) | 0.1880 | 123B | — | medium | ✅ | ❌ |
| 235 | Ministral 3 14B | 0.1874 | 14B | — | small | ✅ | ❌ |
| 236 | Command A | 0.1872 | 111B | — | medium | ✅ | ❌ |
| 237 | Devstral Small | 0.1866 | 24B | — | small | ✅ | ❌ |
| 238 | Qwen3 235B (Non-reasoning) | 0.1863 | 235B | 22B | large | ✅ | ❌ |
| 239 | Llama 3.1 Nemotron 70B | 0.1850 | 70B | — | medium | ✅ | ❌ |
| 240 | Nemotron 3 Nano 4B | 0.1837 | 3.97B | — | tiny | ✅ | ✅ |
| 241 | Qwen3 VL 4B (Reasoning) | 0.1825 | 4.44B | — | tiny | ✅ | ✅ |
| 242 | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1800 | 49B | — | medium | ✅ | ❌ |
| 243 | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1782 | 30.5B | 3.3B | small | ✅ | ❌ |
| 244 | Qwen3 4B | 0.1768 | 4.02B | — | tiny | ✅ | ✅ |
| 245 | Llama 3.1 70B | 0.1763 | 70B | — | medium | ✅ | ❌ |
| 246 | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1761 | 9B | — | small | ✅ | ❌ |
| 247 | Qwen3 32B (Non-reasoning) | 0.1746 | 32.8B | — | small | ✅ | ❌ |
| 248 | GLM-4.5V (Non-reasoning) | 0.1742 | 108B | 12B | medium | ✅ | ❌ |
| 249 | Gemma 4 E2B (Non-reasoning) | 0.1742 | 5.1B | 2.3B | small | ✅ | ❌ |
| 250 | Qwen3.5 2B (Non-reasoning) | 0.1724 | 2.27B | — | tiny | ✅ | ❌ |
| 251 | Granite 4.1 30B | 0.1719 | 30B | — | small | ✅ | ❌ |
| 252 | Olmo 3.1 32B Instruct | 0.1689 | 32.2B | — | small | ✅ | ❌ |
| 253 | Qwen3 Omni 30B A3B | 0.1672 | 35.3B | 3B | small | ✅ | ❌ |
| 254 | Qwen3 4B 2507 (Non-reasoning) | 0.1655 | 4.02B | — | tiny | ✅ | ❌ |
| 255 | Llama 3.1 8B | 0.1637 | 8B | — | small | ✅ | ❌ |
| 256 | Olmo 3 32B Think | 0.1614 | 32.2B | — | small | ✅ | ✅ |
| 257 | DeepSeek R1 Distill Llama 70B | 0.1606 | 70B | — | medium | ✅ | ✅ |
| 258 | Llama 3.3 70B | 0.1604 | 70B | — | medium | ✅ | ❌ |
| 259 | DeepSeek R1 Distill Qwen 14B | 0.1602 | 14B | — | small | ✅ | ✅ |
| 260 | Kimi Linear 48B A3B Instruct | 0.1599 | 49.1B | 3B | medium | ✅ | ❌ |
| 261 | Ministral 3 8B | 0.1586 | 8B | — | small | ✅ | ❌ |
| 262 | Hermes 4 70B (Non-reasoning) | 0.1554 | 70.6B | — | medium | ✅ | ❌ |
| 263 | Jamba Reasoning 3B | 0.1552 | 3B | — | tiny | ✅ | ✅ |
| 264 | EXAONE 4.0 32B (Non-reasoning) | 0.1530 | 32B | — | small | ✅ | ❌ |
| 265 | Granite 4.1 8B | 0.1530 | 8B | — | small | ✅ | ❌ |
| 266 | LFM2 24B A2B | 0.1498 | 23.8B | 2.3B | small | ✅ | ❌ |
| 267 | Jamba 1.7 Large | 0.1487 | 398B | 94B | large | ✅ | ❌ |
| 268 | Qwen3 8B | 0.1480 | 8.19B | — | small | ✅ | ✅ |
| 269 | Sarvam 30B (high) | 0.1469 | 32.2B | 2.4B | small | ✅ | ✅ |
| 270 | Mistral Small 3 | 0.1455 | 24B | — | small | ✅ | ❌ |
| 271 | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1452 | 13.2B | — | small | ✅ | ❌ |
| 272 | MiniCPM-V 4.6 1.3B | 0.1450 | 1.3B | — | tiny | ✅ | ❌ |
| 273 | Qwen3 30B (Non-reasoning) | 0.1408 | 30.5B | 3.3B | small | ✅ | ❌ |
| 274 | Nemotron 3 Nano (Non-reasoning) | 0.1382 | 31.6B | 3.6B | small | ✅ | ❌ |
| 275 | Granite 4.0 H Small | 0.1351 | 32B | 9B | small | ✅ | ❌ |
| 276 | Qwen3 VL 4B | 0.1347 | 4.44B | — | tiny | ✅ | ❌ |
| 277 | Gemma 3 27B | 0.1328 | 27.4B | — | small | ✅ | ❌ |
| 278 | DeepSeek R1 0528 Qwen3 8B | 0.1308 | 8.19B | — | small | ✅ | ✅ |
| 279 | Ministral 3 3B | 0.1294 | 3B | — | tiny | ✅ | ❌ |
| 280 | Qwen3 14B (Non-reasoning) | 0.1291 | 14.8B | — | small | ✅ | ❌ |
| 281 | Phi-4 | 0.1246 | 14B | — | small | ✅ | ❌ |
| 282 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1238 | 4.51B | — | small | ✅ | ✅ |
| 283 | Gemma 3 270M | 0.1216 | 0.268B | — | tiny | ✅ | ❌ |
| 284 | Llama 3 70B | 0.1167 | 70B | — | medium | ✅ | ❌ |
| 285 | Llama 3.2 11B (Vision) | 0.1162 | 11B | — | small | ✅ | ❌ |
| 286 | Llama 3.2 3B | 0.1143 | 3B | — | tiny | ✅ | ❌ |
| 287 | Qwen3.5 0.8B | 0.1134 | 0.873B | — | tiny | ✅ | ✅ |
| 288 | Olmo 3 7B Think | 0.1129 | 7B | — | small | ✅ | ✅ |
| 289 | LFM2.5-1.2B-Instruct | 0.1064 | 1.17B | — | tiny | ✅ | ❌ |
| 290 | Reka Flash 3 | 0.1059 | 21B | — | small | ✅ | ✅ |
| 291 | Ling-mini-2.0 | 0.1055 | 16.3B | 1.4B | small | ✅ | ❌ |
| 292 | LFM2 2.6B | 0.1055 | 2.57B | — | tiny | ✅ | ❌ |
| 293 | Qwen3 8B (Non-reasoning) | 0.1046 | 8.19B | — | small | ✅ | ❌ |
| 294 | Molmo2-8B | 0.1013 | 8.66B | — | small | ✅ | ❌ |
| 295 | Sarvam M | 0.1011 | 23.6B | — | small | ✅ | ✅ |
| 296 | Jamba 1.7 Mini | 0.0999 | 52B | 12B | medium | ✅ | ❌ |
| 297 | LFM2.5-1.2B-Thinking | 0.0985 | 1.17B | — | tiny | ✅ | ✅ |
| 298 | Phi-4 Mini | 0.0962 | 3.84B | — | tiny | ✅ | ❌ |
| 299 | Gemma 3 12B | 0.0960 | 12.2B | — | small | ✅ | ❌ |
| 300 | Apertus 70B Instruct | 0.0918 | 70B | — | medium | ✅ | ❌ |
| 301 | Qwen3.5 0.8B (Non-reasoning) | 0.0915 | 0.873B | — | tiny | ✅ | ❌ |
| 302 | Olmo 3 7B | 0.0904 | 7B | — | small | ✅ | ❌ |
| 303 | Exaone 4.0 1.2B | 0.0895 | 1.28B | — | tiny | ✅ | ✅ |
| 304 | OLMo 2 32B | 0.0893 | 32.2B | — | small | ✅ | ❌ |
| 305 | Granite 4.0 H 1B | 0.0889 | 1.5B | — | tiny | ✅ | ❌ |
| 306 | Llama 3.2 1B | 0.0878 | 1B | — | tiny | ✅ | ❌ |
| 307 | Qwen3 1.7B | 0.0867 | 2.03B | — | tiny | ✅ | ✅ |
| 308 | Granite 4.1 3B | 0.0851 | 3B | — | tiny | ✅ | ❌ |
| 309 | Exaone 4.0 1.2B (Non-reasoning) | 0.0827 | 1.28B | — | tiny | ✅ | ❌ |
| 310 | LFM2 8B A1B | 0.0809 | 8.34B | 1.5B | small | ✅ | ❌ |
| 311 | Granite 4.0 Micro | 0.0783 | 3B | — | tiny | ✅ | ❌ |
| 312 | Phi-3 Mini | 0.0735 | 3.8B | — | tiny | ✅ | ❌ |
| 313 | Granite 3.3 8B | 0.0702 | 8.17B | — | small | ✅ | ❌ |
| 314 | LFM2.5-VL-1.6B | 0.0676 | 1.6B | — | tiny | ✅ | ❌ |
| 315 | Granite 4.0 1B | 0.0670 | 1.6B | — | tiny | ✅ | ❌ |
| 316 | Granite 4.0 350M | 0.0659 | 0.35B | — | tiny | ✅ | ❌ |
| 317 | Gemma 3 4B | 0.0651 | 4.3B | — | tiny | ✅ | ❌ |
| 318 | LFM2 1.2B | 0.0641 | 1.17B | — | tiny | ✅ | ❌ |
| 319 | Qwen3 0.6B | 0.0635 | 0.752B | — | tiny | ✅ | ✅ |
| 320 | Llama 3 8B | 0.0633 | 8B | — | small | ✅ | ❌ |
| 321 | Mistral 7B | 0.0609 | 7B | — | small | ✅ | ❌ |
| 322 | Gemma 3n E4B | 0.0573 | 8.39B | 4B | small | ✅ | ❌ |
| 323 | K2 Horizon 0.9B | 0.0562 | 0.9B | — | tiny | ✅ | ✅ |
| 324 | Qwen3 1.7B (Non-reasoning) | 0.0555 | 2.03B | — | tiny | ✅ | ❌ |
| 325 | OLMo 2 7B | 0.0553 | 7.3B | — | small | ✅ | ❌ |
| 326 | Gemma 3 1B | 0.0550 | 1B | — | tiny | ✅ | ❌ |
| 327 | Apertus 8B Instruct | 0.0540 | 8B | — | small | ✅ | ❌ |
| 328 | Granite 4.0 H 350M | 0.0499 | 0.34B | — | tiny | ✅ | ❌ |
| 329 | Molmo 7B-D | 0.0468 | 8.02B | — | small | ✅ | ❌ |
| 330 | Qwen3 0.6B (Non-reasoning) | 0.0429 | 0.752B | — | tiny | ✅ | ❌ |
| 331 | Gemma 3n E2B | 0.0354 | 5.98B | 2B | small | ✅ | ❌ |
| 332 | Tiny Aya Global | 0.0350 | 3.35B | — | tiny | ✅ | ❌ |
| 333 | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 1.5B | — | tiny | ✅ | ✅ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 7 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且总参数量 ≤，且至少一项严格更优；缺少参数量数据的模型不在图表和表格中）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.1216，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 1.83，r = B/C = 0.546358），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002434，maxdev = 0.1174。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 40，10B–100B: 103，100B–1T: 129，1T–2.8T: 8
- 中位数位置 0.502；左 132 个，右 151 个
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
**模型数（有参数量数据）**: 333（总体帕累托前沿 11 个；图表入图 283 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.1216，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 50 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
