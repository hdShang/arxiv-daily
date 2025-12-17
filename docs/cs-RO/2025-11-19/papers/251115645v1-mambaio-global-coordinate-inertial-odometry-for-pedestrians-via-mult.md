---
layout: default
title: MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling
---

# MambaIO: Global-Coordinate Inertial Odometry for Pedestrians via Multi-Scale Frequency-Decoupled Modeling

**arXiv**: [2511.15645v1](https://arxiv.org/abs/2511.15645) | [PDF](https://arxiv.org/pdf/2511.15645.pdf)

**作者**: Shanshan Zhang

---

## 💡 一句话要点

**提出MambaIO通过多尺度频率解耦建模提升行人惯性里程计定位精度**

**关键词**: `惯性里程计` `多尺度建模` `Mamba架构` `频率解耦` `行人定位`

## 📋 核心要点

1. 核心问题：全球坐标系在行人惯性里程计中可能不适用，需重新评估其有效性。
2. 方法要点：使用拉普拉斯金字塔分解IMU测量，Mamba架构处理低频，卷积处理高频。
3. 实验或效果：在多个公共数据集上显著降低定位误差，达到SOTA性能。

## 📄 摘要（原文）

> Inertial Odometry (IO) enables real-time localization using only acceleration and angular velocity measurements from an Inertial Measurement Unit (IMU), making it a promising solution for localization in consumer-grade applications. Traditionally, IMU measurements in IO have been processed under two coordinate system paradigms: the body coordinate frame and the global coordinate frame, with the latter being widely adopted. However, recent studies in drone scenarios have demonstrated that the body frame can significantly improve localization accuracy, prompting a re-evaluation of the suitability of the global frame for pedestrian IO. To address this issue, this paper systematically evaluates the effectiveness of the global coordinate frame in pedestrian IO through theoretical analysis, qualitative inspection, and quantitative experiments. Building upon these findings, we further propose MambaIO, which decomposes IMU measurements into high-frequency and low-frequency components using a Laplacian pyramid. The low-frequency component is processed by a Mamba architecture to extract implicit contextual motion cues, while the high-frequency component is handled by a convolutional structure to capture fine-grained local motion details. Experiments on multiple public datasets show that MambaIO substantially reduces localization error and achieves state-of-the-art (SOTA) performance. To the best of our knowledge, this is the first application of the Mamba architecture to the inertial odometry task.

