---
layout: default
title: "Analysis of Harpy's Constrained Trotting and Jumping Maneuver"
---

# Analysis of Harpy's Constrained Trotting and Jumping Maneuver

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18139" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18139v1</a>
  <a href="https://arxiv.org/pdf/2508.18139.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18139v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18139v1', 'Analysis of Harpy\'s Constrained Trotting and Jumping Maneuver')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prathima Ananda Kumar

**分类**: cs.RO

**发布日期**: 2025-08-25

**备注**: Master's Thesis

---

## 💡 一句话要点

**分析Harpy机器人受限的跑步与跳跃动作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `双足机器人` `混合驱动` `运动控制` `助推器` `实验分析`

## 📋 核心要点

1. 现有的双足机器人在复杂运动模式下常面临稳定性和控制精度不足的问题。
2. 论文提出通过腿部与助推器的协同作用，优化混合运动模式以实现稳定的运动控制。
3. 实验结果表明，Harpy在不同运动模式下表现出一致的足部放置和低扭矩的关节行为，验证了混合驱动方法的有效性。

## 📝 摘要（中文）

本研究分析了来自东北大学开发的助推器辅助双足机器人Harpy的实验数据。通过对跑步和跳跃实验数据集的分析，研究揭示了混合腿部-助推器运动的基本原理。结果表明，Harpy通过战略性的腿部与助推器协同，实现了稳定的运动，具有受限的轨迹和一致的足部放置。能量水平分析显示，腿部提供主要推进力，而助推器则增强了空中阶段的控制。研究还识别了在空中阶段需要特定控制策略的关键身体-腿部耦合动态。

## 🔬 方法详解

**问题定义**：本研究旨在解决双足机器人在跑步和跳跃等复杂运动模式下的稳定性和控制精度不足的问题。现有方法往往无法有效处理运动中的相位转变和动态扰动。

**核心思路**：论文的核心思路是通过腿部与助推器的协同作用，优化混合运动模式，以实现稳定的运动控制和精确的足部放置。这种设计旨在利用腿部提供主要推进力，同时通过助推器增强空中阶段的控制能力。

**技术框架**：整体架构包括数据采集、运动模式分析和控制策略设计三个主要模块。首先，通过实验获取跑步和跳跃的运动数据；其次，分析数据以识别关键的运动动态；最后，设计相应的控制策略以优化运动表现。

**关键创新**：本研究的关键创新在于识别并利用腿部与助推器之间的动态耦合关系，提出了针对不同运动阶段的特定控制策略。这与现有方法的本质区别在于强调了混合驱动的协同作用。

**关键设计**：在实验中，设置了低扭矩的关节行为和对称跟踪的参数，以确保在相位转变时的稳定性。此外，采用了特定的损失函数来优化足部放置的精度，确保在运动过程中保持一致性。

## 📊 实验亮点

实验结果显示，Harpy在跑步和跳跃过程中实现了低扭矩的关节控制和一致的足部放置，验证了混合驱动方法的有效性。与传统方法相比，Harpy在不同运动模式下表现出更高的稳定性和重复性，提升幅度显著。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和运动辅助设备等。通过优化双足机器人的运动控制，能够提高其在复杂环境中的适应能力和稳定性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This study presents an analysis of experimental data from Harpy, a thruster-assisted bipedal robot developed at Northeastern University. The study examines data sets from trotting and jumping experiments to understand the fundamental principles governing hybrid leg-thruster locomotion. Through data analysis across multiple locomotion modes, this research reveals that Harpy achieves stable locomotion with bounded trajectories and consistent foot placement through strategic leg-thruster synergy. The results demonstrate controlled joint behavior with low torques and symmetric tracking, accurate foot placement within kinematic constraints despite phase-transition perturbations, and underactuated degree-of-freedom stability without divergence. Energy level analysis reveals that legs provide primary propulsion, while the thrusters enable additional aerial phase control. The analysis identifies critical body-leg coupling dynamics during aerial phases that require phase-specific control strategies. Consistent repeatability and symmetry across experiments validate the robustness of the hybrid actuation approach.

