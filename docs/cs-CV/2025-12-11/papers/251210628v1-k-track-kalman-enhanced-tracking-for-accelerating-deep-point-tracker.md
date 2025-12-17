---
layout: default
title: K-Track: Kalman-Enhanced Tracking for Accelerating Deep Point Trackers on Edge Devices
---

# K-Track: Kalman-Enhanced Tracking for Accelerating Deep Point Trackers on Edge Devices

**arXiv**: [2512.10628v1](https://arxiv.org/abs/2512.10628) | [PDF](https://arxiv.org/pdf/2512.10628.pdf)

**作者**: Bishoy Galoaa, Pau Closas, Sarah Ostadabbas

---

## 💡 一句话要点

**提出K-Track框架，结合稀疏深度学习与卡尔曼滤波，加速边缘设备上的点跟踪部署。**

**关键词**: `点跟踪` `边缘计算` `卡尔曼滤波` `深度学习加速` `实时视觉系统`

## 📋 核心要点

1. 核心问题：基于深度学习的点跟踪器在边缘设备上因GPU推理成本高而难以实时部署。
2. 方法要点：使用稀疏关键帧深度学习更新与轻量卡尔曼滤波预测，通过贝叶斯不确定性传播保持时序一致性。
3. 实验或效果：在NVIDIA Jetson Nano等平台实现5-10倍加速，保持超过85%的原始跟踪精度。

## 📄 摘要（原文）

> Point tracking in video sequences is a foundational capability for real-world computer vision applications, including robotics, autonomous systems, augmented reality, and video analysis. While recent deep learning-based trackers achieve state-of-the-art accuracy on challenging benchmarks, their reliance on per-frame GPU inference poses a major barrier to deployment on resource-constrained edge devices, where compute, power, and connectivity are limited. We introduce K-Track (Kalman-enhanced Tracking), a general-purpose, tracker-agnostic acceleration framework designed to bridge this deployment gap. K-Track reduces inference cost by combining sparse deep learning keyframe updates with lightweight Kalman filtering for intermediate frame prediction, using principled Bayesian uncertainty propagation to maintain temporal coherence. This hybrid strategy enables 5-10X speedup while retaining over 85% of the original trackers' accuracy. We evaluate K-Track across multiple state-of-the-art point trackers and demonstrate real-time performance on edge platforms such as the NVIDIA Jetson Nano and RTX Titan. By preserving accuracy while dramatically lowering computational requirements, K-Track provides a practical path toward deploying high-quality point tracking in real-world, resource-limited settings, closing the gap between modern tracking algorithms and deployable vision systems.

