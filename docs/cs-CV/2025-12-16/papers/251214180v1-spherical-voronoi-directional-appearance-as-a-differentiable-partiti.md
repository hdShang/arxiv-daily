---
layout: default
title: "Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere"
---

# Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14180" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14180v1</a>
  <a href="https://arxiv.org/pdf/2512.14180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14180v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14180v1', 'Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出球Voronoi图，用于3D高斯溅射中可微的方向外观建模**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `球Voronoi图` `3D高斯溅射` `新视角合成` `外观建模` `辐射场` `镜面反射` `可微渲染`

## 📋 核心要点

1. 传统球谐函数在辐射场外观建模中存在高频信号处理差、吉布斯振铃等问题，无法有效捕捉镜面反射。
2. 提出球Voronoi图（SV）方法，将方向域划分为可学习区域，实现视角相关效果的直观参数化。
3. SV在漫反射和镜面反射建模上均表现出色，在合成和真实数据集上均达到SOTA，且优化复杂度较低。

## 📝 摘要（中文）

辐射场方法（如3D高斯溅射）已成为新视角合成的强大范例，但其外观建模通常依赖于球谐函数（SH），这存在根本性限制。SH难以处理高频信号，表现出吉布斯振铃伪影，并且无法捕捉镜面反射，而镜面反射是真实感渲染的关键组成部分。虽然像球高斯函数这样的替代方案有所改进，但它们增加了显著的优化复杂性。我们提出了球Voronoi图（SV）作为3D高斯溅射中外观表示的统一框架。SV将方向域划分为具有平滑边界的可学习区域，为视角相关的效果提供了直观且稳定的参数化。对于漫反射外观，SV实现了具有竞争力的结果，同时保持了比现有替代方案更简单的优化。对于SH失效的反射，我们遵循经典图形学的原则，利用SV作为可学习的反射探针，将反射方向作为输入。这种公式在合成和真实世界数据集上获得了最先进的结果，表明SV为显式3D表示中的外观建模提供了一种原则性、高效且通用的解决方案。

## 🔬 方法详解

**问题定义**：现有辐射场方法，特别是基于3D高斯溅射的方法，在外观建模方面依赖于球谐函数（SH）。SH在表示高频信号、捕捉镜面反射等方面存在局限性，导致渲染效果不佳，尤其是在处理具有复杂光照效果的场景时。此外，SH还会引入吉布斯振铃伪影，影响图像质量。替代方案如球高斯函数虽然有所改进，但增加了优化难度。

**核心思路**：论文的核心思路是使用球Voronoi图（SV）来划分方向域，从而实现对视角相关外观的参数化。SV将球体表面分割成多个区域，每个区域对应一个可学习的参数，这些参数可以控制该区域内的外观属性。通过学习这些区域的边界和参数，可以灵活地表示各种外观效果，包括漫反射和镜面反射。

**技术框架**：该方法将SV集成到3D高斯溅射框架中。对于漫反射外观，SV直接用于参数化每个高斯粒子的颜色。对于镜面反射，SV被用作可学习的反射探针，将反射方向作为输入，预测反射颜色。整个框架是可微的，可以使用梯度下降进行端到端优化。主要模块包括：1) SV区域划分模块；2) 颜色/反射预测模块；3) 渲染模块。

**关键创新**：该方法的主要创新在于使用SV作为一种通用的外观表示方法。与传统的SH相比，SV能够更好地处理高频信号和捕捉镜面反射。此外，SV的参数化方式更加直观和稳定，易于优化。将SV作为反射探针也是一个重要的创新，它允许模型学习复杂的反射模式。

**关键设计**：SV的区域数量是一个重要的参数，需要根据场景的复杂程度进行调整。损失函数包括渲染损失（例如L1或L2损失）和正则化项，用于约束SV区域的形状和参数。对于反射探针，可以使用多层感知机（MLP）来预测反射颜色。具体的网络结构和参数需要根据数据集进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180v1/figures/gibbs.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180v1/figures/spatially_varying_light.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180v1/figures/fitting2d.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在合成和真实世界数据集上的实验表明，该方法在外观建模方面优于现有的基于SH的方法。特别是在处理镜面反射时，该方法能够显著提高渲染质量。在某些数据集上，该方法甚至达到了最先进（SOTA）的性能。

## 🎯 应用场景

该研究成果可广泛应用于新视角合成、虚拟现实、增强现实、游戏开发等领域。通过更真实地模拟光照效果，可以提升用户在虚拟环境中的沉浸感和体验。此外，该方法还可以用于三维重建和材质编辑，为数字内容创作提供更强大的工具。

## 📄 摘要（原文）

> Radiance field methods (e.g. 3D Gaussian Splatting) have emerged as a powerful paradigm for novel view synthesis, yet their appearance modeling often relies on Spherical Harmonics (SH), which impose fundamental limitations. SH struggle with high-frequency signals, exhibit Gibbs ringing artifacts, and fail to capture specular reflections - a key component of realistic rendering. Although alternatives like spherical Gaussians offer improvements, they add significant optimization complexity. We propose Spherical Voronoi (SV) as a unified framework for appearance representation in 3D Gaussian Splatting. SV partitions the directional domain into learnable regions with smooth boundaries, providing an intuitive and stable parameterization for view-dependent effects. For diffuse appearance, SV achieves competitive results while keeping optimization simpler than existing alternatives. For reflections - where SH fail - we leverage SV as learnable reflection probes, taking reflected directions as input following principles from classical graphics. This formulation attains state-of-the-art results on synthetic and real-world datasets, demonstrating that SV offers a principled, efficient, and general solution for appearance modeling in explicit 3D representations.

