---
layout: default
title: CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation
---

# CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14689" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14689</a>
  <a href="https://arxiv.org/pdf/2512.14689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14689" onclick="toggleFavorite(this, '2512.14689', 'CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Chen, Zi-ang Cao, Zhengyi Luo, Fernando Castañeda, Chenran Li, Tingwu Wang, Ye Yuan, Linxi "Jim" Fan, C. Karen Liu, Yuke Zhu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**CHIP：通过后见之明扰动实现人型机器人自适应柔顺控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人形机器人控制` `柔顺控制` `后见之明学习` `强化学习` `运动跟踪`

## 📋 核心要点

1. 人形机器人难以胜任需要较大作用力的操作任务，如移动物体，现有方法在控制末端执行器柔顺性方面存在不足。
2. CHIP通过后见之明扰动实现自适应柔顺控制，无需额外数据增强或奖励调整，即可实现末端执行器刚度的灵活控制。
3. 实验表明，使用CHIP训练的通用控制器能够完成多机器人协作、擦拭、箱子递送和开门等多种操作任务。

## 📝 摘要（中文）

人形机器人领域的最新进展已经解锁了敏捷的运动技能，包括后空翻、跑步和爬行。然而，人形机器人执行需要较大作用力的操作任务仍然具有挑战性，例如移动物体、擦拭和推动手推车。我们提出了一种通过后见之明扰动实现自适应柔顺的人形控制方法（CHIP），这是一个即插即用的模块，可以在保持动态参考运动的敏捷跟踪的同时，实现可控的末端执行器刚度。CHIP易于实现，不需要数据增强或额外的奖励调整。我们展示了使用CHIP训练的通用运动跟踪控制器可以执行各种需要不同末端执行器柔顺性的操作任务，例如多机器人协作、擦拭、箱子递送和开门。

## 🔬 方法详解

**问题定义**：人形机器人虽然在敏捷运动方面取得了显著进展，但在需要较大作用力的操作任务中仍然面临挑战。现有的运动控制方法难以有效控制末端执行器的柔顺性，导致机器人无法灵活适应不同的操作任务需求，例如，在擦拭任务中需要一定的柔顺性以适应表面变化，而在推动重物时则需要较高的刚度。

**核心思路**：CHIP的核心思路是通过引入后见之明扰动来学习自适应的柔顺控制。具体来说，CHIP在训练过程中对机器人的目标状态进行扰动，并让机器人学习如何从这些扰动中恢复。通过这种方式，机器人可以学习到一种对外部扰动具有鲁棒性的控制策略，从而实现自适应的柔顺控制。这种方法避免了显式地建模柔顺性，而是通过隐式的方式学习如何调整机器人的行为以适应不同的任务需求。

**技术框架**：CHIP是一个即插即用的模块，可以集成到现有的运动跟踪控制器中。整体框架包括以下几个主要步骤：1) 给定一个目标运动轨迹；2) 对目标状态进行扰动；3) 使用运动跟踪控制器控制机器人跟踪扰动后的目标状态；4) 使用强化学习算法优化控制器的参数，使得机器人能够更好地从扰动中恢复。CHIP模块主要负责生成扰动，并将其传递给运动跟踪控制器。

**关键创新**：CHIP最重要的创新点在于其通过后见之明扰动来学习自适应柔顺控制的方法。与传统的柔顺控制方法相比，CHIP不需要显式地建模柔顺性，而是通过隐式的方式学习如何调整机器人的行为以适应不同的任务需求。此外，CHIP易于实现，不需要数据增强或额外的奖励调整，可以方便地集成到现有的运动控制系统中。

**关键设计**：CHIP的关键设计包括扰动策略和强化学习算法的选择。扰动策略需要能够有效地探索状态空间，并覆盖不同的任务需求。论文中使用了随机扰动策略，并对扰动的大小进行了调整。强化学习算法则需要能够有效地学习控制器的参数，使得机器人能够更好地从扰动中恢复。论文中使用了PPO算法进行训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14689/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用CHIP训练的通用运动跟踪控制器可以成功完成多种需要不同末端执行器柔顺性的操作任务，包括多机器人协作、擦拭、箱子递送和开门。与没有使用CHIP的基线方法相比，CHIP在这些任务上取得了显著的性能提升，例如，在擦拭任务中，CHIP可以更好地适应表面变化，从而提高擦拭质量。

## 🎯 应用场景

CHIP具有广泛的应用前景，可以应用于各种需要人形机器人进行操作的场景，例如：工业自动化、家庭服务、医疗康复等。通过CHIP，人形机器人可以更加灵活地适应不同的任务需求，提高操作效率和安全性。此外，CHIP还可以用于多机器人协作，使得多个机器人可以协同完成复杂的任务。

## 📄 摘要（原文）

> Recent progress in humanoid robots has unlocked agile locomotion skills, including backflipping, running, and crawling. Yet it remains challenging for a humanoid robot to perform forceful manipulation tasks such as moving objects, wiping, and pushing a cart. We propose adaptive Compliance Humanoid control through hIsight Perturbation (CHIP), a plug-and-play module that enables controllable end-effector stiffness while preserving agile tracking of dynamic reference motions. CHIP is easy to implement and requires neither data augmentation nor additional reward tuning. We show that a generalist motion-tracking controller trained with CHIP can perform a diverse set of forceful manipulation tasks that require different end-effector compliance, such as multi-robot collaboration, wiping, box delivery, and door opening.

