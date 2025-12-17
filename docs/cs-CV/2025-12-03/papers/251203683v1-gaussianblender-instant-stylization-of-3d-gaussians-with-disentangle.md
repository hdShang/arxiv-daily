---
layout: default
title: GaussianBlender: Instant Stylization of 3D Gaussians with Disentangled Latent Spaces
---

# GaussianBlender: Instant Stylization of 3D Gaussians with Disentangled Latent Spaces

**arXiv**: [2512.03683v1](https://arxiv.org/abs/2512.03683) | [PDF](https://arxiv.org/pdf/2512.03683.pdf)

**作者**: Melis Ocal, Xiaoyan Xing, Yue Li, Ngo Anh Vien, Sezer Karaoglu, Theo Gevers

---

## 💡 一句话要点

**提出GaussianBlender前馈框架，实现文本驱动的3D高斯体即时风格化，解决现有方法优化耗时和多视角不一致问题。**

**关键词**: `3D风格化` `高斯体表示` `潜在空间解耦` `文本驱动编辑` `前馈框架` `多视角一致性`

## 📋 核心要点

1. 核心问题：现有文本到3D风格化方法依赖2D图像编辑器蒸馏，导致每资产优化耗时且多视角不一致，不适用于大规模生产。
2. 方法要点：从空间分组的3D高斯体学习解耦的几何与外观潜在空间，通过潜在扩散模型进行文本条件编辑，实现前馈即时推理。
3. 实验或效果：评估显示GaussianBlender提供即时、高保真、几何保持、多视角一致的风格化，超越需要每实例测试时优化的方法。

## 📄 摘要（原文）

> 3D stylization is central to game development, virtual reality, and digital arts, where the demand for diverse assets calls for scalable methods that support fast, high-fidelity manipulation. Existing text-to-3D stylization methods typically distill from 2D image editors, requiring time-intensive per-asset optimization and exhibiting multi-view inconsistency due to the limitations of current text-to-image models, which makes them impractical for large-scale production. In this paper, we introduce GaussianBlender, a pioneering feed-forward framework for text-driven 3D stylization that performs edits instantly at inference. Our method learns structured, disentangled latent spaces with controlled information sharing for geometry and appearance from spatially-grouped 3D Gaussians. A latent diffusion model then applies text-conditioned edits on these learned representations. Comprehensive evaluations show that GaussianBlender not only delivers instant, high-fidelity, geometry-preserving, multi-view consistent stylization, but also surpasses methods that require per-instance test-time optimization - unlocking practical, democratized 3D stylization at scale.

