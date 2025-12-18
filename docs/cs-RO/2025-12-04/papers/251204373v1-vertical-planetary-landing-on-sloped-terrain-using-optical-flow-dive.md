---
layout: default
title: Vertical Planetary Landing on Sloped Terrain Using Optical Flow Divergence Estimates
---

# Vertical Planetary Landing on Sloped Terrain Using Optical Flow Divergence Estimates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04373" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04373v1</a>
  <a href="https://arxiv.org/pdf/2512.04373.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04373v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04373v1', 'Vertical Planetary Landing on Sloped Terrain Using Optical Flow Divergence Estimates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hann Woei Ho, Ye Zhou

**分类**: cs.RO

**发布日期**: 2025-12-04

**备注**: This paper is accepted at International Astronautical Congress (IAC 2025)

---

## 💡 一句话要点

**提出基于光流散度估计的非线性控制策略，实现斜坡地形上的垂直行星着陆**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `行星着陆` `光流散度` `非线性控制` `斜坡地形` `自主导航`

## 📋 核心要点

1. 小型航天器在斜坡地形自主着陆面临计算资源和传感器载荷的限制，传统方法难以兼顾鲁棒性和效率。
2. 该论文提出一种基于局部光流散度估计的非线性控制策略，通过调节推力和姿态，实现平稳着陆和地形对齐。
3. 数值模拟结果表明，该方法在不同斜坡和散度设定点下均能实现稳定的着陆，验证了其鲁棒性和有效性。

## 📝 摘要（中文）

对于小型轻量级航天器（如旋翼飞行器和着陆器）而言，在倾斜地形上自主着陆是一项重大挑战。这些航天器处理能力和有效载荷有限，使得先进的深度学习方法和重型传感器不切实际。飞行昆虫（如蜜蜂）以极少的神经和感觉资源实现了卓越的着陆，这主要依赖于光流。通过调节光流散度（垂直速度除以高度的度量），它们可以平稳着陆，其中速度和高度以指数形式衰减。然而，将这种受生物启发的策略用于航天器在倾斜地形上的着陆面临两个关键挑战：全局光流散度估计会掩盖地形倾斜度，并且基于散度的控制的非线性特性在使用传统控制器时可能导致不稳定。本文提出了一种非线性控制策略，该策略利用两个不同的局部光流散度估计来调节垂直着陆期间的推力和姿态。该控制律基于增量非线性动态逆来处理非线性光流散度。推力控制通过保持局部光流散度估计的恒定平均值来确保平稳的垂直下降，而姿态控制通过利用它们的差异使飞行器在触地时与倾斜表面对齐。该方法在数值模拟中使用简化的2D航天器模型，在不同的斜坡和散度设定点上进行了评估。结果表明，调节平均散度可以实现稳定的着陆，并使速度和高度呈指数衰减，而使用散度差可以有效地与倾斜地形对齐。总的来说，该方法提供了一种鲁棒、低资源的着陆策略，增强了小型航天器自主行星任务的可行性。

## 🔬 方法详解

**问题定义**：小型航天器在斜坡地形上自主着陆面临计算资源和传感器载荷的限制。传统控制方法难以处理地形倾斜带来的干扰，且基于全局光流散度的控制策略无法有效区分地形倾斜和航天器姿态，容易导致着陆失败。此外，光流散度与控制量之间的非线性关系也给控制器设计带来了挑战。

**核心思路**：该论文借鉴了昆虫利用光流进行平稳着陆的生物启发式方法，并针对斜坡地形着陆的特殊性进行了改进。核心思路是利用两个局部光流散度估计，分别用于控制推力和姿态。通过调节局部光流散度的平均值，实现平稳的垂直下降；通过调节局部光流散度的差异，实现与倾斜地形的对齐。

**技术框架**：该方法主要包含两个控制环路：推力控制环路和姿态控制环路。推力控制环路通过调节发动机推力，使两个局部光流散度的平均值保持在设定的目标值附近，从而实现平稳的垂直下降。姿态控制环路通过调节航天器的姿态，使两个局部光流散度的差异趋近于零，从而实现与倾斜地形的对齐。整个控制系统基于增量非线性动态逆（Incremental Nonlinear Dynamic Inversion）方法设计，以处理光流散度的非线性特性。

**关键创新**：该方法最重要的创新点在于利用局部光流散度差异进行姿态控制。与传统的基于全局光流散度的方法相比，该方法能够有效区分地形倾斜和航天器姿态，从而实现更精确的地形对齐。此外，采用增量非线性动态逆方法，能够有效处理光流散度的非线性特性，提高控制系统的鲁棒性。

**关键设计**：该方法的关键设计包括：1) 局部光流散度估计器的设计，需要选择合适的图像特征和光流算法，以保证估计的准确性和鲁棒性；2) 推力控制和姿态控制环路的设计，需要选择合适的控制参数，以保证系统的稳定性和响应速度；3) 增量非线性动态逆控制器的设计，需要选择合适的模型和参数，以保证控制精度和鲁棒性。

## 📊 实验亮点

数值模拟结果表明，该方法在不同的斜坡角度和散度设定点下均能实现稳定的着陆。通过调节平均散度，航天器的速度和高度呈指数衰减，实现了平稳的垂直下降。通过调节散度差异，航天器能够有效地与倾斜地形对齐，减小了触地时的冲击力。该方法无需复杂的传感器和大量的计算资源，具有很高的实用价值。

## 🎯 应用场景

该研究成果可应用于小型行星着陆器、无人机等需要在复杂地形上自主着陆的场景。例如，可用于月球、火星等行星表面的探测任务，也可用于灾后救援、环境监测等领域。该方法具有低资源、高鲁棒性的特点，有望降低自主着陆系统的成本和复杂性，提高任务的成功率。

## 📄 摘要（原文）

> Autonomous landing on sloped terrain poses significant challenges for small, lightweight spacecraft, such as rotorcraft and landers. These vehicles have limited processing capability and payload capacity, which makes advanced deep learning methods and heavy sensors impractical. Flying insects, such as bees, achieve remarkable landings with minimal neural and sensory resources, relying heavily on optical flow. By regulating flow divergence, a measure of vertical velocity divided by height, they perform smooth landings in which velocity and height decay exponentially together. However, adapting this bio-inspired strategy for spacecraft landings on sloped terrain presents two key challenges: global flow-divergence estimates obscure terrain inclination, and the nonlinear nature of divergence-based control can lead to instability when using conventional controllers. This paper proposes a nonlinear control strategy that leverages two distinct local flow divergence estimates to regulate both thrust and attitude during vertical landings. The control law is formulated based on Incremental Nonlinear Dynamic Inversion to handle the nonlinear flow divergence. The thrust control ensures a smooth vertical descent by keeping a constant average of the local flow divergence estimates, while the attitude control aligns the vehicle with the inclined surface at touchdown by exploiting their difference. The approach is evaluated in numerical simulations using a simplified 2D spacecraft model across varying slopes and divergence setpoints. Results show that regulating the average divergence yields stable landings with exponential decay of velocity and height, and using the divergence difference enables effective alignment with inclined terrain. Overall, the method offers a robust, low-resource landing strategy that enhances the feasibility of autonomous planetary missions with small spacecraft.

