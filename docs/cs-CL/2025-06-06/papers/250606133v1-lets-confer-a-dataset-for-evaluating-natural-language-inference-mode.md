---
layout: default
title: "Let's CONFER: A Dataset for Evaluating Natural Language Inference Models on CONditional InFERence and Presupposition"
---

# Let's CONFER: A Dataset for Evaluating Natural Language Inference Models on CONditional InFERence and Presupposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06133" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06133v1</a>
  <a href="https://arxiv.org/pdf/2506.06133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06133v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06133v1', 'Let\'s CONFER: A Dataset for Evaluating Natural Language Inference Models on CONditional InFERence and Presupposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tara Azin, Daniel Dumitrescu, Diana Inkpen, Raj Singh

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: This paper is published in the Proceedings of the 38th Canadian Conference on Artificial Intelligence (CAIAC 2025). Please cite the conference version at https://caiac.pubpub.org/pub/keh8ij01

---

## 💡 一句话要点

**提出CONFER数据集以评估NLI模型在条件推理中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言推理` `条件推理` `预设推理` `数据集构建` `大型语言模型`

## 📋 核心要点

1. 现有的NLI模型在处理条件句中的预设推理时表现不佳，尤其是在细粒度的语用推理方面。
2. 本研究提出了CONFER数据集，专门设计用于评估NLI模型在条件句推理中的能力，填补了这一研究空白。
3. 实验结果显示，NLI模型在条件句的预设推理上存在显著困难，微调现有数据集未能有效提升性能。

## 📝 摘要（中文）

自然语言推理（NLI）任务旨在判断句子对之间的蕴含、矛盾或中立关系。尽管现有NLI模型在许多推理任务上表现良好，但它们在处理细粒度的语用推理，特别是条件句中的预设方面仍然不足。本研究引入了CONFER，一个新颖的数据集，旨在评估NLI模型如何处理条件句中的推理。我们评估了四个NLI模型的性能，包括两个预训练模型，以检验它们在条件推理上的泛化能力。此外，我们还在零-shot和few-shot提示设置下评估了大型语言模型（LLMs），如GPT-4o、LLaMA、Gemma和DeepSeek-R1，分析它们在有无上下文的情况下推断预设的能力。研究结果表明，NLI模型在条件句中的预设推理上存在困难，且在现有NLI数据集上进行微调并不一定能提高其性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有NLI模型在条件句中的预设推理能力不足的问题。现有方法在处理细粒度的语用推理时，尤其是条件句中的预设，表现不佳，缺乏有效的评估标准。

**核心思路**：论文提出了CONFER数据集，专注于条件句的推理评估，旨在通过这一新数据集来测试和提升NLI模型的推理能力。通过对比不同模型在该数据集上的表现，研究其在条件推理中的泛化能力。

**技术框架**：整体架构包括数据集构建、模型选择与评估。首先构建CONFER数据集，然后选择四个NLI模型进行评估，最后分析大型语言模型在零-shot和few-shot设置下的表现。

**关键创新**：CONFER数据集是首个专门针对条件句中的预设推理进行评估的数据集，填补了现有研究的空白。与传统NLI数据集相比，CONFER更关注细粒度的语用推理，提供了新的评估标准。

**关键设计**：在模型评估中，采用了多种大型语言模型，并在不同的提示设置下进行测试。关键参数包括模型的预训练状态、提示方式以及评估指标的选择，确保了实验的全面性和准确性。

## 📊 实验亮点

实验结果表明，NLI模型在条件句的预设推理上存在显著困难，尤其是在缺乏上下文的情况下。微调现有NLI数据集未能有效提升模型性能，显示出该领域的研究仍需深入探索。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的推理系统、对话系统以及智能问答等。CONFER数据集的引入为评估和改进NLI模型在复杂语境下的推理能力提供了新的工具，未来可能推动更智能的语言理解系统的发展。

## 📄 摘要（原文）

> Natural Language Inference (NLI) is the task of determining whether a sentence pair represents entailment, contradiction, or a neutral relationship. While NLI models perform well on many inference tasks, their ability to handle fine-grained pragmatic inferences, particularly presupposition in conditionals, remains underexplored. In this study, we introduce CONFER, a novel dataset designed to evaluate how NLI models process inference in conditional sentences. We assess the performance of four NLI models, including two pre-trained models, to examine their generalization to conditional reasoning. Additionally, we evaluate Large Language Models (LLMs), including GPT-4o, LLaMA, Gemma, and DeepSeek-R1, in zero-shot and few-shot prompting settings to analyze their ability to infer presuppositions with and without prior context. Our findings indicate that NLI models struggle with presuppositional reasoning in conditionals, and fine-tuning on existing NLI datasets does not necessarily improve their performance.

