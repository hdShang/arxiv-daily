---
layout: default
title: "jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval"
---

# jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18902" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18902v3</a>
  <a href="https://arxiv.org/pdf/2506.18902.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18902v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18902v3', 'jina-embeddings-v4: Universal Embeddings for Multimodal Multilingual Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Günther, Saba Sturua, Mohammad Kalim Akram, Isabelle Mohr, Andrei Ungureanu, Bo Wang, Sedigheh Eslami, Scott Martens, Maximilian Werk, Nan Wang, Han Xiao

**分类**: cs.AI, cs.CL, cs.IR

**发布日期**: 2025-06-23 (更新: 2025-07-07)

**备注**: 22 pages, 1-10 main, 14-22 experimental results, benchmark tables

---

## 💡 一句话要点

**提出jina-embeddings-v4以解决多模态多语言检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `低秩适配` `嵌入模型` `视觉内容处理` `信息检索` `语义相似性` `图像搜索`

## 📋 核心要点

1. 现有的多模态检索方法在处理视觉丰富内容时表现不佳，难以统一文本和图像的表示。
2. 论文提出了一种新型的多模态嵌入模型，通过低秩适配器优化不同检索任务的性能，支持多种嵌入形式。
3. 实验结果显示，jina-embeddings-v4在多模态检索任务上超越了现有方法，尤其在视觉内容处理上具有显著优势。

## 📝 摘要（中文）

我们介绍了jina-embeddings-v4，这是一个拥有38亿参数的多模态嵌入模型，通过一种新颖的架构统一文本和图像表示，支持单向量和多向量嵌入的后期交互风格。该模型结合了任务特定的低秩适配（LoRA）适配器，以优化在查询-文档检索、语义文本相似性和代码搜索等多种检索场景中的性能。全面评估表明，jina-embeddings-v4在单模态和跨模态检索任务上均达到了最先进的性能，尤其在处理表格、图表、图示和混合媒体格式等视觉丰富内容方面表现突出。为评估该能力，我们还引入了Jina-VDR，这是一个专门为视觉丰富图像检索设计的新基准。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态检索中统一文本与图像表示的挑战，现有方法在处理视觉丰富内容时效果不佳，难以满足实际应用需求。

**核心思路**：论文提出的jina-embeddings-v4模型通过创新的架构设计，结合低秩适配器（LoRA），实现了对多种检索任务的优化，能够有效处理文本和图像的多模态表示。

**技术框架**：该模型的整体架构包括嵌入层、LoRA适配器和后期交互模块，支持单向量和多向量的嵌入方式，能够灵活应对不同的检索需求。

**关键创新**：最重要的技术创新在于引入了低秩适配器，使得模型在不同任务中能够快速适应，显著提升了检索性能，尤其是在视觉内容的处理上。

**关键设计**：模型的参数设置包括38亿个参数，采用了特定的损失函数以优化检索效果，网络结构设计上注重了多模态信息的融合与交互。

## 📊 实验亮点

实验结果表明，jina-embeddings-v4在单模态和跨模态检索任务上均达到了最先进的性能，尤其在处理视觉丰富内容时，性能提升幅度超过了现有基线，展示了其在复杂检索场景中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、图像搜索、语义分析等，能够为多模态数据处理提供强大的支持。其实际价值在于提升了多语言和多模态检索的准确性和效率，未来可能在教育、医疗、金融等行业产生深远影响。

## 📄 摘要（原文）

> We introduce jina-embeddings-v4, a 3.8 billion parameter multimodal embedding model that unifies text and image representations through a novel architecture supporting both single-vector and multi-vector embeddings in the late interaction style. The model incorporates task-specific Low-Rank Adaptation (LoRA) adapters to optimize performance across diverse retrieval scenarios, including query-document retrieval, semantic text similarity, and code search. Comprehensive evaluations demonstrate that jina-embeddings-v4 achieves state-of-the-art performance on both single-modal and cross-modal retrieval tasks, with particular strength in processing visually rich content such as tables, charts, diagrams, and mixed-media formats. To facilitate evaluation of this capability, we also introduce Jina-VDR, a novel benchmark specifically designed for visually rich image retrieval.

