---
layout: default
title: Multi-directional Safe Rectangle Corridor-Based MPC for Nonholonomic Robots Navigation in Cluttered Environment
---

# Multi-directional Safe Rectangle Corridor-Based MPC for Nonholonomic Robots Navigation in Cluttered Environment

**arXiv**: [2512.13215v1](https://arxiv.org/abs/2512.13215) | [PDF](https://arxiv.org/pdf/2512.13215.pdf)

**作者**: Yinsong Qu, Yunxiang Li, Shanlin Zhong

---

## 💡 一句话要点

**提出基于多向安全矩形走廊的改进序列模型预测控制框架，以解决非完整机器人在杂乱环境中的导航问题。**

**关键词**: `非完整机器人导航` `模型预测控制` `安全走廊` `障碍物避让` `实时计算` `杂乱环境`

## 📋 核心要点

1. 核心问题：非完整机器人动力学、静态/动态障碍物交互及非凸约束空间导致导航困难。
2. 方法要点：采用多向安全矩形走廊算法编码自由空间，结合序列MPC框架实现障碍物避让。
3. 实验或效果：实验显示平均走廊面积增加41.05%，生成延迟3毫秒，提升实时性能。

## 📄 摘要（原文）

> Autonomous Mobile Robots (AMRs) have become indispensable in industrial applications due to their operational flexibility and efficiency. Navigation serves as a crucial technical foundation for accomplishing complex tasks. However, navigating AMRs in dense, cluttered, and semi-structured environments remains challenging, primarily due to nonholonomic vehicle dynamics, interactions with mixed static/dynamic obstacles, and the non-convex constrained nature of such operational spaces. To solve these problems, this paper proposes an Improved Sequential Model Predictive Control (ISMPC) navigation framework that systematically reformulates navigation tasks as sequential switched optimal control problems. The framework addresses the aforementioned challenges through two key innovations: 1) Implementation of a Multi-Directional Safety Rectangular Corridor (MDSRC) algorithm, which encodes the free space through rectangular convex regions to avoid collision with static obstacles, eliminating redundant computational burdens and accelerating solver convergence; 2) A sequential MPC navigation framework that integrates corridor constraints with barrier function constraints is proposed to achieve static and dynamic obstacle avoidance. The ISMPC navigation framework enables direct velocity generation for AMRs, simplifying traditional navigation algorithm architectures. Comparative experiments demonstrate the framework's superiority in free-space utilization ( an increase of 41.05$\%$ in the average corridor area) while maintaining real-time computational performance (average corridors generation latency of 3 ms).

