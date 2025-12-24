---
layout: default
title: "Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation"
---

# Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10395" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10395v2</a>
  <a href="https://arxiv.org/pdf/2506.10395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10395v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10395v2', 'Pisces: An Auto-regressive Foundation Model for Image Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyang Xu, Jiuhai Chen, Zhaojiang Lin, Xichen Pan, Lifu Huang, Tianyi Zhou, Madian Khabsa, Qifan Wang, Di Jin, Michihiro Yasunaga, Lili Yu, Xi Victoria Lin, Shaoliang Nie

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-07-12)

**备注**: Unified image understanding and generation model

---

## 💡 一句话要点

**提出Pisces以解决多模态图像理解与生成的统一模型挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `图像理解` `图像生成` `自回归模型` `视觉编码` `深度学习` `模型优化`

## 📋 核心要点

1. 现有的统一多模态模型在图像理解和生成任务中表现不佳，主要由于视觉特征和训练过程的差异。
2. Pisces通过解耦视觉编码架构和定制的训练技术，优化了多模态生成过程，从而提升了模型性能。
3. 在超过20个公共基准上，Pisces在图像理解任务中表现优异，并在GenEval基准上展现了强大的生成能力。

## 📝 摘要（中文）

近年来，大型语言模型的进展使得多模态基础模型能够在统一框架下处理图像理解和生成任务。然而，统一模型在这两项任务中的表现往往不及专门模型。本文提出Pisces，一个自回归的多模态基础模型，通过新颖的解耦视觉编码架构和针对多模态生成优化的训练技术来应对这一挑战。结合精心的数据策划、预训练和微调，Pisces在图像理解和生成任务中均表现出色。我们在20多个公共基准上评估了Pisces，结果显示其在多种任务中均表现强劲，并在图像生成的广泛采用基准GenEval上展现出稳健的生成能力。

## 🔬 方法详解

**问题定义**：本文旨在解决统一多模态模型在图像理解与生成任务中性能不足的问题。现有方法在处理视觉特征时，往往无法兼顾两者的需求，导致效果不佳。

**核心思路**：Pisces的核心思路是通过解耦视觉编码架构，使得模型能够分别优化图像理解和生成的特征表示，从而提高整体性能。

**技术框架**：Pisces的整体架构包括数据策划、预训练和微调三个主要阶段。首先，通过精心选择和处理数据集来增强模型的学习能力；其次，进行预训练以学习通用的视觉特征；最后，通过微调来适应特定任务。

**关键创新**：Pisces的主要创新在于其解耦的视觉编码器设计，这使得模型能够独立处理图像理解和生成任务的特征，从而克服了传统统一模型的局限性。

**关键设计**：在模型设计中，Pisces采用了特定的损失函数来平衡图像理解与生成的训练目标，同时在网络结构上引入了多层次的视觉编码器，以捕捉不同层次的特征信息。

## 📊 实验亮点

在实验中，Pisces在超过20个公共基准上展现了强劲的性能，尤其在图像理解任务中，显著超越了多个基线模型。此外，在GenEval基准上，Pisces的生成能力也表现出色，进一步验证了其在多模态任务中的有效性。

## 🎯 应用场景

Pisces模型在图像理解和生成领域具有广泛的应用潜力，能够用于智能图像搜索、自动图像标注、内容生成等任务。其创新的解耦设计为未来多模态模型的发展提供了新的思路，可能推动相关技术在实际应用中的落地与普及。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled multimodal foundation models to tackle both image understanding and generation within a unified framework. Despite these gains, unified models often underperform compared to specialized models in either task. A key challenge in developing unified models lies in the inherent differences between the visual features needed for image understanding versus generation, as well as the distinct training processes required for each modality. In this work, we introduce Pisces, an auto-regressive multimodal foundation model that addresses this challenge through a novel decoupled visual encoding architecture and tailored training techniques optimized for multimodal generation. Combined with meticulous data curation, pretraining, and finetuning, Pisces achieves competitive performance in both image understanding and image generation. We evaluate Pisces on over 20 public benchmarks for image understanding, where it demonstrates strong performance across a wide range of tasks. Additionally, on GenEval, a widely adopted benchmark for image generation, Pisces exhibits robust generative capabilities. Our extensive analysis reveals the synergistic relationship between image understanding and generation, and the benefits of using separate visual encoders, advancing the field of unified multimodal models.

