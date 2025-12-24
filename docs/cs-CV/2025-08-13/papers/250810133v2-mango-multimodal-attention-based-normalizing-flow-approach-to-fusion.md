---
layout: default
title: "MANGO: Multimodal Attention-based Normalizing Flow Approach to Fusion Learning"
---

# MANGO: Multimodal Attention-based Normalizing Flow Approach to Fusion Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10133" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10133v2</a>
  <a href="https://arxiv.org/pdf/2508.10133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10133v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10133v2', 'MANGO: Multimodal Attention-based Normalizing Flow Approach to Fusion Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thanh-Dat Truong, Christophe Bobda, Nitin Agarwal, Khoa Luu

**分类**: cs.CV

**发布日期**: 2025-08-13 (更新: 2025-11-25)

**备注**: Accepted to NeurIPS'25

---

## 💡 一句话要点

**提出MANGO方法以解决多模态融合学习的特征捕捉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `注意力机制` `归一化流` `特征捕捉` `深度学习`

## 📋 核心要点

1. 现有多模态融合方法无法有效捕捉各模态的核心特征，导致对复杂结构和模态间关联的理解困难。
2. 本文提出了多模态注意力归一化流（MANGO）方法，利用可逆交叉注意力层和新型交叉注意力机制来增强特征捕捉能力。
3. 在语义分割、图像到图像转换和电影类型分类等任务中，MANGO展示了最先进的性能，显著提升了融合学习的效果。

## 📝 摘要（中文）

多模态学习近年来取得了显著成功，但现有的融合方法主要依赖于Transformer的注意力机制，无法有效捕捉各模态的核心特征，导致对复杂结构和模态间关联的理解困难。本文提出了一种新颖的多模态注意力归一化流（MANGO）方法，旨在实现明确、可解释和可处理的多模态融合学习。我们引入了可逆交叉注意力（ICA）层，并提出了三种新的交叉注意力机制，以高效捕捉多模态数据中的复杂关联。实验结果表明，MANGO在语义分割、图像到图像转换和电影类型分类等任务上表现出色，达到了当前最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态融合学习方法无法有效捕捉各模态核心特征的问题，导致对复杂结构和模态间关联的理解不足。

**核心思路**：提出多模态注意力归一化流（MANGO）方法，通过引入可逆交叉注意力层和三种新型交叉注意力机制，显著提升多模态数据的特征捕捉能力。

**技术框架**：MANGO的整体架构包括可逆交叉注意力层、模态间交叉注意力机制（MMCA、IMCA、LICA）和归一化流模型，旨在实现高效的多模态融合。

**关键创新**：最重要的创新点在于引入了可逆交叉注意力层和三种新型交叉注意力机制，使得模型能够明确捕捉模态间的复杂关联，区别于传统的隐式学习方法。

**关键设计**：在设计中，关注了交叉注意力机制的参数设置和损失函数的选择，以确保模型在高维多模态数据上的可扩展性和有效性。

## 📊 实验亮点

实验结果表明，MANGO在语义分割、图像到图像转换和电影类型分类任务上均达到了最先进的性能，相较于基线方法，性能提升幅度显著，具体提升数据未知。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和多模态数据分析等。MANGO方法能够有效提升多模态学习的性能，具有广泛的实际价值，未来可能推动智能系统在复杂任务中的应用，如自动驾驶、智能监控和人机交互等。

## 📄 摘要（原文）

> Multimodal learning has gained much success in recent years. However, current multimodal fusion methods adopt the attention mechanism of Transformers to implicitly learn the underlying correlation of multimodal features. As a result, the multimodal model cannot capture the essential features of each modality, making it difficult to comprehend complex structures and correlations of multimodal inputs. This paper introduces a novel Multimodal Attention-based Normalizing Flow (MANGO) approach to developing explicit, interpretable, and tractable multimodal fusion learning. In particular, we propose a new Invertible Cross-Attention (ICA) layer to develop the Normalizing Flow-based Model for multimodal data. To efficiently capture the complex, underlying correlations in multimodal data in our proposed invertible cross-attention layer, we propose three new cross-attention mechanisms: Modality-to-Modality Cross-Attention (MMCA), Inter-Modality Cross-Attention (IMCA), and Learnable Inter-Modality Cross-Attention (LICA). Finally, we introduce a new Multimodal Attention-based Normalizing Flow to enable the scalability of our proposed method to high-dimensional multimodal data. Our experimental results on three different multimodal learning tasks, i.e., semantic segmentation, image-to-image translation, and movie genre classification, have illustrated the state-of-the-art (SoTA) performance of the proposed approach.

