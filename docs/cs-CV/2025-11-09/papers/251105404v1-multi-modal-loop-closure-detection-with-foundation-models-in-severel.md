---
layout: default
title: Multi-modal Loop Closure Detection with Foundation Models in Severely Unstructured Environments
---

# Multi-modal Loop Closure Detection with Foundation Models in Severely Unstructured Environments

**arXiv**: [2511.05404v1](https://arxiv.org/abs/2511.05404) | [PDF](https://arxiv.org/pdf/2511.05404.pdf)

**作者**: Laura Alejandra Encinar Gonzalez, John Folkesson, Rudolph Triebel, Riccardo Giubilato

---

## 💡 一句话要点

**提出MPRF多模态管道，利用基础模型在严重非结构化环境中实现鲁棒闭环检测**

**关键词**: `闭环检测` `多模态融合` `基础模型` `姿态估计` `SLAM算法` `行星探索`

## 📋 核心要点

1. 核心问题：在GNSS拒止环境中，视觉和LiDAR闭环检测因纹理弱和稀疏性易失效
2. 方法要点：集成视觉检索与6-DoF姿态估计，使用DINOv2和SALAD进行筛选，SONATA进行几何验证
3. 实验效果：在S3LI数据集上超越现有方法，提升精度和姿态估计鲁棒性

## 📄 摘要（原文）

> Robust loop closure detection is a critical component of Simultaneous
> Localization and Mapping (SLAM) algorithms in GNSS-denied environments, such as
> in the context of planetary exploration. In these settings, visual place
> recognition often fails due to aliasing and weak textures, while LiDAR-based
> methods suffer from sparsity and ambiguity. This paper presents MPRF, a
> multimodal pipeline that leverages transformer-based foundation models for both
> vision and LiDAR modalities to achieve robust loop closure in severely
> unstructured environments. Unlike prior work limited to retrieval, MPRF
> integrates a two-stage visual retrieval strategy with explicit 6-DoF pose
> estimation, combining DINOv2 features with SALAD aggregation for efficient
> candidate screening and SONATA-based LiDAR descriptors for geometric
> verification. Experiments on the S3LI dataset and S3LI Vulcano dataset show
> that MPRF outperforms state-of-the-art retrieval methods in precision while
> enhancing pose estimation robustness in low-texture regions. By providing
> interpretable correspondences suitable for SLAM back-ends, MPRF achieves a
> favorable trade-off between accuracy, efficiency, and reliability,
> demonstrating the potential of foundation models to unify place recognition and
> pose estimation. Code and models will be released at github.com/DLR-RM/MPRF.

