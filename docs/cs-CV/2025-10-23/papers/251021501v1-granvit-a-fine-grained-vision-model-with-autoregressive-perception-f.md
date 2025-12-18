---
layout: default
title: GranViT: A Fine-Grained Vision Model With Autoregressive Perception For MLLMs
---

# GranViT: A Fine-Grained Vision Model With Autoregressive Perception For MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21501" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21501v1</a>
  <a href="https://arxiv.org/pdf/2510.21501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21501v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21501v1', 'GranViT: A Fine-Grained Vision Model With Autoregressive Perception For MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanghao Zheng, Bowen Shi, Mingxing Xu, Ruoyu Sun, Peisen Zhao, Zhibo Zhang, Wenrui Dai, Junni Zou, Hongkai Xiong, Xiaopeng Zhang, Qi Tian

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23

**备注**: 21 pages, 6 figures

---

## 💡 一句话要点

**GranViT：面向MLLM的细粒度视觉模型，通过自回归感知提升性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度视觉模型` `视觉Transformer` `多模态大语言模型` `自回归训练` `区域级标注` `视觉问答` `OCR理解`

## 📋 核心要点

1. 现有视觉编码器侧重于全局图像表示，忽略了细粒度的区域分析，限制了多模态大语言模型在视觉语言任务中的性能。
2. GranViT通过区域级别的自回归训练，将细粒度特征提取与大型语言模型的语义对齐，从而提升视觉编码器的细粒度感知能力。
3. GranViT在细粒度识别、多模态VQA和OCR理解方面取得了最先进的结果，证明了其优越的性能和强大的可迁移性。

## 📝 摘要（中文）

本文提出GranViT，一种新型Vision Transformer，它集成了细粒度特征提取和与大型语言模型（LLM）的语义对齐，通过区域级别的自回归训练实现。为了进行大规模的细粒度预训练，我们构建了一个包含200万张自然图像和OCR图像的数据集Gran-29M，并配有超过1.8亿个高质量的区域级标注。我们开发了一个预训练-适应框架，以及一个自蒸馏机制，以在Gran-29M上训练细粒度的GranViT。我们充分利用Gran-29M中的细粒度标注，采用bounding-box到caption的回归来增强视觉编码器在预训练中的局部视觉表示，并采用caption到bounding-box的回归来提高LLM在适应过程中的视觉特征利用率和定位能力。我们进一步结合自蒸馏机制，对视觉编码器施加显式的定位约束，以增强其区域推理能力。大量实验表明，GranViT超越了现有的视觉编码器，并在不同的LLM上实现了强大的可迁移性。值得注意的是，它在细粒度识别、多模态VQA和OCR理解方面取得了最先进的结果。

## 🔬 方法详解

**问题定义**：现有的视觉编码器在处理视觉问答和推理等视觉语言任务时，由于缺乏对图像细粒度区域的分析能力，导致性能受限。主要痛点在于缺乏足够规模的细粒度标注数据以及相应的预训练范式。

**核心思路**：GranViT的核心思路是通过构建大规模的细粒度标注数据集，并结合区域级别的自回归训练，来提升视觉编码器对图像细粒度区域的感知和理解能力。通过预训练和适应阶段的bounding-box和caption之间的回归，实现视觉特征的精确定位和语义对齐。

**技术框架**：GranViT的整体框架包含以下几个主要模块：1) 大规模细粒度标注数据集Gran-29M的构建；2) 基于Gran-29M的预训练阶段，利用bounding-box到caption的回归增强局部视觉表示；3) 适应阶段，利用caption到bounding-box的回归提升LLM的视觉特征利用率和定位能力；4) 自蒸馏机制，通过显式的定位约束增强区域推理能力。

**关键创新**：GranViT的关键创新在于：1) 构建了大规模的细粒度标注数据集Gran-29M，为细粒度视觉模型的训练提供了数据基础；2) 提出了区域级别的自回归训练方法，通过bounding-box和caption之间的回归，实现了视觉特征的精确定位和语义对齐；3) 引入了自蒸馏机制，通过显式的定位约束增强了模型的区域推理能力。与现有方法的本质区别在于，GranViT更加关注图像的细粒度区域信息，并将其与大型语言模型进行有效对齐。

**关键设计**：GranViT的关键设计包括：1) Gran-29M数据集的构建，包含200万张图像和1.8亿个区域级标注；2) 预训练阶段采用bounding-box到caption的回归损失函数，优化视觉编码器的局部视觉表示；3) 适应阶段采用caption到bounding-box的回归损失函数，优化LLM的视觉特征利用率和定位能力；4) 自蒸馏机制中，通过引入额外的定位约束损失函数，增强模型的区域推理能力。

## 📊 实验亮点

GranViT在细粒度识别、多模态VQA和OCR理解等任务上取得了显著的性能提升，超越了现有的视觉编码器。具体而言，在多个benchmark数据集上实现了state-of-the-art的结果，证明了其优越的性能和强大的可迁移性。实验结果表明，GranViT能够有效地提取图像的细粒度特征，并将其与大型语言模型进行有效对齐，从而提升了视觉语言模型的整体性能。

## 🎯 应用场景

GranViT在多模态大语言模型中具有广泛的应用前景，可以应用于视觉问答、图像描述、目标检测、OCR识别等领域。该研究的实际价值在于提升了视觉语言模型的细粒度感知能力，使其能够更好地理解图像内容，从而提高各种视觉语言任务的性能。未来，GranViT可以进一步扩展到其他视觉语言任务中，并与其他模态的信息进行融合，实现更强大的多模态理解能力。

## 📄 摘要（原文）

> Vision encoders are indispensable for allowing impressive performance of Multi-modal Large Language Models (MLLMs) in vision language tasks such as visual question answering and reasoning. However, existing vision encoders focus on global image representations but overlook fine-grained regional analysis. They are limited in fine grained perception due to the scarcity of fine grained annotated data and the lack of a fine grained pre-training paradigm. In this paper, we propose GranViT, a novel Vision Transformer that integrates fine-grained feature extraction with semantic alignment to Large Language Models (LLMs) via region level autoregressive training. We first construct Gran-29M, a dataset comprising 2million natural and OCR images paired with over 180 million high-quality region-level annotations, to enable large scale fine grained pretraining. Consequently, we develop a pretraining-adaptation framework along with a self distillation mechanism to train fine-grained GranViT on Gran-29M. We sufficiently exploit the fine-grained annotations from Gran-29M to resort to bounding-box-to-caption regression to enhance localized visual representation of the vision encoder in the pretraining and caption-to-bounding-box regression to improve vision feature utilization and localization for LLM in the adaptation. We further incorporate a self distillation mechanism that imposes explicit localization constraints on the vision encoder to strengthen its regional reasoning capability. Extensive experiments show that GranViT surpasses existing vision encoders and attains strong transferability to varying LLMs. Remarkably, it achieves state-of-the-art results on fine-grained recognition, multimodal VQA, and OCR understanding.

