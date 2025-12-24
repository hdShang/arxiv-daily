---
layout: default
title: A Vehicle System for Navigating Among Vulnerable Road Users Including Remote Operation
---

# A Vehicle System for Navigating Among Vulnerable Road Users Including Remote Operation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04982" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04982v1</a>
  <a href="https://arxiv.org/pdf/2505.04982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04982v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04982v1', 'A Vehicle System for Navigating Among Vulnerable Road Users Including Remote Operation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Oscar de Groot, Alberto Bertipaglia, Hidde Boekema, Vishrut Jain, Marcell Kegl, Varun Kotian, Ted Lentsch, Yancong Lin, Chrysovalanto Messiou, Emma Schippers, Farzam Tajdari, Shiming Wang, Zimin Xia, Mubariz Zaffar, Ronald Ensing, Mario Garzon, Javier Alonso-Mora, Holger Caesar, Laura Ferranti, Riender Happee, Julian F. P. Kooij, Georgios Papaioannou, Barys Shyrokau, Dariu M. Gavrila

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-08

**备注**: Intelligent Vehicles Symposium 2025

---

## 💡 一句话要点

**提出一种车辆系统以安全高效地导航于脆弱道路用户之间**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `脆弱道路用户` `运动规划` `模型预测控制` `环境感知` `远程操作` `安全性` `效率`

## 📋 核心要点

1. 现有的自动驾驶系统在处理脆弱道路用户时面临安全性和效率的挑战，尤其是在复杂环境中。
2. 本研究提出了一种基于拓扑驱动模型预测控制的运动规划器，能够生成多条轨迹以应对不同的障碍物规避策略。
3. 实验结果表明，所提系统在安全性和效率上优于三种基线方法，且在封闭赛道测试中表现出色。

## 📝 摘要（中文）

本文提出了一种能够安全高效地在脆弱道路用户（如行人和骑自行车者）之间导航的车辆系统。该系统包括环境感知、定位与地图构建、运动规划和控制等关键模块，集成于原型车辆中。其核心创新在于基于拓扑驱动的模型预测控制（T-MPC）的运动规划器，能够并行生成多条轨迹，每条轨迹代表一种不同的障碍物规避或不超车策略。系统还包括远程人工操作选项，以应对超出自主能力的特殊情况，如施工区域或与紧急响应者的遭遇。在仿真中，我们的运动规划器在安全性和效率方面优于三种基线方法，并在封闭赛道上展示了原型车辆在自主和远程操作模式下的完整系统。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆在与脆弱道路用户（如行人和骑自行车者）交互时的安全性和效率问题。现有方法在复杂环境下的表现不足，尤其在特殊情况下容易出现安全隐患。

**核心思路**：本研究的核心思路是通过拓扑驱动的模型预测控制（T-MPC）来实现运动规划，允许车辆在动态环境中生成多条轨迹，以应对不同的障碍物规避策略。这样的设计使得系统能够在不确定性条件下优化轨迹，降低与脆弱道路用户发生碰撞的概率。

**技术框架**：该系统的整体架构包括环境感知模块、定位与地图构建模块、运动规划模块和控制模块。环境感知模块负责实时获取周围环境信息，定位与地图构建模块用于确定车辆位置，运动规划模块生成安全轨迹，控制模块则执行这些轨迹。

**关键创新**：最重要的技术创新在于运动规划器的设计，采用拓扑驱动的模型预测控制方法，能够并行生成多条轨迹以应对不同的障碍物规避策略。这一方法与传统的单一轨迹生成方法本质上不同，提供了更高的灵活性和安全性。

**关键设计**：在运动规划过程中，系统通过约束联合碰撞概率来优化轨迹，考虑了多种不确定性因素。此外，系统还设计了远程人工操作选项，以应对超出自主驾驶能力的特殊情况，如施工区域或紧急响应者的出现。该设计确保了在复杂环境下的安全性。

## 📊 实验亮点

实验结果显示，所提运动规划器在安全性和效率方面优于三种基线方法，具体表现为在复杂环境中碰撞概率显著降低，且在封闭赛道测试中，原型车辆在自主和远程操作模式下均表现出色，验证了系统的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括城市自动驾驶、共享出行服务以及智能交通系统等。通过提高自动驾驶车辆在复杂环境中的安全性和效率，该系统能够有效减少交通事故，提升行人和骑自行车者的安全保障，具有重要的社会价值和实际意义。

## 📄 摘要（原文）

> We present a vehicle system capable of navigating safely and efficiently around Vulnerable Road Users (VRUs), such as pedestrians and cyclists. The system comprises key modules for environment perception, localization and mapping, motion planning, and control, integrated into a prototype vehicle. A key innovation is a motion planner based on Topology-driven Model Predictive Control (T-MPC). The guidance layer generates multiple trajectories in parallel, each representing a distinct strategy for obstacle avoidance or non-passing. The underlying trajectory optimization constrains the joint probability of collision with VRUs under generic uncertainties. To address extraordinary situations ("edge cases") that go beyond the autonomous capabilities - such as construction zones or encounters with emergency responders - the system includes an option for remote human operation, supported by visual and haptic guidance. In simulation, our motion planner outperforms three baseline approaches in terms of safety and efficiency. We also demonstrate the full system in prototype vehicle tests on a closed track, both in autonomous and remotely operated modes.

