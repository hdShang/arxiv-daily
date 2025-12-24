---
layout: default
title: "Two-Stage Reasoning-Infused Learning: Improving Classification with LLM-Generated Reasoning"
---

# Two-Stage Reasoning-Infused Learning: Improving Classification with LLM-Generated Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00214" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00214v1</a>
  <a href="https://arxiv.org/pdf/2507.00214.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00214v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00214v1', 'Two-Stage Reasoning-Infused Learning: Improving Classification with LLM-Generated Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mads Henrichsen, Rasmus Krebs

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出两阶段推理增强学习以提升文本分类性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本分类` `推理生成` `大型语言模型` `情感分析` `自然语言处理` `模型训练` `数据增强`

## 📋 核心要点

1. 现有分类模型缺乏明确的推理过程，可能导致性能和可解释性不足。
2. 提出的两阶段方法通过LLM生成推理，增强训练数据集，从而提升分类效果。
3. 在情感分类实验中，使用新方法的模型准确率提高了8.7个百分点，显示出显著的性能提升。

## 📝 摘要（中文）

标准分类模型通常直接将输入映射到标签，缺乏明确的推理过程，可能限制其性能、鲁棒性和可解释性。本文提出了一种新颖的两阶段方法，通过利用大型语言模型（LLM）生成的推理来增强文本分类。在第一阶段，我们对Llama-3.2-1B-Instruct模型进行微调，以生成给定问题及其答案的文本推理。在第二阶段，利用经过训练的模型生成增强的训练数据集，以训练下游生成模型。实验表明，该方法在情感分类任务中显著提高了8.7个百分点的准确率，强调了推理生成的强泛化能力及其在下游NLP任务中的潜在价值。

## 🔬 方法详解

**问题定义**：本文旨在解决标准分类模型缺乏推理过程的问题，这种缺陷可能影响模型的性能和可解释性。现有方法通常直接将输入映射到标签，未能充分利用推理信息。

**核心思路**：论文提出的两阶段方法通过利用大型语言模型生成的推理文本，增强训练数据集，从而提高下游模型的分类能力。第一阶段生成推理，第二阶段将推理与输入结合进行训练。

**技术框架**：整体架构分为两个主要阶段：第一阶段是对Llama-3.2-1B-Instruct模型进行微调，以生成文本推理；第二阶段使用生成的推理创建增强的训练数据集，并训练下游生成模型。

**关键创新**：最重要的创新在于将推理生成与情感分类结合，显著提升了模型的准确性。这与传统方法的直接标签映射形成鲜明对比，强调了推理在分类任务中的重要性。

**关键设计**：在模型训练中，采用特定的损失函数来优化推理生成和情感预测的联合输出，确保生成的推理与情感标签的相关性。同时，使用了增强的训练数据集以提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，使用新方法训练的生成模型在情感预测任务中准确率提高了8.7个百分点，相较于仅输出情感的基线模型，展现了显著的性能提升。这一结果突显了推理生成在增强模型能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括情感分析、问答系统和其他自然语言处理任务。通过生成推理，模型不仅能够提供更准确的分类结果，还能增强其可解释性，帮助用户理解模型决策的依据。未来，该方法有望在更多NLP任务中推广应用，提升模型的整体性能。

## 📄 摘要（原文）

> Standard classification models often map inputs directly to labels without explicit reasoning, potentially limiting their performance, robustness, and interpretability. This paper introduces a novel two-stage approach to enhance text classification by leveraging Large Language Model (LLM)-generated reasonings. In the first stage, we fine-tune a Llama-3.2-1B-Instruct model (henceforth Llama-R-Gen) on a general-purpose reasoning dataset (syvai/reasoning-gen) to generate textual reasoning (R) given a question and its answer. In the second stage, this generally trained Llama-R-Gen is used offline to create an augmented training dataset for a downstream generative model. This downstream model, based on Llama-3.2-1B-Instruct, takes only the input text (Q) and is trained to output the generated reasoning (R) immediately followed by the predicted emotion (A). We demonstrate this methodology on the dair-ai/emotion dataset for emotion classification. Our experiments show that the generative model trained to output reasoning and the emotion (Classifier Q->RA) achieves a significant improvement of 8.7 percentage points in accuracy (for emotion prediction) compared to a baseline generative model trained solely to output the emotion (Classifier Q->A), highlighting the strong generalization capabilities of the reasoning generation and the benefit of explicit reasoning training. This work underscores the potential of LLM-generated reasonings for creating richer training datasets, thereby improving the performance of diverse downstream NLP tasks and providing explicit explanations.

