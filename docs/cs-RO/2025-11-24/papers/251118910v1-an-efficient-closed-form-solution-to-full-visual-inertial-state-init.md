---
layout: default
title: An Efficient Closed-Form Solution to Full Visual-Inertial State Initialization
---

# An Efficient Closed-Form Solution to Full Visual-Inertial State Initialization

**arXiv**: [2511.18910v1](https://arxiv.org/abs/2511.18910) | [PDF](https://arxiv.org/pdf/2511.18910.pdf)

**作者**: Samuel Cerezo, Seong Hun Lee, Javier Civera

---

## 💡 一句话要点

**提出闭式视觉-惯性状态初始化方法，避免非线性优化，提高效率与稳定性。**

**关键词**: `视觉-惯性状态初始化` `闭式解` `小旋转近似` `恒定速度假设` `EuRoC数据集` `计算效率`

## 📋 核心要点

1. 核心问题：视觉-惯性状态初始化依赖迭代求解器，计算成本高且不稳定。
2. 方法要点：基于小旋转和恒定速度近似，实现解析解，耦合运动与惯性测量。
3. 实验效果：在EuRoC数据集上，初始化误差降低10-20%，计算成本减少5倍。

## 📄 摘要（原文）

> In this letter, we present a closed-form initialization method that recovers the full visual-inertial state without nonlinear optimization. Unlike previous approaches that rely on iterative solvers, our formulation yields analytical, easy-to-implement, and numerically stable solutions for reliable start-up. Our method builds on small-rotation and constant-velocity approximations, which keep the formulation compact while preserving the essential coupling between motion and inertial measurements. We further propose an observability-driven, two-stage initialization scheme that balances accuracy with initialization latency. Extensive experiments on the EuRoC dataset validate our assumptions: our method achieves 10-20% lower initialization error than optimization-based approaches, while using 4x shorter initialization windows and reducing computational cost by 5x.

