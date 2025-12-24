---
layout: default
title: "SynLLM: A Comparative Analysis of Large Language Models for Medical Tabular Synthetic Data Generation via Prompt Engineering"
---

# SynLLM: A Comparative Analysis of Large Language Models for Medical Tabular Synthetic Data Generation via Prompt Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08529" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08529v1</a>
  <a href="https://arxiv.org/pdf/2508.08529.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08529v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08529v1', 'SynLLM: A Comparative Analysis of Large Language Models for Medical Tabular Synthetic Data Generation via Prompt Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arshia Ilaty, Hossein Shirazi, Hajar Homayouni

**分类**: cs.AI

**发布日期**: 2025-08-11

**备注**: 10 Pages, 2 Supplementary Pages, 6 Tables

---

## 💡 一句话要点

**提出SynLLM框架以生成高质量医疗合成数据**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗合成数据` `大型语言模型` `提示工程` `隐私保护` `数据生成`

## 📋 核心要点

1. 现有方法在生成真实医疗数据时缺乏系统的提示策略和全面的多维评估框架，导致生成数据的质量和隐私保护不足。
2. 本文提出的SynLLM框架通过结构化提示，利用20种开源LLMs生成高质量的医疗合成数据，且无需模型微调。
3. 实验结果表明，提示工程对数据质量和隐私风险有显著影响，基于规则的提示在隐私和质量之间达到了最佳平衡。

## 📝 摘要（中文）

由于隐私法规的限制，获取真实医疗数据常常面临障碍，这对医疗研究的进展构成了重大挑战。合成数据作为一种有前景的替代方案，然而生成真实、临床有效且符合隐私要求的记录仍然是一个主要挑战。本文提出了SynLLM，一个模块化框架，利用20种最先进的开源大型语言模型（LLMs），如LLaMA、Mistral和GPT变体，通过结构化提示生成高质量的医疗表格合成数据。我们提出了四种不同的提示类型，从示例驱动到基于规则的约束，编码模式、元数据和领域知识，以控制生成过程而无需模型微调。我们的框架具有全面的评估管道，严格评估生成数据的统计保真度、临床一致性和隐私保护。实验结果表明，提示工程显著影响数据质量和隐私风险，基于规则的提示在隐私和质量之间实现了最佳平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决生成真实且符合隐私要求的医疗合成数据的挑战，现有方法在提示策略和评估框架上存在不足。

**核心思路**：通过设计结构化提示，利用多种开源LLMs生成高质量的医疗表格数据，避免了对模型的微调，从而提高生成数据的质量和隐私保护。

**技术框架**：SynLLM框架包括数据生成模块和评估模块，前者负责生成合成数据，后者则对生成的数据进行统计保真度、临床一致性和隐私保护的评估。

**关键创新**：提出了四种不同类型的提示策略，包括示例驱动和基于规则的提示，这些创新使得生成的数据在临床上更具合理性，同时兼顾隐私保护。

**关键设计**：在提示设计中，结合了模式、元数据和领域知识，确保生成过程的控制和数据的高质量输出。

## 📊 实验亮点

实验结果显示，基于规则的提示在隐私保护和数据质量之间实现了最佳平衡，相较于其他提示类型，生成的数据在统计保真度和临床一致性上有显著提升，表明提示工程在合成数据生成中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗研究、临床试验和健康数据共享等。通过生成高质量的合成医疗数据，研究人员可以在不违反隐私法规的情况下进行数据分析和模型训练，从而推动医疗领域的创新与发展。

## 📄 摘要（原文）

> Access to real-world medical data is often restricted due to privacy regulations, posing a significant barrier to the advancement of healthcare research. Synthetic data offers a promising alternative; however, generating realistic, clinically valid, and privacy-conscious records remains a major challenge. Recent advancements in Large Language Models (LLMs) offer new opportunities for structured data generation; however, existing approaches frequently lack systematic prompting strategies and comprehensive, multi-dimensional evaluation frameworks.
>   In this paper, we present SynLLM, a modular framework for generating high-quality synthetic medical tabular data using 20 state-of-the-art open-source LLMs, including LLaMA, Mistral, and GPT variants, guided by structured prompts. We propose four distinct prompt types, ranging from example-driven to rule-based constraints, that encode schema, metadata, and domain knowledge to control generation without model fine-tuning. Our framework features a comprehensive evaluation pipeline that rigorously assesses generated data across statistical fidelity, clinical consistency, and privacy preservation.
>   We evaluate SynLLM across three public medical datasets, including Diabetes, Cirrhosis, and Stroke, using 20 open-source LLMs. Our results show that prompt engineering significantly impacts data quality and privacy risk, with rule-based prompts achieving the best privacy-quality balance. SynLLM establishes that, when guided by well-designed prompts and evaluated with robust, multi-metric criteria, LLMs can generate synthetic medical data that is both clinically plausible and privacy-aware, paving the way for safer and more effective data sharing in healthcare research.

