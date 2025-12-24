---
layout: default
title: HAD: Hybrid Architecture Distillation Outperforms Teacher in Genomic Sequence Modeling
---

# HAD: Hybrid Architecture Distillation Outperforms Teacher in Genomic Sequence Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20836" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20836v1</a>
  <a href="https://arxiv.org/pdf/2505.20836.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20836v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20836v1', 'HAD: Hybrid Architecture Distillation Outperforms Teacher in Genomic Sequence Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hexiong Yang, Mingrui Chen, Huaibo Huang, Junxian Duan, Jie Cao, Zhen Zhou, Ran He

**分类**: cs.LG, q-bio.GN

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出混合架构蒸馏方法以提升基因序列建模性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `基因序列建模` `混合架构蒸馏` `自监督学习` `深度学习` `生物信息学`

## 📋 核心要点

1. 现有基因序列建模方法依赖大量预训练数据或大规模模型，计算负担重，效率低下。
2. 提出混合架构蒸馏（HAD）方法，通过蒸馏与重建任务结合，提升预训练效率与效果。
3. 实验结果显示，HAD在Nucleotide Transformer Benchmark和Genomic Benchmark上表现优异，超越了更大模型的性能。

## 📝 摘要（中文）

受掩蔽语言建模（MLM）在自然语言领域成功的启发，自监督预训练和微调的范式在DNA序列建模领域也取得了显著进展。然而，现有方法往往依赖于大量的预训练数据或大规模的基础模型，导致计算负担显著。为了解决这一问题，本文提出了一种混合架构蒸馏（HAD）方法，结合蒸馏和重建任务以实现更高效的预训练。我们使用NTv2-500M作为教师模型，并设计了分组掩蔽策略，以对齐可见标记的特征嵌入，同时在MLM预训练过程中重建不可见标记。实验结果表明，与参数相似的模型相比，我们的方法表现优异，甚至在某些子任务上超越了参数超过500倍的蒸馏教师模型。

## 🔬 方法详解

**问题定义**：本文旨在解决基因序列建模中现有方法对大量预训练数据和大规模模型的依赖，导致的计算负担和效率低下问题。

**核心思路**：提出混合架构蒸馏（HAD）方法，通过结合蒸馏和重建任务，利用更紧凑的模型实现高效的预训练，从而提升模型性能。

**技术框架**：HAD方法的整体架构包括教师模型NTv2-500M、分组掩蔽策略和MLM预训练阶段。教师模型提供知识蒸馏，分组掩蔽策略用于对齐可见标记的特征嵌入，同时重建不可见标记。

**关键创新**：HAD的核心创新在于将蒸馏与重建任务结合，设计分组掩蔽策略，使得模型在预训练过程中能够更有效地学习特征表示，显著提升了模型的表现。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡蒸馏与重建任务的权重，同时优化了网络结构以适应基因序列的特性。

## 📊 实验亮点

实验结果表明，HAD方法在Nucleotide Transformer Benchmark和Genomic Benchmark上表现优异，超越了参数超过500倍的蒸馏教师模型，显示出显著的性能提升，证明了其在基因序列建模中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括基因组学、个性化医疗和生物信息学等。通过提高基因序列建模的效率和准确性，HAD方法能够为基因组数据分析提供更强大的工具，推动相关领域的研究与应用发展。

## 📄 摘要（原文）

> Inspired by the great success of Masked Language Modeling (MLM) in the natural language domain, the paradigm of self-supervised pre-training and fine-tuning has also achieved remarkable progress in the field of DNA sequence modeling. However, previous methods often relied on massive pre-training data or large-scale base models with huge parameters, imposing a significant computational burden. To address this, many works attempted to use more compact models to achieve similar outcomes but still fell short by a considerable margin. In this work, we propose a Hybrid Architecture Distillation (HAD) approach, leveraging both distillation and reconstruction tasks for more efficient and effective pre-training. Specifically, we employ the NTv2-500M as the teacher model and devise a grouping masking strategy to align the feature embeddings of visible tokens while concurrently reconstructing the invisible tokens during MLM pre-training. To validate the effectiveness of our proposed method, we conducted comprehensive experiments on the Nucleotide Transformer Benchmark and Genomic Benchmark. Compared to models with similar parameters, our model achieved excellent performance. More surprisingly, it even surpassed the distillation ceiling-teacher model on some sub-tasks, which is more than 500 $\times$ larger. Lastly, we utilize t-SNE for more intuitive visualization, which shows that our model can gain a sophisticated understanding of the intrinsic representation pattern in genomic sequences.

