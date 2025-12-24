---
layout: default
title: "Text-to-LoRA: Instant Transformer Adaption"
---

# Text-to-LoRA: Instant Transformer Adaption

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06105" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06105v2</a>
  <a href="https://arxiv.org/pdf/2506.06105.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06105v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06105v2', 'Text-to-LoRA: Instant Transformer Adaption')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rujikorn Charakorn, Edoardo Cetin, Yujin Tang, Robert Tjarko Lange

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-06-09)

**备注**: Accepted at ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/SakanaAI/text-to-lora)

---

## 💡 一句话要点

**提出Text-to-LoRA以解决大语言模型适应性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基础模型` `自然语言处理` `模型适应` `LoRA` `超网络` `零-shot学习` `高效训练`

## 📋 核心要点

1. 现有的基础模型适应方法需要耗时的微调和数据集策划，且对超参数选择极为敏感。
2. 本文提出的Text-to-LoRA模型能够基于自然语言描述即时适应大型语言模型，显著降低计算需求。
3. 实验结果表明，T2L重构的LoRA实例在多个任务上表现优异，并能够进行零-shot泛化。

## 📝 摘要（中文）

基础模型为快速内容创作提供了通用工具，但通常需要针对特定任务的适应。传统方法需要仔细策划数据集和反复微调模型，耗时且对超参数选择敏感。为克服这些局限性，本文提出了Text-to-LoRA（T2L），一种能够基于自然语言描述即时适应大型语言模型的模型。T2L是一个超网络，能够在一次低成本的前向传递中构建LoRA。经过在9个预训练LoRA适配器上的训练，T2L重构的LoRA实例在相应测试集上的表现与任务特定适配器相匹配。此外，T2L能够压缩数百个LoRA实例，并对全新任务进行零-shot泛化。这一方法为基础模型的专业化民主化提供了重要进展。

## 🔬 方法详解

**问题定义**：本文旨在解决基础模型在特定任务适应中的高成本和低效率问题。现有方法依赖于耗时的微调和数据集策划，导致适应过程繁琐且不灵活。

**核心思路**：论文提出的Text-to-LoRA（T2L）模型通过自然语言描述直接生成LoRA适配器，避免了传统微调过程中的复杂性。该模型通过超网络的设计，能够在一次前向传递中构建适配器，极大提高了适应效率。

**技术框架**：T2L的整体架构包括一个超网络，该网络经过训练后能够根据输入的自然语言描述生成相应的LoRA适配器。模型首先接收任务描述，然后通过内部机制生成适配器参数，最后将这些参数应用于大型语言模型。

**关键创新**：T2L的主要创新在于其能够在一次前向传递中生成LoRA适配器，这与传统方法需要多次微调的方式形成鲜明对比。该方法不仅提高了效率，还降低了对计算资源的需求。

**关键设计**：在模型设计中，T2L使用了特定的损失函数来优化生成的LoRA适配器的性能，并通过在多个预训练LoRA适配器上进行训练，确保其能够有效适应多种任务。

## 📊 实验亮点

实验结果显示，T2L生成的LoRA实例在多个任务上与任务特定适配器的性能相当，且在零-shot设置下能够有效适应全新任务。这表明T2L在适应性和效率上具有显著优势。

## 🎯 应用场景

Text-to-LoRA的潜在应用场景包括自然语言处理、对话系统、文本生成等领域。该研究的实际价值在于能够快速适应不同任务，降低了对计算资源的需求，未来可能推动基础模型在更多应用中的普及和使用。

## 📄 摘要（原文）

> While Foundation Models provide a general tool for rapid content creation, they regularly require task-specific adaptation. Traditionally, this exercise involves careful curation of datasets and repeated fine-tuning of the underlying model. Fine-tuning techniques enable practitioners to adapt foundation models for many new applications but require expensive and lengthy training while being notably sensitive to hyperparameter choices. To overcome these limitations, we introduce Text-to-LoRA (T2L), a model capable of adapting large language models (LLMs) on the fly solely based on a natural language description of the target task. T2L is a hypernetwork trained to construct LoRAs in a single inexpensive forward pass. After training T2L on a suite of 9 pre-trained LoRA adapters (GSM8K, Arc, etc.), we show that the ad-hoc reconstructed LoRA instances match the performance of task-specific adapters across the corresponding test sets. Furthermore, T2L can compress hundreds of LoRA instances and zero-shot generalize to entirely unseen tasks. This approach provides a significant step towards democratizing the specialization of foundation models and enables language-based adaptation with minimal compute requirements.
>   Our code is available at https://github.com/SakanaAI/text-to-lora

