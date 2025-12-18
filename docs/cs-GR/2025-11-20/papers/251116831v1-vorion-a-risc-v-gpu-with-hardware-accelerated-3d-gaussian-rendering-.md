---
layout: default
title: Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training
---

# Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16831" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16831v1</a>
  <a href="https://arxiv.org/pdf/2511.16831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16831v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16831v1', 'Vorion: A RISC-V GPU with Hardware-Accelerated 3D Gaussian Rendering and Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yipeng Wang, Mengtian Yang, Chieh-pu Lo, Jaydeep P. Kulkarni

**分类**: cs.AR, cs.GR

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**Vorion：首个硬件加速3D高斯渲染与训练的RISC-V GPU原型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `硬件加速` `RISC-V GPU` `神经渲染` `实时渲染`

## 📋 核心要点

1. 3D高斯溅射(3DGS)虽然在神经渲染领域表现出色，但其计算密集型特性限制了其在边缘设备和实时4D重建中的应用。
2. Vorion通过专用硬件加速3DGS渲染和训练，旨在克服现有计算瓶颈，实现更高效的实时神经渲染。
3. 该原型系统基于RISC-V架构，采用TSMC 16nm FinFET工艺，渲染速度达到19 FPS，训练速度达到38.6 iterations/s。

## 📝 摘要（中文）

3D高斯溅射(3DGS)已成为实时神经渲染、3D场景生成和体视频(4D)捕获的基础技术。然而，其渲染和训练需要大量的计算，使得在边缘设备上进行实时渲染和在工作站上进行实时4D重建变得不可行。鉴于其固定功能特性以及与传统光栅化的相似性，3DGS为下一代GPU图形管线中的专用硬件提供了一个强有力的理由。本文提出了Vorion，这是第一个具有硬件加速3DGS渲染和训练的GPGPU原型。Vorion具有可扩展的架构、对传统光栅器的最小硬件更改、用于增加并行性的z-tiling以及高斯/像素混合数据流。我们使用TSMC 16nm FinFET技术对最小系统（8个SIMT核心，2个高斯光栅器）进行了原型设计，实现了19 FPS的渲染速度。具有16个光栅器的扩展设计实现了38.6 iterations/s的训练速度。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射(3DGS)方法在实时神经渲染和4D重建等应用中面临巨大的计算挑战。传统GPU在处理3DGS时效率较低，难以满足边缘设备和工作站的实时性需求。因此，需要一种更高效的硬件加速方案来降低计算负担，提升渲染和训练速度。

**核心思路**：Vorion的核心思路是利用专用硬件加速3DGS的渲染和训练过程。通过定制化的硬件架构，针对3DGS的特定计算模式进行优化，从而提高计算效率和并行性。这种方法类似于传统图形管线中对光栅化等操作的硬件加速，能够显著提升性能。

**技术框架**：Vorion采用可扩展的架构，包含多个SIMT核心和高斯光栅器。整体流程包括：数据输入、高斯光栅化、像素处理和输出。Z-tiling技术用于提高并行性，将屏幕划分为多个小块，每个小块独立处理。数据流采用高斯/像素混合模式，根据具体操作选择最合适的数据组织方式。

**关键创新**：Vorion的关键创新在于其硬件加速的3DGS渲染和训练引擎。与传统GPU相比，Vorion通过定制化的硬件设计，实现了更高的计算效率和并行性。此外，Vorion对传统光栅器的硬件改动最小，易于集成到现有的图形管线中。

**关键设计**：Vorion的原型系统包含8个SIMT核心和2个高斯光栅器，采用TSMC 16nm FinFET工艺制造。扩展设计包含16个光栅器，进一步提升了训练速度。Z-tiling的大小和SIMT核心的数量是关键的参数，需要根据具体的应用场景进行调整。损失函数采用标准的3DGS损失函数，网络结构则根据硬件架构进行优化。

## 📊 实验亮点

Vorion原型系统在TSMC 16nm FinFET工艺下，使用8个SIMT核心和2个高斯光栅器实现了19 FPS的渲染速度。扩展设计使用16个光栅器，训练速度达到38.6 iterations/s。这些结果表明，Vorion的硬件加速方案能够显著提升3DGS的性能，为实时神经渲染和4D重建等应用提供了有力的支持。

## 🎯 应用场景

Vorion具有广泛的应用前景，包括实时神经渲染、3D场景生成、体视频(4D)捕获、自动驾驶、机器人导航和增强现实/虚拟现实(AR/VR)等领域。通过提高3DGS的渲染和训练速度，Vorion能够实现更逼真、更流畅的实时体验，并为相关应用带来新的可能性。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently emerged as a foundational technique for real-time neural rendering, 3D scene generation, volumetric video (4D) capture. However, its rendering and training impose massive computation, making real-time rendering on edge devices and real-time 4D reconstruction on workstations currently infeasible. Given its fixed-function nature and similarity with traditional rasterization, 3DGS presents a strong case for dedicated hardware in the graphics pipeline of next-generation GPUs. This work, Vorion, presents the first GPGPU prototype with hardware-accelerated 3DGS rendering and training. Vorion features scalable architecture, minimal hardware change to traditional rasterizers, z-tiling to increase parallelism, and Gaussian/pixel-centric hybrid dataflow. We prototype the minimal system (8 SIMT cores, 2 Gaussian rasterizer) using TSMC 16nm FinFET technology, which achieves 19 FPS for rendering. The scaled design with 16 rasterizers achieves 38.6 iterations/s for training.

