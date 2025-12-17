---
layout: default
title: EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment
---

# EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14019" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14019v1</a>
  <a href="https://arxiv.org/pdf/2512.14019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14019v1" onclick="toggleFavorite(this, '2512.14019v1', 'EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juseung Yun, Sunwoo Yu, Sumin Ha, Jonghyun Kim, Janghyeon Lee, Jongseong Jang, Soonyoung Lee

**分类**: cs.LG, q-bio.QM

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出EXAONE Path 2.5以解决多层次肿瘤生物学建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理模型` `多模态学习` `精准肿瘤学` `生物信息整合` `对比学习` `空间结构保留` `基因组学` `转录组学`

## 📋 核心要点

1. 现有方法主要集中于单一模态，无法全面反映肿瘤生物学的复杂性，导致信息的丢失和模型的局限性。
2. 提出EXAONE Path 2.5，通过联合建模多种生物模态，利用多模态SigLIP损失和F-RoPE模块，增强模型对肿瘤生物学的理解。
3. 在Patho-Bench基准测试中，EXAONE Path 2.5与六个领先模型相比，表现出相当的性能，同时在内部临床数据集上展现出更高的适应性。

## 📝 摘要（中文）

癌症进展源于多个生物层次之间的相互作用，尤其是超越形态学的分子层面。为捕捉这一更广泛的生物景观，本文提出EXAONE Path 2.5，这是一个病理基础模型，联合建模组织学、基因组、表观遗传学和转录组等多种模态，生成更全面的患者表征。该方法包含三大核心组件：多模态SigLIP损失、保留空间结构的片段感知旋转位置编码模块（F-RoPE），以及针对WSI和RNA-seq的领域专用基础模型。通过对比六个领先的病理基础模型，EXAONE Path 2.5在内部临床数据集和Patho-Bench基准上展示了高数据和参数效率，表现出与最先进模型相当的性能，并在内部临床环境中展现出最高的适应性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有病理模型在多层次生物信息整合方面的不足，尤其是无法有效结合形态学与分子层次的信息。

**核心思路**：通过联合建模组织学、基因组、表观遗传学和转录组等多种模态，EXAONE Path 2.5能够生成更全面的患者表征，从而更好地反映肿瘤生物学。

**技术框架**：该模型的整体架构包括多模态SigLIP损失、F-RoPE模块和领域专用基础模型，确保不同模态之间的有效对齐与信息整合。

**关键创新**：最重要的创新在于引入了多模态SigLIP损失和F-RoPE模块，使得模型能够在多种生物模态之间进行有效的对比学习和空间结构保留，显著提升了模型的表现。

**关键设计**：在损失函数方面，采用了多模态SigLIP损失以实现全对比学习；F-RoPE模块则通过旋转位置编码保留了组织切片的空间结构，确保了信息的完整性与准确性。

## 📊 实验亮点

在Patho-Bench基准测试中，EXAONE Path 2.5与六个领先的病理基础模型相比，表现出相当的性能，且在内部临床数据集上展现出最高的适应性，证明了其在数据和参数效率上的优势。

## 🎯 应用场景

EXAONE Path 2.5模型在精准肿瘤学中具有广泛的应用潜力，能够为个体化治疗提供更为全面的生物学依据。通过整合多种生物模态，该模型有助于更好地理解肿瘤的发生发展机制，从而推动新疗法的研发与临床应用。

## 📄 摘要（原文）

> Cancer progression arises from interactions across multiple biological layers, especially beyond morphological and across molecular layers that remain invisible to image-only models. To capture this broader biological landscape, we present EXAONE Path 2.5, a pathology foundation model that jointly models histologic, genomic, epigenetic and transcriptomic modalities, producing an integrated patient representation that reflects tumor biology more comprehensively. Our approach incorporates three key components: (1) multimodal SigLIP loss enabling all-pairwise contrastive learning across heterogeneous modalities, (2) a fragment-aware rotary positional encoding (F-RoPE) module that preserves spatial structure and tissue-fragment topology in WSI, and (3) domain-specialized internal foundation models for both WSI and RNA-seq to provide biologically grounded embeddings for robust multimodal alignment. We evaluate EXAONE Path 2.5 against six leading pathology foundation models across two complementary benchmarks: an internal real-world clinical dataset and the Patho-Bench benchmark covering 80 tasks. Our framework demonstrates high data and parameter efficiency, achieving on-par performance with state-of-the-art foundation models on Patho-Bench while exhibiting the highest adaptability in the internal clinical setting. These results highlight the value of biologically informed multimodal design and underscore the potential of integrated genotype-to-phenotype modeling for next-generation precision oncology.

