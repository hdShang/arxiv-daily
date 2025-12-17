---
layout: default
title: TimePred: efficient and interpretable offline change point detection for high volume data - with application to industrial process monitoring
---

# TimePred: efficient and interpretable offline change point detection for high volume data - with application to industrial process monitoring

**arXiv**: [2512.01562v1](https://arxiv.org/abs/2512.01562) | [PDF](https://arxiv.org/pdf/2512.01562.pdf)

**作者**: Simon Leszek

---

## 💡 一句话要点

**提出TimePred框架，通过预测时间索引实现高效可解释的高维大数据变点检测**

**关键词**: `变点检测` `高维时间序列` `自监督学习` `可解释人工智能` `工业过程监控` `离线检测`

## 📋 核心要点

1. 核心问题：高维大数据时间序列变点检测在统计一致性、可扩展性和可解释性方面存在挑战
2. 方法要点：将多变量变点检测简化为单变量均值漂移检测，支持XAI方法进行特征级解释
3. 实验或效果：实验显示竞争性检测性能，计算成本降低达两个数量级，工业案例验证准确性提升

## 📄 摘要（原文）

> Change-point detection (CPD) in high-dimensional, large-volume time series is challenging for statistical consistency, scalability, and interpretability. We introduce TimePred, a self-supervised framework that reduces multivariate CPD to univariate mean-shift detection by predicting each sample's normalized time index. This enables efficient offline CPD using existing algorithms and supports the integration of XAI attribution methods for feature-level explanations. Our experiments show competitive CPD performance while reducing computational cost by up to two orders of magnitude. In an industrial manufacturing case study, we demonstrate improved detection accuracy and illustrate the practical value of interpretable change-point insights.

