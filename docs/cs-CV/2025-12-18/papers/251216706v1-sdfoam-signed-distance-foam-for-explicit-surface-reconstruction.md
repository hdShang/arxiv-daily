---
layout: default
title: "SDFoam: Signed-Distance Foam for explicit surface reconstruction"
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

**关键词**: `三维重建` `神经辐射场` `有向距离场` `Voronoi图` `光线追踪`

## 📋 核心要点

1. 现有NeRF和3DGS等方法在精确网格重建方面存在不足，难以生成高质量的几何表面。
2. SDFoam结合显式Voronoi图和隐式SDF，利用SDF的度量一致性来约束Voronoi单元，从而优化表面几何。
3. 实验表明，SDFoam在网格重建精度上显著提升（Chamfer距离），同时保持了良好的光度质量和训练效率。

## 📝 摘要（中文）

神经辐射场（NeRF）通过光线追踪的体渲染在视角合成方面取得了显著进展。基于Splatting的方法，如3D高斯溅射（3DGS），通过栅格化3D图元提供了更快的渲染速度。RadiantFoam（RF）通过使用显式Voronoi图（VD）组织辐射，重新引入了光线追踪，实现了与高斯溅射相当的吞吐量。然而，上述方法在精确网格重建方面仍然存在困难。本文通过联合学习显式VD和隐式有向距离场（SDF）来解决这个问题。场景通过光线追踪进行优化，并由Eikonal目标正则化。SDF引入了度量一致的等值面，进而偏置近表面Voronoi单元面与零水平集对齐。由此产生的模型产生更清晰、视角一致的表面，减少了浮动伪影并改善了拓扑结构，同时保持了光度质量，并保持了与RadiantFoam相当的训练速度。在不同的场景中，我们提出的混合隐式-显式公式，我们称之为SDFoam，在不牺牲效率的情况下，显著提高了网格重建精度（Chamfer距离），并具有可比的外观（PSNR，SSIM）。

## 🔬 方法详解

**问题定义**：现有方法，如NeRF和3DGS，虽然在视角合成方面表现出色，但在精确网格重建方面存在局限性。它们难以生成具有清晰细节和良好拓扑结构的表面，尤其是在复杂场景中，容易出现浮动伪影和不准确的几何形状。RadiantFoam虽然提高了渲染速度，但在网格重建精度上仍有提升空间。

**核心思路**：SDFoam的核心思路是将显式的Voronoi图表示与隐式的有向距离场（SDF）表示相结合。Voronoi图用于快速渲染和光线追踪，而SDF则提供度量一致的几何约束。通过联合优化这两种表示，SDFoam能够生成更精确、更清晰的表面几何。SDF的零水平集定义了目标表面，并引导Voronoi单元面与其对齐，从而提高重建精度。

**技术框架**：SDFoam的整体框架包括以下几个主要模块：1) 初始化：初始化一组3D点，并构建其Voronoi图。2) 光线追踪：使用Voronoi图进行光线追踪，计算每个像素的颜色值。3) SDF预测：使用神经网络预测每个点的SDF值。4) 损失计算：计算光度损失（photometric loss）和Eikonal损失（Eikonal loss），以及SDF对Voronoi单元的约束损失。5) 优化：使用优化算法（如Adam）更新Voronoi图的顶点位置和SDF网络的参数。

**关键创新**：SDFoam的关键创新在于将显式Voronoi图和隐式SDF相结合，形成一种混合的表示方法。这种混合表示既利用了Voronoi图的快速渲染能力，又利用了SDF的度量一致性约束。通过联合优化这两种表示，SDFoam能够生成比单独使用Voronoi图或SDF更精确的表面几何。与现有方法相比，SDFoam在网格重建精度和表面质量方面都有显著提升。

**关键设计**：SDFoam的关键设计包括：1) Eikonal损失：使用Eikonal损失来正则化SDF，使其满足梯度范数为1的约束，从而保证SDF的度量一致性。2) SDF约束损失：设计了一种损失函数，用于约束Voronoi单元面与SDF的零水平集对齐，从而提高重建精度。3) 网络结构：SDF网络可以使用MLP或其他适合SDF预测的网络结构。4) 优化策略：采用合适的优化算法和学习率，以保证训练的稳定性和收敛速度。

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

SDFoam在多个数据集上进行了实验，结果表明，与现有方法相比，SDFoam在网格重建精度（Chamfer距离）上取得了显著提升，同时保持了可比的光度质量（PSNR, SSIM）和训练效率。具体而言，SDFoam在重建精度上优于RadiantFoam和其他基线方法，并且在视觉效果上具有更清晰的表面细节和更少的浮动伪影。

## 🎯 应用场景

SDFoam在三维重建、虚拟现实、增强现实、机器人导航等领域具有广泛的应用前景。它可以用于生成高质量的三维模型，用于游戏开发、电影制作等。在机器人领域，SDFoam可以用于构建机器人的环境地图，帮助机器人进行导航和避障。此外，SDFoam还可以应用于医学图像分析，例如对CT或MRI图像进行三维重建，辅助医生进行诊断。

## 📄 摘要（原文）

> Neural radiance fields (NeRF) have driven impressive progress in view synthesis by using ray-traced volumetric rendering. Splatting-based methods such as 3D Gaussian Splatting (3DGS) provide faster rendering by rasterizing 3D primitives. RadiantFoam (RF) brought ray tracing back, achieving throughput comparable to Gaussian Splatting by organizing radiance with an explicit Voronoi Diagram (VD). Yet, all the mentioned methods still struggle with precise mesh reconstruction. We address this gap by jointly learning an explicit VD with an implicit Signed Distance Field (SDF). The scene is optimized via ray tracing and regularized by an Eikonal objective. The SDF introduces metric-consistent isosurfaces, which, in turn, bias near-surface Voronoi cell faces to align with the zero level set. The resulting model produces crisper, view-consistent surfaces with fewer floaters and improved topology, while preserving photometric quality and maintaining training speed on par with RadiantFoam. Across diverse scenes, our hybrid implicit-explicit formulation, which we name SDFoam, substantially improves mesh reconstruction accuracy (Chamfer distance) with comparable appearance (PSNR, SSIM), without sacrificing efficiency.

