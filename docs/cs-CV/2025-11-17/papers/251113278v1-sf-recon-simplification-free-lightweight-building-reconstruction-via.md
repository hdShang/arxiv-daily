---
layout: default
title: SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting
---

# SF-Recon: Simplification-Free Lightweight Building Reconstruction via 3D Gaussian Splatting

**arXiv**: [2511.13278v1](https://arxiv.org/abs/2511.13278) | [PDF](https://arxiv.org/pdf/2511.13278.pdf)

**作者**: Zihan Li, Tengfei Wang, Wentian Gan, Hao Zhan, Xin Wang, Zongqian Zhan

---

## 💡 一句话要点

**提出SF-Recon方法，从多视角图像直接重建轻量建筑表面，避免后处理简化**

**关键词**: `建筑重建` `3D高斯溅射` `多视角图像` `轻量网格` `结构优化` `Delaunay三角化`

## 📋 核心要点

1. 核心问题：传统多视角几何流程依赖密集重建和网格简化，导致繁琐和质量敏感
2. 方法要点：使用3D高斯溅射和法向梯度优化，选择结构对齐的高斯基元并修剪非结构伪影
3. 实验或效果：在SF数据集上验证，重建模型面数和顶点显著减少，保持计算效率

## 📄 摘要（原文）

> Lightweight building surface models are crucial for digital city, navigation, and fast geospatial analytics, yet conventional multi-view geometry pipelines remain cumbersome and quality-sensitive due to their reliance on dense reconstruction, meshing, and subsequent simplification. This work presents SF-Recon, a method that directly reconstructs lightweight building surfaces from multi-view images without post-hoc mesh simplification. We first train an initial 3D Gaussian Splatting (3DGS) field to obtain a view-consistent representation. Building structure is then distilled by a normal-gradient-guided Gaussian optimization that selects primitives aligned with roof and wall boundaries, followed by multi-view edge-consistency pruning to enhance structural sharpness and suppress non-structural artifacts without external supervision. Finally, a multi-view depth-constrained Delaunay triangulation converts the structured Gaussian field into a lightweight, structurally faithful building mesh. Based on a proposed SF dataset, the experimental results demonstrate that our SF-Recon can directly reconstruct lightweight building models from multi-view imagery, achieving substantially fewer faces and vertices while maintaining computational efficiency. Website:https://lzh282140127-cell.github.io/SF-Recon-project/

