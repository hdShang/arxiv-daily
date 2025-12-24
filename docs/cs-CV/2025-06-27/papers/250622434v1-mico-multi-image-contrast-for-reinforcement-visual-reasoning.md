---
layout: default
title: "MiCo: Multi-image Contrast for Reinforcement Visual Reasoning"
---

# MiCo: Multi-image Contrast for Reinforcement Visual Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22434" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22434v1</a>
  <a href="https://arxiv.org/pdf/2506.22434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22434v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22434v1', 'MiCo: Multi-image Contrast for Reinforcement Visual Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xi Chen, Mingkang Zhu, Shaoteng Liu, Xiaoyang Wu, Xiaogang Xu, Yu Liu, Xiang Bai, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出MiCo以解决多图像推理中的逻辑关联问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多图像推理` `自监督学习` `视觉推理` `强化学习` `视觉比较` `逻辑推理` `图像处理`

## 📋 核心要点

1. 现有方法依赖人工整理的问题-答案对，难以处理复杂的视觉细节和逻辑关系。
2. 论文提出通过构建图像三元组，利用自监督学习的方式进行视觉推理，避免人工标注。
3. 实验结果显示，该方法在多图像推理基准上显著提升，且在一般视觉任务中表现强劲。

## 📝 摘要（中文）

本研究探索了如何通过Chain-of-Thought (CoT) 推理将视觉线索连接跨多个图像。现有方法通常依赖于手动整理的问题-答案对，这在处理细致的视觉细节和复杂逻辑时尤为困难。我们借鉴自监督视觉表示学习的理念，构建了包含两个增强视图和一个相似但不同图像的图像三元组。在训练过程中，模型被提示生成推理过程以比较这些图像，并通过基于规则的强化学习进行优化。实验表明，尽管仅在视觉比较任务上训练，所学的推理能力在广泛问题上有效泛化，且无需依赖人工标注的问题-答案对，显著提升了多图像推理基准的表现。

## 🔬 方法详解

**问题定义**：本论文旨在解决多图像推理中视觉线索的逻辑关联问题。现有方法通常依赖人工标注的问题-答案对，难以处理细致的视觉信息和复杂的逻辑关系。

**核心思路**：我们提出了一种新方法，通过构建包含两个增强视图和一个相似但不同图像的图像三元组，利用自监督学习的方式进行推理训练。这样的设计使得模型能够关注细微的视觉变化并进行逻辑推理。

**技术框架**：整体架构包括图像三元组的构建、推理过程的生成和基于规则的强化学习优化。模型在训练时需要比较图像，判断它们是相同还是不同。

**关键创新**：最重要的创新在于利用自监督学习的方式构建图像三元组，避免了对人工标注的依赖，并且通过视觉比较任务训练出有效的推理能力。

**关键设计**：在模型设计中，采用了特定的损失函数来优化推理过程，并通过数据增强技术提升模型对细微变化的敏感性。

## 📊 实验亮点

实验结果显示，所提方法在多图像推理基准上显著提升，超越了现有的主流方法，且在一般视觉任务中表现出色，验证了模型的广泛适用性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括图像理解、自动问答系统和多模态学习等。通过提高模型在复杂视觉推理任务中的表现，能够推动智能系统在实际场景中的应用，提升人机交互的智能化水平。

## 📄 摘要（原文）

> This work explores enabling Chain-of-Thought (CoT) reasoning to link visual cues across multiple images. A straightforward solution is to adapt rule-based reinforcement learning for Vision-Language Models (VLMs). However, such methods typically rely on manually curated question-answer pairs, which can be particularly challenging when dealing with fine grained visual details and complex logic across images. Inspired by self-supervised visual representation learning, we observe that images contain inherent constraints that can serve as supervision. Based on this insight, we construct image triplets comprising two augmented views of the same image and a third, similar but distinct image. During training, the model is prompted to generate a reasoning process to compare these images (i.e., determine same or different). Then we optimize the model with rule-based reinforcement learning. Due to the high visual similarity and the presence of augmentations, the model must attend to subtle visual changes and perform logical reasoning to succeed. Experiments show that, although trained solely on visual comparison tasks, the learned reasoning ability generalizes effectively to a wide range of questions. Without relying on any human-annotated question-answer pairs, our method achieves significant improvements on multi-image reasoning benchmarks and shows strong performance on general vision tasks.

