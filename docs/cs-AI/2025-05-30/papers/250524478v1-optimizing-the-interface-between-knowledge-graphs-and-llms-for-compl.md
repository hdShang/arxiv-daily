---
layout: default
title: Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning
---

# Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24478" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24478v1</a>
  <a href="https://arxiv.org/pdf/2505.24478.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24478v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24478v1', 'Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vasilije Markovic, Lazar Obradovic, Laszlo Hajdu, Jovan Pavlovic

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-30

**备注**: This is a preliminary version. A revised and expanded version is in preparation

---

## 💡 一句话要点

**优化知识图谱与大语言模型接口以提升复杂推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `大语言模型` `超参数优化` `复杂推理` `多跳问答` `Cognee框架` `性能提升`

## 📋 核心要点

1. 现有的知识图谱与大语言模型结合的系统在超参数优化方面研究不足，导致性能提升潜力未被充分挖掘。
2. 本文提出了一种系统的超参数优化方法，针对Cognee框架中的多个模块进行调优，以提升复杂推理任务的性能。
3. 实验结果显示，通过针对性调优可以显著提高性能，尽管不同数据集和评估指标的提升幅度存在差异。

## 📝 摘要（中文）

将大语言模型（LLMs）与知识图谱（KGs）结合，形成复杂系统，涉及众多超参数直接影响性能。然而，系统的超参数优化仍未得到充分探索。本文研究了Cognee框架中的超参数优化问题，使用三种多跳问答基准（HotPotQA、TwoWikiMultiHop和MuSiQue）优化与分块、图构建、检索和提示相关的参数。每种配置使用精确匹配、F1和DeepEval的LLM基于正确性指标进行评分。结果表明，通过有针对性的调优可以实现显著提升，尽管提升在不同数据集和指标间存在差异。这种变异性突显了调优的价值及标准评估措施的局限性。未来的进展不仅依赖于架构的改进，还需更清晰的优化和评估框架。

## 🔬 方法详解

**问题定义**：本文旨在解决知识图谱与大语言模型结合时超参数优化不足的问题。现有方法在复杂系统中缺乏系统的调优策略，导致性能提升不均衡。

**核心思路**：论文提出了一种系统化的超参数优化方法，针对Cognee框架的不同模块进行调优，旨在通过精细化的参数设置提升多跳问答的性能。

**技术框架**：整体架构包括知识图谱的构建、信息检索和问答生成三个主要模块。每个模块的超参数通过实验进行优化，以实现整体性能提升。

**关键创新**：最重要的创新点在于系统化的超参数调优策略，结合多种评估指标，能够在复杂系统中实现显著的性能提升，与传统方法相比，提供了更为全面的优化框架。

**关键设计**：在参数设置上，本文关注分块策略、图构建方法、检索机制和提示设计等关键因素，采用精确匹配、F1和DeepEval指标进行综合评估。通过这些设计，确保了优化过程的有效性和结果的可靠性。

## 📊 实验亮点

实验结果表明，通过针对性调优，性能提升显著。在HotPotQA、TwoWikiMultiHop和MuSiQue等基准上，优化后的模型在精确匹配和F1指标上均有明显改善，展示了超参数调优的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索和知识管理等。通过优化知识图谱与大语言模型的结合，可以提升复杂推理任务的准确性和效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Integrating Large Language Models (LLMs) with Knowledge Graphs (KGs) results in complex systems with numerous hyperparameters that directly affect performance. While such systems are increasingly common in retrieval-augmented generation, the role of systematic hyperparameter optimization remains underexplored. In this paper, we study this problem in the context of Cognee, a modular framework for end-to-end KG construction and retrieval. Using three multi-hop QA benchmarks (HotPotQA, TwoWikiMultiHop, and MuSiQue) we optimize parameters related to chunking, graph construction, retrieval, and prompting. Each configuration is scored using established metrics (exact match, F1, and DeepEval's LLM-based correctness metric). Our results demonstrate that meaningful gains can be achieved through targeted tuning. While the gains are consistent, they are not uniform, with performance varying across datasets and metrics. This variability highlights both the value of tuning and the limitations of standard evaluation measures. While demonstrating the immediate potential of hyperparameter tuning, we argue that future progress will depend not only on architectural advances but also on clearer frameworks for optimization and evaluation in complex, modular systems.

