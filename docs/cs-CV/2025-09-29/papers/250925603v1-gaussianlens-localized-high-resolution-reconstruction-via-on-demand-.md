---
layout: default
title: "GaussianLens: Localized High-Resolution Reconstruction via On-Demand Gaussian Densification"
---

# GaussianLens: Localized High-Resolution Reconstruction via On-Demand Gaussian Densification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25603" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25603v1</a>
  <a href="https://arxiv.org/pdf/2509.25603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25603v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25603v1', 'GaussianLens: Localized High-Resolution Reconstruction via On-Demand Gaussian Densification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijia Weng, Zhicheng Wang, Songyou Peng, Saining Xie, Howard Zhou, Leonidas J. Guibas

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**GaussianLens：基于按需高斯致密化的局部高分辨率重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `局部重建` `高分辨率重建` `按需致密化` `神经渲染`

## 📋 核心要点

1. 现有3DGS方法在处理高分辨率图像时，由于计算成本高昂，难以重建局部精细细节。
2. GaussianLens通过学习一个可泛化的网络，按需对用户指定的局部区域进行高斯致密化，从而重建精细细节。
3. 实验结果表明，GaussianLens在局部细节重建方面优于现有方法，并能有效处理高分辨率图像。

## 📝 摘要（中文）

我们通过主动聚焦来感知周围环境，更加关注感兴趣的区域，例如杂货店中的货架标签。在场景重建方面，这种人类感知特性需要空间上不同程度的细节，以便在关键区域进行更仔细的检查，最好是按需重建。虽然最近的3D高斯溅射（3DGS）在稀疏视图中实现了快速、可泛化的重建，但其均匀分辨率输出导致高计算成本，无法扩展到高分辨率训练。因此，他们无法利用原始高分辨率的可用图像来重建细节。逐场景优化方法通过自适应密度控制重建更精细的细节，但需要密集的观测和耗时的离线优化。为了弥合高分辨率整体重建的过高成本与用户对局部精细细节的需求之间的差距，我们提出了通过按需高斯致密化进行局部高分辨率重建的问题。给定一个低分辨率的3DGS重建，目标是学习一个可泛化的网络，该网络致密化初始3DGS，以基于感兴趣区域（RoI）的稀疏高分辨率观测来捕获用户指定的局部区域中的精细细节。这种公式避免了均匀高分辨率重建的高成本和冗余，并充分利用了关键区域中的高分辨率捕获。我们提出了GaussianLens，这是一个前馈致密化框架，它融合了来自初始3DGS和多视图图像的多模态信息。我们进一步设计了一种像素引导的致密化机制，可以有效地捕获大分辨率增加下的细节。实验表明，我们的方法在局部精细细节重建方面表现出卓越的性能，并且对高达1024x1024分辨率的图像具有强大的可扩展性。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射（3DGS）方法虽然能快速重建场景，但其均匀分辨率的输出在高分辨率图像上计算成本过高，无法有效重建局部精细细节。逐场景优化方法虽然可以重建精细细节，但需要密集的观测和耗时的离线优化。因此，如何在稀疏高分辨率观测下，高效地重建用户感兴趣区域（RoI）的精细细节是一个挑战。

**核心思路**：GaussianLens的核心思路是按需进行局部高分辨率重建。它首先利用低分辨率的3DGS重建作为基础，然后学习一个可泛化的网络，根据用户指定的RoI，对该区域进行高斯致密化，从而在局部实现高分辨率重建。这种方法避免了全局高分辨率重建的计算负担，并充分利用了RoI区域的高分辨率图像信息。

**技术框架**：GaussianLens的整体框架包含以下几个主要步骤：1) 使用低分辨率图像进行初始3DGS重建；2) 用户指定感兴趣区域（RoI）；3) GaussianLens网络融合初始3DGS信息和RoI区域的多视图高分辨率图像信息；4) 通过像素引导的致密化机制，在RoI区域增加高斯点的密度，从而重建精细细节。该框架是一个前馈网络，可以实现快速的按需重建。

**关键创新**：GaussianLens的关键创新在于其按需高斯致密化机制和像素引导的致密化方法。按需致密化避免了全局高分辨率重建的计算负担，而像素引导的致密化方法则能够有效地利用高分辨率图像信息，在RoI区域重建精细细节。与现有方法相比，GaussianLens能够更好地平衡重建质量和计算效率。

**关键设计**：GaussianLens网络融合了来自初始3DGS和多视图图像的多模态信息。像素引导的致密化机制通过分析高分辨率图像的像素信息，指导高斯点的增加和调整。具体的损失函数和网络结构细节在论文中进行了详细描述，旨在优化高斯点的分布，从而更好地重建RoI区域的精细细节。

## 📊 实验亮点

实验结果表明，GaussianLens在局部精细细节重建方面表现出卓越的性能，并且对高达1024x1024分辨率的图像具有强大的可扩展性。与现有方法相比，GaussianLens能够更有效地重建RoI区域的精细细节，同时保持较低的计算成本。具体的性能数据和对比基线在论文中进行了详细展示。

## 🎯 应用场景

GaussianLens在许多领域具有潜在的应用价值。例如，在电商领域，可以用于生成商品的高清局部细节图，方便用户查看商品的材质和纹理。在自动驾驶领域，可以用于重建车辆周围环境的关键区域，提高感知精度。在文物保护领域，可以用于对文物进行局部高分辨率重建，方便研究人员进行分析和修复。该研究的未来影响在于，它为按需高分辨率重建提供了一种高效且可扩展的解决方案。

## 📄 摘要（原文）

> We perceive our surroundings with an active focus, paying more attention to regions of interest, such as the shelf labels in a grocery store. When it comes to scene reconstruction, this human perception trait calls for spatially varying degrees of detail ready for closer inspection in critical regions, preferably reconstructed on demand. While recent works in 3D Gaussian Splatting (3DGS) achieve fast, generalizable reconstruction from sparse views, their uniform resolution output leads to high computational costs unscalable to high-resolution training. As a result, they cannot leverage available images at their original high resolution to reconstruct details. Per-scene optimization methods reconstruct finer details with adaptive density control, yet require dense observations and lengthy offline optimization. To bridge the gap between the prohibitive cost of high-resolution holistic reconstructions and the user needs for localized fine details, we propose the problem of localized high-resolution reconstruction via on-demand Gaussian densification. Given a low-resolution 3DGS reconstruction, the goal is to learn a generalizable network that densifies the initial 3DGS to capture fine details in a user-specified local region of interest (RoI), based on sparse high-resolution observations of the RoI. This formulation avoids the high cost and redundancy of uniformly high-resolution reconstructions and fully leverages high-resolution captures in critical regions. We propose GaussianLens, a feed-forward densification framework that fuses multi-modal information from the initial 3DGS and multi-view images. We further design a pixel-guided densification mechanism that effectively captures details under large resolution increases. Experiments demonstrate our method's superior performance in local fine detail reconstruction and strong scalability to images of up to $1024\times1024$ resolution.

