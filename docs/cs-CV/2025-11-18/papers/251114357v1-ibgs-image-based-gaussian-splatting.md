---
layout: default
title: IBGS: Image-Based Gaussian Splatting
---

# IBGS: Image-Based Gaussian Splatting

**arXiv**: [2511.14357v1](https://arxiv.org/abs/2511.14357) | [PDF](https://arxiv.org/pdf/2511.14357.pdf)

**作者**: Hoang Chuong Nguyen, Wei Mao, Jose M. Alvarez, Miaomiao Liu

---

## 💡 一句话要点

**提出图像基高斯泼溅以提升新视角合成质量，无需增加存储开销**

**关键词**: `新视角合成` `高斯泼溅` `图像基渲染` `视角依赖效果` `残差学习`

## 📋 核心要点

1. 核心问题：3D高斯泼溅难以捕捉空间变化颜色和视角依赖效果，现有方法存储开销大或处理复杂场景差
2. 方法要点：结合标准渲染基色与从邻近图像学习的残差，实现高频细节和准确视角依赖渲染
3. 实验或效果：在标准基准测试中渲染质量显著优于先前高斯泼溅方法，存储占用不变

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently emerged as a fast, high-quality method for novel view synthesis (NVS). However, its use of low-degree spherical harmonics limits its ability to capture spatially varying color and view-dependent effects such as specular highlights. Existing works augment Gaussians with either a global texture map, which struggles with complex scenes, or per-Gaussian texture maps, which introduces high storage overhead. We propose Image-Based Gaussian Splatting, an efficient alternative that leverages high-resolution source images for fine details and view-specific color modeling. Specifically, we model each pixel color as a combination of a base color from standard 3DGS rendering and a learned residual inferred from neighboring training images. This promotes accurate surface alignment and enables rendering images of high-frequency details and accurate view-dependent effects. Experiments on standard NVS benchmarks show that our method significantly outperforms prior Gaussian Splatting approaches in rendering quality, without increasing the storage footprint.

