---
layout: default
title: "SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping"
---

# SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07917" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07917v3</a>
  <a href="https://arxiv.org/pdf/2506.07917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07917v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07917v3', 'SpeeDe3DGS: Speedy Deformable 3D Gaussian Splatting with Temporal Pruning and Motion Grouping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Allen Tu, Haiyang Ying, Alex Hanson, Yonghan Lee, Tom Goldstein, Matthias Zwicker

**分类**: cs.GR, cs.CV

**发布日期**: 2025-06-09 (更新: 2025-11-20)

**备注**: Project Page: https://speede3dgs.github.io/

---

## 💡 一句话要点

**提出SpeeDe3DGS以解决动态3D重建的效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态重建` `高斯点云` `神经网络` `渲染效率` `运动分组` `时间敏感性`

## 📋 核心要点

1. 现有的动态3D高斯点云重建方法在计算效率上存在显著不足，导致推理过程耗时较长。
2. 本文提出SpeeDe3DGS，通过时间敏感性修剪、时间敏感性采样和GroupFlow等模块提升渲染效率与质量。
3. 在MonoDyGauBench的50个动态场景上，SpeeDe3DGS实现了显著的速度提升，渲染速度提高了13.71倍。

## 📝 摘要（中文）

动态扩展的3D高斯点云重建（3DGS）通过神经运动场实现高质量重建，但每个高斯的神经推理使得这些模型计算开销巨大。基于DeformableGS，本文提出了SpeeDe3DGS，通过三个互补模块弥补效率与保真度之间的差距：时间敏感性修剪（TSP）通过时间聚合敏感性分析去除低影响高斯，时间敏感性采样（TSS）扰动时间戳以抑制浮动并改善时间一致性，GroupFlow将学习到的变形场提炼为共享的SE(3)变换以实现高效的组运动。实验表明，整合TSP和TSS后，DeformableGS的渲染速度平均加快6.78倍，同时使用10倍更少的原始数据。添加GroupFlow后，渲染速度达到13.71倍，训练时间缩短2.53倍，超越所有基线，保持优越的图像质量。

## 🔬 方法详解

**问题定义**：本文旨在解决动态3D高斯点云重建中的计算效率问题。现有方法由于每个高斯的独立神经推理，导致计算开销过大，影响实时应用。

**核心思路**：SpeeDe3DGS通过引入时间敏感性修剪（TSP）、时间敏感性采样（TSS）和GroupFlow模块，优化了动态场景中的高斯点云渲染效率，同时保持了高质量的重建效果。

**技术框架**：整体架构包括三个主要模块：TSP用于去除低影响高斯，TSS通过扰动时间戳改善时间一致性，GroupFlow则将变形场提炼为共享变换以实现高效运动处理。

**关键创新**：最重要的创新在于将时间敏感性分析与运动分组相结合，显著提升了渲染速度和训练效率，且在图像质量上优于现有方法。

**关键设计**：在设计中，TSP和TSS模块通过敏感性分析和时间戳扰动实现高效处理，GroupFlow则利用SE(3)变换进行运动聚合，整体减少了所需的原始数据量和计算复杂度。

## 📊 实验亮点

实验结果显示，整合TSP和TSS后，DeformableGS的渲染速度平均提升6.78倍，使用10倍更少的原始数据。引入GroupFlow后，渲染速度进一步提升至13.71倍，训练时间缩短2.53倍，超越所有基线，保持优越的图像质量。

## 🎯 应用场景

该研究在动态场景重建、虚拟现实、游戏开发等领域具有广泛的应用潜力。通过提高渲染效率和质量，SpeeDe3DGS能够支持更复杂的实时交互和视觉效果，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Dynamic extensions of 3D Gaussian Splatting (3DGS) achieve high-quality reconstructions through neural motion fields, but per-Gaussian neural inference makes these models computationally expensive. Building on DeformableGS, we introduce Speedy Deformable 3D Gaussian Splatting (SpeeDe3DGS), which bridges this efficiency-fidelity gap through three complementary modules: Temporal Sensitivity Pruning (TSP) removes low-impact Gaussians via temporally aggregated sensitivity analysis, Temporal Sensitivity Sampling (TSS) perturbs timestamps to suppress floaters and improve temporal coherence, and GroupFlow distills the learned deformation field into shared SE(3) transformations for efficient groupwise motion. On the 50 dynamic scenes in MonoDyGauBench, integrating TSP and TSS into DeformableGS accelerates rendering by 6.78$\times$ on average while maintaining neural-field fidelity and using 10$\times$ fewer primitives. Adding GroupFlow culminates in 13.71$\times$ faster rendering and 2.53$\times$ shorter training, surpassing all baselines in speed while preserving superior image quality.

