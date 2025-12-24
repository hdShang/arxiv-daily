---
layout: default
title: Pretrained LLMs Learn Multiple Types of Uncertainty
---

# Pretrained LLMs Learn Multiple Types of Uncertainty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21218" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21218v1</a>
  <a href="https://arxiv.org/pdf/2505.21218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21218v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21218v1', 'Pretrained LLMs Learn Multiple Types of Uncertainty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roi Cohen, Omri Fahn, Gerard de Melo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**研究大型语言模型捕捉多种不确定性以提升任务准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `不确定性捕捉` `幻觉现象` `预训练` `指令调优` `信息检索` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型在生成文本时容易出现幻觉，导致不准确的信息输出，影响其在实际应用中的可靠性。
2. 本文提出了一种方法，通过将不确定性视为潜在空间中的线性概念，探索LLMs在预训练阶段如何捕捉多种不确定性。
3. 实验结果表明，模型的修正预测与其避免错误信息的能力存在相关性，并且模型规模对捕捉不确定性没有显著影响。

## 📝 摘要（中文）

大型语言模型（LLMs）因其捕捉现实世界知识的能力而在众多下游任务中表现出色。然而，这些模型仍然容易出现所谓的幻觉现象，导致生成不准确的文本。本文研究了LLMs在未经过显式训练的情况下如何捕捉不确定性。我们发现，如果将不确定性视为模型潜在空间中的线性概念，它实际上可以被捕捉到。尽管这一点不直观，LLMs似乎能够捕捉多种不同类型的不确定性，这对特定任务或基准的正确性预测非常有用。此外，我们提供了深入的结果，展示了修正预测与模型避免错误信息的能力之间的相关性，以及模型规模对捕捉不确定性的影响缺乏显著性。最后，我们认为通过指令调优或[IDK]-token调优将不确定性类型统一为单一类型，有助于模型的正确性预测。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成文本时的幻觉现象，探讨其在未显式训练情况下如何捕捉不确定性，现有方法未能有效利用这一特性。

**核心思路**：通过将不确定性视为模型潜在空间中的线性概念，研究LLMs如何在预训练阶段捕捉多种不确定性类型，以提高其在特定任务中的正确性预测能力。

**技术框架**：研究采用了预训练的LLMs作为基础，分析其在不同任务中的表现，重点关注不确定性类型的捕捉与修正预测的相关性。主要模块包括数据集构建、模型训练、性能评估等。

**关键创新**：本文的创新在于揭示了LLMs能够捕捉多种不确定性类型，并且通过指令调优或[IDK]-token调优将这些不确定性统一为单一类型，从而提升模型的正确性预测能力。

**关键设计**：在实验中，采用了特定的损失函数来优化模型的修正预测能力，同时对模型的规模进行了系统性分析，发现其对捕捉不确定性的影响不显著。

## 📊 实验亮点

实验结果显示，模型在修正预测方面与避免错误信息的能力存在显著相关性。此外，模型规模对捕捉不确定性的影响不显著，表明在优化模型时可以关注其他因素。通过指令调优或[IDK]-token调优，模型的正确性预测能力得到了提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过提高大型语言模型在生成文本时的准确性和可靠性，能够为用户提供更可信的信息，减少误导性内容的传播，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Large Language Models are known to capture real-world knowledge, allowing them to excel in many downstream tasks. Despite recent advances, these models are still prone to what are commonly known as hallucinations, causing them to emit unwanted and factually incorrect text. In this work, we study how well LLMs capture uncertainty, without explicitly being trained for that. We show that, if considering uncertainty as a linear concept in the model's latent space, it might indeed be captured, even after only pretraining. We further show that, though unintuitive, LLMs appear to capture several different types of uncertainty, each of which can be useful to predict the correctness for a specific task or benchmark. Furthermore, we provide in-depth results such as demonstrating a correlation between our correction prediction and the model's ability to abstain from misinformation using words, and the lack of impact of model scaling for capturing uncertainty. Finally, we claim that unifying the uncertainty types as a single one using instruction-tuning or [IDK]-token tuning is helpful for the model in terms of correctness prediction.

