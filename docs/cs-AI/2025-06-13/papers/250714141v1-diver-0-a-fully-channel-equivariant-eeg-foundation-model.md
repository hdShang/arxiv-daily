---
layout: default
title: "DIVER-0 : A Fully Channel Equivariant EEG Foundation Model"
---

# DIVER-0 : A Fully Channel Equivariant EEG Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.14141" class="toolbar-btn" target="_blank">📄 arXiv: 2507.14141v1</a>
  <a href="https://arxiv.org/pdf/2507.14141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.14141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.14141v1', 'DIVER-0 : A Fully Channel Equivariant EEG Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danny Dongyeop Han, Ahhyun Lucy Lee, Taeyang Lee, Yonghyeon Gwon, Sebin Lee, Seongjin Lee, David Keetae Park, Shinjae Yoo, Jiook Cha, Chun Kee Chung

**分类**: eess.SP, cs.AI, cs.LG

**发布日期**: 2025-06-13

**备注**: 11 pages, 1 figures, ICML 2025 Workshop on GenBio

---

## 💡 一句话要点

**提出DIVER-0以解决EEG模型通道等变性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑电图` `时空动态建模` `通道置换等变性` `全时空注意力` `滑动时间条件位置编码` `跨数据集泛化` `神经科学` `脑机接口`

## 📋 核心要点

1. 现有EEG基础模型在时空动态建模和通道置换等变性方面存在不足，限制了其在多样电极配置中的鲁棒性。
2. DIVER-0通过全时空注意力机制和滑动时间条件位置编码（STCPE）来解决这些问题，确保模型在不同电极配置下的适应性。
3. 实验结果显示，DIVER-0在仅使用10%预训练数据的情况下，仍能在多种通道置换条件下保持一致的性能，验证了其跨数据集泛化能力。

## 📝 摘要（中文）

脑电图（EEG）是一种广泛应用于脑机接口和临床应用的非侵入性技术，但现有EEG基础模型在建模时空脑动态方面存在局限性，并且缺乏通道置换等变性，导致在不同电极配置下的鲁棒性不足。为了解决这些挑战，本文提出了DIVER-0，一个新颖的EEG基础模型，展示了如何通过全时空注意力而非分离的空间或时间处理，结合旋转位置嵌入（RoPE）和二元注意力偏置，来实现优越的性能。同时，我们引入了滑动时间条件位置编码（STCPE），该方法在保持时间平移等变性和通道置换等变性的同时，能够有效适应在预训练期间未见过的任意电极配置。实验结果表明，DIVER-0在仅使用10%的预训练数据的情况下，仍能在所有通道置换条件下保持一致的结果，验证了其在跨数据集泛化方面的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有EEG基础模型在时空动态建模和通道置换等变性方面的不足，导致其在不同电极配置下的鲁棒性不足。

**核心思路**：DIVER-0通过全时空注意力机制而非分离的空间或时间处理来提升模型性能，同时结合旋转位置嵌入（RoPE）和二元注意力偏置，确保模型能够有效捕捉时间关系和通道差异。

**技术框架**：DIVER-0的整体架构包括全时空注意力模块、旋转位置嵌入和滑动时间条件位置编码（STCPE），这些模块共同作用以实现对时空动态的全面建模。

**关键创新**：DIVER-0的主要创新在于引入了STCPE，该方法在保持时间平移等变性和通道置换等变性的同时，显著提升了模型的适应性和泛化能力。

**关键设计**：在设计中，DIVER-0采用了旋转位置嵌入（RoPE）来处理时间关系，并通过二元注意力偏置来区分不同通道，确保模型在多样电极配置下的鲁棒性。实验中使用的损失函数和网络结构经过精心设计，以优化模型性能。

## 📊 实验亮点

实验结果表明，DIVER-0在仅使用10%预训练数据的情况下，仍能在所有通道置换条件下保持一致的性能，验证了其在跨数据集泛化方面的有效性。这一成果相较于现有模型表现出显著的提升，展示了其在EEG研究中的应用前景。

## 🎯 应用场景

DIVER-0模型在脑机接口、神经科学研究及临床诊断等领域具有广泛的应用潜力。其强大的跨数据集泛化能力使得该模型能够适应不同的电极配置，从而提升脑电图分析的准确性和可靠性，推动相关技术的发展。

## 📄 摘要（原文）

> Electroencephalography (EEG) is a non-invasive technique widely used in brain-computer interfaces and clinical applications, yet existing EEG foundation models face limitations in modeling spatio-temporal brain dynamics and lack channel permutation equivariance, preventing robust generalization across diverse electrode configurations. To address these challenges, we propose DIVER-0, a novel EEG foundation model that demonstrates how full spatio-temporal attention-rather than segregated spatial or temporal processing-achieves superior performance when properly designed with Rotary Position Embedding (RoPE) for temporal relationships and binary attention biases for channel differentiation. We also introduce Sliding Temporal Conditional Positional Encoding (STCPE), which improves upon existing conditional positional encoding approaches by maintaining both temporal translation equivariance and channel permutation equivariance, enabling robust adaptation to arbitrary electrode configurations unseen during pretraining. Experimental results demonstrate that DIVER-0 achieves competitive performance with only 10% of pretraining data while maintaining consistent results across all channel permutation conditions, validating its effectiveness for cross-dataset generalization and establishing key design principles for handling the inherent heterogeneity of neural recording setups.

