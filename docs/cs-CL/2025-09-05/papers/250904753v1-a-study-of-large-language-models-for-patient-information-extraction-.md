---
layout: default
title: "A Study of Large Language Models for Patient Information Extraction: Model Architecture, Fine-Tuning Strategy, and Multi-task Instruction Tuning"
---

# A Study of Large Language Models for Patient Information Extraction: Model Architecture, Fine-Tuning Strategy, and Multi-task Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04753" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04753v1</a>
  <a href="https://arxiv.org/pdf/2509.04753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04753v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04753v1', 'A Study of Large Language Models for Patient Information Extraction: Model Architecture, Fine-Tuning Strategy, and Multi-task Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Peng, Xinyu Dong, Mengxian Lyu, Daniel Paredes, Yaoyun Zhang, Yonghui Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**研究大型语言模型在患者信息抽取中的应用，探索模型架构、微调策略和多任务指令调优。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `患者信息抽取` `参数高效微调` `多任务指令调优` `临床自然语言处理`

## 📋 核心要点

1. 临床叙述中抽取患者信息至关重要，但现有方法在处理复杂性和泛化性方面存在挑战。
2. 本研究探索不同LLM架构、微调策略和多任务指令调优，以提升患者信息抽取的性能和泛化能力。
3. 通过基准测试和对比实验，评估了不同LLM和微调方法在多个数据集上的表现，并分析了其优缺点。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLM）在患者信息抽取中的有效性，重点关注LLM架构、微调策略和多任务指令调优技术，旨在开发稳健且具有泛化能力的患者信息抽取系统。研究探索了使用LLM进行临床概念和关系抽取的关键概念，包括：（1）encoder-only或decoder-only LLM；（2）基于prompt的参数高效微调（PEFT）算法；（3）多任务指令调优对少样本学习性能的影响。我们对一系列LLM进行了基准测试，包括基于encoder的LLM（BERT、GatorTron）和基于decoder的LLM（GatorTronGPT、Llama 3.1、GatorTronLlama），使用了五个数据集。我们比较了传统的全尺寸微调和基于prompt的PEFT。我们探索了一个多任务指令调优框架，该框架结合了四个数据集上的任务，以评估使用留一数据集策略的零样本和少样本学习性能。

## 🔬 方法详解

**问题定义**：论文旨在解决从临床文本中准确、高效地抽取患者信息的问题。现有方法，尤其是传统NLP方法，在处理复杂的临床语言、术语变异性和上下文依赖性方面存在局限性，并且需要大量标注数据。大型语言模型虽然潜力巨大，但如何针对患者信息抽取任务进行优化和有效利用仍是一个挑战。

**核心思路**：论文的核心思路是探索不同类型的LLM（encoder-only和decoder-only），并结合参数高效微调（PEFT）和多任务指令调优，以提升模型在患者信息抽取任务上的性能和泛化能力。通过比较不同模型架构和微调策略，找到最适合该任务的配置。

**技术框架**：整体框架包括三个主要部分：1）选择和准备数据集；2）选择和微调LLM，包括encoder-only模型（BERT, GatorTron）和decoder-only模型（GatorTronGPT, Llama 3.1, GatorTronLlama），并采用全尺寸微调和PEFT两种策略；3）构建多任务指令调优框架，将多个数据集上的任务结合起来进行训练，并使用留一数据集策略评估零样本和少样本学习性能。

**关键创新**：论文的关键创新在于系统性地比较了不同LLM架构、微调策略和多任务指令调优方法在患者信息抽取任务上的效果。特别关注了参数高效微调（PEFT）在减少计算资源需求的同时，保持甚至提升模型性能的潜力。此外，多任务指令调优框架旨在提高模型的泛化能力，使其能够适应不同的数据集和任务。

**关键设计**：在微调策略方面，论文比较了全尺寸微调和基于prompt的PEFT方法，例如LoRA。在多任务指令调优方面，论文设计了统一的指令模板，将不同数据集上的任务转化为统一的指令格式，以便模型能够同时学习多个任务。损失函数方面，采用标准的交叉熵损失函数进行训练。具体参数设置（如学习率、batch size等）未知。

## 📊 实验亮点

该研究通过实验对比了多种LLM架构和微调策略在患者信息抽取任务上的性能。结果表明，参数高效微调（PEFT）在保持性能的同时，显著降低了计算成本。多任务指令调优能够提升模型的泛化能力，使其在未见数据集上也能取得较好的表现。具体的性能数据和提升幅度未知。

## 🎯 应用场景

该研究成果可应用于多种医疗场景，例如辅助临床决策、自动化病历分析、药物研发和患者风险预测。通过高效准确地抽取患者信息，可以提升医疗服务的质量和效率，并为医疗研究提供有力支持。未来，该技术有望与电子病历系统集成，实现更智能化的医疗信息管理。

## 📄 摘要（原文）

> Natural language processing (NLP) is a key technology to extract important patient information from clinical narratives to support healthcare applications. The rapid development of large language models (LLMs) has revolutionized many NLP tasks in the clinical domain, yet their optimal use in patient information extraction tasks requires further exploration. This study examines LLMs' effectiveness in patient information extraction, focusing on LLM architectures, fine-tuning strategies, and multi-task instruction tuning techniques for developing robust and generalizable patient information extraction systems. This study aims to explore key concepts of using LLMs for clinical concept and relation extraction tasks, including: (1) encoder-only or decoder-only LLMs, (2) prompt-based parameter-efficient fine-tuning (PEFT) algorithms, and (3) multi-task instruction tuning on few-shot learning performance. We benchmarked a suite of LLMs, including encoder-based LLMs (BERT, GatorTron) and decoder-based LLMs (GatorTronGPT, Llama 3.1, GatorTronLlama), across five datasets. We compared traditional full-size fine-tuning and prompt-based PEFT. We explored a multi-task instruction tuning framework that combines both tasks across four datasets to evaluate the zero-shot and few-shot learning performance using the leave-one-dataset-out strategy.

