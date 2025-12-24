---
layout: default
title: "JTCSE: Joint Tensor-Modulus Constraints and Cross-Attention for Unsupervised Contrastive Learning of Sentence Embeddings"
---

# JTCSE: Joint Tensor-Modulus Constraints and Cross-Attention for Unsupervised Contrastive Learning of Sentence Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02366" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02366v2</a>
  <a href="https://arxiv.org/pdf/2505.02366.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02366v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02366v2', 'JTCSE: Joint Tensor-Modulus Constraints and Cross-Attention for Unsupervised Contrastive Learning of Sentence Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyu Zong, Hongzhu Yi, Bingkang Shi, Yuanxiang Wang, Jungang Xu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-05 (更新: 2025-05-07)

---

## 💡 一句话要点

**提出JTCSE框架以增强无监督对比学习的句子嵌入**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督对比学习` `句子嵌入` `模约束` `交叉注意力` `自然语言处理` `语义相似性` `BERT模型`

## 📋 核心要点

1. 现有无监督对比学习方法忽视了语义表示张量的模特征，导致对比学习效果不足。
2. 本文提出JTCSE框架，通过模约束和交叉注意力结构增强正样本对齐和CLS标记的注意力。
3. 实验结果表明，JTCSE在七个语义文本相似性任务中超越其他基线，并在130多个零样本任务中表现优异。

## 📝 摘要（中文）

无监督对比学习已成为自然语言处理中的热门研究主题。现有方法通常关注于约束正负样本在高维语义空间中的表示方向分布，但忽视了语义表示张量的模特征，导致对比学习效果不足。因此，本文首次提出了一种训练目标，旨在对语义表示张量施加模约束，以增强正样本之间的对齐。同时，针对BERT类模型中CLS标记的注意力不足问题，提出了双塔模型中的交叉注意力结构，以优化CLS池化的质量。结合这两方面，提出了JTCSE框架，并在七个语义文本相似性计算任务中评估，结果显示其双塔集成模型和单塔蒸馏模型在性能上超越其他基线，成为当前的SOTA。此外，JTCSE在130多个零样本下游任务中也表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有无监督对比学习方法中对语义表示张量模特征的忽视，导致正负样本对齐不足的问题。

**核心思路**：提出了一种新的训练目标，通过施加模约束来增强正样本之间的对齐，同时引入交叉注意力结构以优化CLS标记的注意力分配。

**技术框架**：JTCSE框架由双塔模型和交叉注意力结构组成，双塔模型用于生成句子嵌入，交叉注意力模块增强了对CLS标记的关注。

**关键创新**：最重要的创新在于同时考虑模约束和交叉注意力，显著提升了对比学习的效果，与传统方法相比，能够更好地捕捉语义信息。

**关键设计**：在损失函数中引入模约束项，设计了交叉注意力机制以优化CLS池化，确保模型在训练过程中能够有效关注重要的语义信息。

## 📊 实验亮点

实验结果显示，JTCSE的双塔集成模型和单塔蒸馏模型在七个语义文本相似性任务中均超越了其他基线，成为当前的SOTA。此外，在130多个零样本下游任务中，JTCSE整体表现优异，展现出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括文本相似性计算、信息检索和自然语言理解等。通过提升句子嵌入的质量，JTCSE能够为各种下游任务提供更强的支持，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Unsupervised contrastive learning has become a hot research topic in natural language processing. Existing works usually aim at constraining the orientation distribution of the representations of positive and negative samples in the high-dimensional semantic space in contrastive learning, but the semantic representation tensor possesses both modulus and orientation features, and the existing works ignore the modulus feature of the representations and cause insufficient contrastive learning. % Therefore, we firstly propose a training objective that aims at modulus constraints on the semantic representation tensor, to strengthen the alignment between the positive samples in contrastive learning. Therefore, we first propose a training objective that is designed to impose modulus constraints on the semantic representation tensor, to strengthen the alignment between positive samples in contrastive learning. Then, the BERT-like model suffers from the phenomenon of sinking attention, leading to a lack of attention to CLS tokens that aggregate semantic information. In response, we propose a cross-attention structure among the twin-tower ensemble models to enhance the model's attention to CLS token and optimize the quality of CLS Pooling. Combining the above two motivations, we propose a new \textbf{J}oint \textbf{T}ensor representation modulus constraint and \textbf{C}ross-attention unsupervised contrastive learning \textbf{S}entence \textbf{E}mbedding representation framework JTCSE, which we evaluate in seven semantic text similarity computation tasks, and the experimental results show that JTCSE's twin-tower ensemble model and single-tower distillation model outperform the other baselines and become the current SOTA. In addition, we have conducted an extensive zero-shot downstream task evaluation, which shows that JTCSE outperforms other baselines overall on more than 130 tasks.

