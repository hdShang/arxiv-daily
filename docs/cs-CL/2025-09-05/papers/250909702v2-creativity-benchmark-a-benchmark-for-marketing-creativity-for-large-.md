---
layout: default
title: "Creativity Benchmark: A benchmark for marketing creativity for large language models"
---

# Creativity Benchmark: A benchmark for marketing creativity for large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09702" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09702v2</a>
  <a href="https://arxiv.org/pdf/2509.09702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09702v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09702v2', 'Creativity Benchmark: A benchmark for marketing creativity for large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ninad Bhat, Kieran Browne, Pip Bingemann

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-09-05 (更新: 2025-10-19)

**备注**: 30 Pages, 14 figures. Fixed typos

---

## 💡 一句话要点

**提出创意基准以评估大型语言模型的市场创意能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `市场创意` `评估框架` `人类评估` `模型多样性` `创意生成`

## 📋 核心要点

1. 现有方法在评估大型语言模型的市场创意能力时，缺乏有效的标准化框架，导致评估结果不一致。
2. 论文提出了创意基准，通过对多个品牌和不同提示类型的系统评估，提供了一个全面的评估工具。
3. 实验结果表明，模型之间的性能差异微小，且自动评估与人类评估之间存在显著偏差，强调了人类评估的重要性。

## 📝 摘要（中文）

我们介绍了创意基准，这是一个用于评估大型语言模型（LLMs）在市场创意方面的框架。该基准涵盖100个品牌（12个类别）和三种提示类型（洞察、创意、狂野创意）。通过对678名从业创意者进行的11,012次匿名比较的人类成对偏好分析，采用Bradley-Terry模型，显示出模型性能紧密聚集，没有模型在品牌或提示类型上占据主导地位：最高与最低模型的胜率差异约为0.45，意味着头对头胜率为0.61；最高评分模型仅在约61%的情况下击败最低评分模型。我们还使用余弦距离分析模型多样性，以捕捉模型内部和外部的变化及对提示重构的敏感性。与人类排名的三种LLM评估设置比较显示出弱且不一致的相关性和评估者特定的偏见，强调了自动评估者无法替代人类评估的必要性。传统创意测试在品牌约束任务中也仅部分转移。总体结果强调了专家人类评估和关注多样性的工作流程的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有大型语言模型在市场创意评估中的标准化不足，现有方法无法有效区分模型性能，导致评估结果不可靠。

**核心思路**：论文的核心思路是构建一个系统的评估框架，涵盖多种品牌和提示类型，通过人类评估者的偏好来量化模型的创意能力。

**技术框架**：整体架构包括三个主要模块：品牌选择、提示类型设计和人类评估。首先选择100个品牌，设计三种提示类型，然后通过人类评估者进行成对比较。

**关键创新**：最重要的技术创新点在于引入了多样性分析和人类评估的结合，强调了模型性能的细微差异和人类评估的不可替代性。与现有方法相比，提供了更为全面和细致的评估视角。

**关键设计**：在实验中，使用Bradley-Terry模型分析人类偏好，设置了多种提示类型，并采用余弦距离来评估模型之间的多样性和敏感性。

## 📊 实验亮点

实验结果显示，模型之间的性能差异微小，最高评分模型在约61%的情况下优于最低评分模型，表明模型在创意生成上的竞争力相对接近。此外，自动评估与人类评估之间的相关性较弱，强调了人类评估的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括市场营销、广告创意生成和品牌策略制定。通过提供一个标准化的评估框架，企业可以更有效地利用大型语言模型来生成创意内容，从而提升市场竞争力。未来，该框架还可能扩展到其他创意领域，如艺术创作和内容生成。

## 📄 摘要（原文）

> We introduce Creativity Benchmark, an evaluation framework for large language models (LLMs) in marketing creativity. The benchmark covers 100 brands (12 categories) and three prompt types (Insights, Ideas, Wild Ideas). Human pairwise preferences from 678 practising creatives over 11,012 anonymised comparisons, analysed with Bradley-Terry models, show tightly clustered performance with no model dominating across brands or prompt types: the top-bottom spread is $Δθ\approx 0.45$, which implies a head-to-head win probability of $0.61$; the highest-rated model beats the lowest only about $61\%$ of the time. We also analyse model diversity using cosine distances to capture intra- and inter-model variation and sensitivity to prompt reframing. Comparing three LLM-as-judge setups with human rankings reveals weak, inconsistent correlations and judge-specific biases, underscoring that automated judges cannot substitute for human evaluation. Conventional creativity tests also transfer only partially to brand-constrained tasks. Overall, the results highlight the need for expert human evaluation and diversity-aware workflows.

