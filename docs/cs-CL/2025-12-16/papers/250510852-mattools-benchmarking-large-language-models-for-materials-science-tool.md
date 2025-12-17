---
layout: default
title: MatTools: Benchmarking Large Language Models for Materials Science Tools
---

# MatTools: Benchmarking Large Language Models for Materials Science Tools

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10852" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10852</a>
  <a href="https://arxiv.org/pdf/2505.10852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10852" onclick="toggleFavorite(this, '2505.10852', 'MatTools: Benchmarking Large Language Models for Materials Science Tools')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Liu, Bo Hu, Beilin Ye, Jiamin Xu, David J. Srolovitz, Tongqi Wen

**分类**: cs.CL, cs.DB

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MatTools：评估大语言模型在材料科学工具应用中的基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `材料科学` `基准测试` `物理计算` `代码生成`

## 📋 核心要点

1. 现有材料科学领域缺乏系统评估LLM使用物理计算工具能力的基准测试。
2. MatTools通过构建材料模拟工具问答基准和真实工具使用基准，评估LLM生成和执行材料科学代码的能力。
3. 实验结果表明，通用LLM优于专用LLM，并且模型复杂度与性能并非正相关。

## 📝 摘要（中文）

大语言模型（LLMs）越来越多地应用于材料科学问题，包括文献理解、性质预测、材料发现和合金设计。同时，已经开发了各种基于物理的计算方法，可以通过这些方法计算材料性质。本文提出了一个基准测试应用，旨在评估LLMs通过生成和安全执行基于物理的计算材料科学软件包的代码来回答材料科学问题的能力。MatTools建立在两个互补的组件之上：材料模拟工具问答（QA）基准和真实工具使用基准。我们设计了一种自动化的方法来有效地收集真实的材料科学工具使用示例。QA基准源自pymatgen（Python Materials Genomics）代码库和文档，包含69,225个QA对，用于评估LLM理解材料科学工具的能力。真实基准包含49个任务（138个子任务），需要生成用于材料性质计算的功能性Python代码。我们对各种LLM的评估产生了三个关键见解：（1）通用模型优于专用模型；（2）AI了解AI；（3）越简单越好。MatTools提供了一个标准化的框架，用于评估和改进LLM在材料科学工具应用中的能力，从而促进开发更有效的AI系统，用于材料科学和一般科学研究。

## 🔬 方法详解

**问题定义**：现有材料科学领域缺乏一个标准化的基准来评估大型语言模型（LLMs）在利用物理计算工具解决材料科学问题方面的能力。现有的方法要么是针对特定任务的，要么缺乏对LLM生成代码的实际执行和安全性的考量。因此，需要一个全面的基准来评估LLM在理解材料科学工具、生成可执行代码以及解决实际材料科学问题方面的能力。

**核心思路**：MatTools的核心思路是构建两个互补的基准：一个基于问答（QA）的基准，用于评估LLM对材料科学工具的理解；另一个基于真实工具使用的基准，用于评估LLM生成可执行代码的能力。通过这两个基准，可以全面评估LLM在材料科学工具应用中的能力，并为未来的研究提供一个标准化的评估框架。

**技术框架**：MatTools包含两个主要组件：材料模拟工具问答（QA）基准和真实工具使用基准。QA基准包含69,225个QA对，这些QA对源自pymatgen代码库和文档，用于评估LLM理解材料科学工具的能力。真实工具使用基准包含49个任务（138个子任务），这些任务需要LLM生成用于材料性质计算的功能性Python代码。此外，论文还设计了一种自动化的方法来收集真实的材料科学工具使用示例。

**关键创新**：MatTools的关键创新在于其构建了两个互补的基准，可以全面评估LLM在材料科学工具应用中的能力。QA基准侧重于评估LLM对材料科学工具的理解，而真实工具使用基准侧重于评估LLM生成可执行代码的能力。此外，MatTools还提供了一个标准化的评估框架，可以方便地比较不同LLM的性能。

**关键设计**：QA基准中的QA对是基于pymatgen代码库和文档生成的，涵盖了各种材料科学工具的使用方法。真实工具使用基准中的任务是基于真实的材料科学问题设计的，需要LLM生成用于材料性质计算的功能性Python代码。论文还设计了一种自动化的方法来收集真实的材料科学工具使用示例，以确保基准的真实性和可靠性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.10852/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.10852/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.10852/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，通用LLM在MatTools基准测试中表现优于专用LLM，这表明通用知识对于理解和使用材料科学工具至关重要。此外，研究发现模型复杂度与性能并非正相关，简单的模型有时能取得更好的效果。例如，在某些任务上，GPT-3.5的性能优于更复杂的模型。

## 🎯 应用场景

MatTools可用于评估和改进LLM在材料科学领域的应用能力，例如材料性质预测、材料发现和合金设计。该基准测试框架可以促进开发更有效的AI系统，加速材料科学研究进程，并为其他科学领域的AI应用提供借鉴。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly applied to materials science questions, including literature comprehension, property prediction, materials discovery and alloy design. At the same time, a wide range of physics-based computational approaches have been developed in which materials properties can be calculated. Here, we propose a benchmark application to evaluate the proficiency of LLMs to answer materials science questions through the generation and safe execution of codes based on such physics-based computational materials science packages. MatTools is built on two complementary components: a materials simulation tool question-answer (QA) benchmark and a real-world tool-usage benchmark. We designed an automated methodology to efficiently collect real-world materials science tool-use examples. The QA benchmark, derived from the pymatgen (Python Materials Genomics) codebase and documentation, comprises 69,225 QA pairs that assess the ability of an LLM to understand materials science tools. The real-world benchmark contains 49 tasks (138 subtasks) requiring the generation of functional Python code for materials property calculations. Our evaluation of diverse LLMs yields three key insights: (1)Generalists outshine specialists;(2)AI knows AI; and (3)Simpler is better. MatTools provides a standardized framework for assessing and improving LLM capabilities for materials science tool applications, facilitating the development of more effective AI systems for materials science and general scientific research.

