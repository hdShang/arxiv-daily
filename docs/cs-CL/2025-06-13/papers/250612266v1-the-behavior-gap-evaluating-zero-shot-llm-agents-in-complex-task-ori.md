---
layout: default
title: "The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs"
---

# The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12266" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12266v1</a>
  <a href="https://arxiv.org/pdf/2506.12266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12266v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12266v1', 'The Behavior Gap: Evaluating Zero-shot LLM Agents in Complex Task-Oriented Dialogs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Avinash Baidya, Kamalika Das, Xiang Gao

**分类**: cs.CL, cs.AI, cs.HC, cs.LG

**发布日期**: 2025-06-13

**备注**: ACL 2025; 18 pages, 8 figures

---

## 💡 一句话要点

**提出全面评估框架以解决零-shot LLM代理在复杂任务对话中的行为差距问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `任务导向对话` `行为评估` `零-shot学习` `性能提升` `复杂任务` `对话系统`

## 📋 核心要点

1. 现有的LLM代理在复杂任务导向对话中表现不佳，尤其是在零-shot场景下，行为差距显著影响其性能。
2. 本研究提出了一种新的评估框架，旨在量化AI代理与人类专家之间的行为差距，重点分析对话行为和工具使用。
3. 实验结果表明，行为差距与任务复杂性高度相关，减少行为差距可显著提升LLM代理的整体性能，平均提升24.3%。

## 📝 摘要（中文）

基于大型语言模型（LLM）的代理在任务导向对话系统（TODS）中产生了显著影响，但在零-shot场景中仍面临性能挑战。尽管先前研究已指出这一性能差距，但驱动该差距的行为因素尚未得到充分探讨。本研究提出了一种全面的评估框架，以量化AI代理与人类专家之间的行为差距，重点关注对话行为、工具使用和知识利用的差异。研究发现，行为差距是影响LLM代理性能的关键因素，任务复杂性增加时，行为差距显著扩大，导致代理在复杂任务对话中的性能下降。即使是基于GPT-4o的代理，在最复杂的任务中也表现出与人类行为的低一致性。减少此类行为差距可显著提升性能，平均提升24.3%。

## 🔬 方法详解

**问题定义**：本研究旨在解决LLM代理在复杂任务导向对话中表现不佳的问题，尤其是在零-shot场景下的行为差距。现有方法未能充分探讨影响性能的行为因素，导致代理与人类专家之间存在显著差距。

**核心思路**：论文提出了一种全面的评估框架，通过量化AI代理与人类专家在对话行为、工具使用和知识利用方面的差异，来识别和分析行为差距的根源。

**技术框架**：整体架构包括数据收集、行为分析和性能评估三个主要模块。首先收集对话数据，然后对比分析AI代理与人类专家的行为，最后评估性能差异。

**关键创新**：本研究的创新点在于提出了量化行为差距的方法，强调了行为差距在LLM代理性能中的重要性，与现有方法相比，更加关注行为层面的分析。

**关键设计**：在评估过程中，采用了多种指标来衡量对话行为的F1分数、工具使用的有效性以及外部知识的利用情况，确保评估的全面性和准确性。具体参数设置和损失函数设计尚未详细披露。

## 📊 实验亮点

实验结果显示，随着任务复杂性的增加，行为差距的相关性高达0.963。在最复杂的任务中，基于GPT-4o的代理在对话行为的F1分数仅为0.464，工具使用的F1分数为0.139。通过减少行为差距，代理的性能平均提升了24.3%。

## 🎯 应用场景

该研究的评估框架可广泛应用于任务导向对话系统的开发与优化，特别是在需要处理复杂任务的场景中。通过减少行为差距，LLM代理的性能将得到显著提升，进而提高用户体验和系统效率。未来，该框架还可扩展至其他类型的对话系统和智能代理。

## 📄 摘要（原文）

> Large Language Model (LLM)-based agents have significantly impacted Task-Oriented Dialog Systems (TODS) but continue to face notable performance challenges, especially in zero-shot scenarios. While prior work has noted this performance gap, the behavioral factors driving the performance gap remain under-explored. This study proposes a comprehensive evaluation framework to quantify the behavior gap between AI agents and human experts, focusing on discrepancies in dialog acts, tool usage, and knowledge utilization. Our findings reveal that this behavior gap is a critical factor negatively impacting the performance of LLM agents. Notably, as task complexity increases, the behavior gap widens (correlation: 0.963), leading to a degradation of agent performance on complex task-oriented dialogs. For the most complex task in our study, even the GPT-4o-based agent exhibits low alignment with human behavior, with low F1 scores for dialog acts (0.464), excessive and often misaligned tool usage with a F1 score of 0.139, and ineffective usage of external knowledge. Reducing such behavior gaps leads to significant performance improvement (24.3% on average). This study highlights the importance of comprehensive behavioral evaluations and improved alignment strategies to enhance the effectiveness of LLM-based TODS in handling complex tasks.

