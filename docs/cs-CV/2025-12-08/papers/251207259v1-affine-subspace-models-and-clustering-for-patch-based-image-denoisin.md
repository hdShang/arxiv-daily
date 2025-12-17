---
layout: default
title: Affine Subspace Models and Clustering for Patch-Based Image Denoising
---

# Affine Subspace Models and Clustering for Patch-Based Image Denoising

**arXiv**: [2512.07259v1](https://arxiv.org/abs/2512.07259) | [PDF](https://arxiv.org/pdf/2512.07259.pdf)

**作者**: Tharindu Wickremasinghe, Marco F. Duarte

---

## 💡 一句话要点

**提出仿射子空间模型与聚类方法以改进基于图像块的去噪性能**

**关键词**: `图像去噪` `仿射子空间` `块聚类` `最小二乘投影` `非局部均值`

## 📋 核心要点

1. 核心问题：线性子空间模型不匹配图像块的非负特性，导致聚类效果不佳
2. 方法要点：使用仿射子空间模型更好地拟合图像块向量空间的几何结构
3. 实验或效果：通过最小二乘投影实现去噪，实验显示聚类和去噪性能提升

## 📄 摘要（原文）

> Image tile-based approaches are popular in many image processing applications such as denoising (e.g., non-local means). A key step in their use is grouping the images into clusters, which usually proceeds iteratively splitting the images into clusters and fitting a model for the images in each cluster. Linear subspaces have emerged as a suitable model for tile clusters; however, they are not well matched to images patches given that images are non-negative and thus not distributed around the origin in the tile vector space. We study the use of affine subspace models for the clusters to better match the geometric structure of the image tile vector space. We also present a simple denoising algorithm that relies on the affine subspace clustering model using least squares projection. We review several algorithmic approaches to solve the affine subspace clustering problem and show experimental results that highlight the performance improvements in clustering and denoising.

