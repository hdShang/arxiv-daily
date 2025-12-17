---
layout: default
title: M^3Detection: Multi-Frame Multi-Level Feature Fusion for Multi-Modal 3D Object Detection with Camera and 4D Imaging Radar
---

# M^3Detection: Multi-Frame Multi-Level Feature Fusion for Multi-Modal 3D Object Detection with Camera and 4D Imaging Radar

**arXiv**: [2510.27166v1](https://arxiv.org/abs/2510.27166) | [PDF](https://arxiv.org/pdf/2510.27166.pdf)

**作者**: Xiaozhi Li, Huijun Di, Jian Li, Feng Liu, Wei Liang

---

## 💡 一句话要点

**提出M^3Detection框架，通过多帧多级特征融合解决相机与4D成像雷达多模态3D检测问题**

**关键词**: `多模态3D检测` `相机-雷达融合` `多帧特征融合` `时空推理` `4D成像雷达`

## 📋 核心要点

1. 核心问题：单帧输入导致场景信息不完整，图像退化与雷达稀疏性影响检测性能
2. 方法要点：利用跟踪器轨迹引导全局与局部特征聚合，增强多帧时空推理
3. 实验或效果：在VoD和TJ4DRadSet数据集上实现先进3D检测性能

## 📄 摘要（原文）

> Recent advances in 4D imaging radar have enabled robust perception in adverse
> weather, while camera sensors provide dense semantic information. Fusing the
> these complementary modalities has great potential for cost-effective 3D
> perception. However, most existing camera-radar fusion methods are limited to
> single-frame inputs, capturing only a partial view of the scene. The incomplete
> scene information, compounded by image degradation and 4D radar sparsity,
> hinders overall detection performance. In contrast, multi-frame fusion offers
> richer spatiotemporal information but faces two challenges: achieving robust
> and effective object feature fusion across frames and modalities, and
> mitigating the computational cost of redundant feature extraction.
> Consequently, we propose M^3Detection, a unified multi-frame 3D object
> detection framework that performs multi-level feature fusion on multi-modal
> data from camera and 4D imaging radar. Our framework leverages intermediate
> features from the baseline detector and employs the tracker to produce
> reference trajectories, improving computational efficiency and providing richer
> information for second-stage. In the second stage, we design a global-level
> inter-object feature aggregation module guided by radar information to align
> global features across candidate proposals and a local-level inter-grid feature
> aggregation module that expands local features along the reference trajectories
> to enhance fine-grained object representation. The aggregated features are then
> processed by a trajectory-level multi-frame spatiotemporal reasoning module to
> encode cross-frame interactions and enhance temporal representation. Extensive
> experiments on the VoD and TJ4DRadSet datasets demonstrate that M^3Detection
> achieves state-of-the-art 3D detection performance, validating its
> effectiveness in multi-frame detection with camera-4D imaging radar fusion.

