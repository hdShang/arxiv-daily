---
layout: default
title: Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments
---

# Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14206" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14206v1</a>
  <a href="https://arxiv.org/pdf/2512.14206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14206v1" onclick="toggleFavorite(this, '2512.14206v1', 'Trajectory Tracking for Multi-Manipulator Systems in Constrained Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mayank Sewlia, Christos K. Verginis, Dimos V. Dimarogonas

**分类**: cs.RO, eess.SY

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出多速率规划与控制框架，解决约束环境下多机械臂系统的轨迹跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多机械臂系统` `轨迹跟踪` `约束环境` `多速率控制` `逆运动学`

## 📋 核心要点

1. 现有方法难以在复杂约束环境中实现多机械臂系统的精确轨迹跟踪，尤其是在考虑机器人动力学和环境几何约束的情况下。
2. 论文提出一种多速率规划与控制框架，结合离线轨迹生成和在线约束逆运动学，实现多机械臂的协同重构和精确轨迹跟踪。
3. 通过高保真物理仿真，验证了该方法在三个Franka Emika Panda移动机械臂上的有效性，展示了其在复杂环境下的轨迹跟踪能力。

## 📝 摘要（中文）

本文研究了移动多机械臂系统在复杂约束环境中协同操作的问题，该环境包含障碍物和狭窄通道，并具有时空任务规范。任务要求在满足连续机器人动力学和离散几何约束（由障碍物和狭窄通道引起）的同时，运输抓取的物体。为了解决这种混合结构，我们提出了一种多速率规划和控制框架，该框架结合了离线生成的满足STL的对象轨迹和无碰撞的基座足迹，以及在线约束逆运动学和连续时间反馈控制。由此产生的闭环系统能够协调多个机械臂的重构，同时跟踪期望的物体运动。该方法在高度逼真的物理模拟中使用三个Franka Emika Panda移动机械臂刚性抓取一个物体进行了评估。

## 🔬 方法详解

**问题定义**：论文旨在解决多机械臂系统在复杂约束环境下协同操作时的轨迹跟踪问题。现有方法在处理具有障碍物和狭窄通道等约束的环境时，难以同时满足机器人动力学和几何约束，导致轨迹跟踪精度下降或无法完成任务。此外，如何协调多个机械臂的运动以实现期望的物体运动也是一个挑战。

**核心思路**：论文的核心思路是将轨迹规划和控制解耦，采用多速率方法。首先，离线生成满足时序逻辑（STL）规范的物体轨迹和无碰撞的基座足迹。然后，在线使用约束逆运动学和连续时间反馈控制，协调多个机械臂的运动，以跟踪期望的物体轨迹。这种解耦方法可以降低问题的复杂性，提高系统的实时性和鲁棒性。

**技术框架**：该方法的技术框架包含以下几个主要模块：
1. **离线轨迹规划**：使用STL规范描述任务要求，生成满足规范的物体轨迹和无碰撞的基座足迹。
2. **在线约束逆运动学**：根据期望的物体轨迹和基座位置，计算每个机械臂的关节角度，同时考虑机器人动力学和环境约束。
3. **连续时间反馈控制**：使用反馈控制算法，补偿模型误差和外部扰动，提高轨迹跟踪精度。
4. **多速率协调**：采用不同的速率更新轨迹规划、逆运动学和反馈控制，以平衡计算复杂度和控制性能。

**关键创新**：该方法最重要的技术创新点在于将离线轨迹规划和在线约束逆运动学相结合，并采用多速率控制策略。这种方法能够有效地处理复杂约束环境下的轨迹跟踪问题，并实现多个机械臂的协同运动。与现有方法相比，该方法能够更好地平衡计算复杂度和控制性能，提高系统的实时性和鲁棒性。

**关键设计**：论文的关键设计包括：
1. 使用STL规范描述任务要求，确保轨迹满足时序逻辑约束。
2. 采用约束逆运动学算法，考虑机器人动力学和环境约束。
3. 使用连续时间反馈控制算法，补偿模型误差和外部扰动。
4. 采用多速率控制策略，平衡计算复杂度和控制性能。具体的参数设置和算法细节在论文中进行了详细描述。

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

论文通过高保真物理仿真验证了该方法的有效性。实验结果表明，该方法能够实现多机械臂系统在复杂约束环境下的精确轨迹跟踪。具体而言，三个Franka Emika Panda移动机械臂能够协同抓取物体，并在障碍物和狭窄通道中安全地移动，同时保持较高的轨迹跟踪精度。虽然论文中没有给出具体的性能数据和对比基线，但仿真结果表明该方法具有良好的鲁棒性和适应性。

## 🎯 应用场景

该研究成果可应用于自动化装配、物流搬运、医疗手术等领域。在这些场景中，多机械臂系统需要在复杂约束环境下协同操作，完成高精度、高可靠性的任务。该方法能够提高多机械臂系统的自主性和适应性，降低人工干预的需求，从而提高生产效率和安全性。未来，该方法有望应用于更复杂的机器人系统，例如人机协作机器人、移动服务机器人等。

## 📄 摘要（原文）

> We consider the problem of cooperative manipulation by a mobile multi-manipulator system operating in obstacle-cluttered and highly constrained environments under spatio-temporal task specifications. The task requires transporting a grasped object while respecting both continuous robot dynamics and discrete geometric constraints arising from obstacles and narrow passages. To address this hybrid structure, we propose a multi-rate planning and control framework that combines offline generation of an STL-satisfying object trajectory and collision-free base footprints with online constrained inverse kinematics and continuous-time feedback control. The resulting closed-loop system enables coordinated reconfiguration of multiple manipulators while tracking the desired object motion. The approach is evaluated in high-fidelity physics simulations using three Franka Emika Panda mobile manipulators rigidly grasping an object.

