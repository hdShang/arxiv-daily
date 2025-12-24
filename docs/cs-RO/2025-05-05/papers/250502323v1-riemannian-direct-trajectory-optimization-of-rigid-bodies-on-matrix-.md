---
layout: default
title: Riemannian Direct Trajectory Optimization of Rigid Bodies on Matrix Lie Groups
---

# Riemannian Direct Trajectory Optimization of Rigid Bodies on Matrix Lie Groups

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02323" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02323v1</a>
  <a href="https://arxiv.org/pdf/2505.02323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02323v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02323v1', 'Riemannian Direct Trajectory Optimization of Rigid Bodies on Matrix Lie Groups')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangli Teng, Tzu-Yuan Lin, William A Clark, Ram Vasudevan, Maani Ghaffari

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-05

**备注**: Accepted to Robotics: Science and Systems (RSS) 2025

---

## 💡 一句话要点

**提出黎曼直接轨迹优化方法以解决刚体动态轨迹设计问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `刚体轨迹优化` `黎曼优化` `李群变分积分器` `动态可行性` `机器人技术` `非线性约束` `高效算法`

## 📋 核心要点

1. 现有的直接轨迹优化方法在刚体动态参数化上存在不足，导致收敛速度慢和拓扑结构的破坏。
2. 本文提出了一种基于黎曼优化的框架，利用李群变分积分器和黎曼导数进行轨迹优化。
3. 实验结果显示，所提方法在复杂任务中比传统方法快一个数量级，具有显著的性能提升。

## 📝 摘要（中文）

设计动态可行的刚体轨迹是机器人领域的一个基本问题。尽管直接轨迹优化被广泛应用于解决此问题，但不当的刚体动态参数化常导致收敛速度慢以及旋转群的内在拓扑结构被破坏。本文提出了一种黎曼优化框架，用于刚体的直接轨迹优化。首先，利用李群变分积分器对矩阵李群上的离散刚体动态进行公式化。然后，推导出动态的闭式一阶和二阶黎曼导数。最后，应用线搜索黎曼内部点法（RIPM）在一般非线性约束下进行轨迹优化。由于优化在矩阵李群上进行，因此在构造上保证了旋转群的拓扑结构，并避免了奇异性。仿真结果表明，该方法在复杂的机器人任务中比传统方法快一个数量级。

## 🔬 方法详解

**问题定义**：本文旨在解决刚体轨迹设计中的动态可行性问题。现有方法在参数化刚体动态时存在收敛慢和拓扑结构破坏的痛点。

**核心思路**：论文提出了一种基于黎曼几何的优化框架，通过李群变分积分器来处理刚体动态，确保优化过程遵循旋转群的拓扑结构。

**技术框架**：整体架构包括三个主要模块：首先，使用李群变分积分器公式化离散刚体动态；其次，推导一阶和二阶黎曼导数；最后，应用线搜索黎曼内部点法进行轨迹优化。

**关键创新**：最重要的创新点在于将黎曼优化方法应用于刚体轨迹优化，确保了优化过程的正确性和高效性，避免了传统方法中的奇异性问题。

**关键设计**：在优化过程中，采用了闭式的黎曼导数计算，确保了导数评估和牛顿步骤在规划时间和系统自由度上的线性复杂度。

## 📊 实验亮点

实验结果表明，所提出的方法在复杂机器人任务中比传统方法快一个数量级，展示了优越的性能。具体来说，优化过程中的导数评估和牛顿步骤在规划时间和系统自由度上均表现出线性复杂度，显著提高了效率。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人导航、无人机飞行控制以及机械臂路径规划等。通过提供高效的轨迹优化方法，能够显著提升机器人在复杂环境中的动态表现和任务执行能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Designing dynamically feasible trajectories for rigid bodies is a fundamental problem in robotics. Although direct trajectory optimization is widely applied to solve this problem, inappropriate parameterizations of rigid body dynamics often result in slow convergence and violations of the intrinsic topological structure of the rotation group. This paper introduces a Riemannian optimization framework for direct trajectory optimization of rigid bodies. We first use the Lie Group Variational Integrator to formulate the discrete rigid body dynamics on matrix Lie groups. We then derive the closed-form first- and second-order Riemannian derivatives of the dynamics. Finally, this work applies a line-search Riemannian Interior Point Method (RIPM) to perform trajectory optimization with general nonlinear constraints. As the optimization is performed on matrix Lie groups, it is correct-by-construction to respect the topological structure of the rotation group and be free of singularities. The paper demonstrates that both the derivative evaluations and Newton steps required to solve the RIPM exhibit linear complexity with respect to the planning horizon and system degrees of freedom. Simulation results illustrate that the proposed method is faster than conventional methods by an order of magnitude in challenging robotics tasks.

