---
layout: default
title: "MoCa: Modality-aware Continual Pre-training Makes Better Bidirectional Multimodal Embeddings"
---

# MoCa: Modality-aware Continual Pre-training Makes Better Bidirectional Multimodal Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23115" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23115v1</a>
  <a href="https://arxiv.org/pdf/2506.23115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23115v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23115v1', 'MoCa: Modality-aware Continual Pre-training Makes Better Bidirectional Multimodal Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haonan Chen, Hong Liu, Yuping Luo, Liang Wang, Nan Yang, Furu Wei, Zhicheng Dou

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-29

**备注**: Homepage: https://haon-chen.github.io/MoCa/

---

## 💡 一句话要点

**提出MoCa以解决多模态嵌入模型的关键限制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态嵌入` `因果视觉语言模型` `双向注意力` `联合重建` `异构对比微调` `上下文感知` `模型可扩展性`

## 📋 核心要点

1. 现有多模态嵌入模型在因果注意力机制、数据依赖性和训练目标多样性方面存在显著不足。
2. 提出MoCa框架，通过双向注意力和联合重建目标，提升多模态嵌入模型的性能和可扩展性。
3. 实验结果显示，MoCa在多个基准测试中均超越了现有方法，展现出显著的性能提升。

## 📝 摘要（中文）

多模态嵌入模型基于因果视觉语言模型（VLMs），在多项任务中展现出良好前景。然而，现有方法存在三个主要限制：因果注意力在嵌入任务中的效果不佳；对高质量标注配对数据的依赖导致可扩展性问题；训练目标和数据的多样性有限。为了解决这些问题，本文提出了MoCa，一个将预训练VLM转化为有效双向多模态嵌入模型的两阶段框架。第一阶段引入了联合重建目标，增强了双向上下文感知推理；第二阶段利用丰富的多模态数据进行异构对比微调。实验结果表明，MoCa在MMEB和ViDoRe-v2基准上均实现了新的最先进结果，且在模型规模和训练数据上展现出强大的可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前多模态嵌入模型在因果注意力机制、数据依赖性和训练目标多样性方面的不足。这些问题限制了模型的性能和可扩展性。

**核心思路**：论文提出MoCa框架，通过引入双向注意力机制和联合重建目标，增强模型的上下文感知能力，并利用丰富的多模态数据进行训练，以提高模型的泛化能力。

**技术框架**：MoCa框架分为两个主要阶段：第一阶段是模态感知的持续预训练，采用联合重建目标处理文本和图像输入；第二阶段是异构对比微调，利用多样化的多模态数据进行训练。

**关键创新**：MoCa的核心创新在于引入双向注意力机制和联合重建目标，使得模型在处理多模态输入时能够更好地捕捉上下文信息，与现有方法相比，显著提升了嵌入效果。

**关键设计**：在设计中，采用了联合重建损失函数，以同时处理文本和图像数据，确保模型在多模态输入下的有效性。此外，利用丰富的语义数据进行对比微调，增强了模型的表示能力。

## 📊 实验亮点

实验结果表明，MoCa在MMEB和ViDoRe-v2基准测试中均实现了新的最先进结果，具体性能提升幅度达到X%，显著超越了现有的对比基线，展现出强大的模型规模和训练数据的可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括图像和文本的联合理解、跨模态检索、以及多模态生成任务等。通过提升多模态嵌入模型的性能，MoCa能够在实际应用中提供更准确的结果，推动智能助手、自动驾驶等领域的发展。

## 📄 摘要（原文）

> Multimodal embedding models, built upon causal Vision Language Models (VLMs), have shown promise in various tasks. However, current approaches face three key limitations: the use of causal attention in VLM backbones is suboptimal for embedding tasks; scalability issues due to reliance on high-quality labeled paired data for contrastive learning; and limited diversity in training objectives and data. To address these issues, we propose MoCa, a two-stage framework for transforming pre-trained VLMs into effective bidirectional multimodal embedding models. The first stage, Modality-aware Continual Pre-training, introduces a joint reconstruction objective that simultaneously denoises interleaved text and image inputs, enhancing bidirectional context-aware reasoning. The second stage, Heterogeneous Contrastive Fine-tuning, leverages diverse, semantically rich multimodal data beyond simple image-caption pairs to enhance generalization and alignment. Our method addresses the stated limitations by introducing bidirectional attention through continual pre-training, scaling effectively with massive unlabeled datasets via joint reconstruction objectives, and utilizing diverse multimodal data for enhanced representation robustness. Experiments demonstrate that MoCa consistently improves performance across MMEB and ViDoRe-v2 benchmarks, achieving new state-of-the-art results, and exhibits strong scalability with both model size and training data on MMEB.

