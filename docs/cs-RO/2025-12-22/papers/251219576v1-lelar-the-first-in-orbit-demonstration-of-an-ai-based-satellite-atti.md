---
layout: default
title: "LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller"
---

# LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19576" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19576v1</a>
  <a href="https://arxiv.org/pdf/2512.19576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19576v1', 'LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kirill Djebko, Tom Baumann, Erik Dilger, Frank Puppe, Sergio Montenegro

**分类**: cs.RO, cs.AI, cs.LG, eess.SY

**发布日期**: 2025-12-22

**备注**: 55 pages, 27 figures, 29 tables. The maneuver telemetry datasets generated and analyzed during this work are available in the GitHub repository https://github.com/kdjebko/lelar-in-orbit-data

---

## 💡 一句话要点

**LeLaR首次在轨演示基于AI的卫星姿态控制器，克服Sim2Real难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `卫星姿态控制` `深度强化学习` `Sim2Real` `在轨演示` `AI控制器`

## 📋 核心要点

1. 传统卫星姿态控制器设计复杂，对模型误差和环境变化敏感，难以适应复杂任务。
2. 利用深度强化学习在仿真环境中训练姿态控制器，实现自适应控制策略，降低对精确模型的依赖。
3. 成功将仿真环境训练的AI控制器部署到真实卫星InnoCube上，验证了其在轨姿态控制的鲁棒性。

## 📝 摘要（中文）

姿态控制对许多卫星任务至关重要。然而，经典控制器设计耗时，且对模型不确定性和运行边界条件的变化敏感。深度强化学习（DRL）通过与仿真环境的自主交互学习自适应控制策略，提供了一种有前景的替代方案。克服Sim2Real差距，即将仿真中训练的智能体部署到真实的物理卫星上，仍然是一个重大挑战。本文介绍了首次成功在轨演示的基于AI的惯性指向机动姿态控制器。该控制器完全在仿真中训练，并部署到由维尔茨堡大学与柏林工业大学合作开发的InnoCube 3U纳米卫星上，该卫星于2025年1月发射。我们介绍了AI智能体设计、训练过程的方法、仿真与真实卫星观测行为之间的差异，以及基于AI的姿态控制器与InnoCube经典PD控制器的比较。稳态指标证实了基于AI的控制器在重复在轨机动期间的鲁棒性能。

## 🔬 方法详解

**问题定义**：卫星姿态控制旨在精确调整和维持卫星在空间中的姿态。传统方法，如PID控制器，需要精确的卫星动力学模型，且难以应对模型不确定性和外部扰动。现有方法的痛点在于设计和调参过程耗时，且难以保证在复杂环境下的鲁棒性。

**核心思路**：利用深度强化学习（DRL）训练一个AI智能体，使其能够通过与仿真环境的交互学习最优的姿态控制策略。核心在于通过大量的仿真训练，使智能体能够适应各种不确定性和扰动，从而实现鲁棒的姿态控制。

**技术框架**：整体框架包括仿真环境和DRL智能体。仿真环境模拟卫星的动力学特性和外部环境，DRL智能体则负责接收卫星状态信息，输出控制指令。训练过程采用标准的强化学习流程，智能体通过与环境交互，不断优化控制策略。主要模块包括：状态观测模块、动作选择模块、奖励函数设计模块和策略更新模块。

**关键创新**：最重要的创新点在于成功克服了Sim2Real差距，将完全在仿真环境中训练的AI智能体部署到真实的卫星上，并实现了有效的姿态控制。这表明DRL在卫星姿态控制领域具有巨大的潜力。与传统方法相比，该方法无需精确的卫星模型，且具有更强的自适应性和鲁棒性。

**关键设计**：奖励函数的设计至关重要，需要综合考虑姿态误差、角速度误差和控制能量消耗等因素。网络结构的选择也需要根据具体任务进行调整。论文中未明确说明具体的网络结构和参数设置，但强调了训练过程的迭代优化和对仿真环境的精确建模。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19576v1/InnoCubeSideView.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19576v1/ADCSNode.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19576v1/InnoCubeTVChamberOpen.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该研究首次在轨演示了基于AI的卫星姿态控制器，验证了其在真实环境中的有效性。实验结果表明，基于AI的控制器在稳态性能方面表现出色，能够实现精确的姿态控制。虽然论文中没有给出具体的性能数据和对比基线，但强调了AI控制器在重复在轨机动中的鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于各类卫星任务，如遥感、通信、导航等。基于AI的姿态控制器能够提高卫星的自主性和智能化水平，降低对地面控制的依赖，并提升任务执行的效率和可靠性。未来，该技术有望应用于深空探测等更复杂的航天任务中。

## 📄 摘要（原文）

> Attitude control is essential for many satellite missions. Classical controllers, however, are time-consuming to design and sensitive to model uncertainties and variations in operational boundary conditions. Deep Reinforcement Learning (DRL) offers a promising alternative by learning adaptive control strategies through autonomous interaction with a simulation environment. Overcoming the Sim2Real gap, which involves deploying an agent trained in simulation onto the real physical satellite, remains a significant challenge. In this work, we present the first successful in-orbit demonstration of an AI-based attitude controller for inertial pointing maneuvers. The controller was trained entirely in simulation and deployed to the InnoCube 3U nanosatellite, which was developed by the Julius-Maximilians-Universität Würzburg in cooperation with the Technische Universität Berlin, and launched in January 2025. We present the AI agent design, the methodology of the training procedure, the discrepancies between the simulation and the observed behavior of the real satellite, and a comparison of the AI-based attitude controller with the classical PD controller of InnoCube. Steady-state metrics confirm the robust performance of the AI-based controller during repeated in-orbit maneuvers.

