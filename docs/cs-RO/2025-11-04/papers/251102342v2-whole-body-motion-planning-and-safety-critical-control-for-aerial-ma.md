---
layout: default
title: Whole-body motion planning and safety-critical control for aerial manipulation
---

# Whole-body motion planning and safety-critical control for aerial manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02342" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02342v2</a>
  <a href="https://arxiv.org/pdf/2511.02342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02342v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.02342v2', 'Whole-body motion planning and safety-critical control for aerial manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lin Yang, Jinwoo Lee, Domenico Campolo, H. Jin Kim, Jeonghyun Byun

**分类**: cs.RO

**发布日期**: 2025-11-04 (更新: 2025-11-10)

**备注**: Submitted to 2026 IFAC World Congress with the Journal option (MECHATRONICS)

---

## 💡 一句话要点

**提出基于超二次曲面的无人机操作臂全身运动规划与安全控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机操作臂` `全身运动规划` `安全控制` `超二次曲面` `控制障碍函数`

## 📋 核心要点

1. 现有无人机操作臂轨迹规划方法在复杂环境中难以保证全身避碰，且常用几何抽象（如包围盒或椭球）过于保守。
2. 论文提出基于超二次曲面的全身运动规划方法，结合Voronoi图和平衡流形，生成安全、平滑的轨迹。
3. 实验表明，该方法在仿真和真实环境中均优于现有方法，提升了轨迹速度、安全性和平滑性，并具有更高的几何保真度。

## 📝 摘要（中文）

本文提出了一种基于超二次曲面（SQs）的无人机操作臂全身运动规划和安全关键控制框架，旨在解决复杂环境中安全、动态可行的轨迹规划问题。该方法利用SQ-plus-proxy表示，以可微、几何精确的表面建模无人机和障碍物。在此基础上，引入最大间隙规划器，融合Voronoi图和平衡流形公式，生成平滑、避碰的轨迹。此外，设计了一种安全关键控制器，通过高阶控制障碍函数联合执行推力限制和避碰。仿真结果表明，该方法在复杂环境中优于基于采样的规划器，生成更快、更安全、更平滑的轨迹，并在几何保真度上超过了基于椭球的基线。在真实无人机操作臂平台上的实验验证了该方法的可行性和鲁棒性，证明了其在仿真和硬件设置中的一致性能。

## 🔬 方法详解

**问题定义**：无人机操作臂需要在复杂环境中进行操作，但现有的轨迹规划方法难以同时保证全身避碰和动态可行性。常用的包围盒或椭球等几何抽象过于保守，限制了无人机的运动空间，导致规划出的轨迹不够高效。此外，如何在保证安全的前提下，充分利用无人机的运动能力也是一个挑战。

**核心思路**：论文的核心思路是使用超二次曲面（SQs）来精确建模无人机和环境中的障碍物。SQs具有可微的几何特性，可以方便地进行碰撞检测和梯度计算。通过结合Voronoi图和平衡流形，可以生成既能避开障碍物，又能保持无人机平衡的轨迹。此外，利用控制障碍函数（CBF）设计安全关键控制器，可以在满足推力限制的同时，保证无人机与障碍物之间的安全距离。

**技术框架**：该框架主要包含两个模块：运动规划器和安全控制器。运动规划器首先使用SQs建模无人机和环境，然后利用Voronoi图生成初始路径，再通过平衡流形优化路径，生成平滑、避碰的轨迹。安全控制器则利用CBF，根据无人机的状态和环境信息，实时调整控制输入，保证无人机的安全。整体流程为：环境建模 -> 初始路径规划 -> 轨迹优化 -> 安全控制。

**关键创新**：该论文的关键创新在于以下几点：1) 使用SQs进行全身建模，提高了几何精度；2) 融合Voronoi图和平衡流形，生成高质量的轨迹；3) 利用高阶CBF设计安全关键控制器，保证了无人机的安全性。与现有方法相比，该方法在几何精度、轨迹质量和安全性方面都有显著提升。

**关键设计**：在SQ建模中，使用了SQ-plus-proxy表示，以提高计算效率。在轨迹优化中，平衡流形的构建需要考虑无人机的动力学模型。在CBF设计中，使用了高阶CBF，以提高控制器的鲁棒性。此外，还对推力限制进行了建模，以保证控制输入的合理性。

## 📊 实验亮点

仿真结果表明，该方法在复杂环境中优于基于采样的规划器，生成更快、更安全、更平滑的轨迹。与基于椭球的基线相比，该方法在几何保真度上也有显著提升。在真实无人机操作臂平台上的实验验证了该方法的可行性和鲁棒性，证明了其在仿真和硬件设置中的一致性能。

## 🎯 应用场景

该研究成果可应用于复杂环境下的无人机操作任务，例如桥梁检测、高压线维护、灾后救援等。通过精确的全身建模和安全控制，无人机可以在狭窄空间内灵活操作，完成各种复杂的任务，降低人工成本和风险，提高工作效率。

## 📄 摘要（原文）

> Aerial manipulation combines the maneuverability of multirotors with the dexterity of robotic arms to perform complex tasks in cluttered spaces. Yet planning safe, dynamically feasible trajectories remains difficult due to whole-body collision avoidance and the conservativeness of common geometric abstractions such as bounding boxes or ellipsoids. We present a whole-body motion planning and safety-critical control framework for aerial manipulators built on superquadrics (SQs). Using an SQ-plus-proxy representation, we model both the vehicle and obstacles with differentiable, geometry-accurate surfaces. Leveraging this representation, we introduce a maximum-clearance planner that fuses Voronoi diagrams with an equilibrium-manifold formulation to generate smooth, collision-aware trajectories. We further design a safety-critical controller that jointly enforces thrust limits and collision avoidance via high-order control barrier functions. In simulation, our approach outperforms sampling-based planners in cluttered environments, producing faster, safer, and smoother trajectories and exceeding ellipsoid-based baselines in geometric fidelity. Actual experiments on a physical aerial-manipulation platform confirm feasibility and robustness, demonstrating consistent performance across simulation and hardware settings. The video can be found at https://youtu.be/hQYKwrWf1Ak.

