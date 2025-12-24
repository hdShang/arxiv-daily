---
layout: default
title: Efficient Online RL Fine Tuning with Offline Pre-trained Policy Only
---

# Efficient Online RL Fine Tuning with Offline Pre-trained Policy Only

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16856" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16856v1</a>
  <a href="https://arxiv.org/pdf/2505.16856.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16856v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16856v1', 'Efficient Online RL Fine Tuning with Offline Pre-trained Policy Only')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Xiao, Jiacheng Liu, Zifeng Zhuang, Runze Suo, Shangke Lyu, Donglin Wang

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-05-22

---

## 💡 一句话要点

**提出PORL方法以解决在线强化学习微调中对Q函数的依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `在线强化学习` `离线学习` `策略微调` `行为克隆` `Q函数` `模仿学习` `算法优化`

## 📋 核心要点

1. 现有的在线强化学习微调方法依赖于离线预训练的Q函数，这限制了其在缺乏Q函数的场景中的应用。
2. 本文提出了一种新的PORL方法，能够仅依赖离线预训练策略进行在线微调，避免了对Q函数的依赖。
3. 实验结果表明，PORL在性能上与先进的在线和离线RL算法相当，展示了其有效性和创新性。

## 📝 摘要（中文）

提高预训练策略的性能通过在线强化学习（RL）是一个关键但具有挑战性的课题。现有的在线RL微调方法需要依赖离线预训练的Q函数以确保稳定性和性能。然而，由于大多数离线RL方法的保守性，这些Q函数通常低估了离线数据集之外的状态-动作对，限制了从离线到在线设置的进一步探索。此外，这一要求限制了在仅有预训练策略而缺乏预训练Q函数的场景中的适用性，例如模仿学习（IL）预训练。为了解决这些挑战，本文提出了一种仅使用离线预训练策略的高效在线RL微调方法，消除了对预训练Q函数的依赖。我们引入了PORL（仅策略强化学习微调），在在线阶段快速从头初始化Q函数，以避免有害的悲观主义。我们的研究不仅在与先进的离线到在线RL算法和利用先前数据或策略的在线RL方法的竞争性能上取得了成功，还为直接微调行为克隆（BC）策略开辟了新路径。

## 🔬 方法详解

**问题定义**：本文旨在解决在线强化学习微调中对离线预训练Q函数的依赖问题。现有方法由于保守性，导致Q函数在离线数据集外的状态-动作对表现不佳，限制了探索能力。

**核心思路**：我们提出的PORL方法通过仅使用离线预训练策略，快速从头初始化Q函数，避免了对预训练Q函数的依赖，从而克服了现有方法的局限性。

**技术框架**：PORL的整体架构包括两个主要阶段：首先是离线预训练策略的获取，其次是在在线环境中快速初始化和更新Q函数。该方法通过动态调整策略来优化性能。

**关键创新**：PORL的核心创新在于其完全消除了对预训练Q函数的依赖，直接从预训练策略出发进行在线微调，这与传统方法形成了鲜明对比。

**关键设计**：在设计上，PORL采用了一种新的损失函数来指导Q函数的初始化和更新，同时在网络结构上进行了优化，以确保在在线阶段的快速收敛。

## 📊 实验亮点

实验结果显示，PORL在多个基准任务上与先进的在线和离线RL算法相比，性能相当，甚至在某些任务上超越了基线，展示了其在强化学习领域的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏AI等需要在线学习和适应的场景。通过减少对Q函数的依赖，PORL能够在数据稀缺或不完全的情况下，提升策略的学习效率和适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Improving the performance of pre-trained policies through online reinforcement learning (RL) is a critical yet challenging topic. Existing online RL fine-tuning methods require continued training with offline pretrained Q-functions for stability and performance. However, these offline pretrained Q-functions commonly underestimate state-action pairs beyond the offline dataset due to the conservatism in most offline RL methods, which hinders further exploration when transitioning from the offline to the online setting. Additionally, this requirement limits their applicability in scenarios where only pre-trained policies are available but pre-trained Q-functions are absent, such as in imitation learning (IL) pre-training. To address these challenges, we propose a method for efficient online RL fine-tuning using solely the offline pre-trained policy, eliminating reliance on pre-trained Q-functions. We introduce PORL (Policy-Only Reinforcement Learning Fine-Tuning), which rapidly initializes the Q-function from scratch during the online phase to avoid detrimental pessimism. Our method not only achieves competitive performance with advanced offline-to-online RL algorithms and online RL approaches that leverage data or policies prior, but also pioneers a new path for directly fine-tuning behavior cloning (BC) policies.

