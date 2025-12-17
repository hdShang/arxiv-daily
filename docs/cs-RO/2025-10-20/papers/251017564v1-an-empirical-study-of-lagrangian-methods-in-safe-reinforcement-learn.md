---
layout: default
title: An Empirical Study of Lagrangian Methods in Safe Reinforcement Learning
---

# An Empirical Study of Lagrangian Methods in Safe Reinforcement Learning

**arXiv**: [2510.17564v1](https://arxiv.org/abs/2510.17564) | [PDF](https://arxiv.org/pdf/2510.17564.pdf)

**作者**: Lindsay Spoor, Álvaro Serra-Gómez, Aske Plaat, Thomas Moerland

---

## 💡 一句话要点

**分析拉格朗日乘子在安全强化学习中的最优性与稳定性，提出λ-剖面可视化方法**

**关键词**: `安全强化学习` `拉格朗日方法` `约束优化` `乘子更新` `稳定性分析` `λ-剖面`

## 📋 核心要点

1. 核心问题：拉格朗日乘子λ的选择对安全强化学习性能与约束平衡高度敏感，缺乏通用直觉
2. 方法要点：使用λ-剖面可视化性能与约束权衡，并评估自动乘子更新与PID控制方法
3. 实验或效果：自动更新可恢复或超越最优性能，但存在振荡，需调优以稳定

## 📄 摘要（原文）

> In safety-critical domains such as robotics, navigation and power systems,
> constrained optimization problems arise where maximizing performance must be
> carefully balanced with associated constraints. Safe reinforcement learning
> provides a framework to address these challenges, with Lagrangian methods being
> a popular choice. However, the effectiveness of Lagrangian methods crucially
> depends on the choice of the Lagrange multiplier $\lambda$, which governs the
> trade-off between return and constraint cost. A common approach is to update
> the multiplier automatically during training. Although this is standard in
> practice, there remains limited empirical evidence on the robustness of an
> automated update and its influence on overall performance. Therefore, we
> analyze (i) optimality and (ii) stability of Lagrange multipliers in safe
> reinforcement learning across a range of tasks. We provide $\lambda$-profiles
> that give a complete visualization of the trade-off between return and
> constraint cost of the optimization problem. These profiles show the highly
> sensitive nature of $\lambda$ and moreover confirm the lack of general
> intuition for choosing the optimal value $\lambda^*$. Our findings additionally
> show that automated multiplier updates are able to recover and sometimes even
> exceed the optimal performance found at $\lambda^*$ due to the vast difference
> in their learning trajectories. Furthermore, we show that automated multiplier
> updates exhibit oscillatory behavior during training, which can be mitigated
> through PID-controlled updates. However, this method requires careful tuning to
> achieve consistently better performance across tasks. This highlights the need
> for further research on stabilizing Lagrangian methods in safe reinforcement
> learning. The code used to reproduce our results can be found at
> https://github.com/lindsayspoor/Lagrangian_SafeRL.

