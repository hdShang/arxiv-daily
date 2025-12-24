---
layout: default
title: "NeuralNexus at BEA 2025 Shared Task: Retrieval-Augmented Prompting for Mistake Identification in AI Tutors"
---

# NeuralNexus at BEA 2025 Shared Task: Retrieval-Augmented Prompting for Mistake Identification in AI Tutors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10627" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10627v1</a>
  <a href="https://arxiv.org/pdf/2506.10627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10627v1', 'NeuralNexus at BEA 2025 Shared Task: Retrieval-Augmented Prompting for Mistake Identification in AI Tutors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Numaan Naeem, Sarfraz Ahmad, Momina Ahsan, Hasan Iqbal

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-12

**备注**: 6 pages, 2 figures, 1 table

**🔗 代码/项目**: [GITHUB](https://github.com/NaumanNaeem/BEA_2025)

---

## 💡 一句话要点

**提出基于检索增强提示的AI辅导员错误识别系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `错误识别` `AI辅导员` `检索增强` `提示系统` `教育技术` `机器学习`

## 📋 核心要点

1. 核心问题：现有方法在识别学生数学推理错误时的准确性和解释性不足。
2. 方法要点：提出了基于检索增强的提示系统，结合多个模型和LLM进行错误识别。
3. 实验或效果：最终系统在所有基线测试中表现优异，展示了显著的性能提升。

## 📝 摘要（中文）

本文展示了我们在BEA 2025共享任务中针对AI辅导员错误识别的系统。该任务评估辅导员的回答是否正确识别学生在数学推理中的错误。我们探索了四种方法：1) 基于多个预训练语言模型的机器学习模型集成；2) 使用句子变换器的冻结模型与多层感知机分类器；3) 具有多头注意力的历史感知模型；4) 基于检索增强的少量提示系统，利用大型语言模型（如GPT-4o）。最终系统通过检索语义相似的示例，构建结构化提示，并使用模式引导的输出解析生成可解释的预测，超越所有基线，展示了示例驱动提示与LLM推理结合在教育反馈评估中的有效性。代码可在https://github.com/NaumanNaeem/BEA_2025获取。

## 🔬 方法详解

**问题定义**：本文旨在解决AI辅导员在识别学生数学推理错误时的准确性和解释性不足的问题。现有方法往往无法有效捕捉学生的推理过程，导致错误识别。

**核心思路**：论文提出了一种基于检索增强的提示系统，结合多种模型的优点，通过检索语义相似的示例来构建提示，从而提高错误识别的准确性和可解释性。

**技术框架**：整体架构包括四个主要模块：1) 机器学习模型集成；2) 冻结的句子变换器与MLP分类器；3) 历史感知模型；4) 检索增强的少量提示系统。系统通过检索相关示例，生成结构化提示，并进行输出解析。

**关键创新**：最重要的创新在于结合了示例驱动的提示与大型语言模型的推理能力，显著提升了错误识别的效果。与传统方法相比，该方法在处理复杂推理时表现更佳。

**关键设计**：在模型设计中，使用了多种预训练语言模型的嵌入，采用了多头注意力机制来处理历史信息，并通过模式引导的输出解析来确保结果的可解释性。

## 📊 实验亮点

实验结果表明，最终系统在所有基线测试中均表现优异，具体性能数据未提供，但展示了显著的提升，验证了结合示例驱动提示与LLM推理的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和个性化学习平台。通过提高AI辅导员的错误识别能力，可以为学生提供更精准的反馈，促进学习效果的提升，未来可能在教育评估和个性化学习中发挥重要作用。

## 📄 摘要（原文）

> This paper presents our system for Track 1: Mistake Identification in the BEA 2025 Shared Task on Pedagogical Ability Assessment of AI-powered Tutors. The task involves evaluating whether a tutor's response correctly identifies a mistake in a student's mathematical reasoning. We explore four approaches: (1) an ensemble of machine learning models over pooled token embeddings from multiple pretrained language models (LMs); (2) a frozen sentence-transformer using [CLS] embeddings with an MLP classifier; (3) a history-aware model with multi-head attention between token-level history and response embeddings; and (4) a retrieval-augmented few-shot prompting system with a large language model (LLM) i.e. GPT 4o. Our final system retrieves semantically similar examples, constructs structured prompts, and uses schema-guided output parsing to produce interpretable predictions. It outperforms all baselines, demonstrating the effectiveness of combining example-driven prompting with LLM reasoning for pedagogical feedback assessment. Our code is available at https://github.com/NaumanNaeem/BEA_2025.

