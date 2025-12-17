---
layout: default
title: UniPart: Part-Level 3D Generation with Unified 3D Geom-Seg Latents
---

# UniPart: Part-Level 3D Generation with Unified 3D Geom-Seg Latents

**arXiv**: [2512.09435v1](https://arxiv.org/abs/2512.09435) | [PDF](https://arxiv.org/pdf/2512.09435.pdf)

**作者**: Xufan He, Yushuang Wu, Xiaoyang Guo, Chongjie Ye, Jiaqing Zhou, Tianlei Hu, Xiaoguang Han, Dong Du

---

## 💡 一句话要点

**提出UniPart框架，通过统一几何-分割潜在表示实现图像引导的部分级3D生成**

**关键词**: `部分级3D生成` `几何-分割潜在表示` `潜在扩散框架` `图像引导生成` `双空间生成`

## 📋 核心要点

1. 核心问题：现有部分级3D生成方法依赖隐式分割或外部分割器，控制粒度和数据需求受限
2. 方法要点：引入Geom-Seg VecSet统一表示，结合两阶段潜在扩散框架，在全局和规范空间预测部分潜在
3. 实验或效果：实验显示UniPart在分割可控性和部分级几何质量上优于现有方法

## 📄 摘要（原文）

> Part-level 3D generation is essential for applications requiring decomposable and structured 3D synthesis. However, existing methods either rely on implicit part segmentation with limited granularity control or depend on strong external segmenters trained on large annotated datasets. In this work, we observe that part awareness emerges naturally during whole-object geometry learning and propose Geom-Seg VecSet, a unified geometry-segmentation latent representation that jointly encodes object geometry and part-level structure. Building on this representation, we introduce UniPart, a two-stage latent diffusion framework for image-guided part-level 3D generation. The first stage performs joint geometry generation and latent part segmentation, while the second stage conditions part-level diffusion on both whole-object and part-specific latents. A dual-space generation scheme further enhances geometric fidelity by predicting part latents in both global and canonical spaces. Extensive experiments demonstrate that UniPart achieves superior segmentation controllability and part-level geometric quality compared with existing approaches.

