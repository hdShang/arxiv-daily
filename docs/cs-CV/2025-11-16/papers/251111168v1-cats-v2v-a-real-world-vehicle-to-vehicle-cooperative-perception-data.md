---
layout: default
title: CATS-V2V: A Real-World Vehicle-to-Vehicle Cooperative Perception Dataset with Complex Adverse Traffic Scenarios
---

# CATS-V2V: A Real-World Vehicle-to-Vehicle Cooperative Perception Dataset with Complex Adverse Traffic Scenarios

**arXiv**: [2511.11168v1](https://arxiv.org/abs/2511.11168) | [PDF](https://arxiv.org/pdf/2511.11168.pdf)

**作者**: Hangyu Li, Bofeng Cao, Zhaohui Liang, Wuzhen Li, Juyoung Oh, Yuxuan Chen, Shixiao Liang, Hang Zhou, Chengyuan Ma, Jiaxi Liu, Zheng Li, Peng Zhang, KeKe Long, Maolin Liu, Jackson Jiang, Chunlei Yu, Shengxiang Liu, Hongkai Yu, Xiaopeng Li

---

## 💡 一句话要点

**提出CATS-V2V数据集以解决复杂不利交通场景下车对车协同感知的数据缺乏问题**

**关键词**: `车对车协同感知` `复杂不利交通场景` `LiDAR点云` `多视图相机图像` `4D BEV表示` `目标时间对齐`

## 📋 核心要点

1. 核心问题：现有数据集多关注普通交通场景，限制协同感知在复杂不利条件下的应用
2. 方法要点：通过两辆硬件时间同步车辆收集数据，覆盖多种天气和光照条件
3. 实验或效果：提供大规模LiDAR点云、相机图像和RTK-GNSS/IMU记录，支持4D BEV表示构建

## 📄 摘要（原文）

> Vehicle-to-Vehicle (V2V) cooperative perception has great potential to enhance autonomous driving performance by overcoming perception limitations in complex adverse traffic scenarios (CATS). Meanwhile, data serves as the fundamental infrastructure for modern autonomous driving AI. However, due to stringent data collection requirements, existing datasets focus primarily on ordinary traffic scenarios, constraining the benefits of cooperative perception. To address this challenge, we introduce CATS-V2V, the first-of-its-kind real-world dataset for V2V cooperative perception under complex adverse traffic scenarios. The dataset was collected by two hardware time-synchronized vehicles, covering 10 weather and lighting conditions across 10 diverse locations. The 100-clip dataset includes 60K frames of 10 Hz LiDAR point clouds and 1.26M multi-view 30 Hz camera images, along with 750K anonymized yet high-precision RTK-fixed GNSS and IMU records. Correspondingly, we provide time-consistent 3D bounding box annotations for objects, as well as static scenes to construct a 4D BEV representation. On this basis, we propose a target-based temporal alignment method, ensuring that all objects are precisely aligned across all sensor modalities. We hope that CATS-V2V, the largest-scale, most supportive, and highest-quality dataset of its kind to date, will benefit the autonomous driving community in related tasks.

