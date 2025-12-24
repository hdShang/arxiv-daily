---
layout: default
title: "Negative Matters: Multi-Granularity Hard-Negative Synthesis and Anchor-Token-Aware Pooling for Enhanced Text Embeddings"
---

# Negative Matters: Multi-Granularity Hard-Negative Synthesis and Anchor-Token-Aware Pooling for Enhanced Text Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00842" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00842v1</a>
  <a href="https://arxiv.org/pdf/2509.00842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00842v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00842v1', 'Negative Matters: Multi-Granularity Hard-Negative Synthesis and Anchor-Token-Aware Pooling for Enhanced Text Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tengyu Pan, Zhichao Duan, Zhenyu Li, Bowen Dong, Ning Liu, Xiuxing Li, Jianyong Wang

**分类**: cs.CL

**发布日期**: 2025-08-31

**DOI**: [10.18653/v1/2025.acl-long.1501](https://doi.org/10.18653/v1/2025.acl-long.1501)

---

## 💡 一句话要点

**提出多粒度硬负样本合成与锚标记感知池化以提升文本嵌入**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本嵌入` `对比学习` `负样本生成` `多粒度合成` `锚标记感知池化` `自然语言处理` `语义表示`

## 📋 核心要点

1. 现有文本嵌入模型在负样本生成方面存在不足，难以有效区分细微的语义差异。
2. 提出多粒度硬负样本合成框架，利用大型语言模型生成多样化负样本，并引入锚标记感知池化方法以提升嵌入准确性。
3. 在MTEB基准测试中，所提方法表现优异，超越了现有合成策略，展示了显著的性能提升。

## 📝 摘要（中文）

文本嵌入模型在自然语言处理任务中至关重要，能够有效地将语义信息编码为稠密的向量表示。现有模型通常使用（查询、正样本、负样本）三元组进行对比学习，其中负样本在增强模型区分细微语义差异的能力方面起着关键作用。本文提出了一种多粒度硬负样本（MGH）合成框架，利用大型语言模型（LLMs）生成具有不同相似度的多样化负样本，促进了监督训练中的粗到细的课程学习策略。同时，我们提出了一种锚标记感知（ATA）池化方法，根据LLMs中观察到的聚合模式为锚标记分配更高的权重，从而在不增加模型复杂度的情况下提高文本嵌入的准确性。综合实验结果表明，我们的方法在MTEB基准测试中实现了最先进的性能，超越了现有的合成策略。

## 🔬 方法详解

**问题定义**：本文旨在解决文本嵌入模型在对比学习中负样本生成的不足，现有方法往往无法有效捕捉细微的语义差异，导致模型性能受限。

**核心思路**：通过引入多粒度硬负样本合成框架，利用大型语言模型生成不同相似度的负样本，结合锚标记感知池化方法，提升模型的语义表示能力。

**技术框架**：整体架构包括两个主要模块：多粒度硬负样本合成模块和锚标记感知池化模块。前者负责生成多样化的负样本，后者则通过加权聚合提升嵌入准确性。

**关键创新**：最重要的创新在于多粒度硬负样本合成框架的提出，利用LLMs生成的负样本具有更高的多样性和相似度层次，显著提升了模型的学习能力。

**关键设计**：在参数设置上，锚标记的权重根据聚合模式动态调整，损失函数设计为对比损失，确保模型在训练过程中能够有效学习到细微的语义差异。

## 📊 实验亮点

实验结果表明，所提方法在MTEB基准测试中实现了最先进的性能，相较于现有合成策略，提升幅度达到XX%，在合成数据和公共检索数据集上均表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括文本分类、信息检索和对话系统等自然语言处理任务。通过提升文本嵌入的准确性，能够显著改善模型在实际应用中的表现，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Text embedding models are essential for various natural language processing tasks, enabling the effective encoding of semantic information into dense vector representations. These models are typically optimized using triplets of (query, positive, negative) data pairs for contrastive learning, where the negative samples play a critical role in enhancing the model's ability to discern subtle semantic distinctions. In this work, we introduce a Multi-Granularity Hard-negative (MGH) synthesis framework that leverages large language models (LLMs) to generate diverse negative samples with varying levels of similarity with the query. This approach facilitates a coarse-to-fine curriculum learning strategy during supervised training, allowing the embedding model to progressively learn more nuanced semantic representations. Meanwhile, we propose an Anchor Token Aware (ATA) pooling method that assigns higher weights to anchor tokens based on aggregation patterns observed in LLMs, improving text embedding accuracy without increasing model complexity. Comprehensive experiments on the MTEB benchmark demonstrate that our methods achieve state-of-the-art performance, surpassing existing synthesis strategies both with synthetic data and when combined with public retrieval datasets.

