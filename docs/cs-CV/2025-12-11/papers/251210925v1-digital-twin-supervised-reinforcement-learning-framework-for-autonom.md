---
layout: default
title: Digital Twin Supervised Reinforcement Learning Framework for Autonomous Underwater Navigation
---

# Digital Twin Supervised Reinforcement Learning Framework for Autonomous Underwater Navigation

**arXiv**: [2512.10925v1](https://arxiv.org/abs/2512.10925) | [PDF](https://arxiv.org/pdf/2512.10925.pdf)

**作者**: Zamirddine Mari, Mohamad Motasem Nawaf, Pierre Drap

---

## 💡 一句话要点

**提出数字孪生监督的强化学习框架，用于水下自主导航以应对无GPS和障碍物挑战。**

**关键词**: `水下自主导航` `强化学习` `数字孪生` `障碍物避让` `仿真迁移`

## 📋 核心要点

1. 核心问题：水下环境因无GPS、能见度低和障碍物存在，自主导航面临重大挑战。
2. 方法要点：基于PPO算法，结合目标导航信息、虚拟占用网格和射线投射的观测空间进行学习。
3. 实验或效果：在模拟和物理BlueROV2上验证，PPO策略在复杂环境中优于DWA，减少碰撞并实现仿真到现实的迁移。

## 📄 摘要（原文）

> Autonomous navigation in underwater environments remains a major challenge due to the absence of GPS, degraded visibility, and the presence of submerged obstacles. This article investigates these issues through the case of the BlueROV2, an open platform widely used for scientific experimentation. We propose a deep reinforcement learning approach based on the Proximal Policy Optimization (PPO) algorithm, using an observation space that combines target-oriented navigation information, a virtual occupancy grid, and ray-casting along the boundaries of the operational area. The learned policy is compared against a reference deterministic kinematic planner, the Dynamic Window Approach (DWA), commonly employed as a robust baseline for obstacle avoidance. The evaluation is conducted in a realistic simulation environment and complemented by validation on a physical BlueROV2 supervised by a 3D digital twin of the test site, helping to reduce risks associated with real-world experimentation. The results show that the PPO policy consistently outperforms DWA in highly cluttered environments, notably thanks to better local adaptation and reduced collisions. Finally, the experiments demonstrate the transferability of the learned behavior from simulation to the real world, confirming the relevance of deep RL for autonomous navigation in underwater robotics.

