---
layout: default
title: "E^2GraphRAG: Streamlining Graph-based RAG for High Efficiency and Effectiveness"
---

# E^2GraphRAG: Streamlining Graph-based RAG for High Efficiency and Effectiveness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24226" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24226v4</a>
  <a href="https://arxiv.org/pdf/2505.24226.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24226v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24226v4', 'E^2GraphRAG: Streamlining Graph-based RAG for High Efficiency and Effectiveness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yibo Zhao, Jiapeng Zhu, Ye Guo, Kangkang He, Xiang Li

**分类**: cs.AI

**发布日期**: 2025-05-30 (更新: 2025-06-06)

**备注**: 16 pages

---

## 💡 一句话要点

**提出E^2GraphRAG以解决图基RAG效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图基RAG` `知识检索` `实体图` `双向索引` `自适应检索` `效率提升` `问答系统`

## 📋 核心要点

1. 现有图基RAG方法效率低下，且依赖手动预定义的查询模式，限制了其实际应用。
2. E^2GraphRAG通过构建摘要树和实体图，利用双向索引和自适应检索策略来提升效率和有效性。
3. 实验结果显示，E^2GraphRAG在索引和检索速度上分别比GraphRAG快10倍和比LightRAG快100倍，同时保持了良好的问答性能。

## 📝 摘要（中文）

图基RAG方法如GraphRAG通过构建层次实体图展示了对知识库的全球理解，但常常面临效率低下和依赖手动预定义查询模式的问题，限制了实际应用。本文提出E^2GraphRAG，一个简化的图基RAG框架，旨在提高效率和有效性。在索引阶段，E^2GraphRAG利用大型语言模型构建摘要树，并基于文档块使用SpaCy构建实体图。随后，我们在实体和块之间构建双向索引，以捕捉它们的多对多关系，从而在局部和全局检索中实现快速查找。在检索阶段，我们设计了一种自适应检索策略，利用图结构在局部和全局模式之间进行检索和选择。实验表明，E^2GraphRAG在索引速度上比GraphRAG快10倍，在检索速度上比LightRAG快100倍，同时保持了竞争力的问答性能。

## 🔬 方法详解

**问题定义**：现有的图基RAG方法如GraphRAG在效率上存在明显不足，且依赖手动预定义的查询模式，导致其在实际应用中的灵活性和适用性受到限制。

**核心思路**：E^2GraphRAG通过构建摘要树和实体图，利用双向索引来捕捉实体与文档块之间的多对多关系，从而实现快速检索，解决了效率低下的问题。

**技术框架**：E^2GraphRAG的整体架构包括两个主要阶段：索引阶段和检索阶段。在索引阶段，利用大型语言模型构建摘要树，并使用SpaCy构建实体图；在检索阶段，设计自适应检索策略，利用图结构进行局部和全局检索。

**关键创新**：E^2GraphRAG的主要创新在于双向索引的构建和自适应检索策略的设计，这与传统方法的单向索引和固定查询模式形成了鲜明对比，显著提升了检索效率。

**关键设计**：在参数设置上，E^2GraphRAG优化了实体图的构建过程，并在索引和检索过程中引入了动态调整机制，以适应不同的查询需求和数据特征。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，E^2GraphRAG在索引速度上比GraphRAG快10倍，在检索速度上比LightRAG快100倍，同时在问答性能上保持了竞争力，展示了其在效率和有效性上的显著提升。

## 🎯 应用场景

E^2GraphRAG的研究成果在多个领域具有广泛的应用潜力，包括智能问答系统、信息检索、知识图谱构建等。其高效的检索能力和灵活的查询模式能够显著提升用户体验，推动相关技术的实际应用与发展。

## 📄 摘要（原文）

> Graph-based RAG methods like GraphRAG have shown promising global understanding of the knowledge base by constructing hierarchical entity graphs. However, they often suffer from inefficiency and rely on manually pre-defined query modes, limiting practical use. In this paper, we propose E^2GraphRAG, a streamlined graph-based RAG framework that improves both Efficiency and Effectiveness. During the indexing stage, E^2GraphRAG constructs a summary tree with large language models and an entity graph with SpaCy based on document chunks. We then construct bidirectional indexes between entities and chunks to capture their many-to-many relationships, enabling fast lookup during both local and global retrieval. For the retrieval stage, we design an adaptive retrieval strategy that leverages the graph structure to retrieve and select between local and global modes. Experiments show that E^2GraphRAG achieves up to 10 times faster indexing than GraphRAG and 100 times speedup over LightRAG in retrieval while maintaining competitive QA performance.

