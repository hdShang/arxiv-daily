---
layout: default
title: SSCATeR: Sparse Scatter-Based Convolution Algorithm with Temporal Data Recycling for Real-Time 3D Object Detection in LiDAR Point Clouds
---

# SSCATeR: Sparse Scatter-Based Convolution Algorithm with Temporal Data Recycling for Real-Time 3D Object Detection in LiDAR Point Clouds

**arXiv**: [2512.08557v1](https://arxiv.org/abs/2512.08557) | [PDF](https://arxiv.org/pdf/2512.08557.pdf)

**作者**: Alexander Dow, Manduhu Manduhu, Matheus Santos, Ben Bartlett, Gerard Dooly, James Riordan

---

## 💡 一句话要点

**提出SSCATeR算法，利用时间数据回收和稀疏散射卷积，实现激光雷达点云实时3D目标检测。**

**关键词**: `激光雷达点云` `3D目标检测` `稀疏卷积` `时间数据回收` `实时处理` `散射卷积`

## 📋 核心要点

1. 核心问题：传统稀疏卷积在连续激光雷达扫描中处理未变化区域导致计算冗余，影响实时性。
2. 方法要点：采用滑动时间窗口和短步长，存储卷积结果以重用数据，仅处理点云变化部分，减少卷积操作。
3. 实验或效果：处理时间最多减少6.61倍，特征图与传统方法相同，显著提升计算效率。

## 📄 摘要（原文）

> This work leverages the continuous sweeping motion of LiDAR scanning to concentrate object detection efforts on specific regions that receive a change in point data from one frame to another. We achieve this by using a sliding time window with short strides and consider the temporal dimension by storing convolution results between passes. This allows us to ignore unchanged regions, significantly reducing the number of convolution operations per forward pass without sacrificing accuracy. This data reuse scheme introduces extreme sparsity to detection data. To exploit this sparsity, we extend our previous work on scatter-based convolutions to allow for data reuse, and as such propose Sparse Scatter-Based Convolution Algorithm with Temporal Data Recycling (SSCATeR). This operation treats incoming LiDAR data as a continuous stream and acts only on the changing parts of the point cloud. By doing so, we achieve the same results with as much as a 6.61-fold reduction in processing time. Our test results show that the feature maps output by our method are identical to those produced by traditional sparse convolution techniques, whilst greatly increasing the computational efficiency of the network.

