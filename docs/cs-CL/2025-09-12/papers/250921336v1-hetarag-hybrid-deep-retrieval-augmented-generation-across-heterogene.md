---
layout: default
title: "HetaRAG: Hybrid Deep Retrieval-Augmented Generation across Heterogeneous Data Stores"
---

# HetaRAG: Hybrid Deep Retrieval-Augmented Generation across Heterogeneous Data Stores

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21336" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21336v1</a>
  <a href="https://arxiv.org/pdf/2509.21336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21336v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21336v1', 'HetaRAG: Hybrid Deep Retrieval-Augmented Generation across Heterogeneous Data Stores')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guohang Yan, Yue Zhang, Pinlong Cai, Ding Wang, Song Mao, Hongwei Zhang, Yaoze Zhang, Hairong Zhang, Xinyu Cai, Botian Shi

**分类**: cs.IR, cs.CL

**发布日期**: 2025-09-12

**备注**: 15 pages, 4 figures

**🔗 代码/项目**: [GITHUB](https://github.com/KnowledgeXLab/HetaRAG)

---

## 💡 一句话要点

**HetaRAG：跨异构数据存储的混合深度检索增强生成框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `异构数据融合` `知识图谱` `向量数据库` `全文检索` `大型语言模型` `混合检索`

## 📋 核心要点

1. 现有RAG系统通常是文本单一模态，且依赖单一存储后端，如向量数据库，存在信息检索上的局限性。
2. HetaRAG提出了一种混合深度检索增强生成框架，旨在协同编排来自异构数据存储的跨模态证据，提升检索效果。
3. 论文进行了初步探索，构建了一个初始RAG管道，并开放了部分代码，为后续研究奠定了基础。

## 📝 摘要（中文）

检索增强生成（RAG）已成为缓解大型语言模型（LLM）知识幻觉和过时问题，同时保持数据安全的主要范式。通过从私有的、特定领域的语料库中检索相关证据，并将其注入到精心设计的提示中，RAG 可以在无需微调的巨大成本下提供可信的响应。传统的 RAG 系统仅限于文本，并且通常依赖于单一的存储后端，最常见的是向量数据库。实际上，这种单片设计存在不可避免的权衡：向量搜索捕获语义相似性，但丢失了全局上下文；知识图谱擅长关系精确性，但在召回率方面表现不佳；全文索引快速且精确，但在语义上是盲目的；而诸如 MySQL 之类的关系引擎提供强大的事务保证，但没有语义理解。我们认为这些异构检索范式是互补的，并提出了一种有原则的融合方案来协同编排它们，从而减轻任何单一模式的弱点。在这项工作中，我们介绍了 HetaRAG，一个混合的、深度检索增强生成框架，它协调来自异构数据存储的跨模态证据。我们计划设计一个系统，将向量索引、知识图谱、全文引擎和结构化数据库统一到一个单一的检索平面中，动态地路由和融合证据，以最大限度地提高召回率、精确度和上下文保真度。为了实现这一设计目标，我们进行了初步探索并构建了一个初始的 RAG 管道；本技术报告提供了一个简要概述。部分代码可在 https://github.com/KnowledgeXLab/HetaRAG 获得。

## 🔬 方法详解

**问题定义**：现有RAG系统在处理复杂知识检索时面临挑战。单一模态（如仅文本）和单一存储后端（如向量数据库）无法充分利用不同数据源的优势。向量数据库擅长语义相似性搜索，但缺乏全局上下文；知识图谱提供精确的关系信息，但召回率较低；全文索引快速但语义理解能力弱；关系数据库提供事务保证，但缺乏语义理解。因此，如何有效融合异构数据源的信息，提升RAG系统的检索质量是一个关键问题。

**核心思路**：HetaRAG的核心思想是将多种异构数据存储（向量索引、知识图谱、全文引擎、关系数据库）统一到一个检索平面中，利用它们各自的优势，实现互补。通过动态路由和融合来自不同数据源的证据，HetaRAG旨在最大化召回率、精确度和上下文保真度，从而提升RAG系统的整体性能。

**技术框架**：HetaRAG的整体架构包含以下主要模块：1) 异构数据存储层：包含向量索引、知识图谱、全文引擎和关系数据库等多种数据源；2) 检索层：负责从不同的数据源中检索相关信息；3) 融合层：将来自不同数据源的检索结果进行融合，生成最终的证据；4) 生成层：利用融合后的证据，结合大型语言模型生成最终的响应。具体的流程是：首先，接收到用户查询后，检索层根据查询的特点，选择合适的数据源进行检索；然后，融合层将来自不同数据源的检索结果进行融合；最后，生成层利用融合后的证据，生成最终的响应。

**关键创新**：HetaRAG的关键创新在于提出了一个混合的、深度检索增强生成框架，能够有效地融合来自异构数据存储的跨模态证据。与传统的RAG系统相比，HetaRAG不再局限于单一模态和单一存储后端，而是能够充分利用不同数据源的优势，从而提升检索质量和生成效果。

**关键设计**：由于是技术报告，论文没有详细描述关键设计细节。但从描述中可以推断，关键设计可能包括：1) 如何动态路由查询到不同的数据源；2) 如何设计融合策略，将来自不同数据源的检索结果进行有效融合；3) 如何优化检索和融合过程，以提高效率。

## 📊 实验亮点

该技术报告介绍了HetaRAG的初步探索和初始RAG管道的构建。虽然没有提供具体的性能数据，但其提出的混合检索增强生成框架，以及对异构数据源融合的思路，为RAG系统的发展提供了一个新的方向。开放的部分代码也为后续研究提供了便利。

## 🎯 应用场景

HetaRAG具有广泛的应用前景，可以应用于问答系统、智能客服、知识图谱构建等领域。通过融合异构数据源的信息，HetaRAG可以提供更全面、更准确的知识检索和生成能力，从而提升用户体验和工作效率。未来，HetaRAG有望成为企业级知识管理和智能应用的重要基础设施。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) has become a dominant paradigm for mitigating knowledge hallucination and staleness in large language models (LLMs) while preserving data security. By retrieving relevant evidence from private, domain-specific corpora and injecting it into carefully engineered prompts, RAG delivers trustworthy responses without the prohibitive cost of fine-tuning. Traditional retrieval-augmented generation (RAG) systems are text-only and often rely on a single storage backend, most commonly a vector database. In practice, this monolithic design suffers from unavoidable trade-offs: vector search captures semantic similarity yet loses global context; knowledge graphs excel at relational precision but struggle with recall; full-text indexes are fast and exact yet semantically blind; and relational engines such as MySQL provide strong transactional guarantees but no semantic understanding. We argue that these heterogeneous retrieval paradigms are complementary, and propose a principled fusion scheme to orchestrate them synergistically, mitigating the weaknesses of any single modality. In this work we introduce HetaRAG, a hybrid, deep-retrieval augmented generation framework that orchestrates cross-modal evidence from heterogeneous data stores. We plan to design a system that unifies vector indices, knowledge graphs, full-text engines, and structured databases into a single retrieval plane, dynamically routing and fusing evidence to maximize recall, precision, and contextual fidelity. To achieve this design goal, we carried out preliminary explorations and constructed an initial RAG pipeline; this technical report provides a brief overview. The partial code is available at https://github.com/KnowledgeXLab/HetaRAG.

