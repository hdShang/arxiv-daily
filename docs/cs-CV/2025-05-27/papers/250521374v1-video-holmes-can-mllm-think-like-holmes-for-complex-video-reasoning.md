---
layout: default
title: "Video-Holmes: Can MLLM Think Like Holmes for Complex Video Reasoning?"
---

# Video-Holmes: Can MLLM Think Like Holmes for Complex Video Reasoning?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21374" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21374v1</a>
  <a href="https://arxiv.org/pdf/2505.21374.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21374v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21374v1', 'Video-Holmes: Can MLLM Think Like Holmes for Complex Video Reasoning?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Cheng, Yuying Ge, Teng Wang, Yixiao Ge, Jing Liao, Ying Shan

**分类**: cs.CV

**发布日期**: 2025-05-27

**备注**: Homepage: https://github.com/TencentARC/Video-Holmes

**🔗 代码/项目**: [GITHUB](https://github.com/TencentARC/Video-Holmes)

---

## 💡 一句话要点

**提出Video-Holmes基准以解决复杂视频推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `复杂视频推理` `多模态大语言模型` `信息整合` `视频理解` `推理基准` `福尔摩斯推理` `视觉线索`

## 📋 核心要点

1. 现有视频推理基准主要关注视觉感知，未能有效评估模型在复杂推理中的能力。
2. 本文提出Video-Holmes基准，模拟福尔摩斯的推理过程，设计问题以要求模型整合多个视觉线索。
3. 实验结果显示，尽管模型在视觉感知上表现优异，但在信息整合方面普遍存在不足，准确率普遍低于40%。

## 📝 摘要（中文）

近年来，链式推理和强化学习后训练的进展提升了多模态大语言模型（MLLMs）在视频推理方面的能力。然而，现有的视频基准主要评估视觉感知和基础能力，未能充分捕捉现实世界推理的复杂性。为此，本文提出了Video-Holmes基准，旨在评估MLLMs的复杂视频推理能力。该基准由1,837个问题构成，源自270部手动注释的悬疑短片，涵盖七个精心设计的任务。我们的评估显示，尽管这些模型在视觉感知方面表现良好，但在信息整合上存在显著困难，最佳模型的准确率仅为45%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频推理基准无法有效评估多模态大语言模型在复杂推理中的能力的问题。现有方法往往只关注视觉感知和简单的提示，无法反映人类推理的复杂性。

**核心思路**：论文提出Video-Holmes基准，灵感来源于福尔摩斯的推理过程，设计问题要求模型主动寻找和整合多个视觉线索，以模拟人类的推理方式。

**技术框架**：Video-Holmes基准包含1,837个问题，源自270部悬疑短片，分为七个任务。每个任务通过识别关键事件和因果关系构建，问题设计要求模型在不同视频片段中连接相关线索。

**关键创新**：最重要的创新在于通过模拟复杂的推理过程，提出了一种新的评估标准，强调了信息整合的重要性，与现有方法的单一视觉感知评估形成鲜明对比。

**关键设计**：在设计过程中，任务的构建注重关键事件的识别和因果关系的分析，确保问题能够有效测试模型的推理能力。

## 📊 实验亮点

实验结果显示，最佳模型Gemini-2.5-Pro的准确率仅为45%，大多数模型的得分低于40%。这一结果突显了当前多模态模型在信息整合和复杂推理方面的不足，强调了Video-Holmes基准在推动研究进展中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括智能视频分析、自动化监控和人机交互等。通过提升多模态模型的推理能力，Video-Holmes基准有助于推动相关技术的发展，增强模型在复杂场景下的理解和决策能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in CoT reasoning and RL post-training have been reported to enhance video reasoning capabilities of MLLMs. This progress naturally raises a question: can these models perform complex video reasoning in a manner comparable to human experts? However, existing video benchmarks primarily evaluate visual perception and grounding abilities, with questions that can be answered based on explicit prompts or isolated visual cues. Such benchmarks do not fully capture the intricacies of real-world reasoning, where humans must actively search for, integrate, and analyze multiple clues before reaching a conclusion. To address this issue, we present Video-Holmes, a benchmark inspired by the reasoning process of Sherlock Holmes, designed to evaluate the complex video reasoning capabilities of MLLMs. Video-Holmes consists of 1,837 questions derived from 270 manually annotated suspense short films, which spans seven carefully designed tasks. Each task is constructed by first identifying key events and causal relationships within films, and then designing questions that require models to actively locate and connect multiple relevant visual clues scattered across different video segments. Our comprehensive evaluation of state-of-the-art MLLMs reveals that, while these models generally excel at visual perception, they encounter substantial difficulties with integrating information and often miss critical clues. For example, the best-performing model, Gemini-2.5-Pro, achieves an accuracy of only 45%, with most models scoring below 40%. We aim that Video-Holmes can serve as a "Holmes-test" for multimodal reasoning, motivating models to reason more like humans and emphasizing the ongoing challenges in this field. The benchmark is released in https://github.com/TencentARC/Video-Holmes.

