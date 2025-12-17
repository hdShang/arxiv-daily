---
layout: default
title: Crossing the Sim2Real Gap Between Simulation and Ground Testing to Space Deployment of Autonomous Free-flyer Control
---

# Crossing the Sim2Real Gap Between Simulation and Ground Testing to Space Deployment of Autonomous Free-flyer Control

**arXiv**: [2512.03736v1](https://arxiv.org/abs/2512.03736) | [PDF](https://arxiv.org/pdf/2512.03736.pdf)

**作者**: Kenneth Stewart, Samantha Chapin, Roxana Leontie, Carl Glen Henshaw

---

## 💡 一句话要点

**提出基于强化学习的仿真到现实训练管道，实现国际空间站上自由飞行机器人的自主控制部署**

**关键词**: `强化学习` `仿真到现实` `自主控制` `自由飞行机器人` `国际空间站` `课程学习`

## 📋 核心要点

1. 核心问题：解决仿真与太空微重力环境间的Sim2Real差距，实现强化学习策略在轨部署
2. 方法要点：使用NVIDIA Omniverse物理模拟器和课程学习训练深度神经网络，替代标准姿态与平移控制
3. 实验或效果：在国际空间站上成功演示Astrobee机器人的自主导航，验证训练管道可行性

## 📄 摘要（原文）

> Reinforcement learning (RL) offers transformative potential for robotic control in space. We present the first on-orbit demonstration of RL-based autonomous control of a free-flying robot, the NASA Astrobee, aboard the International Space Station (ISS). Using NVIDIA's Omniverse physics simulator and curriculum learning, we trained a deep neural network to replace Astrobee's standard attitude and translation control, enabling it to navigate in microgravity. Our results validate a novel training pipeline that bridges the simulation-to-reality (Sim2Real) gap, utilizing a GPU-accelerated, scientific-grade simulation environment for efficient Monte Carlo RL training. This successful deployment demonstrates the feasibility of training RL policies terrestrially and transferring them to space-based applications. This paves the way for future work in In-Space Servicing, Assembly, and Manufacturing (ISAM), enabling rapid on-orbit adaptation to dynamic mission requirements.

