---
layout: default
title: Graph-based 3D Human Pose Estimation using WiFi Signals
---

# Graph-based 3D Human Pose Estimation using WiFi Signals

**arXiv**: [2511.19105v1](https://arxiv.org/abs/2511.19105) | [PDF](https://arxiv.org/pdf/2511.19105.pdf)

**作者**: Jichao Chen, YangYang Qu, Ruibo Tang, Dirk Slock

---

## 💡 一句话要点

**提出GraphPose-Fi框架，利用WiFi信号和图结构建模骨骼拓扑以改进3D人体姿态估计**

**关键词**: `WiFi姿态估计` `图卷积网络` `3D人体建模` `注意力机制` `信道状态信息`

## 📋 核心要点

1. 现有WiFi方法忽略关节拓扑关系，直接回归坐标导致精度不足
2. 方法结合CNN编码器、注意力模块和图卷积网络，捕捉局部与全局依赖
3. 在MM-Fi数据集上显著优于现有方法，代码已开源

## 📄 摘要（原文）

> WiFi-based human pose estimation (HPE) has attracted increasing attention due to its resilience to occlusion and privacy-preserving compared to camera-based methods. However, existing WiFi-based HPE approaches often employ regression networks that directly map WiFi channel state information (CSI) to 3D joint coordinates, ignoring the inherent topological relationships among human joints. In this paper, we present GraphPose-Fi, a graph-based framework that explicitly models skeletal topology for WiFi-based 3D HPE. Our framework comprises a CNN encoder shared across antennas for subcarrier-time feature extraction, a lightweight attention module that adaptively reweights features over time and across antennas, and a graph-based regression head that combines GCN layers with self-attention to capture local topology and global dependencies. Our proposed method significantly outperforms existing methods on the MM-Fi dataset in various settings. The source code is available at: https://github.com/Cirrick/GraphPose-Fi.

