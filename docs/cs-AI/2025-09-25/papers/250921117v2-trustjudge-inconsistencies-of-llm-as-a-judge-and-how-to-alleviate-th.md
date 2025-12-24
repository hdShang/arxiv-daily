---
layout: default
title: "TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them"
---

# TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21117" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21117v2</a>
  <a href="https://arxiv.org/pdf/2509.21117.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21117v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21117v2', 'TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yidong Wang, Yunze Song, Tingyuan Zhu, Xuanwang Zhang, Zhuohao Yu, Hao Chen, Chiyu Song, Qiufeng Wang, Cunxiang Wang, Zhen Wu, Xinyu Dai, Yue Zhang, Wei Ye, Shikun Zhang

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-25 (更新: 2025-09-26)

**备注**: 22 pages, 9 figures, 6 tables

**🔗 代码/项目**: [GITHUB](https://github.com/TrustJudge/TrustJudge)

---

## 💡 一句话要点

**TrustJudge：提出概率框架，解决LLM评估中不一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM评估` `自动评估` `一致性` `概率框架` `传递性` `信息熵` `基准测试`

## 📋 核心要点

1. 现有LLM评估方法在评分比较和传递性上存在不一致性，导致评估结果不可靠，难以准确反映模型性能。
2. TrustJudge通过分布敏感评分和似然感知聚合，在概率框架下解决信息损失和平局判断模糊问题，提升评估一致性。
3. 实验表明，TrustJudge能显著降低评分比较和传递性不一致性，同时保持或提升评估准确性，无需额外训练或标注。

## 📝 摘要（中文）

将大型语言模型（LLM）用作自动评估器（LLM-as-a-judge）揭示了当前评估框架中存在的严重不一致性。我们发现了两种基本类型的不一致：（1）评分-比较不一致，即评分较低的回复在成对比较中优于评分较高的回复；（2）成对传递性不一致，表现为循环偏好链（A>B>C>A）和等价矛盾（A=B=C≠A）。我们认为这些问题源于离散评分系统中的信息丢失以及成对评估期间模糊的平局判断。我们提出了TrustJudge，这是一个概率框架，通过两个关键创新来解决这些限制：1）分布敏感评分，从离散评分概率计算连续期望，保留信息熵以实现更精确的评分；2）似然感知聚合，使用双向偏好概率或困惑度来解决传递性违规。我们还正式确定了当前LLM-as-a-judge框架的理论局限性，并展示了TrustJudge的组件如何克服这些局限性。当使用Llama-3.1-70B-Instruct作为评估模型，并使用我们的数据集进行评估时，TrustJudge将评分-比较不一致性降低了8.43%（从23.32%降至14.89%），将成对传递性不一致性降低了10.82%（从15.22%降至4.40%），同时保持了更高的评估准确性。我们的工作首次对LLM-as-a-judge范式中的评估框架不一致性进行了系统分析，为可靠的自动评估提供了理论见解和实际解决方案。该框架展示了各种模型架构和规模的一致改进，无需额外的训练或人工标注即可实现更值得信赖的LLM评估。代码可在https://github.com/TrustJudge/TrustJudge找到。

## 🔬 方法详解

**问题定义**：当前LLM作为评估器（LLM-as-a-judge）的方法存在两种主要的不一致性：评分-比较不一致性（Score-Comparison Inconsistency），即低评分的回复在两两比较中胜过高评分的回复；以及成对传递性不一致性（Pairwise Transitivity Inconsistency），表现为循环偏好（A>B>C>A）或等价矛盾（A=B=C≠A）。这些问题源于离散评分系统的信息损失以及两两比较中对平局判断的模糊性。

**核心思路**：TrustJudge的核心思路是通过概率框架来解决上述不一致性问题。它不再依赖于单一的离散评分，而是通过计算评分的概率分布来保留更多信息。同时，利用似然感知聚合来解决传递性违规，从而提高评估的一致性和可靠性。这样设计的目的是为了更准确地反映模型之间的真实优劣关系，避免因评分系统的局限性而产生误判。

**技术框架**：TrustJudge框架主要包含两个关键模块：分布敏感评分（Distribution-Sensitive Scoring）和似然感知聚合（Likelihood-Aware Aggregation）。首先，分布敏感评分模块将离散评分转化为评分概率分布，并从中计算连续期望，以保留更多信息熵。其次，似然感知聚合模块利用双向偏好概率或困惑度来解决传递性违规，确保评估结果的传递性。整个框架无需额外的训练或人工标注，可以直接应用于现有的LLM评估流程。

**关键创新**：TrustJudge的关键创新在于其概率框架，它通过分布敏感评分和似然感知聚合，有效地解决了传统LLM评估方法中存在的信息损失和平局判断模糊问题。与现有方法相比，TrustJudge不再依赖于单一的离散评分，而是利用评分的概率分布来保留更多信息，从而提高了评估的准确性和一致性。此外，似然感知聚合模块能够有效地解决传递性违规，确保评估结果的可靠性。

**关键设计**：在分布敏感评分模块中，关键在于如何将离散评分转化为评分概率分布。一种常见的方法是使用softmax函数，将评分转化为概率。在似然感知聚合模块中，关键在于如何利用双向偏好概率或困惑度来解决传递性违规。例如，可以使用最小化循环偏好链的损失函数来优化模型参数，从而确保评估结果的传递性。

## 📊 实验亮点

实验结果表明，TrustJudge在Llama-3.1-70B-Instruct作为评估模型时，评分-比较不一致性从23.32%降低到14.89%（降低8.43%），成对传递性不一致性从15.22%降低到4.40%（降低10.82%），同时保持了较高的评估准确性。这些结果表明TrustJudge能够显著提高LLM评估的一致性和可靠性。

## 🎯 应用场景

TrustJudge可广泛应用于LLM的自动评估和基准测试，尤其是在需要高可靠性和一致性的场景下。例如，在模型选择、性能监控和持续集成等环节，TrustJudge可以提供更准确、更可信的评估结果，帮助开发者更好地理解和改进LLM的性能。此外，该框架无需额外训练或标注，易于部署和使用，具有很高的实际应用价值。

## 📄 摘要（原文）

> The adoption of Large Language Models (LLMs) as automated evaluators (LLM-as-a-judge) has revealed critical inconsistencies in current evaluation frameworks. We identify two fundamental types of inconsistencies: (1) Score-Comparison Inconsistency, where lower-rated responses outperform higher-scored ones in pairwise comparisons, and (2) Pairwise Transitivity Inconsistency, manifested through circular preference chains (A>B>C>A) and equivalence contradictions (A=B=C\neq A). We argue that these issues come from information loss in discrete rating systems and ambiguous tie judgments during pairwise evaluation. We propose TrustJudge, a probabilistic framework that addresses these limitations through two key innovations: 1) distribution-sensitive scoring that computes continuous expectations from discrete rating probabilities, preserving information entropy for more precise scoring, and 2) likelihood-aware aggregation that resolves transitivity violations using bidirectional preference probabilities or perplexity. We also formalize the theoretical limitations of current LLM-as-a-judge frameworks and demonstrate how TrustJudge's components overcome them. When evaluated with Llama-3.1-70B-Instruct as judge using our dataset, TrustJudge reduces Score-Comparison inconsistency by 8.43% (from 23.32% to 14.89%) and Pairwise Transitivity inconsistency by 10.82% (from 15.22% to 4.40%), while maintaining higher evaluation accuracy. Our work provides the first systematic analysis of evaluation framework inconsistencies in LLM-as-a-judge paradigms, offering both theoretical insights and practical solutions for reliable automated assessment. The framework demonstrates consistent improvements across various model architectures and scales, enabling more trustworthy LLM evaluation without requiring additional training or human annotations. The codes can be found at https://github.com/TrustJudge/TrustJudge.

