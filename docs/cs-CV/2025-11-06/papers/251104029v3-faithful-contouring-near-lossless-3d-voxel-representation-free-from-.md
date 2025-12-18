---
layout: default
title: Faithful Contouring: Near-Lossless 3D Voxel Representation Free from Iso-surface
---

# Faithful Contouring: Near-Lossless 3D Voxel Representation Free from Iso-surface

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04029" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04029v3</a>
  <a href="https://arxiv.org/pdf/2511.04029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04029v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04029v3', 'Faithful Contouring: Near-Lossless 3D Voxel Representation Free from Iso-surface')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihao Luo, Xianglong He, Chuanyu Pan, Yiwen Chen, Jiaqi Wu, Yangguang Li, Wanli Ouyang, Yuanming Hu, Guang Yang, ChoonHwai Yap

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-06 (更新: 2025-11-12)

---

## 💡 一句话要点

**提出 Faithful Contouring，实现近乎无损的3D体素表示，无需等值面提取。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `3D重建` `体素化` `稀疏表示` `自动编码器` `几何建模`

## 📋 核心要点

1. 现有3D网格体素化方法依赖水密化或渲染优化，牺牲了几何保真度，难以兼顾精度与效率。
2. Faithful Contouring通过稀疏体素化表示，直接对网格进行编码，避免了等值面提取，保留了锐利特征和内部结构。
3. 实验表明，Faithful Contouring在表示精度和重建质量上显著优于现有方法，尤其在复杂几何体上表现突出。

## 📝 摘要（中文）

精确且高效的3D网格体素化表示是3D重建和生成的基础。然而，现有的基于等值面的表示方法严重依赖于水密化或渲染优化，这不可避免地会损害几何保真度。我们提出了Faithful Contouring，一种稀疏体素化表示，支持2048+分辨率的任意网格，无需将网格转换为场函数，也无需在重新划分网格期间提取等值面。通过保留锐度和内部结构，即使对于具有复杂几何和拓扑结构的具有挑战性的情况，它也能实现近乎无损的保真度。所提出的方法还显示出在纹理处理、操作和编辑方面的灵活性。除了表示之外，我们还为Faithful Contouring设计了一种双模自动编码器，从而实现可扩展且保留细节的形状重建。大量实验表明，Faithful Contouring在表示和重建的准确性和效率方面均优于现有方法。对于直接表示，它实现了$10^{-5}$级别的距离误差；对于网格重建，与强大的基线相比，它在Chamfer距离上减少了93％，在F-score上提高了35％，从而证实了其作为3D学习任务表示的卓越保真度。

## 🔬 方法详解

**问题定义**：现有基于等值面的体素化方法，如Marching Cubes等，需要先将网格转换为场函数，再提取等值面。这一过程通常需要水密化处理，会引入几何误差，尤其是在处理复杂拓扑结构时。此外，高分辨率的等值面提取计算成本高昂，限制了表示的精度和效率。因此，如何在保证几何保真度的前提下，实现高效的3D网格体素化表示是一个关键问题。

**核心思路**：Faithful Contouring的核心思路是直接在体素空间中对网格进行编码，避免了中间的场函数转换和等值面提取步骤。它通过一种新的稀疏体素化表示方法，精确地捕捉网格的几何特征，包括锐利边缘和内部结构。这种直接编码的方式可以最大限度地保留原始网格的几何信息，从而实现近乎无损的表示。

**技术框架**：Faithful Contouring的整体框架包括两个主要部分：网格编码和网格重建。在网格编码阶段，输入3D网格被转换为Faithful Contouring表示，即一组稀疏体素。在网格重建阶段，可以使用一个双模自动编码器从Faithful Contouring表示中重建出3D网格。该自动编码器由编码器和解码器组成，编码器将Faithful Contouring表示压缩成潜在向量，解码器则从潜在向量中重建出3D网格。

**关键创新**：Faithful Contouring的关键创新在于其稀疏体素化表示方法，它能够以高精度捕捉网格的几何特征，同时保持较高的效率。与现有方法相比，Faithful Contouring不需要进行水密化处理，避免了由此引入的几何误差。此外，Faithful Contouring还支持高分辨率的表示，可以处理具有复杂几何和拓扑结构的网格。

**关键设计**：Faithful Contouring的关键设计包括：1) 一种新的体素化规则，用于精确地捕捉网格的几何特征；2) 一种稀疏数据结构，用于高效地存储体素化结果；3) 一个双模自动编码器，用于从Faithful Contouring表示中重建出3D网格。自动编码器的损失函数包括重建损失和正则化项，用于保证重建网格的质量和光滑性。具体参数设置未知。

## 📊 实验亮点

实验结果表明，Faithful Contouring在直接表示方面实现了$10^{-5}$级别的距离误差，显著优于现有方法。在网格重建方面，与强大的基线相比，Faithful Contouring在Chamfer距离上减少了93％，在F-score上提高了35％。这些结果表明，Faithful Contouring能够以更高的精度和效率表示和重建3D网格。

## 🎯 应用场景

Faithful Contouring在3D重建、3D生成、计算机辅助设计（CAD）等领域具有广泛的应用前景。它可以用于创建高精度的3D模型，用于虚拟现实、增强现实、游戏开发等应用。此外，Faithful Contouring还可以用于3D打印、逆向工程等领域，提高生产效率和产品质量。未来，该方法有望推动3D视觉和图形学领域的发展。

## 📄 摘要（原文）

> Accurate and efficient voxelized representations of 3D meshes are the foundation of 3D reconstruction and generation. However, existing representations based on iso-surface heavily rely on water-tightening or rendering optimization, which inevitably compromise geometric fidelity. We propose Faithful Contouring, a sparse voxelized representation that supports 2048+ resolutions for arbitrary meshes, requiring neither converting meshes to field functions nor extracting the isosurface during remeshing. It achieves near-lossless fidelity by preserving sharpness and internal structures, even for challenging cases with complex geometry and topology. The proposed method also shows flexibility for texturing, manipulation, and editing. Beyond representation, we design a dual-mode autoencoder for Faithful Contouring, enabling scalable and detail-preserving shape reconstruction. Extensive experiments show that Faithful Contouring surpasses existing methods in accuracy and efficiency for both representation and reconstruction. For direct representation, it achieves distance errors at the $10^{-5}$ level; for mesh reconstruction, it yields a 93\% reduction in Chamfer Distance and a 35\% improvement in F-score over strong baselines, confirming superior fidelity as a representation for 3D learning tasks.

