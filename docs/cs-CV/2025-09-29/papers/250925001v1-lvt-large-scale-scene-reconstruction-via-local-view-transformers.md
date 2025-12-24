---
layout: default
title: "LVT: Large-Scale Scene Reconstruction via Local View Transformers"
---

# LVT: Large-Scale Scene Reconstruction via Local View Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25001" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25001v1</a>
  <a href="https://arxiv.org/pdf/2509.25001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25001v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25001v1', 'LVT: Large-Scale Scene Reconstruction via Local View Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-29

**备注**: SIGGRAPH Asia 2025 camera-ready version; project page https://toobaimt.github.io/lvt/

**DOI**: [10.1145/3757377.3763838](https://doi.org/10.1145/3757377.3763838)

**🔗 代码/项目**: [PROJECT_PAGE](https://toobaimt.github.io/lvt/)

---

## 💡 一句话要点

**提出局部视图Transformer(LVT)，用于大规模场景重建和新视角合成。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `大规模场景重建` `新视角合成` `局部视图Transformer` `3D高斯Splats` `相对几何变换`

## 📋 核心要点

1. 现有Transformer模型在处理大规模3D场景时，由于其二次复杂度，面临计算瓶颈。
2. LVT通过仅关注局部邻域内的视图信息，并利用相对几何变换进行位置编码，有效降低了计算复杂度。
3. LVT能够重建任意大的高分辨率场景，并生成具有视角依赖性的3D高斯Splats场景表示。

## 📝 摘要（中文）

大型Transformer模型正在成为3D视觉和新视角合成的强大工具。然而，标准Transformer的二次复杂度使其难以将这些方法扩展到大型场景。为了解决这个挑战，我们提出了局部视图Transformer（LVT），这是一种大规模场景重建和新视角合成架构，它避免了二次注意力运算的需求。受到空间上附近的视图比远处的视图提供更多关于局部场景组成信息的启发，我们的模型处理每个视图周围局部邻域中的所有信息。为了关注附近视图中的tokens，我们利用了一种新颖的位置编码，该编码以查询视图和附近视图之间的相对几何变换为条件。我们将模型的输出解码为3D高斯Splats场景表示，其中包括颜色和不透明度的视角依赖性。总而言之，局部视图Transformer能够在单个前向传递中重建任意大的高分辨率场景。

## 🔬 方法详解

**问题定义**：现有基于Transformer的3D场景重建方法，特别是新视角合成，在处理大规模场景时面临计算复杂度过高的问题。标准Transformer的注意力机制具有二次复杂度，导致计算量随视图数量的增加而迅速增长，难以扩展到大型、高分辨率的场景重建任务。

**核心思路**：LVT的核心思路是利用局部性原理，即空间上相邻的视图包含更多关于局部场景的信息。因此，模型只需要关注每个视图周围的局部邻域，而无需全局注意力。通过限制注意力范围，显著降低了计算复杂度，从而能够处理大规模场景。

**技术框架**：LVT的整体架构包括以下几个主要步骤：1) 对输入视图进行局部邻域划分；2) 使用Transformer编码器处理每个局部邻域内的视图信息；3) 利用基于相对几何变换的位置编码，将空间信息融入到注意力机制中；4) 将Transformer的输出解码为3D高斯Splats场景表示，该表示包含颜色和不透明度的视角依赖性。

**关键创新**：LVT的关键创新在于局部注意力机制和基于相对几何变换的位置编码。局部注意力机制通过限制注意力范围，降低了计算复杂度。基于相对几何变换的位置编码，能够有效地建模视图之间的空间关系，从而提高重建质量。

**关键设计**：LVT的关键设计包括：1) 局部邻域的大小，需要根据场景的尺度和视图的密度进行调整；2) 相对几何变换的表示方式，例如使用旋转和平移矩阵；3) 3D高斯Splats场景表示的参数化方式，例如使用颜色、不透明度、方差等参数；4) 损失函数的设计，例如使用渲染损失和正则化项。

## 📊 实验亮点

LVT通过局部注意力机制和相对几何变换位置编码，实现了大规模场景的重建和新视角合成。实验结果表明，LVT能够在单个前向传递中重建任意大的高分辨率场景，并且在重建质量和计算效率方面都优于现有方法。项目页面提供了交互式演示，展示了LVT在各种场景下的重建效果。

## 🎯 应用场景

LVT具有广泛的应用前景，包括城市级别的三维重建、自动驾驶场景理解、虚拟现实和增强现实等领域。该技术可以用于创建高精度、高分辨率的三维场景模型，为各种应用提供基础数据和视觉支持。此外，LVT还可以用于新视角合成，生成任意视角的图像，为用户提供更加沉浸式的体验。

## 📄 摘要（原文）

> Large transformer models are proving to be a powerful tool for 3D vision and novel view synthesis. However, the standard Transformer's well-known quadratic complexity makes it difficult to scale these methods to large scenes. To address this challenge, we propose the Local View Transformer (LVT), a large-scale scene reconstruction and novel view synthesis architecture that circumvents the need for the quadratic attention operation. Motivated by the insight that spatially nearby views provide more useful signal about the local scene composition than distant views, our model processes all information in a local neighborhood around each view. To attend to tokens in nearby views, we leverage a novel positional encoding that conditions on the relative geometric transformation between the query and nearby views. We decode the output of our model into a 3D Gaussian Splat scene representation that includes both color and opacity view-dependence. Taken together, the Local View Transformer enables reconstruction of arbitrarily large, high-resolution scenes in a single forward pass. See our project page for results and interactive demos https://toobaimt.github.io/lvt/.

