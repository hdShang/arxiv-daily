---
layout: default
title: Active Tactile Exploration for Rigid Body Pose and Shape Estimation
---

# Active Tactile Exploration for Rigid Body Pose and Shape Estimation

**arXiv**: [2510.13595v1](https://arxiv.org/abs/2510.13595) | [PDF](https://arxiv.org/pdf/2510.13595.pdf)

**作者**: Ethan K. Gordon, Bruke Baraki, Hien Bui, Michael Posa

---

## 💡 一句话要点

**提出主动触觉探索框架，使用触觉数据高效估计刚体姿态与形状**

**关键词**: `触觉感知` `刚体姿态估计` `形状估计` `主动探索` `物理约束优化` `机器人操作`

## 📋 核心要点

1. 核心问题：机器人需处理未知物体，触觉感知稀疏且易致物体移动，需同时估计形状与位置
2. 方法要点：基于物理约束损失函数优化，避免数值刚性，结合期望信息增益最大化探索策略
3. 实验或效果：在模拟和真实机器人实验中，学习凸多面体几何仅需少于10秒数据，显著加速学习

## 📄 摘要（原文）

> General robot manipulation requires the handling of previously unseen
> objects. Learning a physically accurate model at test time can provide
> significant benefits in data efficiency, predictability, and reuse between
> tasks. Tactile sensing can compliment vision with its robustness to occlusion,
> but its temporal sparsity necessitates careful online exploration to maintain
> data efficiency. Direct contact can also cause an unrestrained object to move,
> requiring both shape and location estimation. In this work, we propose a
> learning and exploration framework that uses only tactile data to
> simultaneously determine the shape and location of rigid objects with minimal
> robot motion. We build on recent advances in contact-rich system identification
> to formulate a loss function that penalizes physical constraint violation
> without introducing the numerical stiffness inherent in rigid-body contact.
> Optimizing this loss, we can learn cuboid and convex polyhedral geometries with
> less than 10s of randomly collected data after first contact. Our exploration
> scheme seeks to maximize Expected Information Gain and results in significantly
> faster learning in both simulated and real-robot experiments. More information
> can be found at https://dairlab.github.io/activetactile

