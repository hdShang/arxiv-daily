---
layout: default
title: "SwordRiding: A Unified Navigation Framework for Quadrotors in Unknown Complex Environments via Online Guiding Vector Fields"
---

# SwordRiding: A Unified Navigation Framework for Quadrotors in Unknown Complex Environments via Online Guiding Vector Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22043" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22043v1</a>
  <a href="https://arxiv.org/pdf/2511.22043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22043v1', 'SwordRiding: A Unified Navigation Framework for Quadrotors in Unknown Complex Environments via Online Guiding Vector Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuchen Liu, Ruocheng Li, Bin Xin, Weijia Yao, Qigeng Duan, Jinqiang Cui, Ben M. Chen, Jie Chen

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-27

**备注**: For an experimental demo, see https://www.youtube.com/watch?v=tKYCg266c4o. For the lemma proof, see https://github.com/SmartGroupSystems/GVF_close_loop_planning/blob/main/proofs.md

---

## 💡 一句话要点

**提出基于在线引导向量场的四旋翼无人机未知复杂环境统一导航框架**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `四旋翼无人机` `自主导航` `引导向量场` `环境感知` `闭环控制`

## 📋 核心要点

1. 现有四旋翼导航方法在复杂未知环境中缺乏实时适应性，主要因为其开环特性难以应对环境不确定性和外部扰动。
2. 论文提出基于在线构建引导向量场的闭环导航框架，利用ESDF进行环境感知和路径优化，增强了抗干扰能力。
3. 实验结果表明，该方法在外部干扰下具有更高的鲁棒性和实时性能，验证了其在复杂环境导航中的有效性。

## 📝 摘要（中文）

本文提出了一种用于四旋翼无人机在未知复杂环境中进行实时导航的统一框架，该框架基于从离散参考路径点在线构建引导向量场（GVF）。在该框架中，机载感知模块构建环境的欧几里德符号距离场（ESDF）表示，从而实现障碍物感知和路径距离评估。系统首先使用全局规划器生成离散的、无碰撞的路径点，然后通过均匀B样条对其进行参数化，以生成平滑且物理上可行的参考轨迹。然后，从ESDF和优化的B样条轨迹合成自适应GVF。与传统方法不同，该方法采用闭环导航范例，从而显着提高了在外部干扰下的鲁棒性。与传统的GVF方法相比，所提出的方法直接适应离散路径，并保持与标准规划算法的兼容性。大量的仿真和实际实验表明，该方法在外部干扰下具有更高的鲁棒性和卓越的实时性能。

## 🔬 方法详解

**问题定义**：现有四旋翼导航方法通常采用开环控制，难以应对未知复杂环境中的外部扰动和环境不确定性，导致导航鲁棒性不足。如何在未知环境中实现四旋翼无人机的稳定、实时的导航是一个关键问题。

**核心思路**：论文的核心思路是构建一个基于引导向量场（GVF）的闭环导航系统。通过在线构建GVF，系统能够根据环境变化实时调整导航策略，从而提高对外部扰动的鲁棒性。同时，利用ESDF进行环境感知，确保路径的安全性。

**技术框架**：该导航框架主要包含以下几个模块：1) 环境感知模块：利用机载传感器构建环境的ESDF表示。2) 全局路径规划模块：生成离散的、无碰撞的路径点。3) 轨迹优化模块：使用B样条对离散路径点进行参数化，生成平滑的参考轨迹。4) 引导向量场构建模块：基于ESDF和优化后的轨迹，在线构建自适应GVF。5) 闭环控制模块：利用GVF引导四旋翼无人机进行导航，并实时调整控制策略。

**关键创新**：该方法的主要创新在于：1) 提出了一种基于在线构建GVF的闭环导航框架，显著提高了对外部扰动的鲁棒性。2) 该方法能够直接适应离散路径，并与现有的规划算法兼容。3) 采用自适应GVF，能够根据环境变化实时调整导航策略。

**关键设计**：论文中，ESDF的构建精度和更新频率、B样条的阶数和控制点数量、GVF的构建方法（例如，如何平衡轨迹引导和避障需求）、以及闭环控制器的参数设计等都是关键的技术细节。具体的参数设置和算法实现细节需要在论文正文中查找。

## 📊 实验亮点

论文通过仿真和实际实验验证了所提出方法的有效性。实验结果表明，该方法在外部干扰下具有更高的鲁棒性和卓越的实时性能。具体的性能数据（例如，抗干扰能力提升百分比、导航精度提升百分比等）需要在论文正文中查找。

## 🎯 应用场景

该研究成果可应用于无人机自主巡检、灾后搜救、物流配送等领域。在这些场景中，无人机需要在未知、复杂的环境中自主导航，避开障碍物并完成特定任务。该方法能够提高无人机在这些场景中的鲁棒性和可靠性，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Although quadrotor navigation has achieved high performance in trajectory planning and control, real-time adaptability in unknown complex environments remains a core challenge. This difficulty mainly arises because most existing planning frameworks operate in an open-loop manner, making it hard to cope with environmental uncertainties such as wind disturbances or external perturbations. This paper presents a unified real-time navigation framework for quadrotors in unknown complex environments, based on the online construction of guiding vector fields (GVFs) from discrete reference path points. In the framework, onboard perception modules build a Euclidean Signed Distance Field (ESDF) representation of the environment, which enables obstacle awareness and path distance evaluation. The system first generates discrete, collision-free path points using a global planner, and then parameterizes them via uniform B-splines to produce a smooth and physically feasible reference trajectory. An adaptive GVF is then synthesized from the ESDF and the optimized B-spline trajectory. Unlike conventional approaches, the method adopts a closed-loop navigation paradigm, which significantly enhances robustness under external disturbances. Compared with conventional GVF methods, the proposed approach directly accommodates discretized paths and maintains compatibility with standard planning algorithms. Extensive simulations and real-world experiments demonstrate improved robustness against external disturbances and superior real-time performance.

