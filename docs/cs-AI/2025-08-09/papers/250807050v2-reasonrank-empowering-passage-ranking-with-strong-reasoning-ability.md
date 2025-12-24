---
layout: default
title: "ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability"
---

# ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07050" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07050v2</a>
  <a href="https://arxiv.org/pdf/2508.07050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07050v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07050v2', 'ReasonRank: Empowering Passage Ranking with Strong Reasoning Ability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhan Liu, Xinyu Ma, Weiwei Sun, Yutao Zhu, Yuchen Li, Dawei Yin, Zhicheng Dou

**分类**: cs.IR, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-09 (更新: 2025-08-22)

**备注**: 21 pages

**🔗 代码/项目**: [GITHUB](https://github.com/8421BCD/ReasonRank)

---

## 💡 一句话要点

**提出ReasonRank以解决复杂场景下的段落排名问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `段落排名` `推理模型` `强化学习` `数据合成` `信息检索`

## 📋 核心要点

1. 现有的推理密集型重排名方法在复杂场景中表现不佳，主要由于缺乏高质量的推理训练数据。
2. 本文提出了一种自动化的训练数据合成框架，并结合冷启动微调和强化学习的两阶段后训练方法，以增强重排名能力。
3. ReasonRank在BRIGHT基准测试中取得了40.6的最新性能，相较于现有基线显著提升，并且延迟更低。

## 📝 摘要（中文）

基于大型语言模型的列表排名在许多段落排名任务中表现优异。随着大型推理模型的发展，逐步推理在测试阶段有助于提高列表排名性能。然而，由于推理密集型训练数据的稀缺，现有的重排名方法在复杂排名场景中表现不佳。本文提出了一种自动化的推理密集型训练数据合成框架，并设计了自一致性数据过滤机制，以确保数据质量。此外，提出了两阶段的后训练方法，结合冷启动监督微调和强化学习，显著提升了重排名能力。实验结果表明，ReasonRank在BRIGHT基准测试中达到了40.6的最新性能，且延迟显著低于点对点重排名方法Rank1。

## 🔬 方法详解

**问题定义**：本文旨在解决推理密集型重排名方法在复杂场景中表现不佳的问题，现有方法因缺乏高质量训练数据而受到限制。

**核心思路**：提出一种自动化的训练数据合成框架，通过多领域的查询和段落生成高质量标签，并结合两阶段的后训练方法，提升重排名模型的推理能力。

**技术框架**：整体架构包括数据合成模块、自一致性数据过滤机制、冷启动监督微调阶段和强化学习阶段，确保模型在推理能力和排名性能上的提升。

**关键创新**：最重要的创新在于设计了多视角排名奖励机制，相较于传统的基于排名指标的奖励，更有效地提升了模型的排名能力。

**关键设计**：在冷启动阶段采用监督微调，强化学习阶段则利用多视角奖励机制，确保模型在推理和排名能力上均得到增强。

## 📊 实验亮点

ReasonRank在BRIGHT基准测试中达到了40.6的最新性能，相较于现有基线显著提升，且在延迟方面表现优于点对点重排名方法Rank1，显示出其在实际应用中的高效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、问答系统和推荐系统等，能够有效提升复杂查询场景下的段落排名质量。未来，ReasonRank有望在更广泛的自然语言处理任务中发挥重要作用，推动智能搜索和信息获取的进步。

## 📄 摘要（原文）

> Large Language Model (LLM) based listwise ranking has shown superior performance in many passage ranking tasks. With the development of Large Reasoning Models, many studies have demonstrated that step-by-step reasoning during test-time helps improve listwise ranking performance. However, due to the scarcity of reasoning-intensive training data, existing rerankers perform poorly in many complex ranking scenarios and the ranking ability of reasoning-intensive rerankers remains largely underdeveloped. In this paper, we first propose an automated reasoning-intensive training data synthesis framework, which sources training queries and passages from diverse domains and applies DeepSeek-R1 to generate high-quality training labels. A self-consistency data filtering mechanism is designed to ensure the data quality. To empower the listwise reranker with strong reasoning ability, we further propose a two-stage post-training approach, which includes a cold-start supervised fine-tuning (SFT) stage for reasoning pattern learning and a reinforcement learning (RL) stage for further ranking ability enhancement. During the RL stage, based on the nature of listwise ranking, we design a multi-view ranking reward, which is more effective than a ranking metric-based reward. Extensive experiments demonstrate that our trained reasoning-intensive reranker \textbf{ReasonRank} outperforms existing baselines significantly and also achieves much lower latency than pointwise reranker Rank1. \textbf{Through further experiments, our ReasonRank has achieved state-of-the-art (SOTA) performance 40.6 on the BRIGHT leaderboard\footnote{https://brightbenchmark.github.io/}.} Our codes are available at https://github.com/8421BCD/ReasonRank.

