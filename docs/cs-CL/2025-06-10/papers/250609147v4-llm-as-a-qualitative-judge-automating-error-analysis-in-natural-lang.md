---
layout: default
title: "LLM-as-a-qualitative-judge: automating error analysis in natural language generation"
---

# LLM-as-a-qualitative-judge: automating error analysis in natural language generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09147" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09147v4</a>
  <a href="https://arxiv.org/pdf/2506.09147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09147v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09147v4', 'LLM-as-a-qualitative-judge: automating error analysis in natural language generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nadezhda Chirkova, Tunde Oluwaseyi Ajayi, Seth Aycock, Zain Muhammad Mujahid, Vladana Perlić, Ekaterina Borisova, Markarit Vartampetian

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-10 (更新: 2025-12-19)

**🔗 代码/项目**: [GITHUB](https://github.com/tunde-ajayi/llm-as-a-qualitative-judge)

---

## 💡 一句话要点

**提出LLM作为定性评估工具以自动化自然语言生成错误分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言生成` `大型语言模型` `定性评估` `错误分析` `系统优化`

## 📋 核心要点

1. 现有的LLM评估方法主要依赖数值评分，缺乏对生成文本的定性分析，限制了开发者对系统改进的理解。
2. 本文提出LLM-as-a-qualitative-judge，通过生成结构化的错误报告，帮助开发者识别和分析NLG系统中的常见问题。
3. 实验结果显示，LLM-as-a-qualitative-judge的输出与人工标注的匹配率为2/3，且在实际应用中显著提升了NLG系统的性能。

## 📝 摘要（中文）

在自然语言生成（NLG）中，利用大型语言模型（LLMs）评估生成文本的方式已成为标准的评估方法，通常以数值评分为主要输出。本文提出了LLM作为定性评估工具（LLM-as-a-qualitative-judge），其主要输出为NLG系统输出中常见问题类型的结构化报告。该方法旨在为开发者提供有意义的改进建议，包含开放式逐实例问题分析和使用直观累积算法的发现问题聚类两个主要步骤。实验结果表明，LLM-as-a-qualitative-judge输出的实例特定问题与人工标注的匹配率达到2/3，并且能够生成类似于人工标注者的错误类型报告。案例研究显示，该方法显著提升了NLG系统的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM评估方法缺乏定性分析的问题，现有方法主要依赖数值评分，无法深入理解生成文本中的具体错误类型。

**核心思路**：提出LLM-as-a-qualitative-judge，通过生成结构化的错误报告，帮助开发者识别NLG系统中的常见问题，从而提供有针对性的改进建议。

**技术框架**：整体流程包括两个主要模块：第一步是开放式逐实例问题分析，第二步是使用累积算法对发现的问题进行聚类。这一流程旨在系统化地分析和总结生成文本中的错误。

**关键创新**：最重要的创新点在于将LLM用于定性评估，生成的错误报告不仅包含问题类型，还能提供具体的改进建议，与传统的数值评分方法形成鲜明对比。

**关键设计**：在技术细节上，采用了直观的累积算法进行问题聚类，并结合约300个标注的实例数据进行训练和验证，以确保输出的准确性和实用性。

## 📊 实验亮点

实验结果表明，LLM-as-a-qualitative-judge生成的实例特定问题与人工标注的匹配率达到2/3，显示出其在定性分析中的有效性。此外，案例研究显示，该方法能够显著提升NLG系统的性能，证明了其实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言生成系统的开发与优化，尤其是在对话系统、文本生成和自动摘要等任务中。通过提供定性分析，开发者可以更有效地识别和修正生成文本中的问题，从而提升系统的整体性能和用户体验。未来，该方法可能在更多的NLG应用场景中得到推广，推动智能文本生成技术的发展。

## 📄 摘要（原文）

> Prompting large language models (LLMs) to evaluate generated text, known as LLM-as-a-judge, has become a standard evaluation approach in natural language generation (NLG), but is primarily used as a quantitative tool, i.e. with numerical scores as main outputs. In this work, we propose LLM-as-a-qualitative-judge, an LLM-based evaluation approach with the main output being a structured report of common issue types in the NLG system outputs. Our approach is targeted at providing developers with meaningful insights on what improvements can be done to a given NLG system and consists of two main steps, namely open-ended per-instance issue analysis and clustering of the discovered issues using an intuitive cumulative algorithm. We also introduce a strategy for evaluating the proposed approach, coupled with ~300 annotations of issues in instances from 12 NLG datasets. Our results show that instance-specific issues output by LLM-as-a-qualitative-judge match those annotated by humans in 2/3 cases, and that LLM-as-a-qualitative-judge is capable of producing error type reports resembling the reports composed by human annotators. We also demonstrate in a case study how the use of LLM-as-a-qualitative-judge can substantially improve NLG systems performance. Our code and data are publicly available at https://github.com/tunde-ajayi/llm-as-a-qualitative-judge.

