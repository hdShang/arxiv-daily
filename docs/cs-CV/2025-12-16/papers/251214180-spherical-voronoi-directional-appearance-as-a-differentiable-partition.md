---
layout: default
title: Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere
---

# Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14180" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14180</a>
  <a href="https://arxiv.org/pdf/2512.14180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14180" onclick="toggleFavorite(this, '2512.14180', 'Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出球Voronoi图，用于3D高斯溅射中可微的方向外观建模**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `球Voronoi图` `3D高斯溅射` `新视角合成` `外观建模` `反射建模`

## 📋 核心要点

1. 传统球谐函数在辐射场外观建模中存在高频信号处理差、吉布斯振铃等问题，无法有效捕捉镜面反射。
2. 提出球Voronoi图（SV）方法，将方向域划分为可学习区域，实现对视角相关效果的直观参数化。
3. 实验表明，SV在漫反射和镜面反射建模上均表现出色，尤其在反射建模上达到SOTA效果。

## 📝 摘要（中文）

辐射场方法（如3D高斯溅射）已成为新视角合成的强大范例，但其外观建模通常依赖于球谐函数（SH），这存在根本性限制。SH难以处理高频信号，表现出吉布斯振铃伪影，并且无法捕捉镜面反射——这是真实感渲染的关键组成部分。虽然像球高斯函数这样的替代方案有所改进，但它们增加了显著的优化复杂性。我们提出了球Voronoi图（SV）作为3D高斯溅射中外观表示的统一框架。SV将方向域划分为具有平滑边界的可学习区域，为视角相关的效果提供了直观且稳定的参数化。对于漫反射外观，SV实现了具有竞争力的结果，同时保持了比现有替代方案更简单的优化。对于SH失效的反射，我们遵循经典图形学的原则，利用SV作为可学习的反射探针，将反射方向作为输入。这种公式在合成和真实世界数据集上获得了最先进的结果，表明SV为显式3D表示中的外观建模提供了一种原则性、高效且通用的解决方案。

## 🔬 方法详解

**问题定义**：现有基于辐射场的方法，特别是3D高斯溅射，在外观建模方面依赖于球谐函数（SH）。SH在表示高频信号时存在困难，会导致吉布斯振铃伪影，并且难以捕捉镜面反射等重要视觉效果。这些限制阻碍了真实感渲染的进一步提升。

**核心思路**：论文的核心思路是使用球Voronoi图（SV）来划分方向域，从而实现对外观的灵活且可学习的表示。SV将球面划分为多个区域，每个区域对应一种外观属性。通过学习这些区域的边界和相关属性，可以更好地捕捉复杂的光照效果，包括漫反射和镜面反射。这种方法旨在克服SH的局限性，同时保持较低的优化复杂度。

**技术框架**：该方法将SV集成到3D高斯溅射框架中。对于每个高斯分布，使用SV来表示其方向外观。具体流程包括：1）使用SV划分球面；2）学习SV区域的边界；3）学习每个区域对应的外观属性（例如，颜色、反射率）；4）在渲染过程中，根据视角方向确定对应SV区域，并使用该区域的外观属性进行着色。对于反射建模，将SV作为可学习的反射探针，输入反射方向，输出反射颜色。

**关键创新**：该方法最重要的创新点在于使用SV作为一种可学习的球面划分方法，用于表示方向外观。与传统的SH相比，SV能够更灵活地捕捉高频信号和复杂的光照效果。此外，将SV应用于反射建模，将其作为可学习的反射探针，是一种新颖且有效的方法。

**关键设计**：SV的区域数量是一个关键参数，需要根据场景的复杂程度进行调整。论文中使用了可微分的Voronoi图生成算法，使得SV的边界可以进行优化。损失函数包括渲染损失和正则化项，用于保证SV区域的平滑性和稳定性。对于反射建模，使用了额外的损失函数来鼓励SV学习真实的反射效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180/figures/gibbs.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180/figures/spatially_varying_light.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14180/figures/fitting2d.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在合成和真实世界数据集上的实验表明，该方法在外观建模方面取得了最先进的结果。特别是在反射建模方面，该方法显著优于基于球谐函数的方法。实验数据表明，该方法能够有效地捕捉镜面反射等复杂光照效果，从而生成更逼真的图像。

## 🎯 应用场景

该研究成果可广泛应用于新视角合成、虚拟现实、增强现实、游戏开发等领域。通过更真实地模拟光照效果，可以提升虚拟场景的沉浸感和真实感。此外，该方法还可以应用于材质编辑、光照设计等任务，为艺术家和设计师提供更强大的工具。

## 📄 摘要（原文）

> Radiance field methods (e.g. 3D Gaussian Splatting) have emerged as a powerful paradigm for novel view synthesis, yet their appearance modeling often relies on Spherical Harmonics (SH), which impose fundamental limitations. SH struggle with high-frequency signals, exhibit Gibbs ringing artifacts, and fail to capture specular reflections - a key component of realistic rendering. Although alternatives like spherical Gaussians offer improvements, they add significant optimization complexity. We propose Spherical Voronoi (SV) as a unified framework for appearance representation in 3D Gaussian Splatting. SV partitions the directional domain into learnable regions with smooth boundaries, providing an intuitive and stable parameterization for view-dependent effects. For diffuse appearance, SV achieves competitive results while keeping optimization simpler than existing alternatives. For reflections - where SH fail - we leverage SV as learnable reflection probes, taking reflected directions as input following principles from classical graphics. This formulation attains state-of-the-art results on synthetic and real-world datasets, demonstrating that SV offers a principled, efficient, and general solution for appearance modeling in explicit 3D representations.

