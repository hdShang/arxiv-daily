---
layout: default
title: "Mamba-Adaptor: State Space Model Adaptor for Visual Recognition"
---

# Mamba-Adaptor: State Space Model Adaptor for Visual Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12685" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12685v1</a>
  <a href="https://arxiv.org/pdf/2505.12685.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12685v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12685v1', 'Mamba-Adaptor: State Space Model Adaptor for Visual Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Xie, Jiahao Nie, Yujin Tang, Wenkang Zhang, Hongshen Zhao

**分类**: cs.CV

**发布日期**: 2025-05-19

**备注**: CVPR paper

---

## 💡 一句话要点

**提出Mamba-Adaptor以解决视觉识别中的长程遗忘和空间建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `状态空间模型` `视觉识别` `长程遗忘` `空间建模` `多尺度卷积` `迁移学习` `图像分类`

## 📋 核心要点

1. 现有的Mamba模型在视觉任务中表现不佳，主要由于因果计算无法获取全局上下文和长程遗忘问题。
2. 本文提出了Mamba-Adaptor，利用Adaptor-T和Adaptor-S模块来增强模型的记忆能力和空间建模能力。
3. 实验结果表明，Mamba-Adaptor在多个视觉任务中表现优异，尤其在ImageNet和COCO基准上达到了最先进的性能。

## 📝 摘要（中文）

近年来，状态空间模型（SSM），尤其是Mamba，在视觉建模方面表现出色，但在视觉任务中的应用受到三个主要限制的影响：1）因果计算无法访问全局上下文；2）在计算当前隐藏状态时存在长程遗忘；3）由于输入的序列转换，空间结构建模较弱。为了解决这些问题，本文提出了一种简单而强大的视觉任务适配器Mamba-Adaptor，包含两个功能模块：Adaptor-T和Adaptor-S。通过这两个模块，Mamba-Adaptor能够增强上下文建模，显著提高在ImageNet和COCO基准上的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决Mamba模型在视觉任务中表现不佳的问题，主要痛点包括因果计算无法访问全局上下文、长程遗忘以及空间结构建模不足。

**核心思路**：提出Mamba-Adaptor，通过两个模块（Adaptor-T和Adaptor-S）来增强模型的记忆能力和空间建模能力，以克服现有模型的局限性。

**技术框架**：Mamba-Adaptor由两个主要模块组成：Adaptor-T用于选择可学习的位置作为记忆增强，Adaptor-S利用多尺度膨胀卷积核来提升空间建模能力。整体流程包括输入处理、特征提取和输出增强。

**关键创新**：Mamba-Adaptor的创新在于引入了轻量级的预测模块和多尺度卷积结构，显著提高了上下文建模能力，与传统的因果计算方法形成鲜明对比。

**关键设计**：在设计中，Adaptor-T模块通过选择特定位置来缓解长程遗忘，而Adaptor-S模块则通过多尺度卷积核增强空间特征输出，确保模型能够更好地捕捉图像的结构信息。实验中使用了标准的损失函数和优化策略，以确保模型的有效性。

## 📊 实验亮点

在实验中，Mamba-Adaptor在ImageNet和COCO基准上取得了最先进的性能，相较于传统模型，性能提升幅度显著，验证了其在视觉任务中的有效性和实用性。

## 🎯 应用场景

Mamba-Adaptor的研究成果在多个视觉任务中具有广泛的应用潜力，包括图像分类、目标检测和迁移学习等领域。其高效的模型设计和优越的性能使其在实际应用中能够显著提升视觉系统的识别能力，推动计算机视觉技术的发展。

## 📄 摘要（原文）

> Recent State Space Models (SSM), especially Mamba, have demonstrated impressive performance in visual modeling and possess superior model efficiency. However, the application of Mamba to visual tasks suffers inferior performance due to three main constraints existing in the sequential model: 1) Casual computing is incapable of accessing global context; 2) Long-range forgetting when computing the current hidden states; 3) Weak spatial structural modeling due to the transformed sequential input. To address these issues, we investigate a simple yet powerful vision task Adaptor for Mamba models, which consists of two functional modules: Adaptor-T and Adaptor-S. When solving the hidden states for SSM, we apply a lightweight prediction module Adaptor-T to select a set of learnable locations as memory augmentations to ease long-range forgetting issues. Moreover, we leverage Adapator-S, composed of multi-scale dilated convolutional kernels, to enhance the spatial modeling and introduce the image inductive bias into the feature output. Both modules can enlarge the context modeling in casual computing, as the output is enhanced by the inaccessible features. We explore three usages of Mamba-Adaptor: A general visual backbone for various vision tasks; A booster module to raise the performance of pretrained backbones; A highly efficient fine-tuning module that adapts the base model for transfer learning tasks. Extensive experiments verify the effectiveness of Mamba-Adaptor in three settings. Notably, our Mamba-Adaptor achieves state-of the-art performance on the ImageNet and COCO benchmarks.

