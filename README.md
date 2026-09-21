# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.1244，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 282 个入图，50 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3 (max) | 0.8858 | 2.8T | 104B | large | ✅ | ✅ |
| 2 | GLM-5.3 (max) | 0.8699 | 753B | 40B | large | ✅ | ✅ |
| 3 | Step 5 Preview | 0.8537 | 600B | — | large | ❌ | ✅ |
| 4 | Qwen3.8 2.4T A95B | 0.8288 | 2.4T | 95B | large | ✅ | ✅ |
| 5 | GLM-5.3-Flash | 0.8148 | 320B | 18B | large | ✅ | ✅ |
| 6 | GLM-5.2 (max) | 0.8004 | 753B | 40B | large | ✅ | ✅ |
| 7 | Qwen3.8-Flash-Next | 0.7703 | 180B | 6B | large | ✅ | ✅ |
| 8 | DeepSeek V4 Pro 0813 (max) | 0.7403 | 1.6T | 49B | large | ✅ | ✅ |
| 9 | DeepSeek V4.1 Flash (max) | 0.7204 | 552B | 16B | large | ✅ | ✅ |
| 10 | Qwen3.8 27B (xhigh) | 0.7165 | 27B | — | small | ✅ | ✅ |
| 11 | Kimi K2.6 | 0.7144 | 1T | 32B | large | ✅ | ✅ |
| 12 | DeepSeek V4 Flash Vision (max) | 0.7032 | 284B | — | large | ❌ | ✅ |
| 13 | DeepSeek V4 Flash 0731 (max) | 0.7005 | 284B | 13B | large | ✅ | ✅ |
| 14 | Motif 3 | 0.6864 | 314B | 13.2B | large | ✅ | ✅ |
| 15 | Kimi K3 (low) | 0.6862 | 2.8T | 104B | large | ✅ | ✅ |
| 16 | MiniMax-M3 | 0.6810 | 428B | 23B | large | ✅ | ✅ |
| 17 | DeepSeek V4 Pro (max) | 0.6686 | 1.6T | 49B | large | ✅ | ✅ |
| 18 | GLM-5.1 | 0.6629 | 744B | 40B | large | ✅ | ✅ |
| 19 | DeepSeek V4 Pro (high) | 0.6551 | 1.6T | 49B | large | ✅ | ✅ |
| 20 | K2 Horizon 375B A23B | 0.6532 | 375B | 23B | large | ✅ | ✅ |
| 21 | GLM-5 | 0.6484 | 744B | 40B | large | ✅ | ✅ |
| 22 | Kimi K2.7 Code | 0.6424 | 1T | 32B | large | ✅ | ✅ |
| 23 | Ling-3.0-flash-VL | 0.6269 | 124B | 5.5B | medium | ✅ | ✅ |
| 24 | Inkling Small | 0.6206 | 266B | 12B | large | ✅ | ✅ |
| 25 | MiMo-V2.5-Pro | 0.6190 | 1T | 42B | large | ✅ | ✅ |
| 26 | MiMo-V2.5 | 0.6160 | 310B | 15B | large | ✅ | ✅ |
| 27 | Inkling | 0.6158 | 975B | 41B | large | ✅ | ✅ |
| 28 | DeepSeek V4 Flash (max) | 0.6143 | 284B | 13B | large | ✅ | ✅ |
| 29 | DeepSeek V4 Flash (high) | 0.6104 | 284B | 13B | large | ✅ | ✅ |
| 30 | Solar Open2 250B | 0.6013 | 250B | 15B | large | ✅ | ✅ |
| 31 | Quasar 438B (max) | 0.6006 | 438B | — | large | ❌ | ✅ |
| 32 | Nex-N2-Pro | 0.5970 | 397B | 17B | large | ✅ | ✅ |
| 33 | Motif 3 (Beta) | 0.5967 | 314B | — | large | ❌ | ✅ |
| 34 | Qwen3.5 27B | 0.5926 | 27.8B | — | small | ✅ | ✅ |
| 35 | MiMo-V2-Flash (Feb 2026) | 0.5925 | 309B | 15B | large | ✅ | ✅ |
| 36 | Qwen3.6 27B | 0.5905 | 27.8B | — | small | ✅ | ✅ |
| 37 | Kimi K2.5 | 0.5855 | 1T | 32B | large | ✅ | ✅ |
| 38 | Nemotron 3 Ultra | 0.5843 | 550B | 55B | large | ✅ | ✅ |
| 39 | Qwen3.8 27B (medium) | 0.5795 | 27B | — | small | ✅ | ✅ |
| 40 | Kimi K2 Thinking | 0.5758 | 1T | 32B | large | ✅ | ✅ |
| 41 | Qwen3.5 397B A17B | 0.5725 | 397B | 17B | large | ✅ | ✅ |
| 42 | Hy3 | 0.5691 | 299B | 21B | large | ✅ | ✅ |
| 43 | Kimi K2.6 (Non-reasoning) | 0.5688 | 1T | 32B | large | ✅ | ❌ |
| 44 | A.X-K2 | 0.5667 | 692B | 33B | large | ✅ | ✅ |
| 45 | K2 Horizon MoVA 36B A4B | 0.5656 | 36B | 4B | small | ✅ | ✅ |
| 46 | Qwen3.8 27B (low) | 0.5641 | 27B | — | small | ✅ | ✅ |
| 47 | MiniMax-M2.7 | 0.5639 | 230B | 10B | large | ✅ | ✅ |
| 48 | Hy3-preview | 0.5554 | 295B | 21B | large | ✅ | ✅ |
| 49 | JT-4.1 Flash 236B A21B | 0.5502 | 236B | — | large | ❌ | ❌ |
| 50 | MiniMax-M2.5 | 0.5495 | 230B | 10B | large | ✅ | ✅ |
| 51 | GLM-5.1 (Non-reasoning) | 0.5494 | 744B | 40B | large | ✅ | ❌ |
| 52 | Qwen3.6 35B A3B | 0.5478 | 36B | 3B | small | ✅ | ✅ |
| 53 | Ling 3.0 Flash | 0.5439 | 124B | 5.1B | medium | ✅ | ✅ |
| 54 | Agnes 2.5 Pro Alpha | 0.5432 | 397B | 17B | large | ✅ | ✅ |
| 55 | Qwen3.5 122B A10B | 0.5353 | 125B | 10B | medium | ✅ | ✅ |
| 56 | MiniMax-M2.1 | 0.5344 | 230B | 10B | large | ✅ | ✅ |
| 57 | Step 3.7 Flash | 0.5314 | 198B | 11B | large | ✅ | ✅ |
| 58 | G9v3-39A5B | 0.5307 | 39B | 5B | small | ✅ | ✅ |
| 59 | Qwen3.5 35B A3B | 0.5285 | 36B | 3B | small | ✅ | ✅ |
| 60 | Kimi K2.5 (Non-reasoning) | 0.5236 | 1T | 32B | large | ✅ | ❌ |
| 61 | Qwen3.8 27B | 0.5227 | 27B | — | small | ✅ | ❌ |
| 62 | MiMo-V2-Flash | 0.5223 | 309B | 15B | large | ✅ | ✅ |
| 63 | GLM-4.7 | 0.5188 | 357B | 32B | large | ✅ | ✅ |
| 64 | Gemma 4 31B | 0.5152 | 30.7B | — | small | ✅ | ✅ |
| 65 | DeepSeek V3.2 | 0.5145 | 685B | 37B | large | ✅ | ✅ |
| 66 | Ling-3.0-flash-Fin | 0.5143 | 124B | 5.1B | medium | ✅ | ✅ |
| 67 | GLM-5 (Non-reasoning) | 0.5121 | 744B | 40B | large | ✅ | ❌ |
| 68 | Qwen3.5 397B A17B (Non-reasoning) | 0.5058 | 397B | 17B | large | ✅ | ❌ |
| 69 | Muse Glimmer (high) | 0.5049 | 30B | — | small | ✅ | ✅ |
| 70 | K-EXAONE 2.0 | 0.4910 | 750B | 37B | large | ✅ | ✅ |
| 71 | Qwen3.5 27B (Non-reasoning) | 0.4905 | 27.8B | — | small | ✅ | ❌ |
| 72 | DeepSeek V3.2 Speciale | 0.4894 | 685B | 37B | large | ✅ | ✅ |
| 73 | JT-35B-Flash | 0.4876 | 35B | — | small | ❌ | ❌ |
| 74 | Step 3.5 Flash | 0.4871 | 196B | 11B | large | ✅ | ✅ |
| 75 | Command A+ | 0.4817 | 218B | 25B | large | ✅ | ✅ |
| 76 | Ring-2.6-1T | 0.4814 | 1T | 63B | large | ✅ | ✅ |
| 77 | MiniMax-M2 | 0.4743 | 230B | 10B | large | ✅ | ✅ |
| 78 | K2 Horizon 7B | 0.4738 | 7B | — | small | ✅ | ✅ |
| 79 | Mistral Medium 3.5 | 0.4726 | 128B | — | medium | ✅ | ✅ |
| 80 | DeepSeek V4 Pro (Non-reasoning) | 0.4598 | 1.6T | 49B | large | ✅ | ❌ |
| 81 | GLM-5.2 (Non-reasoning) | 0.4543 | 753B | 40B | large | ✅ | ❌ |
| 82 | LongCat 2.0 | 0.4541 | 1.6T | 48B | large | ✅ | ✅ |
| 83 | Qwen3.6 27B (Non-reasoning) | 0.4483 | 27.8B | — | small | ✅ | ❌ |
| 84 | DeepSeek V3.2 Exp | 0.4426 | 685B | 37B | large | ✅ | ✅ |
| 85 | DeepSeek V3.1 Terminus | 0.4411 | 685B | 37B | large | ✅ | ✅ |
| 86 | Qwen3.5 122B A10B (Non-reasoning) | 0.4288 | 125B | 10B | medium | ✅ | ❌ |
| 87 | Qwen3.5 9B | 0.4240 | 9.65B | — | small | ✅ | ✅ |
| 88 | MiMo-V2.5-Pro (Non-reasoning) | 0.4213 | 1T | 42B | large | ✅ | ❌ |
| 89 | Gemma 4 26B A4B | 0.4181 | 25.2B | 3.8B | small | ✅ | ✅ |
| 90 | Kimi K2 0905 | 0.4176 | 1T | 32B | large | ✅ | ❌ |
| 91 | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | 284B | 13B | large | ✅ | ❌ |
| 92 | Qwen3 VL 235B A22B (Reasoning) | 0.4165 | 235B | 22B | large | ✅ | ✅ |
| 93 | Ling-2.6-1T | 0.4135 | 1T | 63B | large | ✅ | ❌ |
| 94 | DeepSeek V3.2 (Non-reasoning) | 0.4078 | 685B | 37B | large | ✅ | ❌ |
| 95 | EXAONE 4.5 33B | 0.4066 | 34.4B | — | small | ✅ | ✅ |
| 96 | Hy3-preview (Non-reasoning) | 0.4061 | 295B | 21B | large | ✅ | ❌ |
| 97 | Ling 3.0 Tiny | 0.4058 | 7.9B | 1.3B | small | ✅ | ✅ |
| 98 | Qwen3.5 4B | 0.4056 | 4.66B | — | small | ✅ | ✅ |
| 99 | GLM-4.7 (Non-reasoning) | 0.4029 | 357B | 32B | large | ✅ | ❌ |
| 100 | Qwen3.6 35B A3B (Non-reasoning) | 0.3971 | 36B | 3B | small | ✅ | ❌ |
| 101 | Gemma 4 12B | 0.3955 | 12B | — | small | ✅ | ✅ |
| 102 | DeepSeek V3.1 | 0.3945 | 685B | 37B | large | ✅ | ✅ |
| 103 | GLM-4.5 | 0.3937 | 355B | 32B | large | ✅ | ✅ |
| 104 | MiniCPM5-2B | 0.3906 | 2.6B | — | tiny | ✅ | ✅ |
| 105 | Kimi K2 | 0.3838 | 1T | 32B | large | ✅ | ❌ |
| 106 | GLM-4.6 | 0.3834 | 357B | 32B | large | ✅ | ✅ |
| 107 | DeepSeek R1 0528 | 0.3830 | 685B | 37B | large | ✅ | ✅ |
| 108 | K-EXAONE | 0.3816 | 236B | 23B | large | ✅ | ✅ |
| 109 | Gemma 4 31B (Non-reasoning) | 0.3786 | 30.7B | — | small | ✅ | ❌ |
| 110 | K2 Horizon 3.7B | 0.3781 | 3.7B | — | tiny | ✅ | ✅ |
| 111 | Granite 4.2 30B | 0.3759 | 30B | — | small | ✅ | ✅ |
| 112 | Nemotron 3 Super | 0.3746 | 120.6B | 12.7B | medium | ✅ | ✅ |
| 113 | Trinity Large Thinking | 0.3738 | 399B | 13B | large | ✅ | ✅ |
| 114 | Qwen3 VL 32B (Reasoning) | 0.3733 | 33.4B | — | small | ✅ | ✅ |
| 115 | Qwen3.5 9B (Non-reasoning) | 0.3692 | 9.65B | — | small | ✅ | ❌ |
| 116 | GLM-4.7-Flash | 0.3689 | 31.2B | 3B | small | ✅ | ✅ |
| 117 | Nemotron 3.5 Lightning | 0.3683 | 31.6B | 3.6B | small | ✅ | ✅ |
| 118 | Qwen3.5 35B A3B (Non-reasoning) | 0.3660 | 36B | 3B | small | ✅ | ❌ |
| 119 | GLM-4.6 (Non-reasoning) | 0.3657 | 357B | 32B | large | ✅ | ❌ |
| 120 | Qwen3 235B A22B 2507 | 0.3626 | 235B | 22B | large | ✅ | ✅ |
| 121 | Apriel-v1.5-15B-Thinker | 0.3622 | 15B | — | small | ✅ | ✅ |
| 122 | Qwen3 Coder 480B | 0.3566 | 480B | 35B | large | ✅ | ❌ |
| 123 | Nemotron Cascade 2 30B A3B | 0.3552 | 31.6B | 3B | small | ✅ | ✅ |
| 124 | Cogito v2.1 | 0.3547 | 671B | 37B | large | ✅ | ✅ |
| 125 | Apriel-v1.6-15B-Thinker | 0.3516 | 15B | — | small | ✅ | ✅ |
| 126 | G9v3-3B | 0.3512 | 3B | — | tiny | ✅ | ✅ |
| 127 | Gemma 4 26B A4B (Non-reasoning) | 0.3507 | 25.2B | 3.8B | small | ✅ | ❌ |
| 128 | gpt-oss-120b (high) | 0.3495 | 117B | 5.1B | medium | ✅ | ✅ |
| 129 | GLM-4.6V | 0.3493 | 108B | 12B | medium | ✅ | ✅ |
| 130 | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3485 | 685B | 37B | large | ✅ | ❌ |
| 131 | MiMo-V2-Flash (Non-reasoning) | 0.3404 | 309B | 15B | large | ✅ | ❌ |
| 132 | Mistral Small 4 | 0.3363 | 119B | 6.5B | medium | ✅ | ✅ |
| 133 | DeepSeek V3.2 Exp (Non-reasoning) | 0.3309 | 685B | 37B | large | ✅ | ❌ |
| 134 | HyperNova 60B 2605 (high) | 0.3288 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 135 | DeepSeek V3.1 (Non-reasoning) | 0.3276 | 685B | 37B | large | ✅ | ❌ |
| 136 | North Mini Code | 0.3269 | 30B | 3B | small | ✅ | ✅ |
| 137 | Seed-OSS-36B-Instruct | 0.3236 | 36.2B | — | small | ✅ | ✅ |
| 138 | Granite 4.2 8B | 0.3210 | 8B | — | small | ✅ | ✅ |
| 139 | Solar Pro 3 | 0.3175 | 102B | — | medium | ❌ | ✅ |
| 140 | Qwen3 235B 2507 | 0.3165 | 235B | 22B | large | ✅ | ❌ |
| 141 | K2 Think V2 | 0.3154 | 70B | — | medium | ✅ | ✅ |
| 142 | Qwen3 Next 80B A3B (Reasoning) | 0.3088 | 80B | 3B | medium | ✅ | ✅ |
| 143 | Nemotron 3 Nano | 0.3085 | 31.6B | 3.6B | small | ✅ | ✅ |
| 144 | Gemma 4 12B (Non-reasoning) | 0.3078 | 12B | — | small | ✅ | ❌ |
| 145 | Qwen3 VL 235B A22B | 0.3073 | 235B | — | large | ✅ | ❌ |
| 146 | QwQ-32B | 0.3060 | 32.8B | — | small | ✅ | ✅ |
| 147 | Ring-1T | 0.3043 | 1T | 50B | large | ✅ | ✅ |
| 148 | MiniCPM5-1B | 0.3042 | 1B | — | tiny | ✅ | ✅ |
| 149 | MiniCPM5-1B (Non-reasoning) | 0.3041 | 1B | — | tiny | ✅ | ❌ |
| 150 | Pixtral Large | 0.3029 | 124B | — | medium | ✅ | ❌ |
| 151 | Solar Open 100B | 0.2994 | 102B | 12B | medium | ✅ | ✅ |
| 152 | Qwen3 Coder Next | 0.2986 | 79.7B | 3B | medium | ✅ | ❌ |
| 153 | Qwen3.5 4B (Non-reasoning) | 0.2972 | 4.66B | — | small | ✅ | ❌ |
| 154 | MiniMax M1 80k | 0.2960 | 456B | 45.9B | large | ✅ | ✅ |
| 155 | GLM-4.5-Air | 0.2958 | 106B | 12B | medium | ✅ | ✅ |
| 156 | Gemma 4 E4B | 0.2950 | 8B | 4.5B | small | ✅ | ✅ |
| 157 | DiffusionGemma 26B A4B | 0.2910 | 25.2B | 3.8B | small | ✅ | ✅ |
| 158 | MiniMax M1 40k | 0.2895 | 456B | 45.9B | large | ✅ | ✅ |
| 159 | HyperCLOVA X SEED Think (32B) | 0.2887 | 32B | — | small | ✅ | ✅ |
| 160 | DeepSeek V3 0324 | 0.2874 | 671B | 37B | large | ✅ | ❌ |
| 161 | K2-V2 (high) | 0.2865 | 70B | — | medium | ✅ | ✅ |
| 162 | K-EXAONE (Non-reasoning) | 0.2860 | 236B | 23B | large | ✅ | ❌ |
| 163 | DeepSeek R1 (Jan) | 0.2853 | 685B | 37B | large | ✅ | ✅ |
| 164 | Mistral Large 3 | 0.2841 | 675B | 41B | large | ✅ | ❌ |
| 165 | Llama 4 Maverick | 0.2826 | 402B | 17B | large | ✅ | ❌ |
| 166 | gpt-oss-20b (high) | 0.2795 | 21B | 3.6B | small | ✅ | ✅ |
| 167 | INTELLECT-3 | 0.2772 | 107B | 12B | medium | ✅ | ✅ |
| 168 | Nemotron 3 Nano Omni 30B A3B | 0.2762 | 30B | 3B | small | ✅ | ✅ |
| 169 | Qwen3 30B A3B 2507 | 0.2759 | 30.5B | 3.3B | small | ✅ | ✅ |
| 170 | Tri-21B-think Preview | 0.2755 | 21B | — | small | ✅ | ✅ |
| 171 | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 30B | 3B | small | ✅ | ✅ |
| 172 | LongCat Flash Lite | 0.2741 | 68.5B | 3B | medium | ✅ | ❌ |
| 173 | gpt-oss-20b (low) | 0.2732 | 21B | 3.6B | small | ✅ | ✅ |
| 174 | Llama 3.1 405B | 0.2722 | 405B | — | large | ✅ | ❌ |
| 175 | Gemma 4 E4B (Non-reasoning) | 0.2703 | 8B | 4.5B | small | ✅ | ❌ |
| 176 | Ling 2.6 Flash | 0.2703 | 107B | 7.4B | medium | ✅ | ❌ |
| 177 | Tri-21B-Think | 0.2697 | 21B | — | small | ✅ | ✅ |
| 178 | Granite 4.2 3B | 0.2678 | 3B | — | tiny | ✅ | ✅ |
| 179 | Qwen3 VL 32B | 0.2624 | 33.4B | — | small | ✅ | ❌ |
| 180 | Qwen3 Next 80B A3B | 0.2622 | 80B | 3B | medium | ✅ | ❌ |
| 181 | Hermes 4 405B | 0.2605 | 406B | — | large | ✅ | ✅ |
| 182 | K2-V2 (medium) | 0.2576 | 70B | — | medium | ✅ | ✅ |
| 183 | Ling-1T | 0.2569 | 1T | 50B | large | ✅ | ❌ |
| 184 | Motif-2-12.7B | 0.2563 | 12.7B | — | small | ❌ | ✅ |
| 185 | gpt-oss-120b (low) | 0.2558 | 117B | 5.1B | medium | ✅ | ✅ |
| 186 | Qwen3 VL 8B (Reasoning) | 0.2534 | 8.77B | — | small | ✅ | ✅ |
| 187 | Step3 VL 10B | 0.2520 | 10.2B | — | small | ✅ | ✅ |
| 188 | Llama Nemotron Super 49B v1.5 | 0.2496 | 49B | — | medium | ✅ | ✅ |
| 189 | Devstral 2 | 0.2491 | 125B | — | medium | ✅ | ❌ |
| 190 | GLM-4.7-Flash (Non-reasoning) | 0.2488 | 31.2B | 3B | small | ✅ | ❌ |
| 191 | ERNIE 4.5 300B A47B | 0.2462 | 300B | 47B | large | ✅ | ❌ |
| 192 | Qwen3 4B 2507 | 0.2430 | 4.02B | — | tiny | ✅ | ✅ |
| 193 | Mistral Small 4 (Non-reasoning) | 0.2422 | 119B | 6.5B | medium | ✅ | ❌ |
| 194 | Hermes 4 405B (Non-reasoning) | 0.2408 | 406B | — | large | ✅ | ❌ |
| 195 | Qwen3 Coder 30B A3B | 0.2396 | 30.5B | 3.3B | small | ✅ | ❌ |
| 196 | LFM2.5-8B-A1B | 0.2374 | 8.3B | 1.5B | small | ✅ | ✅ |
| 197 | Qwen3 VL 30B A3B | 0.2369 | 30B | 3B | small | ✅ | ❌ |
| 198 | GLM-4.6V (Non-reasoning) | 0.2361 | 108B | 12B | medium | ✅ | ❌ |
| 199 | Gemma 4 E2B | 0.2348 | 5.1B | 2.3B | small | ✅ | ✅ |
| 200 | Qwen3 Omni 30B A3B (Reasoning) | 0.2344 | 35.3B | 3B | small | ✅ | ✅ |
| 201 | LFM2.5-2.6B | 0.2338 | 2.7B | — | tiny | ✅ | ✅ |
| 202 | Qwen3 235B | 0.2305 | 235B | 22B | large | ✅ | ✅ |
| 203 | GLM-4.5V | 0.2295 | 108B | 12B | medium | ✅ | ✅ |
| 204 | NVIDIA Nemotron Nano 12B v2 VL | 0.2286 | 13.2B | — | small | ✅ | ✅ |
| 205 | Mistral Large 2 (Nov) | 0.2276 | 123B | — | medium | ✅ | ❌ |
| 206 | Falcon-H1R-7B | 0.2261 | 7B | — | small | ✅ | ✅ |
| 207 | Devstral Small 2 | 0.2257 | 24B | — | small | ✅ | ❌ |
| 208 | Llama Nemotron Ultra | 0.2253 | 253B | — | large | ✅ | ✅ |
| 209 | DeepSeek V3 (Dec) | 0.2196 | 671B | 37B | large | ✅ | ❌ |
| 210 | Mistral Small 3.2 | 0.2167 | 24B | — | small | ✅ | ❌ |
| 211 | Nanbeige4.1-3B | 0.2162 | 3.93B | — | tiny | ✅ | ✅ |
| 212 | Olmo 3.1 32B Think | 0.2152 | 32.2B | — | small | ✅ | ✅ |
| 213 | Sarvam 105B (high) | 0.2147 | 106B | 10.3B | medium | ✅ | ✅ |
| 214 | EXAONE 4.0 32B | 0.2138 | 32B | — | small | ✅ | ✅ |
| 215 | Magistral Small 1.2 | 0.2130 | 24B | — | small | ✅ | ✅ |
| 216 | K2-V2 (low) | 0.2118 | 70B | — | medium | ✅ | ✅ |
| 217 | NVIDIA Nemotron Nano 9B V2 | 0.2114 | 9B | — | small | ✅ | ✅ |
| 218 | Qwen3.5 2B | 0.2111 | 2.27B | — | tiny | ✅ | ✅ |
| 219 | Ring-flash-2.0 | 0.2089 | 103B | 6.1B | medium | ✅ | ✅ |
| 220 | Llama 4 Scout | 0.2075 | 109B | 17B | medium | ✅ | ❌ |
| 221 | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2071 | 49B | — | medium | ✅ | ❌ |
| 222 | Qwen3 32B | 0.2062 | 32.8B | — | small | ✅ | ✅ |
| 223 | Hermes 4 70B | 0.2054 | 70.6B | — | medium | ✅ | ✅ |
| 224 | Devstral Small (May) | 0.2041 | 23.6B | — | small | ✅ | ❌ |
| 225 | DeepSeek R1 Distill Qwen 32B | 0.2009 | 32B | — | small | ✅ | ✅ |
| 226 | Qwen3 14B | 0.2006 | 14.8B | — | small | ✅ | ✅ |
| 227 | Llama 3.3 Nemotron Super 49B | 0.2006 | 49B | — | medium | ✅ | ✅ |
| 228 | Qwen2.5 72B | 0.1995 | 72B | — | medium | ✅ | ❌ |
| 229 | Ling-flash-2.0 | 0.1985 | 103B | 6.1B | medium | ✅ | ❌ |
| 230 | Qwen3 VL 8B | 0.1981 | 8.77B | — | small | ✅ | ❌ |
| 231 | Qwen3 30B | 0.1966 | 30.5B | 3.3B | small | ✅ | ✅ |
| 232 | Magistral Small 1 | 0.1965 | 23.6B | — | small | ✅ | ✅ |
| 233 | Ministral 3 14B | 0.1927 | 14B | — | small | ✅ | ❌ |
| 234 | Mistral Large 2 (Jul) | 0.1920 | 123B | — | medium | ✅ | ❌ |
| 235 | Command A | 0.1913 | 111B | — | medium | ✅ | ❌ |
| 236 | Devstral Small | 0.1906 | 24B | — | small | ✅ | ❌ |
| 237 | Qwen3 235B (Non-reasoning) | 0.1905 | 235B | 22B | large | ✅ | ❌ |
| 238 | Llama 3.1 Nemotron 70B | 0.1891 | 70B | — | medium | ✅ | ❌ |
| 239 | Nemotron 3 Nano 4B | 0.1873 | 3.97B | — | tiny | ✅ | ✅ |
| 240 | Qwen3 VL 4B (Reasoning) | 0.1866 | 4.44B | — | tiny | ✅ | ✅ |
| 241 | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1840 | 49B | — | medium | ✅ | ❌ |
| 242 | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1821 | 30.5B | 3.3B | small | ✅ | ❌ |
| 243 | Qwen3 4B | 0.1808 | 4.02B | — | tiny | ✅ | ✅ |
| 244 | Llama 3.1 70B | 0.1803 | 70B | — | medium | ✅ | ❌ |
| 245 | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1798 | 9B | — | small | ✅ | ❌ |
| 246 | Qwen3 32B (Non-reasoning) | 0.1789 | 32.8B | — | small | ✅ | ❌ |
| 247 | GLM-4.5V (Non-reasoning) | 0.1781 | 108B | 12B | medium | ✅ | ❌ |
| 248 | Gemma 4 E2B (Non-reasoning) | 0.1780 | 5.1B | 2.3B | small | ✅ | ❌ |
| 249 | Qwen3.5 2B (Non-reasoning) | 0.1758 | 2.27B | — | tiny | ✅ | ❌ |
| 250 | Granite 4.1 30B | 0.1754 | 30B | — | small | ✅ | ❌ |
| 251 | Olmo 3.1 32B Instruct | 0.1725 | 32.2B | — | small | ✅ | ❌ |
| 252 | Qwen3 Omni 30B A3B | 0.1709 | 35.3B | 3B | small | ✅ | ❌ |
| 253 | Qwen3 4B 2507 (Non-reasoning) | 0.1689 | 4.02B | — | tiny | ✅ | ❌ |
| 254 | Llama 3.1 8B | 0.1674 | 8B | — | small | ✅ | ❌ |
| 255 | Olmo 3 32B Think | 0.1648 | 32.2B | — | small | ✅ | ✅ |
| 256 | DeepSeek R1 Distill Qwen 14B | 0.1644 | 14B | — | small | ✅ | ✅ |
| 257 | DeepSeek R1 Distill Llama 70B | 0.1644 | 70B | — | medium | ✅ | ✅ |
| 258 | Llama 3.3 70B | 0.1636 | 70B | — | medium | ✅ | ❌ |
| 259 | Kimi Linear 48B A3B Instruct | 0.1632 | 49.1B | 3B | medium | ✅ | ❌ |
| 260 | Ministral 3 8B | 0.1628 | 8B | — | small | ✅ | ❌ |
| 261 | Hermes 4 70B (Non-reasoning) | 0.1588 | 70.6B | — | medium | ✅ | ❌ |
| 262 | Jamba Reasoning 3B | 0.1582 | 3B | — | tiny | ✅ | ✅ |
| 263 | EXAONE 4.0 32B (Non-reasoning) | 0.1562 | 32B | — | small | ✅ | ❌ |
| 264 | Granite 4.1 8B | 0.1560 | 8B | — | small | ✅ | ❌ |
| 265 | LFM2 24B A2B | 0.1528 | 23.8B | 2.3B | small | ✅ | ❌ |
| 266 | Qwen3 8B | 0.1527 | 8.19B | — | small | ✅ | ✅ |
| 267 | Jamba 1.7 Large | 0.1517 | 398B | 94B | large | ✅ | ❌ |
| 268 | Sarvam 30B (high) | 0.1499 | 32.2B | 2.4B | small | ✅ | ✅ |
| 269 | Mistral Small 3 | 0.1486 | 24B | — | small | ✅ | ❌ |
| 270 | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1482 | 13.2B | — | small | ✅ | ❌ |
| 271 | MiniCPM-V 4.6 1.3B | 0.1477 | 1.3B | — | tiny | ✅ | ❌ |
| 272 | Qwen3 30B (Non-reasoning) | 0.1436 | 30.5B | 3.3B | small | ✅ | ❌ |
| 273 | Nemotron 3 Nano (Non-reasoning) | 0.1409 | 31.6B | 3.6B | small | ✅ | ❌ |
| 274 | Granite 4.0 H Small | 0.1378 | 32B | 9B | small | ✅ | ❌ |
| 275 | Qwen3 VL 4B | 0.1374 | 4.44B | — | tiny | ✅ | ❌ |
| 276 | Gemma 3 27B | 0.1367 | 27.4B | — | small | ✅ | ❌ |
| 277 | DeepSeek R1 0528 Qwen3 8B | 0.1338 | 8.19B | — | small | ✅ | ✅ |
| 278 | Ministral 3 3B | 0.1325 | 3B | — | tiny | ✅ | ❌ |
| 279 | Qwen3 14B (Non-reasoning) | 0.1317 | 14.8B | — | small | ✅ | ❌ |
| 280 | Phi-4 | 0.1271 | 14B | — | small | ✅ | ❌ |
| 281 | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1268 | 4.51B | — | small | ✅ | ✅ |
| 282 | Gemma 3 270M | 0.1244 | 0.268B | — | tiny | ✅ | ❌ |
| 283 | Llama 3 70B | 0.1190 | 70B | — | medium | ✅ | ❌ |
| 284 | Llama 3.2 11B (Vision) | 0.1186 | 11B | — | small | ✅ | ❌ |
| 285 | Llama 3.2 3B | 0.1168 | 3B | — | tiny | ✅ | ❌ |
| 286 | Qwen3.5 0.8B | 0.1155 | 0.873B | — | tiny | ✅ | ✅ |
| 287 | Olmo 3 7B Think | 0.1150 | 7B | — | small | ✅ | ✅ |
| 288 | LFM2.5-1.2B-Instruct | 0.1084 | 1.17B | — | tiny | ✅ | ❌ |
| 289 | Reka Flash 3 | 0.1079 | 21B | — | small | ✅ | ✅ |
| 290 | LFM2 2.6B | 0.1076 | 2.57B | — | tiny | ✅ | ❌ |
| 291 | Ling-mini-2.0 | 0.1074 | 16.3B | 1.4B | small | ✅ | ❌ |
| 292 | Qwen3 8B (Non-reasoning) | 0.1063 | 8.19B | — | small | ✅ | ❌ |
| 293 | Molmo2-8B | 0.1033 | 8.66B | — | small | ✅ | ❌ |
| 294 | Sarvam M | 0.1029 | 23.6B | — | small | ✅ | ✅ |
| 295 | Jamba 1.7 Mini | 0.1016 | 52B | 12B | medium | ✅ | ❌ |
| 296 | LFM2.5-1.2B-Thinking | 0.1002 | 1.17B | — | tiny | ✅ | ✅ |
| 297 | Gemma 3 12B | 0.0982 | 12.2B | — | small | ✅ | ❌ |
| 298 | Phi-4 Mini | 0.0980 | 3.84B | — | tiny | ✅ | ❌ |
| 299 | Apertus 70B Instruct | 0.0935 | 70B | — | medium | ✅ | ❌ |
| 300 | Qwen3.5 0.8B (Non-reasoning) | 0.0929 | 0.873B | — | tiny | ✅ | ❌ |
| 301 | Olmo 3 7B | 0.0919 | 7B | — | small | ✅ | ❌ |
| 302 | OLMo 2 32B | 0.0910 | 32.2B | — | small | ✅ | ❌ |
| 303 | Exaone 4.0 1.2B | 0.0909 | 1.28B | — | tiny | ✅ | ✅ |
| 304 | Granite 4.0 H 1B | 0.0904 | 1.5B | — | tiny | ✅ | ❌ |
| 305 | Llama 3.2 1B | 0.0895 | 1B | — | tiny | ✅ | ❌ |
| 306 | Qwen3 1.7B | 0.0880 | 2.03B | — | tiny | ✅ | ✅ |
| 307 | Granite 4.1 3B | 0.0864 | 3B | — | tiny | ✅ | ❌ |
| 308 | Exaone 4.0 1.2B (Non-reasoning) | 0.0839 | 1.28B | — | tiny | ✅ | ❌ |
| 309 | LFM2 8B A1B | 0.0822 | 8.34B | 1.5B | small | ✅ | ❌ |
| 310 | Granite 4.0 Micro | 0.0795 | 3B | — | tiny | ✅ | ❌ |
| 311 | Phi-3 Mini | 0.0751 | 3.8B | — | tiny | ✅ | ❌ |
| 312 | Granite 3.3 8B | 0.0712 | 8.17B | — | small | ✅ | ❌ |
| 313 | LFM2.5-VL-1.6B | 0.0685 | 1.6B | — | tiny | ✅ | ❌ |
| 314 | Granite 4.0 1B | 0.0678 | 1.6B | — | tiny | ✅ | ❌ |
| 315 | Granite 4.0 350M | 0.0670 | 0.35B | — | tiny | ✅ | ❌ |
| 316 | Gemma 3 4B | 0.0660 | 4.3B | — | tiny | ✅ | ❌ |
| 317 | LFM2 1.2B | 0.0651 | 1.17B | — | tiny | ✅ | ❌ |
| 318 | Qwen3 0.6B | 0.0644 | 0.752B | — | tiny | ✅ | ✅ |
| 319 | Llama 3 8B | 0.0642 | 8B | — | small | ✅ | ❌ |
| 320 | Mistral 7B | 0.0620 | 7B | — | small | ✅ | ❌ |
| 321 | Gemma 3n E4B | 0.0580 | 8.39B | 4B | small | ✅ | ❌ |
| 322 | K2 Horizon 0.9B | 0.0567 | 0.9B | — | tiny | ✅ | ✅ |
| 323 | OLMo 2 7B | 0.0564 | 7.3B | — | small | ✅ | ❌ |
| 324 | Qwen3 1.7B (Non-reasoning) | 0.0561 | 2.03B | — | tiny | ✅ | ❌ |
| 325 | Gemma 3 1B | 0.0557 | 1B | — | tiny | ✅ | ❌ |
| 326 | Apertus 8B Instruct | 0.0547 | 8B | — | small | ✅ | ❌ |
| 327 | Granite 4.0 H 350M | 0.0505 | 0.34B | — | tiny | ✅ | ❌ |
| 328 | Molmo 7B-D | 0.0477 | 8.02B | — | small | ✅ | ❌ |
| 329 | Qwen3 0.6B (Non-reasoning) | 0.0432 | 0.752B | — | tiny | ✅ | ❌ |
| 330 | Gemma 3n E2B | 0.0355 | 5.98B | 2B | small | ✅ | ❌ |
| 331 | Tiny Aya Global | 0.0351 | 3.35B | — | tiny | ✅ | ❌ |
| 332 | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 1.5B | — | tiny | ✅ | ✅ |

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
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.1244，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 1.83，r = B/C = 0.546358），用 11 品牌前沿入图模型的总参数量定出；mse = 0.002434，maxdev = 0.1174。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 40，10B–100B: 103，100B–1T: 128，1T–2.8T: 8
- 中位数位置 0.502；左 132 个，右 150 个
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
**模型数（有参数量数据）**: 332（总体帕累托前沿 11 个；图表入图 282 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.1244，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 50 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
