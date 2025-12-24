---
layout: default
title: "LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model"
---

# LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00676" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00676v1</a>
  <a href="https://arxiv.org/pdf/2509.00676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00676v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00676v1', 'LLaVA-Critic-R1: Your Critic Model is Secretly a Strong Policy Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiyao Wang, Chunyuan Li, Jianwei Yang, Kai Zhang, Bo Liu, Tianyi Xiong, Furong Huang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出LLaVA-Critic-R1以优化多模态生成与评估**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生成` `视觉语言建模` `强化学习` `评论模型` `自我评论` `推理任务`

## 📋 核心要点

1. 现有的评论模型与生成模型之间存在明显的分离，限制了评论模型的直接应用。
2. 本文提出将评论数据集重组为可验证信号，并在基础生成模型上进行强化学习，形成LLaVA-Critic-R1。
3. LLaVA-Critic-R1在多个视觉推理基准上表现出色，平均提升5.7%，并在推理时通过自我评论进一步提高性能。

## 📝 摘要（中文）

在视觉语言建模中，评论模型通常用于评估输出，而非生成响应。本文挑战这一传统，提出将偏好标记的评论数据集重组为可验证的训练信号，并直接在基础生成模型上进行强化学习，生成LLaVA-Critic-R1。该模型不仅在评论任务中表现优异，还在26个视觉推理基准上与专门的推理模型相媲美，平均提升5.7%。进一步扩展至现有强推理模型，LLaVA-Critic-R1+在不牺牲评论质量的情况下，达到了71.9的SoTA性能。此外，增强的评论能力在推理时也带来了显著提升，平均提高13.8%。

## 🔬 方法详解

**问题定义**：现有的评论模型通常仅用于评估输出，缺乏生成能力，导致其在实际应用中的局限性。

**核心思路**：本文通过将偏好标记的评论数据集重组为可验证的训练信号，直接在基础生成模型上进行强化学习，旨在实现评论与生成能力的统一。

**技术框架**：整体架构包括数据集重组、强化学习训练和生成模型优化三个主要模块。首先重组评论数据集，然后通过强化学习优化生成模型，最后实现多模态生成与评估的统一。

**关键创新**：LLaVA-Critic-R1不仅作为高效的评论模型，还展现出强大的生成能力，与传统的评论与生成模型分离的做法形成鲜明对比。

**关键设计**：在训练过程中，采用了特定的损失函数来优化评论质量，并调整了网络结构以增强生成能力，确保模型在推理任务中的表现。

## 📊 实验亮点

LLaVA-Critic-R1在26个视觉推理基准上表现优异，平均提升5.7%，并在现有强推理模型基础上进一步优化，LLaVA-Critic-R1+达到了71.9的SoTA性能。此外，应用自我评论在推理时平均提高了13.8%的性能，显示出显著的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动内容生成和多模态交互系统。通过优化评论与生成的统一模型，可以提升人机交互的自然性和智能化水平，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In vision-language modeling, critic models are typically trained to evaluate outputs -- assigning scalar scores or pairwise preferences -- rather than to generate responses. This separation from policy models, which produce the responses, is so entrenched that critics are rarely considered for direct policy use. In this work, we challenge this convention. We propose to reorganize preference-labeled critic datasets into verifiable training signals and perform reinforcement learning directly on a base generative model, producing LLaVA-Critic-R1, a multimodal critic trained to optimize preference judgments while retaining full generation ability. Surprisingly, LLaVA-Critic-R1 emerges not only as a top-performing critic but also as a competitive policy model -- matching or surpassing specialized reasoning VLMs trained with in-domain data across 26 visual reasoning and understanding benchmarks, with an average gain of +5.7% over its base model (Qwen-2.5-VL-7B). Extending this approach to existing strong reasoning VLMs yields LLaVA-Critic-R1+, which further advances policy performance without sacrificing critic quality, achieving a SoTA performance of 71.9 on MMMU at the 7B scale. Finally, we show that the enhanced critic ability benefits inference: applying self-critique at test time yields an average +13.8% improvement on five representative reasoning tasks without additional training. Our results reveal that RL training on critic data can produce a unified model excelling at both evaluation and generation, offering a simple path toward scalable, self-improving multimodal systems.

