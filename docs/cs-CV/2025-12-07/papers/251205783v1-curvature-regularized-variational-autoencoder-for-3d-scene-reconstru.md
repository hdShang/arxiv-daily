---
layout: default
title: Curvature-Regularized Variational Autoencoder for 3D Scene Reconstruction from Sparse Depth
---

# Curvature-Regularized Variational Autoencoder for 3D Scene Reconstruction from Sparse Depth

**arXiv**: [2512.05783v1](https://arxiv.org/abs/2512.05783) | [PDF](https://arxiv.org/pdf/2512.05783.pdf)

**作者**: Maryam Yousefi, Soodeh Bakhshandeh

---

## 💡 一句话要点

**提出曲率正则化变分自编码器，从稀疏深度数据重建完整3D场景。**

**关键词**: `3D场景重建` `稀疏深度数据` `曲率正则化` `变分自编码器` `几何深度学习`

## 📋 核心要点

1. 核心问题：深度传感器仅提供5%测量时，稀疏重建导致几何误差，影响自动驾驶和机器人应用。
2. 方法要点：通过离散拉普拉斯算子引入曲率正则化，提供稳定梯度和噪声抑制，训练开销仅15%且无推理成本。
3. 实验或效果：相比标准变分自编码器，重建精度提升18.1%，挑战了多几何约束优于单约束的隐含假设。

## 📄 摘要（原文）

> When depth sensors provide only 5% of needed measurements, reconstructing complete 3D scenes becomes difficult. Autonomous vehicles and robots cannot tolerate the geometric errors that sparse reconstruction introduces. We propose curvature regularization through a discrete Laplacian operator, achieving 18.1% better reconstruction accuracy than standard variational autoencoders. Our contribution challenges an implicit assumption in geometric deep learning: that combining multiple geometric constraints improves performance. A single well-designed regularization term not only matches but exceeds the effectiveness of complex multi-term formulations. The discrete Laplacian offers stable gradients and noise suppression with just 15% training overhead and zero inference cost. Code and models are available at https://github.com/Maryousefi/GeoVAE-3D.

