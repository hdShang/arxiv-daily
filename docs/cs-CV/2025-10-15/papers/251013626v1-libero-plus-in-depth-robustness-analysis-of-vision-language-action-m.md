---
layout: default
title: LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
---

# LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

**arXiv**: [2510.13626v1](https://arxiv.org/abs/2510.13626) | [PDF](https://arxiv.org/pdf/2510.13626.pdf)

**作者**: Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He, Shiduo Zhang, Zhaoye Fei, Jinlan Fu, Jingjing Gong, Xipeng Qiu

---

## 💡 一句话要点

**分析视觉-语言-动作模型在七维扰动下的鲁棒性弱点**

**关键词**: `视觉-语言-动作模型` `鲁棒性分析` `扰动测试` `机器人操作` `模型脆弱性` `基准评估`

## 📋 核心要点

1. 核心问题：VLA模型在基准测试中高成功率可能掩盖鲁棒性不足。
2. 方法要点：引入七维扰动进行系统性脆弱性分析。
3. 实验效果：模型性能在扰动下大幅下降，且常忽略语言指令。

## 📄 摘要（原文）

> Visual-Language-Action (VLA) models report impressive success rates on
> robotic manipulation benchmarks, yet these results may mask fundamental
> weaknesses in robustness. We perform a systematic vulnerability analysis by
> introducing controlled perturbations across seven dimensions: objects layout,
> camera viewpoints, robot initial states, language instructions, light
> conditions, background textures and sensor noise. We comprehensively analyzed
> multiple state-of-the-art models and revealed consistent brittleness beneath
> apparent competence. Our analysis exposes critical weaknesses: models exhibit
> extreme sensitivity to perturbation factors, including camera viewpoints and
> robot initial states, with performance dropping from 95% to below 30% under
> modest perturbations. Surprisingly, models are largely insensitive to language
> variations, with further experiments revealing that models tend to ignore
> language instructions completely. Our findings challenge the assumption that
> high benchmark scores equate to true competency and highlight the need for
> evaluation practices that assess reliability under realistic variation.

