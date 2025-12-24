---
layout: default
title: "Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning"
---

# Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19598" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19598v1</a>
  <a href="https://arxiv.org/pdf/2508.19598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19598v1', 'Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiwei Li, Yong Hu, Wenqing Wang

**分类**: cs.LG

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出RLTR框架以解决LLM代理规划能力不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `行动规划` `工具使用奖励` `多目标优化`

## 📋 核心要点

1. 现有的端到端多目标优化方法在行动规划和答案总结之间存在优化目标分配不平衡的问题，且缺乏可验证的数据，限制了代理的规划能力提升。
2. 本文提出的RLTR框架通过解耦训练过程，专注于规划模块的单一目标优化，并引入基于工具使用完整性的奖励信号，直接评估工具调用序列的质量。
3. 实验结果显示，RLTR在规划性能上比现有的端到端基线提高了8%-12%，同时整体代理系统的最终响应质量也提升了5%-6%。

## 📝 摘要（中文）

大型语言模型（LLM）代理的功能主要由行动规划和答案总结两大能力决定。其中，行动规划是决定代理性能的核心能力。然而，现有的训练范式采用端到端的多目标优化，面临优化目标分配不平衡和可验证数据稀缺的挑战，难以提升代理的规划能力。为此，本文提出了一种新的框架——基于工具使用奖励的强化学习（RLTR），该框架解耦了训练过程，使规划模块能够专注于单一目标优化。RLTR引入了基于工具使用完整性的奖励信号，直接评估工具调用序列的质量，提供比最终响应内容更直接可靠的训练信号，从而避免了对可验证数据的需求。实验结果表明，RLTR在规划性能上比端到端基线提高了8%-12%，并且这种增强的规划能力也使整体代理系统的最终响应质量提高了5%-6%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型代理在行动规划能力上的不足，现有方法在多目标优化中面临目标分配不平衡和缺乏可验证数据的挑战。

**核心思路**：RLTR框架通过解耦训练过程，专注于规划模块的单一目标优化，利用工具使用完整性作为奖励信号，直接评估工具调用的质量，避免对最终响应内容的依赖。

**技术框架**：RLTR框架包括两个主要模块：规划模块和奖励评估模块。规划模块负责生成工具调用序列，而奖励评估模块则基于工具使用的完整性来评估这些序列的质量。

**关键创新**：RLTR的主要创新在于引入了基于工具使用完整性的奖励信号，这一设计使得训练信号更加直接和可靠，显著提升了规划能力，与传统的依赖最终响应内容的训练方法形成了本质区别。

**关键设计**：在RLTR中，奖励信号的设计是关键，具体包括如何量化工具使用的完整性，以及如何设置损失函数以优化规划模块的性能。

## 📊 实验亮点

实验结果表明，RLTR框架在规划性能上比端到端基线提高了8%-12%，同时整体代理系统的最终响应质量也提升了5%-6%。这一显著的性能提升展示了RLTR在优化LLM代理能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化决策系统和复杂任务的规划与执行等。通过提升LLM代理的规划能力，能够在多种场景中实现更高效的任务执行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The functionality of Large Language Model (LLM) agents is primarily determined by two capabilities: action planning and answer summarization. The former, action planning, is the core capability that dictates an agent's performance. However, prevailing training paradigms employ end-to-end, multi-objective optimization that jointly trains both capabilities. This paradigm faces two critical challenges: imbalanced optimization objective allocation and scarcity of verifiable data, making it difficult to enhance the agent's planning capability. To address these challenges, we propose Reinforcement Learning with Tool-use Rewards (RLTR), a novel framework that decouples the training process to enable a focused, single-objective optimization of the planning module. Crucially, RLTR introduces a reward signal based on tool-use completeness to directly evaluate the quality of tool invocation sequences. This method offers a more direct and reliable training signal than assessing the final response content, thereby obviating the need for verifiable data. Our experiments demonstrate that RLTR achieves an 8%-12% improvement in planning performance compared to end-to-end baselines. Moreover, this enhanced planning capability, in turn, translates to a 5%-6% increase in the final response quality of the overall agent system.

