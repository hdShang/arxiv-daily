---
layout: default
title: Entropy-Controlled Intrinsic Motivation Reinforcement Learning for Quadruped Robot Locomotion in Complex Terrains
---

# Entropy-Controlled Intrinsic Motivation Reinforcement Learning for Quadruped Robot Locomotion in Complex Terrains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06486" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06486v2</a>
  <a href="https://arxiv.org/pdf/2512.06486.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06486v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.06486v2', 'Entropy-Controlled Intrinsic Motivation Reinforcement Learning for Quadruped Robot Locomotion in Complex Terrains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanru Gong, Xinyi Zheng, Yuan Hui, Zhongjun Li, Weiqiang Wang, Xiaoqing Zhu

**分类**: cs.RO

**发布日期**: 2025-12-06 (更新: 2025-12-13)

---

## 💡 一句话要点

**提出基于熵控制的内在动机强化学习算法，提升四足机器人复杂地形运动能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四足机器人` `强化学习` `内在动机` `熵控制` `复杂地形` `运动控制` `机器人 locomotion`

## 📋 核心要点

1. 传统强化学习算法在四足机器人运动控制中易陷入早熟收敛，导致次优运动策略和任务性能下降。
2. 论文提出ECIM算法，结合熵控制和内在动机，鼓励智能体探索未知状态，避免过早收敛到局部最优解。
3. 实验结果表明，ECIM在多种复杂地形下显著提升了四足机器人的运动性能，降低了能量消耗和关节压力。

## 📝 摘要（中文）

本文提出了一种名为熵控制内在动机（ECIM）的强化学习算法，旨在解决四足机器人运动策略训练中常见的早熟收敛问题。与近端策略优化（PPO）系列算法不同，ECIM通过结合内在动机和自适应探索来减少早熟收敛。实验表明，在Isaac Gym的六种地形类别（向上斜坡、向下斜坡、不平坦粗糙地形、上升楼梯、下降楼梯和平坦地面）中，ECIM始终优于其他基线方法。具体而言，任务奖励提高了4-12%，身体俯仰振荡峰值降低了23-29%，关节加速度降低了20-32%，关节扭矩消耗降低了11-20%。ECIM通过结合熵控制和内在动机控制，在不同地形中实现了更好的四足运动稳定性，同时降低了能量消耗，使其成为复杂机器人控制任务的实用选择。

## 🔬 方法详解

**问题定义**：现有的基于PPO的强化学习算法在训练四足机器人运动策略时，容易出现早熟收敛的问题。这意味着智能体在探索到全局最优策略之前，就陷入了局部最优解，导致最终学习到的运动策略并非最优，从而限制了机器人在复杂地形下的运动能力。现有方法缺乏有效的探索机制，难以跳出局部最优。

**核心思路**：论文的核心思路是引入熵控制的内在动机机制。熵控制用于鼓励智能体探索未知的状态空间，避免过早收敛。内在动机则为智能体提供额外的奖励信号，促使其主动探索环境，学习更鲁棒的运动策略。通过将两者结合，ECIM算法能够有效地平衡探索和利用，从而避免早熟收敛。

**技术框架**：ECIM算法的整体框架仍然基于Actor-Critic架构，类似于PPO。主要包括以下几个模块：1) Actor网络，用于生成动作策略；2) Critic网络，用于评估状态价值；3) 熵奖励模块，根据当前策略的熵值，给予智能体额外的奖励，鼓励探索；4) 内在动机奖励模块，根据智能体对环境的预测误差，给予智能体额外的奖励，鼓励探索未知状态。这些模块共同作用，指导智能体学习最优运动策略。

**关键创新**：ECIM算法的关键创新在于将熵控制和内在动机相结合，并将其应用于四足机器人运动控制。与传统的PPO算法相比，ECIM算法能够更有效地避免早熟收敛，从而学习到更鲁棒、更高效的运动策略。此外，ECIM算法还采用了自适应的探索策略，能够根据环境的复杂程度动态调整探索力度。

**关键设计**：ECIM算法的关键设计包括：1) 熵奖励的设计，通常使用策略分布的熵作为奖励信号，例如使用高斯分布的方差或softmax输出的熵；2) 内在动机奖励的设计，通常基于预测误差，例如使用前向模型的预测误差或状态表征的重构误差；3) Actor和Critic网络的结构，通常使用多层感知机或循环神经网络；4) 损失函数的设计，包括策略梯度损失、价值函数损失、熵奖励损失和内在动机奖励损失。这些设计共同决定了ECIM算法的性能。

## 📊 实验亮点

实验结果表明，ECIM算法在六种复杂地形中均优于基线方法。任务奖励平均提高了4-12%，身体俯仰振荡峰值降低了23-29%，关节加速度降低了20-32%，关节扭矩消耗降低了11-20%。这些数据表明，ECIM算法不仅提升了机器人的运动性能，还降低了能量消耗和关节压力，使其更具实用价值。

## 🎯 应用场景

该研究成果可广泛应用于各种需要四足机器人进行复杂地形运动的场景，例如搜救、勘探、物流和巡检等。通过提升机器人的运动能力和稳定性，可以使其在恶劣环境下执行任务，降低人员风险，提高工作效率。未来，该技术有望进一步推广到其他类型的机器人，例如人形机器人和轮式机器人。

## 📄 摘要（原文）

> Learning is the basis of both biological and artificial systems when it comes to mimicking intelligent behaviors. From the classical PPO (Proximal Policy Optimization), there is a series of deep reinforcement learning algorithms which are widely used in training locomotion policies for quadrupedal robots because of their stability and sample efficiency. However, among all these variants, experiments and simulations often converge prematurely, leading to suboptimal locomotion and reduced task performance. Therefore, in this paper, we introduce Entropy-Controlled Intrinsic Motivation (ECIM), an entropy-based reinforcement learning algorithm in contrast with the PPO series, that can reduce premature convergence by combining intrinsic motivation with adaptive exploration.
>   For experiments, in order to parallel with other baselines, we chose to apply it in Isaac Gym across six terrain categories: upward slopes, downward slopes, uneven rough terrain, ascending stairs, descending stairs, and flat ground as widely used. For comparison, our experiments consistently achieve better performance: task rewards increase by 4--12%, peak body pitch oscillation is reduced by 23--29%, joint acceleration decreases by 20--32%, and joint torque consumption declines by 11--20%. Overall, our model ECIM, by combining entropy control and intrinsic motivation control, achieves better results in stability across different terrains for quadrupedal locomotion, and at the same time reduces energetic cost and makes it a practical choice for complex robotic control tasks.

