---
layout: default
title: Dual-Path Region-Guided Attention Network for Ground Reaction Force and Moment Regression
---

# Dual-Path Region-Guided Attention Network for Ground Reaction Force and Moment Regression

**arXiv**: [2512.05030v1](https://arxiv.org/abs/2512.05030) | [PDF](https://arxiv.org/pdf/2512.05030.pdf)

**作者**: Xuan Li, Samuel Bello

---

## 💡 一句话要点

**提出双路径区域引导注意力网络，用于基于鞋垫的GRF/GRM回归估计**

**关键词**: `地面反作用力估计` `注意力机制` `生物力学建模` `鞋垫传感器` `深度学习回归`

## 📋 核心要点

1. 核心问题：准确估计三维地面反作用力和力矩，对生物力学研究和临床康复评估至关重要
2. 方法要点：集成解剖学启发的空间和时间先验到区域级注意力机制，辅以全传感器场上下文路径
3. 实验或效果：在两个数据集上优于CNN和CNN-LSTM基线，在鞋垫数据集上平均NRMSE为5.78%

## 📄 摘要（原文）

> Accurate estimation of three-dimensional ground reaction forces and moments (GRFs/GRMs) is crucial for both biomechanics research and clinical rehabilitation evaluation. In this study, we focus on insole-based GRF/GRM estimation and further validate our approach on a public walking dataset. We propose a Dual-Path Region-Guided Attention Network that integrates anatomy-inspired spatial priors and temporal priors into a region-level attention mechanism, while a complementary path captures context from the full sensor field. The two paths are trained jointly and their outputs are combined to produce the final GRF/GRM predictions. Conclusions: Our model outperforms strong baseline models, including CNN and CNN-LSTM architectures on two datasets, achieving the lowest six-component average NRMSE of 5.78% on the insole dataset and 1.42% for the vertical ground reaction force on the public dataset. This demonstrates robust performance for ground reaction force and moment estimation.

