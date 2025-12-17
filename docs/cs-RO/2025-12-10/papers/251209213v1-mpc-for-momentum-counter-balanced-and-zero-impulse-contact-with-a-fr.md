---
layout: default
title: MPC for momentum counter-balanced and zero-impulse contact with a free-spinning satellite
---

# MPC for momentum counter-balanced and zero-impulse contact with a free-spinning satellite

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09213" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09213v1</a>
  <a href="https://arxiv.org/pdf/2512.09213.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09213v1" onclick="toggleFavorite(this, '2512.09213v1', 'MPC for momentum counter-balanced and zero-impulse contact with a free-spinning satellite')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Theofania Karampela, Rishie Seshadri, Florian Dörfler, Sarah H. Q. Li

**分类**: eess.SY, cs.RO

**发布日期**: 2025-12-10

**备注**: 21 pages, 4 figures, 5 tables, submission for AIAA SciTech 2026 conference

---

## 💡 一句话要点

**提出基于MPC的控制框架，实现服务卫星与自由旋转目标卫星的零冲量接触**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `模型预测控制` `在轨服务` `零冲量接触` `卫星控制` `机器人操作`

## 📋 核心要点

1. 在轨服务任务中，服务卫星与自由旋转目标卫星的接触能力至关重要，现有方法难以兼顾驱动约束和状态约束。
2. 论文提出基于非线性模型预测控制（MPC）的框架，显式建模服务卫星力矩生成模块和操作模块之间的交叉耦合动力学。
3. 通过蒙特卡罗仿真验证了MPC控制器在各种约束和噪声条件下，维持自旋同步和零冲量接触的有效性，优于现有方法。

## 📝 摘要（中文）

本文提出了一种非线性模型预测控制（MPC）框架，用于生成服务卫星的可行控制策略，以实现与自由旋转目标卫星的零冲量接触。该操作需要服务卫星的两个独立驱动模块之间的协调：(1)力矩生成模块和(2)操作模块。我们应用MPC来控制这两个模块，并显式地对它们之间的交叉耦合动力学进行建模。结果表明，MPC控制器可以强制执行现有控制方法无法考虑的驱动和状态约束。通过数值蒙特卡罗（MC）试验模拟与自由旋转目标卫星的零冲量接触场景，并将仿真结果与先前的控制方法进行比较，评估了MPC控制器的性能。仿真结果验证了MPC控制器在操作约束、移动接触位置以及观测和驱动噪声下，保持自旋同步和零冲量接触的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决服务卫星与自由旋转目标卫星进行零冲量接触的问题。现有控制方法难以同时考虑驱动器和状态约束，并且对服务卫星的两个模块（力矩生成和操作模块）之间的耦合动力学建模不足，导致控制精度和鲁棒性下降。

**核心思路**：论文的核心思路是利用非线性模型预测控制（MPC）来显式地建模和控制服务卫星的两个模块，并考虑它们之间的交叉耦合动力学。MPC能够预测系统未来的状态，并根据约束条件优化控制输入，从而实现更精确和鲁棒的控制。

**技术框架**：整体框架包括以下几个主要部分：1) 建立服务卫星和目标卫星的动力学模型，包括两个模块的运动学和动力学方程，以及它们之间的耦合项。2) 设计MPC控制器，包括状态空间表示、预测模型、成本函数和约束条件。3) 通过数值仿真验证MPC控制器的性能，并与现有控制方法进行比较。

**关键创新**：论文的关键创新在于：1) 显式地建模了服务卫星两个模块之间的交叉耦合动力学，提高了控制精度。2) 利用MPC能够处理约束的特性，强制执行驱动器和状态约束，提高了控制器的鲁棒性。3) 提出了一种适用于零冲量接触的MPC控制框架，为在轨服务任务提供了一种新的解决方案。

**关键设计**：MPC控制器的关键设计包括：1) 状态空间表示：选择合适的状态变量，如位置、速度、姿态和角速度，来描述系统的状态。2) 预测模型：利用动力学模型预测系统未来的状态。3) 成本函数：设计合适的成本函数，以最小化接触时的冲击力，并保持自旋同步。4) 约束条件：考虑驱动器的最大力矩和角速度限制，以及避免碰撞等约束。

## 📊 实验亮点

通过蒙特卡罗仿真，验证了MPC控制器在存在观测和驱动噪声的情况下，仍能有效保持自旋同步和零冲量接触。与现有控制方法相比，该MPC控制器能够更好地处理操作约束，并实现更精确的接触控制，从而提高了在轨服务任务的可靠性。

## 🎯 应用场景

该研究成果可应用于在轨服务（OOS）任务，例如卫星燃料加注、故障维修、部件更换和退役卫星移除等。通过精确控制服务卫星与目标卫星的接触，可以降低操作风险，提高任务成功率，并为未来的空间探索和资源利用提供技术支持。

## 📄 摘要（原文）

> In on-orbit robotics, a servicer satellite's ability to make contact with a free-spinning target satellite is essential to completing most on-orbit servicing (OOS) tasks. This manuscript develops a nonlinear model predictive control (MPC) framework that generates feasible controls for a servicer satellite to achieve zero-impulse contact with a free-spinning target satellite. The overall maneuver requires coordination between two separately actuated modules of the servicer satellite: (1) a moment generation module and (2) a manipulation module. We apply MPC to control both modules by explicitly modeling the cross-coupling dynamics between them. We demonstrate that the MPC controller can enforce actuation and state constraints that prior control approaches could not account for. We evaluate the performance of the MPC controller by simulating zero-impulse contact scenarios with a free-spinning target satellite via numerical Monte Carlo (MC) trials and comparing the simulation results with prior control approaches. Our simulation results validate the effectiveness of the MPC controller in maintaining spin synchronization and zero-impulse contact under operation constraints, moving contact location, and observation and actuation noise.

