---
layout: default
title: "What am I missing here?: Evaluating Large Language Models for Masked Sentence Prediction"
---

# What am I missing here?: Evaluating Large Language Models for Masked Sentence Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07702" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07702v1</a>
  <a href="https://arxiv.org/pdf/2508.07702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07702v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07702v1', 'What am I missing here?: Evaluating Large Language Models for Masked Sentence Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charlie Wyatt, Aditya Joshi, Flora Salim

**分类**: cs.CL

**发布日期**: 2025-08-11

**备注**: Under Review

---

## 💡 一句话要点

**评估大语言模型在掩码句子预测中的表现以解决长程一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `掩码句子预测` `长文本处理` `全局连贯性` `自然语言处理` `Transformer`

## 📋 核心要点

1. 现有的下一标记预测方法在长程一致性和全局连贯性方面存在明显不足，限制了模型的表现。
2. 论文通过掩码句子预测任务评估商业LLMs在不同文本领域的表现，旨在揭示其在长文本处理中的能力。
3. 实验结果显示，尽管商业LLMs在其他任务中表现优异，但在低结构域的掩码句子预测中效果不佳，存在能力缺口。

## 📝 摘要（中文）

本研究探讨了基于Transformer的大语言模型（LLMs）在掩码句子预测（MSP）任务中的表现，指出现有的下一标记预测（NTP）方法在长程一致性和全局连贯性方面的不足。通过对三种商业LLMs（GPT-4o、Claude 3.5 Sonnet和Gemini 2.0 Flash）在不同领域（叙事、程序性和说明性文本）上的评估，发现这些模型在低结构域的掩码句子预测任务中表现不佳，揭示了当前模型能力的缺口。

## 🔬 方法详解

**问题定义**：本研究旨在解决大语言模型在掩码句子预测任务中的表现不足，尤其是在低结构域文本中，现有的NTP方法未能有效处理长程一致性问题。

**核心思路**：论文提出通过评估LLMs在掩码句子预测任务中的表现，来探讨其在长文本处理中的能力，强调全局连贯性的重要性。

**技术框架**：研究评估了三种商业LLMs在三个不同领域的掩码句子预测任务，分别是叙事（ROCStories）、程序性（Recipe1M）和说明性（Wikipedia）文本。

**关键创新**：本研究的创新在于将掩码句子预测作为评估LLMs全局连贯性能力的标准，填补了现有研究的空白，强调了模型在长文本处理中的不足。

**关键设计**：实验中使用了相似性和连贯性两个指标来评估模型的表现，具体参数设置和损失函数的设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果表明，尽管商业LLMs在其他任务中表现优异，但在掩码句子预测任务中，尤其是在低结构域文本中，其表现显著低于预期，揭示了当前模型在处理长文本时的能力缺口。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、文本生成和信息检索等。通过提升LLMs在长文本处理中的能力，可以改善自动写作、对话系统和内容推荐等实际应用的效果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Transformer-based models primarily rely on Next Token Prediction (NTP), which predicts the next token in a sequence based on the preceding context. However, NTP's focus on single-token prediction often limits a model's ability to plan ahead or maintain long-range coherence, raising questions about how well LLMs can predict longer contexts, such as full sentences within structured documents. While NTP encourages local fluency, it provides no explicit incentive to ensure global coherence across sentence boundaries-an essential skill for reconstructive or discursive tasks. To investigate this, we evaluate three commercial LLMs (GPT-4o, Claude 3.5 Sonnet, and Gemini 2.0 Flash) on Masked Sentence Prediction (MSP) - the task of infilling a randomly removed sentence - from three domains: ROCStories (narrative), Recipe1M (procedural), and Wikipedia (expository). We assess both fidelity (similarity to the original sentence) and cohesiveness (fit within the surrounding context). Our key finding reveals that commercial LLMs, despite their superlative performance in other tasks, are poor at predicting masked sentences in low-structured domains, highlighting a gap in current model capabilities.

