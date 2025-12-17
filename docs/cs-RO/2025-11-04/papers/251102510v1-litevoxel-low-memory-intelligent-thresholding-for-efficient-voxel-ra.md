---
layout: default
title: LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization
---

# LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization

**arXiv**: [2511.02510v1](https://arxiv.org/abs/2511.02510) | [PDF](https://arxiv.org/pdf/2511.02510.pdf)

**作者**: Jee Won Lee, Jongseong Brad Choi

---

## 💡 一句话要点

**提出LiteVoxel以解决稀疏体素栅格化中的内存膨胀和低频细节丢失问题**

**关键词**: `稀疏体素栅格化` `内存优化` `自调优训练` `低频感知损失` `深度分位数剪枝` `场景重建`

## 📋 核心要点

1. 稀疏体素栅格化存在内存膨胀、低频内容欠拟合和边界不稳定问题
2. 采用自调优训练管道，包括逆Sobel重加权和深度分位数剪枝逻辑
3. 实验显示内存减少40%-60%，保持PSNR/SSIM和训练时间，提升低频细节

## 📄 摘要（原文）

> Sparse-voxel rasterization is a fast, differentiable alternative for
> optimization-based scene reconstruction, but it tends to underfit low-frequency
> content, depends on brittle pruning heuristics, and can overgrow in ways that
> inflate VRAM. We introduce LiteVoxel, a self-tuning training pipeline that
> makes SV rasterization both steadier and lighter. Our loss is made
> low-frequency aware via an inverse-Sobel reweighting with a mid-training
> gamma-ramp, shifting gradient budget to flat regions only after geometry
> stabilize. Adaptation replaces fixed thresholds with a depth-quantile pruning
> logic on maximum blending weight, stabilized by EMA-hysteresis guards and
> refines structure through ray-footprint-based, priority-driven subdivision
> under an explicit growth budget. Ablations and full-system results across
> Mip-NeRF 360 (6scenes) and Tanks & Temples (3scenes) datasets show mitigation
> of errors in low-frequency regions and boundary instability while keeping
> PSNR/SSIM, training time, and FPS comparable to a strong SVRaster pipeline.
> Crucially, LiteVoxel reduces peak VRAM by ~40%-60% and preserves low-frequency
> detail that prior setups miss, enabling more predictable, memory-efficient
> training without sacrificing perceptual quality.

