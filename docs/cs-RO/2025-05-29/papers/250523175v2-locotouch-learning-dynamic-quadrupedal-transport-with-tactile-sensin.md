---
layout: default
title: "LocoTouch: Learning Dynamic Quadrupedal Transport with Tactile Sensing"
---

# LocoTouch: Learning Dynamic Quadrupedal Transport with Tactile Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23175" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23175v2</a>
  <a href="https://arxiv.org/pdf/2505.23175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23175v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23175v2', 'LocoTouch: Learning Dynamic Quadrupedal Transport with Tactile Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changyi Lin, Yuxin Ray Song, Boda Huo, Mingyang Yu, Yikai Wang, Shiqi Liu, Yuxiang Yang, Wenhao Yu, Tingnan Zhang, Jie Tan, Yiyue Luo, Ding Zhao

**分类**: cs.RO

**发布日期**: 2025-05-29 (更新: 2025-08-30)

**备注**: Project page: https://linchangyi1.github.io/LocoTouch

---

## 💡 一句话要点

**提出LocoTouch以解决四足机器人动态物体运输问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `触觉感知` `动态物体交互` `长距离运输` `高密度传感器` `仿真环境` `鲁棒性` `运输策略`

## 📋 核心要点

1. 现有四足机器人在动态物体交互中缺乏精确的触觉感知与控制，尤其在长距离运输不稳定物体时表现不佳。
2. LocoTouch系统通过高密度触觉传感器和高保真仿真环境，训练触觉感知的运输策略，提升机器人对动态物体的控制能力。
3. 实验结果表明，LocoTouch能够在现实环境中可靠运输多种不稳定圆柱形物体，表现出优越的鲁棒性和适应性。

## 📝 摘要（中文）

四足机器人在复杂地形中展现出卓越的灵活性和鲁棒性，但在动态物体交互中面临挑战，尤其是在长距离运输不稳定圆柱形物体时。为此，本文提出LocoTouch系统，通过高密度分布式触觉传感器覆盖机器人背部，提升触觉反馈的利用效率。我们开发了高保真触觉信号的仿真环境，并采用两阶段学习管道训练触觉感知的运输策略。此外，设计了一种新颖的奖励函数，以促进鲁棒、对称和频率自适应的运动步态。LocoTouch在仿真训练后能够零-shot转移到现实世界，可靠地运输各种尺寸、重量和表面特性的圆柱形物体，并在长距离、崎岖地形和剧烈扰动下保持鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在动态物体运输中的触觉感知与控制问题。现有方法在长距离运输不稳定圆柱形物体时，通常依赖定制的固定机制，导致稳定性不足。

**核心思路**：LocoTouch通过在机器人背部设计高密度分布式触觉传感器，增强触觉反馈的感知能力，并利用高保真仿真环境进行训练，以实现对动态物体的有效控制。

**技术框架**：LocoTouch的整体架构包括触觉传感器模块、仿真环境、两阶段学习管道和奖励函数设计。首先，通过触觉传感器收集数据，然后在仿真环境中训练策略，最后将训练结果迁移到现实世界。

**关键创新**：LocoTouch的主要创新在于结合高密度触觉传感器与高保真仿真环境，形成了一种新的训练和控制方法，显著提升了机器人在动态物体运输中的表现。

**关键设计**：在设计中，采用了高密度传感器布局以覆盖更大区域，损失函数和奖励函数经过精心设计，以促进鲁棒性和适应性步态的学习。

## 📊 实验亮点

实验结果显示，LocoTouch在现实环境中成功运输多种尺寸和重量的圆柱形物体，表现出优越的鲁棒性，能够在长距离和不平坦地形中稳定运行。与基线方法相比，LocoTouch在运输成功率和适应性方面显著提升，展示了其在动态物体交互中的有效性。

## 🎯 应用场景

LocoTouch的研究成果在物流、仓储和救援等领域具有广泛的应用潜力。通过提升四足机器人在动态环境中的物体运输能力，可以有效提高自动化水平，降低人力成本，并在复杂场景中实现更高效的物体搬运。未来，该技术有望推动机器人在更多实际应用中的普及与发展。

## 📄 摘要（原文）

> Quadrupedal robots have demonstrated remarkable agility and robustness in traversing complex terrains. However, they struggle with dynamic object interactions, where contact must be precisely sensed and controlled. To bridge this gap, we present LocoTouch, a system that equips quadrupedal robots with tactile sensing to address a particularly challenging task in this category: long-distance transport of unsecured cylindrical objects, which typically requires custom mounting or fastening mechanisms to maintain stability. For efficient large-area tactile sensing, we design a high-density distributed tactile sensor that covers the entire back of the robot. To effectively leverage tactile feedback for robot control, we develop a simulation environment with high-fidelity tactile signals, and train tactile-aware transport policies using a two-stage learning pipeline. Furthermore, we design a novel reward function to promote robust, symmetric, and frequency-adaptive locomotion gaits. After training in simulation, LocoTouch transfers zero-shot to the real world, reliably transporting a wide range of unsecured cylindrical objects with diverse sizes, weights, and surface properties. Moreover, it remains robust over long distances, on uneven terrain, and under severe perturbations.

