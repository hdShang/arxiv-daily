---
layout: default
title: "Learning to Ball: Composing Policies for Long-Horizon Basketball Moves"
---

# Learning to Ball: Composing Policies for Long-Horizon Basketball Moves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22442" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22442v1</a>
  <a href="https://arxiv.org/pdf/2509.22442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22442v1', 'Learning to Ball: Composing Policies for Long-Horizon Basketball Moves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pei Xu, Zhen Wu, Ruocheng Wang, Vishnu Sarukkai, Kayvon Fatahalian, Ioannis Karamouzas, Victor Zordan, C. Karen Liu

**分类**: cs.GR, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-09-26

**备注**: ACM Transactions on Graphics (Proceedings of SIGGRAPH Asia 2025). Website: http://pei-xu.github.io/basketball. Video: https://youtu.be/2RBFIjjmR2I. Code: https://github.com/xupei0610/basketball

**期刊**: ACM Transactions on Graphics (December 2025)

**DOI**: [10.1145/3763367](https://doi.org/10.1145/3763367)

---

## 💡 一句话要点

**提出一种策略集成框架，用于学习篮球动作等长时程多阶段任务的控制策略。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `强化学习` `策略集成` `长时程任务` `多阶段任务` `篮球动作` `软路由` `运动控制`

## 📋 核心要点

1. 现有强化学习方法在处理篮球动作等长时程任务时，难以实现策略的无缝组合和技能间的平滑过渡。
2. 论文提出一种策略集成框架，通过高层软路由实现不同运动技能间的无缝过渡，从而解决长时程任务的策略组合问题。
3. 实验表明，该方法能有效控制模拟角色与球互动，并根据用户指令完成任务，无需预先设定球的运动轨迹。

## 📝 摘要（中文）

针对篮球动作等长时程多阶段任务中，强化学习方法在策略组合和技能过渡方面面临的挑战，本文提出了一种新的策略集成框架。长时程任务通常包含具有明确目标的不同子任务，以及目标不明确但对整个任务成功至关重要的过渡子任务。现有方法如混合专家和技能链，难以处理各策略共享状态少或阶段间缺乏明确初始/终止状态的任务。本文引入高层软路由，实现子任务间的无缝鲁棒过渡。在篮球技能和过渡上的评估表明，该方法能有效控制模拟角色与球互动，并根据实时用户指令完成长时程任务，无需依赖球的轨迹参考。

## 🔬 方法详解

**问题定义**：论文旨在解决长时程、多阶段任务（如篮球动作）中，强化学习控制策略学习的难题。现有方法，如混合专家模型和技能链，在处理子策略间状态空间重叠较少或缺乏明确初始/终止状态的任务时表现不佳。这些方法难以实现不同技能间的平滑过渡，导致整体任务失败。

**核心思路**：论文的核心思路是将长时程任务分解为多个子任务，并学习每个子任务的控制策略。关键在于设计一个策略集成框架，能够将这些独立的策略组合起来，实现无缝的技能过渡。通过引入高层软路由机制，动态地选择合适的子策略，从而实现鲁棒的策略切换。

**技术框架**：整体框架包含两个主要部分：一是多个独立的子策略，每个策略负责完成一个特定的子任务（例如运球、投篮）。二是高层软路由模块，该模块根据当前状态动态地选择合适的子策略。软路由模块的输出是各个子策略的权重，这些权重用于加权融合各个子策略的动作。

**关键创新**：论文的关键创新在于高层软路由的设计。与传统的硬切换方法不同，软路由允许在多个子策略之间进行平滑过渡，避免了策略切换时的突兀行为。此外，软路由是可学习的，能够根据任务需求自动调整策略切换的策略。

**关键设计**：高层软路由通常由一个神经网络实现，输入是当前状态，输出是各个子策略的权重。损失函数的设计需要考虑两个方面：一是保证每个子策略都能有效地完成其对应的子任务，二是保证软路由能够平滑地切换策略。具体的网络结构和参数设置需要根据具体的任务进行调整。

## 📊 实验亮点

论文在模拟篮球环境中进行了实验，验证了所提出方法的有效性。实验结果表明，该方法能够有效地控制模拟角色完成各种篮球动作，包括运球、传球、投篮等。与传统的技能链方法相比，该方法能够实现更平滑的技能过渡，并且能够更好地适应用户的实时指令。具体性能数据和提升幅度在论文中有详细展示。

## 🎯 应用场景

该研究成果可应用于游戏AI、虚拟角色控制、机器人运动规划等领域。例如，可以用于开发更智能的篮球游戏AI，使虚拟角色能够执行更复杂的篮球动作。此外，该方法还可以应用于机器人领域，使机器人能够完成更复杂的任务，如装配、导航等。未来，该技术有望扩展到其他长时程、多阶段任务，例如自动驾驶、医疗手术等。

## 📄 摘要（原文）

> Learning a control policy for a multi-phase, long-horizon task, such as basketball maneuvers, remains challenging for reinforcement learning approaches due to the need for seamless policy composition and transitions between skills. A long-horizon task typically consists of distinct subtasks with well-defined goals, separated by transitional subtasks with unclear goals but critical to the success of the entire task. Existing methods like the mixture of experts and skill chaining struggle with tasks where individual policies do not share significant commonly explored states or lack well-defined initial and terminal states between different phases. In this paper, we introduce a novel policy integration framework to enable the composition of drastically different motor skills in multi-phase long-horizon tasks with ill-defined intermediate states. Based on that, we further introduce a high-level soft router to enable seamless and robust transitions between the subtasks. We evaluate our framework on a set of fundamental basketball skills and challenging transitions. Policies trained by our approach can effectively control the simulated character to interact with the ball and accomplish the long-horizon task specified by real-time user commands, without relying on ball trajectory references.

