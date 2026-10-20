# LLM Leaderboard — 综合能力 vs 模型参数量

![Pareto Analysis](output/pareto_analysis.png)

## 参数模型（综合能力从高到低）

共收录 **Status: All**（含已弃用）有参数量数据的模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.0912，即前沿左端点 Gemma 3 270M）为 0：综合能力 ≥ 该级的有参数量数据模型 154 个入图，24 个能力低于第一级的不出现在图中；总参数量高于品牌前沿最大值的模型同样不入图（缺少参数量数据的模型不在图表和表格中）。

| # | 模型 | 综合能力 | 总参数量 | 活跃参数量 | 大小类 | 开源 | 推理 |
|---|------|---------|---------|-----------|--------|------|------|
| 1 | Kimi K3 (max) | 0.8394 | 2.8T | 104B | large | ✅ | ✅ |
| 2 | GLM-5.3 (max) | 0.8361 | 753B | 40B | large | ✅ | ✅ |
| 3 | Step 5 Preview | 0.8170 | 600B | — | large | ✅ | ✅ |
| 4 | MiMo-V2.6-Pro | 0.7981 | 1T | 42B | large | ✅ | ✅ |
| 5 | DeepSeek V4.1 Flash 1017 (max) | 0.7757 | 552B | 16B | large | ✅ | ✅ |
| 6 | GLM-5.3-Flash | 0.7729 | 320B | 18B | large | ✅ | ✅ |
| 7 | Qwen3.8 2.4T A95B | 0.7621 | 2.4T | 95B | large | ✅ | ✅ |
| 8 | Muse Spark Open (xhigh) | 0.7574 | 816B | 42B | large | ✅ | ✅ |
| 9 | Qwen3.8-Flash-Next | 0.7366 | 180B | 6B | large | ✅ | ✅ |
| 10 | Ling 3.1 Flash | 0.7111 | 560B | — | large | ✅ | ✅ |
| 11 | DeepSeek V4 Pro 0813 (max) | 0.6864 | 1.6T | 49B | large | ✅ | ✅ |
| 12 | Motif 3 | 0.6621 | 314B | 13.2B | large | ✅ | ✅ |
| 13 | Qwen3.8 27B (xhigh) | 0.6604 | 27B | — | small | ✅ | ✅ |
| 14 | DeepSeek V4 Flash Vision (max) | 0.6501 | 284B | — | large | ❌ | ✅ |
| 15 | Mistral Large 4 Preview | 0.6501 | 1T | — | large | ❌ | ✅ |
| 16 | Kimi K3 (low) | 0.6279 | 2.8T | 104B | large | ✅ | ✅ |
| 17 | JT-4.1 Flash 236B A21B | 0.6276 | 236B | — | large | ❌ | ✅ |
| 18 | MiMo-V2.6-Flash | 0.6259 | 309B | 15B | large | ✅ | ✅ |
| 19 | MiniMax-M3 | 0.6252 | 428B | 23B | large | ✅ | ✅ |
| 20 | K2 Horizon 375B A23B | 0.5885 | 375B | 23B | large | ✅ | ✅ |
| 21 | GLM-5.3 (low) | 0.5882 | 753B | 40B | large | ✅ | ✅ |
| 22 | Kimi K2.7 Code | 0.5876 | 1T | 32B | large | ✅ | ✅ |
| 23 | Nex-N2-Pro | 0.5834 | 397B | 17B | large | ✅ | ✅ |
| 24 | Ling-3.0-flash-VL | 0.5622 | 124B | 5.5B | medium | ✅ | ✅ |
| 25 | Inkling (xhigh) | 0.5493 | 975B | 41B | large | ✅ | ✅ |
| 26 | Beam 1.0 | 0.5474 | 501B | 23B | large | ✅ | ✅ |
| 27 | Solar Open2 250B | 0.5455 | 250B | 15B | large | ✅ | ✅ |
| 28 | Inkling Small | 0.5424 | 266B | 12B | large | ✅ | ✅ |
| 29 | Quasar 438B (max) | 0.5408 | 438B | — | large | ❌ | ✅ |
| 30 | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5372 | 236B | — | large | ❌ | ❌ |
| 31 | Qwen3.8 27B (medium) | 0.5287 | 27B | — | small | ✅ | ✅ |
| 32 | Nemotron 3 Ultra | 0.5272 | 550B | 55B | large | ✅ | ✅ |
| 33 | Qwen3.5 397B A17B | 0.5220 | 397B | 17B | large | ✅ | ✅ |
| 34 | Qwen3.8 27B (low) | 0.5125 | 27B | — | small | ✅ | ✅ |
| 35 | Hy3 | 0.5080 | 299B | 21B | large | ✅ | ✅ |
| 36 | K2 Horizon MoVA 36B A4B | 0.4973 | 36B | 4B | small | ✅ | ✅ |
| 37 | Nemotron 3.5 Super VL | 0.4943 | 120B | 12B | medium | ✅ | ✅ |
| 38 | Qwen3.6 35B A3B | 0.4872 | 36B | 3B | small | ✅ | ✅ |
| 39 | Qwen3.5 397B A17B (non-reasoning) | 0.4860 | 397B | 17B | large | ✅ | ❌ |
| 40 | G9v3-39A5B | 0.4843 | 39B | 5B | small | ✅ | ✅ |
| 41 | Qwen3.5 122B A10B | 0.4787 | 125B | 10B | medium | ✅ | ✅ |
| 42 | Ling-3.0-flash-Fin | 0.4690 | 124B | 5.1B | medium | ✅ | ✅ |
| 43 | JT-35B-Flash | 0.4681 | 35B | — | small | ❌ | ❌ |
| 44 | A.X-K2 | 0.4638 | 692B | 33B | large | ✅ | ✅ |
| 45 | K-EXAONE 2.0 | 0.4574 | 750B | 37B | large | ✅ | ✅ |
| 46 | Gemma 4 31B | 0.4556 | 30.7B | — | small | ✅ | ✅ |
| 47 | Qwen3.8 27B (non-reasoning) | 0.4535 | 27B | — | small | ✅ | ❌ |
| 48 | Solar Mini 4 | 0.4473 | 35B | — | small | ❌ | ✅ |
| 49 | Muse Glimmer (high) | 0.4374 | 30B | — | small | ✅ | ✅ |
| 50 | Mistral Medium 3.5 | 0.4268 | 128B | — | medium | ✅ | ✅ |
| 51 | Ring-2.6-1T | 0.4248 | 1T | 63B | large | ✅ | ✅ |
| 52 | Command A+ | 0.4129 | 218B | 25B | large | ✅ | ✅ |
| 53 | Qwen3.5 122B A10B (non-reasoning) | 0.4121 | 125B | 10B | medium | ✅ | ❌ |
| 54 | K2 Horizon 7B | 0.4093 | 7B | — | small | ✅ | ✅ |
| 55 | LongCat 2.0 | 0.3943 | 1.6T | 48B | large | ✅ | ✅ |
| 56 | Gemma 4 26B A4B | 0.3930 | 25.2B | 3.8B | small | ✅ | ✅ |
| 57 | Nemotron 3.5 Bolt 74B-A9B | 0.3865 | 74B | 9B | medium | ✅ | ✅ |
| 58 | Qwen3.6 35B A3B (non-reasoning) | 0.3752 | 36B | 3B | small | ✅ | ❌ |
| 59 | EXAONE 4.5 33B | 0.3716 | 34.4B | — | small | ✅ | ✅ |
| 60 | Qwen3.5 4B | 0.3709 | 4.66B | — | small | ✅ | ✅ |
| 61 | Gemma 4 12B | 0.3660 | 12B | — | small | ✅ | ✅ |
| 62 | Qwen3.5 9B | 0.3622 | 9.65B | — | small | ✅ | ✅ |
| 63 | Gemma 4 31B (non-reasoning) | 0.3498 | 30.7B | — | small | ✅ | ❌ |
| 64 | Qwen3.5 9B (non-reasoning) | 0.3350 | 9.65B | — | small | ✅ | ❌ |
| 65 | Cogito v2.1 | 0.3317 | 671B | 37B | large | ✅ | ✅ |
| 66 | Apriel-v1.6-15B-Thinker | 0.3274 | 15B | — | small | ✅ | ✅ |
| 67 | Gemma 4 26B A4B (non-reasoning) | 0.3265 | 25.2B | 3.8B | small | ✅ | ❌ |
| 68 | Nemotron Cascade 2 30B A3B | 0.3219 | 31.6B | 3B | small | ✅ | ✅ |
| 69 | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3178 | 1.6T | 49B | large | ✅ | ❌ |
| 70 | K2 Horizon 3.7B | 0.3104 | 3.7B | — | tiny | ✅ | ✅ |
| 71 | Trinity Large Thinking | 0.3102 | 399B | 13B | large | ✅ | ✅ |
| 72 | MiniCPM5-2B | 0.3035 | 2.6B | — | tiny | ✅ | ✅ |
| 73 | Granite 4.2 30B | 0.3029 | 30B | — | small | ✅ | ✅ |
| 74 | Ling 3.0 Tiny | 0.2986 | 7.9B | 1.3B | small | ✅ | ✅ |
| 75 | Nemotron 3.5 Lightning | 0.2985 | 31.6B | 3.6B | small | ✅ | ✅ |
| 76 | gpt-oss-120b (high) | 0.2975 | 117B | 5.1B | medium | ✅ | ✅ |
| 77 | G9v3-3B | 0.2890 | 3B | — | tiny | ✅ | ✅ |
| 78 | Gemma 4 12B (non-reasoning) | 0.2819 | 12B | — | small | ✅ | ❌ |
| 79 | North Mini Code | 0.2806 | 30B | 3B | small | ✅ | ✅ |
| 80 | Mistral Small 4 | 0.2795 | 119B | 6.5B | medium | ✅ | ✅ |
| 81 | K2 Think V2 | 0.2772 | 70B | — | medium | ✅ | ✅ |
| 82 | MiniCPM5-1B | 0.2767 | 1B | — | tiny | ✅ | ✅ |
| 83 | MiniCPM5-1B (non-reasoning) | 0.2764 | 1B | — | tiny | ✅ | ❌ |
| 84 | Solar Open 100B | 0.2728 | 102B | 12B | medium | ✅ | ✅ |
| 85 | HyperNova 60B 2605 (high) | 0.2675 | 58.7B | 4.8B | medium | ✅ | ✅ |
| 86 | Qwen3.5 4B (non-reasoning) | 0.2624 | 4.66B | — | small | ✅ | ❌ |
| 87 | HyperCLOVA X SEED Think (32B) | 0.2623 | 32B | — | small | ✅ | ✅ |
| 88 | Qwen3 Next 80B A3B | 0.2608 | 80B | 3B | medium | ✅ | ✅ |
| 89 | K2-V2 (high) | 0.2602 | 70B | — | medium | ✅ | ✅ |
| 90 | Qwen3 Coder Next | 0.2567 | 79.7B | 3B | medium | ✅ | ❌ |
| 91 | Granite 4.2 8B | 0.2504 | 8B | — | small | ✅ | ✅ |
| 92 | INTELLECT-3 | 0.2500 | 107B | 12B | medium | ✅ | ✅ |
| 93 | DiffusionGemma 26B A4B | 0.2493 | 25.2B | 3.8B | small | ✅ | ✅ |
| 94 | LongCat Flash Lite | 0.2474 | 68.5B | 3B | medium | ✅ | ❌ |
| 95 | gpt-oss-20b (low) | 0.2463 | 21B | 3.6B | small | ✅ | ✅ |
| 96 | Llama 3.1 405B | 0.2450 | 405B | — | large | ✅ | ❌ |
| 97 | Gemma 4 E4B (non-reasoning) | 0.2430 | 8B | 4.5B | small | ✅ | ❌ |
| 98 | Tri-21B-Think | 0.2425 | 21B | — | small | ✅ | ✅ |
| 99 | Nemotron 3 Nano | 0.2404 | 31.6B | 3.6B | small | ✅ | ✅ |
| 100 | Qwen3 Next 80B A3B | 0.2351 | 80B | 3B | medium | ✅ | ❌ |
| 101 | Hermes 4 405B | 0.2332 | 406B | — | large | ✅ | ✅ |
| 102 | Nemotron 3 Nano Omni 30B A3B | 0.2330 | 30B | 3B | small | ✅ | ✅ |
| 103 | K2-V2 (medium) | 0.2304 | 70B | — | medium | ✅ | ✅ |
| 104 | Gemma 4 E4B | 0.2290 | 8B | 4.5B | small | ✅ | ✅ |
| 105 | Motif-2-12.7B | 0.2289 | 12.7B | — | small | ❌ | ✅ |
| 106 | Step3 VL 10B | 0.2239 | 10.2B | — | small | ✅ | ✅ |
| 107 | gpt-oss-20b (high) | 0.2212 | 21B | 3.6B | small | ✅ | ✅ |
| 108 | ERNIE 4.5 300B A47B | 0.2187 | 300B | 47B | large | ✅ | ❌ |
| 109 | Llama 4 Maverick | 0.2180 | 402B | 17B | large | ✅ | ❌ |
| 110 | gpt-oss-120b (low) | 0.2160 | 117B | 5.1B | medium | ✅ | ✅ |
| 111 | Mistral Small 4 (non-reasoning) | 0.2141 | 119B | 6.5B | medium | ✅ | ❌ |
| 112 | Hermes 4 405B (non-reasoning) | 0.2129 | 406B | — | large | ✅ | ❌ |
| 113 | LFM2.5-8B-A1B | 0.2090 | 8.3B | 1.5B | small | ✅ | ✅ |
| 114 | Qwen3 Omni 30B A3B | 0.2058 | 35.3B | 3B | small | ✅ | ✅ |
| 115 | Granite 4.2 3B | 0.2001 | 3B | — | tiny | ✅ | ✅ |
| 116 | NVIDIA Nemotron Nano 12B v2 VL | 0.1998 | 13.2B | — | small | ✅ | ✅ |
| 117 | Falcon-H1R-7B | 0.1975 | 7B | — | small | ✅ | ✅ |
| 118 | Llama Nemotron Ultra | 0.1964 | 253B | — | large | ✅ | ✅ |
| 119 | Gemma 4 E2B | 0.1870 | 5.1B | 2.3B | small | ✅ | ✅ |
| 120 | Olmo 3.1 32B Think | 0.1862 | 32.2B | — | small | ✅ | ✅ |
| 121 | Sarvam 105B (high) | 0.1853 | 106B | 10.3B | medium | ✅ | ✅ |
| 122 | EXAONE 4.0 32B | 0.1846 | 32B | — | small | ✅ | ✅ |
| 123 | K2-V2 (low) | 0.1828 | 70B | — | medium | ✅ | ✅ |
| 124 | NVIDIA Nemotron Nano 9B V2 | 0.1819 | 9B | — | small | ✅ | ✅ |
| 125 | LFM2.5-2.6B | 0.1814 | 2.7B | — | tiny | ✅ | ✅ |
| 126 | Ring-flash-2.0 | 0.1802 | 103B | 6.1B | medium | ✅ | ✅ |
| 127 | Hermes 4 70B | 0.1760 | 70.6B | — | medium | ✅ | ✅ |
| 128 | Nanbeige4.1-3B | 0.1690 | 3.93B | — | tiny | ✅ | ✅ |
| 129 | Magistral Small 1.2 | 0.1675 | 24B | — | small | ✅ | ✅ |
| 130 | Qwen3.5 2B | 0.1673 | 2.27B | — | tiny | ✅ | ✅ |
| 131 | Command A | 0.1613 | 111B | — | medium | ✅ | ❌ |
| 132 | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1495 | 9B | — | small | ✅ | ❌ |
| 133 | Gemma 4 E2B (non-reasoning) | 0.1474 | 5.1B | 2.3B | small | ✅ | ❌ |
| 134 | Llama 4 Scout | 0.1461 | 109B | 17B | medium | ✅ | ❌ |
| 135 | Olmo 3.1 32B Instruct | 0.1419 | 32.2B | — | small | ✅ | ❌ |
| 136 | Qwen3 Omni 30B A3B | 0.1404 | 35.3B | 3B | small | ✅ | ❌ |
| 137 | Ministral 3 14B | 0.1396 | 14B | — | small | ✅ | ❌ |
| 138 | Kimi Linear 48B A3B Instruct | 0.1330 | 49.1B | 3B | medium | ✅ | ❌ |
| 139 | Qwen3.5 2B (non-reasoning) | 0.1309 | 2.27B | — | tiny | ✅ | ❌ |
| 140 | Hermes 4 70B (non-reasoning) | 0.1275 | 70.6B | — | medium | ✅ | ❌ |
| 141 | Jamba Reasoning 3B | 0.1273 | 3B | — | tiny | ✅ | ✅ |
| 142 | Nemotron 3 Nano 4B | 0.1254 | 3.97B | — | tiny | ✅ | ✅ |
| 143 | EXAONE 4.0 32B (non-reasoning) | 0.1254 | 32B | — | small | ✅ | ❌ |
| 144 | Llama 3.3 70B | 0.1237 | 70B | — | medium | ✅ | ❌ |
| 145 | LFM2 24B A2B | 0.1217 | 23.8B | 2.3B | small | ✅ | ❌ |
| 146 | Jamba 1.7 Large | 0.1205 | 398B | 94B | large | ✅ | ❌ |
| 147 | Sarvam 30B (high) | 0.1189 | 32.2B | 2.4B | small | ✅ | ✅ |
| 148 | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1167 | 13.2B | — | small | ✅ | ❌ |
| 149 | Nemotron 3 Nano (non-reasoning) | 0.1102 | 31.6B | 3.6B | small | ✅ | ❌ |
| 150 | Ministral 3 8B | 0.1081 | 8B | — | small | ✅ | ❌ |
| 151 | Granite 4.0 H Small | 0.1062 | 32B | 9B | small | ✅ | ❌ |
| 152 | MiniCPM-V 4.6 1.3B | 0.1036 | 1.3B | — | tiny | ✅ | ❌ |
| 153 | Phi-4 | 0.0954 | 14B | — | small | ✅ | ❌ |
| 154 | Gemma 3 270M | 0.0912 | 0.268B | — | tiny | ✅ | ❌ |
| 155 | Llama 3.2 11B (Vision) | 0.0858 | 11B | — | small | ✅ | ❌ |
| 156 | Olmo 3 7B Think | 0.0828 | 7B | — | small | ✅ | ✅ |
| 157 | Ministral 3 3B | 0.0776 | 3B | — | tiny | ✅ | ❌ |
| 158 | LFM2.5-1.2B-Instruct | 0.0757 | 1.17B | — | tiny | ✅ | ❌ |
| 159 | Reka Flash 3 | 0.0754 | 21B | — | small | ✅ | ✅ |
| 160 | Qwen3.5 0.8B | 0.0723 | 0.873B | — | tiny | ✅ | ✅ |
| 161 | Molmo2-8B | 0.0704 | 8.66B | — | small | ✅ | ❌ |
| 162 | Jamba 1.7 Mini | 0.0687 | 52B | 12B | medium | ✅ | ❌ |
| 163 | LFM2.5-1.2B-Thinking | 0.0673 | 1.17B | — | tiny | ✅ | ✅ |
| 164 | Apertus 70B Instruct | 0.0599 | 70B | — | medium | ✅ | ❌ |
| 165 | Olmo 3 7B | 0.0588 | 7B | — | small | ✅ | ❌ |
| 166 | Exaone 4.0 1.2B | 0.0579 | 1.28B | — | tiny | ✅ | ✅ |
| 167 | Granite 4.0 H 1B | 0.0569 | 1.5B | — | tiny | ✅ | ❌ |
| 168 | Phi-4 Mini | 0.0554 | 3.84B | — | tiny | ✅ | ❌ |
| 169 | Qwen3.5 0.8B (non-reasoning) | 0.0514 | 0.873B | — | tiny | ✅ | ❌ |
| 170 | Exaone 4.0 1.2B (non-reasoning) | 0.0506 | 1.28B | — | tiny | ✅ | ❌ |
| 171 | Granite 4.0 Micro | 0.0459 | 3B | — | tiny | ✅ | ❌ |
| 172 | LFM2.5-VL-1.6B | 0.0346 | 1.6B | — | tiny | ✅ | ❌ |
| 173 | Granite 4.0 350M | 0.0325 | 0.35B | — | tiny | ✅ | ❌ |
| 174 | Apertus 8B Instruct | 0.0201 | 8B | — | small | ✅ | ❌ |
| 175 | Granite 4.0 H 350M | 0.0157 | 0.34B | — | tiny | ✅ | ❌ |
| 176 | Molmo 7B-D | 0.0119 | 8.02B | — | small | ✅ | ❌ |
| 177 | K2 Horizon 0.9B | 0.0060 | 0.9B | — | tiny | ✅ | ✅ |
| 178 | Tiny Aya Global | 0.0000 | 3.35B | — | tiny | ✅ | ❌ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 3 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 2 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 1 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 2 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且总参数量 ≤，且至少一项严格更优；缺少参数量数据的模型不在图表和表格中）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.0912，即前沿左端点 Gemma 3 270M）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（对数）

横轴（总参数量）为 **x = A·ln(B·X+C)+D 对数映射**（B = 1；A、D 按端点定出；C = 3.84，r = B/C = 0.260264），用 11 品牌前沿入图模型的总参数量定出；mse = 0.001296，maxdev = 0.0836。

```
x = 0                            # X = 0
x = A·ln(X+C)+D                  # X > 0
```

- **函数端点**：X = 0 → x = 0；前沿最大值 → x = 1；
- 数量级入图模型数：1B–10B: 27，10B–100B: 61，100B–1T: 57，1T–2.8T: 6
- 中位数位置 0.398；左 91 个，右 63 个
- 前沿最大总参数量 2,800.0B → x = 1；高于该值的模型不入图，表格中有。
- 10^x 数量级指示（位置 = x(10^x)）：10^0→ 0.035，10^1→ 0.194，10^2→ 0.500，10^3→ 0.844

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
**模型数（有参数量数据）**: 178（总体帕累托前沿 13 个；图表入图 154 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，等参数点自下而上）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.0912，前沿左端点 Gemma 3 270M 即 (0,0)），能力低于该级的 24 个模型和总参数量高于品牌前沿最大值的模型不出现在图中；横轴为总参数量（线性）。
