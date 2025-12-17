---
layout: default
title: THE-Pose: Topological Prior with Hybrid Graph Fusion for Estimating Category-Level 6D Object Pose
---

# THE-Pose: Topological Prior with Hybrid Graph Fusion for Estimating Category-Level 6D Object Pose

**arXiv**: [2512.10251v1](https://arxiv.org/abs/2512.10251) | [PDF](https://arxiv.org/pdf/2512.10251.pdf)

**作者**: Eunho Lee, Chaehyeon Song, Seunghoon Jeong, Ayoung Kim

---

## 💡 一句话要点

**提出THE-Pose框架，通过拓扑先验与混合图融合解决类别级6D物体姿态估计中的类内变化与视觉模糊问题。**

**关键词**: `类别级6D姿态估计` `拓扑先验` `混合图融合` `表面嵌入` `点云特征` `视觉模糊性`

## 📋 核心要点

1. 核心问题：现有3D图卷积方法仅关注局部几何与深度信息，对复杂物体和视觉模糊性鲁棒性不足。
2. 方法要点：利用表面嵌入提取拓扑特征，并通过混合图融合模块自适应整合2D图像上下文与3D点云特征。
3. 实验或效果：在REAL275数据集上，相比基线提升35.8%，超越先前最佳方法7.2%，代码已开源。

## 📄 摘要（原文）

> Category-level object pose estimation requires both global context and local structure to ensure robustness against intra-class variations. However, 3D graph convolution (3D-GC) methods only focus on local geometry and depth information, making them vulnerable to complex objects and visual ambiguities. To address this, we present THE-Pose, a novel category-level 6D pose estimation framework that leverages a topological prior via surface embedding and hybrid graph fusion. Specifically, we extract consistent and invariant topological features from the image domain, effectively overcoming the limitations inherent in existing 3D-GC based methods. Our Hybrid Graph Fusion (HGF) module adaptively integrates the topological features with point-cloud features, seamlessly bridging 2D image context and 3D geometric structure. These fused features ensure stability for unseen or complicated objects, even under significant occlusions. Extensive experiments on the REAL275 dataset show that THE-Pose achieves a 35.8% improvement over the 3D-GC baseline (HS-Pose) and surpasses the previous state-of-the-art by 7.2% across all key metrics. The code is avaialbe on https://github.com/EHxxx/THE-Pose

