---
layout: default
title: "A New HOPE: Domain-agnostic Automatic Evaluation of Text Chunking"
---

# A New HOPE: Domain-agnostic Automatic Evaluation of Text Chunking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02171" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02171v1</a>
  <a href="https://arxiv.org/pdf/2505.02171.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02171v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02171v1', 'A New HOPE: Domain-agnostic Automatic Evaluation of Text Chunking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henrik Brådland, Morten Goodwin, Per-Arne Andersen, Alexander S. Nossum, Aditya Gupta

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-04

**备注**: 10 pages, To be published in SIGIR25

**DOI**: [10.1145/3726302.3729882](https://doi.org/10.1145/3726302.3729882)

---

## 💡 一句话要点

**提出HOPE评估方法以优化文本分块策略**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本分块` `检索增强生成` `自动评估` `段落属性` `语义独立性` `性能优化` `自然语言处理`

## 📋 核心要点

1. 现有方法缺乏分析不同文本分块策略对检索增强生成系统影响的框架，导致无法优化分块效果。
2. 本文提出HOPE评估方法，通过量化内在和外在段落属性以及段落一致性，提供领域无关的自动评估。
3. 实验证明，HOPE指标与RAG性能指标显著相关，段落语义独立性提升了系统的事实和答案正确性。

## 📝 摘要（中文）

文档分块在检索增强生成（RAG）中至关重要，因为它决定了源材料在索引前的分段方式。尽管已有证据表明大型语言模型（LLMs）对检索数据的布局和结构敏感，但目前尚无框架分析不同分块方法的影响。本文提出了一种新方法，定义了分块过程的基本特征，包括内在段落属性、外在段落属性和段落-文档一致性。我们提出的HOPE（整体段落评估）是一种领域无关的自动评估指标，量化并聚合这些特征。通过在七个领域的实证评估，HOPE指标与多种RAG性能指标显著相关，揭示了外在和内在段落属性的重要性差异。段落之间的语义独立性对系统性能至关重要，事实正确性提升高达56.2%，答案正确性提升21.1%。相反，传统的段落概念统一假设对性能影响甚微。这些发现为优化分块策略提供了可行的见解，从而改善RAG系统设计，生成更具事实正确性的响应。

## 🔬 方法详解

**问题定义**：本文旨在解决缺乏有效评估文本分块方法对RAG系统影响的问题。现有方法未能充分考虑段落的内在和外在属性，导致分块效果不佳。

**核心思路**：提出HOPE评估方法，通过定义和量化段落的内在属性、外在属性及其一致性，提供一种全面的评估框架，以优化文本分块策略。

**技术框架**：HOPE方法包括三个主要模块：1) 内在段落属性评估，2) 外在段落属性评估，3) 段落与文档一致性评估。每个模块通过特定的指标进行量化，最终整合为一个综合评分。

**关键创新**：HOPE方法的创新在于其领域无关性和全面性，能够同时考虑段落的多种属性，而传统方法往往只关注单一方面。

**关键设计**：在设计中，采用了多种量化指标来评估段落属性，如段落长度、信息密度等，并通过统计分析确保评估结果的可靠性。

## 📊 实验亮点

实验结果显示，HOPE指标与RAG性能指标显著相关，段落之间的语义独立性提升了系统的事实正确性高达56.2%，答案正确性提升21.1%。这些结果表明，优化分块策略对提升系统性能具有重要意义。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、自然语言处理和智能问答系统。通过优化文本分块策略，RAG系统能够生成更准确和可靠的响应，提升用户体验。未来，HOPE评估方法可扩展至其他文本处理任务，推动相关领域的发展。

## 📄 摘要（原文）

> Document chunking fundamentally impacts Retrieval-Augmented Generation (RAG) by determining how source materials are segmented before indexing. Despite evidence that Large Language Models (LLMs) are sensitive to the layout and structure of retrieved data, there is currently no framework to analyze the impact of different chunking methods. In this paper, we introduce a novel methodology that defines essential characteristics of the chunking process at three levels: intrinsic passage properties, extrinsic passage properties, and passages-document coherence. We propose HOPE (Holistic Passage Evaluation), a domain-agnostic, automatic evaluation metric that quantifies and aggregates these characteristics. Our empirical evaluations across seven domains demonstrate that the HOPE metric correlates significantly (p > 0.13) with various RAG performance indicators, revealing contrasts between the importance of extrinsic and intrinsic properties of passages. Semantic independence between passages proves essential for system performance with a performance gain of up to 56.2% in factual correctness and 21.1% in answer correctness. On the contrary, traditional assumptions about maintaining concept unity within passages show minimal impact. These findings provide actionable insights for optimizing chunking strategies, thus improving RAG system design to produce more factually correct responses.

