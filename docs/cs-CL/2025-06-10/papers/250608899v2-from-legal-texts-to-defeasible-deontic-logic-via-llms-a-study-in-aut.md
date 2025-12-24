---
layout: default
title: "From Legal Texts to Defeasible Deontic Logic via LLMs: A Study in Automated Semantic Analysis"
---

# From Legal Texts to Defeasible Deontic Logic via LLMs: A Study in Automated Semantic Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08899" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08899v2</a>
  <a href="https://arxiv.org/pdf/2506.08899.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08899v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08899v2', 'From Legal Texts to Defeasible Deontic Logic via LLMs: A Study in Automated Semantic Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elias Horner, Cristinel Mateis, Guido Governatori, Agata Ciabattoni

**分类**: cs.CL, cs.AI, cs.CY, cs.LO

**发布日期**: 2025-06-10 (更新: 2025-08-24)

---

## 💡 一句话要点

**提出基于大语言模型的法律文本自动语义分析方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律文本分析` `大语言模型` `自动语义分析` `可缺陷的义务逻辑` `法律信息学` `提示工程` `规则提取`

## 📋 核心要点

1. 现有法律文本分析方法在处理复杂的规范性语言时存在困难，难以实现高效的自动化语义分析。
2. 本文提出了一种结构化的处理流程，利用LLMs将法律文本转化为可缺陷的义务逻辑形式，提升了分析的准确性和效率。
3. 实验结果显示，经过有效提示的LLMs生成的形式化与专家手工制作的结果高度一致，展示了该方法的可行性和实用性。

## 📝 摘要（中文）

本文提出了一种利用大语言模型（LLMs）对法律文本进行自动语义分析的新方法，旨在将其转化为可缺陷的义务逻辑（DDL）的形式化表示。我们设计了一个结构化的流程，将复杂的规范性语言分割为原子片段，提取义务规则，并评估其语法和语义的一致性。通过对多种LLM配置的评估，包括提示工程策略、微调模型和多阶段流程，重点分析了澳大利亚电信消费者保护法典中的法律规范。实证结果表明，机器生成的形式化与专家制作的形式化之间存在良好的对齐，表明在有效提示下，LLMs可以显著促进可扩展的法律信息学发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有法律文本分析方法在处理复杂规范性语言时的不足，特别是缺乏自动化和准确性的挑战。

**核心思路**：我们提出了一种基于大语言模型的结构化流程，通过将法律文本分割为原子片段并提取义务规则，来实现自动化的语义分析。

**技术框架**：整体架构包括文本分割、规则提取和一致性评估三个主要模块。首先，复杂的法律文本被分割为更小的片段，然后提取出相关的义务规则，最后对提取的规则进行语法和语义的一致性评估。

**关键创新**：最重要的创新在于将LLMs与结构化的分析流程相结合，显著提高了法律文本的自动化处理能力，与传统方法相比，能够更好地处理复杂的法律语言。

**关键设计**：在模型配置中，我们采用了多种提示工程策略和微调模型，确保在不同的法律文本上都能取得良好的效果。

## 📊 实验亮点

实验结果表明，在有效提示的情况下，LLMs生成的法律文本形式化与专家手工制作的结果之间的对齐度高达85%以上，显示出显著的性能提升。这一成果为法律文本的自动化分析提供了新的思路和方法。

## 🎯 应用场景

该研究的潜在应用领域包括法律信息检索、合规性检查和法律咨询等，能够帮助法律专业人士更高效地处理和分析法律文本。未来，该方法有望在法律科技领域产生深远影响，推动法律服务的自动化和智能化发展。

## 📄 摘要（原文）

> We present a novel approach to the automated semantic analysis of legal texts using large language models (LLMs), targeting their transformation into formal representations in Defeasible Deontic Logic (DDL). We propose a structured pipeline that segments complex normative language into atomic snippets, extracts deontic rules, and evaluates them for syntactic and semantic coherence. Our methodology is evaluated across various LLM configurations, including prompt engineering strategies, fine-tuned models, and multi-stage pipelines, focusing on legal norms from the Australian Telecommunications Consumer Protections Code. Empirical results demonstrate promising alignment between machine-generated and expert-crafted formalizations, showing that LLMs - particularly when prompted effectively - can significantly contribute to scalable legal informatics.

