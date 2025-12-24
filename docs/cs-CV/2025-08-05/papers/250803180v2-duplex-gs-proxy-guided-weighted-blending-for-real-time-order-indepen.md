---
layout: default
title: "Duplex-GS: Proxy-Guided Weighted Blending for Real-Time Order-Independent Gaussian Splatting"
---

# Duplex-GS: Proxy-Guided Weighted Blending for Real-Time Order-Independent Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03180" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03180v2</a>
  <a href="https://arxiv.org/pdf/2508.03180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03180v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03180v2', 'Duplex-GS: Proxy-Guided Weighted Blending for Real-Time Order-Independent Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihang Liu, Yuke Li, Yuxuan Li, Jingyi Yu, Xin Lou

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-11-14)

**备注**: submitted to TCSVT

---

## 💡 一句话要点

**提出Duplex-GS以解决实时高效的高斯渲染问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯渲染` `无序透明度` `实时渲染` `计算机图形学` `虚拟现实` `增强现实` `高效算法`

## 📋 核心要点

1. 现有3D高斯渲染方法依赖于顺序alpha混合，导致在资源受限平台上存在显著的计算开销。
2. Duplex-GS通过代理高斯表示与无序渲染技术的结合，旨在实现高效且高保真的渲染效果。
3. 实验结果表明，Duplex-GS在多种场景下表现出色，速度提升达到1.5到4倍，同时显著降低了排序开销。

## 📝 摘要（中文）

近年来，3D高斯渲染（3DGS）在渲染保真度和效率方面取得了显著进展。然而，现有方法依赖于计算密集型的顺序alpha混合操作，导致在资源受限平台上存在显著开销。本文提出了Duplex-GS，一个双层次框架，结合代理高斯表示和无序渲染技术，实现了逼真的渲染效果，同时保持实时性能。通过引入单元代理管理局部高斯并提出单元搜索光栅化以加速处理，我们与无序透明度（OIT）无缝结合，开发了一种物理启发的加权和渲染技术，消除了“弹跳”和“透明度”伪影，显著提高了准确性和效率。大量实验验证了我们方法在多种真实数据集上的鲁棒性，显示出在现有OIT基础上实现了1.5到4倍的速度提升，并减少了52.2%到86.9%的基数排序开销，且没有质量下降。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D高斯渲染方法在资源受限平台上因顺序alpha混合导致的高计算开销问题。

**核心思路**：Duplex-GS框架通过引入代理高斯表示和无序渲染技术，旨在实现高效的实时渲染，同时保持高保真度。

**技术框架**：该框架包括两个主要模块：代理高斯管理和单元搜索光栅化。代理高斯用于局部高斯的管理，而单元搜索光栅化则加速了渲染过程。

**关键创新**：最重要的创新在于将代理高斯与无序透明度技术相结合，提出了一种新的加权和渲染方法，消除了传统方法中的“弹跳”和“透明度”伪影。

**关键设计**：在设计中，采用了单元代理来管理局部高斯，并通过优化的光栅化流程来减少排序开销，确保了在高质量渲染下的实时性能。

## 📊 实验亮点

实验结果显示，Duplex-GS在多种真实数据集上实现了1.5到4倍的速度提升，且基数排序开销减少了52.2%到86.9%，同时保持了渲染质量，验证了其在高效高斯渲染中的优势。

## 🎯 应用场景

Duplex-GS的研究成果可广泛应用于计算机图形学、虚拟现实和增强现实等领域，尤其是在需要实时渲染的场景中，如游戏开发和模拟训练。其高效的渲染能力将推动更复杂场景的实时可视化，提升用户体验。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated remarkable rendering fidelity and efficiency. However, these methods still rely on computationally expensive sequential alpha-blending operations, resulting in significant overhead, particularly on resource-constrained platforms. In this paper, we propose Duplex-GS, a dual-hierarchy framework that integrates proxy Gaussian representations with order-independent rendering techniques to achieve photorealistic results while sustaining real-time performance. To mitigate the overhead caused by view-adaptive radix sort, we introduce cell proxies for local Gaussians management and propose cell search rasterization for further acceleration. By seamlessly combining our framework with Order-Independent Transparency (OIT), we develop a physically inspired weighted sum rendering technique that simultaneously eliminates "popping" and "transparency" artifacts, yielding substantial improvements in both accuracy and efficiency. Extensive experiments on a variety of real-world datasets demonstrate the robustness of our method across diverse scenarios, including multi-scale training views and large-scale environments. Our results validate the advantages of the OIT rendering paradigm in Gaussian Splatting, achieving high-quality rendering with an impressive 1.5 to 4 speedup over existing OIT based Gaussian Splatting approaches and 52.2% to 86.9% reduction of the radix sort overhead without quality degradation.

