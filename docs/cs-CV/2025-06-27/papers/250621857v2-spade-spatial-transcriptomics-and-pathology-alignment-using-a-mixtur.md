---
layout: default
title: "SPADE: Spatial Transcriptomics and Pathology Alignment Using a Mixture of Data Experts for an Expressive Latent Space"
---

# SPADE: Spatial Transcriptomics and Pathology Alignment Using a Mixture of Data Experts for an Expressive Latent Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21857" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21857v2</a>
  <a href="https://arxiv.org/pdf/2506.21857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21857v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21857v2', 'SPADE: Spatial Transcriptomics and Pathology Alignment Using a Mixture of Data Experts for an Expressive Latent Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ekaterina Redekop, Mara Pleasure, Zichen Wang, Kimberly Flores, Anthony Sisk, William Speier, Corey W. Arnold

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-27 (更新: 2025-10-13)

**🔗 代码/项目**: [GITHUB](https://github.com/uclabair/SPADE)

---

## 💡 一句话要点

**提出SPADE以解决病理图像与空间转录组数据整合问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间转录组学` `数字病理学` `多模态融合` `深度学习` `对比学习`

## 📋 核心要点

1. 现有方法在整合全切片图像与空间转录组学数据方面存在显著不足，无法全面捕捉分子异质性。
2. SPADE模型通过混合数据专家技术，将组织病理学与空间转录组学数据整合，创建ST信息驱动的潜在空间。
3. 在20个下游任务中，SPADE模型的少样本性能显著优于基线模型，展示了形态学与分子信息整合的优势。

## 📝 摘要（中文）

随着数字病理学的快速发展和自监督深度学习的进步，基础模型在多种病理任务中得到了应用。然而，现有的多模态方法在整合全切片图像（WSIs）与空间转录组学（ST）方面仍存在显著不足。本文提出SPADE模型，通过将组织病理学与ST数据结合，创建一个ST信息驱动的潜在空间。SPADE采用混合数据专家技术，通过对比学习进行两阶段成像特征空间聚类，学习共同注册的WSI补丁和基因表达谱的表示。经过在HEST-1k数据集上的预训练，SPADE在20个下游任务中表现出显著优于基线模型的少样本性能，突显了将形态学与分子信息整合到一个潜在空间中的优势。

## 🔬 方法详解

**问题定义**：本文旨在解决全切片图像（WSIs）与空间转录组学（ST）数据整合不足的问题。现有方法未能有效捕捉分子异质性，限制了病理学研究的深度和广度。

**核心思路**：SPADE模型通过混合数据专家技术，将组织病理学与ST数据结合，创建一个ST信息驱动的潜在空间。这一设计旨在通过整合多种数据源，提升图像表示学习的效果。

**技术框架**：SPADE的整体架构包括两个主要模块：首先，通过对比学习进行两阶段成像特征空间聚类，生成多个数据专家；其次，利用这些专家学习共同注册的WSI补丁和基因表达谱的表示。

**关键创新**：SPADE的核心创新在于其混合数据专家技术，能够有效整合形态学与分子信息，形成一个更具表现力的潜在空间。这一方法与传统的单一数据源处理方法有本质区别。

**关键设计**：在模型设计中，采用了对比学习作为损失函数，确保不同数据专家之间的有效协作。此外，网络结构经过精心设计，以适应多模态数据的特性，提升了模型的学习能力。

## 📊 实验亮点

SPADE在20个下游任务中的表现显著优于基线模型，尤其在少样本学习场景中，展示了其强大的学习能力和数据整合优势。具体而言，SPADE在这些任务中的性能提升幅度达到了显著的水平，验证了其方法的有效性。

## 🎯 应用场景

SPADE模型在数字病理学和生物医学研究中具有广泛的应用潜力。通过整合形态学与分子信息，SPADE能够帮助研究人员更好地理解疾病的分子机制，推动个性化医疗的发展。此外，该模型的框架可以扩展到其他多模态数据整合任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The rapid growth of digital pathology and advances in self-supervised deep learning have enabled the development of foundational models for various pathology tasks across diverse diseases. While multimodal approaches integrating diverse data sources have emerged, a critical gap remains in the comprehensive integration of whole-slide images (WSIs) with spatial transcriptomics (ST), which is crucial for capturing critical molecular heterogeneity beyond standard hematoxylin & eosin (H&E) staining. We introduce SPADE, a foundation model that integrates histopathology with ST data to guide image representation learning within a unified framework, in effect creating an ST-informed latent space. SPADE leverages a mixture-of-data experts technique, where experts are created via two-stage imaging feature-space clustering using contrastive learning to learn representations of co-registered WSI patches and gene expression profiles. Pre-trained on the comprehensive HEST-1k dataset, SPADE is evaluated on 20 downstream tasks, demonstrating significantly superior few-shot performance compared to baseline models, highlighting the benefits of integrating morphological and molecular information into one latent space. Code and pretrained weights are available at https://github.com/uclabair/SPADE.

