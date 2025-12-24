---
layout: default
title: "Prepare Before You Act: Learning From Humans to Rearrange Initial States"
---

# Prepare Before You Act: Learning From Humans to Rearrange Initial States

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18043" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18043v1</a>
  <a href="https://arxiv.org/pdf/2509.18043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18043v1', 'Prepare Before You Act: Learning From Humans to Rearrange Initial States')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinlong Dai, Andre Keyser, Dylan P. Losey

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-09-22

---

## 💡 一句话要点

**提出ReSET，通过模仿学习人类预处理环境，提升机器人操作任务的泛化性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模仿学习` `机器人操作` `环境预处理` `泛化能力` `人类行为模仿`

## 📋 核心要点

1. 模仿学习在复杂操作任务中面临泛化性挑战，尤其是在初始状态分布偏移时表现不佳。
2. ReSET算法模仿人类在操作前的环境预处理行为，通过重构场景来提升策略的泛化能力。
3. 实验表明，ReSET在相同训练数据下，能显著提升机器人操作任务的鲁棒性，优于现有方法。

## 📝 摘要（中文）

模仿学习(IL)在各种操作任务中已被证明是有效的。然而，当面临分布外的观察时，例如当目标对象处于先前未见的位置或被其他对象遮挡时，IL策略常常会遇到困难。在这种情况下，当前的IL方法需要大量的演示才能达到鲁棒和可泛化的行为。但是，当人类面对这些非典型的初始状态时，我们通常会重新排列环境，以便更好地执行任务。例如，一个人可能会旋转咖啡杯，以便更容易抓住把手，或者推开一个盒子，以便他们可以直接抓住他们的目标对象。在这项工作中，我们试图让机器人学习者具备同样的能力：使机器人能够在执行其给定策略之前准备环境。我们提出ReSET，一种算法，它接受初始状态（这些状态在策略的分布之外），并自主地修改对象姿势，使重构后的场景类似于训练数据。从理论上讲，我们证明了这个两步过程（在展开给定策略之前重新排列环境）减少了泛化差距。在实践中，我们的ReSET算法将与动作无关的人类视频与与任务无关的遥操作数据相结合，以 i) 决定何时修改场景，ii) 预测人类会采取哪些简化动作，以及 iii) 将这些预测映射到机器人动作原语。与扩散策略、VLAs和其他基线的比较表明，使用ReSET准备环境能够以相同的总训练数据实现更强大的任务执行。

## 🔬 方法详解

**问题定义**：现有模仿学习方法在面对与训练数据分布不同的初始状态时，泛化能力较差。例如，目标物体位置异常或被遮挡时，机器人难以成功完成任务。需要大量的额外训练数据才能提升鲁棒性，但成本很高。

**核心思路**：模仿人类在执行任务前会先对环境进行预处理，例如调整物体位置，使其更易于操作。ReSET算法旨在让机器人学习这种预处理能力，将初始状态调整到更接近训练数据的分布，从而提高后续策略的成功率。

**技术框架**：ReSET包含三个主要步骤：1) 决定何时需要修改场景；2) 预测人类会采取的简化动作；3) 将预测的动作映射到机器人的动作原语。算法利用动作无关的人类视频和任务无关的遥操作数据进行学习。整体流程是，当输入一个初始状态时，ReSET首先判断是否需要进行环境重构。如果需要，则预测人类会采取的动作，并将这些动作转化为机器人可以执行的动作，从而改变环境状态。最后，执行预先训练好的策略。

**关键创新**：ReSET的核心创新在于将环境预处理的概念引入到模仿学习中，通过模仿人类的行为来改善初始状态，从而提升策略的泛化能力。与传统方法直接学习操作策略不同，ReSET学习的是如何改变环境，使其更适合执行策略。

**关键设计**：ReSET使用动作无关的人类视频来学习人类如何预处理环境。同时，利用任务无关的遥操作数据来学习如何将人类的动作转化为机器人的动作原语。具体的网络结构和损失函数细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

实验结果表明，ReSET算法在环境预处理后，能够显著提升机器人操作任务的成功率。与扩散策略、VLAs等基线方法相比，ReSET在相同训练数据量下，能够实现更鲁棒的任务执行。具体的性能提升数据在摘要中未给出，属于未知信息。

## 🎯 应用场景

ReSET算法可应用于各种机器人操作任务，尤其是在复杂、非结构化的环境中。例如，在家庭服务机器人中，可以帮助机器人整理物品、调整物体位置，使其更容易抓取和使用。在工业自动化领域，可以用于处理生产线上位置不确定的零件，提高生产效率。该研究有助于提升机器人的自主性和适应性，使其能够更好地应对真实世界的挑战。

## 📄 摘要（原文）

> Imitation learning (IL) has proven effective across a wide range of manipulation tasks. However, IL policies often struggle when faced with out-of-distribution observations; for instance, when the target object is in a previously unseen position or occluded by other objects. In these cases, extensive demonstrations are needed for current IL methods to reach robust and generalizable behaviors. But when humans are faced with these sorts of atypical initial states, we often rearrange the environment for more favorable task execution. For example, a person might rotate a coffee cup so that it is easier to grasp the handle, or push a box out of the way so they can directly grasp their target object. In this work we seek to equip robot learners with the same capability: enabling robots to prepare the environment before executing their given policy. We propose ReSET, an algorithm that takes initial states -- which are outside the policy's distribution -- and autonomously modifies object poses so that the restructured scene is similar to training data. Theoretically, we show that this two step process (rearranging the environment before rolling out the given policy) reduces the generalization gap. Practically, our ReSET algorithm combines action-agnostic human videos with task-agnostic teleoperation data to i) decide when to modify the scene, ii) predict what simplifying actions a human would take, and iii) map those predictions into robot action primitives. Comparisons with diffusion policies, VLAs, and other baselines show that using ReSET to prepare the environment enables more robust task execution with equal amounts of total training data. See videos at our project website: https://reset2025paper.github.io/

