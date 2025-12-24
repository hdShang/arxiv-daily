---
layout: default
title: "Beyond-Expert Performance with Limited Demonstrations: Efficient Imitation Learning with Double Exploration"
---

# Beyond-Expert Performance with Limited Demonstrations: Efficient Imitation Learning with Double Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20307" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20307v1</a>
  <a href="https://arxiv.org/pdf/2506.20307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20307v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20307v1', 'Beyond-Expert Performance with Limited Demonstrations: Efficient Imitation Learning with Double Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heyang Zhao, Xingrui Yu, David M. Bossens, Ivor W. Tsang, Quanquan Gu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出双重探索的模仿学习算法以实现超越专家的表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `强化学习` `双重探索` `样本效率` `策略优化` `不确定性正则化` `自动驾驶` `机器人控制`

## 📋 核心要点

1. 现有的模仿学习方法在有限演示下难以准确学习专家策略，且状态空间复杂性增加了学习难度。
2. 本文提出的ILDE算法通过双重探索策略，结合乐观的策略优化和好奇心驱动的状态探索，提升了学习效率。
3. 实验结果显示，ILDE在样本效率上超越了现有最先进的模仿学习算法，并在多个任务上实现了超越专家的表现。

## 📝 摘要（中文）

模仿学习是强化学习中的一个核心问题，其目标是学习模仿专家行为的策略。然而，由于状态空间的复杂性，从有限的演示中准确学习专家策略常常具有挑战性。此外，为了实现超越专家的表现，探索环境和收集数据是至关重要的。为了解决这些挑战，本文提出了一种新颖的模仿学习算法——双重探索模仿学习（ILDE），该算法在两个方面实现了探索：一是通过探索奖励优化策略，奖励高不确定性的状态-动作对，以潜在地改善对专家策略的收敛；二是驱动好奇心的状态探索，偏离演示轨迹，以潜在地实现超越专家的表现。实验证明，ILDE在样本效率方面优于现有的模仿学习算法，并在Atari和MuJoCo任务上以更少的演示实现了超越专家的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决在有限演示下，模仿学习难以准确学习专家策略的问题。现有方法在复杂状态空间中面临探索不足和样本效率低下的挑战。

**核心思路**：ILDE算法通过引入双重探索机制，既优化策略以奖励高不确定性的状态-动作对，又探索偏离演示轨迹的状态，以实现超越专家的表现。

**技术框架**：ILDE的整体架构包括两个主要模块：乐观策略优化模块和好奇心驱动的状态探索模块。前者通过奖励机制引导策略优化，后者则通过探索新状态来丰富数据集。

**关键创新**：ILDE的主要创新在于其双重探索机制，结合了乐观的策略优化和好奇心驱动的探索，显著提高了样本效率和学习效果。这与传统的模仿学习方法形成了鲜明对比。

**关键设计**：ILDE采用了不确定性正则化的策略优化方法，设计了探索奖励机制，并在损失函数中引入了对不确定性状态的奖励，以促进更有效的学习。

## 📊 实验亮点

实验结果表明，ILDE在Atari和MuJoCo任务上相较于现有最先进的模仿学习算法，样本效率提高了显著的比例，且在多个任务中实现了超越专家的表现，展示了其强大的学习能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏AI等，能够在有限的示例数据下实现更高效的学习和决策。未来，ILDE算法可能推动更多复杂任务的解决，提升智能体的自主学习能力。

## 📄 摘要（原文）

> Imitation learning is a central problem in reinforcement learning where the goal is to learn a policy that mimics the expert's behavior. In practice, it is often challenging to learn the expert policy from a limited number of demonstrations accurately due to the complexity of the state space. Moreover, it is essential to explore the environment and collect data to achieve beyond-expert performance. To overcome these challenges, we propose a novel imitation learning algorithm called Imitation Learning with Double Exploration (ILDE), which implements exploration in two aspects: (1) optimistic policy optimization via an exploration bonus that rewards state-action pairs with high uncertainty to potentially improve the convergence to the expert policy, and (2) curiosity-driven exploration of the states that deviate from the demonstration trajectories to potentially yield beyond-expert performance. Empirically, we demonstrate that ILDE outperforms the state-of-the-art imitation learning algorithms in terms of sample efficiency and achieves beyond-expert performance on Atari and MuJoCo tasks with fewer demonstrations than in previous work. We also provide a theoretical justification of ILDE as an uncertainty-regularized policy optimization method with optimistic exploration, leading to a regret growing sublinearly in the number of episodes.

