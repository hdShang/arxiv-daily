---
layout: default
title: Fast Policy Learning for 6-DOF Position Control of Underwater Vehicles
---

# Fast Policy Learning for 6-DOF Position Control of Underwater Vehicles

**arXiv**: [2512.13359v1](https://arxiv.org/abs/2512.13359) | [PDF](https://arxiv.org/pdf/2512.13359.pdf)

**作者**: Sümer Tunçay, Alain Andres, Ignacio Carlucho

---

## 💡 一句话要点

**提出GPU加速强化学习训练管道，实现水下机器人六自由度位置控制**

**关键词**: `水下机器人控制` `强化学习` `GPU加速训练` `仿真到现实迁移` `六自由度位置控制`

## 📋 核心要点

1. 核心问题：传统控制器在未建模动态或环境扰动下性能下降，强化学习训练慢且仿真到现实迁移难。
2. 方法要点：基于JAX和MuJoCo-XLA构建GPU加速训练管道，通过JIT编译大规模并行物理仿真和学习更新。
3. 实验或效果：在真实水下实验中实现稳健六自由度轨迹跟踪和扰动抑制，策略零样本从仿真迁移。

## 📄 摘要（原文）

> Autonomous Underwater Vehicles (AUVs) require reliable six-degree-of-freedom (6-DOF) position control to operate effectively in complex and dynamic marine environments. Traditional controllers are effective under nominal conditions but exhibit degraded performance when faced with unmodeled dynamics or environmental disturbances. Reinforcement learning (RL) provides a powerful alternative but training is typically slow and sim-to-real transfer remains challenging. This work introduces a GPU-accelerated RL training pipeline built in JAX and MuJoCo-XLA (MJX). By jointly JIT-compiling large-scale parallel physics simulation and learning updates, we achieve training times of under two minutes.Through systematic evaluation of multiple RL algorithms, we show robust 6-DOF trajectory tracking and effective disturbance rejection in real underwater experiments, with policies transferred zero-shot from simulation. Our results provide the first explicit real-world demonstration of RL-based AUV position control across all six degrees of freedom.

