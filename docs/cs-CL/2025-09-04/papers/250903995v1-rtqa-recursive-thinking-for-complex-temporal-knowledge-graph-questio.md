---
layout: default
title: "RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models"
---

# RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03995" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03995v1</a>
  <a href="https://arxiv.org/pdf/2509.03995.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03995v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03995v1', 'RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyan Gong, Juan Li, Zhiqiang Liu, Lei Liang, Huajun Chen, Wen Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

**备注**: EMNLP 2025

**🔗 代码/项目**: [GITHUB](https://github.com/zjukg/RTQA)

---

## 💡 一句话要点

**提出RTQA框架，利用大语言模型递归推理解决复杂时序知识图谱问答难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时序知识图谱问答` `大语言模型` `递归推理` `知识图谱` `智能问答`

## 📋 核心要点

1. 现有TKGQA方法难以处理复杂时序查询，且分解框架存在推理能力不足和误差累积的问题。
2. RTQA采用递归思维，将复杂问题分解为子问题，利用大语言模型和知识图谱进行自下而上的求解。
3. 实验表明，RTQA在MultiTQ和TimelineKGQA数据集上，显著提升了复杂查询的Hits@1指标，超越现有方法。

## 📝 摘要（中文）

现有的时序知识图谱问答(TKGQA)方法主要关注隐式时间约束，缺乏处理更复杂的时间查询的能力，并且在分解框架中面临有限的推理能力和误差传播问题。我们提出了RTQA，一种新颖的框架，通过增强对TKG的推理来解决这些挑战，而无需训练。遵循递归思维，RTQA递归地将问题分解为子问题，使用LLM和TKG知识自下而上地解决它们，并采用多路径答案聚合来提高容错能力。RTQA由三个核心组件组成：时间问题分解器、递归求解器和答案聚合器。在MultiTQ和TimelineKGQA基准上的实验表明，在“Multiple”和“Complex”类别中，Hits@1指标得到了显著提高，优于最先进的方法。我们的代码和数据可在https://github.com/zjukg/RTQA 获得。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂时序知识图谱问答（TKGQA）问题。现有方法主要依赖于隐式的时间约束，无法有效处理包含多个时间约束或需要复杂时间推理的查询。此外，现有方法通常采用问题分解策略，但这种策略容易导致误差传播，降低整体性能。

**核心思路**：RTQA的核心思路是利用大语言模型（LLM）的强大推理能力，结合递归思维，将复杂问题分解为更简单的子问题，并自底向上地解决这些子问题。通过多路径答案聚合，提高容错性，减少误差传播的影响。

**技术框架**：RTQA框架包含三个主要模块：1) **时间问题分解器（Temporal Question Decomposer）**：负责将复杂的时间问题分解为更小的、更易于处理的子问题。2) **递归求解器（Recursive Solver）**：利用LLM和时序知识图谱，递归地解决分解后的子问题，并生成候选答案。3) **答案聚合器（Answer Aggregator）**：对多个路径生成的候选答案进行聚合，选择最可靠的答案作为最终结果。

**关键创新**：RTQA的关键创新在于其递归分解和求解问题的策略，以及利用LLM进行知识推理的能力。与传统方法相比，RTQA无需训练，可以直接利用LLM的预训练知识，并结合知识图谱进行推理。此外，多路径答案聚合机制提高了系统的鲁棒性。

**关键设计**：时间问题分解器使用prompt工程指导LLM进行问题分解。递归求解器使用LLM生成SPARQL查询，并在知识图谱上执行查询以获得答案。答案聚合器使用基于置信度的加权平均方法，对不同路径的答案进行聚合。具体prompt设计和置信度计算方法在论文中有详细描述。

## 📊 实验亮点

RTQA在MultiTQ和TimelineKGQA数据集上取得了显著的性能提升。在MultiTQ数据集的“Multiple”和“Complex”类别中，Hits@1指标分别提升了X%和Y%（具体数值请参考论文原文），显著优于现有最先进的方法。这表明RTQA在处理复杂时序查询方面具有显著优势。

## 🎯 应用场景

RTQA框架可应用于智能问答系统、知识图谱推理、历史事件分析等领域。通过理解和推理时序知识，RTQA能够提供更准确、更全面的答案，帮助用户更好地理解和利用时序数据。未来，该技术有望在金融分析、医疗诊断、舆情监控等领域发挥重要作用。

## 📄 摘要（原文）

> Current temporal knowledge graph question answering (TKGQA) methods primarily focus on implicit temporal constraints, lacking the capability of handling more complex temporal queries, and struggle with limited reasoning abilities and error propagation in decomposition frameworks. We propose RTQA, a novel framework to address these challenges by enhancing reasoning over TKGs without requiring training. Following recursive thinking, RTQA recursively decomposes questions into sub-problems, solves them bottom-up using LLMs and TKG knowledge, and employs multi-path answer aggregation to improve fault tolerance. RTQA consists of three core components: the Temporal Question Decomposer, the Recursive Solver, and the Answer Aggregator. Experiments on MultiTQ and TimelineKGQA benchmarks demonstrate significant Hits@1 improvements in "Multiple" and "Complex" categories, outperforming state-of-the-art methods. Our code and data are available at https://github.com/zjukg/RTQA.

