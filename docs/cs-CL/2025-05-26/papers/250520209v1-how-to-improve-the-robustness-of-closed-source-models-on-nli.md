---
layout: default
title: How to Improve the Robustness of Closed-Source Models on NLI
---

# How to Improve the Robustness of Closed-Source Models on NLI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20209" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20209v1</a>
  <a href="https://arxiv.org/pdf/2505.20209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20209v1', 'How to Improve the Robustness of Closed-Source Models on NLI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joe Stacey, Lisa Alazraki, Aran Ubhi, Beyza Ermis, Aaron Mueller, Marek Rei

**分类**: cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出数据中心方法以提升闭源模型在NLI任务中的鲁棒性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `闭源模型` `鲁棒性提升` `自然语言推理` `数据中心方法` `大型语言模型`

## 📋 核心要点

1. 现有方法在提升闭源模型鲁棒性时面临挑战，通常需要访问模型内部或修改训练过程。
2. 本文提出通过数据中心的方法来提升闭源LLMs的鲁棒性，避免对模型内部的依赖。
3. 实验结果显示，针对复杂OOD数据集，增加挑战性训练样本可提升鲁棒性1.5%；而简单数据集用LLM生成样本替换可提升3.7%。

## 📝 摘要（中文）

闭源的大型语言模型（LLMs）在自然语言任务中表现出色，但在处理分布外（OOD）数据时鲁棒性不足。现有方法往往依赖于对模型内部的访问或训练过程的修改，无法适用于闭源模型。本文探讨了无需访问模型内部的基于数据的方法来提升闭源LLMs的鲁棒性。研究发现，针对复杂的OOD数据集，通过增加更具挑战性的训练样本可以提升鲁棒性1.5%；而对于较简单的OOD数据集，用LLM生成的样本替换部分训练集则可提升鲁棒性3.7%。此外，研究表明，闭源自回归LLMs的鲁棒性显著优于常用的编码器模型，未来应作为基准选择。

## 🔬 方法详解

**问题定义**：本文旨在解决闭源大型语言模型在处理分布外（OOD）数据时鲁棒性不足的问题。现有方法通常依赖于对模型内部的访问或修改训练过程，导致无法应用于闭源模型。

**核心思路**：论文提出了一种数据中心的方法，通过调整训练数据集来提升模型的鲁棒性，而不需要对模型内部进行修改。这种方法的设计基于对OOD数据复杂性的分析。

**技术框架**：整体架构包括数据集的分析、样本选择和生成策略。首先，评估OOD数据集的复杂性，然后根据复杂性选择合适的训练样本调整策略。

**关键创新**：最重要的创新在于提出了针对不同复杂性OOD数据集的特定策略，尤其是通过增加挑战性样本或用生成样本替换训练集的方式，显著提升了闭源模型的鲁棒性。

**关键设计**：在实验中，针对复杂数据集采用了上采样策略，而对于简单数据集则使用了LLM生成样本替换的策略。具体的参数设置和损失函数设计未在摘要中详细说明，需参考论文的完整内容。

## 📊 实验亮点

实验结果表明，针对复杂的OOD数据集，通过增加挑战性训练样本，模型鲁棒性提升了1.5%；而在处理简单OOD数据集时，用LLM生成的样本替换部分训练集，鲁棒性提升达3.7%。此外，闭源自回归LLMs的鲁棒性显著优于传统编码器模型，显示出其作为基准选择的潜力。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理中的各种任务，如文本分类、情感分析和对话系统等。通过提升闭源模型的鲁棒性，可以在实际应用中更好地处理多样化和复杂的输入数据，从而提高系统的可靠性和用户体验。未来，这一方法可能推动更多闭源模型在实际应用中的广泛使用。

## 📄 摘要（原文）

> Closed-source Large Language Models (LLMs) have become increasingly popular, with impressive performance across a wide range of natural language tasks. These models can be fine-tuned to further improve performance, but this often results in the models learning from dataset-specific heuristics that reduce their robustness on out-of-distribution (OOD) data. Existing methods to improve robustness either perform poorly, or are non-applicable to closed-source models because they assume access to model internals, or the ability to change the model's training procedure. In this work, we investigate strategies to improve the robustness of closed-source LLMs through data-centric methods that do not require access to model internals. We find that the optimal strategy depends on the complexity of the OOD data. For highly complex OOD datasets, upsampling more challenging training examples can improve robustness by up to 1.5%. For less complex OOD datasets, replacing a portion of the training set with LLM-generated examples can improve robustness by 3.7%. More broadly, we find that large-scale closed-source autoregressive LLMs are substantially more robust than commonly used encoder models, and are a more appropriate choice of baseline going forward.

