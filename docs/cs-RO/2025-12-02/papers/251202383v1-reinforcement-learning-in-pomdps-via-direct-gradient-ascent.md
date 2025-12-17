---
layout: default
title: Reinforcement Learning in POMDP's via Direct Gradient Ascent
---

# Reinforcement Learning in POMDP's via Direct Gradient Ascent

**arXiv**: [2512.02383v1](https://arxiv.org/abs/2512.02383) | [PDF](https://arxiv.org/pdf/2512.02383.pdf)

**作者**: Jonathan Baxter, Peter L. Bartlett

---

## 💡 一句话要点

**提出GPOMDP算法，用于在部分可观测马尔可夫决策过程中直接优化策略性能。**

**关键词**: `强化学习` `部分可观测马尔可夫决策过程` `梯度上升` `策略优化` `平均奖励`

## 📋 核心要点

1. 核心问题：在部分可观测马尔可夫决策过程中直接优化策略性能的梯度方法。
2. 方法要点：引入GPOMDP算法，基于单样本路径估计平均奖励梯度，参数少且无需状态知识。
3. 实验或效果：证明算法收敛性，并展示梯度估计可用于共轭梯度法寻找局部最优。

## 📄 摘要（原文）

> This paper discusses theoretical and experimental aspects of gradient-based approaches to the direct optimization of policy performance in controlled POMDPs. We introduce GPOMDP, a REINFORCE-like algorithm for estimating an approximation to the gradient of the average reward as a function of the parameters of a stochastic policy. The algorithm's chief advantages are that it requires only a single sample path of the underlying Markov chain, it uses only one free parameter $β\in [0,1)$, which has a natural interpretation in terms of bias-variance trade-off, and it requires no knowledge of the underlying state. We prove convergence of GPOMDP and show how the gradient estimates produced by GPOMDP can be used in a conjugate-gradient procedure to find local optima of the average reward.

