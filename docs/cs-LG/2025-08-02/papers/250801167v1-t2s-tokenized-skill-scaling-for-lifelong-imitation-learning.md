---
layout: default
title: "T2S: Tokenized Skill Scaling for Lifelong Imitation Learning"
---

# T2S: Tokenized Skill Scaling for Lifelong Imitation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01167" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01167v1</a>
  <a href="https://arxiv.org/pdf/2508.01167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01167v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01167v1', 'T2S: Tokenized Skill Scaling for Lifelong Imitation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongquan Zhang, Jingyu Gong, Zhizhong Zhang, Xin Tan, Yanyun Qu, Yuan Xie

**分类**: cs.LG, cs.RO

**发布日期**: 2025-08-02

---

## 💡 一句话要点

**提出T2S框架以解决终身模仿学习中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `终身学习` `模仿学习` `灾难性遗忘` `技能扩展` `知识转移` `变换器` `参数标记化`

## 📋 核心要点

1. 现有的终身模仿学习方法通常孤立处理灾难性遗忘与新技能获取，未能有效平衡这两者。
2. 论文提出的T2S框架通过标记化模型参数，实现输入与可学习标记之间的交叉注意力，增强模型的可扩展性。
3. 实验结果显示，T2S在三组LIBERO任务中平均实现1.0%的灾难性遗忘率，且新技能扩展仅需8.0%的可训练标记。

## 📝 摘要（中文）

终身模仿学习的主要挑战在于平衡减轻先前技能的灾难性遗忘与保持获取新技能的能力。然而，现有方法通常孤立地处理这些方面，忽视了它们在终身技能获取中的内在关联。我们提出了一种统一框架，称为Tokenized Skill Scaling (T2S)。通过对模型参数进行标记化，传统变换器的线性参数映射被转化为输入与可学习标记之间的交叉注意力，从而通过轻松扩展新标记来增强模型的可扩展性。此外，我们引入了语言引导的技能扩展，以高效地在任务间转移知识，避免参数线性增长。大量实验表明，T2S有效防止灾难性遗忘，新的技能扩展仅需最小的可训练参数，并实现任务间的高效知识转移。

## 🔬 方法详解

**问题定义**：本论文旨在解决终身模仿学习中的灾难性遗忘问题，现有方法往往无法有效平衡对旧技能的保持与新技能的学习，导致性能下降。

**核心思路**：提出Tokenized Skill Scaling (T2S)框架，通过标记化模型参数，利用交叉注意力机制增强模型的可扩展性，从而在学习新技能时有效保留旧技能。

**技术框架**：T2S框架包括两个主要模块：标记化参数模块和语言引导技能扩展模块。前者通过交叉注意力实现输入与可学习标记的关联，后者则通过语言信息促进任务间的知识转移。

**关键创新**：T2S的核心创新在于将传统的线性参数映射转化为交叉注意力机制，这一设计使得模型在扩展新技能时无需线性增加参数，显著提高了模型的灵活性和效率。

**关键设计**：在参数设置上，T2S仅需8.0%的可训练标记，损失函数采用多任务学习策略，网络结构基于变换器架构，优化了模型的训练效率和性能。

## 📊 实验亮点

实验结果表明，T2S在三组LIBERO任务中实现了平均1.0%的灾难性遗忘率，且新技能扩展仅需8.0%的可训练标记，任务间知识转移效率高达77.7%。这些结果显示了T2S在终身模仿学习中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人学习、自动驾驶、智能助手等需要长期学习和适应新环境的场景。通过有效的知识转移和技能扩展，T2S可以显著提升智能体在复杂任务中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> The main challenge in lifelong imitation learning lies in the balance between mitigating catastrophic forgetting of previous skills while maintaining sufficient capacity for acquiring new ones. However, current approaches typically address these aspects in isolation, overlooking their internal correlation in lifelong skill acquisition. We address this limitation with a unified framework named Tokenized Skill Scaling (T2S). Specifically, by tokenizing the model parameters, the linear parameter mapping of the traditional transformer is transformed into cross-attention between input and learnable tokens, thereby enhancing model scalability through the easy extension of new tokens. Additionally, we introduce language-guided skill scaling to transfer knowledge across tasks efficiently and avoid linearly growing parameters. Extensive experiments across diverse tasks demonstrate that T2S: 1) effectively prevents catastrophic forgetting (achieving an average NBT of 1.0% across the three LIBERO task suites), 2) excels in new skill scaling with minimal increases in trainable parameters (needing only 8.0% trainable tokens in an average of lifelong tasks), and 3) enables efficient knowledge transfer between tasks (achieving an average FWT of 77.7% across the three LIBERO task suites), offering a promising solution for lifelong imitation learning.

