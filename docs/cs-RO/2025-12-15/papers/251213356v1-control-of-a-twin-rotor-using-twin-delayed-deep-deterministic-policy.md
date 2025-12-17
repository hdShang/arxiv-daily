---
layout: default
title: Control of a Twin Rotor using Twin Delayed Deep Deterministic Policy Gradient (TD3)
---

# Control of a Twin Rotor using Twin Delayed Deep Deterministic Policy Gradient (TD3)

**arXiv**: [2512.13356v1](https://arxiv.org/abs/2512.13356) | [PDF](https://arxiv.org/pdf/2512.13356.pdf)

**作者**: Zeyad Gamal, Youssef Mahran, Ayman El-Badawy

---

## 💡 一句话要点

**提出基于TD3的强化学习框架以控制双旋翼系统，实现稳定与轨迹跟踪。**

**关键词**: `强化学习控制` `双旋翼系统` `TD3算法` `轨迹跟踪` `抗干扰控制`

## 📋 核心要点

1. 核心问题：双旋翼系统动态复杂非线性，传统控制算法难以有效控制。
2. 方法要点：采用TD3算法训练强化学习代理，无需系统模型，适用于连续状态动作空间。
3. 实验或效果：仿真验证有效性，对比PID控制器测试抗风扰，实验室实验确认实际应用。

## 📄 摘要（原文）

> This paper proposes a reinforcement learning (RL) framework for controlling and stabilizing the Twin Rotor Aerodynamic System (TRAS) at specific pitch and azimuth angles and tracking a given trajectory. The complex dynamics and non-linear characteristics of the TRAS make it challenging to control using traditional control algorithms. However, recent developments in RL have attracted interest due to their potential applications in the control of multirotors. The Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm was used in this paper to train the RL agent. This algorithm is used for environments with continuous state and action spaces, similar to the TRAS, as it does not require a model of the system. The simulation results illustrated the effectiveness of the RL control method. Next, external disturbances in the form of wind disturbances were used to test the controller's effectiveness compared to conventional PID controllers. Lastly, experiments on a laboratory setup were carried out to confirm the controller's effectiveness in real-world applications.

