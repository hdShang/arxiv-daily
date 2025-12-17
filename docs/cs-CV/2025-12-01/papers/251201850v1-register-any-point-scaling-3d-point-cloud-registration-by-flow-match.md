---
layout: default
title: Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching
---

# Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching

**arXiv**: [2512.01850v1](https://arxiv.org/abs/2512.01850) | [PDF](https://arxiv.org/pdf/2512.01850.pdf)

**作者**: Yue Pan, Tao Sun, Liyuan Zhu, Lucas Nunes, Iro Armeni, Jens Behley, Cyrill Stachniss

---

## 💡 一句话要点

**提出基于流匹配的点云配准方法，通过条件生成直接对齐多视图点云。**

**关键词**: `点云配准` `流匹配` `条件生成` `多视图对齐` `三维重建` `机器人定位`

## 📋 核心要点

1. 核心问题：点云配准需对齐未定位点云，传统方法依赖对应匹配和优化，难以处理低重叠场景。
2. 方法要点：将配准建模为条件生成，学习点级速度场将噪声点传输到配准场景，轻量特征提取和刚性约束提升效率。
3. 实验或效果：在成对和多视图配准基准上达到先进结果，尤其低重叠时，泛化跨尺度和传感器，支持重定位等下游任务。

## 📄 摘要（原文）

> Point cloud registration aligns multiple unposed point clouds into a common frame, and is a core step for 3D reconstruction and robot localization. In this work, we cast registration as conditional generation: a learned continuous, point-wise velocity field transports noisy points to a registered scene, from which the pose of each view is recovered. Unlike previous methods that conduct correspondence matching to estimate the transformation between a pair of point clouds and then optimize the pairwise transformations to realize multi-view registration, our model directly generates the registered point cloud. With a lightweight local feature extractor and test-time rigidity enforcement, our approach achieves state-of-the-art results on pairwise and multi-view registration benchmarks, particularly with low overlap, and generalizes across scales and sensor modalities. It further supports downstream tasks including relocalization, multi-robot SLAM, and multi-session map merging. Source code available at: https://github.com/PRBonn/RAP.

