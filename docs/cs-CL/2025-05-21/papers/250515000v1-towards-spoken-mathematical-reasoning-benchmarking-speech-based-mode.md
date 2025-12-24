---
layout: default
title: Towards Spoken Mathematical Reasoning: Benchmarking Speech-based Models over Multi-faceted Math Problems
---

# Towards Spoken Mathematical Reasoning: Benchmarking Speech-based Models over Multi-faceted Math Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15000" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15000v1</a>
  <a href="https://arxiv.org/pdf/2505.15000.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15000v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15000v1', 'Towards Spoken Mathematical Reasoning: Benchmarking Speech-based Models over Multi-faceted Math Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengwei Wei, Bin Wang, Jung-jae Kim, Nancy F. Chen

**分类**: cs.CL

**发布日期**: 2025-05-21

---

## 💡 一句话要点

**提出Spoken-MQA基准以评估语音模型的数学推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音数学推理` `多模态学习` `数学问题解决` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有的语音模型在处理数学推理时表现不足，尤其是在直接算术问题上存在明显的困难。
2. 本文提出Spoken-MQA基准，旨在全面评估语音模型在多样化数学问题上的推理能力。
3. 实验结果显示，当前的语音LLMs在符号数学表达的理解上存在偏差，且数学知识推理能力显著下降。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）和多模态LLMs（MLLMs）的进展使其在多种任务中展现出强大的推理能力。然而，它们在处理语音输入的数学推理方面仍然未得到充分探索。以往的研究主要集中在事实理解或简单音频推理任务上，缺乏对逻辑逐步推理的深入分析。为填补这一空白，本文提出了Spoken Math Question Answering（Spoken-MQA）基准，旨在评估语音模型的数学推理能力，包括级联模型（ASR + LLMs）和端到端语音LLMs。Spoken-MQA涵盖多种数学问题，所有问题均以清晰的自然语言呈现。实验结果表明，尽管一些语音LLMs在基本算术的上下文推理任务中表现良好，但在直接算术问题上仍存在困难。

## 🔬 方法详解

**问题定义**：本文旨在解决语音输入下数学推理能力不足的问题，现有方法主要集中在简单的事实理解，缺乏对复杂逻辑推理的评估。

**核心思路**：通过引入Spoken-MQA基准，评估语音模型在多样化数学问题上的表现，尤其是针对上下文推理和知识导向推理的能力。

**技术框架**：整体架构包括语音识别（ASR）模块和语言模型（LLMs），支持级联和端到端的模型设计，确保对语音输入的有效处理。

**关键创新**：Spoken-MQA基准的提出是本文的核心创新，填补了语音输入数学推理能力评估的空白，与现有的基于文本的评估方法形成鲜明对比。

**关键设计**：在模型设计中，采用了多样化的数学问题集，涵盖纯算术、单步和多步推理，确保模型在自然语言理解和数学推理上的全面评估。

## 📊 实验亮点

实验结果表明，尽管一些语音LLMs在基本算术的上下文推理任务中表现良好，但在直接算术问题上仍存在显著困难。此外，当前LLMs对LaTex符号表达的偏好导致其在口头数学表达的理解上存在困难，数学知识推理能力显著下降。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和语音助手等。通过提升语音模型的数学推理能力，可以为用户提供更为精准的数学问题解答和学习支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) and multimodal LLMs (MLLMs) have led to strong reasoning ability across a wide range of tasks. However, their ability to perform mathematical reasoning from spoken input remains underexplored. Prior studies on speech modality have mostly focused on factual speech understanding or simple audio reasoning tasks, providing limited insight into logical step-by-step reasoning, such as that required for mathematical problem solving. To address this gap, we introduce Spoken Math Question Answering (Spoken-MQA), a new benchmark designed to evaluate the mathematical reasoning capabilities of speech-based models, including both cascade models (ASR + LLMs) and end-to-end speech LLMs. Spoken-MQA covers a diverse set of math problems, including pure arithmetic, single-step and multi-step contextual reasoning, and knowledge-oriented reasoning problems, all presented in unambiguous natural spoken language. Through extensive experiments, we find that: (1) while some speech LLMs perform competitively on contextual reasoning tasks involving basic arithmetic, they still struggle with direct arithmetic problems; (2) current LLMs exhibit a strong bias toward symbolic mathematical expressions written in LaTex and have difficulty interpreting verbalized mathematical expressions; and (3) mathematical knowledge reasoning abilities are significantly degraded in current speech LLMs.

