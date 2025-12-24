---
layout: default
title: "MEDUSA: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions"
---

# MEDUSA: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09556" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09556v2</a>
  <a href="https://arxiv.org/pdf/2506.09556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09556v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09556v2', 'MEDUSA: A Multimodal Deep Fusion Multi-Stage Training Framework for Speech Emotion Recognition in Naturalistic Conditions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Chatzichristodoulou, Despoina Kosmopoulou, Antonios Kritikos, Anastasia Poulopoulou, Efthymios Georgiou, Athanasios Katsamanis, Vassilis Katsouros, Alexandros Potamianos

**分类**: cs.CL

**发布日期**: 2025-06-11 (更新: 2025-09-04)

**备注**: Interspeech 2025

---

## 💡 一句话要点

**提出MEDUSA框架以解决自然条件下的语音情感识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音情感识别` `多模态融合` `深度学习` `集成学习` `自然条件`

## 📋 核心要点

1. 现有的语音情感识别方法面临情感类别不平衡和模糊性的问题，导致识别准确率低。
2. MEDUSA框架通过四阶段训练流程，结合多模态信息和集成学习，有效提升了情感识别的性能。
3. 在2025年国际语音会议的挑战中，MEDUSA在分类情感识别任务中排名第一，显示出其优越性。

## 📝 摘要（中文）

语音情感识别（SER）是一项具有挑战性的任务，主要由于人类情感的主观性及其在自然条件下的不均衡表现。本文提出了MEDUSA，一个多模态框架，采用四阶段训练流程，有效处理类别不平衡和情感模糊性。前两阶段训练一个分类器集成，利用DeepSER，这是一种基于预训练自监督声学和语言表示的深度跨模态变换器融合机制的创新扩展。采用Manifold MixUp进行进一步的正则化。后两阶段优化一个可训练的元分类器，结合集成预测。我们的训练方法结合了人类注释分数作为软目标，并配合平衡数据采样和多任务学习。MEDUSA在2025年国际语音会议的自然条件下语音情感识别挑战中获得了第一名。

## 🔬 方法详解

**问题定义**：本文旨在解决自然条件下语音情感识别中的类别不平衡和情感模糊性问题。现有方法往往无法有效处理这些挑战，导致识别效果不佳。

**核心思路**：MEDUSA框架通过四个训练阶段，利用多模态信息和集成学习策略，增强模型对情感的识别能力。通过引入DeepSER和Manifold MixUp，进一步提升模型的泛化能力。

**技术框架**：整体架构分为四个阶段：前两阶段训练一个分类器集成，后两阶段优化一个元分类器。前者使用DeepSER进行跨模态融合，后者结合集成预测。

**关键创新**：MEDUSA的核心创新在于其四阶段训练流程和DeepSER的引入，显著提高了对情感模糊性的处理能力，与传统方法相比，具有更强的适应性和准确性。

**关键设计**：在模型设计中，采用了人类注释分数作为软目标，结合平衡数据采样和多任务学习，确保模型在训练过程中能够有效学习到情感特征。

## 📊 实验亮点

在2025年国际语音会议的自然条件下语音情感识别挑战中，MEDUSA在分类情感识别任务中获得第一名，展示了其在处理情感模糊性和类别不平衡方面的卓越性能。相较于基线方法，MEDUSA的性能显著提升，具体数据未知。

## 🎯 应用场景

MEDUSA框架在语音情感识别领域具有广泛的应用潜力，尤其是在客服、心理健康监测和人机交互等场景中。其高效的情感识别能力能够提升用户体验，帮助系统更好地理解和响应用户情感。未来，随着技术的进一步发展，MEDUSA可能会在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> SER is a challenging task due to the subjective nature of human emotions and their uneven representation under naturalistic conditions. We propose MEDUSA, a multimodal framework with a four-stage training pipeline, which effectively handles class imbalance and emotion ambiguity. The first two stages train an ensemble of classifiers that utilize DeepSER, a novel extension of a deep cross-modal transformer fusion mechanism from pretrained self-supervised acoustic and linguistic representations. Manifold MixUp is employed for further regularization. The last two stages optimize a trainable meta-classifier that combines the ensemble predictions. Our training approach incorporates human annotation scores as soft targets, coupled with balanced data sampling and multitask learning. MEDUSA ranked 1st in Task 1: Categorical Emotion Recognition in the Interspeech 2025: Speech Emotion Recognition in Naturalistic Conditions Challenge.

