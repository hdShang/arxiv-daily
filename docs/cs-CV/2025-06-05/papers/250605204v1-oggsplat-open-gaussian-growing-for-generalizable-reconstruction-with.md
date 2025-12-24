---
layout: default
title: "OGGSplat: Open Gaussian Growing for Generalizable Reconstruction with Expanded Field-of-View"
---

# OGGSplat: Open Gaussian Growing for Generalizable Reconstruction with Expanded Field-of-View

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05204" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05204v1</a>
  <a href="https://arxiv.org/pdf/2506.05204.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05204v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05204v1', 'OGGSplat: Open Gaussian Growing for Generalizable Reconstruction with Expanded Field-of-View')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanbo Wang, Ziyi Wang, Wenzhao Zheng, Jie Zhou, Jiwen Lu

**分类**: cs.CV

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出OGGSplat以解决稀疏视图下的3D场景重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D重建` `语义感知` `开放高斯` `图像外推` `虚拟现实` `增强现实` `计算机视觉`

## 📋 核心要点

1. 现有的逐场景优化方法依赖于密集输入视图，导致计算成本高且难以扩展。
2. OGGSplat通过开放高斯生长方法，利用语义属性进行图像外推，实现语义一致性与视觉可信性。
3. 在实验中，OGGSplat展示了在仅有两幅智能手机拍摄的图像下进行语义感知场景重建的能力。

## 📝 摘要（中文）

从稀疏视图重建语义感知的3D场景是一项具有挑战性的研究方向，尤其在虚拟现实和具身AI等新兴应用中需求日益增长。现有的逐场景优化方法需要密集的输入视图，计算成本高，而通用方法在重建输入视图锥体外的区域时常常遇到困难。本文提出了OGGSplat，一种开放高斯生长方法，扩展了通用3D重建的视场。我们的关键见解是开放高斯的语义属性为图像外推提供了强有力的先验，从而实现语义一致性和视觉可信性。具体而言，一旦从稀疏视图初始化开放高斯，我们引入了一个RGB-语义一致的修复模块，应用于选定的渲染视图，确保图像扩散模型与语义扩散模型之间的双向控制。

## 🔬 方法详解

**问题定义**：本文旨在解决从稀疏视图重建3D场景时的语义一致性和视觉可信性问题。现有方法通常需要密集的输入视图，计算成本高且难以处理视图锥体外的区域。

**核心思路**：OGGSplat的核心思路是利用开放高斯的语义属性作为图像外推的先验，从而在重建过程中保持语义一致性和视觉可信性。通过初始化开放高斯并引入RGB-语义一致的修复模块，增强了重建效果。

**技术框架**：OGGSplat的整体架构包括开放高斯初始化、RGB-语义一致修复模块和3D空间的高斯参数优化。修复模块确保图像和语义模型之间的双向控制，提升了重建质量。

**关键创新**：OGGSplat的主要创新在于开放高斯生长方法的提出，利用语义属性进行图像外推，与传统方法相比，能够更好地处理稀疏视图下的重建问题。

**关键设计**：在设计中，重点关注开放高斯的初始化过程、修复模块的损失函数设计以及高斯参数的优化策略，以确保重建质量和效率。具体的网络结构和参数设置在实验中进行了详细验证。

## 📊 实验亮点

OGGSplat在Gaussian Outpainting基准测试中表现出色，展示了在语义和生成质量上的显著提升。与现有方法相比，重建的开放词汇场景在语义一致性和视觉效果上均有明显改善，尤其是在仅使用两幅智能手机拍摄的图像时，重建效果依然令人满意。

## 🎯 应用场景

该研究在虚拟现实、增强现实和具身AI等领域具有广泛的应用潜力。通过实现高效的3D场景重建，OGGSplat可以为用户提供更沉浸的体验，推动相关技术的发展和应用。未来，该方法可能在自动驾驶、机器人导航等领域发挥重要作用。

## 📄 摘要（原文）

> Reconstructing semantic-aware 3D scenes from sparse views is a challenging yet essential research direction, driven by the demands of emerging applications such as virtual reality and embodied AI. Existing per-scene optimization methods require dense input views and incur high computational costs, while generalizable approaches often struggle to reconstruct regions outside the input view cone. In this paper, we propose OGGSplat, an open Gaussian growing method that expands the field-of-view in generalizable 3D reconstruction. Our key insight is that the semantic attributes of open Gaussians provide strong priors for image extrapolation, enabling both semantic consistency and visual plausibility. Specifically, once open Gaussians are initialized from sparse views, we introduce an RGB-semantic consistent inpainting module applied to selected rendered views. This module enforces bidirectional control between an image diffusion model and a semantic diffusion model. The inpainted regions are then lifted back into 3D space for efficient and progressive Gaussian parameter optimization. To evaluate our method, we establish a Gaussian Outpainting (GO) benchmark that assesses both semantic and generative quality of reconstructed open-vocabulary scenes. OGGSplat also demonstrates promising semantic-aware scene reconstruction capabilities when provided with two view images captured directly from a smartphone camera.

