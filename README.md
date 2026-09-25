# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.1248，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 284 个入图，50 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3 (max) | 0.8737 | 2.8T | 104B | large | ✅ | ✅ |
| 2 | GLM-5.3 (max) | 0.8552 | 753B | 40B | large | ✅ | ✅ |
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
| 18 | DeepSeek V4 Pro (max) | 0.6625 | 1.6T | 49B | large | ✅ | ✅ |
| 19 | GLM-5.1 | 0.6567 | 744B | 40B | large | ✅ | ✅ |
| 20 | DeepSeek V4 Pro (high) | 0.6499 | 1.6T | 49B | large | ✅ | ✅ |
| 21 | GLM-5 | 0.6469 | 744B | 40B | large | ✅ | ✅ |
| 22 | K2 Horizon 375B A23B | 0.6406 | 375B | 23B | large | ✅ | ✅ |
| 23 | Kimi K2.7 Code | 0.6353 | 1T | 32B | large | ✅ | ✅ |
| 24 | Ling-3.0-flash-VL | 0.6173 | 124B | 5.5B | medium | ✅ | ✅ |
| 25 | Inkling Small | 0.6135 | 266B | 12B | large | ✅ | ✅ |
| 26 | MiMo-V2.5-Pro | 0.6131 | 1T | 42B | large | ✅ | ✅ |
| 27 | MiMo-V2.5 | 0.6098 | 310B | 15B | large | ✅ | ✅ |
| 28 | DeepSeek V4 Flash (max) | 0.6091 | 284B | 13B | large | ✅ | ✅ |
| 29 | GLM-5.3 (low) | 0.6090 | 753B | 40B | large | ✅ | ✅ |
| 30 | Inkling | 0.6069 | 975B | 41B | large | ✅ | ✅ |
| 31 | DeepSeek V4 Flash (high) | 0.6064 | 284B | 13B | large | ✅ | ✅ |
| 32 | Solar Open2 250B | 0.5936 | 250B | 15B | large | ✅ | ✅ |
| 33 | Qwen3.5 27B | 0.5920 | 27.8B | — | small | ✅ | ✅ |
| 34 | MiMo-V2-Flash (Feb 2026) | 0.5917 | 309B | 15B | large | ✅ | ✅ |
| 35 | Quasar 438B (max) | 0.5898 | 438B | — | large | ❌ | ✅ |
| 36 | Nex-N2-Pro | 0.5887 | 397B | 17B | large | ✅ | ✅ |
| 37 | Motif 3 (Beta) | 0.5864 | 314B | — | large | ❌ | ✅ |
| 38 | Qwen3.6 27B | 0.5851 | 27.8B | — | small | ✅ | ✅ |
| 39 | Kimi K2.5 | 0.5831 | 1T | 32B | large | ✅ | ✅ |
| 40 | Nemotron 3 Ultra | 0.5790 | 550B | 55B | large | ✅ | ✅ |
| 41 | Kimi K2 Thinking | 0.5749 | 1T | 32B | large | ✅ | ✅ |
| 42 | Qwen3.8 27B (medium) | 0.5693 | 27B | — | small | ✅ | ✅ |
| 43 | Qwen3.5 397B A17B | 0.5690 | 397B | 17B | large | ✅ | ✅ |
| 44 | Kimi K2.6 (Non-reasoning) | 0.5677 | 1T | 32B | large | ✅ | ❌ |
| 45 | A.X-K2 | 0.5600 | 692B | 33B | large | ✅ | ✅ |
| 46 | MiniMax-M2.7 | 0.5589 | 230B | 10B | large | ✅ | ✅ |
| 47 | Hy3 | 0.5584 | 299B | 21B | large | ✅ | ✅ |
| 48 | K2 Horizon MoVA 36B A4B | 0.5554 | 36B | 4B | small | ✅ | ✅ |
| 49 | Hy3-preview | 0.5542 | 295B | 21B | large | ✅ | ✅ |
| 50 | Qwen3.8 27B (low) | 0.5539 | 27B | — | small | ✅ | ✅ |
| 51 | MiniMax-M2.5 | 0.5488 | 230B | 10B | large | ✅ | ✅ |
| 52 | GLM-5.1 (Non-reasoning) | 0.5477 | 744B | 40B | large | ✅ | ❌ |
| 53 | Qwen3.6 35B A3B | 0.5436 | 36B | 3B | small | ✅ | ✅ |
| 54 | JT-4.1 Flash 236B A21B | 0.5424 | 236B | — | large | ❌ | ❌ |
| 55 | Ling 3.0 Flash | 0.5372 | 124B | 5.1B | medium | ✅ | ✅ |
| 56 | MiniMax-M2.1 | 0.5336 | 230B | 10B | large | ✅ | ✅ |
| 57 | Qwen3.5 122B A10B | 0.5316 | 125B | 10B | medium | ✅ | ✅ |
| 58 | Qwen3.5 35B A3B | 0.5283 | 36B | 3B | small | ✅ | ✅ |
| 59 | Step 3.7 Flash | 0.5278 | 198B | 11B | large | ✅ | ✅ |
| 60 | G9v3-39A5B | 0.5252 | 39B | 5B | small | ✅ | ✅ |
| 61 | Kimi K2.5 (Non-reasoning) | 0.5229 | 1T | 32B | large | ✅ | ❌ |
| 62 | MiMo-V2-Flash | 0.5216 | 309B | 15B | large | ✅ | ✅ |
| 63 | GLM-4.7 | 0.5154 | 357B | 32B | large | ✅ | ✅ |
| 64 | DeepSeek V3.2 | 0.5131 | 685B | 37B | large | ✅ | ✅ |
| 65 | Gemma 4 31B | 0.5121 | 30.7B | — | small | ✅ | ✅ |
| 66 | GLM-5 (Non-reasoning) | 0.5117 | 744B | 40B | large | ✅ | ❌ |
| 67 | Qwen3.8 27B | 0.5111 | 27B | — | small | ✅ | ❌ |
| 68 | Ling-3.0-flash-Fin | 0.5059 | 124B | 5.1B | medium | ✅ | ✅ |
| 69 | Qwen3.5 397B A17B (Non-reasoning) | 0.5049 | 397B | 17B | large | ✅ | ❌ |
| 70 | Muse Glimmer (high) | 0.4983 | 30B | — | small | ✅ | ✅ |
| 71 | Qwen3.5 27B (Non-reasoning) | 0.4901 | 27.8B | — | small | ✅ | ❌ |
| 72 | DeepSeek V3.2 Speciale | 0.4888 | 685B | 37B | large | ✅ | ✅ |
| 73 | JT-35B-Flash | 0.4879 | 35B | — | small | ❌ | ❌ |
| 74 | Step 3.5 Flash | 0.4870 | 196B | 11B | large | ✅ | ✅ |
| 75 | K-EXAONE 2.0 | 0.4851 | 750B | 37B | large | ✅ | ✅ |
| 76 | Command A+ | 0.4798 | 218B | 25B | large | ✅ | ✅ |
| 77 | Ring-2.6-1T | 0.4773 | 1T | 63B | large | ✅ | ✅ |
| 78 | DeepSeek V4.1 Flash (Non-reasoning) | 0.4750 | 552B | 16B | large | ✅ | ❌ |
| 79 | MiniMax-M2 | 0.4744 | 230B | 10B | large | ✅ | ✅ |
| 80 | Mistral Medium 3.5 | 0.4698 | 128B | — | medium | ✅ | ✅ |
| 81 | K2 Horizon 7B | 0.4668 | 7B | — | small | ✅ | ✅ |
| 82 | DeepSeek V4 Pro (Non-reasoning) | 0.4595 | 1.6T | 49B | large | ✅ | ❌ |
| 83 | GLM-5.2 (Non-reasoning) | 0.4473 | 753B | 40B | large | ✅ | ❌ |
| 84 | LongCat 2.0 | 0.4464 | 1.6T | 48B | large | ✅ | ✅ |
| 85 | Qwen3.6 27B (Non-reasoning) | 0.4459 | 27.8B | — | small | ✅ | ❌ |
| 86 | DeepSeek V3.2 Exp | 0.4425 | 685B | 37B | large | ✅ | ✅ |
| 87 | DeepSeek V3.1 Terminus | 0.4381 | 685B | 37B | large | ✅ | ✅ |
| 88 | Qwen3.5 122B A10B (Non-reasoning) | 0.4278 | 125B | 10B | medium | ✅ | ❌ |
| 89 | Qwen3.5 9B | 0.4246 | 9.65B | — | small | ✅ | ✅ |
| 90 | MiMo-V2.5-Pro (Non-reasoning) | 0.4209 | 1T | 42B | large | ✅ | ❌ |
| 91 | Kimi K2 0905 | 0.4180 | 1T | 32B | large | ✅ | ❌ |
| 92 | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | 284B | 13B | large | ✅ | ❌ |
| 93 | Qwen3 VL 235B A22B (Reasoning) | 0.4166 | 235B | 22B | large | ✅ | ✅ |
| 94 | Gemma 4 26B A4B | 0.4155 | 25.2B | 3.8B | small | ✅ | ✅ |
| 95 | Ling-2.6-1T | 0.4138 | 1T | 63B | large | ✅ | ❌ |
| 96 | DeepSeek V3.2 (Non-reasoning) | 0.4081 | 685B | 37B | large | ✅ | ❌ |
| 97 | EXAONE 4.5 33B | 0.4070 | 34.4B | — | small | ✅ | ✅ |
| 98 | Qwen3.5 4B | 0.4063 | 4.66B | — | small | ✅ | ✅ |
| 99 | Hy3-preview (Non-reasoning) | 0.4062 | 295B | 21B | large | ✅ | ❌ |
| 100 | Ling 3.0 Tiny | 0.4033 | 7.9B | 1.3B | small | ✅ | ✅ |
| 101 | GLM-4.7 (Non-reasoning) | 0.4032 | 357B | 32B | large | ✅ | ❌ |
| 102 | Qwen3.6 35B A3B (Non-reasoning) | 0.3956 | 36B | 3B | small | ✅ | ❌ |
| 103 | Gemma 4 12B | 0.3955 | 12B | — | small | ✅ | ✅ |
| 104 | DeepSeek V3.1 | 0.3946 | 685B | 37B | large | ✅ | ✅ |
| 105 | GLM-4.5 | 0.3940 | 355B | 32B | large | ✅ | ✅ |
| 106 | MiniCPM5-2B | 0.3874 | 2.6B | — | tiny | ✅ | ✅ |
| 107 | Kimi K2 | 0.3844 | 1T | 32B | large | ✅ | ❌ |
| 108 | DeepSeek R1 0528 | 0.3830 | 685B | 37B | large | ✅ | ✅ |
| 109 | K-EXAONE | 0.3822 | 236B | 23B | large | ✅ | ✅ |
| 110 | GLM-4.6 | 0.3820 | 357B | 32B | large | ✅ | ✅ |
| 111 | Gemma 4 31B (Non-reasoning) | 0.3789 | 30.7B | — | small | ✅ | ❌ |
| 112 | Qwen3 VL 32B (Reasoning) | 0.3736 | 33.4B | — | small | ✅ | ✅ |
| 113 | K2 Horizon 3.7B | 0.3735 | 3.7B | — | tiny | ✅ | ✅ |
| 114 | Nemotron 3 Super | 0.3732 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 115 | Trinity Large Thinking | 0.3719 | 399B | 13B | large | ✅ | ✅ |
| 116 | Granite 4.2 30B | 0.3716 | 30B | — | small | ✅ | ✅ |
| 117 | Qwen3.5 9B (Non-reasoning) | 0.3696 | 9.65B | — | small | ✅ | ❌ |
| 118 | GLM-4.7-Flash | 0.3695 | 31.2B | 3B | small | ✅ | ✅ |
| 119 | GLM-4.6 (Non-reasoning) | 0.3660 | 357B | 32B | large | ✅ | ❌ |
| 120 | Qwen3.5 35B A3B (Non-reasoning) | 0.3658 | 36B | 3B | small | ✅ | ❌ |
| 121 | Nemotron 3.5 Lightning | 0.3647 | 31.6B | 3.6B | small | ✅ | ✅ |
| 122 | Apriel-v1.5-15B-Thinker | 0.3622 | 15B | — | small | ✅ | ✅ |
| 123 | Qwen3 235B A22B 2507 | 0.3603 | 235B | 22B | large | ✅ | ✅ |
| 124 | Qwen3 Coder 480B | 0.3572 | 480B | 35B | large | ✅ | ❌ |
| 125 | Nemotron Cascade 2 30B A3B | 0.3561 | 31.6B | 3B | small | ✅ | ✅ |
| 126 | Cogito v2.1 | 0.3559 | 671B | 37B | large | ✅ | ✅ |
| 127 | Apriel-v1.6-15B-Thinker | 0.3519 | 15B | — | small | ✅ | ✅ |
| 128 | Gemma 4 26B A4B (Non-reasoning) | 0.3508 | 25.2B | 3.8B | small | ✅ | ❌ |
| 129 | G9v3-3B | 0.3506 | 3B | — | tiny | ✅ | ✅ |
| 130 | GLM-4.6V | 0.3495 | 108B | 12B | medium | ✅ | ✅ |
| 131 | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3488 | 685B | 37B | large | ✅ | ❌ |
| 132 | gpt-oss-120b (high) | 0.3479 | 117B | 5.1B | medium | ✅ | ✅ |
| 133 | MiMo-V2-Flash (Non-reasoning) | 0.3400 | 309B | 15B | large | ✅ | ❌ |
| 134 | Mistral Small 4 | 0.3346 | 119B | 6.5B | medium | ✅ | ✅ |
| 135 | DeepSeek V3.2 Exp (Non-reasoning) | 0.3312 | 685B | 37B | large | ✅ | ❌ |
| 136 | HyperNova 60B 2605 (high) | 0.3294 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 137 | DeepSeek V3.1 (Non-reasoning) | 0.3280 | 685B | 37B | large | ✅ | ❌ |
| 138 | North Mini Code | 0.3252 | 30B | 3B | small | ✅ | ✅ |
| 139 | Seed-OSS-36B-Instruct | 0.3242 | 36.2B | — | small | ✅ | ✅ |
| 140 | Granite 4.2 8B | 0.3183 | 8B | — | small | ✅ | ✅ |
| 141 | Solar Pro 3 | 0.3174 | 102B | — | medium | ❌ | ✅ |
| 142 | Qwen3 235B 2507 | 0.3167 | 235B | 22B | large | ✅ | ❌ |
| 143 | K2 Think V2 | 0.3160 | 70B | — | medium | ✅ | ✅ |
| 144 | Qwen3 Next 80B A3B (Reasoning) | 0.3096 | 80B | 3B | medium | ✅ | ✅ |
| 145 | Gemma 4 12B (Non-reasoning) | 0.3083 | 12B | — | small | ✅ | ❌ |
| 146 | Qwen3 VL 235B A22B | 0.3077 | 235B | — | large | ✅ | ❌ |
| 147 | Nemotron 3 Nano | 0.3076 | 31.6B | 3.6B | small | ✅ | ✅ |
| 148 | QwQ-32B | 0.3059 | 32.8B | — | small | ✅ | ✅ |
| 149 | Ring-1T | 0.3048 | 1T | 50B | large | ✅ | ✅ |
| 150 | MiniCPM5-1B | 0.3048 | 1B | — | tiny | ✅ | ✅ |
| 151 | MiniCPM5-1B (Non-reasoning) | 0.3046 | 1B | — | tiny | ✅ | ❌ |
| 152 | Pixtral Large | 0.3034 | 124B | — | medium | ✅ | ❌ |
| 153 | Solar Open 100B | 0.3001 | 102B | 12B | medium | ✅ | ✅ |
| 154 | Qwen3.5 4B (Non-reasoning) | 0.2979 | 4.66B | — | small | ✅ | ❌ |
| 155 | Qwen3 Coder Next | 0.2973 | 79.7B | 3B | medium | ✅ | ❌ |
| 156 | GLM-4.5-Air | 0.2966 | 106B | 12B | medium | ✅ | ✅ |
| 157 | MiniMax M1 80k | 0.2964 | 456B | 45.9B | large | ✅ | ✅ |
| 158 | Gemma 4 E4B | 0.2956 | 8B | 4.5B | small | ✅ | ✅ |
| 159 | DiffusionGemma 26B A4B | 0.2910 | 25.2B | 3.8B | small | ✅ | ✅ |
| 160 | MiniMax M1 40k | 0.2895 | 456B | 45.9B | large | ✅ | ✅ |
| 161 | HyperCLOVA X SEED Think (32B) | 0.2894 | 32B | — | small | ✅ | ✅ |
| 162 | K2-V2 (high) | 0.2872 | 70B | — | medium | ✅ | ✅ |
| 163 | K-EXAONE (Non-reasoning) | 0.2869 | 236B | 23B | large | ✅ | ❌ |
| 164 | DeepSeek V3 0324 | 0.2857 | 671B | 37B | large | ✅ | ❌ |
| 165 | DeepSeek R1 (Jan) | 0.2832 | 685B | 37B | large | ✅ | ✅ |
| 166 | Mistral Large 3 | 0.2826 | 675B | 41B | large | ✅ | ❌ |
| 167 | Llama 4 Maverick | 0.2812 | 402B | 17B | large | ✅ | ❌ |
| 168 | gpt-oss-20b (high) | 0.2781 | 21B | 3.6B | small | ✅ | ✅ |
| 169 | INTELLECT-3 | 0.2774 | 107B | 12B | medium | ✅ | ✅ |
| 170 | Nemotron 3 Nano Omni 30B A3B | 0.2769 | 30B | 3B | small | ✅ | ✅ |
| 171 | Tri-21B-think Preview | 0.2766 | 21B | — | small | ✅ | ✅ |
| 172 | LongCat Flash Lite | 0.2749 | 68.5B | 3B | medium | ✅ | ❌ |
| 173 | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 30B | 3B | small | ✅ | ✅ |
| 174 | Qwen3 30B A3B 2507 | 0.2746 | 30.5B | 3.3B | small | ✅ | ✅ |
| 175 | gpt-oss-20b (low) | 0.2742 | 21B | 3.6B | small | ✅ | ✅ |
| 176 | Llama 3.1 405B | 0.2731 | 405B | — | large | ✅ | ❌ |
| 177 | Ling 2.6 Flash | 0.2716 | 107B | 7.4B | medium | ✅ | ❌ |
| 178 | Gemma 4 E4B (Non-reasoning) | 0.2711 | 8B | 4.5B | small | ✅ | ❌ |
| 179 | Tri-21B-Think | 0.2709 | 21B | — | small | ✅ | ✅ |
| 180 | Granite 4.2 3B | 0.2659 | 3B | — | tiny | ✅ | ✅ |
| 181 | Qwen3 Next 80B A3B | 0.2630 | 80B | 3B | medium | ✅ | ❌ |
| 182 | Qwen3 VL 32B | 0.2627 | 33.4B | — | small | ✅ | ❌ |
| 183 | Hermes 4 405B | 0.2610 | 406B | — | large | ✅ | ✅ |
| 184 | K2-V2 (medium) | 0.2585 | 70B | — | medium | ✅ | ✅ |
| 185 | Ling-1T | 0.2577 | 1T | 50B | large | ✅ | ❌ |
| 186 | Motif-2-12.7B | 0.2571 | 12.7B | — | small | ❌ | ✅ |
| 187 | gpt-oss-120b (low) | 0.2568 | 117B | 5.1B | medium | ✅ | ✅ |
| 188 | Qwen3 VL 8B (Reasoning) | 0.2540 | 8.77B | — | small | ✅ | ✅ |
| 189 | Step3 VL 10B | 0.2523 | 10.2B | — | small | ✅ | ✅ |
| 190 | Llama Nemotron Super 49B v1.5 | 0.2501 | 49B | — | medium | ✅ | ✅ |
| 191 | GLM-4.7-Flash (Non-reasoning) | 0.2497 | 31.2B | 3B | small | ✅ | ❌ |
| 192 | Devstral 2 | 0.2479 | 125B | — | medium | ✅ | ❌ |
| 193 | ERNIE 4.5 300B A47B | 0.2470 | 300B | 47B | large | ✅ | ❌ |
| 194 | Qwen3 4B 2507 | 0.2439 | 4.02B | — | tiny | ✅ | ✅ |
| 195 | Mistral Small 4 (Non-reasoning) | 0.2428 | 119B | 6.5B | medium | ✅ | ❌ |
| 196 | Hermes 4 405B (Non-reasoning) | 0.2417 | 406B | — | large | ✅ | ❌ |
| 197 | Qwen3 Coder 30B A3B | 0.2404 | 30.5B | 3.3B | small | ✅ | ❌ |
| 198 | LFM2.5-8B-A1B | 0.2381 | 8.3B | 1.5B | small | ✅ | ✅ |
| 199 | Qwen3 VL 30B A3B | 0.2372 | 30B | 3B | small | ✅ | ❌ |
| 200 | GLM-4.6V (Non-reasoning) | 0.2367 | 108B | 12B | medium | ✅ | ❌ |
| 201 | Gemma 4 E2B | 0.2353 | 5.1B | 2.3B | small | ✅ | ✅ |
| 202 | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 35.3B | 3B | small | ✅ | ✅ |
| 203 | LFM2.5-2.6B | 0.2331 | 2.7B | — | tiny | ✅ | ✅ |
| 204 | Qwen3 235B | 0.2307 | 235B | 22B | large | ✅ | ✅ |
| 205 | GLM-4.5V | 0.2300 | 108B | 12B | medium | ✅ | ✅ |
| 206 | NVIDIA Nemotron Nano 12B v2 VL | 0.2293 | 13.2B | — | small | ✅ | ✅ |
| 207 | Mistral Large 2 (Nov) | 0.2283 | 123B | — | medium | ✅ | ❌ |
| 208 | Falcon-H1R-7B | 0.2268 | 7B | — | small | ✅ | ✅ |
| 209 | Llama Nemotron Ultra | 0.2258 | 253B | — | large | ✅ | ✅ |
| 210 | Devstral Small 2 | 0.2246 | 24B | — | small | ✅ | ❌ |
| 211 | DeepSeek V3 (Dec) | 0.2181 | 671B | 37B | large | ✅ | ❌ |
| 212 | Nanbeige4.1-3B | 0.2166 | 3.93B | — | tiny | ✅ | ✅ |
| 213 | Olmo 3.1 32B Think | 0.2160 | 32.2B | — | small | ✅ | ✅ |
| 214 | Mistral Small 3.2 | 0.2157 | 24B | — | small | ✅ | ❌ |
| 215 | Sarvam 105B (high) | 0.2151 | 106B | 10.3B | medium | ✅ | ✅ |
| 216 | EXAONE 4.0 32B | 0.2142 | 32B | — | small | ✅ | ✅ |
| 217 | Magistral Small 1.2 | 0.2137 | 24B | — | small | ✅ | ✅ |
| 218 | K2-V2 (low) | 0.2127 | 70B | — | medium | ✅ | ✅ |
| 219 | NVIDIA Nemotron Nano 9B V2 | 0.2122 | 9B | — | small | ✅ | ✅ |
| 220 | Qwen3.5 2B | 0.2122 | 2.27B | — | tiny | ✅ | ✅ |
| 221 | Ring-flash-2.0 | 0.2096 | 103B | 6.1B | medium | ✅ | ✅ |
| 222 | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2080 | 49B | — | medium | ✅ | ❌ |
| 223 | Llama 4 Scout | 0.2071 | 109B | 17B | medium | ✅ | ❌ |
| 224 | Hermes 4 70B | 0.2059 | 70.6B | — | medium | ✅ | ✅ |
| 225 | Devstral Small (May) | 0.2049 | 23.6B | — | small | ✅ | ❌ |
| 226 | Qwen3 32B | 0.2045 | 32.8B | — | small | ✅ | ✅ |
| 227 | Llama 3.3 Nemotron Super 49B | 0.2012 | 49B | — | medium | ✅ | ✅ |
| 228 | DeepSeek R1 Distill Qwen 32B | 0.2009 | 32B | — | small | ✅ | ✅ |
| 229 | Qwen2.5 72B | 0.2002 | 72B | — | medium | ✅ | ❌ |
| 230 | Qwen3 14B | 0.1995 | 14.8B | — | small | ✅ | ✅ |
| 231 | Ling-flash-2.0 | 0.1994 | 103B | 6.1B | medium | ✅ | ❌ |
| 232 | Qwen3 VL 8B | 0.1988 | 8.77B | — | small | ✅ | ❌ |
| 233 | Qwen3 30B | 0.1973 | 30.5B | 3.3B | small | ✅ | ✅ |
| 234 | Magistral Small 1 | 0.1969 | 23.6B | — | small | ✅ | ✅ |
| 235 | Mistral Large 2 (Jul) | 0.1929 | 123B | — | medium | ✅ | ❌ |
| 236 | Ministral 3 14B | 0.1924 | 14B | — | small | ✅ | ❌ |
| 237 | Command A | 0.1921 | 111B | — | medium | ✅ | ❌ |
| 238 | Devstral Small | 0.1914 | 24B | — | small | ✅ | ❌ |
| 239 | Qwen3 235B (Non-reasoning) | 0.1912 | 235B | 22B | large | ✅ | ❌ |
| 240 | Llama 3.1 Nemotron 70B | 0.1899 | 70B | — | medium | ✅ | ❌ |
| 241 | Nemotron 3 Nano 4B | 0.1885 | 3.97B | — | tiny | ✅ | ✅ |
| 242 | Qwen3 VL 4B (Reasoning) | 0.1873 | 4.44B | — | tiny | ✅ | ✅ |
| 243 | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1847 | 49B | — | medium | ✅ | ❌ |
| 244 | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1829 | 30.5B | 3.3B | small | ✅ | ❌ |
| 245 | Qwen3 4B | 0.1815 | 4.02B | — | tiny | ✅ | ✅ |
| 246 | Llama 3.1 70B | 0.1809 | 70B | — | medium | ✅ | ❌ |
| 247 | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1807 | 9B | — | small | ✅ | ❌ |
| 248 | Qwen3 32B (Non-reasoning) | 0.1792 | 32.8B | — | small | ✅ | ❌ |
| 249 | GLM-4.5V (Non-reasoning) | 0.1788 | 108B | 12B | medium | ✅ | ❌ |
| 250 | Gemma 4 E2B (Non-reasoning) | 0.1787 | 5.1B | 2.3B | small | ✅ | ❌ |
| 251 | Qwen3.5 2B (Non-reasoning) | 0.1770 | 2.27B | — | tiny | ✅ | ❌ |
| 252 | Granite 4.1 30B | 0.1765 | 30B | — | small | ✅ | ❌ |
| 253 | Olmo 3.1 32B Instruct | 0.1733 | 32.2B | — | small | ✅ | ❌ |
| 254 | Qwen3 Omni 30B A3B | 0.1716 | 35.3B | 3B | small | ✅ | ❌ |
| 255 | Qwen3 4B 2507 (Non-reasoning) | 0.1698 | 4.02B | — | tiny | ✅ | ❌ |
| 256 | Llama 3.1 8B | 0.1680 | 8B | — | small | ✅ | ❌ |
| 257 | Olmo 3 32B Think | 0.1656 | 32.2B | — | small | ✅ | ✅ |
| 258 | DeepSeek R1 Distill Llama 70B | 0.1648 | 70B | — | medium | ✅ | ✅ |
| 259 | Llama 3.3 70B | 0.1646 | 70B | — | medium | ✅ | ❌ |
| 260 | DeepSeek R1 Distill Qwen 14B | 0.1644 | 14B | — | small | ✅ | ✅ |
| 261 | Kimi Linear 48B A3B Instruct | 0.1641 | 49.1B | 3B | medium | ✅ | ❌ |
| 262 | Ministral 3 8B | 0.1627 | 8B | — | small | ✅ | ❌ |
| 263 | Hermes 4 70B (Non-reasoning) | 0.1595 | 70.6B | — | medium | ✅ | ❌ |
| 264 | Jamba Reasoning 3B | 0.1592 | 3B | — | tiny | ✅ | ✅ |
| 265 | EXAONE 4.0 32B (Non-reasoning) | 0.1570 | 32B | — | small | ✅ | ❌ |
| 266 | Granite 4.1 8B | 0.1570 | 8B | — | small | ✅ | ❌ |
| 267 | LFM2 24B A2B | 0.1537 | 23.8B | 2.3B | small | ✅ | ❌ |
| 268 | Jamba 1.7 Large | 0.1526 | 398B | 94B | large | ✅ | ❌ |
| 269 | Qwen3 8B | 0.1519 | 8.19B | — | small | ✅ | ✅ |
| 270 | Sarvam 30B (high) | 0.1507 | 32.2B | 2.4B | small | ✅ | ✅ |
| 271 | Mistral Small 3 | 0.1493 | 24B | — | small | ✅ | ❌ |
| 272 | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 13.2B | — | small | ✅ | ❌ |
| 273 | MiniCPM-V 4.6 1.3B | 0.1488 | 1.3B | — | tiny | ✅ | ❌ |
| 274 | Qwen3 30B (Non-reasoning) | 0.1445 | 30.5B | 3.3B | small | ✅ | ❌ |
| 275 | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 31.6B | 3.6B | small | ✅ | ❌ |
| 276 | Granite 4.0 H Small | 0.1387 | 32B | 9B | small | ✅ | ❌ |
| 277 | Qwen3 VL 4B | 0.1383 | 4.44B | — | tiny | ✅ | ❌ |
| 278 | Gemma 3 27B | 0.1363 | 27.4B | — | small | ✅ | ❌ |
| 279 | DeepSeek R1 0528 Qwen3 8B | 0.1342 | 8.19B | — | small | ✅ | ✅ |
| 280 | Ministral 3 3B | 0.1328 | 3B | — | tiny | ✅ | ❌ |
| 281 | Qwen3 14B (Non-reasoning) | 0.1325 | 14.8B | — | small | ✅ | ❌ |
| 282 | Phi-4 | 0.1278 | 14B | — | small | ✅ | ❌ |
| 283 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | 4.51B | — | small | ✅ | ✅ |
| 284 | Gemma 3 270M | 0.1248 | 0.268B | — | tiny | ✅ | ❌ |
| 285 | Llama 3 70B | 0.1197 | 70B | — | medium | ✅ | ❌ |
| 286 | Llama 3.2 11B (Vision) | 0.1192 | 11B | — | small | ✅ | ❌ |
| 287 | Llama 3.2 3B | 0.1173 | 3B | — | tiny | ✅ | ❌ |
| 288 | Qwen3.5 0.8B | 0.1164 | 0.873B | — | tiny | ✅ | ✅ |
| 289 | Olmo 3 7B Think | 0.1158 | 7B | — | small | ✅ | ✅ |
| 290 | LFM2.5-1.2B-Instruct | 0.1092 | 1.17B | — | tiny | ✅ | ❌ |
| 291 | Reka Flash 3 | 0.1087 | 21B | — | small | ✅ | ✅ |
| 292 | Ling-mini-2.0 | 0.1083 | 16.3B | 1.4B | small | ✅ | ❌ |
| 293 | LFM2 2.6B | 0.1082 | 2.57B | — | tiny | ✅ | ❌ |
| 294 | Qwen3 8B (Non-reasoning) | 0.1073 | 8.19B | — | small | ✅ | ❌ |
| 295 | Molmo2-8B | 0.1040 | 8.66B | — | small | ✅ | ❌ |
| 296 | Sarvam M | 0.1037 | 23.6B | — | small | ✅ | ✅ |
| 297 | Jamba 1.7 Mini | 0.1025 | 52B | 12B | medium | ✅ | ❌ |
| 298 | LFM2.5-1.2B-Thinking | 0.1011 | 1.17B | — | tiny | ✅ | ✅ |
| 299 | Phi-4 Mini | 0.0987 | 3.84B | — | tiny | ✅ | ❌ |
| 300 | Gemma 3 12B | 0.0985 | 12.2B | — | small | ✅ | ❌ |
| 301 | Apertus 70B Instruct | 0.0942 | 70B | — | medium | ✅ | ❌ |
| 302 | Qwen3.5 0.8B (Non-reasoning) | 0.0939 | 0.873B | — | tiny | ✅ | ❌ |
| 303 | Olmo 3 7B | 0.0928 | 7B | — | small | ✅ | ❌ |
| 304 | Exaone 4.0 1.2B | 0.0918 | 1.28B | — | tiny | ✅ | ✅ |
| 305 | OLMo 2 32B | 0.0917 | 32.2B | — | small | ✅ | ❌ |
| 306 | Granite 4.0 H 1B | 0.0912 | 1.5B | — | tiny | ✅ | ❌ |
| 307 | Llama 3.2 1B | 0.0901 | 1B | — | tiny | ✅ | ❌ |
| 308 | Qwen3 1.7B | 0.0890 | 2.03B | — | tiny | ✅ | ✅ |
| 309 | Granite 4.1 3B | 0.0873 | 3B | — | tiny | ✅ | ❌ |
| 310 | Exaone 4.0 1.2B (Non-reasoning) | 0.0848 | 1.28B | — | tiny | ✅ | ❌ |
| 311 | LFM2 8B A1B | 0.0830 | 8.34B | 1.5B | small | ✅ | ❌ |
| 312 | Granite 4.0 Micro | 0.0804 | 3B | — | tiny | ✅ | ❌ |
| 313 | Phi-3 Mini | 0.0754 | 3.8B | — | tiny | ✅ | ❌ |
| 314 | Granite 3.3 8B | 0.0720 | 8.17B | — | small | ✅ | ❌ |
| 315 | LFM2.5-VL-1.6B | 0.0694 | 1.6B | — | tiny | ✅ | ❌ |
| 316 | Granite 4.0 1B | 0.0687 | 1.6B | — | tiny | ✅ | ❌ |
| 317 | Granite 4.0 350M | 0.0677 | 0.35B | — | tiny | ✅ | ❌ |
| 318 | Gemma 3 4B | 0.0668 | 4.3B | — | tiny | ✅ | ❌ |
| 319 | LFM2 1.2B | 0.0658 | 1.17B | — | tiny | ✅ | ❌ |
| 320 | Qwen3 0.6B | 0.0652 | 0.752B | — | tiny | ✅ | ✅ |
| 321 | Llama 3 8B | 0.0649 | 8B | — | small | ✅ | ❌ |
| 322 | Mistral 7B | 0.0625 | 7B | — | small | ✅ | ❌ |
| 323 | Gemma 3n E4B | 0.0588 | 8.39B | 4B | small | ✅ | ❌ |
| 324 | K2 Horizon 0.9B | 0.0577 | 0.9B | — | tiny | ✅ | ✅ |
| 325 | Qwen3 1.7B (Non-reasoning) | 0.0570 | 2.03B | — | tiny | ✅ | ❌ |
| 326 | OLMo 2 7B | 0.0568 | 7.3B | — | small | ✅ | ❌ |
| 327 | Gemma 3 1B | 0.0564 | 1B | — | tiny | ✅ | ❌ |
| 328 | Apertus 8B Instruct | 0.0555 | 8B | — | small | ✅ | ❌ |
| 329 | Granite 4.0 H 350M | 0.0512 | 0.34B | — | tiny | ✅ | ❌ |
| 330 | Molmo 7B-D | 0.0480 | 8.02B | — | small | ✅ | ❌ |
| 331 | Qwen3 0.6B (Non-reasoning) | 0.0440 | 0.752B | — | tiny | ✅ | ❌ |
| 332 | Gemma 3n E2B | 0.0363 | 5.98B | 2B | small | ✅ | ❌ |
| 333 | Tiny Aya Global | 0.0359 | 3.35B | — | tiny | ✅ | ❌ |
| 334 | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 1.5B | — | tiny | ✅ | ✅ |

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
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

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

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 1.83，r = B/C = 0.546358），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002434，maxdev = 0.1174。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 40，10B–100B: 103，100B–1T: 130，1T–2.8T: 8
- 中位数位置 0.504；左 132 个，右 152 个
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
**模型数（有参数量数据）**: 334（总体帕累托前沿 11 个；图表入图 284 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.1248，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 50 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
