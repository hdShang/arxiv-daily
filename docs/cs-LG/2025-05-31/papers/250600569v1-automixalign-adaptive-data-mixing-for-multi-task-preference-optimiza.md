---
layout: default
title: "AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs"
---

# AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00569" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00569v1</a>
  <a href="https://arxiv.org/pdf/2506.00569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00569v1', 'AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicholas E. Corrado, Julian Katz-Samuels, Adithya Devraj, Hyokun Yun, Chao Zhang, Yi Xu, Yi Pan, Bing Yin, Trishul Chilimbi

**分类**: cs.LG

**发布日期**: 2025-05-31

**备注**: ACL 2025, Main Conference

---

## 💡 一句话要点

**提出AutoMixAlign以解决多任务偏好优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多任务学习` `偏好优化` `自适应数据混合` `大型语言模型` `极小极大优化`

## 📋 核心要点

1. 现有方法在选择训练数据混合时面临高成本和低效的问题，难以在多任务上实现最佳性能。
2. 论文提出的AutoMixAlign算法通过自适应数据混合，优化多任务的偏好表现，采用专家模型与通用模型的结合。
3. 实验结果表明，AMA在多个多任务对齐设置中优于传统的总损失优化方法和模型合并方法。

## 📝 摘要（中文）

在对齐大型语言模型（LLMs）时，其在多项任务（如有用性、无害性和诚实性）上的表现严重依赖于训练数据的组成。然而，选择一个能够在所有任务上都表现良好的数据混合是具有挑战性的。现有方法依赖于大量的消融研究、启发式方法或人类直觉，这些方法往往成本高昂且效果不佳。本文研究了通过DPO进行偏好优化的问题，并提出了AutoMixAlign（AMA），这是一种理论基础的算法，能够在训练过程中自适应地混合数据集，以平衡各任务的表现。AMA首先为每个任务训练“专家模型”，以确定与强任务表现相对应的损失。然后，使用一种新颖的极小极大优化方法训练通用模型，优先考虑通用模型损失与专家模型损失偏差最大的任务。

## 🔬 方法详解

**问题定义**：本文旨在解决在对齐大型语言模型时，如何选择合适的数据混合以优化多任务表现的问题。现有方法依赖于消融研究和启发式方法，成本高且效果不佳。

**核心思路**：论文提出的AutoMixAlign算法通过自适应地混合数据集，平衡各任务的表现。首先训练专家模型以确定各任务的损失，然后通过极小极大优化方法训练通用模型，优先考虑损失偏差较大的任务。

**技术框架**：AMA的整体架构包括两个主要阶段：第一阶段是为每个任务训练专家模型，第二阶段是训练通用模型，采用两种算法（AMA-R和AMA-S）来优化任务优先级和数据采样。

**关键创新**：AMA的创新之处在于其自适应数据混合策略，通过动态调整任务优先级和数据采样，显著提升了多任务的对齐效果。这与传统的总损失优化方法有本质区别。

**关键设计**：AMA-R算法通过自适应重加权目标函数来优先考虑任务，而AMA-S算法则通过调整每个任务的数据采样量来实现优先级优化。两者在凸情况下的收敛速率为O(1/√T)，并且AMA-S的收敛证明使用了在线学习技术，如EXP3。

## 📊 实验亮点

实验结果显示，AutoMixAlign在多个多任务对齐设置中表现优于传统的总损失优化方法，且在模型合并方法上也有显著提升。具体而言，AMA在各任务的表现上均衡性更好，提升幅度明显，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括多任务学习、自然语言处理和智能助手等。通过优化多任务的偏好表现，AutoMixAlign能够提升大型语言模型在实际应用中的可靠性和有效性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> When aligning large language models (LLMs), their performance on various tasks (such as being helpful, harmless, and honest) depends heavily on the composition of their training data. However, selecting a data mixture that achieves strong performance across all tasks is challenging. Existing approaches rely on large ablation studies, heuristics, or human intuition, but these can be prohibitively expensive and suboptimal. We study this problem in the setting of preference optimization via DPO and introduce AutoMixAlign (AMA), a theoretically-grounded algorithm that adaptively mixes datasets during training to balance performance across tasks. AMA first trains \textit{specialist models} for each task to determine losses that correspond to strong task performance. Then, it trains a generalist model using a novel minimax optimization that prioritizes tasks for which generalist model losses deviate most from specialist model losses. To optimize this problem, we propose two algorithms: (1) AMA-R, which adaptively reweights the objective to prioritize tasks, and (2) AMA-S, which adaptively adjusts how much data is sampled from each task to prioritize tasks. Both algorithms achieve a convergence rate of $O(1/\sqrt{T})$ in the convex case. AMA-R's convergence result follows from Sagawa et al. (2019), and we provide a convergence proof for AMA-S using online learning techniques such as EXP3. We evaluate AMA on several multitask alignment setups and find that AMA outperforms the standard alignment approach -- which simply optimizes the total loss across all tasks -- and also outperforms model merging methods.

