---
layout: default
title: First-order Sobolev Reinforcement Learning
---

# First-order Sobolev Reinforcement Learning

**arXiv**: [2511.19165v1](https://arxiv.org/abs/2511.19165) | [PDF](https://arxiv.org/pdf/2511.19165.pdf)

**作者**: Fabian Schramm, Nicolas Perrin-Gilbert, Justin Carpentier

---

## 💡 一句话要点

**提出一阶Sobolev强化学习，通过一阶贝尔曼一致性改进TD学习，提升收敛与稳定性。**

**关键词**: `强化学习` `时间差分学习` `Sobolev损失` `贝尔曼方程` `策略梯度` `值函数逼近`

## 📋 核心要点

1. 核心问题：传统TD学习仅匹配值函数，忽略导数一致性，可能影响收敛与稳定性。
2. 方法要点：通过可微动态微分贝尔曼备份，使用Sobolev损失函数对齐值与导数。
3. 实验或效果：可集成现有算法如DDPG、SAC，潜在加速收敛并稳定策略梯度。

## 📄 摘要（原文）

> We propose a refinement of temporal-difference learning that enforces first-order Bellman consistency: the learned value function is trained to match not only the Bellman targets in value but also their derivatives with respect to states and actions. By differentiating the Bellman backup through differentiable dynamics, we obtain analytically consistent gradient targets. Incorporating these into the critic objective using a Sobolev-type loss encourages the critic to align with both the value and local geometry of the target function. This first-order TD matching principle can be seamlessly integrated into existing algorithms, such as Q-learning or actor-critic methods (e.g., DDPG, SAC), potentially leading to faster critic convergence and more stable policy gradients without altering their overall structure.

