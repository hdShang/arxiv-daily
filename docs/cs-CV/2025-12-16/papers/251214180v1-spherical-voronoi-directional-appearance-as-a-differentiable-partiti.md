---
layout: default
title: Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere
---

# Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14180" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14180v1</a>
  <a href="https://arxiv.org/pdf/2512.14180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14180v1" onclick="toggleFavorite(this, '2512.14180v1', 'Spherical Voronoi: Directional Appearance as a Differentiable Partition of the Sphere')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Francesco Di Sario, Daniel Rebain, Dor Verbin, Marco Grangetto, Andrea Tagliasacchi

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出球面Voronoi方法，用于3D高斯溅射中高效可微的方向外观建模**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `球面Voronoi图` `3D高斯溅射` `新视角合成` `外观建模` `反射探针` `辐射场` `可微渲染`

## 📋 核心要点

1. 球面谐波在辐射场方法中外观建模受限，无法有效处理高频信号和镜面反射。
2. 提出球面Voronoi方法，将方向域划分为可学习区域，实现视角相关效果的参数化。
3. 实验表明，该方法在漫反射和镜面反射建模上均有出色表现，并在合成和真实数据集上达到SOTA。

## 📝 摘要（中文）

辐射场方法（如3D高斯溅射）已成为新视角合成的强大范例，但其外观建模通常依赖于球面谐波（SH），这存在根本性限制。SH难以处理高频信号，表现出吉布斯振铃伪影，并且无法捕捉镜面反射——这是真实感渲染的关键组成部分。虽然球面高斯等替代方案有所改进，但它们增加了显著的优化复杂性。我们提出球面Voronoi（SV）作为3D高斯溅射中外观表示的统一框架。SV将方向域划分为具有平滑边界的可学习区域，为视角相关的效果提供了直观且稳定的参数化。对于漫反射外观，SV实现了具有竞争力的结果，同时保持了比现有替代方案更简单的优化。对于SH失效的反射，我们遵循经典图形学的原则，利用SV作为可学习的反射探针，将反射方向作为输入。这种公式在合成和真实世界数据集上获得了最先进的结果，证明SV为显式3D表示中的外观建模提供了一种原则性、高效且通用的解决方案。

## 🔬 方法详解

**问题定义**：现有辐射场方法，特别是基于3D高斯溅射的方法，在外观建模方面依赖球面谐波(SH)。SH在表示高频信号时存在困难，容易产生Gibbs ringing伪影，并且难以捕捉镜面反射等重要视觉效果。这些限制阻碍了真实感渲染的进一步提升。

**核心思路**：论文的核心思路是使用球面Voronoi (SV) 图来划分方向空间，并为每个Voronoi区域学习一个外观表示。通过这种方式，可以避免SH的局限性，并提供更灵活和高效的外观建模方法。SV图的平滑边界使得优化过程更加稳定。

**技术框架**：该方法将SV图集成到3D高斯溅射框架中。首先，使用SV图将每个高斯分布的方向空间划分为多个区域。然后，为每个区域学习一个颜色值或反射探针。在渲染时，根据视角方向确定所属的Voronoi区域，并使用该区域对应的颜色或反射探针进行着色。对于反射建模，将SV作为可学习的反射探针，输入反射方向，输出颜色。

**关键创新**：该方法的关键创新在于使用球面Voronoi图作为一种可学习的方向空间划分方式，从而克服了球面谐波的局限性。与直接优化球面高斯分布相比，SV图的优化更加稳定和高效。此外，将SV图应用于反射建模，实现了高质量的镜面反射效果。

**关键设计**：SV图的顶点位置是可学习的参数，通过优化这些顶点的位置来调整Voronoi区域的形状和大小。损失函数包括渲染损失和正则化项，用于保证SV图的平滑性和稳定性。对于反射建模，使用一个小型神经网络将反射方向映射到反射探针的颜色值。

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

该方法在合成和真实数据集上均取得了state-of-the-art的结果。在反射建模方面，显著优于基于球面谐波的方法。实验结果表明，该方法能够有效地捕捉高频信号和镜面反射，生成更逼真的图像。具体性能数据在论文中有详细展示，相较于现有方法在PSNR、SSIM等指标上均有显著提升。

## 🎯 应用场景

该研究成果可应用于新视角合成、虚拟现实、增强现实、游戏开发等领域。通过更真实地模拟物体表面的外观，可以提升用户在虚拟环境中的沉浸感和体验。此外，该方法还可以用于材质编辑和反光效果设计，为艺术家和设计师提供更强大的工具。

## 📄 摘要（原文）

> Radiance field methods (e.g. 3D Gaussian Splatting) have emerged as a powerful paradigm for novel view synthesis, yet their appearance modeling often relies on Spherical Harmonics (SH), which impose fundamental limitations. SH struggle with high-frequency signals, exhibit Gibbs ringing artifacts, and fail to capture specular reflections - a key component of realistic rendering. Although alternatives like spherical Gaussians offer improvements, they add significant optimization complexity. We propose Spherical Voronoi (SV) as a unified framework for appearance representation in 3D Gaussian Splatting. SV partitions the directional domain into learnable regions with smooth boundaries, providing an intuitive and stable parameterization for view-dependent effects. For diffuse appearance, SV achieves competitive results while keeping optimization simpler than existing alternatives. For reflections - where SH fail - we leverage SV as learnable reflection probes, taking reflected directions as input following principles from classical graphics. This formulation attains state-of-the-art results on synthetic and real-world datasets, demonstrating that SV offers a principled, efficient, and general solution for appearance modeling in explicit 3D representations.

