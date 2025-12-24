---
layout: default
title: SayCoNav: Utilizing Large Language Models for Adaptive Collaboration in Decentralized Multi-Robot Navigation
---

# SayCoNav: Utilizing Large Language Models for Adaptive Collaboration in Decentralized Multi-Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13729" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13729v1</a>
  <a href="https://arxiv.org/pdf/2505.13729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13729v1', 'SayCoNav: Utilizing Large Language Models for Adaptive Collaboration in Decentralized Multi-Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abhinav Rajvanshi, Pritish Sahu, Tixiao Shan, Karan Sikka, Han-Pang Chiu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出SayCoNav以解决多机器人自主导航中的协作问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多机器人系统` `自主导航` `协作策略` `大型语言模型` `动态适应性` `搜索效率` `信息共享`

## 📋 核心要点

1. 现有方法在多机器人协作导航中缺乏灵活性，难以适应不同机器人的技能和环境变化。
2. SayCoNav通过利用大型语言模型，自动生成适应性强的协作策略，使每个机器人能够独立生成计划并进行动态调整。
3. 实验结果显示，SayCoNav在多目标导航任务中相较于基线方法提高了最多44.28%的搜索效率，展现出良好的适应性。

## 📝 摘要（中文）

自适应协作对于一组自主机器人在大规模未知环境中执行复杂导航任务至关重要。有效的协作策略应根据每个机器人的技能和当前状态进行确定和调整，以成功实现共同目标。本文提出了SayCoNav，一种利用大型语言模型（LLMs）自动生成机器人团队协作策略的新方法。基于协作策略，每个机器人利用LLM以去中心化的方式生成其计划和行动。在导航过程中，机器人之间共享信息，并根据需要不断更新其逐步计划。我们在多目标导航任务上评估SayCoNav，实验结果表明，通过有效的协作，SayCoNav能够将搜索效率提高最多44.28%。

## 🔬 方法详解

**问题定义**：本文旨在解决多机器人在复杂导航任务中协作不足的问题。现有方法往往无法根据机器人个体的能力和环境变化进行有效调整，导致效率低下。

**核心思路**：SayCoNav的核心思想是利用大型语言模型（LLMs）自动生成协作策略，使每个机器人能够根据自身状态和环境动态生成行动计划，从而实现去中心化的协作。

**技术框架**：SayCoNav的整体架构包括信息共享模块、协作策略生成模块和计划执行模块。机器人通过信息共享模块获取其他机器人的状态信息，并利用LLM生成适应性计划。

**关键创新**：SayCoNav的主要创新在于将大型语言模型应用于多机器人协作导航中，能够实时生成和调整协作策略，显著提升了机器人之间的协作效率。

**关键设计**：在设计中，LLM的输入包括机器人的当前状态和环境信息，输出为具体的行动计划。损失函数设计为优化协作效率，确保机器人在执行任务时能够灵活应对变化。

## 📊 实验亮点

实验结果表明，SayCoNav在多目标导航任务中相较于基线方法提高了最多44.28%的搜索效率，展现出良好的适应性和协作能力。通过不同团队组合和条件的验证，证明了该方法的有效性和灵活性。

## 🎯 应用场景

SayCoNav的研究成果在多个领域具有广泛的应用潜力，包括智能物流、无人驾驶车队、搜索与救援等场景。通过提升多机器人系统的协作能力，能够有效提高任务执行效率，降低人力成本，推动自主机器人技术的实际应用。未来，该方法还可扩展至更复杂的多智能体系统中。

## 📄 摘要（原文）

> Adaptive collaboration is critical to a team of autonomous robots to perform complicated navigation tasks in large-scale unknown environments. An effective collaboration strategy should be determined and adapted according to each robot's skills and current status to successfully achieve the shared goal. We present SayCoNav, a new approach that leverages large language models (LLMs) for automatically generating this collaboration strategy among a team of robots. Building on the collaboration strategy, each robot uses the LLM to generate its plans and actions in a decentralized way. By sharing information to each other during navigation, each robot also continuously updates its step-by-step plans accordingly. We evaluate SayCoNav on Multi-Object Navigation (MultiON) tasks, that require the team of the robots to utilize their complementary strengths to efficiently search multiple different objects in unknown environments. By validating SayCoNav with varied team compositions and conditions against baseline methods, our experimental results show that SayCoNav can improve search efficiency by at most 44.28% through effective collaboration among heterogeneous robots. It can also dynamically adapt to the changing conditions during task execution.

