---
layout: default
title: Manifold-Aware Point Cloud Completion via Geodesic-Attentive Hierarchical Feature Learning
---

# Manifold-Aware Point Cloud Completion via Geodesic-Attentive Hierarchical Feature Learning

**arXiv**: [2512.05710v1](https://arxiv.org/abs/2512.05710) | [PDF](https://arxiv.org/pdf/2512.05710.pdf)

**作者**: Jianan Sun, Dongzhihan Wang, Mingyu Fan

---

## 💡 一句话要点

**提出基于测地距离的分层特征学习框架，以解决点云补全中的几何一致性问题。**

**关键词**: `点云补全` `测地距离` `流形感知` `分层特征学习` `几何一致性`

## 📋 核心要点

1. 核心问题：现有方法依赖欧氏距离，忽略点云内在非线性几何结构，导致几何一致性差和语义模糊。
2. 方法要点：引入测地距离近似器和流形感知特征提取器，通过测地距离引导分层特征学习，提升语义连贯性。
3. 实验或效果：在基准数据集上验证，重建质量优于现有方法，增强结构保真度。

## 📄 摘要（原文）

> Point cloud completion seeks to recover geometrically consistent shapes from partial or sparse 3D observations. Although recent methods have achieved reasonable global shape reconstruction, they often rely on Euclidean proximity and overlook the intrinsic nonlinear geometric structure of point clouds, resulting in suboptimal geometric consistency and semantic ambiguity. In this paper, we present a manifold-aware point cloud completion framework that explicitly incorporates nonlinear geometry information throughout the feature learning pipeline. Our approach introduces two key modules: a Geodesic Distance Approximator (GDA), which estimates geodesic distances between points to capture the latent manifold topology, and a Manifold-Aware Feature Extractor (MAFE), which utilizes geodesic-based $k$-NN groupings and a geodesic-relational attention mechanism to guide the hierarchical feature extraction process. By integrating geodesic-aware relational attention, our method promotes semantic coherence and structural fidelity in the reconstructed point clouds. Extensive experiments on benchmark datasets demonstrate that our approach consistently outperforms state-of-the-art methods in reconstruction quality.

