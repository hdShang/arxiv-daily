---
layout: default
title: "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch"
---

# BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22171" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22171v1</a>
  <a href="https://arxiv.org/pdf/2511.22171.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22171v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22171v1', 'BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pu Li, Wenhao Zhang, Weize Quan, Biao Zhang, Peter Wonka, Dong-Ming Yan

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**BrepGPT：基于Voronoi Half-Patch的单阶段自回归B-rep生成框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `B-rep生成` `CAD模型` `自回归模型` `Voronoi Half-Patch` `VQ-VAE`

## 📋 核心要点

1. 现有B-rep生成方法依赖多阶段网络，存在误差累积和计算效率低下的问题。
2. BrepGPT提出Voronoi Half-Patch (VHP)表示，将B-rep分解为统一的局部单元，简化编码。
3. 实验表明，BrepGPT在无条件B-rep生成上达到SOTA，并可应用于条件生成等任务。

## 📝 摘要（中文）

本文提出BrepGPT，一个用于B-rep（边界表示）生成的单阶段自回归框架。B-rep是现代工业设计中CAD模型表示的事实标准。由于B-rep结构中几何和拓扑元素之间复杂的耦合关系，现有的生成方法依赖于级联的多阶段网络，导致误差累积和计算效率低下。BrepGPT的关键创新在于Voronoi Half-Patch (VHP) 表示，它通过将几何信息分配给最近的半边并采样它们的下一个指针，将B-rep分解为统一的局部单元。与需要为不同结构级别进行多种不同编码的分层表示不同，VHP表示有助于在单个连贯的格式中统一几何属性和拓扑关系。此外，利用双VQ-VAE将顶点拓扑和Voronoi Half-Patch编码为基于顶点的token，实现更紧凑的序列编码。然后训练一个仅解码器的Transformer来自回归地预测这些token，这些token随后被映射到基于顶点的特征并解码为完整的B-rep模型。实验表明，BrepGPT在无条件B-rep生成方面取得了最先进的性能。该框架在各种应用中也表现出通用性，包括来自类别标签、点云、文本描述和图像的条件生成，以及B-rep自动补全和插值。

## 🔬 方法详解

**问题定义**：论文旨在解决CAD模型B-rep表示的生成问题。现有方法通常采用多阶段级联网络，这导致了误差累积，并且计算效率不高。B-rep结构中几何和拓扑元素之间存在复杂的耦合关系，使得单阶段生成具有挑战性。

**核心思路**：论文的核心思路是将B-rep分解为统一的局部单元，即Voronoi Half-Patch (VHP)。通过将几何信息分配给最近的半边并预测它们的下一个指针，VHP表示能够以一种紧凑且连贯的方式统一几何属性和拓扑关系。这种统一的表示方式使得可以使用单阶段自回归模型进行生成。

**技术框架**：BrepGPT框架包含以下主要模块：1) VHP表示：将B-rep分解为VHP单元。2) 双VQ-VAE编码器：将顶点拓扑和VHP编码为基于顶点的token。3) 解码器-Only Transformer：自回归地预测token序列。4) 解码器：将token序列解码为完整的B-rep模型。整个流程是一个端到端的训练过程。

**关键创新**：最重要的技术创新点在于Voronoi Half-Patch (VHP) 表示。与传统的层级表示方法不同，VHP表示能够将几何和拓扑信息统一编码，避免了多阶段编码带来的误差累积。此外，双VQ-VAE的使用进一步压缩了编码空间，提高了生成效率。

**关键设计**：论文使用了双VQ-VAE来编码顶点拓扑和Voronoi Half-Patches，具体结构未知。Transformer解码器用于自回归预测token序列，损失函数未知。VHP的采样策略和几何信息分配方式未知。

## 📊 实验亮点

BrepGPT在无条件B-rep生成方面取得了state-of-the-art的性能。此外，该框架还展示了在条件生成任务中的通用性，例如从类别标签、点云、文本描述和图像生成B-rep模型。这些实验结果表明BrepGPT具有强大的生成能力和广泛的应用潜力。具体的性能数据和对比基线未知。

## 🎯 应用场景

BrepGPT具有广泛的应用前景，包括CAD模型设计、逆向工程、游戏资产生成等。它可以用于自动生成各种形状的CAD模型，加速设计流程。此外，BrepGPT还可以应用于B-rep模型的自动补全和插值，提高模型的完整性和质量。该研究有望推动工业设计和计算机图形学领域的发展。

## 📄 摘要（原文）

> Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation.

