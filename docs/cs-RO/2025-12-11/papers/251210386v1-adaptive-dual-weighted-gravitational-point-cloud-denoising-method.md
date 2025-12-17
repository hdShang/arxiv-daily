---
layout: default
title: Adaptive Dual-Weighted Gravitational Point Cloud Denoising Method
---

# Adaptive Dual-Weighted Gravitational Point Cloud Denoising Method

**arXiv**: [2512.10386v1](https://arxiv.org/abs/2512.10386) | [PDF](https://arxiv.org/pdf/2512.10386.pdf)

**作者**: Ge Zhang, Chunyang Wang, Bo Xiao, Xuelian Liu, Bin Liu

---

## 💡 一句话要点

**提出自适应双权重引力点云去噪方法，以在多种噪声场景下同时实现高精度、强边缘保持和实时性能。**

**关键词**: `点云去噪` `自适应权重` `引力模型` `八叉树加速` `实时处理` `噪声鲁棒性`

## 📋 核心要点

1. 核心问题：现有方法难以平衡点云去噪精度、边缘细节保留和计算效率，影响自动驾驶等应用。
2. 方法要点：采用八叉树空间分区并行加速，结合自适应体素统计和kNN密度估计快速去除噪声，再通过密度与距离双权重引力评分精细区分噪声点。
3. 实验或效果：在多个数据集上验证，相比现有方法，F1、PSNR和Chamfer Distance指标提升，单帧处理时间减少，展现高精度、鲁棒性和实时性。

## 📄 摘要（原文）

> High-quality point cloud data is a critical foundation for tasks such as autonomous driving and 3D reconstruction. However, LiDAR-based point cloud acquisition is often affected by various disturbances, resulting in a large number of noise points that degrade the accuracy of subsequent point cloud object detection and recognition. Moreover, existing point cloud denoising methods typically sacrifice computational efficiency in pursuit of higher denoising accuracy, or, conversely, improve processing speed at the expense of preserving object boundaries and fine structural details, making it difficult to simultaneously achieve high denoising accuracy, strong edge preservation, and real-time performance. To address these limitations, this paper proposes an adaptive dual-weight gravitational-based point cloud denoising method. First, an octree is employed to perform spatial partitioning of the global point cloud, enabling parallel acceleration. Then, within each leaf node, adaptive voxel-based occupancy statistics and k-nearest neighbor (kNN) density estimation are applied to rapidly remove clearly isolated and low-density noise points, thereby reducing the effective candidate set. Finally, a gravitational scoring function that combines density weights with adaptive distance weights is constructed to finely distinguish noise points from object points. Experiments conducted on the Stanford 3D Scanning Repository, the Canadian Adverse Driving Conditions (CADC) dataset, and in-house FMCW LiDAR point clouds acquired in our laboratory demonstrate that, compared with existing methods, the proposed approach achieves consistent improvements in F1, PSNR, and Chamfer Distance (CD) across various noise conditions while reducing the single-frame processing time, thereby validating its high accuracy, robustness, and real-time performance in multi-noise scenarios.

