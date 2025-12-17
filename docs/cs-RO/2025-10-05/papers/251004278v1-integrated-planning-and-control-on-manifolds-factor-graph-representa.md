---
layout: default
title: Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit
---

# Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04278" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04278v1</a>
  <a href="https://arxiv.org/pdf/2510.04278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04278v1" onclick="toggleFavorite(this, '2510.04278v1', 'Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiwen Yang, Weisong Wen, Runqiu Yang, Yuanyuan Zhang, Jiahao Hu, Yingming Chen, Naigui Xiao, Jiaqi Zhao

**分类**: cs.RO

**发布日期**: 2025-10-05

---

## 💡 一句话要点

**提出FactorMPC：基于因子图的流形上集成规划与控制工具包**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `因子图` `流形优化` `机器人控制` `控制障碍函数`

## 📋 核心要点

1. 传统MPC在处理流形上的机器人控制时面临奇异性、过度参数化等问题，导致性能下降。
2. FactorMPC利用因子图统一建模系统动力学、约束和目标，支持流形状态和高斯不确定性，实现高效优化。
3. 实验表明，FactorMPC在四旋翼飞行器上实现了优越的轨迹跟踪和避障性能，并开源代码以促进研究。

## 📝 摘要（中文）

本文提出FactorMPC，一个基于因子图的模型预测控制(MPC)工具包，旨在解决传统欧几里得公式在处理非线性流形上的系统（如机器人姿态动力学和约束运动规划）时遇到的奇异性、过度参数化和收敛性差等问题。该方法将系统动力学、约束和目标统一到一个模块化、用户友好且高效的优化结构中。FactorMPC原生支持流形值状态，并在切空间中建模高斯不确定性。通过利用因子图的稀疏性和概率结构，该工具包即使对于具有复杂约束的高维系统也能实现实时性能。此外，还设计了基于速度扩展的流形控制障碍函数(CBF)的避障因子，用于安全关键应用。通过桥接图形模型与安全关键MPC，该工作为集成规划和控制提供了一个可扩展且几何一致的框架。四旋翼飞行器上的仿真和实验结果表明，与基线方法相比，该方法具有卓越的轨迹跟踪和避障性能。为了促进研究的可重复性，我们提供了开源实现，提供即插即用的因子。

## 🔬 方法详解

**问题定义**：传统模型预测控制(MPC)在处理机器人姿态控制等非线性流形上的系统时，由于欧几里得空间的局限性，容易出现奇异性、过度参数化和收敛性差等问题。此外，安全约束的有效集成也是一个挑战，尤其是在动态环境中。

**核心思路**：FactorMPC的核心思路是将系统动力学、约束和目标函数统一表示为因子图，利用因子图的稀疏性和概率结构进行高效优化。通过在流形的切空间中建模状态和不确定性，避免了欧几里得空间的局限性。同时，引入基于控制障碍函数(CBF)的因子，确保安全约束的满足。

**技术框架**：FactorMPC的整体框架包括以下几个主要模块：1) 系统动力学建模：使用因子图表示系统的状态转移方程。2) 约束建模：将状态约束和控制约束表示为因子图中的因子。3) 目标函数建模：将轨迹跟踪、能量最小化等目标表示为因子图中的因子。4) 优化求解：利用因子图的稀疏性，使用高效的优化算法求解MPC问题。5) 安全保障：通过CBF因子确保安全约束。

**关键创新**：FactorMPC的关键创新在于：1) 基于因子图的统一建模框架，能够灵活地集成系统动力学、约束和目标函数。2) 原生支持流形值状态，避免了欧几里得空间的局限性。3) 引入基于速度扩展的流形控制障碍函数(CBF)的避障因子，实现安全关键控制。4) 开源实现，方便研究人员使用和扩展。

**关键设计**：FactorMPC的关键设计包括：1) 使用李群和李代数表示流形上的状态和控制量。2) 在切空间中建模高斯不确定性。3) 设计合适的因子来表示系统动力学、约束和目标函数。4) 使用高效的优化算法，如Gauss-Newton或Levenberg-Marquardt算法，求解因子图优化问题。5) CBF因子的设计需要仔细选择CBF函数和参数，以确保安全约束的满足。

## 📊 实验亮点

实验结果表明，FactorMPC在四旋翼飞行器上实现了优越的轨迹跟踪和避障性能。与基线方法相比，FactorMPC能够更准确地跟踪目标轨迹，并有效地避开障碍物。此外，FactorMPC还具有良好的实时性能，能够满足实际应用的需求。开源代码的提供也为其他研究人员提供了便利，促进了该领域的发展。

## 🎯 应用场景

FactorMPC适用于各种需要在非线性流形上进行规划和控制的机器人系统，例如无人机、无人车、机械臂等。特别是在需要考虑安全约束的场景下，如动态环境中的避障、人机协作等，FactorMPC具有重要的应用价值。该研究成果有助于提升机器人系统的自主性和安全性，推动机器人技术在工业、物流、医疗等领域的应用。

## 📄 摘要（原文）

> Model predictive control (MPC) faces significant limitations when applied to systems evolving on nonlinear manifolds, such as robotic attitude dynamics and constrained motion planning, where traditional Euclidean formulations struggle with singularities, over-parameterization, and poor convergence. To overcome these challenges, this paper introduces FactorMPC, a factor-graph based MPC toolkit that unifies system dynamics, constraints, and objectives into a modular, user-friendly, and efficient optimization structure. Our approach natively supports manifold-valued states with Gaussian uncertainties modeled in tangent spaces. By exploiting the sparsity and probabilistic structure of factor graphs, the toolkit achieves real-time performance even for high-dimensional systems with complex constraints. The velocity-extended on-manifold control barrier function (CBF)-based obstacle avoidance factors are designed for safety-critical applications. By bridging graphical models with safety-critical MPC, our work offers a scalable and geometrically consistent framework for integrated planning and control. The simulations and experimental results on the quadrotor demonstrate superior trajectory tracking and obstacle avoidance performance compared to baseline methods. To foster research reproducibility, we have provided open-source implementation offering plug-and-play factors.

