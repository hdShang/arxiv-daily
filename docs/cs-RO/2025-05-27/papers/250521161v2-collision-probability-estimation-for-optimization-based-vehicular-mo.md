---
layout: default
title: Collision Probability Estimation for Optimization-based Vehicular Motion Planning
---

# Collision Probability Estimation for Optimization-based Vehicular Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21161" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21161v2</a>
  <a href="https://arxiv.org/pdf/2505.21161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21161v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21161v2', 'Collision Probability Estimation for Optimization-based Vehicular Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leon Tolksdorf, Arturo Tejada, Christian Birkner, Nathan van de Wouw

**分类**: cs.RO, math.OC

**发布日期**: 2025-05-27 (更新: 2025-05-30)

**备注**: 14 pages, 6 figures

---

## 💡 一句话要点

**提出基于优化的碰撞概率估计以提升自动驾驶运动规划**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `碰撞概率估计` `自动驾驶` `运动规划` `随机模型预测控制` `高斯不确定性` `多圆形近似` `安全保障`

## 📋 核心要点

1. 现有的碰撞概率估计方法多基于采样，计算效率低且结果不确定，难以满足优化算法的需求。
2. 本文提出通过多圆形近似来估计两辆车的碰撞概率，考虑了车辆形状及运动预测的不确定性，尤其是朝向角度。
3. 实验结果表明，所提算法在处理不同不确定性水平时，能够生成可重复的轨迹并保持控制器的可行性。

## 📝 摘要（中文）

许多自动驾驶的运动规划算法需要估计碰撞概率（POC），以应对道路使用者运动测量和估计中的不确定性。现有的POC估计技术多采用基于采样的方法，存在计算效率低和估计结果不确定性的问题。本文提出了一种通过多圆形近似来估计两辆车之间的POC的方法，模型中考虑了车辆的形状和运动预测的不确定性，特别是车辆的朝向角度。我们保证所提供的POC是一个过度估计，这对于提供安全保障至关重要，并提出了一种计算效率高的算法，用于在位置和朝向的高斯不确定性下计算POC估计。该算法被应用于路径跟踪的随机模型预测控制器（SMPC）中，生成可重复的轨迹，同时保持控制器的可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶中碰撞概率估计的计算效率低和结果不确定性的问题。现有方法多依赖于采样，导致每次估计结果有所不同，无法满足优化算法的需求。

**核心思路**：我们提出了一种新的碰撞概率估计方法，通过多圆形近似来表示车辆形状，并将车辆的位置信息和朝向视为随机变量，从而更准确地捕捉运动预测中的不确定性。

**技术框架**：该方法的整体架构包括碰撞概率的计算模块和随机模型预测控制器（SMPC）。首先，通过多圆形近似计算两辆车的碰撞概率，然后将该估计结果应用于SMPC中进行运动规划。

**关键创新**：最重要的创新在于将车辆的朝向角度纳入碰撞概率的估计中，确保所提供的POC为过度估计，从而增强安全性。这一设计与现有方法的本质区别在于对朝向角度的重视。

**关键设计**：在算法实现中，采用高斯分布来描述位置和朝向的不确定性，确保计算效率高且结果稳定。关键参数设置包括多圆形近似的精度和高斯分布的方差，这些设计使得算法在不同不确定性水平下均能有效工作。

## 📊 实验亮点

实验结果显示，所提算法在处理不同不确定性水平时，能够生成可重复的轨迹，并在多个测试案例中保持控制器的可行性。与传统方法相比，碰撞概率估计的计算效率显著提高，确保了优化算法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的运动规划、智能交通系统以及机器人导航等。通过提供高效且可靠的碰撞概率估计，能够显著提升自动驾驶系统的安全性和可行性，推动智能交通技术的发展。

## 📄 摘要（原文）

> Many motion planning algorithms for automated driving require estimating the probability of collision (POC) to account for uncertainties in the measurement and estimation of the motion of road users. Common POC estimation techniques often utilize sampling-based methods that suffer from computational inefficiency and a non-deterministic estimation, i.e., each estimation result for the same inputs is slightly different. In contrast, optimization-based motion planning algorithms require computationally efficient POC estimation, ideally using deterministic estimation, such that typical optimization algorithms for motion planning retain feasibility. Estimating the POC analytically, however, is challenging because it depends on understanding the collision conditions (e.g., vehicle's shape) and characterizing the uncertainty in motion prediction. In this paper, we propose an approach in which we estimate the POC between two vehicles by over-approximating their shapes by a multi-circular shape approximation. The position and heading of the predicted vehicle are modelled as random variables, contrasting with the literature, where the heading angle is often neglected. We guarantee that the provided POC is an over-approximation, which is essential in providing safety guarantees, and present a computationally efficient algorithm for computing the POC estimate for Gaussian uncertainty in the position and heading. This algorithm is then used in a path-following stochastic model predictive controller (SMPC) for motion planning. With the proposed algorithm, the SMPC generates reproducible trajectories while the controller retains its feasibility in the presented test cases and demonstrates the ability to handle varying levels of uncertainty.

