---
layout: default
title: "The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget"
---

# The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13666" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13666v1</a>
  <a href="https://arxiv.org/pdf/2508.13666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13666v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13666v1', 'The Hidden Cost of Readability: How Code Formatting Silently Consumes Your LLM Budget')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dangfeng Pan, Zhensu Sun, Cenyuan Zhang, David Lo, Xiaoning Du

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-19

**备注**: Accepted by ICSE'26 (First Cycle)

---

## 💡 一句话要点

**提出代码格式优化策略以降低LLM计算成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码格式化` `大型语言模型` `计算效率` `性能优化` `编程语言` `实验研究` `智能编程` `工具开发`

## 📋 核心要点

1. 现有代码格式化方法在提升人类可读性方面有效，但对LLM的性能和效率却造成了额外的计算负担。
2. 本文提出通过去除代码中的格式化元素来优化LLM的输入，降低计算成本，同时保持性能稳定。
3. 实验结果表明，去除格式化元素可使输入标记减少24.5%，并且通过提示和微调可进一步减少输出代码长度，最高可达36.1%。

## 📝 摘要（中文）

源代码通常通过缩进和换行等元素进行格式化，以提高人类开发者的可读性。然而，这些视觉辅助对大型语言模型（LLMs）并没有显著益处，因为代码被处理为线性序列的标记。此外，这些额外的标记会导致计算成本增加和响应时间延长。为了解决这一问题，本文通过对四种编程语言（Java、Python、C++、C#）和十种LLM进行大规模实验，系统分析了去除格式化元素对LLM性能和效率的影响。研究发现，LLM在格式化和未格式化代码之间的性能保持一致，输入标记平均减少24.5%，输出标记减少微乎其微。这使得去除代码格式成为提高LLM效率的实用优化策略。进一步研究表明，提示和微调LLM可以显著减少输出代码长度（最高达36.1%），而不影响正确性。为此，本文开发了一种双向代码转换工具，便于在现有LLM推理工作流中集成，确保人类可读性和LLM效率。

## 🔬 方法详解

**问题定义**：本文旨在解决代码格式化对LLM性能和计算成本的影响，现有方法未能考虑格式化元素的冗余性，导致不必要的计算开销。

**核心思路**：通过去除代码中的格式化元素，评估其对LLM性能的影响，从而提出一种优化策略，以降低计算成本并提高效率。

**技术框架**：研究采用大规模实验设计，涵盖四种编程语言和十种LLM，分析去除格式化元素前后的性能变化，主要模块包括数据预处理、实验设计、性能评估等。

**关键创新**：本文的创新在于系统性地分析了代码格式对LLM的影响，提出了去除格式化元素作为优化策略，与现有方法相比，提供了更为高效的解决方案。

**关键设计**：在实验中，设置了不同的格式化元素组合，采用标准的性能评估指标，确保实验结果的可靠性和可重复性。

## 📊 实验亮点

实验结果显示，去除代码格式化元素后，LLM的输入标记平均减少24.5%，而输出标记减少幅度微小。此外，通过提示和微调，输出代码长度可减少最高达36.1%，在保持正确性的前提下显著提升了效率。

## 🎯 应用场景

该研究的潜在应用领域包括代码自动生成、智能编程助手和软件开发工具等。通过优化代码格式，能够有效降低LLM的计算成本，提高开发效率，推动智能编程技术的进一步发展。

## 📄 摘要（原文）

> Source code is usually formatted with elements like indentation and newlines to improve readability for human developers. However, these visual aids do not seem to be beneficial for large language models (LLMs) in the same way since the code is processed as a linear sequence of tokens. Furthermore, these additional tokens can lead to increased computational costs and longer response times for LLMs. If such formatting elements are non-essential to LLMs, we can reduce such costs by removing them from the code. To figure out the role played by formatting elements, we conduct a comprehensive empirical study to evaluate the impact of code formatting on LLM performance and efficiency. Through large-scale experiments on Fill-in-the-Middle Code Completion tasks across four programming languages (Java, Python, C++, C\#) and ten LLMs-including both commercial and open-source models-we systematically analyze token count and performance when formatting elements are removed. Key findings indicate that LLMs can maintain performance across formatted code and unformatted code, achieving an average input token reduction of 24.5\% with negligible output token reductions. This makes code format removal a practical optimization strategy for improving LLM efficiency. Further exploration reveals that both prompting and fine-tuning LLMs can lead to significant reductions (up to 36.1\%) in output code length without compromising correctness. To facilitate practical applications, we develop a bidirectional code transformation tool for format processing, which can be seamlessly integrated into existing LLM inference workflows, ensuring both human readability and LLM efficiency.

