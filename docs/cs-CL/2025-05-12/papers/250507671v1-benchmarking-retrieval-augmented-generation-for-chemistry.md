---
layout: default
title: Benchmarking Retrieval-Augmented Generation for Chemistry
---

# Benchmarking Retrieval-Augmented Generation for Chemistry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07671" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07671v1</a>
  <a href="https://arxiv.org/pdf/2505.07671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07671v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07671v1', 'Benchmarking Retrieval-Augmented Generation for Chemistry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianrui Zhong, Bowen Jin, Siru Ouyang, Yanzhen Shen, Qiao Jin, Yin Fang, Zhiyong Lu, Jiawei Han

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出ChemRAG-Bench以评估化学领域的检索增强生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `化学领域` `大型语言模型` `评估基准` `知识整合` `工具包` `性能提升`

## 📋 核心要点

1. 现有方法在化学领域的应用受限于缺乏高质量的领域特定语料库和评估基准，导致RAG的潜力未能充分发挥。
2. 本文提出ChemRAG-Bench基准和ChemRAG-Toolkit工具包，旨在系统评估和提升RAG在化学任务中的表现。
3. 实验结果表明，RAG方法相较于直接推理方法平均提升17.4%，并提供了关于检索器架构和语料选择的深入分析。

## 📝 摘要（中文）

检索增强生成（RAG）已成为增强大型语言模型（LLMs）与外部知识结合的强大框架，尤其在需要专业和动态信息的科学领域。然而，RAG在化学领域的应用仍然未被充分探索，主要由于缺乏高质量的领域特定语料库和良好策划的评估基准。本文介绍了ChemRAG-Bench，这是一个全面的基准，旨在系统评估RAG在多样化化学相关任务中的有效性。所附的化学语料库整合了异构知识源，包括科学文献、PubChem数据库、PubMed摘要、教科书和维基百科条目。此外，我们还提出了ChemRAG-Toolkit，这是一个模块化和可扩展的RAG工具包，支持五种检索算法和八种LLMs。使用ChemRAG-Toolkit，我们展示了RAG在性能上显著提升，平均相对提高17.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决化学领域中检索增强生成（RAG）方法应用不足的问题，现有方法缺乏高质量的领域特定语料库和评估基准，限制了其有效性和可用性。

**核心思路**：通过引入ChemRAG-Bench基准和ChemRAG-Toolkit工具包，系统评估RAG在化学任务中的表现，整合多种异构知识源以增强模型的知识获取能力。

**技术框架**：整体架构包括ChemRAG-Bench基准和ChemRAG-Toolkit，前者用于评估RAG的有效性，后者支持多种检索算法和大型语言模型的集成。

**关键创新**：最重要的创新在于构建了一个专门针对化学领域的评估基准和工具包，填补了现有RAG应用中的空白，提供了系统化的评估方法。

**关键设计**：工具包支持五种检索算法和八种大型语言模型，设计上考虑了检索器架构、语料选择和检索段落数量等关键参数，以优化RAG的性能。

## 📊 实验亮点

实验结果显示，使用ChemRAG-Toolkit的RAG方法在性能上实现了平均17.4%的提升，相较于直接推理方法具有显著优势。这一结果表明，RAG在化学领域的应用潜力巨大，能够有效提升任务完成的准确性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括化学文献检索、药物发现、科学教育等。通过提供高效的知识检索和生成能力，ChemRAG-Bench和ChemRAG-Toolkit能够显著提升化学领域的研究效率和信息获取能力，推动相关领域的进一步发展。

## 📄 摘要（原文）

> Retrieval-augmented generation (RAG) has emerged as a powerful framework for enhancing large language models (LLMs) with external knowledge, particularly in scientific domains that demand specialized and dynamic information. Despite its promise, the application of RAG in the chemistry domain remains underexplored, primarily due to the lack of high-quality, domain-specific corpora and well-curated evaluation benchmarks. In this work, we introduce ChemRAG-Bench, a comprehensive benchmark designed to systematically assess the effectiveness of RAG across a diverse set of chemistry-related tasks. The accompanying chemistry corpus integrates heterogeneous knowledge sources, including scientific literature, the PubChem database, PubMed abstracts, textbooks, and Wikipedia entries. In addition, we present ChemRAG-Toolkit, a modular and extensible RAG toolkit that supports five retrieval algorithms and eight LLMs. Using ChemRAG-Toolkit, we demonstrate that RAG yields a substantial performance gain -- achieving an average relative improvement of 17.4% over direct inference methods. We further conduct in-depth analyses on retriever architectures, corpus selection, and the number of retrieved passages, culminating in practical recommendations to guide future research and deployment of RAG systems in the chemistry domain. The code and data is available at https://chemrag.github.io.

