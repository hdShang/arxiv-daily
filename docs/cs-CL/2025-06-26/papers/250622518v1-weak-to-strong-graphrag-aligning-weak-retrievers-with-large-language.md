---
layout: default
title: "Weak-to-Strong GraphRAG: Aligning Weak Retrievers with Large Language Models for Graph-based Retrieval Augmented Generation"
---

# Weak-to-Strong GraphRAG: Aligning Weak Retrievers with Large Language Models for Graph-based Retrieval Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22518" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22518v1</a>
  <a href="https://arxiv.org/pdf/2506.22518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22518v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22518v1', 'Weak-to-Strong GraphRAG: Aligning Weak Retrievers with Large Language Models for Graph-based Retrieval Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deyu Zou, Yongqiang Chen, Mufei Li, Siqi Miao, Chenxi Liu, Bo Han, James Cheng, Pan Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出Refined Graph-based RAG以解决弱检索器与大语言模型对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图检索` `知识图谱` `生成模型` `弱监督学习` `结构重组` `大语言模型` `信息检索`

## 📋 核心要点

1. 现有的基于图的RAG方法依赖于弱检索器，导致训练过程中引入虚假信号和检索结果的无序性。
2. 本文提出的ReG通过引入LLM反馈和结构感知重组模块，旨在提高检索结果的质量和逻辑性。
3. 实验表明，ReG在多个基准测试中显著提升性能，使用5%的训练数据即可达到最先进的效果，并在推理型LLMs中减少推理token成本30%。

## 📝 摘要（中文）

基于图的检索增强生成（RAG）使大语言模型（LLMs）能够利用最新知识图谱（KGs）中的结构化外部知识来增强响应的准确性并减少幻觉。然而，LLMs通常依赖于弱检索器，这导致了训练过程中引入虚假信号和检索结果的无序性。为了解决这些问题，本文提出了Refined Graph-based RAG（ReG），通过引入LLM反馈来消除虚假信号并改善监督质量。同时，ReG还引入了结构感知重组模块，将检索结果重构为逻辑连贯的证据链。实验结果表明，ReG在不同LLM基础上显著提升性能，最多可提高10%。

## 🔬 方法详解

**问题定义**：本文旨在解决弱检索器在基于图的RAG中引入虚假信号和检索结果无序性的问题。现有方法缺乏有效的监督，导致生成的响应质量下降。

**核心思路**：ReG通过结合LLM反馈来消除虚假信号，并引入结构感知重组模块，旨在提升检索结果的质量和逻辑连贯性。这样的设计使得生成的响应更加准确和可靠。

**技术框架**：ReG的整体架构包括两个主要模块：一是基于LLM的反馈机制，二是结构感知重组模块。前者用于优化检索器的输出，后者则负责将检索结果重构为逻辑连贯的证据链。

**关键创新**：ReG的主要创新在于将LLM反馈与结构感知重组相结合，这一方法显著改善了弱检索器的输出质量，与传统方法相比，能够更有效地消除虚假信号。

**关键设计**：在设计中，ReG采用了特定的损失函数来优化检索器的输出，并通过结构感知重组模块确保检索结果的逻辑性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，ReG在多个基准测试中显著提升了性能，最多可提高10%。此外，使用5%的训练数据即可达到最先进的效果，并且在推理型LLMs中，ReG能够减少推理token成本高达30%，同时提升性能4%。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和知识管理等。通过提高检索结果的质量和逻辑性，ReG能够为用户提供更准确的答案，进而提升用户体验。未来，该方法可能在多种需要实时知识更新的应用场景中发挥重要作用。

## 📄 摘要（原文）

> Graph-based retrieval-augmented generation (RAG) enables large language models (LLMs) to ground responses with structured external knowledge from up-to-date knowledge graphs (KGs) and reduce hallucinations. However, LLMs often rely on a weak retriever in graph-based RAG: I) Due to the lack of ground truth, the retriever is often trained on weak supervision, which often introduces spurious signals to the LLMs. II) Due to the abstraction of graph data, the retrieved knowledge is often presented in unorganized forms. To mitigate the issue, we present Refined Graph-based RAG (ReG) to align weak retrievers to LLMs for graph-based RAG. Specifically, ReG incorporates LLM feedback to get rid of spurious signals and improve the quality of the supervision. Meanwhile, ReG introduces a structure-aware reorganization module to refactor the retrieval results into logically coherent evidence chains. Experiments on prominent benchmarks demonstrate that ReG significantly and consistently brings improvements across different LLM backbones by up to 10%. The improved supervision quality enables ReG to match the state-of-the-art performance with 5% training data and to transfer to out-of-distribution KGs. Notably, when adopted to reasoning-based LLMs, ReG reduces the reasoning token cost by up to 30% and improves the performance by up to 4%.

