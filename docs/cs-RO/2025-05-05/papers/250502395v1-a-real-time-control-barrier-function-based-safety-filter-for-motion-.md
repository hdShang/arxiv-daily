---
layout: default
title: A Real-Time Control Barrier Function-Based Safety Filter for Motion Planning with Arbitrary Road Boundary Constraints
---

# A Real-Time Control Barrier Function-Based Safety Filter for Motion Planning with Arbitrary Road Boundary Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02395" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02395v1</a>
  <a href="https://arxiv.org/pdf/2505.02395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02395v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02395v1', 'A Real-Time Control Barrier Function-Based Safety Filter for Motion Planning with Arbitrary Road Boundary Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianye Xu, Chang Che, Bassam Alrifaee

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出基于控制屏障函数的实时安全过滤器以解决运动规划中的碰撞避免问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `控制屏障函数` `运动规划` `碰撞避免` `实时系统` `优化算法` `自动驾驶` `智能交通`

## 📋 核心要点

1. 现有运动规划方法在处理复杂道路边界时常常依赖保守的近似，导致安全性不足和效率低下。
2. 本文提出的安全过滤器利用控制屏障函数，能够直接处理任意形状的道路几何，确保碰撞避免。
3. 通过大量的数值实验验证，该方法在复杂交通场景下表现出高达40 Hz的执行频率，安全性和效率均有显著提升。

## 📝 摘要（中文）

本文提出了一种实时安全过滤器，旨在运动规划（如基于学习的方法）中使用控制屏障函数（CBFs），为避免与道路边界的碰撞提供形式化保障。该方法的一个关键特性是能够直接纳入任意形状的道路几何，而无需依赖保守的过度近似。我们将安全过滤器形式化为一个约束优化问题，采用二次规划（QP）形式。通过对名义运动规划器发出的控制动作进行最小必要的调整，实现安全性。我们通过在多种复杂道路交通场景下进行广泛的数值实验验证了该安全过滤器的有效性，结果表明其安全性可靠且计算效率高（执行频率可达40 Hz）。

## 🔬 方法详解

**问题定义**：本文旨在解决运动规划中与道路边界碰撞避免的问题。现有方法在处理复杂道路几何时，往往需要保守的近似，导致安全性不足和效率低下。

**核心思路**：我们提出的安全过滤器基于控制屏障函数，能够直接纳入任意形状的道路几何，避免了保守近似的需要。通过将安全性问题形式化为约束优化问题，确保在调整控制动作时保持安全。

**技术框架**：整体架构包括三个主要模块：首先是名义运动规划器生成初步控制动作；其次是安全过滤器对这些动作进行调整以满足安全约束；最后是执行调整后的控制动作。

**关键创新**：本研究的主要创新在于能够处理任意形状的道路几何，避免了传统方法中的保守近似，从而提高了安全性和效率。

**关键设计**：在设计中，我们采用了二次规划（QP）形式来解决约束优化问题，确保调整的控制动作是最小必要的。同时，设置了合适的参数以平衡安全性与控制效率。

## 📊 实验亮点

实验结果表明，所提出的安全过滤器在多种复杂交通场景下能够可靠地避免碰撞，执行频率高达40 Hz，显著优于传统方法，确保了在动态环境中的安全性和实时性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提供可靠的碰撞避免机制，该方法能够显著提升自动化系统在复杂环境中的安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present a real-time safety filter for motion planning, such as learning-based methods, using Control Barrier Functions (CBFs), which provides formal guarantees for collision avoidance with road boundaries. A key feature of our approach is its ability to directly incorporate road geometries of arbitrary shape without resorting to conservative overapproximations. We formulate the safety filter as a constrained optimization problem in the form of a Quadratic Program (QP). It achieves safety by making minimal, necessary adjustments to the control actions issued by the nominal motion planner. We validate our safety filter through extensive numerical experiments across a variety of traffic scenarios featuring complex roads. The results confirm its reliable safety and high computational efficiency (execution frequency up to 40 Hz). Code & Video Demo: github.com/bassamlab/SigmaRL

