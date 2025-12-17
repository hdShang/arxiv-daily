---
layout: default
title: Estimation of Stochastic Optimal Transport Maps
---

# Estimation of Stochastic Optimal Transport Maps

**arXiv**: [2512.09499v1](https://arxiv.org/abs/2512.09499) | [PDF](https://arxiv.org/pdf/2512.09499.pdf)

**作者**: Sloan Nietert, Ziv Goldfeld

---

## 💡 一句话要点

**提出随机最优传输映射估计框架，以处理现实应用中确定性映射失效的场景。**

**关键词**: `随机最优传输` `映射估计` `有限样本风险` `对抗性鲁棒性` `概率分布变换`

## 📋 核心要点

1. 核心问题：现有最优传输映射理论依赖严格假设，在现实问题中常失效，需处理随机映射。
2. 方法要点：引入新度量评估随机映射传输质量，开发高效估计器，具有近最优有限样本风险界。
3. 实验或效果：实验验证理论，在现有理论失效场景中展示实用性，支持对抗性样本污染。

## 📄 摘要（原文）

> The optimal transport (OT) map is a geometry-driven transformation between high-dimensional probability distributions which underpins a wide range of tasks in statistics, applied probability, and machine learning. However, existing statistical theory for OT map estimation is quite restricted, hinging on Brenier's theorem (quadratic cost, absolutely continuous source) to guarantee existence and uniqueness of a deterministic OT map, on which various additional regularity assumptions are imposed to obtain quantitative error bounds. In many real-world problems these conditions fail or cannot be certified, in which case optimal transportation is possible only via stochastic maps that can split mass. To broaden the scope of map estimation theory to such settings, this work introduces a novel metric for evaluating the transportation quality of stochastic maps. Under this metric, we develop computationally efficient map estimators with near-optimal finite-sample risk bounds, subject to easy-to-verify minimal assumptions. Our analysis further accommodates common forms of adversarial sample contamination, yielding estimators with robust estimation guarantees. Empirical experiments are provided which validate our theory and demonstrate the utility of the proposed framework in settings where existing theory fails. These contributions constitute the first general-purpose theory for map estimation, compatible with a wide spectrum of real-world applications where optimal transport may be intrinsically stochastic.

