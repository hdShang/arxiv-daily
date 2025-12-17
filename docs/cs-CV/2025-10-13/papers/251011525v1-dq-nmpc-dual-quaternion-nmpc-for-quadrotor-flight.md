---
layout: default
title: DQ-NMPC: Dual-Quaternion NMPC for Quadrotor Flight
---

# DQ-NMPC: Dual-Quaternion NMPC for Quadrotor Flight

**arXiv**: [2510.11525v1](https://arxiv.org/abs/2510.11525) | [PDF](https://arxiv.org/pdf/2510.11525.pdf)

**作者**: Luis F. Recalde, Dhruv Agrawal, Jon Arrizabalaga, Guanrui Li

---

## 💡 一句话要点

**提出基于对偶四元数的NMPC框架，以提升四旋翼飞行器在复杂环境中的精确控制性能。**

**关键词**: `四旋翼控制` `非线性模型预测控制` `对偶四元数` `姿态跟踪` `敏捷飞行` `动力学耦合`

## 📋 核心要点

1. 四旋翼飞行器在敏捷飞行中面临欠驱动和动力学耦合的精确控制挑战。
2. 使用对偶四元数流形表示动力学和姿态误差，实现紧凑且全局非奇异的控制公式。
3. 实验显示跟踪误差降低超56%，并在高速高加速场景中优于基线控制器。

## 📄 摘要（原文）

> MAVs have great potential to assist humans in complex tasks, with
> applications ranging from logistics to emergency response. Their agility makes
> them ideal for operations in complex and dynamic environments. However,
> achieving precise control in agile flights remains a significant challenge,
> particularly due to the underactuated nature of quadrotors and the strong
> coupling between their translational and rotational dynamics. In this work, we
> propose a novel NMPC framework based on dual-quaternions (DQ-NMPC) for
> quadrotor flight. By representing both quadrotor dynamics and the pose error
> directly on the dual-quaternion manifold, our approach enables a compact and
> globally non-singular formulation that captures the quadrotor coupled dynamics.
> We validate our approach through simulations and real-world experiments,
> demonstrating better numerical conditioning and significantly improved tracking
> performance, with reductions in position and orientation errors of up to 56.11%
> and 56.77%, compared to a conventional baseline NMPC method. Furthermore, our
> controller successfully handles aggressive trajectories, reaching maximum
> speeds up to 13.66 m/s and accelerations reaching 4.2 g within confined space
> conditions of dimensions 11m x 4.5m x 3.65m under which the baseline controller
> fails.

