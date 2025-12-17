---
layout: default
title: Perception-aware Exploration for Consumer-grade UAVs
---

# Perception-aware Exploration for Consumer-grade UAVs

**arXiv**: [2511.14393v1](https://arxiv.org/abs/2511.14393) | [PDF](https://arxiv.org/pdf/2511.14393.pdf)

**作者**: Svetlana Seliunina, Daniel Schleich, Sven Behnke

---

## 💡 一句话要点

**提出感知感知探索方法以扩展消费级无人机自主多机探索能力**

**关键词**: `无人机探索` `感知感知规划` `多机系统` `消费级硬件` `轨迹规划` `地图重建`

## 📋 核心要点

1. 核心问题：消费级无人机硬件限制下实现安全自主多机探索与地图重建
2. 方法要点：选择视点对估计深度，规划满足运动约束的轨迹，采用半分布式通信平衡负载
3. 实验或效果：仿真评估多无人机数量，证明安全探索与地图重建能力

## 📄 摘要（原文）

> In our work, we extend the current state-of-the-art approach for autonomous multi-UAV exploration to consumer-level UAVs, such as the DJI Mini 3 Pro. We propose a pipeline that selects viewpoint pairs from which the depth can be estimated and plans the trajectory that satisfies motion constraints necessary for odometry estimation. For the multi-UAV exploration, we propose a semi-distributed communication scheme that distributes the workload in a balanced manner. We evaluate our model performance in simulation for different numbers of UAVs and prove its ability to safely explore the environment and reconstruct the map even with the hardware limitations of consumer-grade UAVs.

