---
layout: default
title: "F2RVLM: Boosting Fine-grained Fragment Retrieval for Multi-Modal Long-form Dialogue with Vision Language Model"
---

# F2RVLM: Boosting Fine-grained Fragment Retrieval for Multi-Modal Long-form Dialogue with Vision Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17714" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17714v2</a>
  <a href="https://arxiv.org/pdf/2508.17714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17714v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17714v2', 'F2RVLM: Boosting Fine-grained Fragment Retrieval for Multi-Modal Long-form Dialogue with Vision Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanbo Bi, Zhiqiang Yuan, Zexi Jia, Jiapei Zhang, Chongyang Li, Peixiang Luo, Ying Deng, Xiaoyue Duan, Jinchao Zhang

**分类**: cs.CV

**发布日期**: 2025-08-25 (更新: 2025-11-10)

---

## 💡 一句话要点

**提出F2RVLM以解决多模态长对话中的细粒度片段检索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度检索` `多模态对话` `视觉语言模型` `强化学习` `课程学习` `语义一致性` `长对话理解`

## 📋 核心要点

1. 现有对话检索方法无法有效处理长对话中分散的语义一致内容，导致用户体验不佳。
2. 本文提出F2RVLM模型，通过两阶段训练和多目标奖励机制，增强片段检索的语义一致性和相关性。
3. F2RVLM在多个数据集上超越了现有流行的视觉语言模型，展示了优越的检索性能。

## 📝 摘要（中文）

传统对话检索方法往往无法满足用户在长对话中回访语义一致内容的需求。为此，本文定义了细粒度片段检索（FFR）任务，要求模型从多模态长对话中定位与查询相关的片段，包括发言和图像。我们构建了最长轮次的多模态对话检索数据集MLDR，并提出F2RVLM模型，通过两阶段训练和难度感知课程采样，显著提升了检索性能。

## 🔬 方法详解

**问题定义**：本文旨在解决传统对话检索方法在长对话中无法有效定位语义一致片段的问题。现有方法往往只关注最近的发言或图像，忽视了长对话中信息的分散性和复杂性。

**核心思路**：论文提出细粒度片段检索（FFR）任务，要求模型从多模态对话中提取相关片段。通过引入F2RVLM模型，采用两阶段训练策略，首先进行有监督的微调，然后通过基于GRPO的强化学习优化检索质量。

**技术框架**：F2RVLM的整体架构包括两个主要阶段：第一阶段为有监督微调，注入片段级检索知识；第二阶段为强化学习，使用多目标奖励机制提升语义精确性和上下文一致性。此外，采用难度感知课程采样，逐步引导模型处理更复杂的样本。

**关键创新**：F2RVLM的核心创新在于其两阶段训练方法和难度感知课程采样策略，显著提升了模型在长对话中的推理能力和检索效果。这与现有方法的单一训练方式形成鲜明对比。

**关键设计**：在模型设计中，采用了GRPO强化学习框架，结合多目标奖励函数，优化语义一致性、相关性和上下文连贯性。同时，难度感知课程采样通过模型预测的难度对训练实例进行排序，逐步增加训练难度。

## 📊 实验亮点

F2RVLM在多个数据集上表现出色，在领域内和真实场景中均超越了流行的视觉语言模型，检索性能显著提升，具体表现为在MLDR数据集上检索准确率提高了XX%，在WeChat测试集上表现优于基线模型。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、社交媒体分析和多模态信息检索等。通过提升对话系统在长对话中的检索能力，能够更好地满足用户的需求，提升用户体验，未来可能推动更智能的对话系统的发展。

## 📄 摘要（原文）

> Traditional dialogue retrieval aims to select the most appropriate utterance or image from recent dialogue history. However, they often fail to meet users' actual needs for revisiting semantically coherent content scattered across long-form conversations. To fill this gap, we define the Fine-grained Fragment Retrieval (FFR) task, requiring models to locate query-relevant fragments, comprising both utterances and images, from multimodal long-form dialogues. As a foundation for FFR, we construct MLDR, the longest-turn multimodal dialogue retrieval dataset to date, averaging 25.45 turns per dialogue, with each naturally spanning three distinct topics. To evaluate generalization in real-world scenarios, we curate and annotate a WeChat-based test set comprising real-world multimodal dialogues with an average of 75.38 turns. Building on these resources, we explore existing generation-based Vision-Language Models (VLMs) on FFR and observe that they often retrieve incoherent utterance-image fragments. While optimized for generating responses from visual-textual inputs, these models lack explicit supervision to ensure semantic coherence within retrieved fragments. To this end, we propose F2RVLM, a generative retrieval model trained in a two-stage paradigm: (1) supervised fine-tuning to inject fragment-level retrieval knowledge, and (2) GRPO-based reinforcement learning with multi-objective rewards promoting semantic precision, relevance, and contextual coherence. To handle varying intra-fragment complexity, from locally dense to sparsely distributed, we introduce difficulty-aware curriculum sampling that ranks training instances by model-predicted difficulty and gradually exposes the model to harder samples. This boosts reasoning ability in long, multi-turn contexts. F2RVLM outperforms popular VLMs in both in-domain and real-domain settings, demonstrating superior retrieval performance.

