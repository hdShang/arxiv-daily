---
layout: default
title: "Microrobot Vascular Parkour: Analytic Geometry-based Path Planning with Real-time Dynamic Obstacle Avoidance"
---

# Microrobot Vascular Parkour: Analytic Geometry-based Path Planning with Real-time Dynamic Obstacle Avoidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05500" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05500v1</a>
  <a href="https://arxiv.org/pdf/2509.05500.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05500v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05500v1', 'Microrobot Vascular Parkour: Analytic Geometry-based Path Planning with Real-time Dynamic Obstacle Avoidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanda Yang, Max Sokolich, Fatma Ceren Kirmizitas, Sambeeta Das, Andreas A. Malikopoulos

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-05

**备注**: 56 pages, 19 figures including Supplementary Materials. Supplementary videos available at https://robotyyd.github.io/yanda-yang.github.io/vascular-parkour.html. Preprint. This version has not been peer reviewed

---

## 💡 一句话要点

**提出基于解析几何的微型机器人血管导航路径规划与动态避障方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `微型机器人` `血管导航` `路径规划` `动态避障` `解析几何` `强化学习` `实时控制`

## 📋 核心要点

1. 血管内微型机器人导航面临移动障碍物密集和动态的挑战，现有方法难以兼顾全局规划效率和局部避障能力。
2. 论文提出结合解析几何全局规划器（AGP）和反应式局部控制器的混合框架，实现快速全局路径规划和实时动态避障。
3. 实验结果表明，该方法在仿真和真实环境中均能有效避开移动障碍物，并实现快速路径规划，平均规划时间为40ms。

## 📝 摘要（中文）

本文提出了一种用于血管内自主微型机器人导航的实时路径规划框架，该框架结合了解析几何全局规划器（AGP）和两个反应式局部避障控制器，分别基于规则和强化学习，以应对突发的移动障碍。系统利用实时成像技术估计微型机器人、障碍物和目标的位置，并计算无碰撞运动轨迹。仿真结果表明，AGP在保持可行性和确定性的前提下，比加权A*（WA*）、粒子群优化（PSO）和快速探索随机树（RRT）产生更短的路径和更快的规划速度。AGP可以从2D扩展到3D，且不损失速度。在仿真和实验中，全局规划器和局部控制器的组合能够可靠地避开移动障碍并到达目标。平均规划时间为每帧40毫秒，与25 fps的图像采集和实时闭环控制兼容。这些结果推进了自主微型机器人导航和血管环境中的靶向药物递送。

## 🔬 方法详解

**问题定义**：论文旨在解决微型机器人在血管环境中自主导航的问题，特别是在存在密集且移动的障碍物时。现有方法，如加权A*（WA*）、粒子群优化（PSO）和快速探索随机树（RRT），在规划速度、路径长度或避障能力方面存在局限性，难以满足实时性和安全性的要求。

**核心思路**：论文的核心思路是将全局路径规划和局部动态避障解耦，利用解析几何全局规划器（AGP）快速生成全局最优路径，然后使用反应式局部控制器实时调整路径以避开移动障碍物。这种混合方法旨在结合全局规划的效率和局部控制的灵活性。

**技术框架**：该系统包含三个主要模块：1) 基于实时成像的感知模块，用于估计微型机器人、障碍物和目标的位置；2) 解析几何全局规划器（AGP），用于生成初始的全局路径；3) 两个反应式局部控制器，一个基于规则，另一个基于强化学习，用于实时调整路径以避开移动障碍物。整个流程是闭环控制，根据实时感知信息不断更新路径。

**关键创新**：最重要的技术创新点在于解析几何全局规划器（AGP）的设计。与传统的基于搜索的规划算法（如A*、RRT）不同，AGP利用解析几何原理直接计算两点之间的最优路径，从而显著提高了规划速度。此外，结合基于规则和强化学习的两种局部控制器，增强了系统的鲁棒性和适应性。

**关键设计**：AGP的关键设计在于利用解析几何方法计算路径，具体实现细节未知。局部控制器方面，基于规则的控制器可能包含一些预定义的避障策略，而基于强化学习的控制器则通过与环境交互学习最优的避障策略。论文中提到平均规划时间为40ms，与25fps的图像采集频率兼容，表明系统具有良好的实时性。

## 📊 实验亮点

论文的主要实验结果表明，所提出的AGP方法在仿真环境中比WA*、PSO和RRT具有更短的路径和更快的规划速度，同时保持了可行性和确定性。此外，该方法可以从2D扩展到3D而不会损失速度。在仿真和真实实验中，全局规划器和局部控制器的组合能够可靠地避开移动障碍物并到达目标，平均规划时间为40ms。

## 🎯 应用场景

该研究成果可应用于微创医疗领域，例如靶向药物递送、血管内手术等。通过自主导航的微型机器人，可以更精确地将药物输送到病灶，减少对健康组织的损伤。未来，该技术有望在疾病诊断、治疗和康复等方面发挥重要作用。

## 📄 摘要（原文）

> Autonomous microrobots in blood vessels could enable minimally invasive therapies, but navigation is challenged by dense, moving obstacles. We propose a real-time path planning framework that couples an analytic geometry global planner (AGP) with two reactive local escape controllers, one based on rules and one based on reinforcement learning, to handle sudden moving obstacles. Using real-time imaging, the system estimates the positions of the microrobot, obstacles, and targets and computes collision-free motions. In simulation, AGP yields shorter paths and faster planning than weighted A* (WA*), particle swarm optimization (PSO), and rapidly exploring random trees (RRT), while maintaining feasibility and determinism. We extend AGP from 2D to 3D without loss of speed. In both simulations and experiments, the combined global planner and local controllers reliably avoid moving obstacles and reach targets. The average planning time is 40 ms per frame, compatible with 25 fps image acquisition and real-time closed-loop control. These results advance autonomous microrobot navigation and targeted drug delivery in vascular environments.

