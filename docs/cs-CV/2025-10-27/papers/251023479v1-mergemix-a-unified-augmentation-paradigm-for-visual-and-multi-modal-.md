---
layout: default
title: "MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding"
---

# MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23479" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23479v1</a>
  <a href="https://arxiv.org/pdf/2510.23479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23479v1', 'MergeMix: A Unified Augmentation Paradigm for Visual and Multi-Modal Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Jin, Siyuan Li, Siyong Jian, Kai Yu, Huan Wang

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: Code Link: https://github.com/JinXins/MergeMix

---

## 💡 一句话要点

**提出MergeMix，统一视觉和多模态理解的增强范式，提升效率和对齐质量。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉-语言对齐` `数据增强` `偏好学习` `大型语言模型`

## 📋 核心要点

1. 现有MLLM依赖SFT或RL进行视觉-语言对齐，但SFT需要大量标注，RL则开销大且不稳定。
2. MergeMix通过注意力感知的图像混合和偏好驱动的训练，桥接SFT和RL，提升对齐质量。
3. 实验表明，MergeMix在分类任务中超越了其他启发式方法，并在效率和准确性上取得了平衡。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)中的视觉-语言对齐通常依赖于监督微调(SFT)或强化学习(RL)。SFT稳定高效，但需要大规模人工标注且无法捕捉细微偏好；RL引入奖励信号进行训练，但存在开销和不稳定问题。这些限制突出了可扩展性、鲁棒性和对齐质量之间的权衡。为了解决这个问题，我们提出了MergeMix，一种桥接SFT和RL的训练时增强范式。它首先应用基于注意力机制的图像混合，通过token合并实现更强的聚类表示和空间上下文感知，然后通过构建混合图像和原始图像的偏好对，提出了一种偏好驱动的MLLM训练范式，并通过SimPO损失进行优化。作为一种mixup增强，MergeMix增强了注意力一致性和效率，在分类任务中超越了其他基于启发式的方法。大量实验表明，MergeMix在提高效率的同时实现了具有竞争力的准确性，为分类和MLLM中的偏好对齐提供了一种可扩展的方法。

## 🔬 方法详解

**问题定义**：现有视觉-语言对齐方法，如监督微调（SFT）和强化学习（RL），存在各自的局限性。SFT依赖大量人工标注数据，成本高昂，且难以捕捉细微的偏好。RL虽然可以通过奖励信号进行训练，但训练过程不稳定，计算开销大。因此，如何在保证模型性能的同时，降低对人工标注的依赖，并提高训练的稳定性和效率，是本文要解决的核心问题。

**核心思路**：MergeMix的核心思想是结合SFT和RL的优点，通过一种新的数据增强方法和偏好学习策略，实现高效且高质量的视觉-语言对齐。它利用注意力机制指导图像混合，生成新的训练样本，并构建混合图像和原始图像的偏好对，引导模型学习更符合人类偏好的表示。

**技术框架**：MergeMix的整体框架包含两个主要步骤：1) 注意力感知的图像混合：使用token merge方法，根据注意力权重将图像的不同区域进行混合，生成新的图像。这种混合方式能够保留更多的聚类表示和空间上下文信息。2) 偏好驱动的训练：构建混合图像和原始图像的偏好对，并使用SimPO损失函数进行优化。SimPO损失函数鼓励模型对原始图像的偏好高于混合图像，从而引导模型学习更符合人类偏好的表示。

**关键创新**：MergeMix的关键创新在于其统一的增强范式，它将数据增强和偏好学习相结合，有效地利用了未标注数据，降低了对人工标注的依赖。此外，注意力感知的图像混合方法能够保留更多的图像信息，提高了模型的性能。

**关键设计**：在注意力感知的图像混合中，使用了token merge方法，该方法根据注意力权重将图像的不同区域进行合并。在偏好驱动的训练中，使用了SimPO损失函数，该损失函数定义如下：SimPO(s_θ(x), s_θ(x')) = -log(sigmoid(s_θ(x) - s_θ(x')))，其中s_θ(x)和s_θ(x')分别表示模型对原始图像x和混合图像x'的打分。该损失函数鼓励模型对原始图像的打分高于混合图像。

## 📊 实验亮点

实验结果表明，MergeMix在分类任务中超越了其他基于启发式的方法，实现了具有竞争力的准确性，同时提高了训练效率。具体性能数据未知，但论文强调了MergeMix在效率和准确性上的平衡，以及其在偏好对齐方面的优势。

## 🎯 应用场景

MergeMix可广泛应用于多模态大型语言模型，提升视觉-语言对齐效果，改进图像分类、图像描述、视觉问答等任务的性能。该方法降低了对大规模标注数据的依赖，具有实际应用价值，并为未来多模态学习研究提供新思路。

## 📄 摘要（原文）

> Vision-language alignment in multi-modal large language models (MLLMs) typically relies on supervised fine-tuning (SFT) or reinforcement learning (RL). SFT is stable and efficient but requires large-scale human annotations and cannot capture subtle preferences, while RL brings in a reward signal for training, but suffers from overhead and instability. These limitations highlight a trade-off between scalability, robustness, and alignment quality. To address this, we propose MergeMix, a training-time augmentation paradigm that bridges SFT and RL. It first applies an attention-aware image mixing via token merge with more cluster representation and spatial context, and then presents a preference-driven training paradigm for MLLMs by building preference pairs with mixed images and raw images, and optimizing via SimPO loss. As a mixup augmentation, MergeMix enhances attention consistency and efficiency, surpassing other heuristic-based methods in classification. Extensive experiments demonstrate that MergeMix achieves competitive accuracy with improved efficiency, providing a scalable approach to preference alignment in classification and MLLMs.

