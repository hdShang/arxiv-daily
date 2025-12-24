---
layout: default
title: "IGFuse: Interactive 3D Gaussian Scene Reconstruction via Multi-Scans Fusion"
---

# IGFuse: Interactive 3D Gaussian Scene Reconstruction via Multi-Scans Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13153" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13153v1</a>
  <a href="https://arxiv.org/pdf/2508.13153.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13153v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13153v1', 'IGFuse: Interactive 3D Gaussian Scene Reconstruction via Multi-Scans Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhao Hu, Zesheng Li, Haonan Zhou, Liu Liu, Xuexiang Wen, Zhizhong Su, Xi Li, Gaoang Wang

**分类**: cs.CV

**发布日期**: 2025-08-18

**备注**: Project page: https://whhu7.github.io/IGFuse

---

## 💡 一句话要点

**提出IGFuse以解决3D场景重建中的遮挡与覆盖问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `高斯场` `多次扫描` `物体遮挡` `计算机视觉` `机器人技术` `场景理解`

## 📋 核心要点

1. 现有的3D场景重建方法在处理物体遮挡和传感器覆盖不足时存在显著不足，导致重建效果不佳。
2. IGFuse通过融合多次扫描的观察，利用物体重排揭示遮挡区域，构建分割感知的高斯场，确保光度和语义一致性。
3. 实验结果表明，IGFuse在新场景配置上具有强泛化能力，能够实现高保真渲染和物体级操作，优于传统方法。

## 📝 摘要（中文）

完整且交互式的3D场景重建在计算机视觉和机器人领域仍然是一个基本挑战，尤其是在物体遮挡和传感器覆盖有限的情况下。单次场景扫描的多视角观察往往无法捕捉到完整的结构细节。现有方法通常依赖于多阶段管道，如分割、背景补全和修复，或需要对每个物体进行密集扫描，这些方法都容易出错且不易扩展。我们提出了IGFuse，一个通过融合多次扫描观察重建交互式高斯场景的新框架，其中自然物体重排揭示了先前被遮挡的区域。该方法构建了分割感知的高斯场，并在扫描之间强制双向光度和语义一致性。为了解决空间错位问题，我们引入了伪中间场景状态以实现统一对齐，并采用协作共修剪策略来精炼几何形状。IGFuse能够在没有密集观察或复杂管道的情况下实现高保真渲染和物体级场景操作。大量实验验证了该框架对新场景配置的强泛化能力，展示了其在现实世界3D重建和真实到仿真转移中的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决3D场景重建中由于物体遮挡和传感器覆盖不足导致的结构细节缺失问题。现有方法通常依赖于多阶段处理流程，容易出错且不具备良好的扩展性。

**核心思路**：IGFuse的核心思路是通过融合多次扫描的观察，利用物体在捕捉过程中的自然重排来揭示被遮挡的区域，从而实现更完整的场景重建。

**技术框架**：IGFuse的整体架构包括多个模块，首先是多次扫描数据的融合，然后构建分割感知的高斯场，接着通过引入伪中间场景状态实现对齐，最后采用协作共修剪策略来优化几何形状。

**关键创新**：IGFuse的主要创新在于其通过自然物体重排揭示遮挡区域的能力，以及在多个扫描之间强制光度和语义一致性，这与传统方法的单一视角处理方式有本质区别。

**关键设计**：在技术细节上，IGFuse采用了特定的损失函数来确保光度和语义的一致性，并设计了高效的网络结构以处理多次扫描数据的融合与对齐。具体参数设置和网络架构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，IGFuse在新场景配置上展现出强大的泛化能力，能够在没有密集观察的情况下实现高保真渲染。与传统方法相比，IGFuse在重建精度和效率上均有显著提升，具体性能数据在实验部分进行了详细对比。

## 🎯 应用场景

IGFuse的研究成果在多个领域具有潜在应用价值，包括虚拟现实、增强现实和机器人导航等。通过实现高保真的3D场景重建，该技术能够提升用户体验，并为自动化系统提供更准确的环境理解能力，推动相关领域的发展。

## 📄 摘要（原文）

> Reconstructing complete and interactive 3D scenes remains a fundamental challenge in computer vision and robotics, particularly due to persistent object occlusions and limited sensor coverage. Multiview observations from a single scene scan often fail to capture the full structural details. Existing approaches typically rely on multi stage pipelines, such as segmentation, background completion, and inpainting or require per-object dense scanning, both of which are error-prone, and not easily scalable. We propose IGFuse, a novel framework that reconstructs interactive Gaussian scene by fusing observations from multiple scans, where natural object rearrangement between captures reveal previously occluded regions. Our method constructs segmentation aware Gaussian fields and enforces bi-directional photometric and semantic consistency across scans. To handle spatial misalignments, we introduce a pseudo-intermediate scene state for unified alignment, alongside collaborative co-pruning strategies to refine geometry. IGFuse enables high fidelity rendering and object level scene manipulation without dense observations or complex pipelines. Extensive experiments validate the framework's strong generalization to novel scene configurations, demonstrating its effectiveness for real world 3D reconstruction and real-to-simulation transfer. Our project page is available online.

