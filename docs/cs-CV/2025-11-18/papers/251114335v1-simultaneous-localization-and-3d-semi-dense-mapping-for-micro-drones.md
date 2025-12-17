---
layout: default
title: Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors
---

# Simultaneous Localization and 3D-Semi Dense Mapping for Micro Drones Using Monocular Camera and Inertial Sensors

**arXiv**: [2511.14335v1](https://arxiv.org/abs/2511.14335) | [PDF](https://arxiv.org/pdf/2511.14335.pdf)

**作者**: Jeryes Danial, Yosi Ben Asher, Itzik Klein

---

## 💡 一句话要点

**提出轻量级单目SLAM系统，结合稀疏姿态估计与稠密边缘重建，解决无人机实时建图与导航问题。**

**关键词**: `单目SLAM` `边缘重建` `惯性融合` `实时建图` `无人机导航`

## 📋 核心要点

1. 核心问题：单目SLAM存在尺度模糊和稀疏方法几何细节不足，学习驱动方法计算量大。
2. 方法要点：融合深度学习深度预测与边缘检测，结合惯性数据通过扩展卡尔曼滤波器优化几何一致性。
3. 实验或效果：在低功耗平台实时运行，实现室内走廊和TUM RGBD数据集上的自主导航与避障。

## 📄 摘要（原文）

> Monocular simultaneous localization and mapping (SLAM) algorithms estimate drone poses and build a 3D map using a single camera. Current algorithms include sparse methods that lack detailed geometry, while learning-driven approaches produce dense maps but are computationally intensive. Monocular SLAM also faces scale ambiguities, which affect its accuracy. To address these challenges, we propose an edge-aware lightweight monocular SLAM system combining sparse keypoint-based pose estimation with dense edge reconstruction. Our method employs deep learning-based depth prediction and edge detection, followed by optimization to refine keypoints and edges for geometric consistency, without relying on global loop closure or heavy neural computations. We fuse inertial data with vision by using an extended Kalman filter to resolve scale ambiguity and improve accuracy. The system operates in real time on low-power platforms, as demonstrated on a DJI Tello drone with a monocular camera and inertial sensors. In addition, we demonstrate robust autonomous navigation and obstacle avoidance in indoor corridors and on the TUM RGBD dataset. Our approach offers an effective, practical solution to real-time mapping and navigation in resource-constrained environments.

