---
layout: default
title: Probabilistically-Safe Bipedal Navigation over Uncertain Terrain via Conformal Prediction and Contraction Analysis
---

# Probabilistically-Safe Bipedal Navigation over Uncertain Terrain via Conformal Prediction and Contraction Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07725" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07725v1</a>
  <a href="https://arxiv.org/pdf/2510.07725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07725v1" onclick="toggleFavorite(this, '2510.07725v1', 'Probabilistically-Safe Bipedal Navigation over Uncertain Terrain via Conformal Prediction and Contraction Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kasidit Muenprasitivej, Ye Zhao, Glen Chou

**分类**: cs.RO

**发布日期**: 2025-10-09

**备注**: 9 pages, 4 figures

---

## 💡 一句话要点

**提出基于一致性预测和收缩分析的概率安全双足机器人导航方法，解决地形不确定性下的稳健行走问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `双足机器人` `崎岖地形导航` `概率安全` `一致性预测` `收缩分析` `模型预测控制` `高斯过程回归`

## 📋 核心要点

1. 现有双足机器人在崎岖地形导航中，难以同时保证动态可行性、质心鲁棒性以及地形不确定性下的安全性。
2. 利用高斯过程回归和一致性预测对地形不确定性建模，并结合基于收缩分析的可达管和扭矩控制，实现概率安全导航。
3. 通过MuJoCo仿真Digit双足机器人，验证了所提框架在崎岖地形下的安全导航能力和目标可达性。

## 📝 摘要（中文）

本文提出了一种概率安全的规划和控制策略，旨在使双足机器人能够在粗糙地形上行走，确保在地形不确定性下具有动态可行性和质心鲁棒性。具体而言，我们提出了一个高层模型预测控制（MPC）导航框架，该框架为双足机器人指定了安全置信水平，(i) 能够在具有不确定高程的地形图上安全地朝期望的目标位置移动，并且 (ii) 将不确定性边界正式纳入运动控制的质心动力学中。为了对粗糙地形进行建模，我们采用高斯过程（GP）回归来估计高程图，并利用一致性预测（CP）来构建校准的置信区间，以捕获真实的地形高程。在此基础上，我们制定了基于收缩的可达管，明确考虑了地形不确定性，从而确保状态收敛和管不变性。此外，我们为降阶线性倒立摆模型（LIPM）引入了一种基于收缩的飞轮扭矩控制律，该控制律稳定了关于质心（CoM）的角动量。该公式提供了概率安全性和目标可达性保证。对于给定的置信水平，我们通过证明实际CoM相空间轨迹和高层规划器规定的期望轨迹的指数稳定，来建立所提出的扭矩控制律的前向不变性。最后，我们通过MuJoCo中Digit双足机器人的基于物理的仿真来评估我们的规划框架的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决双足机器人在未知或不确定地形上的安全导航问题。现有方法通常难以在保证动态可行性的同时，有效处理地形高度的不确定性，导致机器人容易跌倒或无法到达目标点。因此，需要一种能够在地形不确定性下，提供概率安全保证的导航方法。

**核心思路**：论文的核心思路是将地形不确定性纳入到规划和控制框架中，通过高斯过程回归和一致性预测来估计地形高度的置信区间，并利用基于收缩分析的可达管来保证状态收敛和管不变性。同时，设计基于收缩的扭矩控制律来稳定机器人的角动量，从而实现概率安全和目标可达性。

**技术框架**：整体框架包含以下几个主要模块：1) 地形建模：使用高斯过程回归估计地形高度，并利用一致性预测构建置信区间。2) 高层规划：使用模型预测控制（MPC）生成期望的质心轨迹。3) 可达管生成：基于收缩分析，考虑地形不确定性，生成保证状态收敛和管不变性的可达管。4) 低层控制：设计基于收缩的飞轮扭矩控制律，稳定角动量。

**关键创新**：论文的关键创新在于将一致性预测与收缩分析相结合，为双足机器人的导航提供了概率安全保证。具体来说，一致性预测能够提供校准的置信区间，准确反映地形高度的不确定性；而收缩分析则能够保证状态收敛和管不变性，从而确保机器人在不确定地形下的安全行走。

**关键设计**：关键设计包括：1) 高斯过程回归的核函数选择和参数优化。2) 一致性预测的置信水平选择。3) 基于收缩分析的可达管的构造方法，需要仔细选择收缩率和李雅普诺夫函数。4) 飞轮扭矩控制律的设计，需要平衡稳定性和控制力矩的大小。

## 📊 实验亮点

通过MuJoCo仿真Digit双足机器人，验证了所提框架的有效性。实验结果表明，该方法能够在崎岖地形下实现安全导航，并保证目标可达性。具体而言，在给定的置信水平下，机器人能够成功避开障碍物，并稳定地朝目标点移动，证明了该方法在地形不确定性下的鲁棒性和安全性。

## 🎯 应用场景

该研究成果可应用于搜索救援、灾后重建、复杂地形勘探等领域。通过提升双足机器人在不确定环境下的导航能力，可以使其在人类难以到达的危险区域执行任务，从而降低人员伤亡风险，提高工作效率。未来，该技术有望进一步推广到其他类型的机器人，例如四足机器人和人形机器人。

## 📄 摘要（原文）

> We address the challenge of enabling bipedal robots to traverse rough terrain by developing probabilistically safe planning and control strategies that ensure dynamic feasibility and centroidal robustness under terrain uncertainty. Specifically, we propose a high-level Model Predictive Control (MPC) navigation framework for a bipedal robot with a specified confidence level of safety that (i) enables safe traversal toward a desired goal location across a terrain map with uncertain elevations, and (ii) formally incorporates uncertainty bounds into the centroidal dynamics of locomotion control. To model the rough terrain, we employ Gaussian Process (GP) regression to estimate elevation maps and leverage Conformal Prediction (CP) to construct calibrated confidence intervals that capture the true terrain elevation. Building on this, we formulate contraction-based reachable tubes that explicitly account for terrain uncertainty, ensuring state convergence and tube invariance. In addition, we introduce a contraction-based flywheel torque control law for the reduced-order Linear Inverted Pendulum Model (LIPM), which stabilizes the angular momentum about the center-of-mass (CoM). This formulation provides both probabilistic safety and goal reachability guarantees. For a given confidence level, we establish the forward invariance of the proposed torque control law by demonstrating exponential stabilization of the actual CoM phase-space trajectory and the desired trajectory prescribed by the high-level planner. Finally, we evaluate the effectiveness of our planning framework through physics-based simulations of the Digit bipedal robot in MuJoCo.

