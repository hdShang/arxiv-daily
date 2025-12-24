---
layout: default
title: "Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS"
---

# Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09534" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09534v2</a>
  <a href="https://arxiv.org/pdf/2506.09534.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09534v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09534v2', 'Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Wang, Mengyu Li, Geduo Zeng, Cheng Meng, Qiong Zhang

**分类**: cs.CV

**发布日期**: 2025-06-11 (更新: 2025-09-23)

**备注**: 26 pages, 15 figures

**🔗 代码/项目**: [GITHUB](https://github.com/DrunkenPoet/GHAP)

---

## 💡 一句话要点

**提出全局高斯混合简化方法以解决3D高斯点云渲染的内存问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯混合简化` `最优传输` `3D高斯点云` `渲染优化` `计算机图形学`

## 📋 核心要点

1. 现有的3D高斯点云渲染方法通常需要大量冗余的高斯原语，导致内存和渲染效率低下。
2. 本文提出了一种基于最优传输的全局高斯混合简化方法，通过最小化复合传输散度来实现高效压缩。
3. 实验结果显示，所提方法在渲染质量上几乎没有损失，并且在性能上优于现有的压缩技术。

## 📝 摘要（中文）

3D高斯点云渲染（3DGS）是一种强大的辐射场渲染技术，但通常需要数百万个冗余的高斯原语，导致内存和渲染预算的过载。现有的压缩方法通过基于启发式重要性评分来修剪高斯，但未能保证全局保真度。为了解决这一问题，本文提出了一种新颖的最优传输视角，将3DGS压缩视为全局高斯混合简化。具体而言，我们首先在KD树分区上最小化复合传输散度，以生成紧凑的几何表示，然后通过微调颜色和不透明度属性，解耦外观与几何，使用更少的高斯原语。实验结果表明，我们的方法在渲染质量（PSNR、SSIM、LPIPS）上与标准3DGS相比几乎没有损失，仅使用10%的高斯，并且始终优于最先进的3DGS压缩技术。

## 🔬 方法详解

**问题定义**：本文旨在解决3D高斯点云渲染中冗余高斯原语导致的内存和渲染预算过载问题。现有方法通过启发式评分修剪高斯，缺乏全局保真度的保证。

**核心思路**：我们提出了一种最优传输的视角，将3DGS的压缩视为全局高斯混合简化。通过最小化复合传输散度，生成紧凑的几何表示，并通过微调颜色和不透明度来解耦外观与几何。

**技术框架**：整体流程包括两个主要阶段：首先在KD树分区上进行复合传输散度的最小化，以获得紧凑的几何表示；其次，通过调整颜色和不透明度属性，进一步减少所需的高斯原语数量。

**关键创新**：最重要的创新在于将3DGS压缩问题转化为全局高斯混合简化的最优传输问题，这一视角确保了全局保真度的提升。

**关键设计**：在技术细节上，采用KD树进行空间分区，设计了复合传输散度的损失函数，并通过微调策略优化颜色和不透明度属性，以实现高效的高斯原语减少。

## 📊 实验亮点

实验结果表明，所提方法在渲染质量（PSNR、SSIM、LPIPS）上与标准3DGS相比几乎没有损失，仅使用10%的高斯原语。此外，该方法在多个基准数据集上均优于现有的最先进3DGS压缩技术，展现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括计算机图形学、虚拟现实和增强现实等领域，能够显著提高渲染效率和降低内存消耗。未来，该方法可能推动轻量级神经渲染技术的发展，促进更高效的实时渲染应用。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for radiance field rendering, but it typically requires millions of redundant Gaussian primitives, overwhelming memory and rendering budgets. Existing compaction approaches address this by pruning Gaussians based on heuristic importance scores, without global fidelity guarantee. To bridge this gap, we propose a novel optimal transport perspective that casts 3DGS compaction as global Gaussian mixture reduction. Specifically, we first minimize the composite transport divergence over a KD-tree partition to produce a compact geometric representation, and then decouple appearance from geometry by fine-tuning color and opacity attributes with far fewer Gaussian primitives. Experiments on benchmark datasets show that our method (i) yields negligible loss in rendering quality (PSNR, SSIM, LPIPS) compared to vanilla 3DGS with only 10% Gaussians; and (ii) consistently outperforms state-of-the-art 3DGS compaction techniques. Notably, our method is applicable to any stage of vanilla or accelerated 3DGS pipelines, providing an efficient and agnostic pathway to lightweight neural rendering. The code is publicly available at https://github.com/DrunkenPoet/GHAP

