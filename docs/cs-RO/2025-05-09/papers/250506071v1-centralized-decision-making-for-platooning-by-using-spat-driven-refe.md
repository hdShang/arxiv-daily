---
layout: default
title: Centralized Decision-Making for Platooning By Using SPaT-Driven Reference Speeds
---

# Centralized Decision-Making for Platooning By Using SPaT-Driven Reference Speeds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06071" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06071v1</a>
  <a href="https://arxiv.org/pdf/2505.06071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06071v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06071v1', 'Centralized Decision-Making for Platooning By Using SPaT-Driven Reference Speeds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Melih Yazgan, Süleyman Tatar, J. Marius Zöllner

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-09

**备注**: Accepted for publication at IV 2025

---

## 💡 一句话要点

**提出集中决策方法以优化城市车队行驶效率**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `车队行驶` `燃油效率` `V2X通信` `模型预测控制` `交通流优化` `智能交通系统` `动态控制策略`

## 📋 核心要点

1. 现有方法在城市车队行驶中面临燃油消耗高、交通流不畅等挑战。
2. 论文提出了一种基于V2X通信和SPaT数据的集中式决策方法，优化车队行驶轨迹。
3. 仿真结果表明，该方法可实现高达41.2%的燃油节省，并改善交通流动性。

## 📝 摘要（中文）

本文提出了一种集中式方法，通过实时的车与一切（V2X）通信和信号相位与时序（SPaT）数据，优化城市车队的燃油效率。采用非线性模型预测控制（MPC）算法，优化车队领头车辆的轨迹，使用不对称成本函数以最小化燃油消耗。跟随车辆则采用基于间距和速度的控制策略，并通过车队控制消息（PCM）和车队意识消息（PAM）进行动态车队拆分。通过CARLA环境的仿真结果显示，燃油节省高达41.2%，同时实现了更平稳的交通流、减少车辆停靠和提高交叉口通行能力。

## 🔬 方法详解

**问题定义**：本文旨在解决城市车队行驶中的燃油效率低和交通流不畅的问题。现有方法往往缺乏实时数据支持，导致决策不够精准。

**核心思路**：论文提出利用实时的V2X通信和SPaT数据，通过集中式决策来优化车队的行驶轨迹，从而提高燃油效率和交通流动性。

**技术框架**：整体架构包括三个主要模块：首先，利用MPC算法优化车队领头车辆的轨迹；其次，跟随车辆采用基于间距和速度的控制策略；最后，通过PCM和PAM进行动态车队拆分和信息共享。

**关键创新**：最重要的技术创新在于引入不对称成本函数以最小化燃油消耗，并通过实时数据驱动的集中决策来优化车队行驶效率，这与传统的分散式控制方法有本质区别。

**关键设计**：在MPC算法中，设计了不对称成本函数以强调燃油消耗的最小化，同时在跟随车辆控制中，采用了动态间距和速度控制策略，确保车队的稳定性和安全性。仿真中使用的CARLA环境提供了真实的交通场景，增强了实验的可靠性。

## 📊 实验亮点

实验结果显示，采用该集中决策方法后，燃油节省高达41.2%，同时实现了更平稳的交通流和减少车辆停靠，显著提高了交叉口的通行能力。这些结果表明该方法在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶车辆的协调行驶以及城市交通管理。通过优化车队行驶效率，可以显著降低城市交通的碳排放，提升交通流动性，具有重要的社会和环境价值。

## 📄 摘要（原文）

> This paper introduces a centralized approach for fuel-efficient urban platooning by leveraging real-time Vehicle- to-Everything (V2X) communication and Signal Phase and Timing (SPaT) data. A nonlinear Model Predictive Control (MPC) algorithm optimizes the trajectories of platoon leader vehicles, employing an asymmetric cost function to minimize fuel-intensive acceleration. Following vehicles utilize a gap- and velocity-based control strategy, complemented by dynamic platoon splitting logic communicated through Platoon Control Messages (PCM) and Platoon Awareness Messages (PAM). Simulation results obtained from the CARLA environment demonstrate substantial fuel savings of up to 41.2%, along with smoother traffic flows, fewer vehicle stops, and improved intersection throughput.

