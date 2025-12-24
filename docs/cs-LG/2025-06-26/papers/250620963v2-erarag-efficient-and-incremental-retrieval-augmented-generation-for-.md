---
layout: default
title: "EraRAG: Efficient and Incremental Retrieval Augmented Generation for Growing Corpora"
---

# EraRAG: Efficient and Incremental Retrieval Augmented Generation for Growing Corpora

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20963" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20963v2</a>
  <a href="https://arxiv.org/pdf/2506.20963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20963v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20963v2', 'EraRAG: Efficient and Incremental Retrieval Augmented Generation for Growing Corpora')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fangyuan Zhang, Zhengjun Huang, Yingli Zhou, Qintian Guo, Zhixun Li, Wensheng Luo, Di Jiang, Yixiang Fang, Xiaofang Zhou

**分类**: cs.IR, cs.LG

**发布日期**: 2025-06-26 (更新: 2025-07-04)

**备注**: Under review

**🔗 代码/项目**: [GITHUB](https://github.com/EverM0re/EraRAG-Official)

---

## 💡 一句话要点

**提出EraRAG以解决动态语料库更新效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图结构` `检索增强生成` `局部敏感哈希` `动态更新` `语言模型`

## 📋 核心要点

1. 现有的Graph-RAG方法假设语料库是静态的，导致在新文档到达时需要进行昂贵的全图重构，限制了可扩展性。
2. EraRAG通过多层次的图结构和局部敏感哈希（LSH）技术，实现了对动态更新的高效支持，避免了重训练和高成本的重新计算。
3. 实验结果显示，EraRAG在更新速度和令牌消耗上相比现有系统有显著提升，且在准确性上表现优越。

## 📝 摘要（中文）

基于图的检索增强生成（Graph-RAG）通过对外部语料库进行结构化检索来增强大型语言模型（LLMs）。然而，现有方法通常假设语料库是静态的，当新文档到达时需要昂贵的全图重构，限制了其在动态环境中的可扩展性。为了解决这些问题，我们提出了EraRAG，这是一种新颖的多层Graph-RAG框架，支持高效和可扩展的动态更新。我们的方法利用基于超平面的局部敏感哈希（LSH）将原始语料库分区并组织成层次图结构，使得在不干扰现有拓扑的情况下高效局部插入新数据。该设计消除了重新训练或高成本重新计算的需求，同时保持高检索准确性和低延迟。在大规模基准测试中的实验表明，EraRAG在更新时间和令牌消耗上比现有Graph-RAG系统减少了一个数量级，同时提供了更优的准确性表现。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有Graph-RAG方法在动态环境中更新语料库时的效率问题。现有方法需要全图重构，导致更新成本高，难以适应不断增长的语料库。

**核心思路**：EraRAG的核心思路是通过多层次的图结构和局部敏感哈希（LSH）技术，实现对新数据的高效局部插入，避免了全图重构的需求。这样的设计使得系统能够在不干扰现有拓扑的情况下，快速适应新文档的加入。

**技术框架**：EraRAG的整体架构包括数据分区、图结构构建和动态更新三个主要模块。首先，利用LSH对原始语料库进行分区，然后构建层次图结构，最后实现对新数据的高效插入。

**关键创新**：EraRAG的主要创新在于其多层次图结构和基于LSH的局部插入机制。这与现有方法的全图重构方式形成了本质区别，显著提高了更新效率。

**关键设计**：在设计中，EraRAG采用了超平面划分的LSH技术，确保了数据的高效组织和检索。此外，系统在参数设置上进行了优化，以平衡检索准确性和更新速度。

## 📊 实验亮点

实验结果表明，EraRAG在更新时间和令牌消耗上相比现有Graph-RAG系统减少了一个数量级，同时在检索准确性上表现出色，展示了其在动态环境中的优越性能。

## 🎯 应用场景

EraRAG的研究成果在需要频繁更新的动态语料库场景中具有广泛的应用潜力，如新闻推荐系统、实时信息检索和社交媒体分析等。其高效的更新机制能够显著提升系统的响应速度和用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Graph-based Retrieval-Augmented Generation (Graph-RAG) enhances large language models (LLMs) by structuring retrieval over an external corpus. However, existing approaches typically assume a static corpus, requiring expensive full-graph reconstruction whenever new documents arrive, limiting their scalability in dynamic, evolving environments. To address these limitations, we introduce EraRAG, a novel multi-layered Graph-RAG framework that supports efficient and scalable dynamic updates. Our method leverages hyperplane-based Locality-Sensitive Hashing (LSH) to partition and organize the original corpus into hierarchical graph structures, enabling efficient and localized insertions of new data without disrupting the existing topology. The design eliminates the need for retraining or costly recomputation while preserving high retrieval accuracy and low latency. Experiments on large-scale benchmarks demonstrate that EraRag achieves up to an order of magnitude reduction in update time and token consumption compared to existing Graph-RAG systems, while providing superior accuracy performance. This work offers a practical path forward for RAG systems that must operate over continually growing corpora, bridging the gap between retrieval efficiency and adaptability. Our code and data are available at https://github.com/EverM0re/EraRAG-Official.

