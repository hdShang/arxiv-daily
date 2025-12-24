---
layout: default
title: "SurfAAV: Design and Implementation of a Novel Multimodal Surfing Aquatic-Aerial Vehicle"
---

# SurfAAV: Design and Implementation of a Novel Multimodal Surfing Aquatic-Aerial Vehicle

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15450" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15450v1</a>
  <a href="https://arxiv.org/pdf/2506.15450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15450v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15450v1', 'SurfAAV: Design and Implementation of a Novel Multimodal Surfing Aquatic-Aerial Vehicle')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Liu, Junhao Xiao, Hao Lin, Yue Cao, Hui Peng, Kaihong Huang, Huimin Lu

**分类**: cs.RO

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出SurfAAV以解决水下、表面和空中运动效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水面-空中机器人` `多模态运动` `水下导航` `表面滑行` `差动推力矢量水翼`

## 📋 核心要点

1. 现有水面-空中机器人在同时进行水下、表面和空中运动时效率不足，限制了其应用范围。
2. 本文提出SurfAAV，通过新型差动推力矢量水翼设计，整合水下导航、表面滑行和空中飞行能力。
3. 实验结果显示，SurfAAV的最大表面滑行速度为7.96 m/s，最大水下速度为3.1 m/s，超越现有同类机器人。

## 📝 摘要（中文）

尽管水面-空中机器人研究取得了显著进展，但现有配置在同时进行水下、表面和空中运动时效率较低。本文提出了一种新型的多模态冲浪水面-空中车辆SurfAAV，能够有效整合水下导航、表面滑行和空中飞行能力。得益于新型差动推力矢量水翼的设计，SurfAAV无需浮力调整系统即可实现高效的表面滑行和水下导航。这种设计为水面和水下任务提供了灵活的操作能力，使机器人能够快速进行水下监测。此外，当需要到达另一个水体时，SurfAAV可以通过滑行起飞切换到空中模式，飞往目标水域执行相应任务。本文的主要贡献在于提出了一种新的水下、表面和空中运动解决方案，设计了新型混合原型概念，开发了所需的控制律，并验证了机器人成功执行表面滑行和滑行起飞的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有水面-空中机器人在水下、表面和空中运动效率低下的问题，现有方法往往需要复杂的浮力调整系统，限制了其灵活性和应用场景。

**核心思路**：SurfAAV通过创新的差动推力矢量水翼设计，能够在不依赖浮力调整的情况下，实现高效的水下导航和表面滑行，从而提升多模态运动的效率。

**技术框架**：SurfAAV的整体架构包括水下导航模块、表面滑行模块和空中飞行模块，三者通过控制系统进行协调，确保在不同环境下的高效切换和操作。

**关键创新**：SurfAAV的核心创新在于其差动推力矢量水翼设计，使得机器人能够在水下和表面滑行时无需浮力调整，显著提高了运动效率和灵活性。

**关键设计**：在设计中，SurfAAV的推力矢量控制通过精确的参数设置和控制律实现，确保在不同模式下的稳定性和响应速度。

## 📊 实验亮点

实验结果表明，SurfAAV在表面滑行中的最大速度达到7.96 m/s，水下速度为3.1 m/s，均超过现有水面-空中车辆的性能。这一显著提升展示了其在多模态运动中的优越性。

## 🎯 应用场景

SurfAAV的设计使其在水下监测、环境监测、海洋研究等领域具有广泛的应用潜力。其高效的多模态运动能力能够满足复杂环境下的任务需求，未来可能在海洋探测、救援行动等场景中发挥重要作用。

## 📄 摘要（原文）

> Despite significant advancements in the research of aquatic-aerial robots, existing configurations struggle to efficiently perform underwater, surface, and aerial movement simultaneously. In this paper, we propose a novel multimodal surfing aquatic-aerial vehicle, SurfAAV, which efficiently integrates underwater navigation, surface gliding, and aerial flying capabilities. Thanks to the design of the novel differential thrust vectoring hydrofoil, SurfAAV can achieve efficient surface gliding and underwater navigation without the need for a buoyancy adjustment system. This design provides flexible operational capabilities for both surface and underwater tasks, enabling the robot to quickly carry out underwater monitoring activities. Additionally, when it is necessary to reach another water body, SurfAAV can switch to aerial mode through a gliding takeoff, flying to the target water area to perform corresponding tasks. The main contribution of this letter lies in proposing a new solution for underwater, surface, and aerial movement, designing a novel hybrid prototype concept, developing the required control laws, and validating the robot's ability to successfully perform surface gliding and gliding takeoff. SurfAAV achieves a maximum surface gliding speed of 7.96 m/s and a maximum underwater speed of 3.1 m/s. The prototype's surface gliding maneuverability and underwater cruising maneuverability both exceed those of existing aquatic-aerial vehicles.

