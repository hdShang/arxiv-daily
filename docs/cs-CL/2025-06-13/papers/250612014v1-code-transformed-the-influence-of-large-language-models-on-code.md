---
layout: default
title: "code_transformed: The Influence of Large Language Models on Code"
---

# code_transformed: The Influence of Large Language Models on Code

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12014" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12014v1</a>
  <a href="https://arxiv.org/pdf/2506.12014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12014v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12014v1', 'code_transformed: The Influence of Large Language Models on Code')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuliang Xu, Siming Huang, Mingmeng Geng, Yao Wan, Xuanhua Shi, Dongping Chen

**分类**: cs.CL, cs.AI, cs.LG, cs.SE

**发布日期**: 2025-06-13

**备注**: We release all the experimental dataset and source code at: https://github.com/ignorancex/LLM_code

---

## 💡 一句话要点

**研究LLM对代码风格的影响及其特征分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码风格` `编程实践` `命名规范` `复杂性分析` `可维护性` `GitHub数据分析`

## 📋 核心要点

1. 现有研究对大型语言模型对代码风格的影响缺乏系统性分析，难以量化其变化。
2. 本文通过分析大量GitHub代码库，提出了一种量化LLMs对代码风格影响的方法，关注命名规范、复杂性、可维护性等方面。
3. 实验结果显示，LLMs的使用与代码风格的演变存在显著关联，例如变量命名风格的变化趋势。

## 📝 摘要（中文）

编程是人机交互的基本方式之一。随着大型语言模型（LLMs）的快速发展，代码生成能力开始显著改变编程实践。本文探讨了LLMs是否改变了代码风格，并如何表征这种变化。通过分析2020至2025年间与arXiv论文相关的19,000多个GitHub代码库，我们识别出与LLM生成代码特征相一致的可测量的编码风格演变趋势。例如，Python代码中snake_case变量名的比例从2023年第一季度的47%增加到2025年第一季度的51%。此外，我们还研究了LLMs在算法问题上的推理过程。实验结果提供了LLMs影响现实编程风格的首个大规模实证证据。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型对代码风格影响的量化分析问题。现有方法缺乏对代码风格变化的系统性研究，难以评估LLMs的实际影响。

**核心思路**：通过分析与arXiv论文相关的GitHub代码库，识别出代码风格的演变趋势，特别是命名规范和复杂性等方面的变化，以此来表征LLMs的影响。

**技术框架**：研究采用数据挖掘和统计分析的方法，首先收集相关代码库数据，然后进行命名规范、复杂性和可维护性等特征的量化分析，最后通过对比分析得出结论。

**关键创新**：本文的创新在于首次大规模实证研究LLMs对代码风格的影响，提供了可量化的趋势数据，填补了相关领域的研究空白。

**关键设计**：在数据收集阶段，选择了2020至2025年间的19,000多个GitHub代码库，分析了不同时间段内的变量命名风格变化，使用统计方法评估了代码复杂性和可维护性等指标。

## 📊 实验亮点

实验结果显示，Python代码中snake_case变量名的比例从2023年第一季度的47%增加到2025年第一季度的51%。这一变化表明，LLMs的使用与代码风格的演变存在显著关联，为理解现代编程实践提供了重要的实证依据。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码审查和教育等。通过理解LLMs对代码风格的影响，开发者可以更好地利用这些模型提高代码质量和可维护性。此外，教育机构可以根据这些趋势调整编程教学内容，以适应新的编程实践。未来，随着LLMs的进一步发展，相关研究将继续推动编程领域的创新与变革。

## 📄 摘要（原文）

> Coding remains one of the most fundamental modes of interaction between humans and machines. With the rapid advancement of Large Language Models (LLMs), code generation capabilities have begun to significantly reshape programming practices. This development prompts a central question: Have LLMs transformed code style, and how can such transformation be characterized? In this paper, we present a pioneering study that investigates the impact of LLMs on code style, with a focus on naming conventions, complexity, maintainability, and similarity. By analyzing code from over 19,000 GitHub repositories linked to arXiv papers published between 2020 and 2025, we identify measurable trends in the evolution of coding style that align with characteristics of LLM-generated code. For instance, the proportion of snake\_case variable names in Python code increased from 47% in Q1 2023 to 51% in Q1 2025. Furthermore, we investigate how LLMs approach algorithmic problems by examining their reasoning processes. Given the diversity of LLMs and usage scenarios, among other factors, it is difficult or even impossible to precisely estimate the proportion of code generated or assisted by LLMs. Our experimental results provide the first large-scale empirical evidence that LLMs affect real-world programming style.

