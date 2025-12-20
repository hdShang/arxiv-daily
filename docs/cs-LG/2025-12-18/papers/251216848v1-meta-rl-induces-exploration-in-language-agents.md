---
layout: default
title: Meta-RL Induces Exploration in Language Agents
---

# Meta-RL Induces Exploration in Language Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16848" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16848v1</a>
  <a href="https://arxiv.org/pdf/2512.16848.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16848v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16848v1', 'Meta-RL Induces Exploration in Language Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yulun Jiang, Liangze Jiang, Damien Teney, Michael Moor, Maria Brbic

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**LaMer：基于元强化学习提升语言Agent在复杂环境中的探索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `元强化学习` `语言Agent` `主动探索` `策略调整` `上下文学习`

## 📋 核心要点

1. 现有RL训练的LLM Agent在需要主动探索和长期规划的任务中表现不足，缺乏有效的探索机制。
2. LaMer通过元强化学习框架，鼓励Agent在训练时进行跨episode的探索，并在测试时通过反思进行策略调整。
3. 实验表明，LaMer在Sokoban、MineSweeper和Webshop等任务上显著优于RL基线，并具有更好的泛化能力。

## 📝 摘要（中文）

强化学习(RL)使得训练大型语言模型(LLM) Agent与环境交互并解决多轮长时序任务成为可能。然而，RL训练的Agent在需要主动探索的任务中表现不佳，并且无法有效地从试错经验中学习。本文提出了LaMer，一个通用的元强化学习框架，使LLM Agent能够在测试时主动探索并从环境反馈中学习。LaMer包含两个关键组件：(i)一个跨episode的训练框架，鼓励探索和长期奖励优化；(ii)通过反思进行上下文策略调整，允许Agent从任务反馈信号中调整其策略，而无需梯度更新。在不同环境中的实验表明，LaMer显著提高了性能，在Sokoban、MineSweeper和Webshop上的性能分别提高了11%、14%和19%。此外，与RL训练的Agent相比，LaMer还展示了对更具挑战性或先前未见过的任务的更好泛化能力。总的来说，我们的结果表明，元强化学习提供了一种原则性的方法来诱导语言Agent进行探索，从而通过学习到的探索策略实现对新环境的更稳健的适应。

## 🔬 方法详解

**问题定义**：现有基于强化学习训练的语言Agent在复杂环境中进行探索时效率低下，难以适应新的任务和环境。传统的强化学习方法往往侧重于利用已有的知识，而忽略了主动探索的重要性，导致Agent容易陷入局部最优解，无法有效地发现新的策略和行为。

**核心思路**：LaMer的核心思路是利用元强化学习的思想，让Agent学习如何进行有效的探索。通过跨episode的训练，Agent可以学习到一种通用的探索策略，使其能够更好地适应新的任务和环境。此外，LaMer还引入了反思机制，允许Agent根据环境的反馈信号动态调整其策略，从而提高其适应性和鲁棒性。

**技术框架**：LaMer框架包含两个主要组成部分：跨episode训练和上下文策略调整。在跨episode训练阶段，Agent在多个不同的任务episode中进行训练，目标是学习一种能够最大化长期奖励的通用策略。在上下文策略调整阶段，Agent根据当前任务的反馈信号，通过反思机制动态调整其策略，从而更好地适应当前任务。整个框架无需梯度更新，降低了计算成本。

**关键创新**：LaMer的关键创新在于将元强化学习的思想引入到语言Agent的训练中，并结合反思机制实现了高效的探索和策略调整。与传统的强化学习方法相比，LaMer能够更好地适应新的任务和环境，并具有更强的泛化能力。此外，LaMer的上下文策略调整机制无需梯度更新，降低了计算成本，使其更易于部署和应用。

**关键设计**：LaMer的关键设计包括：(1)跨episode训练框架，鼓励Agent进行多样化的探索；(2)基于反思的上下文策略调整机制，允许Agent根据环境反馈动态调整策略；(3)奖励函数的设计，鼓励Agent进行长期规划和优化；(4)合适的LLM选择，保证Agent具备足够的表达能力和推理能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16848v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LaMer在Sokoban、MineSweeper和Webshop等多个环境中的实验结果表明，其性能显著优于传统的强化学习基线，分别取得了11%、14%和19%的性能提升。此外，LaMer还展示了对更具挑战性或先前未见过的任务的更好泛化能力，证明了其在复杂环境中的有效性和鲁棒性。

## 🎯 应用场景

LaMer具有广泛的应用前景，可以应用于各种需要语言Agent进行主动探索和适应的任务中，例如机器人导航、游戏AI、智能助手等。该研究有助于提升Agent在复杂环境中的智能水平，使其能够更好地完成各种任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has enabled the training of large language model (LLM) agents to interact with the environment and to solve multi-turn long-horizon tasks. However, the RL-trained agents often struggle in tasks that require active exploration and fail to efficiently adapt from trial-and-error experiences. In this paper, we present LaMer, a general Meta-RL framework that enables LLM agents to actively explore and learn from the environment feedback at test time. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long-term rewards optimization; and (ii) in-context policy adaptation via reflection, allowing the agent to adapt their policy from task feedback signal without gradient update. Experiments across diverse environments show that LaMer significantly improves performance over RL baselines, with 11%, 14%, and 19% performance gains on Sokoban, MineSweeper and Webshop, respectively. Moreover, LaMer also demonstrates better generalization to more challenging or previously unseen tasks compared to the RL-trained agents. Overall, our results demonstrate that Meta-RL provides a principled approach to induce exploration in language agents, enabling more robust adaptation to novel environments through learned exploration strategies.

