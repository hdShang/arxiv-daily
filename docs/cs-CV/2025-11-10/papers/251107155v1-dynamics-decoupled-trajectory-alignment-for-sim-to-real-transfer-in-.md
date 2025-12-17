---
layout: default
title: Dynamics-Decoupled Trajectory Alignment for Sim-to-Real Transfer in Reinforcement Learning for Autonomous Driving
---

# Dynamics-Decoupled Trajectory Alignment for Sim-to-Real Transfer in Reinforcement Learning for Autonomous Driving

**arXiv**: [2511.07155v1](https://arxiv.org/abs/2511.07155) | [PDF](https://arxiv.org/pdf/2511.07155.pdf)

**作者**: Thomas Steinecker, Alexander Bienemann, Denis Trescher, Thorsten Luettel, Mirko Maehlisch

---

## 💡 一句话要点

**提出动态解耦轨迹对齐框架，实现强化学习在自动驾驶中的零样本仿真到现实迁移**

**关键词**: `仿真到现实迁移` `强化学习` `自动驾驶` `轨迹对齐` `动态解耦` `零样本学习`

## 📋 核心要点

1. 核心问题：仿真与现实间车辆动态不匹配，阻碍强化学习代理直接部署
2. 方法要点：通过时空对齐策略，将运动规划与控制解耦，使用蒸馏轨迹预测和Stanley控制器
3. 实验或效果：在真实车辆上验证，实现零样本迁移，提升鲁棒性

## 📄 摘要（原文）

> Reinforcement learning (RL) has shown promise in robotics, but deploying RL
> on real vehicles remains challenging due to the complexity of vehicle dynamics
> and the mismatch between simulation and reality. Factors such as tire
> characteristics, road surface conditions, aerodynamic disturbances, and vehicle
> load make it infeasible to model real-world dynamics accurately, which hinders
> direct transfer of RL agents trained in simulation. In this paper, we present a
> framework that decouples motion planning from vehicle control through a spatial
> and temporal alignment strategy between a virtual vehicle and the real system.
> An RL agent is first trained in simulation using a kinematic bicycle model to
> output continuous control actions. Its behavior is then distilled into a
> trajectory-predicting agent that generates finite-horizon ego-vehicle
> trajectories, enabling synchronization between virtual and real vehicles. At
> deployment, a Stanley controller governs lateral dynamics, while longitudinal
> alignment is maintained through adaptive update mechanisms that compensate for
> deviations between virtual and real trajectories. We validate our approach on a
> real vehicle and demonstrate that the proposed alignment strategy enables
> robust zero-shot transfer of RL-based motion planning from simulation to
> reality, successfully decoupling high-level trajectory generation from
> low-level vehicle control.

