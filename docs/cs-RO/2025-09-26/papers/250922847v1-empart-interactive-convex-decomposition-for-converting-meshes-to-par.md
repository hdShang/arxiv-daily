---
layout: default
title: "Empart: Interactive Convex Decomposition for Converting Meshes to Parts"
---

# Empart: Interactive Convex Decomposition for Converting Meshes to Parts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22847" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22847v1</a>
  <a href="https://arxiv.org/pdf/2509.22847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22847v1', 'Empart: Interactive Convex Decomposition for Converting Meshes to Parts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brandon Vu, Shameek Ganguly, Pushkar Joshi

**分类**: cs.RO

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**Empart：交互式凸分解工具，实现网格模型的区域定制简化，提升机器人仿真效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `凸分解` `网格简化` `机器人仿真` `交互式工具` `区域定制` `并行计算` `碰撞检测`

## 📋 核心要点

1. 现有网格简化方法采用全局统一误差容忍度，无法兼顾机器人应用中不同区域对精度和性能的不同需求。
2. Empart通过交互式界面，允许用户为网格的不同区域指定不同的简化容忍度，实现区域定制的简化。
3. 实验表明，Empart显著减少了凸部件数量，提升了仿真性能，在机器人拾取放置任务中仿真时间缩短了69%。

## 📝 摘要（中文）

复杂3D网格简化是机器人应用中的关键步骤，可实现高效的运动规划和物理仿真。近似凸分解等常用方法将网格表示为简单部件的集合，从而降低计算成本。然而，现有方法通常采用全局统一的误差容忍度，导致精度和性能之间的折衷不佳。例如，机器人抓取物体时，接触面附近需要高精度几何，而其他区域可以粗略简化。统一容忍度可能导致非关键区域细节过多，或关键区域细节不足。为了解决此问题，我们提出了Empart，一个交互式工具，允许用户为网格的选定区域指定不同的简化容忍度。我们的方法利用现有的凸分解算法作为子程序，并使用一种新颖的并行化框架来高效处理区域特定约束。Empart提供了一个用户友好的界面，具有近似误差和仿真性能的可视化反馈，使设计人员能够迭代地优化分解。实验表明，在固定误差阈值下，与最先进的方法（V-HACD）相比，我们的方法显著减少了凸部件的数量，从而显著提高了仿真性能。对于机器人拾取放置任务，与统一分解相比，Empart生成的碰撞网格将整体仿真时间缩短了69%，突出了交互式、区域特定简化对于高性能机器人应用的价值。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂3D网格简化中，现有方法采用全局统一误差容忍度，导致在机器人应用中精度和性能之间折衷不佳的问题。现有方法无法根据不同区域的重要性进行差异化简化，导致非关键区域细节冗余，关键区域精度不足，最终影响仿真效率。

**核心思路**：Empart的核心思路是提供一个交互式的工具，允许用户根据网格不同区域的重要性，指定不同的简化容忍度。通过区域定制的简化，可以在保证关键区域精度的前提下，最大程度地减少非关键区域的细节，从而提高仿真效率。

**技术框架**：Empart的技术框架主要包含以下几个模块：1) 用户交互界面：允许用户选择网格区域并设置简化容忍度；2) 并行化凸分解引擎：利用现有的凸分解算法作为子程序，并采用并行化框架来高效处理区域特定约束；3) 可视化反馈模块：提供近似误差和仿真性能的可视化反馈，帮助用户迭代优化分解。整体流程是用户在交互界面上选择区域并设置容忍度，系统根据设置进行并行化凸分解，并将结果和性能反馈给用户，用户根据反馈进行调整，直到达到满意的结果。

**关键创新**：Empart的关键创新在于其交互式和区域定制的简化方法。与现有方法采用全局统一的误差容忍度不同，Empart允许用户根据网格不同区域的重要性，指定不同的简化容忍度。此外，Empart还采用了并行化框架来高效处理区域特定约束，保证了分解效率。

**关键设计**：Empart的关键设计包括：1) 用户友好的交互界面，方便用户选择区域和设置容忍度；2) 并行化的凸分解引擎，保证分解效率；3) 可视化反馈模块，帮助用户迭代优化分解。具体的参数设置和损失函数等技术细节在论文中没有详细描述，属于现有凸分解算法的范畴。

## 📊 实验亮点

Empart在机器人拾取放置任务中，与采用统一分解的V-HACD方法相比，生成的碰撞网格将整体仿真时间缩短了69%。在固定误差阈值下，Empart显著减少了凸部件的数量，从而显著提高了仿真性能。这些实验结果表明，Empart的交互式和区域定制的简化方法，能够有效地提高仿真效率。

## 🎯 应用场景

Empart可广泛应用于机器人仿真、游戏开发、虚拟现实等领域。在机器人领域，Empart可以用于生成高效的机器人碰撞模型，提高运动规划和物理仿真的效率。在游戏开发和虚拟现实领域，Empart可以用于简化复杂3D模型，降低渲染负担，提高用户体验。Empart的交互式和区域定制的简化方法，为不同应用场景提供了更大的灵活性和优化空间。

## 📄 摘要（原文）

> Simplifying complex 3D meshes is a crucial step in robotics applications to enable efficient motion planning and physics simulation. Common methods, such as approximate convex decomposition, represent a mesh as a collection of simple parts, which are computationally inexpensive to simulate. However, existing approaches apply a uniform error tolerance across the entire mesh, which can result in a sub-optimal trade-off between accuracy and performance. For instance, a robot grasping an object needs high-fidelity geometry in the vicinity of the contact surfaces but can tolerate a coarser simplification elsewhere. A uniform tolerance can lead to excessive detail in non-critical areas or insufficient detail where it's needed most.
>   To address this limitation, we introduce Empart, an interactive tool that allows users to specify different simplification tolerances for selected regions of a mesh. Our method leverages existing convex decomposition algorithms as a sub-routine but uses a novel, parallelized framework to handle region-specific constraints efficiently. Empart provides a user-friendly interface with visual feedback on approximation error and simulation performance, enabling designers to iteratively refine their decomposition. We demonstrate that our approach significantly reduces the number of convex parts compared to a state-of-the-art method (V-HACD) at a fixed error threshold, leading to substantial speedups in simulation performance. For a robotic pick-and-place task, Empart-generated collision meshes reduced the overall simulation time by 69% compared to a uniform decomposition, highlighting the value of interactive, region-specific simplification for performant robotics applications.

