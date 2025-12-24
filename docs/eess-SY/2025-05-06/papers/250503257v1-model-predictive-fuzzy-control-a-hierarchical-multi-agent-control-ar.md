---
layout: default
title: Model Predictive Fuzzy Control: A Hierarchical Multi-Agent Control Architecture for Outdoor Search-and-Rescue Robots
---

# Model Predictive Fuzzy Control: A Hierarchical Multi-Agent Control Architecture for Outdoor Search-and-Rescue Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03257" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03257v1</a>
  <a href="https://arxiv.org/pdf/2505.03257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03257v1', 'Model Predictive Fuzzy Control: A Hierarchical Multi-Agent Control Architecture for Outdoor Search-and-Rescue Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Craig Maxwell, Mirko Baglioni, Anahita Jamshidnejad

**分类**: eess.SY, cs.RO

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出模型预测模糊控制以优化户外搜救机器人调度**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `模糊逻辑控制` `多机器人系统` `搜救机器人` `自主决策` `任务规划` `环境映射`

## 📋 核心要点

1. 现有的搜救机器人控制方法在处理复杂环境时效率低下，难以实现快速决策。
2. 本文提出的MPFC架构通过结合MPC和FLC，实现了局部控制与全局优化的有效结合。
3. 实验结果表明，MPFC在多机器人搜救系统中性能优于去中心化FLC控制器，同时计算资源消耗更低。

## 📝 摘要（中文）

在未知的搜救环境中，自主机器人能够显著提高任务效率，快速定位和救援被困者。本文提出了一种新颖的集成层次控制架构，称为模型预测模糊控制（MPFC），用于多机器人搜救系统的自主任务规划。该架构结合了模型预测控制（MPC）和模糊逻辑控制（FLC），通过中央MPC控制器调优局部FLC控制器的参数，从而实现高效的环境映射。MPFC架构在计算效率上与去中心化FLC控制器相当，但在多机器人搜救系统的性能上有所提升，同时在路径规划方面的表现与中心化MPC相当，但所需计算资源显著减少。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂未知环境中，搜救机器人在任务规划和决策时的效率问题。现有方法往往面临计算资源消耗大、实时性不足等挑战。

**核心思路**：论文提出的MPFC架构通过将MPC与FLC结合，利用FLC进行实时局部控制，同时通过MPC优化全局性能，提升了决策效率和任务执行能力。

**技术框架**：MPFC架构分为两个主要模块：局部FLC控制器负责实时决策，中央MPC控制器负责全局参数优化。局部控制器的参数根据MPC的优化结果进行调整，以适应环境变化。

**关键创新**：MPFC的核心创新在于将模糊控制的启发式决策与模型预测的全局优化相结合，克服了传统模糊控制器缺乏最优性的问题。

**关键设计**：在设计中，FLC控制器的参数通过MPC进行调优，优化目标包括路径规划的效率和资源消耗，确保在动态环境中保持高效的决策能力。实验中使用MATLAB构建了离散的二维网格模型进行模拟。

## 📊 实验亮点

实验结果显示，MPFC架构在多机器人搜救系统中的性能优于传统的去中心化FLC控制器，且在路径规划方面与中心化MPC的表现相当。MPFC在计算资源消耗上显著降低，优化变量数量减少，使得实时决策更加高效。

## 🎯 应用场景

该研究的潜在应用领域包括灾难救援、环境监测和自动化物流等。通过提高多机器人系统在复杂环境中的自主决策能力，MPFC架构能够有效提升救援效率，减少人力资源的依赖，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Autonomous robots deployed in unknown search-and-rescue (SaR) environments can significantly improve the efficiency of the mission by assisting in fast localisation and rescue of the trapped victims. We propose a novel integrated hierarchical control architecture, called model predictive fuzzy control (MPFC), for autonomous mission planning of multi-robot SaR systems that should efficiently map an unknown environment: We combine model predictive control (MPC) and fuzzy logic control (FLC), where the robots are locally controlled by computationally efficient FLC controllers, and the parameters of these local controllers are tuned via a centralised MPC controller, in a regular or event-triggered manner. The proposed architecture provides three main advantages: (1) The control decisions are made by the FLC controllers, thus the real-time computation time is affordable. (2) The centralised MPC controller optimises the performance criteria with a global and predictive vision of the system dynamics, and updates the parameters of the FLC controllers accordingly. (3) FLC controllers are heuristic by nature and thus do not take into account optimality in their decisions, while the tuned parameters via the MPC controller can indirectly incorporate some level of optimality in local decisions of the robots. A simulation environment for victim detection in a disaster environment was designed in MATLAB using discrete, 2-D grid-based models. While being comparable from the point of computational efficiency, the integrated MPFC architecture improves the performance of the multi-robot SaR system compared to decentralised FLC controllers. Moreover, the performance of MPFC is comparable to the performance of centralised MPC for path planning of SaR robots, whereas MPFC requires significantly less computational resources, since the number of the optimisation variables in the control problem are reduced.

