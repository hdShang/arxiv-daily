---
layout: default
title: rareboost3d: a synthetic lidar dataset with enhanced rare classes
---

# rareboost3d: a synthetic lidar dataset with enhanced rare classes

**arXiv**: [2510.10876v1](https://arxiv.org/abs/2510.10876) | [PDF](https://arxiv.org/pdf/2510.10876.pdf)

**作者**: Shutong Lin, Zhengkang Xiang, Jianzhong Qi, Kourosh Khoshelham

---

## 💡 一句话要点

**提出RareBoost3D合成数据集和CSC损失方法以解决LiDAR点云分割中的长尾问题**

**关键词**: `LiDAR点云分割` `长尾问题` `合成数据集` `跨域对齐` `语义分割`

## 📋 核心要点

1. 核心问题：真实LiDAR数据集存在长尾问题，稀有类别实例不足，影响分割性能。
2. 方法要点：引入合成数据集RareBoost3D，并设计跨域语义对齐CSC损失以对齐特征。
3. 实验或效果：实验表明该方法显著提升LiDAR点云分割模型在真实数据上的性能。

## 📄 摘要（原文）

> Real-world point cloud datasets have made significant contributions to the
> development of LiDAR-based perception technologies, such as object segmentation
> for autonomous driving. However, due to the limited number of instances in some
> rare classes, the long-tail problem remains a major challenge in existing
> datasets. To address this issue, we introduce a novel, synthetic point cloud
> dataset named RareBoost3D, which complements existing real-world datasets by
> providing significantly more instances for object classes that are rare in
> real-world datasets. To effectively leverage both synthetic and real-world
> data, we further propose a cross-domain semantic alignment method named CSC
> loss that aligns feature representations of the same class across different
> domains. Experimental results demonstrate that this alignment significantly
> enhances the performance of LiDAR point cloud segmentation models over
> real-world data.

