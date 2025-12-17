---
layout: default
title: Flatness-based trajectory planning for 3D overhead cranes with friction compensation and collision avoidance
---

# Flatness-based trajectory planning for 3D overhead cranes with friction compensation and collision avoidance

**arXiv**: [2510.24457v1](https://arxiv.org/abs/2510.24457) | [PDF](https://arxiv.org/pdf/2510.24457.pdf)

**作者**: Jorge Vicente-Martinez, Edgar Ramirez-Laboreo

---

## 💡 一句话要点

**提出基于微分平坦度的轨迹规划方法，用于3D桥式起重机，补偿摩擦并避免碰撞。**

**关键词**: `轨迹规划` `微分平坦度` `摩擦补偿` `碰撞避免` `3D起重机` `仿真验证`

## 📋 核心要点

1. 核心问题：3D桥式起重机轨迹规划需处理非线性摩擦和碰撞，忽略摩擦会导致执行器饱和和碰撞。
2. 方法要点：利用微分平坦度直接纳入物理约束，仅约束最终点载荷摆动，支持激进运动。
3. 实验或效果：仿真比较验证方法，摩擦建模对快速安全轨迹至关重要。

## 📄 摘要（原文）

> This paper presents an optimal trajectory generation method for 3D overhead
> cranes by leveraging differential flatness. This framework enables the direct
> inclusion of complex physical and dynamic constraints, such as nonlinear
> friction and collision avoidance for both payload and rope. Our approach allows
> for aggressive movements by constraining payload swing only at the final point.
> A comparative simulation study validates our approach, demonstrating that
> neglecting dry friction leads to actuator saturation and collisions. The
> results show that friction modeling is a fundamental requirement for fast and
> safe crane trajectories.

