---
layout: default
title: "TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning"
---

# TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00344" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00344v1</a>
  <a href="https://arxiv.org/pdf/2312.00344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00344v1', 'TRC: Trust Region Conditional Value at Risk for Safe Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dohyeong Kim, Songhwai Oh

**分类**: cs.RO, cs.LG

**发布日期**: 2023-12-01

**备注**: RA-L and ICRA 2022

**期刊**: IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 2621-2628, April 2022

**DOI**: [10.1109/LRA.2022.3141829](https://doi.org/10.1109/LRA.2022.3141829)

---

## 💡 一句话要点

**提出TRC方法以实现安全强化学习中的CVaR约束**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `安全强化学习` `条件价值风险` `信任区域` `策略梯度` `机器人导航` `风险控制` `性能优化`

## 📋 核心要点

1. 现有的安全强化学习方法在处理高成本导致的失败概率时存在不足，难以有效满足安全约束。
2. 本文提出的TRC方法通过信任区域和条件价值风险（CVaR）约束，优化了策略的安全性和性能。
3. 实验结果表明，TRC在多种机器人导航任务中表现优异，性能提升达到1.93倍，同时满足所有安全约束。

## 📝 摘要（中文）

安全性在机器人领域至关重要，因此安全强化学习（safe RL）受到了广泛关注。本文提出了一种基于信任区域的安全强化学习方法TRC，旨在最大化期望回报的同时满足条件价值风险（CVaR）约束。我们首先推导了CVaR的上界，并在信任区域内以可微分的形式近似该上界。通过这种近似，构建了一个用于获取策略梯度的子问题，并通过迭代求解该子问题来训练策略。TRC在多种机器人模拟的安全导航任务中进行了评估，并在Clearpath的Jackal机器人上进行了仿真与现实环境的对比实验。与其他安全强化学习方法相比，TRC在所有实验中均满足约束条件，且性能提升了1.93倍。

## 🔬 方法详解

**问题定义**：本文旨在解决安全强化学习中如何有效满足条件价值风险（CVaR）约束的问题。现有方法在高成本情况下的失败概率控制上存在不足，难以保证安全性。

**核心思路**：TRC方法通过信任区域的框架，推导并近似CVaR的上界，以此为基础构建策略梯度的优化问题，从而实现安全与性能的平衡。

**技术框架**：TRC的整体架构包括CVaR上界的推导、可微分近似的构建和策略梯度的子问题求解。主要模块包括安全约束的定义、信任区域的设置及策略的迭代更新。

**关键创新**：TRC的核心创新在于将信任区域方法与CVaR约束结合，形成了一种新的安全强化学习框架，显著提升了策略的安全性和效率。与现有方法相比，TRC在满足约束的同时，优化了策略的回报。

**关键设计**：在设计中，关键参数包括信任区域的大小和CVaR的计算方式，损失函数则结合了回报和安全约束，确保在训练过程中始终满足安全性要求。

## 📊 实验亮点

实验结果显示，TRC方法在多种安全导航任务中表现出色，性能提升达1.93倍，且在所有实验中均满足CVaR约束。这一结果表明TRC在安全强化学习领域的有效性和优越性，超越了现有的安全强化学习方法。

## 🎯 应用场景

TRC方法在机器人导航、自动驾驶和其他需要高安全性的强化学习应用中具有广泛的潜在应用价值。通过有效控制风险，该方法能够提升系统的安全性和可靠性，推动智能机器人在复杂环境中的应用。未来，TRC还可能扩展到更多领域，如金融决策和医疗诊断等，进一步提升决策过程的安全性。

## 📄 摘要（原文）

> As safety is of paramount importance in robotics, reinforcement learning that reflects safety, called safe RL, has been studied extensively. In safe RL, we aim to find a policy which maximizes the desired return while satisfying the defined safety constraints. There are various types of constraints, among which constraints on conditional value at risk (CVaR) effectively lower the probability of failures caused by high costs since CVaR is a conditional expectation obtained above a certain percentile. In this paper, we propose a trust region-based safe RL method with CVaR constraints, called TRC. We first derive the upper bound on CVaR and then approximate the upper bound in a differentiable form in a trust region. Using this approximation, a subproblem to get policy gradients is formulated, and policies are trained by iteratively solving the subproblem. TRC is evaluated through safe navigation tasks in simulations with various robots and a sim-to-real environment with a Jackal robot from Clearpath. Compared to other safe RL methods, the performance is improved by 1.93 times while the constraints are satisfied in all experiments.

