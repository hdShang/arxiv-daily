---
layout: default
title: "NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks"
---

# NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02046" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02046v2</a>
  <a href="https://arxiv.org/pdf/2508.02046.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02046v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02046v2', 'NaviMaster: Learning a Unified Policy for GUI and Embodied Navigation Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Luo, Wentao Yan, Jingyu Gong, Min Wang, Zhizhong Zhang, Xuhong Wang, Yuan Xie, Xin Tan

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-04 (更新: 2025-10-11)

**备注**: Homepage: https://iron-boyy.github.io/navimaster/

---

## 💡 一句话要点

**提出NaviMaster以统一GUI与实体导航任务**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图形用户界面` `实体导航` `马尔可夫决策过程` `强化学习` `多任务学习`

## 📋 核心要点

1. 现有的GUI和实体导航任务在数据集和训练方法上存在显著差异，导致两者无法有效结合。
2. NaviMaster通过将这两项任务统一为马尔可夫决策过程，提出了一种新的视觉目标轨迹收集管道和统一的强化学习框架。
3. 实验结果表明，NaviMaster在多个任务上均优于现有最先进的智能体，验证了其统一训练策略和奖励设计的有效性。

## 📝 摘要（中文）

近年来，图形用户界面（GUI）和实体导航的进展显著，但这两个领域的发展大多是孤立的，数据集和训练范式各异。本文观察到这两项任务均可被表述为马尔可夫决策过程（MDP），从而为其统一提供了基础原则。因此，我们提出了NaviMaster，这是第一个能够在单一框架内统一GUI导航和实体导航的智能体。具体而言，NaviMaster (i) 提出了一个视觉目标轨迹收集管道，使用单一公式为GUI和实体任务生成轨迹；(ii) 在混合数据上采用统一的强化学习框架以提高泛化能力；(iii) 设计了一种新颖的距离感知奖励，以确保从轨迹中高效学习。通过在域外基准上的广泛实验，NaviMaster在GUI导航、空间可用性预测和实体导航方面均超越了现有最先进的智能体。

## 🔬 方法详解

**问题定义**：本文旨在解决GUI和实体导航任务之间的孤立发展问题，现有方法在数据集和训练范式上存在差异，限制了其性能的提升。

**核心思路**：NaviMaster通过将GUI和实体导航任务统一为马尔可夫决策过程，利用单一的轨迹收集管道和统一的强化学习框架来提升任务间的协同学习能力。

**技术框架**：NaviMaster的整体架构包括三个主要模块：视觉目标轨迹收集管道、统一的强化学习框架和距离感知奖励设计。该框架通过混合数据进行训练，以提高模型的泛化能力。

**关键创新**：NaviMaster的核心创新在于首次将GUI和实体导航任务统一在一个框架内，采用单一的轨迹生成方法和统一的学习策略，显著提升了任务间的协同效果。

**关键设计**：在设计中，NaviMaster使用了距离感知奖励机制，以确保从生成的轨迹中高效学习，同时在强化学习过程中采用了混合数据策略，以增强模型的泛化能力。

## 📊 实验亮点

在实验中，NaviMaster在GUI导航、空间可用性预测和实体导航任务上均超越了现有最先进的智能体，特别是在GUI导航任务中，性能提升幅度达到XX%，显示出其在多任务学习中的优势。

## 🎯 应用场景

NaviMaster的研究成果具有广泛的应用潜力，尤其在智能助手、机器人导航和人机交互等领域。通过统一的导航策略，NaviMaster能够提升智能体在复杂环境中的适应能力，推动相关技术的进步与应用。未来，该方法可能会影响多模态学习和自主系统的发展方向。

## 📄 摘要（原文）

> Recent advances in Graphical User Interface (GUI) and embodied navigation have driven progress, yet these domains have largely evolved in isolation, with disparate datasets and training paradigms. In this paper, we observe that both tasks can be formulated as Markov Decision Processes (MDP), suggesting a foundational principle for their unification. Hence, we present NaviMaster, the first unified agent capable of unifying GUI navigation and embodied navigation within a single framework. Specifically, NaviMaster (i) proposes a visual-target trajectory collection pipeline that generates trajectories for both GUI and embodied tasks using a single formulation. (ii) employs a unified reinforcement learning framework on the mix data to improve generalization. (iii) designs a novel distance-aware reward to ensure efficient learning from the trajectories. Through extensive experiments on out-of-domain benchmarks, NaviMaster is shown to outperform state-of-the-art agents in GUI navigation, spatial affordance prediction, and embodied navigation. Ablation studies further demonstrate the efficacy of our unified training strategy, data mixing strategy, and reward design.

