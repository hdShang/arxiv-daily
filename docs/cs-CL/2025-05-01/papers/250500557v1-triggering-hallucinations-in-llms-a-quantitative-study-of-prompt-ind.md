---
layout: default
title: Triggering Hallucinations in LLMs: A Quantitative Study of Prompt-Induced Hallucination in Large Language Models
---

# Triggering Hallucinations in LLMs: A Quantitative Study of Prompt-Induced Hallucination in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00557" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00557v1</a>
  <a href="https://arxiv.org/pdf/2505.00557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00557v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00557v1', 'Triggering Hallucinations in LLMs: A Quantitative Study of Prompt-Induced Hallucination in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Makoto Sato

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出基于提示的框架以量化大型语言模型的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻觉现象` `提示设计` `量化评估` `模型安全性`

## 📋 核心要点

1. 幻觉现象在大型语言模型中普遍存在，导致生成的内容缺乏事实可靠性，影响实际应用。
2. 提出了幻觉诱导提示（HIP）和幻觉量化提示（HQP），通过合成语义上远离的概念来触发幻觉并量化其影响。
3. 实验显示，HIPs产生的响应比对照组更不连贯，且不同模型在幻觉表现上存在显著差异。

## 📝 摘要（中文）

大型语言模型（LLMs）中的幻觉现象在医疗和法律等需要事实可靠性的实际应用中日益成为挑战。尽管在对齐和指令调优方面取得了进展，LLMs仍然可能生成流畅但根本不真实的输出。本文提出了一种基于提示的框架，通过幻觉诱导提示（HIP）和幻觉量化提示（HQP）系统地触发和量化幻觉。实验结果表明，HIPs产生的响应一致性较差且幻觉现象更为明显，且不同模型的表现存在差异。该框架为研究幻觉脆弱性提供了可重复的测试平台，并为开发更安全的LLMs铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中幻觉现象的触发与量化问题。现有方法在理解幻觉的认知动态方面存在不足，难以系统性地评估幻觉的影响。

**核心思路**：提出了一种基于提示的框架，通过设计幻觉诱导提示（HIP）来合成语义上不相关的概念，从而触发幻觉，同时使用幻觉量化提示（HQP）来评估生成内容的可信度和一致性。

**技术框架**：整体框架包括两个主要模块：幻觉诱导提示（HIP）用于生成幻觉内容，幻觉量化提示（HQP）用于评估输出的可信度、信心和连贯性。实验通过对比不同模型的响应来验证框架的有效性。

**关键创新**：最重要的创新在于提出了系统化的提示设计方法，能够有效触发并量化幻觉现象。这一方法与现有的随机生成或简单对比方法有本质区别。

**关键设计**：在设计提示时，采用了语义融合的策略，通过将不相关的概念组合在一起，形成误导性的提示。同时，HQP的评分机制考虑了多个维度，包括输出的连贯性和可信度。

## 📊 实验亮点

实验结果表明，使用幻觉诱导提示（HIP）生成的响应在连贯性和真实性上显著低于对照组，且不同模型的幻觉表现存在显著差异。这为理解和改善大型语言模型的输出质量提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、法律和教育等需要高可靠性信息的场景。通过量化和理解幻觉现象，可以为大型语言模型的安全性和可靠性提供指导，推动更智能的自我调节机制的发展，减少错误信息的传播。

## 📄 摘要（原文）

> Hallucinations in large language models (LLMs) present a growing challenge across real-world applications, from healthcare to law, where factual reliability is essential. Despite advances in alignment and instruction tuning, LLMs can still generate outputs that are fluent yet fundamentally untrue. Understanding the cognitive dynamics that underlie these hallucinations remains an open problem. In this study, we propose a prompt-based framework to systematically trigger and quantify hallucination: a Hallucination-Inducing Prompt (HIP), which synthetically fuses semantically distant concepts (e.g., periodic table of elements and tarot divination) in a misleading way, and a Hallucination Quantifying Prompt (HQP), which scores the plausibility, confidence, and coherence of the output. Controlled experiments across multiple LLMs revealed that HIPs consistently produced less coherent and more hallucinated responses than their null-fusion controls. These effects varied across models, with reasoning-oriented LLMs showing distinct profiles from general-purpose ones. Our framework provides a reproducible testbed for studying hallucination vulnerability, and opens the door to developing safer, more introspective LLMs that can detect and self-regulate the onset of conceptual instability.

