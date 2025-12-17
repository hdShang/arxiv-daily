---
layout: default
title: Mesh RAG: Retrieval Augmentation for Autoregressive Mesh Generation
---

# Mesh RAG: Retrieval Augmentation for Autoregressive Mesh Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16807" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16807v1</a>
  <a href="https://arxiv.org/pdf/2511.16807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16807v1" onclick="toggleFavorite(this, '2511.16807v1', 'Mesh RAG: Retrieval Augmentation for Autoregressive Mesh Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiatao Sun, Chen Liang, Qian Wang, Daniel Rakita

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**Mesh RAG：用于自回归网格生成的检索增强框架，提升质量与速度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `网格生成` `自回归模型` `检索增强` `点云处理` `三维重建`

## 📋 核心要点

1. 现有自回归网格生成模型依赖更大的模型或更长的序列来提高质量，导致生成时间过长，存在质量与速度的严重权衡。
2. Mesh RAG通过检索、生成和集成网格组件来增强生成过程，解耦了生成过程的顺序依赖性，实现了高效的并行推理。
3. 实验表明，Mesh RAG显著提高了网格质量，加快了生成速度，并支持增量编辑，且无需重新训练模型。

## 📝 摘要（中文）

本文提出Mesh RAG，一个新颖的、免训练的、即插即用的自回归网格生成模型框架。受语言模型RAG的启发，该方法通过利用点云分割、空间变换和点云配准来检索、生成和集成网格组件，从而增强生成过程。这种基于检索的方法将生成与严格的顺序依赖性解耦，从而促进高效且可并行化的推理。实验证明Mesh RAG在各种基础自回归网格生成模型中具有广泛的适用性，与顺序部件预测相比，它显著提高了网格质量，加快了生成速度，并实现了增量编辑，所有这些都不需要模型重新训练。

## 🔬 方法详解

**问题定义**：论文旨在解决自回归网格生成中质量与速度的权衡问题，以及顺序生成带来的增量编辑困难。现有方法依赖于扩大模型规模或增加序列长度来提升质量，导致生成速度显著下降，并且难以进行局部修改。

**核心思路**：核心思路是借鉴语言模型中的检索增强生成（RAG）思想，通过检索已有的网格部件来辅助生成过程，避免完全依赖自回归模型的顺序预测。这样可以将生成过程解耦，实现并行化，从而提高生成速度和支持增量编辑。

**技术框架**：Mesh RAG框架主要包含三个阶段：检索阶段、生成阶段和集成阶段。在检索阶段，利用点云分割、空间变换和点云配准等技术，从已有的网格部件库中检索出与当前需要生成的部件相似的部件。在生成阶段，利用检索到的部件作为先验信息，指导自回归模型生成新的网格部件。在集成阶段，将生成的网格部件与已有的网格进行融合，形成最终的完整网格。

**关键创新**：最重要的创新点在于将检索增强的思想引入到自回归网格生成中，打破了传统自回归模型的顺序依赖性，实现了并行化生成和增量编辑。与现有方法相比，Mesh RAG无需重新训练模型，即可显著提高生成质量和速度。

**关键设计**：Mesh RAG的关键设计包括：1) 使用点云分割技术将网格分解为部件；2) 使用空间变换和点云配准技术进行部件检索；3) 使用检索到的部件作为先验信息，指导自回归模型生成新的部件；4) 设计合适的融合策略，将生成的部件与已有网格进行无缝集成。具体的参数设置、损失函数和网络结构等细节取决于所使用的基础自回归网格生成模型。

## 📊 实验亮点

实验结果表明，Mesh RAG在多个自回归网格生成模型上均取得了显著的性能提升。与顺序部件预测相比，Mesh RAG显著提高了网格质量，加快了生成速度，并实现了增量编辑，且无需重新训练模型。具体的性能数据（例如，在特定指标上的提升幅度）在论文中进行了详细的展示。

## 🎯 应用场景

Mesh RAG在工业设计、游戏开发、仿真和机器人等领域具有广泛的应用前景。它可以加速3D模型的创建过程，降低人工成本，并提高模型的质量和多样性。此外，Mesh RAG的增量编辑能力使得用户可以方便地对现有模型进行修改和定制，满足个性化需求。未来，Mesh RAG有望成为3D内容创作的重要工具。

## 📄 摘要（原文）

> 3D meshes are a critical building block for applications ranging from industrial design and gaming to simulation and robotics. Traditionally, meshes are crafted manually by artists, a process that is time-intensive and difficult to scale. To automate and accelerate this asset creation, autoregressive models have emerged as a powerful paradigm for artistic mesh generation. However, current methods to enhance quality typically rely on larger models or longer sequences that result in longer generation time, and their inherent sequential nature imposes a severe quality-speed trade-off. This sequential dependency also significantly complicates incremental editing. To overcome these limitations, we propose Mesh RAG, a novel, training-free, plug-and-play framework for autoregressive mesh generation models. Inspired by RAG for language models, our approach augments the generation process by leveraging point cloud segmentation, spatial transformation, and point cloud registration to retrieve, generate, and integrate mesh components. This retrieval-based approach decouples generation from its strict sequential dependency, facilitating efficient and parallelizable inference. We demonstrate the wide applicability of Mesh RAG across various foundational autoregressive mesh generation models, showing it significantly enhances mesh quality, accelerates generation speed compared to sequential part prediction, and enables incremental editing, all without model retraining.

