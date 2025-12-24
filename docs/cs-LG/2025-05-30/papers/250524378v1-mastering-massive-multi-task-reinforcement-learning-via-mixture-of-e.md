---
layout: default
title: Mastering Massive Multi-Task Reinforcement Learning via Mixture-of-Expert Decision Transformer
---

# Mastering Massive Multi-Task Reinforcement Learning via Mixture-of-Expert Decision Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24378" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24378v1</a>
  <a href="https://arxiv.org/pdf/2505.24378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24378v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24378v1', 'Mastering Massive Multi-Task Reinforcement Learning via Mixture-of-Expert Decision Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yilun Kong, Guozheng Ma, Qi Zhao, Haoyu Wang, Li Shen, Xueqian Wang, Dacheng Tao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30

**备注**: ICML 2025

---

## 💡 一句话要点

**提出M3DT框架以解决大规模多任务强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多任务强化学习` `混合专家` `决策Transformer` `模型可扩展性` `三阶段训练机制`

## 📋 核心要点

1. 现有的多任务强化学习方法在任务数量扩展上存在显著不足，简单增加参数无法有效提升性能。
2. 提出M3DT框架，通过混合专家机制增强模型参数的可扩展性，优化决策Transformer以应对任务负载。
3. 实验结果显示，M3DT在固定任务数量下性能持续提升，并成功扩展到160个任务，表现优越。

## 📝 摘要（中文）

尽管近期离线多任务强化学习（MTRL）在Transformer架构的应用上取得了进展，但大规模任务的扩展仍然是一个巨大挑战。本文首先重新审视任务数量对现有MTRL方法的影响，并指出简单扩展参数不足以应对任务数量增加带来的性能下降。基于此，提出了一种新颖的混合专家（MoE）框架M3DT，通过增强决策Transformer（DT）骨干网络，减少参数子集上的任务负载，并引入三阶段训练机制以实现高效训练。实验结果表明，M3DT在任务数量增加时性能持续提升，成功扩展至160个任务并表现出优越性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多任务强化学习方法在面对大量任务时的性能下降问题。现有方法在任务数量增加时，简单扩展模型参数并未能有效提升性能，导致任务处理能力受限。

**核心思路**：论文提出的M3DT框架通过混合专家（MoE）机制来增强模型的参数可扩展性，旨在减轻每个专家的任务负载，从而提高整体性能。通过优化决策Transformer（DT）骨干网络，M3DT能够更有效地处理多任务场景。

**技术框架**：M3DT的整体架构包括多个专家模块，每个专家负责处理特定的任务子集。此外，论文引入了三阶段训练机制，分别为预训练、微调和最终优化，以确保模型在不同阶段的高效学习。

**关键创新**：M3DT的主要创新在于结合了混合专家机制与决策Transformer，显著提升了模型在大规模任务上的处理能力。这一设计与传统方法的根本区别在于通过专家分工来优化任务处理，而非单一模型的参数扩展。

**关键设计**：在模型设计中，M3DT采用了动态专家选择机制，根据任务需求动态激活不同的专家。此外，损失函数的设计也考虑了任务间的相互影响，以优化整体性能。

## 📊 实验亮点

实验结果表明，M3DT在任务数量增加时性能持续提升，成功扩展至160个任务，较基线方法在相同任务数量下性能提升显著，展示了其卓越的任务可扩展性和处理能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能推荐系统和自动驾驶等多任务场景。M3DT框架能够有效处理大规模任务，提升系统的智能化水平，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Despite recent advancements in offline multi-task reinforcement learning (MTRL) have harnessed the powerful capabilities of the Transformer architecture, most approaches focus on a limited number of tasks, with scaling to extremely massive tasks remaining a formidable challenge. In this paper, we first revisit the key impact of task numbers on current MTRL method, and further reveal that naively expanding the parameters proves insufficient to counteract the performance degradation as the number of tasks escalates. Building upon these insights, we propose M3DT, a novel mixture-of-experts (MoE) framework that tackles task scalability by further unlocking the model's parameter scalability. Specifically, we enhance both the architecture and the optimization of the agent, where we strengthen the Decision Transformer (DT) backbone with MoE to reduce task load on parameter subsets, and introduce a three-stage training mechanism to facilitate efficient training with optimal performance. Experimental results show that, by increasing the number of experts, M3DT not only consistently enhances its performance as model expansion on the fixed task numbers, but also exhibits remarkable task scalability, successfully extending to 160 tasks with superior performance.

