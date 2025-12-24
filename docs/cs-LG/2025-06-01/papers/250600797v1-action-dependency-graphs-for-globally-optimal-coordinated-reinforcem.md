---
layout: default
title: Action Dependency Graphs for Globally Optimal Coordinated Reinforcement Learning
---

# Action Dependency Graphs for Globally Optimal Coordinated Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00797" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00797v1</a>
  <a href="https://arxiv.org/pdf/2506.00797.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00797v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00797v1', 'Action Dependency Graphs for Globally Optimal Coordinated Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianglin Ding, Jingcheng Tang, Gangshan Jing

**分类**: cs.LG, cs.AI, eess.SY, math.OC

**发布日期**: 2025-06-01

---

## 💡 一句话要点

**提出动作依赖图以解决多智能体强化学习的全局最优问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `动作依赖图` `全局最优` `策略迭代` `计算复杂性` `协调控制` `智能交通` `机器人协作`

## 📋 核心要点

1. 现有的自回归动作依赖策略在智能体数量增加时导致计算复杂度显著上升，限制了多智能体强化学习的可扩展性。
2. 本文提出了一种新的动作依赖图（ADG）模型，能够更灵活地表示智能体间的动作依赖关系，从而实现全局最优策略。
3. 实验结果表明，所提出的方法在复杂环境中表现出色，验证了其在多智能体强化学习中的广泛适用性和鲁棒性。

## 📝 摘要（中文）

动作依赖的个体策略，结合环境状态和其他智能体的动作进行决策，已成为实现多智能体强化学习（MARL）全局最优的有前景的范式。然而，现有文献通常采用自回归的动作依赖策略，使得每个智能体的策略依赖于所有前置智能体的动作，这在智能体数量增加时会导致计算复杂度显著上升，限制了可扩展性。本文考虑了一类更为广泛的动作依赖策略，不必遵循自回归形式。我们提出使用动作依赖图（ADG）来建模智能体间的动作依赖关系。我们证明了在由协调图结构化的MARL问题中，满足特定条件的稀疏ADG的动作依赖策略可以实现全局最优。基于此理论基础，我们开发了一种具有全局最优保证的表格策略迭代算法，并将我们的框架整合到多个最先进的算法中，实验结果验证了我们方法在更一般场景中的鲁棒性和适用性。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体强化学习中自回归动作依赖策略带来的计算复杂性问题。现有方法在智能体数量增加时，策略的计算负担显著加重，影响了系统的可扩展性。

**核心思路**：我们提出了一种新的动作依赖图（ADG）模型，允许智能体之间的动作依赖关系不再遵循自回归形式，从而降低计算复杂度并提高策略的灵活性。

**技术框架**：整体架构包括动作依赖图的构建、策略的设计与优化，以及基于稀疏ADG的全局最优保证的策略迭代算法。具体流程为：首先构建ADG，然后利用该图进行策略优化，最后通过迭代算法实现全局最优。

**关键创新**：最重要的创新点在于引入了动作依赖图（ADG），使得策略设计不再局限于自回归形式，从而显著降低了计算复杂度，并在特定条件下保证全局最优性。

**关键设计**：在算法设计中，采用了稀疏ADG以减少计算负担，并通过特定的损失函数和参数设置来优化策略的收敛性和稳定性。

## 📊 实验亮点

实验结果显示，所提出的方法在复杂环境中相较于基线算法表现出显著提升，尤其在全局最优性和计算效率方面，验证了其在多智能体强化学习中的有效性和适用性。

## 🎯 应用场景

该研究的潜在应用领域包括多智能体系统的协调控制、智能交通系统、机器人群体协作等。通过优化智能体间的决策过程，可以显著提升系统的整体效率和性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Action-dependent individual policies, which incorporate both environmental states and the actions of other agents in decision-making, have emerged as a promising paradigm for achieving global optimality in multi-agent reinforcement learning (MARL). However, the existing literature often adopts auto-regressive action-dependent policies, where each agent's policy depends on the actions of all preceding agents. This formulation incurs substantial computational complexity as the number of agents increases, thereby limiting scalability. In this work, we consider a more generalized class of action-dependent policies, which do not necessarily follow the auto-regressive form. We propose to use the `action dependency graph (ADG)' to model the inter-agent action dependencies. Within the context of MARL problems structured by coordination graphs, we prove that an action-dependent policy with a sparse ADG can achieve global optimality, provided the ADG satisfies specific conditions specified by the coordination graph. Building on this theoretical foundation, we develop a tabular policy iteration algorithm with guaranteed global optimality. Furthermore, we integrate our framework into several SOTA algorithms and conduct experiments in complex environments. The empirical results affirm the robustness and applicability of our approach in more general scenarios, underscoring its potential for broader MARL challenges.

