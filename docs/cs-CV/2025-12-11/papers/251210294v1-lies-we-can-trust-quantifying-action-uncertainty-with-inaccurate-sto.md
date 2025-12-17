---
layout: default
title: Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups
---

# Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups

**arXiv**: [2512.10294v1](https://arxiv.org/abs/2512.10294) | [PDF](https://arxiv.org/pdf/2512.10294.pdf)

**作者**: Luís Marques, Maani Ghaffari, Dmitry Berenson

---

## 💡 一句话要点

**提出CLAPS算法，通过对称感知的保形预测量化动作不确定性，适用于非欧几里得配置空间。**

**关键词**: `保形预测` `Lie群` `不确定性量化` `非欧几里得配置空间` `安全控制` `动作预测集`

## 📋 核心要点

1. 核心问题：现有不确定性量化方法依赖强假设或未校准估计，不适用于非欧几里得配置空间的安全控制。
2. 方法要点：基于保形预测和Lie群理论，构建动作预测集，提供分布无关的概率保证，无需强动态模型假设。
3. 实验或效果：在模拟JetBot和真实MBot上验证，对称感知的非一致性评分产生更体积高效的预测区域，优于现有方法。

## 📄 摘要（原文）

> We propose Conformal Lie-group Action Prediction Sets (CLAPS), a symmetry-aware conformal prediction-based algorithm that constructs, for a given action, a set guaranteed to contain the resulting system configuration at a user-defined probability. Our assurance holds under both aleatoric and epistemic uncertainty, non-asymptotically, and does not require strong assumptions about the true system dynamics, the uncertainty sources, or the quality of the approximate dynamics model. Typically, uncertainty quantification is tackled by making strong assumptions about the error distribution or magnitude, or by relying on uncalibrated uncertainty estimates - i.e., with no link to frequentist probabilities - which are insufficient for safe control. Recently, conformal prediction has emerged as a statistical framework capable of providing distribution-free probabilistic guarantees on test-time prediction accuracy. While current conformal methods treat robots as Euclidean points, many systems have non-Euclidean configurations, e.g., some mobile robots have SE(2). In this work, we rigorously analyze configuration errors using Lie groups, extending previous Euclidean Space theoretical guarantees to SE(2). Our experiments on a simulated JetBot, and on a real MBot, suggest that by considering the configuration space's structure, our symmetry-informed nonconformity score leads to more volume-efficient prediction regions which represent the underlying uncertainty better than existing approaches.

