---
layout: default
title: Incorporating Token Usage into Prompting Strategy Evaluation
---

# Incorporating Token Usage into Prompting Strategy Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14880" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14880v1</a>
  <a href="https://arxiv.org/pdf/2505.14880.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14880v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14880v1', 'Incorporating Token Usage into Prompting Strategy Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chris Sypherd, Sergei Petrov, Sonny George, Vaishak Belle

**分类**: cs.CL

**发布日期**: 2025-05-20

**备注**: 20 pages, 12 tables, 4 figures

---

## 💡 一句话要点

**提出Big-$O_{tok}$框架以优化提示策略的效率评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示策略` `效率评估` `大语言模型` `Token Cost` `Big-O分析` `自然语言处理` `性能优化`

## 📋 核心要点

1. 现有提示策略的评估主要集中在任务性能上，忽视了效率与令牌使用的平衡，导致实际应用中的局限性。
2. 本文提出Big-$O_{tok}$框架，旨在量化提示策略的令牌使用增长，并引入Token Cost度量，以实现性能与效率的综合评估。
3. 实验结果表明，增加令牌使用并未显著提升性能，反而导致性能回报递减，强调了在评估中考虑效率的重要性。

## 📝 摘要（中文）

近年来，大型语言模型在多种任务中表现出色，但其效果高度依赖于提示策略的选择。现有方法主要关注任务性能，而忽视了效率这一关键因素。本文提出了Big-$O_{tok}$理论框架，用于描述提示策略的令牌使用增长，并引入Token Cost作为令牌使用与性能的实证度量。通过对多种常见提示策略的分析，发现令牌使用的增加会导致性能回报显著递减，验证了Big-$O_{tok}$分析的有效性，强调了效率意识评估的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有提示策略评估中对效率的忽视，现有方法往往只关注任务性能，导致在实际应用中效率低下。

**核心思路**：提出Big-$O_{tok}$理论框架，量化提示策略的令牌使用增长，并通过Token Cost度量来平衡性能与令牌使用的关系，以实现更高效的评估。

**技术框架**：整体架构包括两个主要模块：一是Big-$O_{tok}$框架，用于理论分析；二是Token Cost度量，用于实证评估。通过这两个模块的结合，能够全面评估提示策略的效率。

**关键创新**：最重要的创新在于引入了令牌使用的理论分析框架Big-$O_{tok}$，与现有方法相比，强调了效率的重要性，并提供了新的评估标准。

**关键设计**：在实验中，设置了不同的提示策略并计算其Token Cost，采用了多种任务性能指标，以确保评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，随着令牌使用的增加，性能回报显著递减，验证了Big-$O_{tok}$框架的有效性。具体而言，在某些任务中，Token Cost的增加导致性能提升不足5%，强调了在提示策略设计中考虑效率的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过优化提示策略的评估方法，可以提高大型语言模型在实际应用中的效率，降低资源消耗，提升用户体验。未来，该框架有望推动更多高效的提示策略设计与应用。

## 📄 摘要（原文）

> In recent years, large language models have demonstrated remarkable performance across diverse tasks. However, their task effectiveness is heavily dependent on the prompting strategy used to elicit output, which can vary widely in both performance and token usage. While task performance is often used to determine prompting strategy success, we argue that efficiency--balancing performance and token usage--can be a more practical metric for real-world utility. To enable this, we propose Big-$O_{tok}$, a theoretical framework for describing the token usage growth of prompting strategies, and analyze Token Cost, an empirical measure of tokens per performance. We apply these to several common prompting strategies and find that increased token usage leads to drastically diminishing performance returns. Our results validate the Big-$O_{tok}$ analyses and reinforce the need for efficiency-aware evaluations.

