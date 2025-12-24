---
layout: default
title: Scaling Point-based Differentiable Rendering for Large-scale Reconstruction
---

# Scaling Point-based Differentiable Rendering for Large-scale Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20017" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20017v1</a>
  <a href="https://arxiv.org/pdf/2512.20017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20017v1', 'Scaling Point-based Differentiable Rendering for Large-scale Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hexu Zhao, Xiaoteng Liu, Xiwen Min, Jianhao Huang, Youming Deng, Yanfei Li, Ang Li, Jinyang Li, Aurojit Panda

**分类**: cs.DC, cs.GR

**发布日期**: 2025-12-23

**备注**: 13 pages main text, plus appendix

---

## 💡 一句话要点

**Gaian：面向大规模重建，可扩展的基于点的可微渲染通用分布式训练系统**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `可微渲染` `分布式训练` `点云重建` `数据局部性` `大规模场景`

## 📋 核心要点

1. 现有PBDR系统难以扩展到高分辨率和大型场景，且与特定方法耦合，数据局部性差导致通信开销大。
2. Gaian通过统一API支持多种PBDR方法，并利用数据访问信息优化局部性，从而减少通信。
3. 实验表明，Gaian在多个数据集和GPU配置下，显著降低通信量并提升训练吞吐量。

## 📝 摘要（中文）

基于点的可微渲染(PBDR)能够实现高保真3D场景重建，但将PBDR扩展到高分辨率和大型场景需要高效的分布式训练系统。现有的系统与特定的PBDR方法紧密耦合，并且由于较差的数据局部性而遭受严重的通信开销。本文提出Gaian，一个通用的PBDR分布式训练系统。Gaian提供了一个统一的API，该API具有足够的表达能力来支持现有的PBDR方法，同时暴露了丰富的数据访问信息，Gaian利用这些信息来优化局部性并减少通信。通过实现4种PBDR算法来评估Gaian。我们的实现实现了高性能和资源效率：在六个数据集和高达128个GPU上，它减少了高达91%的通信，并将训练吞吐量提高了1.50倍-3.71倍。

## 🔬 方法详解

**问题定义**：论文旨在解决基于点的可微渲染（PBDR）在大规模场景重建中面临的扩展性问题。现有PBDR系统通常与特定算法紧密耦合，缺乏通用性。此外，由于数据局部性差，分布式训练过程中存在大量的通信开销，严重限制了训练效率。

**核心思路**：Gaian的核心思路是设计一个通用的分布式训练系统，通过统一的API支持多种PBDR算法，并利用数据访问信息优化数据局部性，从而减少通信开销。这种解耦的设计使得系统更具灵活性和可扩展性。

**技术框架**：Gaian系统包含一个统一的API，用于描述不同的PBDR算法。该API暴露了丰富的数据访问信息，例如哪些点需要被哪些GPU访问。Gaian利用这些信息进行数据划分和任务调度，以最大化数据局部性。系统还包含一个通信优化模块，用于减少GPU之间的通信量。

**关键创新**：Gaian的关键创新在于其通用性和数据局部性优化。通过统一的API，Gaian可以支持多种PBDR算法，而无需为每种算法单独设计分布式训练系统。通过利用数据访问信息优化数据局部性，Gaian可以显著减少通信开销，提高训练效率。

**关键设计**：Gaian的API设计允许用户指定点云数据的划分方式和渲染过程中的数据依赖关系。系统使用一种基于图的优化算法来确定最佳的数据划分方案，以最大化数据局部性。通信优化模块使用诸如梯度累积和异步通信等技术来进一步减少通信开销。损失函数和网络结构取决于具体的PBDR算法，Gaian提供了一个灵活的框架来支持不同的选择。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20017v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20017v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20017v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Gaian在六个数据集和高达128个GPU上，相比现有系统，减少了高达91%的通信量，并将训练吞吐量提高了1.50倍-3.71倍。这些结果验证了Gaian的有效性和优越性，表明其能够显著提高大规模PBDR的训练效率。

## 🎯 应用场景

Gaian可应用于大规模3D场景重建，例如城市建模、自动驾驶、虚拟现实等领域。通过提高PBDR的训练效率，Gaian能够加速这些应用的发展，并降低计算成本。未来，Gaian可以进一步扩展到支持其他类型的可微渲染算法，并应用于更广泛的计算机视觉和图形学任务。

## 📄 摘要（原文）

> Point-based Differentiable Rendering (PBDR) enables high-fidelity 3D scene reconstruction, but scaling PBDR to high-resolution and large scenes requires efficient distributed training systems. Existing systems are tightly coupled to a specific PBDR method. And they suffer from severe communication overhead due to poor data locality. In this paper, we present Gaian, a general distributed training system for PBDR. Gaian provides a unified API expressive enough to support existing PBDR methods, while exposing rich data-access information, which Gaian leverages to optimize locality and reduce communication. We evaluated Gaian by implementing 4 PBDR algorithms. Our implementations achieve high performance and resource efficiency: across six datasets and up to 128 GPUs, it reduces communication by up to 91% and improves training throughput by 1.50x-3.71x.

