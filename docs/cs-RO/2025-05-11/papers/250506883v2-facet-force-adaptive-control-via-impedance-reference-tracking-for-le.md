---
layout: default
title: FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots
---

# FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06883" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06883v2</a>
  <a href="https://arxiv.org/pdf/2505.06883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06883v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06883v2', 'FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Botian Xu, Haoyang Weng, Qingzhou Lu, Yang Gao, Huazhe Xu

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-11 (更新: 2025-05-19)

---

## 💡 一句话要点

**提出FACET以解决腿部机器人在力交互中的控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `腿部机器人` `强化学习` `力自适应控制` `合规性` `鲁棒性` `虚拟弹簧` `冲击控制`

## 📋 核心要点

1. 现有的腿部机器人控制方法对力的敏感性不足，导致在强力交互中表现出僵硬和危险的行为。
2. 本文提出的FACET方法通过模仿虚拟质量-弹簧-阻尼器系统，利用强化学习实现力自适应控制。
3. 实验结果显示，四足机器人在大冲击下的鲁棒性提高，冲击减少达80%，并能有效进行大力交互。

## 📝 摘要（中文）

强化学习（RL）在腿部机器人控制方面取得了显著进展，使其能够在多样化地形上行走并具备复杂的运动操控能力。然而，现有基于位置或速度跟踪的目标对机器人所经历的力缺乏敏感性，导致机器人在力交互中表现出僵硬且潜在危险的行为。为了解决这一局限性，本文提出了力自适应控制（FACET），通过模仿虚拟质量-弹簧-阻尼器系统，利用RL训练控制策略，从而在外部力作用下实现精细控制。仿真结果表明，四足机器人在大冲击下（高达200 Ns）表现出更好的鲁棒性，并实现了80%的冲击减少。该策略已在物理机器人上部署，展示了其在大力交互中的合规性和能力。

## 🔬 方法详解

**问题定义**：本文旨在解决腿部机器人在强力交互中控制不灵活的问题。现有方法多基于位置或速度跟踪，未能有效应对外部力的影响，导致机器人行为僵硬且潜在危险。

**核心思路**：FACET方法通过模仿虚拟质量-弹簧-阻尼器系统，利用强化学习训练控制策略，使机器人能够在外部力作用下进行精细控制，增强其合规性和鲁棒性。

**技术框架**：该方法的整体架构包括强化学习训练模块、虚拟弹簧参数调整模块和力反馈控制模块。通过不断迭代训练，优化控制策略以适应不同的外部力环境。

**关键创新**：FACET的核心创新在于将力自适应控制与强化学习结合，突破了传统控制方法对力的忽视，使机器人在复杂环境中能够灵活应对外部冲击。

**关键设计**：在设计中，采用了特定的损失函数来平衡位置跟踪与力反馈，同时优化了网络结构以提高训练效率和控制精度。

## 📊 实验亮点

实验结果表明，四足机器人在面对高达200 Ns的冲击时，表现出显著的鲁棒性，冲击减少达80%。此外，机器人在进行大力交互时，展现出良好的合规性，能够有效拉动其重量的2/3的负载。

## 🎯 应用场景

FACET方法具有广泛的应用潜力，尤其在复杂环境下的腿部机器人控制、救援任务、物流搬运等领域。其能够有效提升机器人在动态环境中的适应能力和安全性，未来可能推动机器人在更多实际应用中的普及与发展。

## 📄 摘要（原文）

> Reinforcement learning (RL) has made significant strides in legged robot control, enabling locomotion across diverse terrains and complex loco-manipulation capabilities. However, the commonly used position or velocity tracking-based objectives are agnostic to forces experienced by the robot, leading to stiff and potentially dangerous behaviors and poor control during forceful interactions. To address this limitation, we present \emph{Force-Adaptive Control via Impedance Reference Tracking} (FACET). Inspired by impedance control, we use RL to train a control policy to imitate a virtual mass-spring-damper system, allowing fine-grained control under external forces by manipulating the virtual spring. In simulation, we demonstrate that our quadruped robot achieves improved robustness to large impulses (up to 200 Ns) and exhibits controllable compliance, achieving an 80% reduction in collision impulse. The policy is deployed to a physical robot to showcase both compliance and the ability to engage with large forces by kinesthetic control and pulling payloads up to 2/3 of its weight. Further extension to a legged loco-manipulator and a humanoid shows the applicability of our method to more complex settings to enable whole-body compliance control. Project Website: https://facet.pages.dev/

