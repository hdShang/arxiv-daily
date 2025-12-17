---
layout: default
title: A Learning-based Control Methodology for Transitioning VTOL UAVs
---

# A Learning-based Control Methodology for Transitioning VTOL UAVs

**arXiv**: [2512.03548v1](https://arxiv.org/abs/2512.03548) | [PDF](https://arxiv.org/pdf/2512.03548.pdf)

**作者**: Zexin Lin, Yebin Zhong, Hanwen Wan, Jiu Cheng, Zhenglong Sun, Xiaoqiang Ji

---

## 💡 一句话要点

**提出基于强化学习的耦合过渡控制方法，以解决VTOL无人机过渡过程中的振动问题。**

**关键词**: `VTOL无人机` `过渡控制` `强化学习` `耦合控制` `轨迹跟踪`

## 📋 核心要点

1. 核心问题：VTOL无人机过渡控制因倾斜转子机制导致重心和推力方向变化，现有解耦控制方法引起显著振动。
2. 方法要点：采用强化学习驱动的控制器实现耦合过渡控制，将巡航模式视为悬停的特殊情况。
3. 实验或效果：在仿真和真实环境中验证，实现精确位置和姿态控制，轨迹跟踪优秀且振动减少。

## 📄 摘要（原文）

> Transition control poses a critical challenge in Vertical Take-Off and Landing Unmanned Aerial Vehicle (VTOL UAV) development due to the tilting rotor mechanism, which shifts the center of gravity and thrust direction during transitions. Current control methods' decoupled control of altitude and position leads to significant vibration, and limits interaction consideration and adaptability. In this study, we propose a novel coupled transition control methodology based on reinforcement learning (RL) driven controller. Besides, contrasting to the conventional phase-transition approach, the ST3M method demonstrates a new perspective by treating cruise mode as a special case of hover. We validate the feasibility of applying our method in simulation and real-world environments, demonstrating efficient controller development and migration while accurately controlling UAV position and attitude, exhibiting outstanding trajectory tracking and reduced vibrations during the transition process.

