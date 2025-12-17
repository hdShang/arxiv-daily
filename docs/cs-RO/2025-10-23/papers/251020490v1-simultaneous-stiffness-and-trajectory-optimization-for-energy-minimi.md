---
layout: default
title: Simultaneous Stiffness and Trajectory Optimization for Energy Minimization of Pick-and-Place Tasks of SEA-Actuated Parallel Kinematic Manipulators
---

# Simultaneous Stiffness and Trajectory Optimization for Energy Minimization of Pick-and-Place Tasks of SEA-Actuated Parallel Kinematic Manipulators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20490" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20490v1</a>
  <a href="https://arxiv.org/pdf/2510.20490.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20490v1" onclick="toggleFavorite(this, '2510.20490v1', 'Simultaneous Stiffness and Trajectory Optimization for Energy Minimization of Pick-and-Place Tasks of SEA-Actuated Parallel Kinematic Manipulators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Kordik, Hubert Gattringer, Andreas Mueller

**分类**: cs.RO, math.DS

**发布日期**: 2025-10-23

**期刊**: Journal of Computational and Nonlinear Dynamics, Volume 20, Issue 8, August 2025

**DOI**: [10.1115/1.4068321](https://doi.org/10.1115/1.4068321)

---

## 💡 一句话要点

**针对SEA驱动并联机器人，提出刚度和轨迹同步优化方法以最小化能量消耗**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `并联机器人` `串联弹性驱动器` `能量优化` `轨迹规划` `刚度优化` `最优控制` `动态建模`

## 📋 核心要点

1. 工业机器人常执行重复性取放任务，能量消耗是关键问题。传统方法未充分利用弹性元件的潜力。
2. 本文提出一种同步优化轨迹和SEA刚度的方法，通过激发固有运动的振荡特性来降低能耗。
3. 实验结果表明，该方法在并联机器人应用中有效降低了能量消耗，验证了方法的有效性。

## 📝 摘要（中文）

本文研究了采用串联弹性驱动器（SEA）的并联机器人（PKM）在执行重复的取放任务时，如何最小化能量消耗。核心思想是激发由驱动器弹簧产生的固有运动，并利用其振荡特性。针对一个预定的循环取放操作，建立了SEA驱动PKM的动态模型。随后，构建了一个能量最小化的最优控制问题，其中同时优化操作轨迹和SEA刚度。优化驱动器刚度并非指可变刚度驱动器，而是作为设计和尺寸确定过程的工具。通过两个（并联）机器人应用验证了能量降低的假设，并探讨了冗余驱动。

## 🔬 方法详解

**问题定义**：论文旨在解决SEA驱动的并联机器人在执行重复取放任务时能量消耗过高的问题。现有方法通常没有充分利用SEA的弹性特性，导致能量效率不高。此外，如何同时优化轨迹和驱动器的刚度以达到最佳能量效率也是一个挑战。

**核心思路**：论文的核心思路是利用SEA的弹性特性，通过激发系统的固有运动并利用其振荡特性来减少能量消耗。通过同步优化机器人的运动轨迹和SEA的刚度，使系统在运动过程中能够更有效地存储和释放能量，从而降低整体的能量消耗。

**技术框架**：该方法首先建立SEA驱动的并联机器人的动态模型。然后，将能量最小化问题形式化为一个最优控制问题，其中控制变量包括机器人的运动轨迹和SEA的刚度。通过求解该最优控制问题，可以得到能量消耗最小的运动轨迹和SEA刚度。该框架包括以下主要步骤：1) 建立SEA驱动PKM的动态模型；2) 构建能量最小化的最优控制问题；3) 同步优化操作轨迹和SEA刚度；4) 通过实验验证方法的有效性。

**关键创新**：该论文的关键创新在于提出了一个同步优化轨迹和SEA刚度的方法，从而能够充分利用SEA的弹性特性来降低能量消耗。与传统方法相比，该方法能够更有效地利用系统的固有运动，从而实现更高的能量效率。此外，该方法还考虑了冗余驱动的情况，使其更适用于实际应用。

**关键设计**：在最优控制问题的构建中，需要选择合适的性能指标来衡量能量消耗。同时，需要选择合适的优化算法来求解该问题。在实验验证中，需要选择合适的机器人平台和实验参数，以确保实验结果的可靠性。SEA刚度的优化并非指可变刚度驱动器，而是作为设计和尺寸确定过程的工具。

## 📊 实验亮点

论文通过两个并联机器人应用验证了该方法的有效性。实验结果表明，通过同步优化轨迹和SEA刚度，可以显著降低机器人的能量消耗。此外，论文还探讨了冗余驱动对能量消耗的影响，为实际应用提供了有价值的参考。

## 🎯 应用场景

该研究成果可应用于工业机器人、自动化生产线等领域，尤其适用于需要长时间重复执行取放任务的场景。通过降低机器人的能量消耗，可以显著降低生产成本，提高生产效率，并减少对环境的影响。未来，该方法有望推广到其他类型的机器人和自动化系统中。

## 📄 摘要（原文）

> A major field of industrial robot applications deals with repetitive tasks that alternate between operating points. For these so-called pick-and-place operations, parallel kinematic manipulators (PKM) are frequently employed. These tasks tend to automatically run for a long period of time and therefore minimizing energy consumption is always of interest. Recent research addresses this topic by the use of elastic elements and particularly series elastic actuators (SEA). This paper explores the possibilities of minimizing energy consumption of SEA actuated PKM performing pick-and-place tasks. The basic idea is to excite eigenmotions that result from the actuator springs and exploit their oscillating characteristics. To this end, a prescribed cyclic pick-and-place operation is analyzed and a dynamic model of SEA driven PKM is derived. Subsequently, an energy minimizing optimal control problem is formulated where operating trajectories as well as SEA stiffnesses are optimized simultaneously. Here, optimizing the actuator stiffness does not account for variable stiffness actuators. It serves as a tool for the design and dimensioning process. The hypothesis on energy reduction is tested on two (parallel) robot applications where redundant actuation is also addressed. The results confirm the validity of this approach.

