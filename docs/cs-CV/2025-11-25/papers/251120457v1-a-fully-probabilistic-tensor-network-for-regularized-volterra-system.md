---
layout: default
title: A Fully Probabilistic Tensor Network for Regularized Volterra System Identification
---

# A Fully Probabilistic Tensor Network for Regularized Volterra System Identification

**arXiv**: [2511.20457v1](https://arxiv.org/abs/2511.20457) | [PDF](https://arxiv.org/pdf/2511.20457.pdf)

**作者**: Afra Kilic, Kim Batselier

---

## 💡 一句话要点

**提出贝叶斯张量网络Volterra核机以解决非线性系统建模中的维数灾难问题**

**关键词**: `Volterra系统辨识` `贝叶斯张量网络` `不确定性估计` `稀疏诱导先验` `自动秩确定`

## 📋 核心要点

1. 核心问题：Volterra级数建模中核系数随模型阶数指数增长，导致高复杂度
2. 方法要点：使用规范多分量分解表示Volterra核，将复杂度从O(I^D)降至O(DIR)
3. 实验或效果：实证显示竞争性精度、改进的不确定性量化和降低计算成本

## 📄 摘要（原文）

> Modeling nonlinear systems with Volterra series is challenging because the number of kernel coefficients grows exponentially with the model order. This work introduces Bayesian Tensor Network Volterra kernel machines (BTN-V), extending the Bayesian Tensor Network framework to Volterra system identification. BTN-V represents Volterra kernels using canonical polyadic decomposition, reducing model complexity from O(I^D) to O(DIR). By treating all tensor components and hyperparameters as random variables, BTN-V provides predictive uncertainty estimation at no additional computational cost. Sparsity-inducing hierarchical priors enable automatic rank determination and the learning of fading-memory behavior directly from data, improving interpretability and preventing overfitting. Empirical results demonstrate competitive accuracy, enhanced uncertainty quantification, and reduced computational cost.

