---
layout: default
title: "ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS"
---

# ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23734" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23734v4</a>
  <a href="https://arxiv.org/pdf/2505.23734.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23734v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23734v4', 'ZPressor: Bottleneck-Aware Compression for Scalable Feed-Forward 3DGS')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijie Wang, Donny Y. Chen, Zeyu Zhang, Duochao Shi, Akide Liu, Bohan Zhuang

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-11-17)

**备注**: NeurIPS 2025, Project Page: https://lhmd.top/zpressor, Code: https://github.com/ziplab/ZPressor

---

## 💡 一句话要点

**提出ZPressor以解决3D高斯点云模型的可扩展性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `视图合成` `信息瓶颈` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有的前馈3D高斯点云模型在处理大量输入视图时面临性能下降和内存消耗过大的挑战。
2. 论文提出ZPressor模块，通过信息瓶颈原则实现多视图输入的高效压缩，保留重要信息。
3. 实验结果表明，ZPressor在多个前馈3DGS模型中均能提升性能，并在密集视图设置下增强鲁棒性。

## 📝 摘要（中文）

近年来，前馈3D高斯点云（3DGS）模型作为新颖视图合成的有效解决方案，能够实现一次性推理而无需针对每个场景进行3DGS优化。然而，随着输入视图数量的增加，其模型的可扩展性受到限制，导致性能下降或内存消耗过大。本文通过信息瓶颈原则分析前馈3DGS框架，提出了一种轻量级的架构无关模块ZPressor，能够高效地将多视图输入压缩为紧凑的潜在状态Z，保留场景的关键信息并去除冗余。ZPressor使现有的前馈3DGS模型能够在80GB GPU上扩展到超过100个480P分辨率的输入视图，并在两个大型基准测试DL3DV-10K和RealEstate10K上显著提升性能和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决前馈3D高斯点云模型在处理大量输入视图时的可扩展性问题，现有方法在视图数量增加时会导致性能下降和内存消耗过大。

**核心思路**：ZPressor模块通过将输入视图划分为锚视图和支持视图，利用交叉注意力机制将支持视图的信息压缩到锚视图中，从而形成紧凑的潜在状态Z，保留关键信息并去除冗余。

**技术框架**：ZPressor的整体架构包括视图的划分、信息压缩和潜在状态的生成三个主要阶段。首先，将输入视图分为锚视图和支持视图；然后，通过交叉注意力机制进行信息压缩；最后，生成紧凑的潜在状态Z供后续模型使用。

**关键创新**：ZPressor的主要创新在于其轻量级架构和高效的信息压缩能力，使得前馈3DGS模型能够在不牺牲性能的情况下处理超过100个输入视图，这在现有方法中是前所未有的。

**关键设计**：在设计中，ZPressor采用了交叉注意力机制来实现信息的有效压缩，并在参数设置上进行了优化，以确保在80GB GPU上能够高效运行，同时保持480P分辨率的输入视图处理能力。

## 📊 实验亮点

在DL3DV-10K和RealEstate10K两个大型基准测试中，集成ZPressor的前馈3DGS模型在中等输入视图下性能显著提升，且在密集视图设置下表现出更强的鲁棒性，具体提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

ZPressor的研究成果在虚拟现实、增强现实和计算机图形学等领域具有广泛的应用潜力。通过提升3D视图合成的效率和质量，该技术可以为实时场景重建、游戏开发和影视制作等提供更强大的支持，推动相关领域的发展。

## 📄 摘要（原文）

> Feed-forward 3D Gaussian Splatting (3DGS) models have recently emerged as a promising solution for novel view synthesis, enabling one-pass inference without the need for per-scene 3DGS optimization. However, their scalability is fundamentally constrained by the limited capacity of their models, leading to degraded performance or excessive memory consumption as the number of input views increases. In this work, we analyze feed-forward 3DGS frameworks through the lens of the Information Bottleneck principle and introduce ZPressor, a lightweight architecture-agnostic module that enables efficient compression of multi-view inputs into a compact latent state $Z$ that retains essential scene information while discarding redundancy. Concretely, ZPressor enables existing feed-forward 3DGS models to scale to over 100 input views at 480P resolution on an 80GB GPU, by partitioning the views into anchor and support sets and using cross attention to compress the information from the support views into anchor views, forming the compressed latent state $Z$. We show that integrating ZPressor into several state-of-the-art feed-forward 3DGS models consistently improves performance under moderate input views and enhances robustness under dense view settings on two large-scale benchmarks DL3DV-10K and RealEstate10K. The video results, code and trained models are available on our project page: https://lhmd.top/zpressor.

