---
layout: default
title: "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models"
---

# Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05176" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05176v3</a>
  <a href="https://arxiv.org/pdf/2506.05176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05176v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05176v3', 'Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang, Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, Fei Huang, Jingren Zhou

**分类**: cs.CL

**发布日期**: 2025-06-05 (更新: 2025-06-11)

---

## 💡 一句话要点

**提出Qwen3嵌入以提升文本嵌入和重排序能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本嵌入` `重排序` `多语言处理` `无监督学习` `监督微调` `模型合并` `基础模型`

## 📋 核心要点

1. 现有文本嵌入和重排序方法在多语言理解和生成能力上存在不足，难以满足多样化的应用需求。
2. 论文提出的Qwen3嵌入系列通过多阶段训练流程，结合无监督预训练和监督微调，提升了模型的鲁棒性和适应性。
3. 实验结果显示，Qwen3嵌入系列在多项基准测试中实现了最先进的性能，特别是在多语言评估和检索任务中表现突出。

## 📝 摘要（中文）

本文介绍了Qwen3嵌入系列，相较于其前身GTE-Qwen系列在文本嵌入和重排序能力上有显著进展。该系列基于Qwen3基础模型，利用其在多语言文本理解和生成方面的强大能力，采用创新的多阶段训练流程，结合大规模无监督预训练与高质量数据集的监督微调。有效的模型合并策略进一步确保了Qwen3嵌入系列的鲁棒性和适应性。Qwen3嵌入系列提供多种模型规模（0.6B、4B、8B），适用于不同的部署场景，用户可根据效率或效果进行优化。实证评估表明，该系列在多项基准测试中取得了领先的结果，尤其在多语言评估基准MTEB和各种检索任务中表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文本嵌入和重排序方法在多语言处理中的不足，尤其是对多样化数据和任务的适应性差的问题。

**核心思路**：论文提出的Qwen3嵌入系列通过创新的多阶段训练流程，结合大规模无监督预训练与高质量数据集的监督微调，旨在提升模型的性能和适应性。

**技术框架**：整体架构包括多个阶段：首先进行大规模无监督预训练，然后在高质量数据集上进行监督微调，最后通过模型合并策略增强模型的鲁棒性。

**关键创新**：最重要的技术创新在于利用Qwen3 LLMs作为基础模型，不仅提供强大的文本理解能力，还能合成高质量的多样化训练数据，显著提升训练效果。

**关键设计**：在模型设计中，采用了不同规模的模型（0.6B、4B、8B），并通过有效的损失函数和网络结构设计，确保在不同任务中的高效性和有效性。

## 📊 实验亮点

实验结果表明，Qwen3嵌入系列在多项基准测试中取得了领先的性能，特别是在多语言评估基准MTEB上表现优异，显著优于现有基线，提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

Qwen3嵌入系列可广泛应用于多语言文本处理、信息检索、推荐系统等领域，具有重要的实际价值。其灵活的模型规模和高效的性能使其适合于不同的应用场景，推动了相关领域的研究与发展。

## 📄 摘要（原文）

> In this work, we introduce the Qwen3 Embedding series, a significant advancement over its predecessor, the GTE-Qwen series, in text embedding and reranking capabilities, built upon the Qwen3 foundation models. Leveraging the Qwen3 LLMs' robust capabilities in multilingual text understanding and generation, our innovative multi-stage training pipeline combines large-scale unsupervised pre-training with supervised fine-tuning on high-quality datasets. Effective model merging strategies further ensure the robustness and adaptability of the Qwen3 Embedding series. During the training process, the Qwen3 LLMs serve not only as backbone models but also play a crucial role in synthesizing high-quality, rich, and diverse training data across multiple domains and languages, thus enhancing the training pipeline. The Qwen3 Embedding series offers a spectrum of model sizes (0.6B, 4B, 8B) for both embedding and reranking tasks, addressing diverse deployment scenarios where users can optimize for either efficiency or effectiveness. Empirical evaluations demonstrate that the Qwen3 Embedding series achieves state-of-the-art results across diverse benchmarks. Notably, it excels on the multilingual evaluation benchmark MTEB for text embedding, as well as in various retrieval tasks, including code retrieval, cross-lingual retrieval and multilingual retrieval. To facilitate reproducibility and promote community-driven research and development, the Qwen3 Embedding models are publicly available under the Apache 2.0 license.

