---
layout: default
title: "Drive Fast, Learn Faster: On-Board RL for High Performance Autonomous Racing"
---

# Drive Fast, Learn Faster: On-Board RL for High Performance Autonomous Racing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07321" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07321v1</a>
  <a href="https://arxiv.org/pdf/2505.07321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07321v1', 'Drive Fast, Learn Faster: On-Board RL for High Performance Autonomous Racing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benedict Hildisch, Edoardo Ghignone, Nicolas Baumann, Cheng Hu, Andrea Carron, Michele Magno

**分类**: cs.RO

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出一种基于实时强化学习的自主赛车框架以解决高性能挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主赛车` `强化学习` `实时决策` `软演员-评论家` `多步时间差学习` `异步训练` `动态系统`

## 📋 核心要点

1. 现有的强化学习方法在真实环境中的迁移效果不佳，尤其是在高速度和动态条件下的自主赛车中面临重大挑战。
2. 本文提出了一种车载强化学习框架，消除了对仿真预训练的依赖，采用改进的SAC算法和残差RL结构以增强实时控制能力。
3. 在F1TENTH赛车平台上的实验表明，残差RL控制器在圈速上比基线控制器提高了11.5%，且仅需20分钟的训练时间。

## 📝 摘要（中文）

自主赛车面临独特的挑战，包括非线性动力学、高速行驶以及在动态和不可预测条件下实时决策的关键需求。传统的强化学习方法通常依赖于广泛的基于仿真的预训练，这在向真实环境转移时面临重大挑战。本文提出了一种强大的车载强化学习框架，旨在消除对基于仿真的预训练的依赖，从而实现直接的现实世界适应。该系统引入了一种改进的软演员-评论家（SAC）算法，通过集成多步时间差学习、异步训练管道和启发式延迟奖励调整（HDRA）来增强经典控制器的实时性能，提高样本效率和训练稳定性。通过在F1TENTH赛车平台上的广泛实验验证，该框架的残差RL控制器在基线控制器上表现出色，圈速比最先进技术减少了11.5%，仅需20分钟训练。此外，无基线控制器训练的端到端RL控制器超越了之前的最佳结果，持续在赛道上学习。这些发现使该框架成为高性能自主赛车的强大解决方案，并为其他实时动态自主系统提供了有前景的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决自主赛车中传统强化学习方法在真实环境中迁移效果差的问题，尤其是在高速和动态条件下的实时决策挑战。

**核心思路**：提出一种车载强化学习框架，消除对仿真预训练的依赖，直接在真实环境中进行学习和适应，采用改进的SAC算法以增强控制性能。

**技术框架**：整体架构包括残差RL控制器、异步训练管道和HDRA模块，结合多步时间差学习以提高样本效率和训练稳定性。

**关键创新**：引入残差RL结构和HDRA机制是本文的主要创新，与传统方法相比，能够在不依赖仿真预训练的情况下实现高效的实时学习。

**关键设计**：在算法设计中，采用了多步时间差学习以提升学习效率，异步训练管道以加速训练过程，HDRA用于优化奖励信号，从而提高了训练的稳定性和效果。

## 📊 实验亮点

实验结果显示，残差RL控制器在F1TENTH赛车平台上表现优异，圈速比基线控制器提高了11.5%，且仅需20分钟的训练时间。此外，端到端RL控制器在没有基线控制器的情况下也超越了之前的最佳结果，展现出持续的赛道学习能力。

## 🎯 应用场景

该研究的潜在应用领域包括高性能自主赛车、无人驾驶汽车以及其他需要实时决策的动态系统。其框架能够在复杂环境中快速适应，具有重要的实际价值，未来可能推动更多实时动态系统的开发与应用。

## 📄 摘要（原文）

> Autonomous racing presents unique challenges due to its non-linear dynamics, the high speed involved, and the critical need for real-time decision-making under dynamic and unpredictable conditions. Most traditional Reinforcement Learning (RL) approaches rely on extensive simulation-based pre-training, which faces crucial challenges in transfer effectively to real-world environments. This paper introduces a robust on-board RL framework for autonomous racing, designed to eliminate the dependency on simulation-based pre-training enabling direct real-world adaptation. The proposed system introduces a refined Soft Actor-Critic (SAC) algorithm, leveraging a residual RL structure to enhance classical controllers in real-time by integrating multi-step Temporal-Difference (TD) learning, an asynchronous training pipeline, and Heuristic Delayed Reward Adjustment (HDRA) to improve sample efficiency and training stability. The framework is validated through extensive experiments on the F1TENTH racing platform, where the residual RL controller consistently outperforms the baseline controllers and achieves up to an 11.5 % reduction in lap times compared to the State-of-the-Art (SotA) with only 20 min of training. Additionally, an End-to-End (E2E) RL controller trained without a baseline controller surpasses the previous best results with sustained on-track learning. These findings position the framework as a robust solution for high-performance autonomous racing and a promising direction for other real-time, dynamic autonomous systems.

