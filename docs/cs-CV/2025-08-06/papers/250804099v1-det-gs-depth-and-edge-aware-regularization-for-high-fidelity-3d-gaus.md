---
layout: default
title: "DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D Gaussian Splatting"
---

# DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04099" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04099v1</a>
  <a href="https://arxiv.org/pdf/2508.04099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04099v1', 'DET-GS: Depth- and Edge-Aware Regularization for High-Fidelity 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zexu Huang, Min Xu, Stuart Perry

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出DET-GS以解决稀疏视图下3D重建精度不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D重建` `深度学习` `边缘检测` `视觉合成` `高保真渲染` `计算机视觉` `图形学` `深度正则化`

## 📋 核心要点

1. 现有方法在稀疏视图条件下的几何重建精度不足，且对深度估计噪声敏感。
2. 提出DET-GS框架，通过分层几何深度监督和边缘感知正则化，增强结构一致性。
3. 实验表明，DET-GS在几何准确性和视觉保真度上显著优于现有最先进方法。

## 📝 摘要（中文）

3D Gaussian Splatting (3DGS) 在高保真新视图合成领域取得了显著进展，但在稀疏视图条件下实现准确的几何重建仍然是一个基本挑战。现有方法通常依赖于非局部深度正则化，无法捕捉细粒度结构，并且对深度估计噪声高度敏感。此外，传统平滑方法忽视语义边界，导致重要边缘和纹理的降解，从而限制了重建的整体质量。为此，本文提出了DET-GS，一个统一的深度和边缘感知正则化框架，显著提高了结构保真度和对深度估计噪声的鲁棒性。通过广泛的实验，DET-GS在稀疏视图新视图合成基准上超越了现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在稀疏视图条件下进行高保真3D重建时，现有方法对细粒度结构捕捉不足及对深度估计噪声敏感的问题。

**核心思路**：DET-GS框架通过引入分层几何深度监督和边缘感知正则化，适应性地增强多层次几何一致性，从而提高结构保真度和鲁棒性。

**技术框架**：整体架构包括深度监督模块和边缘感知正则化模块，前者通过多层次深度信息增强几何一致性，后者则利用Canny边缘检测生成的语义掩码来指导正则化过程。

**关键创新**：最重要的创新在于引入了RGB引导的边缘保留总变差损失，能够选择性地平滑同质区域，同时严格保留高频细节和纹理，这在现有方法中尚未实现。

**关键设计**：设计中包括多层次深度监督的参数设置，以及基于Canny边缘检测的语义掩码生成，确保在保留重要边缘和纹理的同时，提升整体重建质量。

## 📊 实验亮点

DET-GS在稀疏视图新视图合成基准上表现出色，几何准确性和视觉保真度显著提升，超越了现有最先进方法，具体性能数据未提供，但实验结果表明其在多个指标上均有显著改善。

## 🎯 应用场景

该研究在计算机视觉和图形学领域具有广泛的应用潜力，尤其是在虚拟现实、增强现实和影视特效制作中。通过提高稀疏视图下的3D重建精度，DET-GS能够为用户提供更真实的视觉体验，推动相关技术的发展和应用。未来，该方法可能在自动驾驶、机器人导航等领域也展现出重要价值。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) represents a significant advancement in the field of efficient and high-fidelity novel view synthesis. Despite recent progress, achieving accurate geometric reconstruction under sparse-view conditions remains a fundamental challenge. Existing methods often rely on non-local depth regularization, which fails to capture fine-grained structures and is highly sensitive to depth estimation noise. Furthermore, traditional smoothing methods neglect semantic boundaries and indiscriminately degrade essential edges and textures, consequently limiting the overall quality of reconstruction. In this work, we propose DET-GS, a unified depth and edge-aware regularization framework for 3D Gaussian Splatting. DET-GS introduces a hierarchical geometric depth supervision framework that adaptively enforces multi-level geometric consistency, significantly enhancing structural fidelity and robustness against depth estimation noise. To preserve scene boundaries, we design an edge-aware depth regularization guided by semantic masks derived from Canny edge detection. Furthermore, we introduce an RGB-guided edge-preserving Total Variation loss that selectively smooths homogeneous regions while rigorously retaining high-frequency details and textures. Extensive experiments demonstrate that DET-GS achieves substantial improvements in both geometric accuracy and visual fidelity, outperforming state-of-the-art (SOTA) methods on sparse-view novel view synthesis benchmarks.

