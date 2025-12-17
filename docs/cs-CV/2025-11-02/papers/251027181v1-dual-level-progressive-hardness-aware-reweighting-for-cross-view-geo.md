---
layout: default
title: Dual-level Progressive Hardness-Aware Reweighting for Cross-View Geo-Localization
---

# Dual-level Progressive Hardness-Aware Reweighting for Cross-View Geo-Localization

**arXiv**: [2510.27181v1](https://arxiv.org/abs/2510.27181) | [PDF](https://arxiv.org/pdf/2510.27181.pdf)

**作者**: Guozheng Zheng, Jian Guan, Mingjie Xie, Xuanjia Zhao, Congyi Fan, Shiheng Zhang, Pengming Feng

---

## 💡 一句话要点

**提出双级渐进硬度感知重加权策略以解决跨视角地理定位中的硬负样本问题**

**关键词**: `跨视角地理定位` `硬负样本挖掘` `损失重加权` `渐进学习` `无人机-卫星图像匹配`

## 📋 核心要点

1. 核心问题：跨视角地理定位因视角差异和硬负样本导致训练不稳定和收敛困难
2. 方法要点：结合样本级难度感知重加权和批级渐进损失加权，动态调整样本权重
3. 实验或效果：在University-1652和SUES-200基准上优于现有方法，提升鲁棒性

## 📄 摘要（原文）

> Cross-view geo-localization (CVGL) between drone and satellite imagery
> remains challenging due to severe viewpoint gaps and the presence of hard
> negatives, which are visually similar but geographically mismatched samples.
> Existing mining or reweighting strategies often use static weighting, which is
> sensitive to distribution shifts and prone to overemphasizing difficult samples
> too early, leading to noisy gradients and unstable convergence. In this paper,
> we present a Dual-level Progressive Hardness-aware Reweighting (DPHR) strategy.
> At the sample level, a Ratio-based Difficulty-Aware (RDA) module evaluates
> relative difficulty and assigns fine-grained weights to negatives. At the batch
> level, a Progressive Adaptive Loss Weighting (PALW) mechanism exploits a
> training-progress signal to attenuate noisy gradients during early optimization
> and progressively enhance hard-negative mining as training matures. Experiments
> on the University-1652 and SUES-200 benchmarks demonstrate the effectiveness
> and robustness of the proposed DPHR, achieving consistent improvements over
> state-of-the-art methods.

