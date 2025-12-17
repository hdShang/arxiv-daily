---
layout: default
title: Learning-Augmented Ski Rental with Discrete Distributions: A Bayesian Approach
---

# Learning-Augmented Ski Rental with Discrete Distributions: A Bayesian Approach

**arXiv**: [2512.07313v1](https://arxiv.org/abs/2512.07313) | [PDF](https://arxiv.org/pdf/2512.07313.pdf)

**作者**: Bosun Kang, Hyejun Park, Chenglin Fan

---

## 💡 一句话要点

**提出离散贝叶斯框架以解决带预测的滑雪租赁问题，统一传统与学习增强方法。**

**关键词**: `滑雪租赁问题` `贝叶斯决策` `学习增强算法` `不确定性量化` `在线决策` `离散分布`

## 📋 核心要点

1. 核心问题：滑雪租赁问题中如何结合贝叶斯决策与机器学习预测，量化不确定性并整合先验知识。
2. 方法要点：基于离散分布维护精确后验，实现竞争性保证，并在最坏情况与完全信息间平滑插值。
3. 实验或效果：实验显示在多样场景下性能优越，准确先验下接近最优，同时保持鲁棒最坏情况保证。

## 📄 摘要（原文）

> We revisit the classic ski rental problem through the lens of Bayesian decision-making and machine-learned predictions. While traditional algorithms minimize worst-case cost without assumptions, and recent learning-augmented approaches leverage noisy forecasts with robustness guarantees, our work unifies these perspectives. We propose a discrete Bayesian framework that maintains exact posterior distributions over the time horizon, enabling principled uncertainty quantification and seamless incorporation of expert priors. Our algorithm achieves prior-dependent competitive guarantees and gracefully interpolates between worst-case and fully-informed settings. Our extensive experimental evaluation demonstrates superior empirical performance across diverse scenarios, achieving near-optimal results under accurate priors while maintaining robust worst-case guarantees. This framework naturally extends to incorporate multiple predictions, non-uniform priors, and contextual information, highlighting the practical advantages of Bayesian reasoning in online decision problems with imperfect predictions.

