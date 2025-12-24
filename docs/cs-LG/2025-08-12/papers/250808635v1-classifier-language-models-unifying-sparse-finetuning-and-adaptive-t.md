---
layout: default
title: "Classifier Language Models: Unifying Sparse Finetuning and Adaptive Tokenization for Specialized Classification Tasks"
---

# Classifier Language Models: Unifying Sparse Finetuning and Adaptive Tokenization for Specialized Classification Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08635" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08635v1</a>
  <a href="https://arxiv.org/pdf/2508.08635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08635v1', 'Classifier Language Models: Unifying Sparse Finetuning and Adaptive Tokenization for Specialized Classification Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adit Krishnan, Chu Wang, Chris Kong

**分类**: cs.LG

**发布日期**: 2025-08-12

**备注**: 10 pages, 4 figures, currently under review

---

## 💡 一句话要点

**提出稀疏微调与自适应标记化结合的方法以解决专业分类任务问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义文本分类` `稀疏微调` `小型语言模型` `专业分类任务` `模型优化` `推理速度` `领域专家标注`

## 📋 核心要点

1. 现有的语义分类方法往往依赖于领域专家的标注，且推理速度慢，限制了模型的应用。
2. 本文提出了一种稀疏微调策略，通过标记驱动的方式适应小型语言模型，避免了引入额外参数。
3. 实验结果表明，该方法在多个分类任务上表现优异，训练成本仅为传统方法的一半，且稳定性更高。

## 📝 摘要（中文）

语义文本分类需要理解特定标记的上下文意义，而不仅仅是表面模式或关键词，这使得大型语言模型（LLMs）非常适合此任务。然而，行业中的语义分类应用通常高度专业化，需要领域专家进行标注，并且通常要求高推理吞吐量，从而限制了模型的规模。为此，本文提出了一种基于标记驱动的稀疏微调策略，旨在将小型语言模型适应于专业分类任务。通过利用任务特定的标记构造，识别并微调模型参数的敏感子集，同时保持大部分预训练权重不变。实验结果显示，该方法在五个不同的语义分类任务上超越了端到端微调、LoRA、层选择和前缀调优，且训练成本降低了一半。

## 🔬 方法详解

**问题定义**：本文旨在解决语义文本分类中现有方法的不足，尤其是在专业领域中对模型大小和推理速度的要求。现有方法往往需要大量的领域专家标注，并且推理速度较慢，限制了其实际应用。

**核心思路**：论文提出了一种基于标记驱动的稀疏微调策略，专注于微调小型语言模型的敏感参数，而不改变大部分预训练权重。这种方法通过识别与任务相关的语义标记来优化模型性能。

**技术框架**：整体架构包括数据预处理、标记识别、参数微调和模型评估四个主要模块。首先，通过分析任务特定的数据集，识别出关键的语义标记；然后，针对这些标记微调模型的相关参数，最后进行模型的性能评估。

**关键创新**：该方法的创新在于不引入额外的参数，而是通过稀疏微调现有模型的敏感参数来实现性能提升。这与传统的适配器方法（如LoRA）形成鲜明对比。

**关键设计**：在微调过程中，采用了特定的损失函数来优化与任务相关的参数，同时保持大部分预训练权重不变。模型结构上，选择了小型语言模型作为基础，确保在推理速度和成本上具有优势。

## 📊 实验亮点

实验结果显示，提出的方法在五个不同的语义分类任务上均优于传统的端到端微调、LoRA、层选择和前缀调优，训练成本降低至一半，且模型稳定性显著提高，展示了其在专业分类任务中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括客户意图检测、语义角色标注等专业分类任务，能够有效提高模型在特定领域的性能和效率。未来，该方法有望在更多行业中推广，帮助企业快速适应市场变化，提升服务质量。

## 📄 摘要（原文）

> Semantic text classification requires the understanding of the contextual significance of specific tokens rather than surface-level patterns or keywords (as in rule-based or statistical text classification), making large language models (LLMs) well-suited for this task. However, semantic classification applications in industry, like customer intent detection or semantic role labeling, tend to be highly specialized. They require annotation by domain experts in contrast to general-purpose corpora for pretraining. Further, they typically require high inference throughputs which limits the model size from latency and cost perspectives. Thus, for a range of specialized classification tasks, the preferred solution is to develop customized classifiers by finetuning smaller language models (e.g., mini-encoders, small language models).
>   In this work, we develop a token-driven sparse finetuning strategy to adapt small language models to specialized classification tasks. We identify and finetune a small sensitive subset of model parameters by leveraging task-specific token constructs in the finetuning dataset, while leaving most of the pretrained weights unchanged. Unlike adapter approaches such as low rank adaptation (LoRA), we do not introduce additional parameters to the model. Our approach identifies highly relevant semantic tokens (case study in the Appendix) and outperforms end-to-end finetuning, LoRA, layer selection, and prefix tuning on five diverse semantic classification tasks. We achieve greater stability and half the training costs vs. end-to-end finetuning.

