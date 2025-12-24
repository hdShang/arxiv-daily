---
layout: default
title: "You Only Fine-tune Once: Many-Shot In-Context Fine-Tuning for Large Language Model"
---

# You Only Fine-tune Once: Many-Shot In-Context Fine-Tuning for Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11103" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11103v1</a>
  <a href="https://arxiv.org/pdf/2506.11103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11103v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11103v1', 'You Only Fine-tune Once: Many-Shot In-Context Fine-Tuning for Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenchong He, Liqian Peng, Zhe Jiang, Alex Go

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**提出ManyICL以解决大语言模型微调效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `上下文学习` `微调方法` `自然语言处理` `机器学习`

## 📋 核心要点

1. 现有的少量上下文微调方法在性能上仍然落后于专门微调，无法充分利用大语言模型的潜力。
2. 本文提出ManyICL方法，通过将每个上下文答案视为监督目标，提升了多样本微调的效率。
3. 实验结果显示，ManyICL在多个下游任务上显著优于零/少量微调，接近专门微调的性能，并减轻了灾难性遗忘问题。

## 📝 摘要（中文）

大语言模型（LLMs）具备出色的上下文学习（ICL）能力，能够同时处理多个下游任务而无需特定任务的微调。然而，现有的少量上下文微调方法仍然不及专门微调的效果。本文提出了一种新方法Many-Shot In-Context Fine-tuning（ManyICL），通过将ICL扩展到多样本设置，显著缩小了这一性能差距。我们提出了一种新训练目标，将上下文中的每个答案视为监督学习的目标，从而有效提升了模型的学习效率。实验结果表明，ManyICL在分类、摘要、问答等多种任务上表现优异，接近专门微调的效果，并显著减轻了灾难性遗忘问题。

## 🔬 方法详解

**问题定义**：本文旨在解决现有少量上下文微调方法在性能和效率上的不足，尤其是在处理长序列和多个上下文示例时的低效问题。

**核心思路**：ManyICL方法通过将上下文中的每个答案视为监督学习目标，改变了传统的微调方式，使得多样本示例不仅作为提示，还作为自回归学习的目标，从而提升了模型的学习效果。

**技术框架**：该方法的整体架构包括数据准备、上下文构建、训练目标定义和模型训练四个主要模块。数据准备阶段收集多样本数据，构建上下文后进行训练。

**关键创新**：ManyICL的核心创新在于将每个上下文答案视为训练目标，这一设计与传统方法的本质区别在于提升了模型对多样本的学习能力，缩小了与专门微调的性能差距。

**关键设计**：在训练过程中，采用新的损失函数来优化每个上下文答案的预测，确保模型能够有效学习到多样本信息。此外，模型架构保持了自回归特性，以适应新的训练目标。

## 📊 实验亮点

实验结果表明，ManyICL在分类、摘要、问答等任务上显著优于传统的零/少量微调方法，性能接近专门微调的模型。例如，在某些任务上，ManyICL的准确率提升幅度达到10%以上，且有效减轻了灾难性遗忘问题，展现出更好的模型稳定性和泛化能力。

## 🎯 应用场景

ManyICL方法在自然语言处理领域具有广泛的应用潜力，包括文本分类、摘要生成、问答系统和自然语言推理等。其高效的微调方式能够帮助研究人员和开发者更快速地适应不同任务，提升模型的实用性和灵活性。未来，该方法可能推动更多领域的智能应用，提升人机交互的自然性和智能化水平。

## 📄 摘要（原文）

> Large language models (LLMs) possess a remarkable ability to perform in-context learning (ICL), which enables them to handle multiple downstream tasks simultaneously without requiring task-specific fine-tuning. Recent studies have shown that even moderately sized LLMs, such as Mistral 7B, Gemma 7B and Llama-3 8B, can achieve ICL through few-shot in-context fine-tuning of all tasks at once. However, this approach still lags behind dedicated fine-tuning, where a separate model is trained for each individual task.
>   In this paper, we propose a novel approach, Many-Shot In-Context Fine-tuning (ManyICL), which significantly narrows this performance gap by extending the principles of ICL to a many-shot setting. To unlock the full potential of ManyICL and address the inherent inefficiency of processing long sequences with numerous in-context examples, we propose a novel training objective. Instead of solely predicting the final answer, our approach treats every answer within the context as a supervised training target. This effectively shifts the role of many-shot examples from prompts to targets for autoregressive learning. Through extensive experiments on diverse downstream tasks, including classification, summarization, question answering, natural language inference, and math, we demonstrate that ManyICL substantially outperforms zero/few-shot fine-tuning and approaches the performance of dedicated fine-tuning. Furthermore, ManyICL significantly mitigates catastrophic forgetting issues observed in zero/few-shot fine-tuning. The code will be made publicly available upon publication.

