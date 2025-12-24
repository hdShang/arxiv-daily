---
layout: default
title: Intrinsic Goals for Autonomous Agents: Model-Based Exploration in Virtual Zebrafish Predicts Ethological Behavior and Whole-Brain Dynamics
---

# Intrinsic Goals for Autonomous Agents: Model-Based Exploration in Virtual Zebrafish Predicts Ethological Behavior and Whole-Brain Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00138" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00138v2</a>
  <a href="https://arxiv.org/pdf/2506.00138.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00138v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00138v2', 'Intrinsic Goals for Autonomous Agents: Model-Based Exploration in Virtual Zebrafish Predicts Ethological Behavior and Whole-Brain Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reece Keller, Alyn Kirsch, Felix Pei, Xaq Pitkow, Leo Kozachkov, Aran Nayebi

**分类**: q-bio.NC, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-05-30 (更新: 2025-10-24)

**备注**: 17 pages, 7 figures

---

## 💡 一句话要点

**提出3M-Progress以解决自主智能体探索不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主智能体` `内在动机` `模型驱动` `探索策略` `神经计算`

## 📋 核心要点

1. 现有的强化学习方法在无奖励环境中的探索表现不稳定，无法有效捕捉动物的自主行为。
2. 本文提出的3M-Progress方法，通过跟踪世界模型与先验的差异，实现了动物般的自主探索。
3. 实验结果表明，3M-Progress智能体能够有效捕捉自主行为和全脑神经-胶质动态，展示了其优越性。

## 📝 摘要（中文）

自主性是动物智能的标志，使其能够在复杂环境中进行适应性和智能行为，而无需依赖外部奖励或任务结构。现有的强化学习方法在无奖励环境中的探索表现不稳定，未能收敛到有效的探索策略，无法捕捉到动物的自主行为。此外，系统神经科学主要关注动物在外部奖励驱动下的行为，忽视了自主性的神经基础。为了解决这些问题，本文提出了一种新颖的基于模型的内在驱动3M-Progress，旨在模拟动物的自主探索。该方法通过跟踪在线世界模型与固定先验之间的差异，实现了类似动物的探索。我们首次展示了完全通过自我监督优化内在目标预测脑数据的自主实体智能体，提供了神经-胶质计算的目标驱动群体模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在无奖励环境中探索不稳定的问题，现有方法未能有效模拟动物的自主行为。

**核心思路**：提出的3M-Progress方法通过跟踪在线世界模型与固定先验之间的差异，模拟动物的自主探索行为，旨在实现更自然的行为模式。

**技术框架**：该方法包括三个主要模块：在线世界模型的构建、固定先验的学习和内在目标的自我监督优化，整体流程通过不断更新模型来实现自主探索。

**关键创新**：3M-Progress是首个完全通过自我监督优化内在目标来预测脑数据的自主智能体，突破了传统方法依赖外部奖励的局限。

**关键设计**：在设计中，采用了特定的损失函数来优化模型的预测能力，并通过调整网络结构来增强模型的表达能力，确保其能够捕捉复杂的行为模式。

## 📊 实验亮点

实验结果显示，3M-Progress智能体在捕捉自主行为模式和全脑神经-胶质动态方面表现优异，能够解释行为模式的方差，并与传统方法相比，展示了显著的性能提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括机器人自主导航、智能代理的行为建模以及生物启发的人工智能系统。通过建立与动物行为相似的自主智能体，未来可以在复杂环境中实现更高效的决策和适应能力，推动智能系统的发展。

## 📄 摘要（原文）

> Autonomy is a hallmark of animal intelligence, enabling adaptive and intelligent behavior in complex environments without relying on external reward or task structure. Existing reinforcement learning approaches to exploration in reward-free environments, including a class of methods known as model-based intrinsic motivation, exhibit inconsistent exploration patterns and do not converge to an exploratory policy, thus failing to capture robust autonomous behaviors observed in animals. Moreover, systems neuroscience has largely overlooked the neural basis of autonomy, focusing instead on experimental paradigms where animals are motivated by external reward rather than engaging in ethological, naturalistic and task-independent behavior. To bridge these gaps, we introduce a novel model-based intrinsic drive explicitly designed after the principles of autonomous exploration in animals. Our method (3M-Progress) achieves animal-like exploration by tracking divergence between an online world model and a fixed prior learned from an ecological niche. To the best of our knowledge, we introduce the first autonomous embodied agent that predicts brain data entirely from self-supervised optimization of an intrinsic goal -- without any behavioral or neural training data -- demonstrating that 3M-Progress agents capture the explainable variance in behavioral patterns and whole-brain neural-glial dynamics recorded from autonomously behaving larval zebrafish, thereby providing the first goal-driven, population-level model of neural-glial computation. Our findings establish a computational framework connecting model-based intrinsic motivation to naturalistic behavior, providing a foundation for building artificial agents with animal-like autonomy.

