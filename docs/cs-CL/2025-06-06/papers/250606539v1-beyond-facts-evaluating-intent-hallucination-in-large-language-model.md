---
layout: default
title: "Beyond Facts: Evaluating Intent Hallucination in Large Language Models"
---

# Beyond Facts: Evaluating Intent Hallucination in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06539" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06539v1</a>
  <a href="https://arxiv.org/pdf/2506.06539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06539v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06539v1', 'Beyond Facts: Evaluating Intent Hallucination in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijie Hao, Haofei Yu, Jiaxuan You

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

**备注**: Accepted to ACL 2025 main conference

**期刊**: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2025)

---

## 💡 一句话要点

**提出FAITHQA基准以评估大型语言模型的意图幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意图幻觉` `大型语言模型` `FAITHQA` `自动评估` `自然语言处理` `检索增强生成` `CONSTRAINT SCORE`

## 📋 核心要点

1. 当前大型语言模型在复杂查询中常出现意图幻觉，导致响应不完整或误解查询。
2. 本文提出FAITHQA基准，系统评估意图幻觉，涵盖多种查询和生成设置。
3. 实验结果表明，意图幻觉普遍存在，且CONSTRAINT SCORE在检测上优于现有基线。

## 📝 摘要（中文）

在面对包含多个条件的复杂查询时，当前的大型语言模型（LLMs）往往只部分满足查询，忽略某些条件。为此，本文引入了意图幻觉的概念，指的是LLMs在生成响应时要么遗漏（未能处理某些部分），要么误解（回应虚构的查询部分）给定查询的元素。为系统评估意图幻觉，本文提出了FAITHQA，一个包含20,068个问题的新基准，涵盖查询和检索增强生成（RAG）设置，涉及不同主题和难度。FAITHQA是首个超越事实验证的幻觉基准，旨在识别意图幻觉的根本原因。通过在FAITHQA上评估多种LLMs，发现意图幻觉是即使是最先进模型也普遍存在的问题，且该现象源于LLMs的遗漏或误解。为促进未来研究，本文引入了一种自动LLM生成评估指标CONSTRAINT SCORE，用于检测意图幻觉。人类评估结果表明，CONSTRAINT SCORE在意图幻觉检测上更接近人类表现。

## 🔬 方法详解

**问题定义**：本文解决的是大型语言模型在处理复杂查询时的意图幻觉问题，现有方法未能有效识别和评估这一现象，导致生成的响应不准确或不完整。

**核心思路**：论文的核心思路是通过构建FAITHQA基准，系统性地评估意图幻觉，识别模型在生成过程中遗漏或误解查询的根本原因。

**技术框架**：FAITHQA基准包含20,068个问题，分为查询仅和检索增强生成两种设置，涵盖多种主题和难度，旨在全面评估意图幻觉。

**关键创新**：最重要的技术创新是引入了CONSTRAINT SCORE评估指标，能够自动检测意图幻觉，且在性能上更接近人类评估。

**关键设计**：在设计中，FAITHQA的构建考虑了多样性和难度，CONSTRAINT SCORE的计算方式基于对生成内容的约束分析，确保能够有效识别意图幻觉。

## 📊 实验亮点

实验结果显示，意图幻觉在当前的最先进模型中普遍存在，CONSTRAINT SCORE在检测意图幻觉方面的表现显著优于现有基线，接近人类评估结果，表明该指标的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等，能够帮助开发更为精准和可靠的语言模型，提升用户体验和信息获取的准确性。未来，随着意图幻觉问题的深入研究，可能会推动更智能的AI系统的出现。

## 📄 摘要（原文）

> When exposed to complex queries containing multiple conditions, today's large language models (LLMs) tend to produce responses that only partially satisfy the query while neglecting certain conditions. We therefore introduce the concept of Intent Hallucination. In this phenomenon, LLMs either omit (neglecting to address certain parts) or misinterpret (responding to invented query parts) elements of the given query, leading to intent hallucinated generation. To systematically evaluate intent hallucination, we introduce FAITHQA, a novel benchmark for intent hallucination that contains 20,068 problems, covering both query-only and retrieval-augmented generation (RAG) setups with varying topics and difficulty. FAITHQA is the first hallucination benchmark that goes beyond factual verification, tailored to identify the fundamental cause of intent hallucination. By evaluating various LLMs on FAITHQA, we find that (1) intent hallucination is a common issue even for state-of-the-art models, and (2) the phenomenon stems from omission or misinterpretation of LLMs. To facilitate future research, we introduce an automatic LLM generation evaluation metric, CONSTRAINT SCORE, for detecting intent hallucination. Human evaluation results demonstrate that CONSTRAINT SCORE is closer to human performance for intent hallucination compared to baselines.

