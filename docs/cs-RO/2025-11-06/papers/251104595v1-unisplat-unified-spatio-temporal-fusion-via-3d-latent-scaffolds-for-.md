---
layout: default
title: UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction
---

# UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

**arXiv**: [2511.04595v1](https://arxiv.org/abs/2511.04595) | [PDF](https://arxiv.org/pdf/2511.04595.pdf)

**作者**: Chen Shi, Shaoshuai Shi, Xiaoyang Lyu, Chunyang Liu, Kehua Sheng, Bo Zhang, Li Jiang

---

## 💡 一句话要点

**提出UniSplat框架，通过3D潜在支架实现动态驾驶场景重建，解决稀疏非重叠视图和复杂动态问题。**

**关键词**: `3D重建` `动态场景建模` `潜在表示` `高斯生成` `自动驾驶视觉`

## 📋 核心要点

1. 核心问题：稀疏非重叠相机视图和复杂场景动态导致3D重建困难。
2. 方法要点：构建3D潜在支架，统一融合时空信息，使用双分支解码器生成动态高斯。
3. 实验或效果：在真实数据集上实现最先进的新视图合成，提供高质量渲染。

## 📄 摘要（原文）

> Feed-forward 3D reconstruction for autonomous driving has advanced rapidly,
> yet existing methods struggle with the joint challenges of sparse,
> non-overlapping camera views and complex scene dynamics. We present UniSplat, a
> general feed-forward framework that learns robust dynamic scene reconstruction
> through unified latent spatio-temporal fusion. UniSplat constructs a 3D latent
> scaffold, a structured representation that captures geometric and semantic
> scene context by leveraging pretrained foundation models. To effectively
> integrate information across spatial views and temporal frames, we introduce an
> efficient fusion mechanism that operates directly within the 3D scaffold,
> enabling consistent spatio-temporal alignment. To ensure complete and detailed
> reconstructions, we design a dual-branch decoder that generates dynamic-aware
> Gaussians from the fused scaffold by combining point-anchored refinement with
> voxel-based generation, and maintain a persistent memory of static Gaussians to
> enable streaming scene completion beyond current camera coverage. Extensive
> experiments on real-world datasets demonstrate that UniSplat achieves
> state-of-the-art performance in novel view synthesis, while providing robust
> and high-quality renderings even for viewpoints outside the original camera
> coverage.

