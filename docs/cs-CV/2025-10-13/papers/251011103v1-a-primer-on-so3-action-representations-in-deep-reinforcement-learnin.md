---
layout: default
title: A Primer on SO(3) Action Representations in Deep Reinforcement Learning
---

# A Primer on SO(3) Action Representations in Deep Reinforcement Learning

**arXiv**: [2510.11103v1](https://arxiv.org/abs/2510.11103) | [PDF](https://arxiv.org/pdf/2510.11103.pdf)

**作者**: Martin Schuck, Sherif Samy, Angela P. Schoellig

---

## 💡 一句话要点

**评估SO(3)动作表示在深度强化学习中的影响，提供机器人控制指南**

**关键词**: `SO(3)表示` `深度强化学习` `机器人控制` `动作几何` `探索优化` `实验评估`

## 📋 核心要点

1. 机器人控制中SO(3)几何使动作表示非平凡，常见参数化引入约束和失败模式
2. 系统评估Euler角、四元数等表示在PPO、SAC、TD3算法下的探索和稳定性
3. 实验显示局部切向量表示最可靠，量化几何对优化影响并给出实用选择指南

## 📄 摘要（原文）

> Many robotic control tasks require policies to act on orientations, yet the
> geometry of SO(3) makes this nontrivial. Because SO(3) admits no global,
> smooth, minimal parameterization, common representations such as Euler angles,
> quaternions, rotation matrices, and Lie algebra coordinates introduce distinct
> constraints and failure modes. While these trade-offs are well studied for
> supervised learning, their implications for actions in reinforcement learning
> remain unclear. We systematically evaluate SO(3) action representations across
> three standard continuous control algorithms, PPO, SAC, and TD3, under dense
> and sparse rewards. We compare how representations shape exploration, interact
> with entropy regularization, and affect training stability through empirical
> studies and analyze the implications of different projections for obtaining
> valid rotations from Euclidean network outputs. Across a suite of robotics
> benchmarks, we quantify the practical impact of these choices and distill
> simple, implementation-ready guidelines for selecting and using rotation
> actions. Our results highlight that representation-induced geometry strongly
> influences exploration and optimization and show that representing actions as
> tangent vectors in the local frame yields the most reliable results across
> algorithms.

