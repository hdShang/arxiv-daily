---
layout: default
title: Safe Bayesian optimization across noise models via scenario programming
---

# Safe Bayesian optimization across noise models via scenario programming

**arXiv**: [2512.11580v1](https://arxiv.org/abs/2512.11580) | [PDF](https://arxiv.org/pdf/2512.11580.pdf)

**作者**: Abdullah Tokmak, Thomas B. Schön, Dominik Baumann

---

## 💡 一句话要点

**提出基于场景编程的安全贝叶斯优化方法，以处理多种噪声模型**

**关键词**: `安全贝叶斯优化` `高斯过程` `场景编程` `噪声模型` `控制器调优`

## 📋 核心要点

1. 核心问题：现有安全贝叶斯优化算法假设同方差次高斯噪声，不适用于异方差重尾分布等实际场景。
2. 方法要点：通过场景方法提供测量噪声的高概率界，并集成到置信区间中，确保算法安全性和最优性。
3. 实验或效果：在合成示例和Franka Emika机械臂控制器调优仿真中部署验证。

## 📄 摘要（原文）

> Safe Bayesian optimization (BO) with Gaussian processes is an effective tool for tuning control policies in safety-critical real-world systems, specifically due to its sample efficiency and safety guarantees. However, most safe BO algorithms assume homoscedastic sub-Gaussian measurement noise, an assumption that does not hold in many relevant applications. In this article, we propose a straightforward yet rigorous approach for safe BO across noise models, including homoscedastic sub-Gaussian and heteroscedastic heavy-tailed distributions. We provide a high-probability bound on the measurement noise via the scenario approach, integrate these bounds into high probability confidence intervals, and prove safety and optimality for our proposed safe BO algorithm. We deploy our algorithm in synthetic examples and in tuning a controller for the Franka Emika manipulator in simulation.

