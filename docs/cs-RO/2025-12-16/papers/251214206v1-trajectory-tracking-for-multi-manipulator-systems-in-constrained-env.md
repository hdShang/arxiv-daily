---
layout: default
title: Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments
---

# Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14206v1</a>
  <a href="https://arxiv.org/pdf/2512.14206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14206v1', 'Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayank Sewlia, Christos K. Verginis, Dimos V. Dimarogonas

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出多速率规划控制框架，解决约束环境下多机械臂系统的轨迹跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多机械臂系统` `轨迹跟踪` `约束环境` `STL规划` `逆运动学`

## 📋 核心要点

1. 现有方法难以在复杂约束环境中实现多机械臂系统的精确轨迹跟踪，尤其是在考虑机器人动力学和几何约束时。
2. 论文提出一种多速率规划和控制框架，通过离线生成轨迹和在线反馈控制相结合，实现多机械臂的协同运动。
3. 通过高保真物理仿真，验证了该方法在三个Franka Emika Panda移动机械臂上的有效性，展示了其在复杂环境中的轨迹跟踪能力。

## 📝 摘要（中文）

本文研究了移动多机械臂系统在复杂约束环境中协同操作的问题，该环境包含障碍物和狭窄通道，并具有时空任务规范。任务要求在满足连续机器人动力学和离散几何约束（由障碍物和狭窄通道引起）的同时，运输抓取的物体。为了解决这种混合结构，我们提出了一种多速率规划和控制框架，该框架结合了离线生成满足STL的对象轨迹和无碰撞的基座足迹，以及在线约束逆运动学和连续时间反馈控制。由此产生的闭环系统能够协调多个机械臂的重构，同时跟踪期望的物体运动。该方法在高度逼真的物理模拟中使用三个Franka Emika Panda移动机械臂刚性抓取一个物体进行了评估。

## 🔬 方法详解

**问题定义**：论文旨在解决多机械臂系统在复杂约束环境中进行轨迹跟踪的问题。现有方法在处理此类问题时，通常难以同时满足机器人动力学约束、几何约束（如避障和通过狭窄通道）以及时空任务规范。这些约束使得轨迹规划和控制变得非常复杂，尤其是在需要多个机械臂协同操作的情况下。

**核心思路**：论文的核心思路是将轨迹规划和控制分解为多个速率不同的层次。离线阶段，利用信号时序逻辑（STL）生成满足任务规范的对象轨迹和无碰撞的基座足迹。在线阶段，利用约束逆运动学和连续时间反馈控制，实现机械臂的协调重构和精确轨迹跟踪。这种分层方法能够有效地处理混合约束，并提高系统的鲁棒性。

**技术框架**：该方法的技术框架主要包含以下几个模块：1) 离线轨迹规划器：基于STL生成满足任务规范的对象轨迹和基座足迹，同时考虑环境中的障碍物和狭窄通道。2) 在线约束逆运动学：根据期望的对象轨迹和基座位置，计算每个机械臂的关节角度，并确保满足机械臂的运动学约束。3) 连续时间反馈控制器：利用反馈控制，补偿系统误差和扰动，实现精确的轨迹跟踪。整个框架采用多速率结构，离线规划以较低的速率进行，在线控制以较高的速率进行。

**关键创新**：该论文的关键创新在于将STL用于离线轨迹规划，并将其与在线约束逆运动学和连续时间反馈控制相结合。这种混合方法能够有效地处理复杂约束，并实现多机械臂系统的协同运动。此外，多速率结构的设计也提高了系统的效率和鲁棒性。

**关键设计**：在离线轨迹规划中，STL规范被用于描述任务需求，例如对象需要经过的特定区域和需要避免的障碍物。在在线约束逆运动学中，采用了优化方法来求解关节角度，同时考虑机械臂的运动学约束和避免碰撞。在连续时间反馈控制中，采用了PID控制器或更高级的控制算法，以实现精确的轨迹跟踪。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过高保真物理仿真验证了该方法的有效性。实验结果表明，该方法能够使三个Franka Emika Panda移动机械臂在复杂约束环境中协同操作，精确地跟踪期望的对象轨迹。虽然论文中没有提供具体的性能数据和对比基线，但仿真结果展示了该方法在实际应用中的潜力。

## 🎯 应用场景

该研究成果可应用于自动化装配、物流搬运、灾难救援等领域。在这些场景中，多机械臂系统需要在复杂约束环境中协同操作，完成特定的任务。该方法能够提高系统的灵活性、鲁棒性和安全性，从而实现更高效、更可靠的自动化作业。未来，该研究可以进一步扩展到更多类型的机械臂系统和更复杂的任务场景。

## 📄 摘要（原文）

> We consider the problem of cooperative manipulation by a mobile multi-manipulator system operating in obstacle-cluttered and highly constrained environments under spatio-temporal task specifications. The task requires transporting a grasped object while respecting both continuous robot dynamics and discrete geometric constraints arising from obstacles and narrow passages. To address this hybrid structure, we propose a multi-rate planning and control framework that combines offline generation of an STL-satisfying object trajectory and collision-free base footprints with online constrained inverse kinematics and continuous-time feedback control. The resulting closed-loop system enables coordinated reconfiguration of multiple manipulators while tracking the desired object motion. The approach is evaluated in high-fidelity physics simulations using three Franka Emika Panda mobile manipulators rigidly grasping an object.

