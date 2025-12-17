---
layout: default
title: Iterative Tuning of Nonlinear Model Predictive Control for Robotic Manufacturing Tasks
---

# Iterative Tuning of Nonlinear Model Predictive Control for Robotic Manufacturing Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13170" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13170v1</a>
  <a href="https://arxiv.org/pdf/2512.13170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13170v1" onclick="toggleFavorite(this, '2512.13170v1', 'Iterative Tuning of Nonlinear Model Predictive Control for Robotic Manufacturing Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deepak Ingole, Valentin Bhend, Shiva Ganesh Murali, Oliver Dobrich, Alisa Rupenayan

**分类**: cs.RO, cs.LG, eess.SY, math.OC

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出一种基于任务级反馈的非线性模型预测控制迭代调优框架，用于机器人制造任务。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `非线性模型预测控制` `迭代学习控制` `机器人控制` `自适应控制` `机器人制造`

## 📋 核心要点

1. 重复性制造过程易受环境漂移和系统磨损的影响，即使在重复操作中也需要重新调整控制。
2. 该方法通过构建经验灵敏度矩阵，自适应调整NMPC权重，无需解析导数即可实现结构化的权重更新。
3. 在UR10e机器人碳纤维缠绕任务中，仅需4次在线重复即可达到接近离线贝叶斯优化的跟踪性能。

## 📝 摘要（中文）

本文提出了一种迭代学习框架，用于自动调整非线性模型预测控制（NMPC）的权重矩阵，该调整基于任务级性能反馈。受范数最优迭代学习控制（ILC）的启发，该方法自适应地调整NMPC权重Q和R，通过多次任务重复来最小化与跟踪精度、控制努力和饱和度相关的关键性能指标（KPI）。与需要对NMPC求解器进行微分的基于梯度的方法不同，我们构建了一个经验灵敏度矩阵，从而能够在没有解析导数的情况下进行结构化的权重更新。该框架通过在UR10e机器人上执行四面体核心碳纤维缠绕的仿真进行了验证。结果表明，与贝叶斯优化（BO）算法所需的100次离线评估相比，所提出的方法仅需4次在线重复即可收敛到接近最优的跟踪性能（RMSE在离线贝叶斯优化（BO）的0.3%以内）。该方法为重复性机器人任务中的自适应NMPC调优提供了一种实用的解决方案，它结合了精心优化的控制器的精度和在线自适应的灵活性。

## 🔬 方法详解

**问题定义**：论文旨在解决重复性机器人制造任务中，由于环境变化和系统损耗导致非线性模型预测控制（NMPC）性能下降，需要频繁手动调整权重矩阵的问题。现有方法，如基于梯度的方法，需要对NMPC求解器进行微分，计算复杂度高，难以在线应用。

**核心思路**：论文借鉴迭代学习控制（ILC）的思想，通过任务级的性能反馈，迭代地调整NMPC的权重矩阵Q和R，以最小化关键性能指标（KPI），如跟踪误差、控制能量和饱和度。核心在于避免直接计算NMPC的梯度，而是通过构建经验灵敏度矩阵来近似权重更新的方向。

**技术框架**：整体框架包含以下几个主要步骤：1) 执行一次任务；2) 收集任务级的性能指标（KPI）；3) 构建经验灵敏度矩阵，该矩阵描述了权重变化对KPI的影响；4) 基于灵敏度矩阵更新NMPC的权重Q和R；5) 重复上述步骤，直到KPI收敛。

**关键创新**：最重要的创新在于使用经验灵敏度矩阵来近似NMPC的梯度，避免了对NMPC求解器进行微分，从而降低了计算复杂度，使其能够在线应用。与传统的梯度下降方法相比，该方法不需要解析导数，更加灵活，适用于复杂的NMPC模型。

**关键设计**：经验灵敏度矩阵的构建方法是关键。具体来说，通过对权重矩阵进行微小的扰动，观察KPI的变化，从而估计权重变化对KPI的影响。权重更新的幅度由一个学习率参数控制，该参数需要根据具体任务进行调整。KPI的选择也至关重要，需要能够反映任务的性能，例如跟踪误差的均方根误差（RMSE）、控制输入的能量等。

## 📊 实验亮点

在UR10e机器人碳纤维缠绕任务的仿真实验中，该方法仅需4次在线迭代即可达到接近离线贝叶斯优化的跟踪性能（RMSE在离线贝叶斯优化的0.3%以内），而贝叶斯优化需要100次离线评估。这表明该方法能够快速有效地调整NMPC的权重，提高机器人的控制性能。

## 🎯 应用场景

该研究成果可应用于各种重复性的机器人制造任务，例如焊接、喷涂、装配、打磨等。通过自动调整NMPC的权重，可以提高机器人的控制精度和鲁棒性，减少人工干预，提高生产效率。该方法还可扩展到其他类型的控制算法和机器人平台，具有广泛的应用前景。

## 📄 摘要（原文）

> Manufacturing processes are often perturbed by drifts in the environment and wear in the system, requiring control re-tuning even in the presence of repetitive operations. This paper presents an iterative learning framework for automatic tuning of Nonlinear Model Predictive Control (NMPC) weighting matrices based on task-level performance feedback. Inspired by norm-optimal Iterative Learning Control (ILC), the proposed method adaptively adjusts NMPC weights Q and R across task repetitions to minimize key performance indicators (KPIs) related to tracking accuracy, control effort, and saturation. Unlike gradient-based approaches that require differentiating through the NMPC solver, we construct an empirical sensitivity matrix, enabling structured weight updates without analytic derivatives. The framework is validated through simulation on a UR10e robot performing carbon fiber winding on a tetrahedral core. Results demonstrate that the proposed approach converges to near-optimal tracking performance (RMSE within 0.3% of offline Bayesian Optimization (BO)) in just 4 online repetitions, compared to 100 offline evaluations required by BO algorithm. The method offers a practical solution for adaptive NMPC tuning in repetitive robotic tasks, combining the precision of carefully optimized controllers with the flexibility of online adaptation.

