---
layout: default
title: "EgoPrompt: Prompt Learning for Egocentric Action Recognition"
---

# EgoPrompt: Prompt Learning for Egocentric Action Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03266" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03266v2</a>
  <a href="https://arxiv.org/pdf/2508.03266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03266v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03266v2', 'EgoPrompt: Prompt Learning for Egocentric Action Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaihai Lyu, Chaofan Chen, Yuheng Ji, Changsheng Xu

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-08-07)

---

## 💡 一句话要点

**提出EgoPrompt以解决第一人称动作识别中的语义关系问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `第一人称动作识别` `提示学习` `语义关系` `跨成分交互` `增强现实` `虚拟现实` `深度学习`

## 📋 核心要点

1. 现有方法将动词和名词成分视为独立任务，忽略了它们的语义关系，导致表示碎片化和泛化能力不足。
2. EgoPrompt框架通过构建统一的提示池，促进动词和名词成分之间的交互，从而提升识别性能。
3. 在Ego4D、EPIC-Kitchens和EGTEA数据集上的实验表明，EgoPrompt在各项基准测试中均表现出色，达到了最先进的性能。

## 📝 摘要（中文）

随着增强现实和虚拟现实应用需求的增加，第一人称动作识别成为一个重要的研究领域。该任务通常分为两个子任务：识别行为（动词成分）和识别被作用的对象（名词成分）。然而，现有方法将这两个成分视为独立的分类任务，忽视了它们之间的语义和上下文关系，导致表示的碎片化和泛化能力不足。为了解决这些挑战，本文提出了一种基于提示学习的框架EgoPrompt，通过构建统一的提示池空间来促进两种成分表示之间的交互。实验结果表明，EgoPrompt在多个数据集上均实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决第一人称动作识别中动词和名词成分之间的语义关系不足的问题。现有方法通常将这两者视为独立的分类任务，导致信息的碎片化和泛化能力的下降。

**核心思路**：EgoPrompt通过构建统一的提示池，捕捉成分特定知识，并促进动词和名词成分之间的交互，从而增强整体识别性能。

**技术框架**：EgoPrompt的整体架构包括两个主要模块：首先，将动词和名词成分的表示分解为细粒度模式；其次，通过基于注意力的机制融合这些模式，以实现跨成分的交互。

**关键创新**：本文的主要创新在于引入了统一的提示池空间和多样化池标准，确保提示池的信息量丰富，从而提升了模型的表现。

**关键设计**：在训练过程中，采用了提示选择频率正则化和提示知识正交化的损失函数设计，以确保提示池的多样性和有效性。

## 📊 实验亮点

EgoPrompt在Ego4D、EPIC-Kitchens和EGTEA数据集上均取得了最先进的性能，尤其在跨数据集和基础到新颖的泛化基准测试中，表现出显著的提升，验证了其有效性和优越性。

## 🎯 应用场景

EgoPrompt的研究成果在增强现实和虚拟现实等领域具有广泛的应用潜力，能够提升人机交互的智能化水平。通过更准确的动作识别，相关应用可以实现更自然的用户体验，推动智能设备的进一步发展。

## 📄 摘要（原文）

> Driven by the increasing demand for applications in augmented and virtual reality, egocentric action recognition has emerged as a prominent research area. It is typically divided into two subtasks: recognizing the performed behavior (i.e., verb component) and identifying the objects being acted upon (i.e., noun component) from the first-person perspective. However, most existing approaches treat these two components as independent classification tasks, focusing on extracting component-specific knowledge while overlooking their inherent semantic and contextual relationships, leading to fragmented representations and sub-optimal generalization capability. To address these challenges, we propose a prompt learning-based framework, EgoPrompt, to conduct the egocentric action recognition task. Building on the existing prompting strategy to capture the component-specific knowledge, we construct a Unified Prompt Pool space to establish interaction between the two types of component representations. Specifically, the component representations (from verbs and nouns) are first decomposed into fine-grained patterns with the prompt pair form. Then, these pattern-level representations are fused through an attention-based mechanism to facilitate cross-component interaction. To ensure the prompt pool is informative, we further introduce a novel training objective, Diverse Pool Criteria. This objective realizes our goals from two perspectives: Prompt Selection Frequency Regularization and Prompt Knowledge Orthogonalization. Extensive experiments are conducted on the Ego4D, EPIC-Kitchens, and EGTEA datasets. The results consistently show that EgoPrompt achieves state-of-the-art performance across within-dataset, cross-dataset, and base-to-novel generalization benchmarks.

