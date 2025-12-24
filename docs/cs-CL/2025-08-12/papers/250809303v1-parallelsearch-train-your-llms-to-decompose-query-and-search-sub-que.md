---
layout: default
title: "ParallelSearch: Train your LLMs to Decompose Query and Search Sub-queries in Parallel with Reinforcement Learning"
---

# ParallelSearch: Train your LLMs to Decompose Query and Search Sub-queries in Parallel with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09303" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09303v1</a>
  <a href="https://arxiv.org/pdf/2508.09303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09303v1', 'ParallelSearch: Train your LLMs to Decompose Query and Search Sub-queries in Parallel with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shu Zhao, Tan Yu, Anbang Xu, Japinder Singh, Aaditya Shukla, Rama Akkiraju

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出ParallelSearch以解决搜索查询的并行处理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `并行处理` `强化学习` `信息检索` `查询分解` `大型语言模型`

## 📋 核心要点

1. 现有方法在处理搜索查询时存在严格的顺序处理限制，导致计算效率低下，尤其是在需要多个实体比较的情况下。
2. 本文提出ParallelSearch框架，使大型语言模型能够识别并行化查询结构，支持同时执行多个搜索操作。
3. 实验结果显示，ParallelSearch在七个问答基准上平均提升2.9%的性能，在可并行化问题上提升12.7%，且减少了LLM调用次数。

## 📝 摘要（中文）

增强推理的搜索代理如Search-R1，通过可验证奖励的强化学习（RLVR）训练，展现了从外部知识源进行多步信息检索的卓越能力。然而，现有方法在处理搜索查询时存在严格的顺序处理限制，导致计算效率低下。为了解决这一问题，本文提出了ParallelSearch，一个新的强化学习框架，使大型语言模型（LLMs）能够识别可并行化的查询结构并同时执行多个搜索操作。实验结果表明，ParallelSearch在七个问答基准上平均提升了2.9%的性能，在可并行化问题上提升了12.7%，且仅需69.6%的LLM调用次数。

## 🔬 方法详解

**问题定义**：本文旨在解决现有搜索代理在处理查询时的顺序处理限制，导致计算效率低下的问题。现有方法无法有效利用查询中的并行性，影响了多步信息检索的性能。

**核心思路**：提出ParallelSearch框架，通过强化学习使LLMs能够识别并行化的查询结构，从而实现多个搜索操作的并行执行，提升信息检索效率。

**技术框架**：ParallelSearch的整体架构包括查询分解模块、并行搜索模块和奖励评估模块。查询分解模块负责识别独立的查询成分，并将其传递给并行搜索模块进行处理，最后通过奖励评估模块对结果进行评估和优化。

**关键创新**：本文的主要创新在于引入了专门的奖励函数，激励模型识别独立的查询组件，同时考虑答案的准确性、查询分解质量和并行执行的好处。这一设计使得模型能够在保持准确性的同时，提升处理效率。

**关键设计**：在模型训练中，设置了针对并行查询的损失函数，优化了查询分解的质量，并设计了适应并行执行的网络结构，以支持高效的信息检索。

## 📊 实验亮点

实验结果显示，ParallelSearch在七个问答基准上平均提升了2.9%的性能，尤其在可并行化问题上提升了12.7%。此外，相较于顺序方法，ParallelSearch仅需69.6%的LLM调用次数，显著提高了计算效率。

## 🎯 应用场景

该研究的潜在应用领域包括智能搜索引擎、问答系统和信息检索平台。通过提升查询处理效率，ParallelSearch能够在大规模数据环境中提供更快速和准确的响应，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Reasoning-augmented search agents such as Search-R1, trained via reinforcement learning with verifiable rewards (RLVR), demonstrate remarkable capabilities in multi-step information retrieval from external knowledge sources. These agents address the limitations of their parametric memory by dynamically gathering relevant facts to address complex reasoning tasks. However, existing approaches suffer from a fundamental architectural limitation: they process search queries strictly sequentially, even when handling inherently parallelizable and logically independent comparisons. This sequential bottleneck significantly constrains computational efficiency, particularly for queries that require multiple entity comparisons. To address this critical limitation, we propose ParallelSearch, a novel reinforcement learning framework that empowers large language models (LLMs) to recognize parallelizable query structures and execute multiple search operations concurrently. Our approach introduces dedicated reward functions that incentivize the identification of independent query components while preserving answer accuracy through jointly considering correctness, query decomposition quality, and parallel execution benefits. Comprehensive experiments demonstrate that ParallelSearch outperforms state-of-the-art baselines by an average performance gain of 2.9% across seven question-answering benchmarks. Notably, on parallelizable questions, our method achieves a 12.7% performance improvement while requiring only 69.6% of the LLM calls compared to sequential approaches.

