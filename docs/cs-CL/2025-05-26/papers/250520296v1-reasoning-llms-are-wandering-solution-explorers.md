---
layout: default
title: Reasoning LLMs are Wandering Solution Explorers
---

# Reasoning LLMs are Wandering Solution Explorers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20296" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20296v1</a>
  <a href="https://arxiv.org/pdf/2505.20296.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20296v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20296v1', 'Reasoning LLMs are Wandering Solution Explorers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Lu, Ziwei Xu, Mohan Kankanhalli

**分类**: cs.CL, cs.AI, cs.LG, cs.MM

**发布日期**: 2025-05-26

**备注**: 71 pages, 14 figures, 2 tables

---

## 💡 一句话要点

**提出系统性问题解决框架以提升推理LLM的探索能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理LLM` `系统性问题解决` `解空间探索` `评估框架` `性能分析`

## 📋 核心要点

1. 现有推理LLM在系统性探索解空间方面存在显著不足，导致推理过程中的无效步骤和冗余探索。
2. 论文提出了一种新的评估框架，强调系统性问题解决的重要性，并建议关注推理过程的结构。
3. 通过对多种LLM的分析，发现其在复杂任务中的表现显著下降，呼吁改进评估标准以反映真实推理能力。

## 📝 摘要（中文）

大型语言模型（LLMs）通过链式思维提示和树状推理等测试时计算（TTC）技术展现了出色的推理能力。然而，本文指出现有的推理LLM（RLLMs）在系统性探索解空间方面存在不足。我们形式化了系统性问题解决的定义，并识别了常见的失败模式，揭示了推理LLM更像是游荡者而非系统性探索者。通过对多种最先进LLM的定性和定量分析，我们发现了持续存在的问题，如无效的推理步骤、冗余的探索、幻觉或不真实的结论等。我们的研究表明，当前模型在简单任务上的表现看似优秀，但随着复杂度的增加，性能急剧下降。基于这些发现，我们倡导新的评估指标和工具，不仅评估最终输出，还要关注推理过程的结构。

## 🔬 方法详解

**问题定义**：本文旨在解决推理LLM在系统性问题解决中的不足，特别是它们在解空间探索时的无效和冗余行为。现有方法缺乏对推理过程的深入分析，导致在复杂任务中表现不佳。

**核心思路**：论文的核心思路是形式化系统性问题解决的概念，并通过定性和定量分析识别推理LLM的常见失败模式，以此为基础提出新的评估标准。

**技术框架**：整体架构包括对多种LLM的分析，分为定性分析和定量评估两个主要模块，分别关注推理步骤的有效性和结果的可靠性。

**关键创新**：最重要的技术创新在于提出了一种新的评估框架，强调推理过程的结构性，而不仅仅是最终输出的质量。这与传统方法的评估方式有本质区别。

**关键设计**：在实验中，采用了多种评估指标来量化推理过程的有效性，包括推理步骤的有效性、冗余探索的频率等，确保全面反映模型的推理能力。

## 📊 实验亮点

实验结果显示，当前推理LLM在简单任务上表现良好，但在复杂任务中的性能下降幅度可达50%以上。通过新的评估框架，能够更准确地识别模型的推理缺陷，为未来的研究提供了重要的方向。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化问答系统和复杂决策支持系统。通过提升推理LLM的系统性探索能力，可以在更复杂的任务中实现更高的准确性和可靠性，从而为实际应用提供更强的支持。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated impressive reasoning abilities through test-time computation (TTC) techniques such as chain-of-thought prompting and tree-based reasoning. However, we argue that current reasoning LLMs (RLLMs) lack the ability to systematically explore the solution space. This paper formalizes what constitutes systematic problem solving and identifies common failure modes that reveal reasoning LLMs to be wanderers rather than systematic explorers. Through qualitative and quantitative analysis across multiple state-of-the-art LLMs, we uncover persistent issues: invalid reasoning steps, redundant explorations, hallucinated or unfaithful conclusions, and so on. Our findings suggest that current models' performance can appear to be competent on simple tasks yet degrade sharply as complexity increases. Based on the findings, we advocate for new metrics and tools that evaluate not just final outputs but the structure of the reasoning process itself.

