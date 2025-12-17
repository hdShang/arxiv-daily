---
layout: default
title: Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization
---

# Gaussian Entropy Fields: Driving Adaptive Sparsity in 3D Gaussian Optimization

**arXiv**: [2512.04542v1](https://arxiv.org/abs/2512.04542) | [PDF](https://arxiv.org/pdf/2512.04542.pdf)

**作者**: Hong Kuang, Jianchen Liu

---

## 💡 一句话要点

**提出高斯熵场以驱动3D高斯优化中的自适应稀疏性，提升表面重建精度与渲染质量。**

**关键词**: `3D高斯泼溅` `熵驱动优化` `表面重建` `自适应稀疏性` `多尺度几何` `新视角合成`

## 📋 核心要点

1. 核心问题：3D高斯泼溅中表面重建的冗余组件导致几何精度不足，需优化配置熵以增强稀疏性。
2. 方法要点：通过熵最小化、自适应空间正则化和多尺度几何对齐，实现低熵表面建模与高效组件抑制。
3. 实验或效果：在DTU和T&T基准上获得优越几何精度，在Mip-NeRF 360上实现最佳渲染质量指标。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a leading technique for novel view synthesis, demonstrating exceptional rendering efficiency. \replaced[]{Well-reconstructed surfaces can be characterized by low configurational entropy, where dominant primitives clearly define surface geometry while redundant components are suppressed.}{The key insight is that well-reconstructed surfaces naturally exhibit low configurational entropy, where dominant primitives clearly define surface geometry while suppressing redundant components.} Three complementary technical contributions are introduced: (1) entropy-driven surface modeling via entropy minimization for low configurational entropy in primitive distributions; (2) adaptive spatial regularization using the Surface Neighborhood Redundancy Index (SNRI) and image entropy-guided weighting; (3) multi-scale geometric preservation through competitive cross-scale entropy alignment. Extensive experiments demonstrate that GEF achieves competitive geometric precision on DTU and T\&T benchmarks, while delivering superior rendering quality compared to existing methods on Mip-NeRF 360. Notably, superior Chamfer Distance (0.64) on DTU and F1 score (0.44) on T\&T are obtained, alongside the best SSIM (0.855) and LPIPS (0.136) among baselines on Mip-NeRF 360, validating the framework's ability to enhance surface reconstruction accuracy without compromising photometric fidelity.

