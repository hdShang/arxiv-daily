---
layout: default
title: "MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction"
---

# MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24096" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24096v2</a>
  <a href="https://arxiv.org/pdf/2506.24096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24096v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24096v2', 'MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antoine Guédon, Diego Gomez, Nissim Maruani, Bingchen Gong, George Drettakis, Maks Ovsjanikov

**分类**: cs.CV

**发布日期**: 2025-06-30 (更新: 2025-10-29)

**备注**: 10 pages. A presentation video of our approach is available at https://youtu.be/_SGNhhNz0fE

---

## 💡 一句话要点

**提出MILo框架以解决高质量3D表面重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯点云` `3D重建` `表面提取` `可微分方法` `几何表示` `虚拟现实` `物理模拟`

## 📋 核心要点

1. 现有方法在从图像重建3D表面时，通常需要耗时的后处理，导致细节损失和网格过于密集。
2. MILo框架通过可微分提取网格，直接从3D高斯参数构建网格，解决了体积与表面表示之间的转换问题。
3. 实验表明，MILo能够以更少的网格顶点重建完整场景，质量达到最先进水平，适用于物理模拟和动画等应用。

## 📝 摘要（中文）

尽管最近的高斯点云技术使得从图像快速重建高质量3D场景成为可能，但提取准确的表面网格仍然是一个挑战。现有方法通常通过耗时的后处理步骤提取表面，导致细节损失或生成数百万顶点的密集网格。MILo框架通过可微分地从3D高斯中提取网格，弥补了体积表示与表面表示之间的差距。该方法引入了双向一致性框架、适应性网格提取过程以及计算有符号距离的新方法，能够以更少的网格顶点重建完整场景，且具备良好的下游应用潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决从图像重建高质量3D表面网格的挑战，现有方法在提取过程中往往需要耗时的后处理，导致细节损失和生成过于密集的网格。

**核心思路**：MILo框架通过可微分的方式直接从3D高斯中提取网格，避免了传统方法中体积到表面表示的转换限制，从而更好地保留几何结构。

**技术框架**：该方法包括三个主要模块：双向一致性框架、适应性网格提取过程和有符号距离计算。双向一致性确保高斯和提取的网格在训练过程中捕捉相同的几何结构。

**关键创新**：MILo的主要创新在于其可微分的网格提取过程，利用高斯作为Delaunay三角剖分的可微分支点，显著提高了表面提取的精度和效率。

**关键设计**：在训练过程中，优化的唯一参数是高斯的参数，网格的顶点位置和连接性在每次迭代中直接构建，确保了高效的训练和高质量的重建。该方法避免了几何侵蚀，能够精确提取表面。

## 📊 实验亮点

实验结果表明，MILo能够以比现有方法少一个数量级的网格顶点重建完整场景，同时保持最先进的重建质量。这一成果显著提升了3D重建的效率和效果，展示了该方法在实际应用中的巨大潜力。

## 🎯 应用场景

MILo框架在3D重建领域具有广泛的应用潜力，尤其适用于需要高质量几何表示的场景，如虚拟现实、游戏开发、物理模拟和动画制作。其轻量级网格结构使得在实时应用中表现优异，能够有效支持复杂场景的处理与展示。

## 📄 摘要（原文）

> While recent advances in Gaussian Splatting have enabled fast reconstruction of high-quality 3D scenes from images, extracting accurate surface meshes remains a challenge. Current approaches extract the surface through costly post-processing steps, resulting in the loss of fine geometric details or requiring significant time and leading to very dense meshes with millions of vertices. More fundamentally, the a posteriori conversion from a volumetric to a surface representation limits the ability of the final mesh to preserve all geometric structures captured during training. We present MILo, a novel Gaussian Splatting framework that bridges the gap between volumetric and surface representations by differentiably extracting a mesh from the 3D Gaussians. We design a fully differentiable procedure that constructs the mesh-including both vertex locations and connectivity-at every iteration directly from the parameters of the Gaussians, which are the only quantities optimized during training. Our method introduces three key technical contributions: a bidirectional consistency framework ensuring both representations-Gaussians and the extracted mesh-capture the same underlying geometry during training; an adaptive mesh extraction process performed at each training iteration, which uses Gaussians as differentiable pivots for Delaunay triangulation; a novel method for computing signed distance values from the 3D Gaussians that enables precise surface extraction while avoiding geometric erosion. Our approach can reconstruct complete scenes, including backgrounds, with state-of-the-art quality while requiring an order of magnitude fewer mesh vertices than previous methods. Due to their light weight and empty interior, our meshes are well suited for downstream applications such as physics simulations or animation.

