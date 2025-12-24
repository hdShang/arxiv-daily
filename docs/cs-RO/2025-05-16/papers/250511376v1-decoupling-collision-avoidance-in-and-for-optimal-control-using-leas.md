---
layout: default
title: Decoupling Collision Avoidance in and for Optimal Control using Least-Squares Support Vector Machines
---

# Decoupling Collision Avoidance in and for Optimal Control using Least-Squares Support Vector Machines

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11376" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11376v1</a>
  <a href="https://arxiv.org/pdf/2505.11376.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11376v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11376v1', 'Decoupling Collision Avoidance in and for Optimal Control using Least-Squares Support Vector Machines')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dries Dirckx, Wilm Decré, Jan Swevers

**分类**: math.OC, cs.RO

**发布日期**: 2025-05-16

---

## 💡 一句话要点

**提出基于最小二乘支持向量机的碰撞避免方法以优化控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `最优控制` `碰撞避免` `最小二乘支持向量机` `运动规划` `非凸约束` `算法优化` `机器人导航`

## 📋 核心要点

1. 现有方法在处理非凸碰撞避免约束时面临计算复杂度高和效率低的问题。
2. 论文提出通过将分离超平面定理转化为分类问题，消除超平面作为优化变量，从而线性化非凸约束。
3. 实验结果显示，该方法在复杂环境中表现出优越的可扩展性，计算时间显著减少，提升幅度高达90%。

## 📝 摘要（中文）

本文详细介绍了一种线性化可微但非凸碰撞避免约束的方法，专门针对凸形状。通过将凸对象的微分碰撞避免约束引入最优控制问题（OCP），并利用分离超平面定理，将超平面视为分类问题，从而将其作为优化变量从OCP中消除。这有效地将非凸约束转化为线性约束。双层算法在优化求解器的迭代之间计算超平面，并将其作为参数嵌入OCP。实验表明，该方法在复杂环境中的可扩展性良好，并适用于多种运动规划方法。与直接将超平面作为变量的先进方法相比，计算轨迹的时间减少了50%至90%。

## 🔬 方法详解

**问题定义**：本文旨在解决在最优控制问题中处理非凸碰撞避免约束的复杂性，现有方法通常将超平面作为优化变量，导致计算效率低下。

**核心思路**：通过将分离超平面定理视为分类问题，论文消除了超平面作为优化变量，从而将非凸约束转化为线性约束，简化了优化过程。

**技术框架**：整体架构包括双层算法，其中第一层计算超平面，第二层将这些超平面作为参数嵌入到最优控制问题中。主要模块包括超平面计算和最优控制求解。

**关键创新**：最重要的创新在于将非凸碰撞避免约束转化为线性约束，显著提高了计算效率，与传统方法相比，减少了超平面作为变量的复杂性。

**关键设计**：在算法设计中，关键参数包括超平面的计算精度和迭代次数，损失函数则用于优化超平面的分类性能，确保在复杂环境中的有效性。

## 📊 实验亮点

实验结果表明，该方法在复杂环境中的计算时间减少了50%至90%，相较于直接将超平面作为变量的先进方法，展现出显著的性能提升。这一成果表明了该方法在实际应用中的可行性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶车辆的运动规划以及任何需要实时碰撞避免的动态系统。通过提高计算效率，该方法能够在复杂环境中实现更快速的决策，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> This paper details an approach to linearise differentiable but non-convex collision avoidance constraints tailored to convex shapes. It revisits introducing differential collision avoidance constraints for convex objects into an optimal control problem (OCP) using the separating hyperplane theorem. By framing this theorem as a classification problem, the hyperplanes are eliminated as optimisation variables from the OCP. This effectively transforms non-convex constraints into linear constraints. A bi-level algorithm computes the hyperplanes between the iterations of an optimisation solver and subsequently embeds them as parameters into the OCP. Experiments demonstrate the approach's favourable scalability towards cluttered environments and its applicability to various motion planning approaches. It decreases trajectory computation times between 50\% and 90\% compared to a state-of-the-art approach that directly includes the hyperplanes as variables in the optimal control problem.

