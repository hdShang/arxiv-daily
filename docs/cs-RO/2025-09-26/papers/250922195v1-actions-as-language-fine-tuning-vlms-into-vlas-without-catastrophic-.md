---
layout: default
title: "Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting"
---

# Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22195" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22195v1</a>
  <a href="https://arxiv.org/pdf/2509.22195.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22195v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22195v1', 'Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Asher J. Hancock, Xindi Wu, Lihan Zha, Olga Russakovsky, Anirudha Majumdar

**分类**: cs.RO

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出VLM2VLA以解决机器人遥控中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `机器人遥控` `灾难性遗忘` `低秩适应` `多模态学习` `零-shot泛化` `自然语言处理`

## 📋 核心要点

1. 现有的视觉语言模型在机器人遥控数据上微调时，容易导致基础推理和多模态理解能力的下降。
2. 提出VLM2VLA，通过自然语言表示低级动作，解决VLM与机器人数据之间的分布不匹配问题。
3. 实验结果表明，VLM2VLA在保持VLM核心能力的同时，实现了对新任务的零-shot泛化，具有良好的实际应用潜力。

## 📝 摘要（中文）

本研究针对在机器人遥控数据上微调视觉语言模型（VLM）以创建视觉语言动作（VLA）模型时，面临的灾难性遗忘问题进行了探讨。我们认为，这种遗忘源于VLM的互联网规模预训练语料与机器人微调数据之间的分布不匹配。为了解决这一问题，我们提出了VLM2VLA训练范式，通过自然语言表示低级动作，从数据层面解决分布不匹配。该方法仅使用低秩适应（LoRA）对VLM进行微调，避免了对基础架构的重大修改。通过大量的视觉问答（VQA）研究和800多个真实世界的机器人实验，我们证明了VLM2VLA能够保持VLM的核心能力，实现对新任务的零-shot泛化。

## 🔬 方法详解

**问题定义**：本研究旨在解决在机器人遥控数据上微调视觉语言模型（VLM）时出现的灾难性遗忘问题。现有方法在学习生成动作时，往往会削弱VLM的基础推理和多模态理解能力，影响其在新场景中的泛化能力。

**核心思路**：论文提出的VLM2VLA训练范式，通过自然语言对低级动作进行表示，从而在数据层面解决VLM与机器人微调数据之间的分布不匹配。这种对齐方式使得可以仅通过低秩适应（LoRA）对VLM进行微调，避免了对基础架构的重大修改。

**技术框架**：VLM2VLA的整体架构包括数据预处理、自然语言表示生成、低秩适应微调和评估模块。首先，通过自然语言对低级动作进行表示，然后使用LoRA对VLM进行微调，最后在真实世界的机器人任务中进行评估。

**关键创新**：VLM2VLA的核心创新在于通过自然语言表示低级动作，从而解决了VLM与机器人数据之间的分布不匹配问题。这一方法与现有的直接微调方法本质上不同，避免了灾难性遗忘。

**关键设计**：在技术细节上，VLM2VLA使用了低秩适应（LoRA）作为微调策略，确保对VLM的基础架构进行最小修改。此外，损失函数的设计也考虑了多模态数据的特性，以增强模型的泛化能力。

## 📊 实验亮点

实验结果显示，VLM2VLA在视觉问答（VQA）任务中表现优异，能够在不进行昂贵的共同训练的情况下，保持VLM的核心能力。通过800多个真实世界的机器人实验，VLM2VLA实现了对新任务的零-shot泛化，显著提升了模型的实际应用能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人遥控、智能家居、自动化生产等。通过保持VLM的核心能力，VLM2VLA可以在多种新任务中实现零-shot泛化，具有广泛的实际价值和未来影响力，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Fine-tuning vision-language models (VLMs) on robot teleoperation data to create vision-language-action (VLA) models is a promising paradigm for training generalist policies, but it suffers from a fundamental tradeoff: learning to produce actions often diminishes the VLM's foundational reasoning and multimodal understanding, hindering generalization to novel scenarios, instruction following, and semantic understanding. We argue that this catastrophic forgetting is due to a distribution mismatch between the VLM's internet-scale pretraining corpus and the robotics fine-tuning data. Inspired by this observation, we introduce VLM2VLA: a VLA training paradigm that first resolves this mismatch at the data level by representing low-level actions with natural language. This alignment makes it possible to train VLAs solely with Low-Rank Adaptation (LoRA), thereby minimally modifying the VLM backbone and averting catastrophic forgetting. As a result, the VLM can be fine-tuned on robot teleoperation data without fundamentally altering the underlying architecture and without expensive co-training on internet-scale VLM datasets. Through extensive Visual Question Answering (VQA) studies and over 800 real-world robotics experiments, we demonstrate that VLM2VLA preserves the VLM's core capabilities, enabling zero-shot generalization to novel tasks that require open-world semantic reasoning and multilingual instruction following.

