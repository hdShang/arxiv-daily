---
layout: default
title: RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning
---

# RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning

**arXiv**: [2512.02729v1](https://arxiv.org/abs/2512.02729) | [PDF](https://arxiv.org/pdf/2512.02729.pdf)

**作者**: Yuhong Zhang, Zihan Gao, Shengpeng Li, Ling-Hao Chen, Kaisheng Liu, Runqing Cheng, Xiao Lin, Junjia Liu, Zhuoheng Li, Jingyi Feng, Ziyan He, Jintian Lin, Zheyan Huang, Zhifang Liu, Haoqian Wang

---

## 💡 一句话要点

**提出RoboWheel数据引擎，从真实人手交互视频生成跨形态机器人学习的训练监督**

**关键词**: `人手交互重建` `跨形态重定向` `仿真数据增强` `机器人学习监督` `多模态数据集`

## 📋 核心要点

1. 核心问题：如何利用人手交互视频为不同形态机器人提供有效监督数据
2. 方法要点：通过高精度重建与强化学习优化，实现物理合理的轨迹重定向与仿真增强
3. 实验或效果：验证数据在主流模型上性能稳定，媲美遥操作，支持大规模数据集构建

## 📄 摘要（原文）

> We introduce Robowheel, a data engine that converts human hand object interaction (HOI) videos into training-ready supervision for cross morphology robotic learning. From monocular RGB or RGB-D inputs, we perform high precision HOI reconstruction and enforce physical plausibility via a reinforcement learning (RL) optimizer that refines hand object relative poses under contact and penetration constraints. The reconstructed, contact rich trajectories are then retargeted to cross-embodiments, robot arms with simple end effectors, dexterous hands, and humanoids, yielding executable actions and rollouts. To scale coverage, we build a simulation-augmented framework on Isaac Sim with diverse domain randomization (embodiments, trajectories, object retrieval, background textures, hand motion mirroring), which enriches the distributions of trajectories and observations while preserving spatial relationships and physical plausibility. The entire data pipeline forms an end to end pipeline from video,reconstruction,retargeting,augmentation data acquisition. We validate the data on mainstream vision language action (VLA) and imitation learning architectures, demonstrating that trajectories produced by our pipeline are as stable as those from teleoperation and yield comparable continual performance gains. To our knowledge, this provides the first quantitative evidence that HOI modalities can serve as effective supervision for robotic learning. Compared with teleoperation, Robowheel is lightweight, a single monocular RGB(D) camera is sufficient to extract a universal, embodiment agnostic motion representation that could be flexibly retargeted across embodiments. We further assemble a large scale multimodal dataset combining multi-camera captures, monocular videos, and public HOI corpora for training and evaluating embodied models.

