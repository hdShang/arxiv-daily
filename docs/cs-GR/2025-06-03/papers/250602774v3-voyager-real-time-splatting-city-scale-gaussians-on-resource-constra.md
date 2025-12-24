---
layout: default
title: "Voyager: Real-Time Splatting City-Scale Gaussians on Resource-Constrained Devices"
---

# Voyager: Real-Time Splatting City-Scale Gaussians on Resource-Constrained Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02774" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02774v3</a>
  <a href="https://arxiv.org/pdf/2506.02774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02774v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02774v3', 'Voyager: Real-Time Splatting City-Scale Gaussians on Resource-Constrained Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Liu, He Zhu, Xinyang Li, Yirun Wang, Yujiao Shi, Yiming Gan, Wei Li, Jingwen Leng, Minyi Guo, Yu Feng

**分类**: cs.GR

**发布日期**: 2025-06-03 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出Voyager以解决资源受限设备上的城市规模3D高斯渲染问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯渲染` `移动设备` `实时渲染` `细节层次` `光栅化` `能量节省` `城市规模场景` `时间感知技术`

## 📋 核心要点

1. 现有方法在资源受限的移动设备上实时渲染城市规模3D高斯场景面临LoD搜索和光栅化的计算瓶颈。
2. 本文提出Voyager，通过时间感知的LoD搜索和预先过滤技术加速渲染过程，利用用户运动的时间相关性。
3. 实验结果表明，Voyager相比现有方案实现了6.6倍的速度提升和85%的能量节省，同时保持了更高的渲染质量。

## 📝 摘要（中文）

3D高斯点云渲染（3DGS）是一种新兴的真实感3D场景渲染技术。然而，在资源受限的移动设备上实时渲染城市规模的3DGS场景仍然面临重大挑战，主要由于细节层次（LoD）搜索和光栅化这两个计算密集型阶段。本文提出了Voyager，一个有效的解决方案，通过利用用户运动下新可见高斯点数目相对恒定的时间相关性，提出了一种时间感知的LoD搜索方法来识别必要的高斯点。对于剩余的渲染过程，我们通过预先过滤光栅化瓶颈阶段来加速渲染。通过上述优化，我们的系统能够在移动设备上实现低延迟的城市规模3DGS渲染。与现有解决方案相比，Voyager实现了高达6.6倍的加速和85%的能量节省，同时保持了优越的渲染质量。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限的移动设备上实时渲染城市规模3D高斯场景的挑战，现有方法在细节层次搜索和光栅化阶段存在显著的计算瓶颈。

**核心思路**：论文的核心思路是利用用户运动下新可见高斯点数目相对恒定的特性，提出了一种时间感知的LoD搜索方法，以识别渲染所需的高斯点，从而减少计算量。

**技术框架**：整体架构包括两个主要模块：时间感知的LoD搜索模块和光栅化加速模块。前者负责识别当前视锥内需要渲染的高斯点，后者通过预先过滤技术加速光栅化过程。

**关键创新**：最重要的技术创新点在于引入了时间感知的LoD搜索方法和预先过滤光栅化技术，这与现有方法的静态处理方式形成了鲜明对比，显著提升了渲染效率。

**关键设计**：在参数设置上，系统通过分析用户运动模式来动态调整LoD搜索的范围，光栅化阶段则采用了预先过滤的策略，以减少不必要的计算，确保渲染质量与速度的平衡。

## 📊 实验亮点

实验结果显示，Voyager在渲染速度上实现了高达6.6倍的提升，并且在能量消耗上节省了85%。与现有方案相比，Voyager不仅提高了渲染效率，还保持了更高的渲染质量，展现了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括移动游戏、增强现实（AR）和虚拟现实（VR）等场景，能够在资源受限的设备上实现高质量的3D场景渲染，提升用户体验。未来，随着移动设备性能的提升和算法的进一步优化，Voyager有望在更广泛的应用中发挥重要作用。

## 📄 摘要（原文）

> 3D Gaussian splatting (3DGS) is an emerging technique for photorealistic 3D scene rendering. However, rendering city-scale 3DGS scenes on resource-constrained mobile devices in real-time remains a significant challenge due to two compute-intensive stages: level-of-detail (LoD) search and rasterization.
>   In this paper, we propose Voyager, an effective solution to accelerate city-scale 3DGS rendering on mobile devices. Our key insight is that, under normal user motion, the number of newly visible Gaussians within the view frustum remains roughly constant. Leveraging this temporal correlation, we propose a temporal-aware LoD search to identify the necessary Gaussians for the remaining rendering stages. For the remaining rendering process, we accelerate the bottleneck stage, rasterization, via preemptive $α$-filtering. With all optimizations above, our system can deliver low-latency, city-scale 3DGS rendering on mobile devices. Compared to existing solutions, Voyager achieves up to 6.6$\times$ speedup and 85\% energy savings with superior rendering quality.

