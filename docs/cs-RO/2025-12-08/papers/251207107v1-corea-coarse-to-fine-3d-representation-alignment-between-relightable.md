---
layout: default
title: COREA: Coarse-to-Fine 3D Representation Alignment Between Relightable 3D Gaussians and SDF via Bidirectional 3D-to-3D Supervision
---

# COREA: Coarse-to-Fine 3D Representation Alignment Between Relightable 3D Gaussians and SDF via Bidirectional 3D-to-3D Supervision

**arXiv**: [2512.07107v1](https://arxiv.org/abs/2512.07107) | [PDF](https://arxiv.org/pdf/2512.07107.pdf)

**作者**: Jaeyoon Lee, Hojoon Jung, Sungtae Hwang, Jihyong Oh, Jongwon Choi

---

## 💡 一句话要点

**提出COREA框架，通过双向3D到3D监督实现可重光照3D高斯与SDF的联合学习，以提升几何重建和重光照精度。**

**关键词**: `3D高斯溅射` `符号距离场` `几何重建` `物理渲染` `3D表示对齐` `可重光照模型`

## 📋 核心要点

1. 核心问题：现有3D高斯方法依赖2D渲染学习几何，导致表面粗糙和BRDF-光照分解不可靠。
2. 方法要点：采用粗到细双向3D到3D对齐策略，结合深度、梯度、法线优化几何，并引入密度控制机制。
3. 实验或效果：在标准基准测试中，在新视角合成、网格重建和PBR方面表现优异。

## 📄 摘要（原文）

> We present COREA, the first unified framework that jointly learns relightable 3D Gaussians and a Signed Distance Field (SDF) for accurate geometry reconstruction and faithful relighting. While recent 3D Gaussian Splatting (3DGS) methods have extended toward mesh reconstruction and physically-based rendering (PBR), their geometry is still learned from 2D renderings, leading to coarse surfaces and unreliable BRDF-lighting decomposition. To address these limitations, COREA introduces a coarse-to-fine bidirectional 3D-to-3D alignment strategy that allows geometric signals to be learned directly in 3D space. Within this strategy, depth provides coarse alignment between the two representations, while depth gradients and normals refine fine-scale structure, and the resulting geometry supports stable BRDF-lighting decomposition. A density-control mechanism further stabilizes Gaussian growth, balancing geometric fidelity with memory efficiency. Experiments on standard benchmarks demonstrate that COREA achieves superior performance in novel-view synthesis, mesh reconstruction, and PBR within a unified framework.

