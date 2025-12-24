---
layout: default
title: "MacRAG: Compress, Slice, and Scale-up for Multi-Scale Adaptive Context RAG"
---

# MacRAG: Compress, Slice, and Scale-up for Multi-Scale Adaptive Context RAG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06569" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06569v2</a>
  <a href="https://arxiv.org/pdf/2505.06569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06569v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06569v2', 'MacRAG: Compress, Slice, and Scale-up for Multi-Scale Adaptive Context RAG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Woosang Lim, Zekun Li, Gyuwan Kim, Sungyoung Ji, HyeonJung Kim, Kyuri Choi, Jin Hyuk Lim, Kyungpyo Park, William Yang Wang

**分类**: cs.CL, cs.AI, cs.IR, cs.LG

**发布日期**: 2025-05-10 (更新: 2025-05-20)

**🔗 代码/项目**: [GITHUB](https://github.com/Leezekun/MacRAG)

---

## 💡 一句话要点

**提出MacRAG以解决长上下文RAG系统的检索不精确问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文` `检索增强生成` `多尺度处理` `信息整合` `复杂推理`

## 📋 核心要点

1. 现有的RAG系统在检索精度、上下文覆盖和信息整合方面存在显著不足，限制了其在复杂任务中的应用。
2. MacRAG通过将文档分割为不同粒度的上下文，并自适应地合并相关信息，提供了一种新的解决方案以提升检索效果。
3. 在多个基准测试中，MacRAG在生成任务的表现上显著优于传统RAG方法，展示了其在长上下文处理中的优势。

## 📝 摘要（中文）

长上下文大语言模型（LC LLMs）结合检索增强生成（RAG）在复杂的多跳和大文档任务中具有强大潜力。然而，现有的RAG系统常常面临检索不精确、在受限窗口下上下文覆盖不完整以及信息碎片化等问题。为此，本文提出了多尺度自适应上下文RAG（MacRAG），该框架将文档压缩并分割为粗到细的粒度，然后通过实时的块级和文档级扩展自适应地合并相关上下文。MacRAG从最细粒度的检索开始，逐步引入更广泛的高层上下文，从而构建有效的查询特定长上下文，优化了精度和覆盖率。在HotpotQA、2WikiMultihopQA和Musique的LongBench扩展评估中，MacRAG在使用Llama-3.1-8B、Gemini-1.5-pro和GPT-4o的单步和多步生成任务中始终超越基线RAG管道。我们的结果确立了MacRAG作为现实世界长上下文多跳推理的高效可扩展解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG系统在长上下文任务中检索不精确和上下文覆盖不足的问题。现有方法在信息整合时常常导致信息碎片化，影响生成质量。

**核心思路**：MacRAG的核心思路是通过多尺度的上下文分割和自适应合并，逐步构建查询特定的长上下文。这种方法能够在检索初期聚焦于细粒度信息，随后扩展到更广泛的上下文，从而提高生成的准确性和全面性。

**技术框架**：MacRAG的整体架构包括三个主要模块：文档压缩与分割、上下文自适应合并和实时扩展。首先，将文档压缩为不同粒度的上下文，然后根据检索结果自适应地合并相关信息，最后进行实时的上下文扩展以满足生成需求。

**关键创新**：MacRAG的主要创新在于其多尺度自适应上下文合并机制，这与传统RAG方法的单一上下文处理方式形成鲜明对比。通过这种设计，MacRAG能够有效提升检索的精度和上下文的覆盖率。

**关键设计**：在参数设置上，MacRAG采用了动态调整的上下文窗口大小和自适应的检索策略，以优化信息的整合和生成效果。损失函数设计上，结合了检索精度和生成质量的综合考量，确保模型在训练过程中能够平衡这两方面的需求。

## 📊 实验亮点

在实验中，MacRAG在HotpotQA、2WikiMultihopQA和Musique的LongBench扩展上表现优异，使用Llama-3.1-8B、Gemini-1.5-pro和GPT-4o时，生成任务的性能均显著超过传统RAG基线，展示了其在单步和多步生成中的优势。

## 🎯 应用场景

MacRAG的研究成果在多个领域具有广泛的应用潜力，尤其是在需要处理长上下文和复杂推理的任务中，如法律文书分析、学术研究文献检索和智能问答系统等。其高效的上下文处理能力能够显著提升信息检索和生成的质量，为实际应用提供更强的支持。

## 📄 摘要（原文）

> Long-context large language models (LC LLMs) combined with retrieval-augmented generation (RAG) hold strong potential for complex multi-hop and large-document tasks. However, existing RAG systems often suffer from imprecise retrieval, incomplete context coverage under constrained windows, and fragmented information from suboptimal context construction. We introduce Multi-scale Adaptive Context RAG (MacRAG), a hierarchical RAG framework that compresses and partitions documents into coarse-to-fine granularities, then adaptively merges relevant contexts through real-time chunk- and document-level expansions. By initiating with finest-level retrieval and progressively incorporating broader, higher-level context, MacRAG constructs effective query-specific long contexts, optimizing both precision and coverage. Evaluations on challenging LongBench expansions of HotpotQA, 2WikiMultihopQA, and Musique confirm MacRAG consistently surpasses baseline RAG pipelines in single- and multi-step generation using Llama-3.1-8B, Gemini-1.5-pro, and GPT-4o. Our results establish MacRAG as an efficient, scalable solution for real-world long-context, multi-hop reasoning. Our code is available at https://github.com/Leezekun/MacRAG.

