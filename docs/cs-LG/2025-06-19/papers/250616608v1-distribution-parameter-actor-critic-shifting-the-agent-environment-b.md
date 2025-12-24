---
layout: default
title: "Distribution Parameter Actor-Critic: Shifting the Agent-Environment Boundary for Diverse Action Spaces"
---

# Distribution Parameter Actor-Critic: Shifting the Agent-Environment Boundary for Diverse Action Spaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16608" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16608v1</a>
  <a href="https://arxiv.org/pdf/2506.16608.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16608v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16608v1', 'Distribution Parameter Actor-Critic: Shifting the Agent-Environment Boundary for Diverse Action Spaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiamin He, A. Rupam Mahmood, Martha White

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出分布参数演员-评论家以解决多样化动作空间问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `分布参数` `演员-评论家` `连续控制` `多样化动作空间`

## 📋 核心要点

1. 现有强化学习方法在处理多样化动作空间时存在局限，尤其是在离散与连续动作的混合场景中。
2. 论文提出将分布参数作为动作进行重新参数化，设计了分布参数策略梯度（DPPG）以降低学习方差。
3. DPAC在MuJoCo连续控制任务中表现优于TD3，且在离散动作空间中也展现出竞争力，验证了其有效性。

## 📝 摘要（中文）

我们提出了一种新颖的强化学习框架，将分布参数视为动作，重新定义了智能体与环境之间的边界。这种重新参数化使得新的动作空间连续，无论原始动作类型（离散、连续、混合等）如何。在这种新参数化下，我们开发了一种广义的确定性策略梯度估计器——分布参数策略梯度（DPPG），其方差低于原始动作空间中的梯度。尽管在分布参数上学习评论家面临新挑战，我们引入了插值评论家学习（ICL），这是一种简单而有效的增强学习策略，得到了来自赌博设置的启示。基于强基线TD3，我们提出了一种实用的基于DPPG的演员-评论家算法——分布参数演员-评论家（DPAC）。实证结果表明，DPAC在OpenAI Gym和DeepMind Control Suite的MuJoCo连续控制任务中优于TD3，并在相同的离散动作空间环境中表现出竞争力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有强化学习方法在多样化动作空间中的局限性，尤其是离散与连续动作混合场景下的学习效率低下问题。

**核心思路**：通过将分布参数视为动作，重新定义智能体与环境的边界，从而使得动作空间变为连续。这种设计使得策略学习更加灵活，能够适应不同类型的动作。

**技术框架**：整体架构包括分布参数策略梯度（DPPG）估计器和插值评论家学习（ICL）策略。DPPG用于计算梯度，ICL则用于优化评论家网络的学习过程。

**关键创新**：最重要的技术创新在于将分布参数作为动作进行处理，这一方法显著降低了学习过程中的方差，并提高了策略的稳定性。

**关键设计**：在DPPG中，采用了新的损失函数和网络结构设计，以适应分布参数的学习需求，同时在插值评论家学习中引入了基于赌博设置的启示，以增强学习效果。

## 📊 实验亮点

实验结果显示，DPAC在MuJoCo连续控制任务中相较于TD3提升了性能，具体表现为在多个任务中获得了更高的平均回报，验证了其在复杂环境中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏智能体以及复杂决策系统等。通过有效处理多样化的动作空间，DPAC能够在更广泛的实际场景中实现高效的决策制定，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce a novel reinforcement learning (RL) framework that treats distribution parameters as actions, redefining the boundary between agent and environment. This reparameterization makes the new action space continuous, regardless of the original action type (discrete, continuous, mixed, etc.). Under this new parameterization, we develop a generalized deterministic policy gradient estimator, Distribution Parameter Policy Gradient (DPPG), which has lower variance than the gradient in the original action space. Although learning the critic over distribution parameters poses new challenges, we introduce interpolated critic learning (ICL), a simple yet effective strategy to enhance learning, supported by insights from bandit settings. Building on TD3, a strong baseline for continuous control, we propose a practical DPPG-based actor-critic algorithm, Distribution Parameter Actor-Critic (DPAC). Empirically, DPAC outperforms TD3 in MuJoCo continuous control tasks from OpenAI Gym and DeepMind Control Suite, and demonstrates competitive performance on the same environments with discretized action spaces.

