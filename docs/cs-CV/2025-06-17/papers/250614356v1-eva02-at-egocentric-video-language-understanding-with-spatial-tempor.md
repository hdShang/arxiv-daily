---
layout: default
title: "EVA02-AT: Egocentric Video-Language Understanding with Spatial-Temporal Rotary Positional Embeddings and Symmetric Optimization"
---

# EVA02-AT: Egocentric Video-Language Understanding with Spatial-Temporal Rotary Positional Embeddings and Symmetric Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14356" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14356v1</a>
  <a href="https://arxiv.org/pdf/2506.14356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14356v1', 'EVA02-AT: Egocentric Video-Language Understanding with Spatial-Temporal Rotary Positional Embeddings and Symmetric Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoqi Wang, Yi Wang, Lap-Pui Chau

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-17

**🔗 代码/项目**: [GITHUB](https://github.com/xqwang14/EVA02-AT)

---

## 💡 一句话要点

**提出EVA02-AT以解决自我中心视频语言理解中的多重挑战**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我中心视频理解` `时空建模` `多实例检索` `旋转位置嵌入` `对称多相似性损失` `视频语言模型` `深度学习`

## 📋 核心要点

1. 现有方法在自我中心视频语言理解中面临高预训练成本、时空编码无效和学习目标不精确等挑战。
2. 本文提出EVA02-AT，通过单阶段预训练将CLIP模型转化为视频编码器，并引入时空旋转位置嵌入和联合注意力机制。
3. 在Ego4D、EPIC-Kitchens-100和Charades-Ego等数据集上，EVA02-AT在零-shot和微调设置下均实现了最先进的性能。

## 📝 摘要（中文）

自我中心视频语言理解需要高效且准确的时空建模。现有方法面临三大挑战：一是多阶段预训练导致的高成本，二是手动分割的3D旋转位置嵌入影响特征交互，三是软标签多实例检索中的学习目标不精确，忽视负样本相关性。本文提出EVA02-AT，一个基于EVA02的视频语言基础模型，专为自我中心视频理解任务设计。EVA02-AT通过单阶段预训练高效地将图像基础的CLIP模型转化为统一的视频编码器，并引入时空旋转位置嵌入和联合注意力机制，有效编码空间和时间信息。我们还提出对称多相似性损失（SMS），为正负样本提供更精确的学习目标。实验表明，EVA02-AT在多个数据集上实现了最先进的性能，且参数更少。

## 🔬 方法详解

**问题定义**：本文旨在解决自我中心视频语言理解中的高预训练成本、时空编码无效及学习目标不精确等问题。现有方法往往依赖于复杂的多阶段预训练流程，导致效率低下，同时手动分割的旋转位置嵌入影响特征的有效交互。

**核心思路**：EVA02-AT通过单阶段预训练高效地将图像基础的CLIP模型转化为视频编码器，避免了多阶段预训练的复杂性。同时，采用时空旋转位置嵌入与联合注意力机制，能够在整个隐藏维度上有效编码空间和时间信息，从而学习到跨轴关系。

**技术框架**：EVA02-AT的整体架构包括一个统一的视频编码器，时空旋转位置嵌入模块，以及对称多相似性损失（SMS）模块。模型首先通过单阶段预训练进行初始化，然后在多实例视频语言检索任务中进行微调。

**关键创新**：最重要的创新在于引入时空旋转位置嵌入和联合注意力机制，使得模型能够同时有效地捕捉空间和时间信息，进而改善视频中的运动和交互建模。与现有方法相比，EVA02-AT在特征交互上具有更高的灵活性和准确性。

**关键设计**：在损失函数方面，采用对称多相似性损失（SMS），为正负样本提供更精确的学习目标。此外，模型设计中还包括优化的参数设置，以减少模型的复杂性并提升性能。通过这些设计，EVA02-AT在多个数据集上展现了优越的性能。

## 📊 实验亮点

EVA02-AT在Ego4D、EPIC-Kitchens-100和Charades-Ego等数据集上实现了最先进的性能，尤其在多实例检索基准上，采用SMS损失的模型表现出显著的性能提升，参数数量更少，效率更高。

## 🎯 应用场景

该研究在自我中心视频理解领域具有广泛的应用潜力，尤其是在智能监控、虚拟现实和人机交互等场景中。通过提高视频与语言的理解能力，EVA02-AT能够为自动化视频分析、内容检索和用户交互提供更智能的解决方案，未来可能推动相关技术的进一步发展。

## 📄 摘要（原文）

> Egocentric video-language understanding demands both high efficiency and accurate spatial-temporal modeling. Existing approaches face three key challenges: 1) Excessive pre-training cost arising from multi-stage pre-training pipelines, 2) Ineffective spatial-temporal encoding due to manually split 3D rotary positional embeddings that hinder feature interactions, and 3) Imprecise learning objectives in soft-label multi-instance retrieval, which neglect negative pair correlations. In this paper, we introduce EVA02-AT, a suite of EVA02-based video-language foundation models tailored to egocentric video understanding tasks. EVA02-AT first efficiently transfers an image-based CLIP model into a unified video encoder via a single-stage pretraining. Second, instead of applying rotary positional embeddings to isolated dimensions, we introduce spatial-temporal rotary positional embeddings along with joint attention, which can effectively encode both spatial and temporal information on the entire hidden dimension. This joint encoding of spatial-temporal features enables the model to learn cross-axis relationships, which are crucial for accurately modeling motion and interaction in videos. Third, focusing on multi-instance video-language retrieval tasks, we introduce the Symmetric Multi-Similarity (SMS) loss and a novel training framework that advances all soft labels for both positive and negative pairs, providing a more precise learning objective. Extensive experiments on Ego4D, EPIC-Kitchens-100, and Charades-Ego under zero-shot and fine-tuning settings demonstrate that EVA02-AT achieves state-of-the-art performance across diverse egocentric video-language tasks with fewer parameters. Models with our SMS loss also show significant performance gains on multi-instance retrieval benchmarks. Our code and models are publicly available at https://github.com/xqwang14/EVA02-AT .

