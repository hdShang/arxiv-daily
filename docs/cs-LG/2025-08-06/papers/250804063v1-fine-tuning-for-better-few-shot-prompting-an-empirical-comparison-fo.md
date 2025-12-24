---
layout: default
title: "Fine-tuning for Better Few Shot Prompting: An Empirical Comparison for Short Answer Grading"
---

# Fine-tuning for Better Few Shot Prompting: An Empirical Comparison for Short Answer Grading

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04063" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04063v1</a>
  <a href="https://arxiv.org/pdf/2508.04063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04063v1', 'Fine-tuning for Better Few Shot Prompting: An Empirical Comparison for Short Answer Grading')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joel Walsh, Siddarth Mamidanna, Benjamin Nye, Mark Core, Daniel Auerbach

**分类**: cs.LG

**发布日期**: 2025-08-06

**备注**: Proceedings of the Second Workshop on Automated Evaluation of Learning and Assessment Content co-located with 26th International Conference on Artificial Intelligence in Education (AIED 2025)

---

## 💡 一句话要点

**提出微调方法以改善少量样本提示的短答案评分**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动评分` `短答案评分` `微调方法` `少量样本学习` `大型语言模型` `合成数据生成` `教育技术`

## 📋 核心要点

1. 现有的自动短答案评分方法在使用大型语言模型时，往往依赖于大量计算资源和数据，限制了其普适性。
2. 论文提出了两种微调方法，旨在通过少量样本提示改善短答案评分的效果，尤其是在资源受限的情况下。
3. 实验结果显示，微调方法在OpenAI的封闭模型上表现优于少量样本基线，而对Llama开放权重模型的效用有限。

## 📝 摘要（中文）

近期关于自动短答案评分的研究集中在使用大型语言模型（LLMs）进行提示工程和少量样本提示，以实现最佳结果。这与传统的微调方法形成对比，后者通常需要大型计算集群。新兴的封闭模型方法如OpenAI的微调服务承诺在仅有100个示例的情况下取得结果，而使用开放权重的量化低秩自适应（QLORA）方法则可以在消费者GPU上微调模型。我们评估了这两种微调方法，测量它们与少量样本提示在自动短答案评分中的交互。结果表明，使用少量数据的微调对Llama开放权重模型的效用有限，但对于OpenAI的封闭模型，微调方法可以超越少量样本基线。尽管我们的评估集有限，但我们发现微调的好处可能受到领域主题的影响。最后，我们观察到通过用大量廉价生成的合成训练数据来初始化训练示例，LLama 3.1 8B-Instruct开放权重模型的表现显著提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何在资源有限的情况下，利用少量样本提示和微调方法来提升自动短答案评分的效果。现有方法往往需要大量数据和计算资源，限制了其应用范围。

**核心思路**：论文的核心思路是评估不同微调方法在少量样本提示下的表现，特别是对比封闭模型和开放权重模型的效果。通过微调，模型能够更好地适应特定领域的任务，从而提高评分准确性。

**技术框架**：整体架构包括数据准备、模型微调和性能评估三个主要阶段。首先，收集少量样本数据并生成合成数据；其次，应用微调方法对模型进行训练；最后，使用结构化输出评估模型在短答案评分任务中的表现。

**关键创新**：最重要的技术创新点在于通过微调方法在少量样本情况下提升模型性能，尤其是在OpenAI的封闭模型上表现优于传统的少量样本提示方法。与现有方法相比，微调能够更有效地利用有限的数据资源。

**关键设计**：在微调过程中，关键设计包括选择合适的损失函数和优化算法，以及如何生成合成训练数据以增强模型的学习能力。这些设计决定了模型在特定任务上的适应性和表现。

## 📊 实验亮点

实验结果表明，微调方法在OpenAI的封闭模型上超越了少量样本基线，显示出显著的性能提升。尤其是LLama 3.1 8B-Instruct开放权重模型，通过使用大量合成训练数据，表现出显著的改进，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线学习平台和自动评分系统。通过提升短答案评分的准确性，能够为教师和学生提供更高效的反馈机制，促进个性化学习。此外，微调方法的灵活性使其适用于多种领域的文本处理任务，具有广泛的实际价值。

## 📄 摘要（原文）

> Research to improve Automated Short Answer Grading has recently focused on Large Language Models (LLMs) with prompt engineering and no- or few-shot prompting to achieve best results. This is in contrast to the fine-tuning approach, which has historically required large-scale compute clusters inaccessible to most users. New closed-model approaches such as OpenAI's fine-tuning service promise results with as few as 100 examples, while methods using open weights such as quantized low-rank adaptive (QLORA) can be used to fine-tune models on consumer GPUs. We evaluate both of these fine-tuning methods, measuring their interaction with few-shot prompting for automated short answer grading (ASAG) with structured (JSON) outputs. Our results show that finetuning with small amounts of data has limited utility for Llama open-weight models, but that fine-tuning methods can outperform few-shot baseline instruction-tuned LLMs for OpenAI's closed models. While our evaluation set is limited, we find some evidence that the observed benefits of finetuning may be impacted by the domain subject matter. Lastly, we observed dramatic improvement with the LLama 3.1 8B-Instruct open-weight model by seeding the initial training examples with a significant amount of cheaply generated synthetic training data.

