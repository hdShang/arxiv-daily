---
layout: default
title: NMPC-Lander: Nonlinear MPC with Barrier Function for UAV Landing on a Mobile Platform
---

# NMPC-Lander: Nonlinear MPC with Barrier Function for UAV Landing on a Mobile Platform

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03931" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03931v1</a>
  <a href="https://arxiv.org/pdf/2505.03931.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03931v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03931v1', 'NMPC-Lander: Nonlinear MPC with Barrier Function for UAV Landing on a Mobile Platform')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amber Batool, Faryal Batool, Roohan Ahmed Khan, Muhammad Ahsan Mustafa, Aleksey Fedoseev, Dzmitry Tsetserukou

**分类**: cs.RO

**发布日期**: 2025-05-06

**备注**: This manuscript has been submitted to the IEEE International Conference on Systems, Man, and Cybernetics (SMC), 2025

---

## 💡 一句话要点

**提出NMPC-Lander以解决无人机在移动平台上安全着陆问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无人机` `非线性模型预测控制` `控制障碍函数` `自主着陆` `动态平台` `轨迹跟踪` `安全性`

## 📋 核心要点

1. 现有无人机着陆方法在动态平台上存在精度不足和安全性问题，限制了其应用。
2. 论文提出NMPC-Lander，通过结合非线性模型预测控制和控制障碍函数，实现精确的自主着陆。
3. 实验结果表明，NMPC-Lander在静态和动态平台上的着陆精度显著提高，位置跟踪性能优于现有方法。

## 📝 摘要（中文）

四旋翼无人机作为多功能空中机器人，在许多关键应用中日益受到关注。然而，其操作效率受到电池寿命和飞行范围的限制。为了解决这些挑战，自动无人机在静态或动态充电和换电站的着陆能力变得至关重要。本研究提出了NMPC-Lander，这是一种新颖的控制架构，将非线性模型预测控制（NMPC）与控制障碍函数（CBF）相结合，以实现对静态和动态平台的精确安全着陆。实验评估显示，在实际硬件上，静态平台的平均最终位置误差为9.0厘米，移动平台为11厘米。NMPC-Lander在位置跟踪方面的表现比结合B样条和A*规划方法提高了近三倍，突显了其卓越的鲁棒性和实用性。

## 🔬 方法详解

**问题定义**：本论文旨在解决无人机在移动平台上安全着陆的挑战，现有方法在动态环境中表现不佳，导致着陆精度和安全性不足。

**核心思路**：NMPC-Lander通过将非线性模型预测控制与控制障碍函数相结合，确保无人机在复杂环境中安全着陆，提供了更高的精度和鲁棒性。

**技术框架**：该方法包括两个主要模块：首先，使用NMPC进行轨迹跟踪和着陆控制；其次，利用CBF确保无人机在着陆过程中避免与静态障碍物发生碰撞。

**关键创新**：NMPC-Lander的核心创新在于将NMPC与CBF有效结合，显著提升了无人机在动态平台上的着陆能力，与传统方法相比，提供了更高的安全性和精确度。

**关键设计**：在设计中，NMPC的参数设置经过优化，以适应不同的着陆场景；CBF的设计确保了在复杂环境中无人机的安全性，避免了潜在的碰撞风险。实验中使用的损失函数和控制策略经过多次迭代调整，以实现最佳性能。

## 📊 实验亮点

实验结果显示，NMPC-Lander在静态平台上的平均最终位置误差为9.0厘米，而在移动平台上为11厘米。与结合B样条和A*规划方法相比，NMPC-Lander在位置跟踪性能上提高了近三倍，展现出其卓越的鲁棒性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机在城市环境中的自动充电、紧急救援任务中的快速着陆、以及物流配送中的高效着陆操作。NMPC-Lander的设计能够提升无人机在复杂环境中的自主性和安全性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Quadcopters are versatile aerial robots gaining popularity in numerous critical applications. However, their operational effectiveness is constrained by limited battery life and restricted flight range. To address these challenges, autonomous drone landing on stationary or mobile charging and battery-swapping stations has become an essential capability. In this study, we present NMPC-Lander, a novel control architecture that integrates Nonlinear Model Predictive Control (NMPC) with Control Barrier Functions (CBF) to achieve precise and safe autonomous landing on both static and dynamic platforms. Our approach employs NMPC for accurate trajectory tracking and landing, while simultaneously incorporating CBF to ensure collision avoidance with static obstacles. Experimental evaluations on the real hardware demonstrate high precision in landing scenarios, with an average final position error of 9.0 cm and 11 cm for stationary and mobile platforms, respectively. Notably, NMPC-Lander outperforms the B-spline combined with the A* planning method by nearly threefold in terms of position tracking, underscoring its superior robustness and practical effectiveness.

