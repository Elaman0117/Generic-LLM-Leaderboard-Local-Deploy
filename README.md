# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.1248，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 285 个入图，50 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3 (max) | 0.8737 | 2.8T | 104B | large | ✅ | ✅ |
| 2 | GLM-5.3 (max) | 0.8551 | 753B | 40B | large | ✅ | ✅ |
| 3 | MiMo-V2.6-Pro | 0.8500 | 1T | 42B | large | ✅ | ✅ |
| 4 | Step 5 Preview | 0.8321 | 600B | — | large | ❌ | ✅ |
| 5 | GLM-5.3-Flash | 0.8146 | 320B | 18B | large | ✅ | ✅ |
| 6 | Qwen3.8 2.4T A95B | 0.8119 | 2.4T | 95B | large | ✅ | ✅ |
| 7 | GLM-5.2 (max) | 0.7927 | 753B | 40B | large | ✅ | ✅ |
| 8 | Qwen3.8-Flash-Next | 0.7548 | 180B | 6B | large | ✅ | ✅ |
| 9 | DeepSeek V4 Pro 0813 (max) | 0.7251 | 1.6T | 49B | large | ✅ | ✅ |
| 10 | DeepSeek V4.1 Flash (max) | 0.7196 | 552B | 16B | large | ✅ | ✅ |
| 11 | Kimi K2.6 | 0.7085 | 1T | 32B | large | ✅ | ✅ |
| 12 | Qwen3.8 27B (xhigh) | 0.7036 | 27B | — | small | ✅ | ✅ |
| 13 | DeepSeek V4 Flash Vision (max) | 0.6890 | 284B | — | large | ❌ | ✅ |
| 14 | DeepSeek V4 Flash 0731 (max) | 0.6859 | 284B | 13B | large | ✅ | ✅ |
| 15 | Motif 3 | 0.6776 | 314B | 13.2B | large | ✅ | ✅ |
| 16 | Kimi K3 (low) | 0.6772 | 2.8T | 104B | large | ✅ | ✅ |
| 17 | MiniMax-M3 | 0.6733 | 428B | 23B | large | ✅ | ✅ |
| 18 | MiMo-V2.6-Flash | 0.6716 | 309B | 15B | large | ✅ | ✅ |
| 19 | DeepSeek V4 Pro (max) | 0.6625 | 1.6T | 49B | large | ✅ | ✅ |
| 20 | GLM-5.1 | 0.6567 | 744B | 40B | large | ✅ | ✅ |
| 21 | DeepSeek V4 Pro (high) | 0.6499 | 1.6T | 49B | large | ✅ | ✅ |
| 22 | GLM-5 | 0.6469 | 744B | 40B | large | ✅ | ✅ |
| 23 | K2 Horizon 375B A23B | 0.6406 | 375B | 23B | large | ✅ | ✅ |
| 24 | Kimi K2.7 Code | 0.6353 | 1T | 32B | large | ✅ | ✅ |
| 25 | Ling-3.0-flash-VL | 0.6173 | 124B | 5.5B | medium | ✅ | ✅ |
| 26 | Inkling Small | 0.6135 | 266B | 12B | large | ✅ | ✅ |
| 27 | MiMo-V2.5-Pro | 0.6131 | 1T | 42B | large | ✅ | ✅ |
| 28 | MiMo-V2.5 | 0.6098 | 310B | 15B | large | ✅ | ✅ |
| 29 | DeepSeek V4 Flash (max) | 0.6091 | 284B | 13B | large | ✅ | ✅ |
| 30 | GLM-5.3 (low) | 0.6090 | 753B | 40B | large | ✅ | ✅ |
| 31 | Inkling | 0.6069 | 975B | 41B | large | ✅ | ✅ |
| 32 | DeepSeek V4 Flash (high) | 0.6064 | 284B | 13B | large | ✅ | ✅ |
| 33 | Solar Open2 250B | 0.5936 | 250B | 15B | large | ✅ | ✅ |
| 34 | Qwen3.5 27B | 0.5920 | 27.8B | — | small | ✅ | ✅ |
| 35 | MiMo-V2-Flash (Feb 2026) | 0.5917 | 309B | 15B | large | ✅ | ✅ |
| 36 | Quasar 438B (max) | 0.5898 | 438B | — | large | ❌ | ✅ |
| 37 | Nex-N2-Pro | 0.5887 | 397B | 17B | large | ✅ | ✅ |
| 38 | Motif 3 (Beta) | 0.5864 | 314B | — | large | ❌ | ✅ |
| 39 | Qwen3.6 27B | 0.5851 | 27.8B | — | small | ✅ | ✅ |
| 40 | Kimi K2.5 | 0.5831 | 1T | 32B | large | ✅ | ✅ |
| 41 | Nemotron 3 Ultra | 0.5790 | 550B | 55B | large | ✅ | ✅ |
| 42 | Kimi K2 Thinking | 0.5749 | 1T | 32B | large | ✅ | ✅ |
| 43 | Qwen3.8 27B (medium) | 0.5693 | 27B | — | small | ✅ | ✅ |
| 44 | Qwen3.5 397B A17B | 0.5690 | 397B | 17B | large | ✅ | ✅ |
| 45 | Kimi K2.6 (Non-reasoning) | 0.5677 | 1T | 32B | large | ✅ | ❌ |
| 46 | A.X-K2 | 0.5600 | 692B | 33B | large | ✅ | ✅ |
| 47 | MiniMax-M2.7 | 0.5589 | 230B | 10B | large | ✅ | ✅ |
| 48 | Hy3 | 0.5584 | 299B | 21B | large | ✅ | ✅ |
| 49 | K2 Horizon MoVA 36B A4B | 0.5554 | 36B | 4B | small | ✅ | ✅ |
| 50 | Hy3-preview | 0.5542 | 295B | 21B | large | ✅ | ✅ |
| 51 | Qwen3.8 27B (low) | 0.5539 | 27B | — | small | ✅ | ✅ |
| 52 | MiniMax-M2.5 | 0.5488 | 230B | 10B | large | ✅ | ✅ |
| 53 | GLM-5.1 (Non-reasoning) | 0.5477 | 744B | 40B | large | ✅ | ❌ |
| 54 | Qwen3.6 35B A3B | 0.5436 | 36B | 3B | small | ✅ | ✅ |
| 55 | JT-4.1 Flash 236B A21B | 0.5424 | 236B | — | large | ❌ | ❌ |
| 56 | Ling 3.0 Flash | 0.5372 | 124B | 5.1B | medium | ✅ | ✅ |
| 57 | MiniMax-M2.1 | 0.5336 | 230B | 10B | large | ✅ | ✅ |
| 58 | Qwen3.5 122B A10B | 0.5316 | 125B | 10B | medium | ✅ | ✅ |
| 59 | Qwen3.5 35B A3B | 0.5283 | 36B | 3B | small | ✅ | ✅ |
| 60 | Step 3.7 Flash | 0.5278 | 198B | 11B | large | ✅ | ✅ |
| 61 | G9v3-39A5B | 0.5252 | 39B | 5B | small | ✅ | ✅ |
| 62 | Kimi K2.5 (Non-reasoning) | 0.5229 | 1T | 32B | large | ✅ | ❌ |
| 63 | MiMo-V2-Flash | 0.5216 | 309B | 15B | large | ✅ | ✅ |
| 64 | GLM-4.7 | 0.5154 | 357B | 32B | large | ✅ | ✅ |
| 65 | DeepSeek V3.2 | 0.5131 | 685B | 37B | large | ✅ | ✅ |
| 66 | Gemma 4 31B | 0.5121 | 30.7B | — | small | ✅ | ✅ |
| 67 | GLM-5 (Non-reasoning) | 0.5117 | 744B | 40B | large | ✅ | ❌ |
| 68 | Qwen3.8 27B | 0.5111 | 27B | — | small | ✅ | ❌ |
| 69 | Ling-3.0-flash-Fin | 0.5059 | 124B | 5.1B | medium | ✅ | ✅ |
| 70 | Qwen3.5 397B A17B (Non-reasoning) | 0.5049 | 397B | 17B | large | ✅ | ❌ |
| 71 | Muse Glimmer (high) | 0.4983 | 30B | — | small | ✅ | ✅ |
| 72 | Qwen3.5 27B (Non-reasoning) | 0.4901 | 27.8B | — | small | ✅ | ❌ |
| 73 | DeepSeek V3.2 Speciale | 0.4888 | 685B | 37B | large | ✅ | ✅ |
| 74 | JT-35B-Flash | 0.4879 | 35B | — | small | ❌ | ❌ |
| 75 | Step 3.5 Flash | 0.4870 | 196B | 11B | large | ✅ | ✅ |
| 76 | K-EXAONE 2.0 | 0.4851 | 750B | 37B | large | ✅ | ✅ |
| 77 | Command A+ | 0.4798 | 218B | 25B | large | ✅ | ✅ |
| 78 | Ring-2.6-1T | 0.4773 | 1T | 63B | large | ✅ | ✅ |
| 79 | DeepSeek V4.1 Flash (Non-reasoning) | 0.4750 | 552B | 16B | large | ✅ | ❌ |
| 80 | MiniMax-M2 | 0.4744 | 230B | 10B | large | ✅ | ✅ |
| 81 | Mistral Medium 3.5 | 0.4698 | 128B | — | medium | ✅ | ✅ |
| 82 | K2 Horizon 7B | 0.4668 | 7B | — | small | ✅ | ✅ |
| 83 | DeepSeek V4 Pro (Non-reasoning) | 0.4595 | 1.6T | 49B | large | ✅ | ❌ |
| 84 | GLM-5.2 (Non-reasoning) | 0.4473 | 753B | 40B | large | ✅ | ❌ |
| 85 | LongCat 2.0 | 0.4464 | 1.6T | 48B | large | ✅ | ✅ |
| 86 | Qwen3.6 27B (Non-reasoning) | 0.4459 | 27.8B | — | small | ✅ | ❌ |
| 87 | DeepSeek V3.2 Exp | 0.4425 | 685B | 37B | large | ✅ | ✅ |
| 88 | DeepSeek V3.1 Terminus | 0.4381 | 685B | 37B | large | ✅ | ✅ |
| 89 | Qwen3.5 122B A10B (Non-reasoning) | 0.4278 | 125B | 10B | medium | ✅ | ❌ |
| 90 | MiMo-V2.5-Pro (Non-reasoning) | 0.4209 | 1T | 42B | large | ✅ | ❌ |
| 91 | Qwen3.5 9B | 0.4195 | 9.65B | — | small | ✅ | ✅ |
| 92 | Kimi K2 0905 | 0.4180 | 1T | 32B | large | ✅ | ❌ |
| 93 | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | 284B | 13B | large | ✅ | ❌ |
| 94 | Qwen3 VL 235B A22B (Reasoning) | 0.4166 | 235B | 22B | large | ✅ | ✅ |
| 95 | Gemma 4 26B A4B | 0.4155 | 25.2B | 3.8B | small | ✅ | ✅ |
| 96 | Ling-2.6-1T | 0.4138 | 1T | 63B | large | ✅ | ❌ |
| 97 | DeepSeek V3.2 (Non-reasoning) | 0.4081 | 685B | 37B | large | ✅ | ❌ |
| 98 | EXAONE 4.5 33B | 0.4070 | 34.4B | — | small | ✅ | ✅ |
| 99 | Qwen3.5 4B | 0.4063 | 4.66B | — | small | ✅ | ✅ |
| 100 | Hy3-preview (Non-reasoning) | 0.4062 | 295B | 21B | large | ✅ | ❌ |
| 101 | Ling 3.0 Tiny | 0.4033 | 7.9B | 1.3B | small | ✅ | ✅ |
| 102 | GLM-4.7 (Non-reasoning) | 0.4032 | 357B | 32B | large | ✅ | ❌ |
| 103 | Qwen3.6 35B A3B (Non-reasoning) | 0.3956 | 36B | 3B | small | ✅ | ❌ |
| 104 | Gemma 4 12B | 0.3955 | 12B | — | small | ✅ | ✅ |
| 105 | DeepSeek V3.1 | 0.3946 | 685B | 37B | large | ✅ | ✅ |
| 106 | GLM-4.5 | 0.3940 | 355B | 32B | large | ✅ | ✅ |
| 107 | MiniCPM5-2B | 0.3874 | 2.6B | — | tiny | ✅ | ✅ |
| 108 | Kimi K2 | 0.3844 | 1T | 32B | large | ✅ | ❌ |
| 109 | DeepSeek R1 0528 | 0.3830 | 685B | 37B | large | ✅ | ✅ |
| 110 | K-EXAONE | 0.3822 | 236B | 23B | large | ✅ | ✅ |
| 111 | GLM-4.6 | 0.3820 | 357B | 32B | large | ✅ | ✅ |
| 112 | Gemma 4 31B (Non-reasoning) | 0.3789 | 30.7B | — | small | ✅ | ❌ |
| 113 | Qwen3 VL 32B (Reasoning) | 0.3736 | 33.4B | — | small | ✅ | ✅ |
| 114 | K2 Horizon 3.7B | 0.3735 | 3.7B | — | tiny | ✅ | ✅ |
| 115 | Nemotron 3 Super | 0.3732 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 116 | Trinity Large Thinking | 0.3719 | 399B | 13B | large | ✅ | ✅ |
| 117 | Granite 4.2 30B | 0.3716 | 30B | — | small | ✅ | ✅ |
| 118 | Qwen3.5 9B (Non-reasoning) | 0.3696 | 9.65B | — | small | ✅ | ❌ |
| 119 | GLM-4.7-Flash | 0.3695 | 31.2B | 3B | small | ✅ | ✅ |
| 120 | GLM-4.6 (Non-reasoning) | 0.3660 | 357B | 32B | large | ✅ | ❌ |
| 121 | Qwen3.5 35B A3B (Non-reasoning) | 0.3658 | 36B | 3B | small | ✅ | ❌ |
| 122 | Nemotron 3.5 Lightning | 0.3647 | 31.6B | 3.6B | small | ✅ | ✅ |
| 123 | Apriel-v1.5-15B-Thinker | 0.3622 | 15B | — | small | ✅ | ✅ |
| 124 | Qwen3 235B A22B 2507 | 0.3603 | 235B | 22B | large | ✅ | ✅ |
| 125 | Qwen3 Coder 480B | 0.3572 | 480B | 35B | large | ✅ | ❌ |
| 126 | Nemotron Cascade 2 30B A3B | 0.3561 | 31.6B | 3B | small | ✅ | ✅ |
| 127 | Cogito v2.1 | 0.3559 | 671B | 37B | large | ✅ | ✅ |
| 128 | Apriel-v1.6-15B-Thinker | 0.3519 | 15B | — | small | ✅ | ✅ |
| 129 | Gemma 4 26B A4B (Non-reasoning) | 0.3508 | 25.2B | 3.8B | small | ✅ | ❌ |
| 130 | G9v3-3B | 0.3506 | 3B | — | tiny | ✅ | ✅ |
| 131 | GLM-4.6V | 0.3495 | 108B | 12B | medium | ✅ | ✅ |
| 132 | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3488 | 685B | 37B | large | ✅ | ❌ |
| 133 | gpt-oss-120b (high) | 0.3479 | 117B | 5.1B | medium | ✅ | ✅ |
| 134 | MiMo-V2-Flash (Non-reasoning) | 0.3400 | 309B | 15B | large | ✅ | ❌ |
| 135 | Mistral Small 4 | 0.3346 | 119B | 6.5B | medium | ✅ | ✅ |
| 136 | DeepSeek V3.2 Exp (Non-reasoning) | 0.3312 | 685B | 37B | large | ✅ | ❌ |
| 137 | HyperNova 60B 2605 (high) | 0.3294 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 138 | DeepSeek V3.1 (Non-reasoning) | 0.3280 | 685B | 37B | large | ✅ | ❌ |
| 139 | North Mini Code | 0.3252 | 30B | 3B | small | ✅ | ✅ |
| 140 | Seed-OSS-36B-Instruct | 0.3242 | 36.2B | — | small | ✅ | ✅ |
| 141 | Granite 4.2 8B | 0.3183 | 8B | — | small | ✅ | ✅ |
| 142 | Solar Pro 3 | 0.3174 | 102B | — | medium | ❌ | ✅ |
| 143 | Qwen3 235B 2507 | 0.3167 | 235B | 22B | large | ✅ | ❌ |
| 144 | K2 Think V2 | 0.3160 | 70B | — | medium | ✅ | ✅ |
| 145 | Qwen3 Next 80B A3B (Reasoning) | 0.3096 | 80B | 3B | medium | ✅ | ✅ |
| 146 | Gemma 4 12B (Non-reasoning) | 0.3083 | 12B | — | small | ✅ | ❌ |
| 147 | Qwen3 VL 235B A22B | 0.3077 | 235B | — | large | ✅ | ❌ |
| 148 | Nemotron 3 Nano | 0.3076 | 31.6B | 3.6B | small | ✅ | ✅ |
| 149 | QwQ-32B | 0.3059 | 32.8B | — | small | ✅ | ✅ |
| 150 | Ring-1T | 0.3048 | 1T | 50B | large | ✅ | ✅ |
| 151 | MiniCPM5-1B | 0.3048 | 1B | — | tiny | ✅ | ✅ |
| 152 | MiniCPM5-1B (Non-reasoning) | 0.3046 | 1B | — | tiny | ✅ | ❌ |
| 153 | Pixtral Large | 0.3034 | 124B | — | medium | ✅ | ❌ |
| 154 | Solar Open 100B | 0.3001 | 102B | 12B | medium | ✅ | ✅ |
| 155 | Qwen3.5 4B (Non-reasoning) | 0.2979 | 4.66B | — | small | ✅ | ❌ |
| 156 | Qwen3 Coder Next | 0.2973 | 79.7B | 3B | medium | ✅ | ❌ |
| 157 | GLM-4.5-Air | 0.2966 | 106B | 12B | medium | ✅ | ✅ |
| 158 | MiniMax M1 80k | 0.2964 | 456B | 45.9B | large | ✅ | ✅ |
| 159 | Gemma 4 E4B | 0.2956 | 8B | 4.5B | small | ✅ | ✅ |
| 160 | DiffusionGemma 26B A4B | 0.2910 | 25.2B | 3.8B | small | ✅ | ✅ |
| 161 | MiniMax M1 40k | 0.2895 | 456B | 45.9B | large | ✅ | ✅ |
| 162 | HyperCLOVA X SEED Think (32B) | 0.2894 | 32B | — | small | ✅ | ✅ |
| 163 | K2-V2 (high) | 0.2872 | 70B | — | medium | ✅ | ✅ |
| 164 | K-EXAONE (Non-reasoning) | 0.2869 | 236B | 23B | large | ✅ | ❌ |
| 165 | DeepSeek V3 0324 | 0.2857 | 671B | 37B | large | ✅ | ❌ |
| 166 | DeepSeek R1 (Jan) | 0.2832 | 685B | 37B | large | ✅ | ✅ |
| 167 | Mistral Large 3 | 0.2826 | 675B | 41B | large | ✅ | ❌ |
| 168 | Llama 4 Maverick | 0.2812 | 402B | 17B | large | ✅ | ❌ |
| 169 | gpt-oss-20b (high) | 0.2781 | 21B | 3.6B | small | ✅ | ✅ |
| 170 | INTELLECT-3 | 0.2774 | 107B | 12B | medium | ✅ | ✅ |
| 171 | Nemotron 3 Nano Omni 30B A3B | 0.2769 | 30B | 3B | small | ✅ | ✅ |
| 172 | Tri-21B-think Preview | 0.2766 | 21B | — | small | ✅ | ✅ |
| 173 | LongCat Flash Lite | 0.2749 | 68.5B | 3B | medium | ✅ | ❌ |
| 174 | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 30B | 3B | small | ✅ | ✅ |
| 175 | Qwen3 30B A3B 2507 | 0.2746 | 30.5B | 3.3B | small | ✅ | ✅ |
| 176 | gpt-oss-20b (low) | 0.2742 | 21B | 3.6B | small | ✅ | ✅ |
| 177 | Llama 3.1 405B | 0.2731 | 405B | — | large | ✅ | ❌ |
| 178 | Ling 2.6 Flash | 0.2716 | 107B | 7.4B | medium | ✅ | ❌ |
| 179 | Gemma 4 E4B (Non-reasoning) | 0.2711 | 8B | 4.5B | small | ✅ | ❌ |
| 180 | Tri-21B-Think | 0.2709 | 21B | — | small | ✅ | ✅ |
| 181 | Granite 4.2 3B | 0.2659 | 3B | — | tiny | ✅ | ✅ |
| 182 | Qwen3 Next 80B A3B | 0.2630 | 80B | 3B | medium | ✅ | ❌ |
| 183 | Qwen3 VL 32B | 0.2627 | 33.4B | — | small | ✅ | ❌ |
| 184 | Hermes 4 405B | 0.2610 | 406B | — | large | ✅ | ✅ |
| 185 | K2-V2 (medium) | 0.2585 | 70B | — | medium | ✅ | ✅ |
| 186 | Ling-1T | 0.2577 | 1T | 50B | large | ✅ | ❌ |
| 187 | Motif-2-12.7B | 0.2571 | 12.7B | — | small | ❌ | ✅ |
| 188 | gpt-oss-120b (low) | 0.2568 | 117B | 5.1B | medium | ✅ | ✅ |
| 189 | Qwen3 VL 8B (Reasoning) | 0.2540 | 8.77B | — | small | ✅ | ✅ |
| 190 | Step3 VL 10B | 0.2523 | 10.2B | — | small | ✅ | ✅ |
| 191 | Llama Nemotron Super 49B v1.5 | 0.2501 | 49B | — | medium | ✅ | ✅ |
| 192 | GLM-4.7-Flash (Non-reasoning) | 0.2497 | 31.2B | 3B | small | ✅ | ❌ |
| 193 | Devstral 2 | 0.2479 | 125B | — | medium | ✅ | ❌ |
| 194 | ERNIE 4.5 300B A47B | 0.2470 | 300B | 47B | large | ✅ | ❌ |
| 195 | Qwen3 4B 2507 | 0.2439 | 4.02B | — | tiny | ✅ | ✅ |
| 196 | Mistral Small 4 (Non-reasoning) | 0.2428 | 119B | 6.5B | medium | ✅ | ❌ |
| 197 | Hermes 4 405B (Non-reasoning) | 0.2417 | 406B | — | large | ✅ | ❌ |
| 198 | Qwen3 Coder 30B A3B | 0.2404 | 30.5B | 3.3B | small | ✅ | ❌ |
| 199 | LFM2.5-8B-A1B | 0.2381 | 8.3B | 1.5B | small | ✅ | ✅ |
| 200 | Qwen3 VL 30B A3B | 0.2372 | 30B | 3B | small | ✅ | ❌ |
| 201 | GLM-4.6V (Non-reasoning) | 0.2367 | 108B | 12B | medium | ✅ | ❌ |
| 202 | Gemma 4 E2B | 0.2353 | 5.1B | 2.3B | small | ✅ | ✅ |
| 203 | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 35.3B | 3B | small | ✅ | ✅ |
| 204 | LFM2.5-2.6B | 0.2331 | 2.7B | — | tiny | ✅ | ✅ |
| 205 | Qwen3 235B | 0.2307 | 235B | 22B | large | ✅ | ✅ |
| 206 | GLM-4.5V | 0.2300 | 108B | 12B | medium | ✅ | ✅ |
| 207 | NVIDIA Nemotron Nano 12B v2 VL | 0.2293 | 13.2B | — | small | ✅ | ✅ |
| 208 | Mistral Large 2 (Nov) | 0.2283 | 123B | — | medium | ✅ | ❌ |
| 209 | Falcon-H1R-7B | 0.2268 | 7B | — | small | ✅ | ✅ |
| 210 | Llama Nemotron Ultra | 0.2258 | 253B | — | large | ✅ | ✅ |
| 211 | Devstral Small 2 | 0.2246 | 24B | — | small | ✅ | ❌ |
| 212 | DeepSeek V3 (Dec) | 0.2181 | 671B | 37B | large | ✅ | ❌ |
| 213 | Nanbeige4.1-3B | 0.2166 | 3.93B | — | tiny | ✅ | ✅ |
| 214 | Olmo 3.1 32B Think | 0.2160 | 32.2B | — | small | ✅ | ✅ |
| 215 | Mistral Small 3.2 | 0.2157 | 24B | — | small | ✅ | ❌ |
| 216 | Sarvam 105B (high) | 0.2151 | 106B | 10.3B | medium | ✅ | ✅ |
| 217 | EXAONE 4.0 32B | 0.2142 | 32B | — | small | ✅ | ✅ |
| 218 | Magistral Small 1.2 | 0.2137 | 24B | — | small | ✅ | ✅ |
| 219 | K2-V2 (low) | 0.2127 | 70B | — | medium | ✅ | ✅ |
| 220 | NVIDIA Nemotron Nano 9B V2 | 0.2122 | 9B | — | small | ✅ | ✅ |
| 221 | Qwen3.5 2B | 0.2122 | 2.27B | — | tiny | ✅ | ✅ |
| 222 | Ring-flash-2.0 | 0.2096 | 103B | 6.1B | medium | ✅ | ✅ |
| 223 | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2080 | 49B | — | medium | ✅ | ❌ |
| 224 | Llama 4 Scout | 0.2071 | 109B | 17B | medium | ✅ | ❌ |
| 225 | Hermes 4 70B | 0.2059 | 70.6B | — | medium | ✅ | ✅ |
| 226 | Devstral Small (May) | 0.2049 | 23.6B | — | small | ✅ | ❌ |
| 227 | Qwen3 32B | 0.2045 | 32.8B | — | small | ✅ | ✅ |
| 228 | Llama 3.3 Nemotron Super 49B | 0.2012 | 49B | — | medium | ✅ | ✅ |
| 229 | DeepSeek R1 Distill Qwen 32B | 0.2009 | 32B | — | small | ✅ | ✅ |
| 230 | Qwen2.5 72B | 0.2002 | 72B | — | medium | ✅ | ❌ |
| 231 | Qwen3 14B | 0.1995 | 14.8B | — | small | ✅ | ✅ |
| 232 | Ling-flash-2.0 | 0.1994 | 103B | 6.1B | medium | ✅ | ❌ |
| 233 | Qwen3 VL 8B | 0.1988 | 8.77B | — | small | ✅ | ❌ |
| 234 | Qwen3 30B | 0.1973 | 30.5B | 3.3B | small | ✅ | ✅ |
| 235 | Magistral Small 1 | 0.1969 | 23.6B | — | small | ✅ | ✅ |
| 236 | Mistral Large 2 (Jul) | 0.1929 | 123B | — | medium | ✅ | ❌ |
| 237 | Ministral 3 14B | 0.1924 | 14B | — | small | ✅ | ❌ |
| 238 | Command A | 0.1921 | 111B | — | medium | ✅ | ❌ |
| 239 | Devstral Small | 0.1914 | 24B | — | small | ✅ | ❌ |
| 240 | Qwen3 235B (Non-reasoning) | 0.1912 | 235B | 22B | large | ✅ | ❌ |
| 241 | Llama 3.1 Nemotron 70B | 0.1899 | 70B | — | medium | ✅ | ❌ |
| 242 | Nemotron 3 Nano 4B | 0.1885 | 3.97B | — | tiny | ✅ | ✅ |
| 243 | Qwen3 VL 4B (Reasoning) | 0.1873 | 4.44B | — | tiny | ✅ | ✅ |
| 244 | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1847 | 49B | — | medium | ✅ | ❌ |
| 245 | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1829 | 30.5B | 3.3B | small | ✅ | ❌ |
| 246 | Qwen3 4B | 0.1815 | 4.02B | — | tiny | ✅ | ✅ |
| 247 | Llama 3.1 70B | 0.1809 | 70B | — | medium | ✅ | ❌ |
| 248 | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1807 | 9B | — | small | ✅ | ❌ |
| 249 | Qwen3 32B (Non-reasoning) | 0.1792 | 32.8B | — | small | ✅ | ❌ |
| 250 | GLM-4.5V (Non-reasoning) | 0.1788 | 108B | 12B | medium | ✅ | ❌ |
| 251 | Gemma 4 E2B (Non-reasoning) | 0.1787 | 5.1B | 2.3B | small | ✅ | ❌ |
| 252 | Qwen3.5 2B (Non-reasoning) | 0.1770 | 2.27B | — | tiny | ✅ | ❌ |
| 253 | Granite 4.1 30B | 0.1765 | 30B | — | small | ✅ | ❌ |
| 254 | Olmo 3.1 32B Instruct | 0.1733 | 32.2B | — | small | ✅ | ❌ |
| 255 | Qwen3 Omni 30B A3B | 0.1716 | 35.3B | 3B | small | ✅ | ❌ |
| 256 | Qwen3 4B 2507 (Non-reasoning) | 0.1698 | 4.02B | — | tiny | ✅ | ❌ |
| 257 | Llama 3.1 8B | 0.1680 | 8B | — | small | ✅ | ❌ |
| 258 | Olmo 3 32B Think | 0.1656 | 32.2B | — | small | ✅ | ✅ |
| 259 | DeepSeek R1 Distill Llama 70B | 0.1648 | 70B | — | medium | ✅ | ✅ |
| 260 | Llama 3.3 70B | 0.1646 | 70B | — | medium | ✅ | ❌ |
| 261 | DeepSeek R1 Distill Qwen 14B | 0.1644 | 14B | — | small | ✅ | ✅ |
| 262 | Kimi Linear 48B A3B Instruct | 0.1641 | 49.1B | 3B | medium | ✅ | ❌ |
| 263 | Ministral 3 8B | 0.1627 | 8B | — | small | ✅ | ❌ |
| 264 | Hermes 4 70B (Non-reasoning) | 0.1595 | 70.6B | — | medium | ✅ | ❌ |
| 265 | Jamba Reasoning 3B | 0.1592 | 3B | — | tiny | ✅ | ✅ |
| 266 | EXAONE 4.0 32B (Non-reasoning) | 0.1570 | 32B | — | small | ✅ | ❌ |
| 267 | Granite 4.1 8B | 0.1570 | 8B | — | small | ✅ | ❌ |
| 268 | LFM2 24B A2B | 0.1537 | 23.8B | 2.3B | small | ✅ | ❌ |
| 269 | Jamba 1.7 Large | 0.1526 | 398B | 94B | large | ✅ | ❌ |
| 270 | Qwen3 8B | 0.1519 | 8.19B | — | small | ✅ | ✅ |
| 271 | Sarvam 30B (high) | 0.1507 | 32.2B | 2.4B | small | ✅ | ✅ |
| 272 | Mistral Small 3 | 0.1493 | 24B | — | small | ✅ | ❌ |
| 273 | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 13.2B | — | small | ✅ | ❌ |
| 274 | MiniCPM-V 4.6 1.3B | 0.1488 | 1.3B | — | tiny | ✅ | ❌ |
| 275 | Qwen3 30B (Non-reasoning) | 0.1445 | 30.5B | 3.3B | small | ✅ | ❌ |
| 276 | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 31.6B | 3.6B | small | ✅ | ❌ |
| 277 | Granite 4.0 H Small | 0.1387 | 32B | 9B | small | ✅ | ❌ |
| 278 | Qwen3 VL 4B | 0.1383 | 4.44B | — | tiny | ✅ | ❌ |
| 279 | Gemma 3 27B | 0.1363 | 27.4B | — | small | ✅ | ❌ |
| 280 | DeepSeek R1 0528 Qwen3 8B | 0.1342 | 8.19B | — | small | ✅ | ✅ |
| 281 | Ministral 3 3B | 0.1328 | 3B | — | tiny | ✅ | ❌ |
| 282 | Qwen3 14B (Non-reasoning) | 0.1325 | 14.8B | — | small | ✅ | ❌ |
| 283 | Phi-4 | 0.1278 | 14B | — | small | ✅ | ❌ |
| 284 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | 4.51B | — | small | ✅ | ✅ |
| 285 | Gemma 3 270M | 0.1248 | 0.268B | — | tiny | ✅ | ❌ |
| 286 | Llama 3 70B | 0.1197 | 70B | — | medium | ✅ | ❌ |
| 287 | Llama 3.2 11B (Vision) | 0.1192 | 11B | — | small | ✅ | ❌ |
| 288 | Llama 3.2 3B | 0.1173 | 3B | — | tiny | ✅ | ❌ |
| 289 | Qwen3.5 0.8B | 0.1164 | 0.873B | — | tiny | ✅ | ✅ |
| 290 | Olmo 3 7B Think | 0.1158 | 7B | — | small | ✅ | ✅ |
| 291 | LFM2.5-1.2B-Instruct | 0.1092 | 1.17B | — | tiny | ✅ | ❌ |
| 292 | Reka Flash 3 | 0.1087 | 21B | — | small | ✅ | ✅ |
| 293 | Ling-mini-2.0 | 0.1083 | 16.3B | 1.4B | small | ✅ | ❌ |
| 294 | LFM2 2.6B | 0.1082 | 2.57B | — | tiny | ✅ | ❌ |
| 295 | Qwen3 8B (Non-reasoning) | 0.1073 | 8.19B | — | small | ✅ | ❌ |
| 296 | Molmo2-8B | 0.1040 | 8.66B | — | small | ✅ | ❌ |
| 297 | Sarvam M | 0.1037 | 23.6B | — | small | ✅ | ✅ |
| 298 | Jamba 1.7 Mini | 0.1025 | 52B | 12B | medium | ✅ | ❌ |
| 299 | LFM2.5-1.2B-Thinking | 0.1011 | 1.17B | — | tiny | ✅ | ✅ |
| 300 | Phi-4 Mini | 0.0987 | 3.84B | — | tiny | ✅ | ❌ |
| 301 | Gemma 3 12B | 0.0985 | 12.2B | — | small | ✅ | ❌ |
| 302 | Apertus 70B Instruct | 0.0942 | 70B | — | medium | ✅ | ❌ |
| 303 | Qwen3.5 0.8B (Non-reasoning) | 0.0939 | 0.873B | — | tiny | ✅ | ❌ |
| 304 | Olmo 3 7B | 0.0928 | 7B | — | small | ✅ | ❌ |
| 305 | Exaone 4.0 1.2B | 0.0918 | 1.28B | — | tiny | ✅ | ✅ |
| 306 | OLMo 2 32B | 0.0917 | 32.2B | — | small | ✅ | ❌ |
| 307 | Granite 4.0 H 1B | 0.0912 | 1.5B | — | tiny | ✅ | ❌ |
| 308 | Llama 3.2 1B | 0.0901 | 1B | — | tiny | ✅ | ❌ |
| 309 | Qwen3 1.7B | 0.0890 | 2.03B | — | tiny | ✅ | ✅ |
| 310 | Granite 4.1 3B | 0.0873 | 3B | — | tiny | ✅ | ❌ |
| 311 | Exaone 4.0 1.2B (Non-reasoning) | 0.0848 | 1.28B | — | tiny | ✅ | ❌ |
| 312 | LFM2 8B A1B | 0.0830 | 8.34B | 1.5B | small | ✅ | ❌ |
| 313 | Granite 4.0 Micro | 0.0804 | 3B | — | tiny | ✅ | ❌ |
| 314 | Phi-3 Mini | 0.0754 | 3.8B | — | tiny | ✅ | ❌ |
| 315 | Granite 3.3 8B | 0.0720 | 8.17B | — | small | ✅ | ❌ |
| 316 | LFM2.5-VL-1.6B | 0.0694 | 1.6B | — | tiny | ✅ | ❌ |
| 317 | Granite 4.0 1B | 0.0687 | 1.6B | — | tiny | ✅ | ❌ |
| 318 | Granite 4.0 350M | 0.0677 | 0.35B | — | tiny | ✅ | ❌ |
| 319 | Gemma 3 4B | 0.0668 | 4.3B | — | tiny | ✅ | ❌ |
| 320 | LFM2 1.2B | 0.0658 | 1.17B | — | tiny | ✅ | ❌ |
| 321 | Qwen3 0.6B | 0.0652 | 0.752B | — | tiny | ✅ | ✅ |
| 322 | Llama 3 8B | 0.0649 | 8B | — | small | ✅ | ❌ |
| 323 | Mistral 7B | 0.0625 | 7B | — | small | ✅ | ❌ |
| 324 | Gemma 3n E4B | 0.0588 | 8.39B | 4B | small | ✅ | ❌ |
| 325 | K2 Horizon 0.9B | 0.0577 | 0.9B | — | tiny | ✅ | ✅ |
| 326 | Qwen3 1.7B (Non-reasoning) | 0.0570 | 2.03B | — | tiny | ✅ | ❌ |
| 327 | OLMo 2 7B | 0.0568 | 7.3B | — | small | ✅ | ❌ |
| 328 | Gemma 3 1B | 0.0564 | 1B | — | tiny | ✅ | ❌ |
| 329 | Apertus 8B Instruct | 0.0555 | 8B | — | small | ✅ | ❌ |
| 330 | Granite 4.0 H 350M | 0.0512 | 0.34B | — | tiny | ✅ | ❌ |
| 331 | Molmo 7B-D | 0.0480 | 8.02B | — | small | ✅ | ❌ |
| 332 | Qwen3 0.6B (Non-reasoning) | 0.0440 | 0.752B | — | tiny | ✅ | ❌ |
| 333 | Gemma 3n E2B | 0.0363 | 5.98B | 2B | small | ✅ | ❌ |
| 334 | Tiny Aya Global | 0.0359 | 3.35B | — | tiny | ✅ | ❌ |
| 335 | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 1.5B | — | tiny | ✅ | ✅ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 7 |
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
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.1248，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 1.63，r = B/C = 0.613273），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002688，maxdev = 0.1250。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 40，10B–100B: 103，100B–1T: 131，1T–2.8T: 8
- 中位数位置 0.511；左 131 个，右 154 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.064，10^1→ 0.264，10^2→ 0.555，10^3→ 0.862

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
**模型数（有参数量数据）**: 335（总体帕累托前沿 11 个；图表入图 285 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.1248，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 50 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
