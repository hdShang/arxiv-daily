---
layout: default
title: Solving the Right Problem with Multi-Robot Formations
---

# Solving the Right Problem with Multi-Robot Formations

**arXiv**: [2510.25422v1](https://arxiv.org/abs/2510.25422) | [PDF](https://arxiv.org/pdf/2510.25422.pdf)

**作者**: Chaz Cornwall, Jeremy P. Bos

---

## 💡 一句话要点

**提出多机器人编队规划器以减少编队与成本函数之间的不匹配**

**关键词**: `多机器人编队` `编队控制` `成本函数优化` `非合作控制` `代理成本函数` `军事应用`

## 📋 核心要点

1. 核心问题：静态编队形状与原始成本函数最小化存在差异，导致性能下降。
2. 方法要点：采用两步优化，通过加权代理成本函数估计并最小化非线性成本。
3. 实验或效果：模拟显示单成本降低超75%，多成本同时降低20-40%。

## 📄 摘要（原文）

> Formation control simplifies minimizing multi-robot cost functions by
> encoding a cost function as a shape the robots maintain. However, by reducing
> complex cost functions to formations, discrepancies arise between maintaining
> the shape and minimizing the original cost function. For example, a Diamond or
> Box formation shape is often used for protecting all members of the formation.
> When more information about the surrounding environment becomes available, a
> static shape often no longer minimizes the original protection cost. We propose
> a formation planner to reduce mismatch between a formation and the cost
> function while still leveraging efficient formation controllers. Our formation
> planner is a two-step optimization problem that identifies desired relative
> robot positions. We first solve a constrained problem to estimate non-linear
> and non-differentiable costs with a weighted sum of surrogate cost functions.
> We theoretically analyze this problem and identify situations where weights do
> not need to be updated. The weighted, surrogate cost function is then minimized
> using relative positions between robots. The desired relative positions are
> realized using a non-cooperative formation controller derived from Lyapunov's
> direct approach. We then demonstrate the efficacy of this approach for
> military-like costs such as protection and obstacle avoidance. In simulations,
> we show a formation planner can reduce a single cost by over 75%. When
> minimizing a variety of cost functions simultaneously, using a formation
> planner with adaptive weights can reduce the cost by 20-40%. Formation planning
> provides better performance by minimizing a surrogate cost function that
> closely approximates the original cost function instead of relying on a shape
> abstraction.

