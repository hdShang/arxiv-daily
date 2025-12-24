---
layout: default
title: Scaling Multi Agent Reinforcement Learning for Underwater Acoustic Tracking via Autonomous Vehicles
---

# Scaling Multi Agent Reinforcement Learning for Underwater Acoustic Tracking via Autonomous Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08222" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08222v2</a>
  <a href="https://arxiv.org/pdf/2505.08222.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08222v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08222v2', 'Scaling Multi Agent Reinforcement Learning for Underwater Acoustic Tracking via Autonomous Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Matteo Gallici, Ivan Masmitja, Mario Martín

**分类**: cs.RO, cs.AI, cs.DC, cs.PF

**发布日期**: 2025-05-13 (更新: 2025-10-17)

---

## 💡 一句话要点

**提出迭代蒸馏方法以解决水下声学跟踪中的多智能体强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `水下声学跟踪` `自主车辆` `蒸馏训练` `GPU加速` `Transformer架构` `样本效率` `海洋任务`

## 📋 核心要点

1. 现有的多智能体强化学习方法在处理快速、不确定运动的多目标跟踪时面临显著的计算挑战，样本效率低下。
2. 本文提出了一种迭代蒸馏方法，将高保真模拟转移到简化的GPU加速环境中，显著提高训练速度和效率。
3. 实验结果表明，所提方法在Gazebo中实现了高达30,000倍的速度提升，跟踪误差保持在5米以下，表现出色。

## 📝 摘要（中文）

自主车辆（AV）为水下跟踪等科学任务提供了一种经济有效的解决方案。近年来，强化学习（RL）已成为控制AV在复杂海洋环境中的强大方法。然而，将这些技术扩展到舰队以实现多目标跟踪或快速、不确定运动的目标面临重大计算挑战。多智能体强化学习（MARL）通常样本效率低，而高保真模拟器如Gazebo的LRAUV在单机器人模拟中提供100倍的实时速度提升，但在多车辆场景中并未显著加速，导致MARL训练不切实际。为了解决这些限制，本文提出了一种迭代蒸馏方法，将高保真模拟转移到简化的GPU加速环境中，同时保持高层次动态。这种方法通过并行化实现了高达30,000倍的速度提升，使得通过端到端GPU加速进行高效训练成为可能。此外，我们引入了一种新颖的基于Transformer的架构（TransfMAPPO），能够学习与智能体和目标数量无关的多智能体策略，显著提高样本效率。经过在GPU上进行的大规模课程学习，我们在Gazebo中进行了广泛评估，证明该方法在多个快速移动目标的情况下，跟踪误差保持在5米以下，持续时间较长。此项工作弥合了大规模MARL训练与高保真部署之间的差距，为现实海洋任务中的自主舰队控制提供了可扩展框架。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体强化学习在水下声学跟踪中的计算效率问题。现有方法在多车辆场景中训练效率低，难以满足实际应用需求。

**核心思路**：提出了一种迭代蒸馏方法，将高保真模拟转化为简化的GPU加速环境，以保持动态特性并提高训练速度。

**技术框架**：整体架构包括高保真模拟器的使用、蒸馏过程的设计以及基于Transformer的多智能体策略学习模块。通过并行化处理，显著提升训练效率。

**关键创新**：最重要的创新在于提出的TransfMAPPO架构，能够学习与智能体数量无关的策略，显著提高样本效率，解决了传统MARL方法的样本效率低下问题。

**关键设计**：在设计中，采用了GPU加速的简化环境，设置了适当的损失函数以优化策略学习，同时确保高层次动态的保留。

## 📊 实验亮点

实验结果显示，所提方法在Gazebo中实现了高达30,000倍的速度提升，相较于传统方法，跟踪误差保持在5米以下，表现出色，尤其在多个快速移动目标的情况下，展现了良好的稳定性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括水下探测、海洋科学研究及环境监测等。通过提高多智能体系统的训练效率，能够在复杂的海洋环境中实现更高效的自主控制，推动相关领域的技术进步和实际应用。

## 📄 摘要（原文）

> Autonomous vehicles (AV) offer a cost-effective solution for scientific missions such as underwater tracking. Recently, reinforcement learning (RL) has emerged as a powerful method for controlling AVs in complex marine environments. However, scaling these techniques to a fleet--essential for multi-target tracking or targets with rapid, unpredictable motion--presents significant computational challenges. Multi-Agent Reinforcement Learning (MARL) is notoriously sample-inefficient, and while high-fidelity simulators like Gazebo's LRAUV provide 100x faster-than-real-time single-robot simulations, they offer no significant speedup for multi-vehicle scenarios, making MARL training impractical. To address these limitations, we propose an iterative distillation method that transfers high-fidelity simulations into a simplified, GPU-accelerated environment while preserving high-level dynamics. This approach achieves up to a 30,000x speedup over Gazebo through parallelization, enabling efficient training via end-to-end GPU acceleration. Additionally, we introduce a novel Transformer-based architecture (TransfMAPPO) that learns multi-agent policies invariant to the number of agents and targets, significantly improving sample efficiency. Following large-scale curriculum learning conducted entirely on GPU, we perform extensive evaluations in Gazebo, demonstrating that our method maintains tracking errors below 5 meters over extended durations, even in the presence of multiple fast-moving targets. This work bridges the gap between large-scale MARL training and high-fidelity deployment, providing a scalable framework for autonomous fleet control in real-world sea missions.

