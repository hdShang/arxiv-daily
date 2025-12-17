---
layout: default
title: The Adaptive Vekua Cascade: A Differentiable Spectral-Analytic Solver for Physics-Informed Representation
---

# The Adaptive Vekua Cascade: A Differentiable Spectral-Analytic Solver for Physics-Informed Representation

**arXiv**: [2512.11776v1](https://arxiv.org/abs/2512.11776) | [PDF](https://arxiv.org/pdf/2512.11776.pdf)

**作者**: Vladimer Khasia

---

## 💡 一句话要点

**提出自适应Vekua级联以解决坐标神经网络中的谱偏差和维度灾难问题**

**关键词**: `坐标神经网络` `谱偏差` `维度灾难` `可微分求解器` `物理信息表示` `自适应Vekua级联`

## 📋 核心要点

1. 核心问题：坐标神经网络存在谱偏差和维度灾难，影响高频率学习和参数效率
2. 方法要点：使用深度网络学习物理域变形，结合可微分线性求解器优化谱系数
3. 实验或效果：在物理基准测试中实现高精度，参数减少数量级，收敛速度提升2-3倍

## 📄 摘要（原文）

> Coordinate-based neural networks have emerged as a powerful tool for representing continuous physical fields, yet they face two fundamental pathologies: spectral bias, which hinders the learning of high-frequency dynamics, and the curse of dimensionality, which causes parameter explosion in discrete feature grids. We propose the Adaptive Vekua Cascade (AVC), a hybrid architecture that bridges deep learning and classical approximation theory. AVC decouples manifold learning from function approximation by using a deep network to learn a diffeomorphic warping of the physical domain, projecting complex spatiotemporal dynamics onto a latent manifold where the solution is represented by a basis of generalized analytic functions. Crucially, we replace the standard gradient-descent output layer with a differentiable linear solver, allowing the network to optimally resolve spectral coefficients in a closed form during the forward pass. We evaluate AVC on a suite of five rigorous physics benchmarks, including high-frequency Helmholtz wave propagation, sparse medical reconstruction, and unsteady 3D Navier-Stokes turbulence. Our results demonstrate that AVC achieves state-of-the-art accuracy while reducing parameter counts by orders of magnitude (e.g., 840 parameters vs. 4.2 million for 3D grids) and converging 2-3x faster than implicit neural representations. This work establishes a new paradigm for memory-efficient, spectrally accurate scientific machine learning. The code is available at https://github.com/VladimerKhasia/vecua.

