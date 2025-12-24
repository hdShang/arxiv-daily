---
layout: default
title: "KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model"
---

# KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20923" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20923v5</a>
  <a href="https://arxiv.org/pdf/2506.20923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20923v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20923v5', 'KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinping Zhao, Xinshuo Hu, Zifei Shan, Shouzheng Huang, Yao Zhou, Xin Zhang, Zetian Sun, Zhenyu Liu, Dongfang Li, Xinyuan Wei, Youcheng Pan, Yang Xiang, Meishan Zhang, Haofen Wang, Jun Yu, Baotian Hu, Min Zhang

**分类**: cs.CL

**发布日期**: 2025-06-26 (更新: 2025-10-14)

**备注**: 32 pages, 16 tables, 5 figures

---

## 💡 一句话要点

**提出KaLM-Embedding-V2以提升文本嵌入模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本嵌入` `训练技术` `数据质量` `对比蒸馏` `多阶段训练` `高质量数据` `模型微调`

## 📋 核心要点

1. 现有的文本嵌入模型在训练技术和数据质量方面探索不足，限制了其性能提升。
2. 提出KaLM-Embedding-V2，通过优越的训练技术和高质量数据，系统性提升LLMs的嵌入能力。
3. KaLM-Embedding-V2在大规模文本嵌入基准上表现优异，超越同类模型，设定了新的性能标准。

## 📝 摘要（中文）

近年来，基于大型语言模型（LLMs）的文本嵌入模型主要集中在数据扩展或合成上，然而对训练技术和数据质量的探索有限，制约了性能。在本研究中，我们提出了KaLM-Embedding-V2系列多功能紧凑型嵌入模型，通过优越的训练技术和高质量数据系统性地激励LLMs的嵌入能力。我们在0.5B紧凑型模型上实现了简单的均值池化以生成固定长度的嵌入，并移除了因果注意力掩码以实现完全双向表示学习。通过逐步多阶段训练流程，结合任务特定指令和困难样本挖掘，我们的KaLM-Embedding-V2系列在大规模文本嵌入基准上达到了最先进的性能，超越了同类模型，并与3-26倍更大的模型相媲美。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有大型语言模型在文本嵌入任务中训练技术和数据质量不足的问题，这导致模型性能受限。

**核心思路**：论文提出KaLM-Embedding-V2，通过引入先进的训练技术和高质量的数据，系统性地提升嵌入模型的能力，特别是在小型模型中实现高效的表现。

**技术框架**：整体架构包括三个主要阶段：首先在弱监督的大规模数据集上进行预训练，其次在高质量的监督数据集上进行微调，最后通过对比蒸馏和细粒度软信号进行训练，结合焦点式重加权和在线困难负样本混合。

**关键创新**：最重要的创新在于逐步多阶段的训练流程和高质量数据的精心策划，这与现有方法的单一训练阶段和数据质量不足形成鲜明对比。

**关键设计**：模型采用0.5B的紧凑结构，使用简单的均值池化生成固定长度嵌入，移除因果注意力掩码以实现双向学习，同时在数据策划中涵盖超过20个类别用于预训练和100个类别用于微调与对比蒸馏。

## 📊 实验亮点

在实验中，KaLM-Embedding-V2系列在大规模文本嵌入基准上实现了最先进的性能，超越了同类模型，并与3-26倍更大的模型相媲美，设定了新的性能标准，展示了其在紧凑型嵌入模型中的卓越能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、信息检索和推荐系统等。通过提升文本嵌入模型的性能，KaLM-Embedding-V2能够为多种下游任务提供更高质量的特征表示，进而提高系统的整体效果和用户体验。未来，该模型有望在更广泛的应用场景中发挥重要作用。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs)-based text embedding models primarily focus on data scaling or synthesis, yet limited exploration of training techniques and data quality, thereby constraining performance. In this work, we propose KaLM-Embedding-V2, a series of versatile and compact embedding models, systematically incentivizing advanced embedding capability in LLMs by superior training techniques and high-quality data. For model architecture, we implement the models on a 0.5B compact size with simple mean-pooling to produce fixed-length embeddings and remove the causal attention mask to enable fully bidirectional representation learning. For training techniques, we propose a progressive multi-stage training pipeline: pre-training on weakly supervised large-scale datasets, fine-tuning with supervised high-quality datasets, and contrastive distillation with fine-grained soft signals, integrated with focal-style reweighting and online hard-negative mixing to emphasize difficult samples and enrich hard negatives, respectively. For training data, we curate over 20 categories for pre-training and 100 categories for fine-tuning and contrastive distillation, to improve both performance and generalization, leveraging task-specific instructions, hard-negative mining, and example-based multi-class labeling to ensure high quality. Combining these techniques, our KaLM-Embedding-V2 series achieves state-of-the-art performance on the Massive Text Embedding Benchmark, outperforming models of comparable size and rivaling models 3-26x larger, setting a new standard for versatile and compact embedding models under 1B parameters.

