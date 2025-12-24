---
layout: default
title: SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics
---

# SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11494" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11494v2</a>
  <a href="https://arxiv.org/pdf/2505.11494.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11494v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11494v2', 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lizhi Yang, Blake Werner, Ryan K. Cosner, David Fridovich-Keil, Preston Culbertson, Aaron D. Ames

**分类**: cs.RO

**发布日期**: 2025-05-16 (更新: 2025-08-01)

**备注**: Video at https://youtu.be/-Qv1wR4jfj4. To appear at IROS 2025

---

## 💡 一句话要点

**提出SHIELD框架以解决人形机器人动态安全问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态安全` `人形机器人` `控制障碍函数` `强化学习` `随机动态模型` `安全导航` `机器人学习`

## 📋 核心要点

1. 现有的动态控制策略在确保安全性方面存在挑战，尤其是在动态环境中约束的满足问题。
2. SHIELD框架通过训练生成的随机动态模型，并在学习的控制器上添加安全层，提供了动态安全的解决方案。
3. 在Unitree G1人形机器人上的实验表明，SHIELD能够在多种环境中安全导航，展示了其在动态安全性方面的有效性。

## 📝 摘要（中文）

机器人学习已经为复杂任务（如人形机器人的动态行走）提供了有效的“黑箱”控制器。然而，确保动态安全性，即约束满足，仍然是这些策略面临的挑战。强化学习通过奖励工程启发式地嵌入约束，而添加或修改约束需要重新训练。基于模型的方法，如控制障碍函数（CBFs），能够在运行时指定约束并提供形式化保证，但需要准确的动态模型。本文提出SHIELD，一个分层安全框架，通过训练生成的随机动态残差模型和在学习的控制器上添加安全层，利用随机离散时间CBF形式在概率上强制执行安全约束，从而实现了对现有自主系统的最小干预安全层。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人在动态环境中执行复杂任务时的安全性问题。现有的强化学习方法在动态安全性方面存在不足，尤其是在约束的实时满足上。

**核心思路**：SHIELD框架的核心思路是通过训练一个生成的随机动态残差模型，捕捉系统行为和不确定性，并在此基础上添加一个安全层，以在概率上强制执行安全约束。

**技术框架**：SHIELD的整体架构包括两个主要模块：首先是基于真实世界数据训练的随机动态模型，其次是基于该模型的控制障碍函数（CBF）安全层。该框架能够与现有的学习控制器无缝集成。

**关键创新**：SHIELD的主要创新在于其通过生成的动态模型与控制障碍函数的结合，提供了一种在不需要重新训练的情况下实现动态安全的方案。这与传统的强化学习方法有本质区别。

**关键设计**：在设计中，关键参数包括动态模型的训练数据来源、CBF的概率约束形式以及与学习控制器的集成方式。这些设计确保了安全层的最小干预性和高效性。

## 📊 实验亮点

在Unitree G1人形机器人上的实验结果表明，SHIELD框架能够在多种室内和室外环境中实现安全导航，成功避免障碍物。与传统方法相比，SHIELD在动态安全性方面提供了显著的性能提升，确保了在不确定性条件下的安全性。

## 🎯 应用场景

SHIELD框架具有广泛的应用潜力，特别是在需要动态安全保障的机器人导航任务中。其能够在复杂和不确定的环境中有效地执行任务，具有重要的实际价值，未来可扩展至更多类型的机器人系统和应用场景。

## 📄 摘要（原文）

> Robot learning has produced remarkably effective ``black-box'' controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

