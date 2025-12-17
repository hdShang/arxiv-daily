---
layout: default
title: Efficient Collision-Avoidance Constraints for Ellipsoidal Obstacles in Optimal Control: Application to Path-Following MPC and UAVs
---

# Efficient Collision-Avoidance Constraints for Ellipsoidal Obstacles in Optimal Control: Application to Path-Following MPC and UAVs

**arXiv**: [2510.26531v1](https://arxiv.org/abs/2510.26531) | [PDF](https://arxiv.org/pdf/2510.26531.pdf)

**作者**: David Leprich, Mario Rosenfelder, Markus Herrmann-Wicklmayr, Kathrin Flaßkamp, Peter Eberhard, Henrik Ebel

---

## 💡 一句话要点

**提出高效椭球障碍物避碰约束，应用于路径跟踪MPC与无人机。**

**关键词**: `椭球障碍物避碰` `模型预测控制` `最优控制` `无人机导航` `路径跟踪` `硬件实验`

## 📋 核心要点

1. 核心问题：三维椭球障碍物避碰在最优控制中的计算效率与可微性需求。
2. 方法要点：引入计算高效且连续可微的碰撞检测条件与两阶段优化方法。
3. 实验或效果：通过仿真和Crazyflie四旋翼实验验证有效性，首次硬件演示。

## 📄 摘要（原文）

> This article proposes a modular optimal control framework for local
> three-dimensional ellipsoidal obstacle avoidance, exemplarily applied to model
> predictive path-following control. Static as well as moving obstacles are
> considered. Central to the approach is a computationally efficient and
> continuously differentiable condition for detecting collisions with ellipsoidal
> obstacles. A novel two-stage optimization approach mitigates numerical issues
> arising from the structure of the resulting optimal control problem. The
> effectiveness of the approach is demonstrated through simulations and
> real-world experiments with the Crazyflie quadrotor. This represents the first
> hardware demonstration of an MPC controller of this kind for UAVs in a
> three-dimensional task.

