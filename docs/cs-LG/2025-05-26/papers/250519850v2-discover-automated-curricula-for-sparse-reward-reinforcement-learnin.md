---
layout: default
title: "DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning"
---

# DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19850" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19850v2</a>
  <a href="https://arxiv.org/pdf/2505.19850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19850v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19850v2', 'DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leander Diaz-Bone, Marco Bagatella, Jonas Hübotter, Andreas Krause

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-05-26 (更新: 2025-10-20)

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出DISCOVER以解决稀疏奖励强化学习中的探索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `稀疏奖励` `强化学习` `探索策略` `目标选择` `高维环境` `自我改进代理` `人工智能`

## 📋 核心要点

1. 现有稀疏奖励强化学习方法在高维、长时间任务的探索上面临巨大挑战，导致解决效率低下。
2. 本文提出的DISCOVER方法通过选择与目标任务相关的简单任务来指导探索，提升了学习效率。
3. 实验结果表明，DISCOVER在高维环境中表现优异，解决了以往方法无法处理的探索问题。

## 📝 摘要（中文）

稀疏奖励强化学习（RL）能够建模多种复杂任务，但解决稀疏奖励任务的核心在于高效探索和长时间信用分配。现有方法通常关注解决多个稀疏奖励任务，导致个别高维、长时间任务的探索变得不可行。本文提出了一种新的方法DISCOVER，旨在通过选择与目标任务相关的简单任务来指导探索，从而提高解决复杂任务的能力。我们将DISCOVER与有原则的探索方法相连接，理论上界定了达到目标任务所需的时间，并在高维环境中进行了全面评估，结果表明该方法在探索问题上超越了现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏奖励强化学习中的探索效率问题。现有方法在面对高维、长时间任务时，往往无法有效指导探索，导致学习过程缓慢且低效。

**核心思路**：论文提出的DISCOVER方法通过选择与目标任务相关的简单任务来引导探索，帮助代理学习解决复杂任务所需的技能。这种方法不依赖于任何先验信息，能够从现有的强化学习算法中提取探索方向。

**技术框架**：DISCOVER的整体架构包括目标选择模块和探索策略模块。目标选择模块负责从简单任务中选择与目标任务相关的探索目标，而探索策略模块则根据这些目标指导代理的学习过程。

**关键创新**：DISCOVER的主要创新在于将目标选择与有原则的探索方法相结合，理论上界定了达到目标任务所需的时间。这一方法的独特之处在于它不依赖于任务空间的体积，而是关注代理与目标之间的初始距离。

**关键设计**：在设计上，DISCOVER采用了特定的损失函数来优化目标选择过程，并使用了高维环境中的适应性探索策略。具体参数设置和网络结构设计在实验中经过多次调整，以确保最佳性能。

## 📊 实验亮点

实验结果显示，DISCOVER在高维环境中的探索效率显著提升，相较于现有最先进的探索方法，解决了更多复杂任务，表现出更快的学习速度和更高的成功率。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏AI、自动驾驶等需要解决复杂决策任务的场景。通过提高稀疏奖励任务的学习效率，DISCOVER有助于构建更智能的自我改进代理，推动人工智能技术的进步。

## 📄 摘要（原文）

> Sparse-reward reinforcement learning (RL) can model a wide range of highly complex tasks. Solving sparse-reward tasks is RL's core premise, requiring efficient exploration coupled with long-horizon credit assignment, and overcoming these challenges is key for building self-improving agents with superhuman ability. Prior work commonly explores with the objective of solving many sparse-reward tasks, making exploration of individual high-dimensional, long-horizon tasks intractable. We argue that solving such challenging tasks requires solving simpler tasks that are relevant to the target task, i.e., whose achieval will teach the agent skills required for solving the target task. We demonstrate that this sense of direction, necessary for effective exploration, can be extracted from existing RL algorithms, without leveraging any prior information. To this end, we propose a method for directed sparse-reward goal-conditioned very long-horizon RL (DISCOVER), which selects exploratory goals in the direction of the target task. We connect DISCOVER to principled exploration in bandits, formally bounding the time until the target task becomes achievable in terms of the agent's initial distance to the target, but independent of the volume of the space of all tasks. We then perform a thorough evaluation in high-dimensional environments. We find that the directed goal selection of DISCOVER solves exploration problems that are beyond the reach of prior state-of-the-art exploration methods in RL.

