---
layout: default
title: "GRAM-R$^2$: Self-Training Generative Foundation Reward Models for Reward Reasoning"
---

# GRAM-R$^2$: Self-Training Generative Foundation Reward Models for Reward Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02492" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02492v3</a>
  <a href="https://arxiv.org/pdf/2509.02492.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02492v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02492v3', 'GRAM-R$^2$: Self-Training Generative Foundation Reward Models for Reward Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenglong Wang, Yongyu Mu, Hang Zhou, Yifu Huo, Ziming Zhu, Jiali Zeng, Murun Yang, Bei Li, Xiaoyang Hao, Chunliang Zhang, Fandong Meng, Jingbo Zhu, Tong Xiao

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-02 (更新: 2025-11-16)

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出GRAM-R$^2$，通过自训练生成式奖励模型实现奖励推理，提升任务泛化性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `奖励推理` `自训练` `生成式模型` `Transformer` `人机反馈强化学习` `响应排序`

## 📋 核心要点

1. 现有奖励模型严重依赖大规模标注偏好数据，成本高昂且泛化性受限。
2. 提出GRAM-R$^2$，通过自训练生成式奖励模型，利用未标注数据进行奖励推理。
3. 实验表明，GRAM-R$^2$在响应排序、任务适应和人机反馈强化学习中表现出色。

## 📝 摘要（中文）

近年来，奖励建模的显著进展得益于从任务特定设计向通用奖励模型的范式转变。尽管如此，开发有效的奖励模型仍然是一个根本性的挑战：严重依赖大规模标注的偏好数据。在大量未标注数据上进行预训练提供了一个有希望的方向，但现有方法未能将显式推理融入奖励模型。为了弥合这一差距，我们提出了一种自训练方法，该方法利用未标注数据来激发奖励模型中的奖励推理。基于此，我们开发了GRAM-R$^2$，一个生成式奖励模型，经过训练不仅可以生成偏好标签，还可以生成伴随的奖励理由。GRAM-R$^2$可以作为奖励推理的基础模型，并可以应用于各种任务，只需极少或无需额外的微调。它可以支持下游应用，如响应排序和任务特定奖励调整。在响应排序、任务适应和基于人类反馈的强化学习方面的实验表明，GRAM-R$^2$始终提供强大的性能，优于几个强大的判别式和生成式基线。

## 🔬 方法详解

**问题定义**：现有奖励模型依赖大量人工标注的偏好数据，获取成本高昂，且模型难以泛化到新的任务和场景。缺乏显式的推理能力，使得模型难以理解奖励背后的原因，限制了其应用范围。

**核心思路**：利用未标注数据进行自训练，通过生成奖励理由来增强奖励模型的推理能力。核心思想是让模型不仅预测偏好标签，还要解释为什么做出这样的偏好选择，从而学习到更深层次的奖励机制。

**技术框架**：GRAM-R$^2$是一个生成式奖励模型，其训练过程包含以下几个主要阶段：1) 使用未标注数据进行预训练，模型学习生成偏好标签和对应的奖励理由；2) 使用少量标注数据进行微调，进一步提升模型在特定任务上的性能；3) 将训练好的模型应用于下游任务，如响应排序和任务特定奖励调整。

**关键创新**：主要创新在于引入了奖励理由生成机制，使得模型能够进行显式的奖励推理。与传统的判别式奖励模型相比，GRAM-R$^2$能够更好地理解奖励背后的原因，从而具有更强的泛化能力和可解释性。与现有的生成式奖励模型相比，GRAM-R$^2$更加注重奖励推理能力的培养。

**关键设计**：GRAM-R$^2$采用Transformer架构，使用交叉熵损失函数来训练模型生成偏好标签和奖励理由。在训练过程中，采用了多种技巧来提高模型的稳定性和性能，例如，使用teacher forcing来加速训练，使用beam search来生成高质量的奖励理由。奖励理由的长度和内容也经过精心设计，以确保其能够有效地表达奖励背后的原因。

## 📊 实验亮点

实验结果表明，GRAM-R$^2$在响应排序、任务适应和基于人类反馈的强化学习等任务上均取得了显著的性能提升。例如，在响应排序任务上，GRAM-R$^2$的性能优于多个强大的判别式和生成式基线。在任务适应任务上，GRAM-R$^2$仅需少量微调即可达到与专门训练的模型相媲美的性能。

## 🎯 应用场景

GRAM-R$^2$可广泛应用于对话系统、推荐系统、机器人控制等领域。通过学习人类的偏好和奖励机制，可以提升系统的智能化水平和用户体验。例如，在对话系统中，可以利用GRAM-R$^2$来评估不同回复的质量，选择最符合用户意图的回复。在机器人控制中，可以利用GRAM-R$^2$来学习人类的驾驶习惯，从而实现自动驾驶。

## 📄 摘要（原文）

> Significant progress in reward modeling over recent years has been driven by a paradigm shift from task-specific designs towards generalist reward models. Despite this trend, developing effective reward models remains a fundamental challenge: the heavy reliance on large-scale labeled preference data. Pre-training on abundant unlabeled data offers a promising direction, but existing approaches fall short of instilling explicit reasoning into reward models. To bridge this gap, we propose a self-training approach that leverages unlabeled data to elicit reward reasoning in reward models. Based on this approach, we develop GRAM-R$^2$, a generative reward model trained to produce not only preference labels but also accompanying reward rationales. GRAM-R$^2$ can serve as a foundation model for reward reasoning and can be applied to a wide range of tasks with minimal or no additional fine-tuning. It can support downstream applications such as response ranking and task-specific reward tuning. Experiments on response ranking, task adaptation, and reinforcement learning from human feedback demonstrate that GRAM-R$^2$ consistently delivers strong performance, outperforming several strong discriminative and generative baselines.

