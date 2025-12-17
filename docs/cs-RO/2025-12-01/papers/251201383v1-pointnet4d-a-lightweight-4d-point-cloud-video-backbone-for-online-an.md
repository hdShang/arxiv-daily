---
layout: default
title: PointNet4D: A Lightweight 4D Point Cloud Video Backbone for Online and Offline Perception in Robotic Applications
---

# PointNet4D: A Lightweight 4D Point Cloud Video Backbone for Online and Offline Perception in Robotic Applications

**arXiv**: [2512.01383v1](https://arxiv.org/abs/2512.01383) | [PDF](https://arxiv.org/pdf/2512.01383.pdf)

**作者**: Yunze Liu, Zifan Wang, Peiran Wu, Jiayang Ao

---

## 💡 一句话要点

**提出PointNet4D轻量4D点云视频骨干网络，用于机器人应用中的在线与离线感知。**

**关键词**: `4D点云视频` `轻量骨干网络` `在线感知` `离线感知` `机器人应用` `时间融合`

## 📋 核心要点

1. 核心问题：现有4D骨干网络依赖计算密集的时空卷积和Transformer，不适合实时机器人应用。
2. 方法要点：采用混合Mamba-Transformer时间融合块，结合高效状态空间建模和双向建模能力。
3. 实验或效果：在7个数据集9个任务上评估，并构建机器人应用系统，在基准测试中取得显著提升。

## 📄 摘要（原文）

> Understanding dynamic 4D environments-3D space evolving over time-is critical for robotic and interactive systems. These applications demand systems that can process streaming point cloud video in real-time, often under resource constraints, while also benefiting from past and present observations when available. However, current 4D backbone networks rely heavily on spatiotemporal convolutions and Transformers, which are often computationally intensive and poorly suited to real-time applications. We propose PointNet4D, a lightweight 4D backbone optimized for both online and offline settings. At its core is a Hybrid Mamba-Transformer temporal fusion block, which integrates the efficient state-space modeling of Mamba and the bidirectional modeling power of Transformers. This enables PointNet4D to handle variable-length online sequences efficiently across different deployment scenarios. To enhance temporal understanding, we introduce 4DMAP, a frame-wise masked auto-regressive pretraining strategy that captures motion cues across frames. Our extensive evaluations across 9 tasks on 7 datasets, demonstrating consistent improvements across diverse domains. We further demonstrate PointNet4D's utility by building two robotic application systems: 4D Diffusion Policy and 4D Imitation Learning, achieving substantial gains on the RoboTwin and HandoverSim benchmarks.

