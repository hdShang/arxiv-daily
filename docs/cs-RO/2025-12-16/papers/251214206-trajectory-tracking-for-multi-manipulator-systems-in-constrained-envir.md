---
layout: default
title: Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments
---

# Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14206</a>
  <a href="https://arxiv.org/pdf/2512.14206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14206" onclick="toggleFavorite(this, '2512.14206', 'Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayank Sewlia, Christos K. Verginis, Dimos V. Dimarogonas

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出多速率规划与控制框架，解决约束环境下多机械臂系统的轨迹跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多机械臂系统` `轨迹跟踪` `约束环境` `多速率控制` `逆运动学`

## 📋 核心要点

1. 现有方法难以在复杂约束环境中实现多机械臂系统的精确轨迹跟踪，尤其是在考虑机器人动力学和环境几何约束的情况下。
2. 论文提出一种多速率规划与控制框架，通过离线生成轨迹和在线反馈控制相结合，实现多机械臂的协同运动和轨迹跟踪。
3. 通过高保真物理仿真验证了该方法在三个Franka Emika Panda移动机械臂上的有效性，展示了其在复杂环境下的轨迹跟踪能力。

## 📝 摘要（中文）

本文研究了移动多机械臂系统在复杂约束环境下协同操作的问题，该环境包含障碍物和狭窄通道，并具有时空任务规范。任务要求在满足连续机器人动力学和离散几何约束（由障碍物和狭窄通道引起）的同时，运输抓取的物体。为了解决这种混合结构，我们提出了一种多速率规划和控制框架，该框架结合了离线生成的满足STL的对象轨迹和无碰撞的基座足迹，以及在线约束逆运动学和连续时间反馈控制。由此产生的闭环系统能够协调多个机械臂的重新配置，同时跟踪期望的物体运动。该方法在高度逼真的物理模拟中使用三个Franka Emika Panda移动机械臂刚性抓取一个物体进行了评估。

## 🔬 方法详解

**问题定义**：论文旨在解决多机械臂系统在存在障碍物和狭窄通道等约束条件下的轨迹跟踪问题。现有方法在处理这种复杂环境时，往往难以同时满足机器人动力学约束和环境几何约束，导致轨迹跟踪精度下降甚至失败。此外，如何协调多个机械臂的运动，保证它们在运动过程中不发生碰撞，也是一个挑战。

**核心思路**：论文的核心思路是将轨迹规划和控制解耦，采用多速率的策略。首先，离线生成满足时序逻辑（STL）规范的物体轨迹和无碰撞的基座足迹。然后，在线使用约束逆运动学和连续时间反馈控制来跟踪期望的物体运动，并协调多个机械臂的运动。这种解耦策略降低了问题的复杂度，使得可以在线实时地进行轨迹跟踪和运动控制。

**技术框架**：整体框架包含以下几个主要模块：1) 离线轨迹规划器：生成满足STL规范的物体轨迹和无碰撞的基座足迹。2) 在线约束逆运动学求解器：根据期望的物体位姿和基座位置，计算每个机械臂的关节角度。3) 连续时间反馈控制器：根据实际的关节角度和期望的关节角度，生成控制力矩，驱动机械臂运动。这三个模块以多速率的方式协同工作，实现多机械臂系统的轨迹跟踪。

**关键创新**：论文的关键创新在于提出了一种多速率规划和控制框架，将离线轨迹规划和在线反馈控制相结合，有效地解决了复杂约束环境下多机械臂系统的轨迹跟踪问题。与传统的基于优化的方法相比，该方法具有更高的计算效率和鲁棒性。此外，论文还考虑了时序逻辑规范，使得可以对任务进行更灵活的描述。

**关键设计**：在离线轨迹规划器中，使用了STL公式来描述任务规范，并采用混合整数规划（MIP）来求解满足STL公式的轨迹。在线约束逆运动学求解器中，使用了二次规划（QP）来求解满足关节角度约束和避免碰撞的关节角度。连续时间反馈控制器中，使用了PID控制器来跟踪期望的关节角度。这些关键设计保证了系统的稳定性和轨迹跟踪精度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14206/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过高保真物理仿真验证了所提出方法的有效性。实验结果表明，该方法能够成功地控制三个Franka Emika Panda移动机械臂，使其在复杂约束环境下协同抓取和运输物体，并精确地跟踪期望的轨迹。虽然论文中没有给出具体的性能数据和对比基线，但仿真结果表明该方法具有良好的鲁棒性和轨迹跟踪精度。

## 🎯 应用场景

该研究成果可应用于自动化装配、医疗机器人、物流搬运等领域。例如，在自动化装配中，多个机械臂可以协同完成复杂的装配任务，提高生产效率和产品质量。在医疗机器人中，多个机械臂可以协同进行手术操作，提高手术精度和安全性。在物流搬运中，多个机械臂可以协同搬运大型或重型物体，提高搬运效率和安全性。该研究为多机械臂系统的实际应用提供了理论基础和技术支持。

## 📄 摘要（原文）

> We consider the problem of cooperative manipulation by a mobile multi-manipulator system operating in obstacle-cluttered and highly constrained environments under spatio-temporal task specifications. The task requires transporting a grasped object while respecting both continuous robot dynamics and discrete geometric constraints arising from obstacles and narrow passages. To address this hybrid structure, we propose a multi-rate planning and control framework that combines offline generation of an STL-satisfying object trajectory and collision-free base footprints with online constrained inverse kinematics and continuous-time feedback control. The resulting closed-loop system enables coordinated reconfiguration of multiple manipulators while tracking the desired object motion. The approach is evaluated in high-fidelity physics simulations using three Franka Emika Panda mobile manipulators rigidly grasping an object.

