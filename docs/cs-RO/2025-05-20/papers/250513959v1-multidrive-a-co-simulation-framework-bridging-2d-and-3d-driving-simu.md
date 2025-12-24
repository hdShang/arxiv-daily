---
layout: default
title: "MultiDrive: A Co-Simulation Framework Bridging 2D and 3D Driving Simulation for AV Software Validation"
---

# MultiDrive: A Co-Simulation Framework Bridging 2D and 3D Driving Simulation for AV Software Validation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13959" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13959v1</a>
  <a href="https://arxiv.org/pdf/2505.13959.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13959v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13959v1', 'MultiDrive: A Co-Simulation Framework Bridging 2D and 3D Driving Simulation for AV Software Validation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marc Kaufeld, Korbinian Moller, Alessio Gambi, Paolo Arcaini, Johannes Betz

**分类**: cs.RO

**发布日期**: 2025-05-20

**备注**: 7 pages, Submitted to the IEEE International Conference on Intelligent Transportation Systems (ITSC 2025), Australia

**🔗 代码/项目**: [GITHUB](https://github.com/TUM-AVS/MultiDrive)

---

## 💡 一句话要点

**提出MultiDrive框架以解决AV软件验证中的2D与3D模拟问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `自动驾驶` `软件验证` `场景测试` `多智能体协同` `程序化生成` `高保真模拟` `低保真模拟`

## 📋 核心要点

1. 现有方法在自动驾驶软件验证中面临低保真与高保真模拟器之间的选择困境，导致测试效率低下。
2. 本文提出的MultiDrive框架通过多智能体协同仿真和程序化场景生成，支持跨低高保真模拟器的场景测试。
3. 实验结果表明，框架能够揭示规划器的预期与实际行为之间的差异，帮助识别规划假设的弱点。

## 📝 摘要（中文）

基于场景的测试是自动驾驶汽车（AV）软件验证的基石。以往，开发者需要在低保真2D模拟器和高保真3D模拟器之间进行选择，前者有助于高效探索场景空间，后者则用于更详细地研究相关场景。本文提出了一种新颖的框架，利用多智能体协同仿真和程序化场景生成，支持在低保真和高保真模拟器之间进行场景测试，旨在减少场景在模拟器之间转换的工作量，并自动化实验执行、轨迹分析和可视化。通过与参考运动规划器的实验，框架揭示了规划器预期行为与实际行为之间的差异，从而暴露了在更现实条件下规划假设的弱点。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶软件验证中，开发者在低保真2D模拟器与高保真3D模拟器之间选择的困境。现有方法在场景转换和测试效率上存在明显不足。

**核心思路**：MultiDrive框架通过多智能体协同仿真和程序化场景生成，简化了场景在不同模拟器之间的转换过程，并实现了实验的自动化执行与分析。

**技术框架**：该框架包含多个模块，包括场景生成模块、协同仿真模块、实验执行模块和结果分析模块。通过这些模块的协同工作，实现了高效的场景测试。

**关键创新**：最重要的创新在于实现了低保真与高保真模拟器之间的无缝协作，显著降低了场景转换的工作量，并提高了测试的自动化程度。

**关键设计**：框架中采用了程序化场景生成技术，确保了场景的多样性和复杂性，同时在实验执行中引入了自动化分析工具，以便快速识别规划器的行为差异。

## 📊 实验亮点

实验结果显示，使用MultiDrive框架的测试能够有效揭示规划器的预期行为与实际行为之间的差异，帮助开发者识别潜在的规划假设弱点。与传统方法相比，框架在场景转换和测试效率上有显著提升，具体性能数据尚未披露。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的开发与测试、智能交通系统的优化以及机器人导航等。通过提供高效的场景测试工具，MultiDrive框架能够显著提升自动驾驶软件的验证效率和可靠性，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Scenario-based testing using simulations is a cornerstone of Autonomous Vehicles (AVs) software validation. So far, developers needed to choose between low-fidelity 2D simulators to explore the scenario space efficiently, and high-fidelity 3D simulators to study relevant scenarios in more detail, thus reducing testing costs while mitigating the sim-to-real gap. This paper presents a novel framework that leverages multi-agent co-simulation and procedural scenario generation to support scenario-based testing across low- and high-fidelity simulators for the development of motion planning algorithms. Our framework limits the effort required to transition scenarios between simulators and automates experiment execution, trajectory analysis, and visualization. Experiments with a reference motion planner show that our framework uncovers discrepancies between the planner's intended and actual behavior, thus exposing weaknesses in planning assumptions under more realistic conditions. Our framework is available at: https://github.com/TUM-AVS/MultiDrive

