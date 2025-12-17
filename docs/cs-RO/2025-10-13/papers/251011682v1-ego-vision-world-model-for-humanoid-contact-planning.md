---
layout: default
title: Ego-Vision World Model for Humanoid Contact Planning
---

# Ego-Vision World Model for Humanoid Contact Planning

**arXiv**: [2510.11682v1](https://arxiv.org/abs/2510.11682) | [PDF](https://arxiv.org/pdf/2510.11682.pdf)

**作者**: Hang Liu, Yuman Gao, Sangli Teng, Yufeng Chi, Yakun Sophia Shao, Zhongyu Li, Maani Ghaffari, Koushil Sreenath

---

## 💡 一句话要点

**提出结合世界模型与模型预测控制的人形机器人接触规划框架，以提升非结构化环境中的自主性。**

**关键词**: `人形机器人` `接触规划` `世界模型` `模型预测控制` `离线强化学习` `自我中心视觉`

## 📋 核心要点

1. 核心问题：传统优化规划器难以处理复杂接触，在线强化学习样本效率低且多任务能力有限。
2. 方法要点：使用离线数据集训练世界模型，在压缩潜在空间预测未来，结合采样MPC和代理价值函数。
3. 实验或效果：在物理人形机器人上实现实时接触规划，支持扰动后支撑、阻挡物体和穿越限高拱门等任务。

## 📄 摘要（原文）

> Enabling humanoid robots to exploit physical contact, rather than simply
> avoid collisions, is crucial for autonomy in unstructured environments.
> Traditional optimization-based planners struggle with contact complexity, while
> on-policy reinforcement learning (RL) is sample-inefficient and has limited
> multi-task ability. We propose a framework combining a learned world model with
> sampling-based Model Predictive Control (MPC), trained on a demonstration-free
> offline dataset to predict future outcomes in a compressed latent space. To
> address sparse contact rewards and sensor noise, the MPC uses a learned
> surrogate value function for dense, robust planning. Our single, scalable model
> supports contact-aware tasks, including wall support after perturbation,
> blocking incoming objects, and traversing height-limited arches, with improved
> data efficiency and multi-task capability over on-policy RL. Deployed on a
> physical humanoid, our system achieves robust, real-time contact planning from
> proprioception and ego-centric depth images. Website:
> https://ego-vcp.github.io/

