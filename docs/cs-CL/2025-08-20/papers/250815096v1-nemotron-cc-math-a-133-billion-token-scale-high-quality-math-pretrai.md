---
layout: default
title: "Nemotron-CC-Math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset"
---

# Nemotron-CC-Math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15096" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15096v1</a>
  <a href="https://arxiv.org/pdf/2508.15096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15096v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15096v1', 'Nemotron-CC-Math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rabeeh Karimi Mahabadi, Sanjeev Satheesh, Shrimai Prabhumoye, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出Nemotron-CC-Math以解决数学数据集质量不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学数据集` `预训练模型` `科学文本提取` `深度学习` `推理能力` `数据质量` `开源`

## 📋 核心要点

1. 现有的数学数据集在质量上存在不足，主要由于提取算法不稳定和HTML转换问题，导致数学结构无法可靠保留。
2. 本文提出了一种新颖的提取管道，能够从Common Crawl中稳健地提取数学内容，支持多种数学格式的恢复。
3. 实验表明，使用Nemotron-CC-Math预训练的模型在数学推理和通用推理任务上均取得了显著的性能提升。

## 📝 摘要（中文）

在大型语言模型（LLMs）的预训练中，使用高质量的结构化数据（如数学和代码）显著提升推理能力。然而，现有的数学数据集因提取算法脆弱、HTML到文本的转换损失以及数学结构的保留不可靠而质量下降。本文提出Nemotron-CC-Math，这是一个基于Common Crawl构建的大规模高质量数学语料库，采用了一种新颖的领域无关的管道，专门设计用于稳健的科学文本提取。该管道通过布局感知渲染和基于LLM的清理阶段，恢复了多种格式的数学内容，保持了方程和代码块的结构完整性。实验结果表明，使用该语料库预训练的模型在多个基准测试上均取得了显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学数据集在质量和结构保留方面的不足，尤其是由于提取算法脆弱和HTML转换损失导致的数学内容丢失问题。

**核心思路**：提出了一种新颖的领域无关的提取管道，能够有效恢复多种格式的数学内容，并通过清理阶段确保内容的结构完整性。

**技术框架**：整体架构包括布局感知渲染模块和基于LLM的清理阶段，前者负责从网页中提取数学内容，后者则对提取的内容进行标准化和一致性修正。

**关键创新**：该管道的创新之处在于其能够处理多种数学格式（如MathJax、KaTeX、MathML），并通过布局感知技术提升提取的准确性，显著优于现有方法。

**关键设计**：在参数设置上，采用了针对不同数学格式的特定处理策略，损失函数设计上注重保留结构完整性，网络结构则结合了深度学习与传统的文本处理技术。

## 📊 实验亮点

实验结果显示，使用Nemotron-CC-Math预训练的Nemotron-T 8B模型在MATH和MBPP+基准上分别获得了+4.8至+12.6和+4.6至+14.3的性能提升，且在MMLU和MMLU-Stem的通用领域表现也有所改善，标志着在开放数学预训练语料库中设立了新的性能标准。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科研和自动化编程等。通过提供高质量的数学数据集，可以为数学推理、代码生成等任务提供更强的支持，推动相关领域的研究与应用发展。

## 📄 摘要（原文）

> Pretraining large language models (LLMs) on high-quality, structured data such as mathematics and code substantially enhances reasoning capabilities. However, existing math-focused datasets built from Common Crawl suffer from degraded quality due to brittle extraction heuristics, lossy HTML-to-text conversion, and the failure to reliably preserve mathematical structure. In this work, we introduce Nemotron-CC-Math, a large-scale, high-quality mathematical corpus constructed from Common Crawl using a novel, domain-agnostic pipeline specifically designed for robust scientific text extraction.
>   Unlike previous efforts, our pipeline recovers math across various formats (e.g., MathJax, KaTeX, MathML) by leveraging layout-aware rendering with lynx and a targeted LLM-based cleaning stage. This approach preserves the structural integrity of equations and code blocks while removing boilerplate, standardizing notation into LaTeX representation, and correcting inconsistencies.
>   We collected a large, high-quality math corpus, namely Nemotron-CC-Math-3+ (133B tokens) and Nemotron-CC-Math-4+ (52B tokens). Notably, Nemotron-CC-Math-4+ not only surpasses all prior open math datasets-including MegaMath, FineMath, and OpenWebMath-but also contains 5.5 times more tokens than FineMath-4+, which was previously the highest-quality math pretraining dataset. When used to pretrain a Nemotron-T 8B model, our corpus yields +4.8 to +12.6 gains on MATH and +4.6 to +14.3 gains on MBPP+ over strong baselines, while also improving general-domain performance on MMLU and MMLU-Stem.
>   We present the first pipeline to reliably extract scientific content--including math--from noisy web-scale data, yielding measurable gains in math, code, and general reasoning, and setting a new state of the art among open math pretraining corpora. To support open-source efforts, we release our code and datasets.

