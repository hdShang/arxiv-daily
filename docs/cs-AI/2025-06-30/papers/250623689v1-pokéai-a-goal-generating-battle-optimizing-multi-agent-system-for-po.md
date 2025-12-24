---
layout: default
title: "PokéAI: A Goal-Generating, Battle-Optimizing Multi-agent System for Pokemon Red"
---

# PokéAI: A Goal-Generating, Battle-Optimizing Multi-agent System for Pokemon Red

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23689" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23689v1</a>
  <a href="https://arxiv.org/pdf/2506.23689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23689v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23689v1', 'PokéAI: A Goal-Generating, Battle-Optimizing Multi-agent System for Pokemon Red')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Liu, Xinhang Sui, Yueran Song, Siwen Wang

**分类**: cs.AI, cs.MA

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出PokéAI以解决宝可梦红版游戏中的自主决策问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `自主决策` `游戏AI` `宝可梦` `战斗优化` `语言模型` `策略推理`

## 📋 核心要点

1. 现有的游戏AI系统通常缺乏自主决策能力，难以在复杂环境中有效应对多变的游戏情境。
2. PokéAI通过引入三个专门的智能体，形成闭环决策系统，能够自主生成任务并执行，从而提升游戏表现。
3. 实验结果表明，PokéAI的战斗模块在战斗中取得了80.8%的胜率，接近人类玩家的表现，且不同模型展现出独特的游戏风格。

## 📝 摘要（中文）

我们介绍了PokéAI，这是第一个基于文本的多智能体大语言模型（LLM）框架，旨在自主玩耍并推进宝可梦红版游戏。该系统由三个专门的智能体组成：规划、执行和评估，每个智能体都有自己的记忆库、角色和技能。规划智能体作为中央大脑，生成任务以推进游戏，执行智能体在游戏环境中执行这些任务，而评估智能体则在任务完成后评估结果。我们的初步实验显示，执行智能体中的战斗模块在50次野外遭遇中实现了80.8%的平均胜率，仅比经验丰富的人类玩家低6%。此外，我们发现模型的战斗表现与其在语言相关任务中的LLM Arena得分高度相关，表明语言能力与战略推理之间存在重要联系。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有游戏AI在复杂环境中自主决策能力不足的问题，特别是在宝可梦红版游戏中，现有方法难以有效应对多变的战斗和任务需求。

**核心思路**：PokéAI通过设计三个专门的智能体（规划、执行和评估），形成闭环决策系统，能够自主生成和执行任务，从而提高游戏的自主性和智能性。

**技术框架**：系统由三个主要模块组成：规划智能体负责生成任务，执行智能体在游戏环境中执行这些任务，评估智能体则对任务结果进行评估，形成反馈循环。

**关键创新**：最重要的创新在于引入了多智能体协作机制，使得系统能够在复杂环境中进行有效的任务分配和执行，显著提升了游戏的自主决策能力。

**关键设计**：在战斗模块中，设计了特定的参数设置和评估机制，以确保战斗AI的表现能够与人类玩家相媲美，同时通过LLM Arena得分与战斗表现的相关性分析，揭示了语言能力与战略推理之间的联系。

## 📊 实验亮点

实验结果显示，PokéAI的战斗模块在50次野外遭遇中实现了80.8%的胜率，仅比经验丰富的人类玩家低6%。此外，模型的战斗表现与其LLM Arena得分之间存在显著相关性，表明语言能力与战略推理之间的联系。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI的开发、智能体系统的设计以及复杂决策任务的自动化。PokéAI的框架可以扩展到其他类型的游戏或模拟环境中，具有广泛的实际价值和未来影响，尤其是在提高AI自主性和智能决策能力方面。

## 📄 摘要（原文）

> We introduce PokéAI, the first text-based, multi-agent large language model (LLM) framework designed to autonomously play and progress through Pokémon Red. Our system consists of three specialized agents-Planning, Execution, and Critique-each with its own memory bank, role, and skill set. The Planning Agent functions as the central brain, generating tasks to progress through the game. These tasks are then delegated to the Execution Agent, which carries them out within the game environment. Upon task completion, the Critique Agent evaluates the outcome to determine whether the objective was successfully achieved. Once verification is complete, control returns to the Planning Agent, forming a closed-loop decision-making system.
>   As a preliminary step, we developed a battle module within the Execution Agent. Our results show that the battle AI achieves an average win rate of 80.8% across 50 wild encounters, only 6% lower than the performance of an experienced human player. Furthermore, we find that a model's battle performance correlates strongly with its LLM Arena score on language-related tasks, indicating a meaningful link between linguistic ability and strategic reasoning. Finally, our analysis of gameplay logs reveals that each LLM exhibits a unique playstyle, suggesting that individual models develop distinct strategic behaviors.

