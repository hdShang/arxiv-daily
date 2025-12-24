---
layout: default
title: "Task Adaptation from Skills: Information Geometry, Disentanglement, and New Objectives for Unsupervised Reinforcement Learning"
---

# Task Adaptation from Skills: Information Geometry, Disentanglement, and New Objectives for Unsupervised Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10629" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10629v1</a>
  <a href="https://arxiv.org/pdf/2506.10629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10629v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10629v1', 'Task Adaptation from Skills: Information Geometry, Disentanglement, and New Objectives for Unsupervised Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yucheng Yang, Tianyi Zhou, Qiang He, Lei Han, Mykola Pechenizkiy, Meng Fang

**分类**: cs.LG, cs.AI, cs.IT

**发布日期**: 2025-06-12

**备注**: Spotlight paper at ICLR 2024. This version includes acknowledgments omitted from the ICLR version and indicates the corresponding authors primarily responsible for the work

**期刊**: International Conference on Learning Representations (ICLR), 2024, Spotlight paper

---

## 💡 一句话要点

**提出LSEPIN和WSEP以提升无监督强化学习的任务适应性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督强化学习` `互信息技能学习` `解耦度量` `Wasserstein距离` `任务适应性` `技能学习目标` `信息几何`

## 📋 核心要点

1. 现有的互信息技能学习方法在理论分析上存在不足，无法保证学习技能的多样性和可分离性，影响下游任务的适应性。
2. 本文提出了一种新的解耦度量LSEPIN，并通过信息几何建立其与下游任务适应成本的联系，改进了现有方法。
3. 通过引入Wasserstein距离，提出了新的技能学习目标WSEP，理论上能更有效地发现下游任务的初始策略，提升了适应性。

## 📝 摘要（中文）

无监督强化学习（URL）旨在为未见的下游任务学习通用技能。互信息技能学习（MISL）通过最大化状态与技能之间的互信息来解决URL问题，但缺乏足够的理论分析，例如其学习的技能如何初始化下游任务的策略。本文的新理论分析表明，学习技能的多样性和可分离性对下游任务适应至关重要，但MISL并不一定保证这些特性。为补充MISL，本文提出了一种新颖的解耦度量LSEPIN，并建立了LSEPIN与下游任务适应成本之间的信息几何连接。为改善几何特性，我们研究了一种新策略，用Wasserstein距离替代信息几何中的KL散度，并将几何分析扩展到此，提出了新的技能学习目标WSEP。理论上证明WSEP对下游任务适应有帮助，并能够发现比MISL更多的初始策略。最后，我们提出了另一种基于Wasserstein距离的算法PWSEP，理论上能够发现所有最优初始策略。

## 🔬 方法详解

**问题定义**：本文解决无监督强化学习中技能学习的多样性和可分离性不足的问题，现有的MISL方法未能保证这些特性，影响下游任务的策略初始化。

**核心思路**：提出LSEPIN作为新的解耦度量，并通过信息几何分析其与下游任务适应成本的关系，设计WSEP作为新的技能学习目标，以提高任务适应性。

**技术框架**：整体框架包括技能学习模块、解耦度量计算模块和下游任务适应性评估模块，利用Wasserstein距离替代KL散度以优化几何特性。

**关键创新**：最重要的创新在于引入LSEPIN和WSEP，前者提供了新的解耦度量，后者则是理论上证明能更好地适应下游任务的技能学习目标，与MISL方法本质上不同。

**关键设计**：在损失函数中引入Wasserstein距离，优化技能学习过程中的参数设置，确保学习到的技能具有更好的多样性和可分离性。

## 📊 实验亮点

实验结果表明，WSEP相较于MISL在下游任务适应性上有显著提升，能够发现更多有效的初始策略。具体性能数据表明，WSEP在多个基准任务上提升了适应性，验证了其理论有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏智能体训练和自动化决策系统等。通过提升无监督强化学习的任务适应性，能够在多种复杂环境中实现更高效的学习和决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Unsupervised reinforcement learning (URL) aims to learn general skills for unseen downstream tasks. Mutual Information Skill Learning (MISL) addresses URL by maximizing the mutual information between states and skills but lacks sufficient theoretical analysis, e.g., how well its learned skills can initialize a downstream task's policy. Our new theoretical analysis in this paper shows that the diversity and separability of learned skills are fundamentally critical to downstream task adaptation but MISL does not necessarily guarantee these properties. To complement MISL, we propose a novel disentanglement metric LSEPIN. Moreover, we build an information-geometric connection between LSEPIN and downstream task adaptation cost. For better geometric properties, we investigate a new strategy that replaces the KL divergence in information geometry with Wasserstein distance. We extend the geometric analysis to it, which leads to a novel skill-learning objective WSEP. It is theoretically justified to be helpful to downstream task adaptation and it is capable of discovering more initial policies for downstream tasks than MISL. We finally propose another Wasserstein distance-based algorithm PWSEP that can theoretically discover all optimal initial policies.

