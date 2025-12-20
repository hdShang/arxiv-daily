---
layout: default
title: SDFoam: Signed-Distance Foam for explicit surface reconstruction
---

# SDFoam: Signed-Distance Foam for explicit surface reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16706" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16706v1</a>
  <a href="https://arxiv.org/pdf/2512.16706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16706v1', 'SDFoam: Signed-Distance Foam for explicit surface reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonella Rech, Nicola Conci, Nicola Garau

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**SDFoam：结合显式Voronoi图和隐式SDF，实现精确表面重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `三维重建` `有向距离场` `Voronoi图` `光线追踪` `隐式表示` `显式表示`

## 📋 核心要点

1. 现有NeRF和3DGS等方法在精确网格重建方面存在不足，难以生成高质量的几何表面。
2. SDFoam联合学习显式Voronoi图和隐式SDF，利用SDF的度量一致性来约束Voronoi图，从而优化表面几何。
3. 实验表明，SDFoam在保持光度质量和训练速度的同时，显著提高了网格重建精度，减少了伪影。

## 📝 摘要（中文）

神经辐射场（NeRF）通过光线追踪的体渲染在视角合成方面取得了显著进展。基于Splatting的方法，如3D高斯溅射（3DGS），通过栅格化3D图元提供了更快的渲染速度。RadiantFoam（RF）通过使用显式Voronoi图（VD）组织辐射，重新引入了光线追踪，实现了与高斯溅射相当的吞吐量。然而，上述方法在精确网格重建方面仍然存在困难。我们通过联合学习显式VD和隐式有向距离场（SDF）来解决这个问题。场景通过光线追踪进行优化，并由Eikonal目标正则化。SDF引入了度量一致的等值面，进而使近表面Voronoi单元面与零水平集对齐。由此产生的模型产生更清晰、视角一致的表面，减少了漂浮伪影并改善了拓扑结构，同时保持了光度质量，并保持了与RadiantFoam相当的训练速度。在不同的场景中，我们提出的混合隐式-显式公式，我们称之为SDFoam，在不牺牲效率的情况下，显著提高了网格重建精度（Chamfer距离），并具有可比的外观（PSNR，SSIM）。

## 🔬 方法详解

**问题定义**：现有神经渲染方法，如NeRF和3DGS，虽然在视角合成方面表现出色，但在精确网格重建方面存在局限性。这些方法生成的网格表面通常不够清晰，存在漂浮伪影，并且拓扑结构可能不准确。RadiantFoam虽然提高了渲染速度，但仍然难以实现高质量的几何重建。因此，如何提高神经渲染方法在网格重建方面的精度和质量是一个关键问题。

**核心思路**：SDFoam的核心思路是将显式的Voronoi图和隐式的有向距离场（SDF）相结合，利用SDF的度量一致性来约束Voronoi图的形状，从而优化表面的几何结构。Voronoi图用于快速渲染，而SDF则提供精确的表面几何信息，两者相互补充，共同优化。

**技术框架**：SDFoam的整体框架包括以下几个主要步骤：1) 初始化：使用一组3D点初始化场景，并构建Voronoi图。2) 光线追踪：通过光线追踪渲染场景，并计算渲染损失。3) SDF优化：使用Eikonal损失优化SDF，使其与真实表面一致。4) Voronoi图优化：利用SDF的梯度信息，调整Voronoi图的形状，使其与SDF的零水平集对齐。5) 迭代优化：重复步骤2-4，直到收敛。

**关键创新**：SDFoam的关键创新在于将显式的Voronoi图和隐式的SDF相结合，形成一种混合的隐式-显式表示。这种混合表示既能实现快速渲染，又能提供精确的表面几何信息。与传统的NeRF方法相比，SDFoam能够生成更清晰、更准确的网格表面。与RadiantFoam相比，SDFoam通过引入SDF约束，显著提高了网格重建的精度。

**关键设计**：SDFoam的关键设计包括：1) Eikonal损失：使用Eikonal损失来正则化SDF，使其梯度范数接近于1，从而保证SDF的度量一致性。2) Voronoi图对齐：利用SDF的梯度信息，调整Voronoi图的形状，使其与SDF的零水平集对齐。具体来说，通过最小化Voronoi单元面与SDF零水平集之间的距离来实现。3) 光线追踪优化：使用光线追踪渲染场景，并计算渲染损失，从而优化场景的外观。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16706v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SDFoam在网格重建精度方面显著优于现有方法。在多个数据集上，SDFoam的Chamfer距离比RadiantFoam降低了显著比例，同时保持了与RadiantFoam相当的PSNR和SSIM。这意味着SDFoam在提高几何重建精度的同时，没有牺牲外观质量。此外，SDFoam的训练速度与RadiantFoam相当，表明其具有较高的效率。

## 🎯 应用场景

SDFoam在三维重建、虚拟现实、增强现实、机器人导航等领域具有广泛的应用前景。它可以用于生成高质量的三维模型，用于游戏开发、电影制作等。此外，SDFoam还可以用于机器人导航，帮助机器人理解周围环境的几何结构，从而实现更精确的定位和导航。该研究的未来影响在于推动神经渲染技术在实际应用中的发展，使其能够更好地服务于各个领域。

## 📄 摘要（原文）

> Neural radiance fields (NeRF) have driven impressive progress in view synthesis by using ray-traced volumetric rendering. Splatting-based methods such as 3D Gaussian Splatting (3DGS) provide faster rendering by rasterizing 3D primitives. RadiantFoam (RF) brought ray tracing back, achieving throughput comparable to Gaussian Splatting by organizing radiance with an explicit Voronoi Diagram (VD). Yet, all the mentioned methods still struggle with precise mesh reconstruction. We address this gap by jointly learning an explicit VD with an implicit Signed Distance Field (SDF). The scene is optimized via ray tracing and regularized by an Eikonal objective. The SDF introduces metric-consistent isosurfaces, which, in turn, bias near-surface Voronoi cell faces to align with the zero level set. The resulting model produces crisper, view-consistent surfaces with fewer floaters and improved topology, while preserving photometric quality and maintaining training speed on par with RadiantFoam. Across diverse scenes, our hybrid implicit-explicit formulation, which we name SDFoam, substantially improves mesh reconstruction accuracy (Chamfer distance) with comparable appearance (PSNR, SSIM), without sacrificing efficiency.

