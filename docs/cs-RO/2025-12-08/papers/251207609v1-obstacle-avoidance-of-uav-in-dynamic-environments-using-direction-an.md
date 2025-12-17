---
layout: default
title: Obstacle Avoidance of UAV in Dynamic Environments Using Direction and Velocity-Adaptive Artificial Potential Field
---

# Obstacle Avoidance of UAV in Dynamic Environments Using Direction and Velocity-Adaptive Artificial Potential Field

**arXiv**: [2512.07609v1](https://arxiv.org/abs/2512.07609) | [PDF](https://arxiv.org/pdf/2512.07609.pdf)

**作者**: Nikita Vaibhav Pavle, Shrreya Rajneesh, Rakesh Kumar Sahoo, Manoranjan Sinha

---

## 💡 一句话要点

**提出方向与相对速度加权人工势场以解决无人机动态环境避障问题**

**关键词**: `无人机避障` `人工势场` `动态环境` `模型预测控制` `轨迹规划`

## 📋 核心要点

1. 核心问题：传统人工势场存在局部极小点且无法处理移动障碍物运动学。
2. 方法要点：引入有界加权函数动态调整排斥势，结合模型预测控制生成轨迹。
3. 实验或效果：仿真显示方法有效解决局部极小点，提升安全性和路径完整性。

## 📄 摘要（原文）

> The conventional Artificial Potential Field (APF) is fundamentally limited by the local minima issue and its inability to account for the kinematics of moving obstacles. This paper addresses the critical challenge of autonomous collision avoidance for Unmanned Aerial Vehicles (UAVs) operating in dynamic and cluttered airspace by proposing a novel Direction and Relative Velocity Weighted Artificial Potential Field (APF). In this approach, a bounded weighting function, $ω(θ,v_{e})$, is introduced to dynamically scale the repulsive potential based on the direction and velocity of the obstacle relative to the UAV. This robust APF formulation is integrated within a Model Predictive Control (MPC) framework to generate collision-free trajectories while adhering to kinematic constraints. Simulation results demonstrate that the proposed method effectively resolves local minima and significantly enhances safety by enabling smooth, predictive avoidance maneuvers. The system ensures superior path integrity and reliable performance, confirming its viability for autonomous navigation in complex environments.

