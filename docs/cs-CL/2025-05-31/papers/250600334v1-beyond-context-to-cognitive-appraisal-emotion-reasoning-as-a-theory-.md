---
layout: default
title: "Beyond Context to Cognitive Appraisal: Emotion Reasoning as a Theory of Mind Benchmark for Large Language Models"
---

# Beyond Context to Cognitive Appraisal: Emotion Reasoning as a Theory of Mind Benchmark for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00334" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00334v1</a>
  <a href="https://arxiv.org/pdf/2506.00334.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00334v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00334v1', 'Beyond Context to Cognitive Appraisal: Emotion Reasoning as a Theory of Mind Benchmark for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gerard Christopher Yeo, Kokil Jaidka

**分类**: cs.CL

**发布日期**: 2025-05-31

**备注**: 9 pages, 3 figures

---

## 💡 一句话要点

**提出情感推理作为大语言模型的理论心智基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感推理` `理论心智` `认知评估` `大语言模型` `心理学理论` `上下文理解` `情感分析`

## 📋 核心要点

1. 现有情感识别方法主要依赖显性线索，难以处理隐性上下文线索，导致情感推理能力不足。
2. 本研究提出基于认知评估理论的理论心智评估数据集，评估大语言模型在情感推理中的表现。
3. 实验结果显示，大语言模型在情感推理方面有一定能力，但在情境结果与情感的关联上表现不佳。

## 📝 摘要（中文）

情感识别任务的数据集通常包含显性线索，用于预测文本中表达的情感。然而，文本有时包含隐性上下文线索，富含情感语义，需更高阶推理能力来推断情感状态。本研究超越表面感知特征，探讨大语言模型如何在理论心智框架下利用上下文信息推理他人的情感状态。基于认知评估理论，我们策划了一个专门的理论心智评估数据集，以评估前向推理（从上下文到情感）和后向推理（从情感到推断上下文）。研究表明，尽管大语言模型在推理方面有一定能力，但在将情境结果和评估与特定情感关联方面表现较差。我们的工作强调了在情感推理背景下，心理学理论在大语言模型训练和评估中的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决大语言模型在情感推理中对隐性上下文线索的理解不足，现有方法多依赖显性线索，无法有效推断情感状态。

**核心思路**：通过构建基于认知评估理论的理论心智评估数据集，评估大语言模型在前向和后向推理中的能力，推动模型在情感推理方面的进步。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。数据集包含丰富的上下文信息，模型通过上下文推理情感状态，并进行反向推理。

**关键创新**：本研究的创新点在于引入认知评估理论作为评估框架，强调心理学理论在情感推理中的重要性，推动大语言模型的情感理解能力。

**关键设计**：在数据集构建中，精心设计了上下文与情感的关联，模型训练中采用了特定的损失函数，以提高情感推理的准确性。

## 📊 实验亮点

实验结果表明，大语言模型在情感推理任务中表现出一定的推理能力，但在将情境结果与特定情感关联方面的准确性较低，显示出模型在情感理解上的局限性。具体性能数据尚未提供。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、社交媒体监测和人机交互等。通过提升大语言模型的情感推理能力，可以更好地理解用户情感，改善用户体验，推动情感计算的发展。

## 📄 摘要（原文）

> Datasets used for emotion recognition tasks typically contain overt cues that can be used in predicting the emotions expressed in a text. However, one challenge is that texts sometimes contain covert contextual cues that are rich in affective semantics, which warrant higher-order reasoning abilities to infer emotional states, not simply the emotions conveyed. This study advances beyond surface-level perceptual features to investigate how large language models (LLMs) reason about others' emotional states using contextual information, within a Theory-of-Mind (ToM) framework. Grounded in Cognitive Appraisal Theory, we curate a specialized ToM evaluation dataset1 to assess both forward reasoning - from context to emotion- and backward reasoning - from emotion to inferred context. We showed that LLMs can reason to a certain extent, although they are poor at associating situational outcomes and appraisals with specific emotions. Our work highlights the need for psychological theories in the training and evaluation of LLMs in the context of emotion reasoning.

