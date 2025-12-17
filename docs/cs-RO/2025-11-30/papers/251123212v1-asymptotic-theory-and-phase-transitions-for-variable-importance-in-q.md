---
layout: default
title: Asymptotic Theory and Phase Transitions for Variable Importance in Quantile Regression Forests
---

# Asymptotic Theory and Phase Transitions for Variable Importance in Quantile Regression Forests

**arXiv**: [2511.23212v1](https://arxiv.org/abs/2511.23212) | [PDF](https://arxiv.org/pdf/2511.23212.pdf)

**作者**: Tomoshige Nakamura, Hiroshi Shiraishi

---

## 💡 一句话要点

**建立分位数回归森林变量重要性的渐近理论，揭示子采样率导致的相变现象**

**关键词**: `分位数回归森林` `变量重要性` `渐近理论` `相变` `偏差校正` `非参数推断`

## 📋 核心要点

1. 核心问题：分位数回归森林中变量重要性统计推断困难，源于损失函数非光滑和偏差-方差权衡复杂
2. 方法要点：利用Knight恒等式处理非可微损失，证明估计量的渐近正态性，并分析子采样率β控制的相变
3. 实验或效果：发现偏差主导机制下标准推断失效，推导渐近偏差显式形式，探讨偏差校正的理论可行性

## 📄 摘要（原文）

> Quantile Regression Forests (QRF) are widely used for non-parametric conditional quantile estimation, yet statistical inference for variable importance measures remains challenging due to the non-smoothness of the loss function and the complex bias-variance trade-off. In this paper, we develop a asymptotic theory for variable importance defined as the difference in pinball loss risks. We first establish the asymptotic normality of the QRF estimator by handling the non-differentiable pinball loss via Knight's identity. Second, we uncover a "phase transition" phenomenon governed by the subsampling rate $β$ (where $s \asymp n^β$). We prove that in the bias-dominated regime ($β\ge 1/2$), which corresponds to large subsample sizes typically favored in practice to maximize predictive accuracy, standard inference breaks down as the estimator converges to a deterministic bias constant rather than a zero-mean normal distribution. Finally, we derive the explicit analytic form of this asymptotic bias and discuss the theoretical feasibility of restoring valid inference via analytic bias correction. Our results highlight a fundamental trade-off between predictive performance and inferential validity, providing a theoretical foundation for understanding the intrinsic limitations of random forest inference in high-dimensional settings.

