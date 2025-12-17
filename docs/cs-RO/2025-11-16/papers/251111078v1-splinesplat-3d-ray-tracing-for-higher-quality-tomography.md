---
layout: default
title: SplineSplat: 3D Ray Tracing for Higher-Quality Tomography
---

# SplineSplat: 3D Ray Tracing for Higher-Quality Tomography

**arXiv**: [2511.11078v1](https://arxiv.org/abs/2511.11078) | [PDF](https://arxiv.org/pdf/2511.11078.pdf)

**作者**: Youssef Haouchat, Sepand Kashani, Aleix Boquet-Pujadas, Philippe Thévenaz, Michael Unser

---

## 💡 一句话要点

**提出基于B样条和神经网络的3D射线追踪方法，以提升断层扫描重建质量**

**关键词**: `3D断层扫描` `B样条表示` `射线追踪算法` `神经网络加速` `体积重建`

## 📋 核心要点

1. 核心问题：传统体素方法在断层扫描中重建质量不足，需高效计算3D投影
2. 方法要点：使用B样条组合表示体积，结合神经网络高效计算基函数贡献
3. 实验或效果：在数据充分条件下，重建质量优于传统方法，无需正则化

## 📄 摘要（原文）

> We propose a method to efficiently compute tomographic projections of a 3D volume represented by a linear combination of shifted B-splines. To do so, we propose a ray-tracing algorithm that computes 3D line integrals with arbitrary projection geometries. One of the components of our algorithm is a neural network that computes the contribution of the basis functions efficiently. In our experiments, we consider well-posed cases where the data are sufficient for accurate reconstruction without the need for regularization. We achieve higher reconstruction quality than traditional voxel-based methods.

