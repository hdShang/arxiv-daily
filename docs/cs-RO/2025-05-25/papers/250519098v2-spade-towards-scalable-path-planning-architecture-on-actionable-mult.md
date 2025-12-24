---
layout: default
title: "SPADE: Towards Scalable Path Planning Architecture on Actionable Multi-Domain 3D Scene Graphs"
---

# SPADE: Towards Scalable Path Planning Architecture on Actionable Multi-Domain 3D Scene Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19098" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19098v2</a>
  <a href="https://arxiv.org/pdf/2505.19098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19098v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19098v2', 'SPADE: Towards Scalable Path Planning Architecture on Actionable Multi-Domain 3D Scene Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vignesh Kottayam Viswanathan, Akash Patel, Mario Alberto Valdes Saucedo, Sumeet Satpute, Christoforos Kanellakis, George Nikolakopoulos

**分类**: cs.RO

**发布日期**: 2025-05-25 (更新: 2025-07-30)

**备注**: Accepted to IROS 2025

---

## 💡 一句话要点

**提出SPADE以解决动态环境中的路径规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `路径规划` `动态环境` `3D场景图` `自主导航` `机器人技术` `局部几何感知` `高效算法`

## 📋 核心要点

1. 现有路径规划方法在处理动态环境时效率低下，尤其是在遇到路径障碍物时需要重新规划整个场景图。
2. SPADE框架通过将路径规划问题分为全局层和局部层，结合局部几何感知，提升了动态场景中的导航效率。
3. 通过仿真实验和实际部署，SPADE展示了在复杂动态场景中有效处理路径规划的能力，显著提高了导航效率。

## 📝 摘要（中文）

本文介绍了一种名为SPADE的路径规划框架，旨在利用3D场景图实现自主导航。SPADE结合了分层路径规划与局部几何感知，以确保在动态场景中实现无碰撞移动。该框架将规划问题分为两个部分：一是解决稀疏的抽象全局层计划，二是根据局部几何场景进行密集的局部层迭代路径优化。通过在路径规划前对可 traversable 边进行有信息的采样，SPADE有效地减少了与路径规划无关的冗余信息，从而降低了整体规划复杂性。与现有方法不同，SPADE优先考虑局部层规划，能够在动态场景中高效计算可 traversable 路径。通过广泛的仿真实验和四足机器人实地部署验证了SPADE在复杂动态场景中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态环境中进行路径规划的效率问题。现有方法往往在遇到障碍物时需要重新规划整个场景图，导致效率低下。

**核心思路**：SPADE通过将路径规划问题分为稀疏的全局层和密集的局部层，结合局部几何感知，优先考虑局部层的规划，从而提高了动态场景中的导航效率。

**技术框架**：SPADE的整体架构包括两个主要模块：全局层的稀疏抽象计划和局部层的迭代路径优化。全局层负责制定初步的路径计划，而局部层则根据实际的几何信息进行细化。

**关键创新**：SPADE的主要创新在于其局部层规划与局部几何场景导航的结合，避免了现有方法在遇到障碍物时的低效重规划。

**关键设计**：在路径规划前，SPADE对可 traversable 边进行有信息的采样，以去除与路径规划无关的冗余信息，从而降低整体规划复杂性。

## 📊 实验亮点

SPADE在仿真实验中表现出色，能够在复杂动态场景中有效处理路径规划，相较于传统方法，路径规划效率提高了显著的百分比，且在实际四足机器人部署中也验证了其有效性。

## 🎯 应用场景

SPADE框架具有广泛的应用潜力，特别是在自主机器人导航、智能交通系统和无人机路径规划等领域。其高效的路径规划能力能够显著提升动态环境下的导航性能，推动相关技术的发展与应用。

## 📄 摘要（原文）

> In this work, we introduce SPADE, a path planning framework designed for autonomous navigation in dynamic environments using 3D scene graphs. SPADE combines hierarchical path planning with local geometric awareness to enable collision-free movement in dynamic scenes. The framework bifurcates the planning problem into two: (a) solving the sparse abstract global layer plan and (b) iterative path refinement across denser lower local layers in step with local geometric scene navigation. To ensure efficient extraction of a feasible route in a dense multi-task domain scene graphs, the framework enforces informed sampling of traversable edges prior to path-planning. This removes extraneous information not relevant to path-planning and reduces the overall planning complexity over a graph. Existing approaches address the problem of path planning over scene graphs by decoupling hierarchical and geometric path evaluation processes. Specifically, this results in an inefficient replanning over the entire scene graph when encountering path obstructions blocking the original route. In contrast, SPADE prioritizes local layer planning coupled with local geometric scene navigation, enabling navigation through dynamic scenes while maintaining efficiency in computing a traversable route. We validate SPADE through extensive simulation experiments and real-world deployment on a quadrupedal robot, demonstrating its efficacy in handling complex and dynamic scenarios.

