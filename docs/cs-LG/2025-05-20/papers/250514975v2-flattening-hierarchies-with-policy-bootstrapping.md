---
layout: default
title: Flattening Hierarchies with Policy Bootstrapping
---

# Flattening Hierarchies with Policy Bootstrapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14975" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14975v2</a>
  <a href="https://arxiv.org/pdf/2505.14975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14975v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14975v2', 'Flattening Hierarchies with Policy Bootstrapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: John L. Zhou, Jonathan C. Kao

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-05-20 (更新: 2025-10-15)

**备注**: NeurIPS 2025 (Spotlight, top 3.2%)

**🔗 代码/项目**: [PROJECT_PAGE](https://johnlyzhou.github.io/saw/)

---

## 💡 一句话要点

**提出一种新算法以解决长时间目标条件强化学习中的层次性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `目标条件强化学习` `层次强化学习` `优势加权重要性采样` `高维控制` `策略训练`

## 📋 核心要点

1. 现有的目标条件强化学习方法在长时间目标任务中面临稀疏奖励和折扣的挑战，难以有效扩展。
2. 本文提出了一种通过优势加权重要性采样引导子目标条件策略的算法，旨在训练平坦的目标条件策略。
3. 实验结果表明，该方法在多种状态和像素基础的运动与操作基准上超越了现有的离线GCRL算法，适应复杂任务。

## 📝 摘要（中文）

离线目标条件强化学习（GCRL）是一种有前景的方法，用于在大规模无奖励轨迹数据集上预训练通用策略。然而，由于稀疏奖励和折扣的结合，使得将GCRL扩展到更长的时间范围变得具有挑战性。现有的层次强化学习方法在长时间目标达成任务上表现良好，但其对模块化、特定时间尺度策略和子目标生成的依赖增加了复杂性，限制了在高维目标空间的扩展。本文提出了一种通过优势加权重要性采样对子目标条件策略进行引导的算法，以训练平坦的（非层次）目标条件策略。我们的研究表明，该方法在复杂的长时间任务中表现优异，超越了现有的离线GCRL算法。

## 🔬 方法详解

**问题定义**：本文旨在解决长时间目标条件强化学习中由于稀疏奖励和折扣导致的策略训练困难，现有层次方法的复杂性限制了其在高维目标空间的应用。

**核心思路**：通过引导子目标条件策略，利用优势加权重要性采样来训练一个平坦的目标条件策略，从而简化模型结构并提高扩展性。

**技术框架**：整体框架包括对子目标的条件策略进行训练，利用优势加权重要性采样来优化策略，避免了对生成模型的需求，适应高维控制任务。

**关键创新**：本研究的主要创新在于消除了对（子）目标空间生成模型的需求，使得在大状态空间中的扩展成为可能，与现有层次方法相比，简化了策略设计。

**关键设计**：在算法实现中，采用了优势加权重要性采样作为核心技术，设计了适应高维控制的损失函数和网络结构，确保了策略的有效性和稳定性。

## 📊 实验亮点

实验结果显示，本文方法在多项状态和像素基础的基准测试中，性能与现有最先进的离线GCRL算法相当或更优，尤其在复杂的长时间任务中，表现出显著的提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、智能制造等高维复杂任务场景。通过简化策略训练过程，能够有效提升系统在长时间目标达成任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Offline goal-conditioned reinforcement learning (GCRL) is a promising approach for pretraining generalist policies on large datasets of reward-free trajectories, akin to the self-supervised objectives used to train foundation models for computer vision and natural language processing. However, scaling GCRL to longer horizons remains challenging due to the combination of sparse rewards and discounting, which obscures the comparative advantages of primitive actions with respect to distant goals. Hierarchical RL methods achieve strong empirical results on long-horizon goal-reaching tasks, but their reliance on modular, timescale-specific policies and subgoal generation introduces significant additional complexity and hinders scaling to high-dimensional goal spaces. In this work, we introduce an algorithm to train a flat (non-hierarchical) goal-conditioned policy by bootstrapping on subgoal-conditioned policies with advantage-weighted importance sampling. Our approach eliminates the need for a generative model over the (sub)goal space, which we find is key for scaling to high-dimensional control in large state spaces. We further show that existing hierarchical and bootstrapping-based approaches correspond to specific design choices within our derivation. Across a comprehensive suite of state- and pixel-based locomotion and manipulation benchmarks, our method matches or surpasses state-of-the-art offline GCRL algorithms and scales to complex, long-horizon tasks where prior approaches fail. Project page: https://johnlyzhou.github.io/saw/

