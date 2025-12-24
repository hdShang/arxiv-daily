---
layout: default
title: "BrainMT: A Hybrid Mamba-Transformer Architecture for Modeling Long-Range Dependencies in Functional MRI Data"
---

# BrainMT: A Hybrid Mamba-Transformer Architecture for Modeling Long-Range Dependencies in Functional MRI Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22591" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22591v1</a>
  <a href="https://arxiv.org/pdf/2506.22591.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22591v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22591v1', 'BrainMT: A Hybrid Mamba-Transformer Architecture for Modeling Long-Range Dependencies in Functional MRI Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arunkumar Kannan, Martin A. Lindquist, Brian Caffo

**分类**: cs.CV

**发布日期**: 2025-06-27

**备注**: Accepted at MICCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/arunkumar-kannan/BrainMT-fMRI)

---

## 💡 一句话要点

**提出BrainMT以解决fMRI数据长程依赖建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `功能性磁共振成像` `深度学习` `长程依赖` `时空特征` `神经影像学` `混合架构` `自注意力机制`

## 📋 核心要点

1. 现有方法在处理fMRI数据时，难以捕捉长程空间和时间依赖性，导致建模效果不佳。
2. BrainMT框架通过双向Mamba模块和变换器模块的结合，有效整合长程时空特征，提升建模能力。
3. 在UKBioBank和人类连接组项目数据集上，BrainMT在分类和回归任务中均表现出色，超越了现有技术。

## 📝 摘要（中文）

近年来，深度学习的进步使得直接从功能性磁共振成像（fMRI）脑体积预测表型指标成为可能，激发了神经影像学界的广泛关注。然而，现有方法主要基于卷积神经网络或变换器架构，往往难以建模fMRI数据中固有的复杂关系，尤其是在捕捉长程空间和时间依赖性方面存在局限。为了解决这些问题，本文提出了BrainMT，一个新颖的混合框架，旨在有效学习和整合fMRI数据中的长程时空属性。通过在UKBioBank和人类连接组项目等两个大型公共数据集上的广泛实验，BrainMT在性别预测和认知智能预测任务上均达到了最先进的性能，显著超越了现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有fMRI数据分析方法在捕捉长程空间和时间依赖性方面的不足，导致建模效果不理想的问题。

**核心思路**：BrainMT框架结合了Mamba模块和变换器模块，前者通过时间优先的扫描机制捕捉全局时间交互，后者利用自注意力机制建模全局空间关系，从而有效整合时空特征。

**技术框架**：BrainMT的整体架构分为两个主要阶段：第一阶段是双向Mamba模块，专注于时间维度的特征提取；第二阶段是变换器模块，处理Mamba模块输出的深层特征以捕捉空间关系。

**关键创新**：BrainMT的核心创新在于其混合架构设计，能够同时高效捕捉长程时空依赖性，区别于传统的卷积或单一变换器方法。

**关键设计**：在设计中，Mamba模块采用了时间优先的扫描机制，变换器模块则利用自注意力机制，确保了全局特征的有效整合，具体的参数设置和损失函数将在公开代码中详细说明。

## 📊 实验亮点

BrainMT在UKBioBank和人类连接组项目数据集上的实验结果显示，其在性别预测和认知智能预测任务中均达到了最先进的性能，相较于现有方法，分类任务的准确率提升了显著的幅度，验证了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学研究、临床诊断和个性化医疗等。通过准确建模fMRI数据，BrainMT有助于深入理解脑功能和结构之间的关系，推动神经影像学的发展，并可能在认知障碍和精神疾病的早期诊断中发挥重要作用。

## 📄 摘要（原文）

> Recent advances in deep learning have made it possible to predict phenotypic measures directly from functional magnetic resonance imaging (fMRI) brain volumes, sparking significant interest in the neuroimaging community. However, existing approaches, primarily based on convolutional neural networks or transformer architectures, often struggle to model the complex relationships inherent in fMRI data, limited by their inability to capture long-range spatial and temporal dependencies. To overcome these shortcomings, we introduce BrainMT, a novel hybrid framework designed to efficiently learn and integrate long-range spatiotemporal attributes in fMRI data. Our framework operates in two stages: (1) a bidirectional Mamba block with a temporal-first scanning mechanism to capture global temporal interactions in a computationally efficient manner; and (2) a transformer block leveraging self-attention to model global spatial relationships across the deep features processed by the Mamba block. Extensive experiments on two large-scale public datasets, UKBioBank and the Human Connectome Project, demonstrate that BrainMT achieves state-of-the-art performance on both classification (sex prediction) and regression (cognitive intelligence prediction) tasks, outperforming existing methods by a significant margin. Our code and implementation details will be made publicly available at this https://github.com/arunkumar-kannan/BrainMT-fMRI

