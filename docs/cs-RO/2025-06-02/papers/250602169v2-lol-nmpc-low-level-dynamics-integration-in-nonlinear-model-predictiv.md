---
layout: default
title: "LoL-NMPC: Low-Level Dynamics Integration in Nonlinear Model Predictive Control for Unmanned Aerial Vehicles"
---

# LoL-NMPC: Low-Level Dynamics Integration in Nonlinear Model Predictive Control for Unmanned Aerial Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02169" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02169v2</a>
  <a href="https://arxiv.org/pdf/2506.02169.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02169v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02169v2', 'LoL-NMPC: Low-Level Dynamics Integration in Nonlinear Model Predictive Control for Unmanned Aerial Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Parakh M. Gupta, Ondřej Procházka, Jan Hřebec, Matej Novosad, Robert Pěnička, Martin Saska

**分类**: cs.RO

**发布日期**: 2025-06-02 (更新: 2025-07-31)

**备注**: Accepted to IROS 2025

**DOI**: [10.1109/IROS60139.2025.11246583](https://doi.org/10.1109/IROS60139.2025.11246583)

---

## 💡 一句话要点

**提出LoL-NMPC以解决无人机高速度轨迹跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机` `非线性模型预测控制` `轨迹跟踪` `低级控制器动态` `高速度飞行` `执行器约束` `实时控制`

## 📋 核心要点

1. 现有的非线性模型预测控制方法忽略了低级飞行控制器的动态，导致高速度下的跟踪误差较大。
2. 本文提出的LoL-NMPC方法显式整合了低级控制器和电机动态，以提高轨迹跟踪精度。
3. 实验结果表明，LoL-NMPC在100 Hz的实时性下，平均减少了21.97%的轨迹跟踪误差。

## 📝 摘要（中文）

本文针对无人机在高速度下跟踪敏捷轨迹时的模型不准确性问题，提出了一种新的非线性模型预测控制方法LoL-NMPC。现有的非线性模型预测控制方法通常忽略低级飞行控制器的动态特性，导致在高速和加速情况下的跟踪性能不佳。LoL-NMPC显式地将低级控制器和电机动态纳入模型，以最小化轨迹跟踪误差，同时保持计算效率。通过在低级动态中利用线性约束，该方法能够自然而然地考虑执行器约束，而无需额外的重新分配策略。仿真和实际实验验证了该方法在速度高达98.57 km/h和加速度为3.5 g的情况下，跟踪精度和鲁棒性均有所提升，平均轨迹跟踪误差减少了21.97%。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机在高速度下轨迹跟踪中的模型不准确性问题。现有的非线性模型预测控制方法未能考虑低级控制器的动态特性，导致在高速和加速情况下的跟踪性能不理想。

**核心思路**：LoL-NMPC方法的核心思路是将低级控制器动态和电机动态显式纳入控制模型中，以减少轨迹跟踪误差并提高计算效率。通过这种设计，能够更好地适应高速度和高加速度的飞行需求。

**技术框架**：该方法的整体架构包括低级控制器动态模型、NMPC优化模块和执行器约束处理。首先，建立低级控制器的动态模型，然后在NMPC框架中进行优化，最后通过线性约束处理执行器的限制。

**关键创新**：LoL-NMPC的主要创新在于显式整合低级控制器动态，克服了传统NMPC方法的不足，使得控制器能够在高速度下实现更优的跟踪性能。与现有方法相比，该方法在处理执行器约束时更为高效。

**关键设计**：在设计中，采用了特定的损失函数来量化轨迹跟踪误差，并通过优化算法实现实时控制。参数设置方面，确保了在100 Hz的频率下，控制器能够快速响应飞行状态的变化。

## 📊 实验亮点

实验结果显示，LoL-NMPC在速度高达98.57 km/h和加速度为3.5 g的情况下，平均轨迹跟踪误差减少了21.97%。该方法在100 Hz的实时性下，保持了良好的计算效率，展现出优越的跟踪精度和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机的自动飞行、农业监测、物流运输等。通过提高无人机在复杂环境中的轨迹跟踪能力，能够显著提升其在实际任务中的执行效率和安全性。未来，该技术有望推广至更多类型的无人系统，推动无人机技术的进一步发展。

## 📄 摘要（原文）

> [Accepted to IROS 2025] In this paper, we address the problem of tracking high-speed agile trajectories for Unmanned Aerial Vehicles(UAVs), where model inaccuracies can lead to large tracking errors. Existing Nonlinear Model Predictive Controller(NMPC) methods typically neglect the dynamics of the low-level flight controllers such as underlying PID controller present in many flight stacks, and this results in sub-optimal tracking performance at high speeds and accelerations. To this end, we propose a novel NMPC formulation, LoL-NMPC, which explicitly incorporates low-level controller dynamics and motor dynamics in order to minimize trajectory tracking errors while maintaining computational efficiency. By leveraging linear constraints inside low-level dynamics, our approach inherently accounts for actuator constraints without requiring additional reallocation strategies. The proposed method is validated in both simulation and real-world experiments, demonstrating improved tracking accuracy and robustness at speeds up to 98.57 km/h and accelerations of 3.5 g. Our results show an average 21.97 % reduction in trajectory tracking error over standard NMPC formulation, with LoL-NMPC maintaining real-time feasibility at 100 Hz on an embedded ARM-based flight computer.

