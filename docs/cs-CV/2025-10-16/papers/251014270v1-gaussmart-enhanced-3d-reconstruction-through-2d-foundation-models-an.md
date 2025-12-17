---
layout: default
title: GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering
---

# GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and Geometric Filtering

**arXiv**: [2510.14270v1](https://arxiv.org/abs/2510.14270) | [PDF](https://arxiv.org/pdf/2510.14270.pdf)

**作者**: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang

---

## 💡 一句话要点

**提出GauSSmart，通过2D基础模型和几何过滤增强3D高斯溅射重建**

**关键词**: `3D重建` `高斯溅射` `2D基础模型` `几何过滤` `语义特征监督`

## 📋 核心要点

1. 核心问题：高斯溅射在稀疏3D数据区域难以捕捉细节和保持真实感
2. 方法要点：集成2D分割先验和特征嵌入，指导高斯溅射的致密化和细化
3. 实验或效果：在多个数据集上优于现有高斯溅射方法，提升覆盖率和细节保留

## 📄 摘要（原文）

> Scene reconstruction has emerged as a central challenge in computer vision,
> with approaches such as Neural Radiance Fields (NeRF) and Gaussian Splatting
> achieving remarkable progress. While Gaussian Splatting demonstrates strong
> performance on large-scale datasets, it often struggles to capture fine details
> or maintain realism in regions with sparse coverage, largely due to the
> inherent limitations of sparse 3D training data.
>   In this work, we propose GauSSmart, a hybrid method that effectively bridges
> 2D foundational models and 3D Gaussian Splatting reconstruction. Our approach
> integrates established 2D computer vision techniques, including convex
> filtering and semantic feature supervision from foundational models such as
> DINO, to enhance Gaussian-based scene reconstruction. By leveraging 2D
> segmentation priors and high-dimensional feature embeddings, our method guides
> the densification and refinement of Gaussian splats, improving coverage in
> underrepresented areas and preserving intricate structural details.
>   We validate our approach across three datasets, where GauSSmart consistently
> outperforms existing Gaussian Splatting in the majority of evaluated scenes.
> Our results demonstrate the significant potential of hybrid 2D-3D approaches,
> highlighting how the thoughtful combination of 2D foundational models with 3D
> reconstruction pipelines can overcome the limitations inherent in either
> approach alone.

