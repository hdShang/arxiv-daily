---
layout: default
title: Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation
---

# Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20829" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20829v2</a>
  <a href="https://arxiv.org/pdf/2505.20829.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20829v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20829v2', 'Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiyuan Zhi, Peiyang Li, Jianqin Yin, Baoxiong Jia, Siyuan Huang

**分类**: cs.RO

**发布日期**: 2025-05-27 (更新: 2025-10-04)

**备注**: website: https://unified-force.github.io/

---

## 💡 一句话要点

**提出统一策略以解决腿式机器人位置与力控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `腿式机器人` `位置控制` `力控制` `强化学习` `操控任务` `接触交互` `策略学习`

## 📋 核心要点

1. 现有的机器人运动控制方法往往单独学习位置或力控制，缺乏对两者的联合建模，导致在复杂环境中的表现不足。
2. 本文提出了一种新的统一策略，能够在不依赖力传感器的情况下，联合学习位置和力控制，从而实现更灵活的操控能力。
3. 实验结果表明，所提出的策略在四个复杂的操控任务中成功率提高了约39.5%，验证了其在多种场景下的有效性和鲁棒性。

## 📝 摘要（中文）

机器人运动操作任务通常涉及与环境的接触交互，需要同时建模接触力和机器人位置。然而，现有的视觉运动策略往往仅关注位置或力控制，忽视了它们的共同学习。本文提出了首个统一策略，针对腿式机器人在不依赖力传感器的情况下联合建模力和位置控制。通过模拟多种位置和力命令的组合以及外部干扰力，利用强化学习学习出一种策略，该策略能够从历史机器人状态中估计力，并通过位置和速度调整进行补偿。这一策略支持多种操控行为，并在四个复杂的接触丰富操控任务中相比位置控制策略提高了约39.5%的成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决腿式机器人在运动操作中位置与力控制的联合建模问题。现有方法通常只关注其中一方面，导致在复杂环境中的操控能力不足。

**核心思路**：提出的统一策略通过强化学习，利用历史状态估计接触力，并通过调整位置和速度来进行补偿，从而实现位置与力的共同控制。

**技术框架**：整体架构包括多个模块：首先是状态历史的收集与处理，然后是力的估计模块，最后是基于估计结果的控制策略调整。

**关键创新**：最重要的创新在于首次实现了不依赖力传感器的情况下，联合学习位置与力控制，显著提升了机器人在接触丰富环境中的操控能力。

**关键设计**：在设计中，采用了特定的损失函数来平衡位置与力的控制目标，并优化了网络结构以提高策略的学习效率和准确性。通过多种参数设置，确保了模型的稳定性和鲁棒性。

## 📊 实验亮点

实验结果显示，所提出的统一策略在四个复杂的接触丰富操控任务中，相比传统的仅位置控制策略，成功率提高了约39.5%。这一显著提升验证了该策略在多样化操控行为中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人以及工业自动化等场景，能够在复杂环境中实现更高效的操控和交互，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Robotic loco-manipulation tasks often involve contact-rich interactions with the environment, requiring the joint modeling of contact force and robot position. However, recent visuomotor policies often focus solely on learning position or force control, overlooking their co-learning. In this work, we propose the first unified policy for legged robots that jointly models force and position control learned without reliance on force sensors. By simulating diverse combinations of position and force commands alongside external disturbance forces, we use reinforcement learning to learn a policy that estimates forces from historical robot states and compensates for them through position and velocity adjustments. This policy enables a wide range of manipulation behaviors under varying force and position inputs, including position tracking, force application, force tracking, and compliant interactions. Furthermore, we demonstrate that the learned policy enhances trajectory-based imitation learning pipelines by incorporating essential contact information through its force estimation module, achieving approximately 39.5% higher success rates across four challenging contact-rich manipulation tasks compared to position-control policies. Extensive experiments on both a quadrupedal manipulator and a humanoid robot validate the versatility and robustness of the proposed policy across diverse scenarios.

