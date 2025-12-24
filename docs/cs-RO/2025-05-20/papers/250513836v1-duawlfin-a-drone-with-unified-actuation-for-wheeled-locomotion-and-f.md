---
layout: default
title: "Duawlfin: A Drone with Unified Actuation for Wheeled Locomotion and Flight Operation"
---

# Duawlfin: A Drone with Unified Actuation for Wheeled Locomotion and Flight Operation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13836" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13836v1</a>
  <a href="https://arxiv.org/pdf/2505.13836.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13836v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13836v1', 'Duawlfin: A Drone with Unified Actuation for Wheeled Locomotion and Flight Operation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jerry Tang, Ruiqi Zhang, Kaan Beyduz, Yiwei Jiang, Cody Wiebe, Haoyu Zhang, Osaruese Asoro, Mark W. Mueller

**分类**: cs.RO

**发布日期**: 2025-05-20

**备注**: 8 pages, 8 figures

---

## 💡 一句话要点

**提出Duawlfin以实现高效的双向地面移动和飞行操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机` `地面移动` `飞行操作` `能效优化` `控制策略` `城市物流` `室内导航`

## 📋 核心要点

1. 现有的混合动力无人机在地面移动和飞行操作中存在能耗高和系统复杂等问题。
2. Duawlfin通过统一驱动设计，利用四旋翼电机和单向轴承实现地面与飞行模式的无缝切换。
3. 实验结果表明，Duawlfin在飞行模式下性能稳定，地面模式下能有效攀爬30°坡度，具备接近1g的横向加速度。

## 📝 摘要（中文）

本文介绍了Duawlfin，这是一种具有统一驱动的无人机，能够实现高效的双向地面移动和飞行操作。与现有的混合设计不同，Duawlfin通过仅利用标准的四旋翼电机和引入单向轴承的差速驱动系统，消除了对额外驱动器或螺旋桨驱动的地面推进的需求。这一创新简化了机械系统，显著降低了能耗，并防止了螺旋桨在地面附近旋转所造成的干扰，如尘埃对传感器的影响。此外，单向轴承最小化了电机在地面模式下向螺旋桨的功率传输，使得该车辆能够安全地在人群附近操作。我们提供了详细的机械设计，展示了快速平滑的模式切换控制策略，并通过广泛的实验测试验证了该概念。

## 🔬 方法详解

**问题定义**：本文旨在解决现有混合动力无人机在地面移动和飞行操作中的能耗高、系统复杂及干扰问题。现有方法通常需要额外的驱动器，导致机械系统复杂且能效低下。

**核心思路**：Duawlfin的核心思路是通过仅使用标准四旋翼电机和单向轴承的差速驱动系统，实现高效的地面移动与飞行操作。这种设计简化了机械结构，降低了能耗，并减少了对环境的干扰。

**技术框架**：Duawlfin的整体架构包括四个主要模块：四旋翼电机、单向轴承差速驱动系统、控制策略模块和传感器系统。控制策略模块负责在飞行模式和地面模式之间进行快速平滑的切换。

**关键创新**：最重要的技术创新在于采用单向轴承来实现地面模式下的动力传输最小化，这与现有方法的多驱动器设计形成了本质区别。

**关键设计**：在设计中，单向轴承的选择和配置至关重要，确保在地面模式下电机的功率不会过多传递给螺旋桨。此外，控制策略的设计也考虑了快速响应和稳定性，以实现无缝的模式切换。

## 📊 实验亮点

实验结果显示，Duawlfin在飞行模式下的稳定性与传统四旋翼无人机相当，而在地面模式下能够有效攀爬30°的坡度，并实现接近1g的横向加速度，展示了其卓越的性能和灵活性。

## 🎯 应用场景

Duawlfin的设计具有广泛的应用潜力，尤其在城市物流和室内导航等领域。其高效的地面移动能力和稳定的飞行性能，使其能够在复杂环境中灵活操作，提升了无人机在实际应用中的价值和效率。未来，Duawlfin可能会在紧急救援、监测和配送等场景中发挥重要作用。

## 📄 摘要（原文）

> This paper presents Duawlfin, a drone with unified actuation for wheeled locomotion and flight operation that achieves efficient, bidirectional ground mobility. Unlike existing hybrid designs, Duawlfin eliminates the need for additional actuators or propeller-driven ground propulsion by leveraging only its standard quadrotor motors and introducing a differential drivetrain with one-way bearings. This innovation simplifies the mechanical system, significantly reduces energy usage, and prevents the disturbance caused by propellers spinning near the ground, such as dust interference with sensors. Besides, the one-way bearings minimize the power transfer from motors to propellers in the ground mode, which enables the vehicle to operate safely near humans. We provide a detailed mechanical design, present control strategies for rapid and smooth mode transitions, and validate the concept through extensive experimental testing. Flight-mode tests confirm stable aerial performance comparable to conventional quadcopters, while ground-mode experiments demonstrate efficient slope climbing (up to 30°) and agile turning maneuvers approaching 1g lateral acceleration. The seamless transitions between aerial and ground modes further underscore the practicality and effectiveness of our approach for applications like urban logistics and indoor navigation. All the materials including 3-D model files, demonstration video and other assets are open-sourced at https://sites.google.com/view/Duawlfin.

