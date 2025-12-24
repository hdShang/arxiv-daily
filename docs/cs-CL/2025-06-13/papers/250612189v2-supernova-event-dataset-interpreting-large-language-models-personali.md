---
layout: default
title: "Supernova Event Dataset: Interpreting Large Language Models' Personality through Critical Event Analysis"
---

# Supernova Event Dataset: Interpreting Large Language Models' Personality through Critical Event Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12189" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12189v2</a>
  <a href="https://arxiv.org/pdf/2506.12189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12189v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12189v2', 'Supernova Event Dataset: Interpreting Large Language Models\' Personality through Critical Event Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranav Agarwal, Ioana Ciucă

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-06-22)

**备注**: Accepted at Actionable Interpretability Workshop at ICML 2025

---

## 💡 一句话要点

**提出超新星事件数据集以解析大型语言模型的个性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `个性分析` `超新星事件数据集` `事件提取` `模型可解释性` `情感推理` `科学发现`

## 📋 核心要点

1. 现有大型语言模型在决策过程和个性理解上存在不足，缺乏有效的评估框架。
2. 论文提出超新星事件数据集，通过提取和排序关键事件来解析模型个性，使用另一个LLM作为评判者。
3. 实验结果显示不同模型展现出独特的个性特征，提升了模型的可解释性和用户友好性。

## 📝 摘要（中文）

大型语言模型（LLMs）在日常应用中的整合日益增加。随着其影响力的扩大，理解其决策过程和潜在个性变得至关重要。本研究通过提出超新星事件数据集，解析模型个性。该数据集包含多样化的文章，涵盖传记、历史事件、新闻和科学发现。我们利用该数据集对LLMs在提取和排序文本中的关键事件进行基准测试，评估小型模型如Phi-4、Orca 2和Qwen 2.5，以及大型模型如Claude 3.7、Gemini 2.5和OpenAI o3。我们提出一个框架，利用另一个LLM作为评判者，根据模型对事件的选择和分类推断其个性。分析结果显示出不同的个性特征，提升了模型的可解释性，使其在多样化应用中更具用户友好性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型个性理解的具体问题，现有方法在评估模型决策过程和个性特征方面存在不足，缺乏系统性和可解释性。

**核心思路**：通过构建超新星事件数据集，论文提出了一种新的评估框架，利用另一个LLM作为评判者，分析模型在提取和排序事件时的个性表现。这样的设计能够更全面地反映模型的决策逻辑和个性特征。

**技术框架**：整体架构包括数据集构建、模型评估和个性分析三个主要模块。首先，收集多样化的文本数据以构建超新星事件数据集；其次，评估不同规模的LLMs在事件提取和排序中的表现；最后，通过评判者LLM分析模型个性。

**关键创新**：论文的主要创新在于提出了超新星事件数据集和基于LLM的个性评估框架，区别于传统的静态评估方法，提供了动态和多维度的个性分析。

**关键设计**：在模型评估中，采用了多种模型（如Orca 2、Qwen 2.5等）进行对比，设置了特定的评估指标，以确保对模型个性的准确捕捉和分析。

## 📊 实验亮点

实验结果表明，Orca 2在情感推理方面表现突出，Qwen 2.5则展现出更具战略性的分析风格。Claude 3.7在科学发现事件分析中强调概念框架，而Gemini 2.5 Pro则优先考虑实证验证，o3则偏向逐步因果推理。这些发现为模型个性化提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、教育工具和内容生成等。通过提升大型语言模型的可解释性，用户能够更好地理解和信任模型的决策过程，从而在多样化的应用场景中实现更高的用户满意度和参与度。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly integrated into everyday applications. As their influence grows, understanding their decision making and underlying personality becomes essential. In this work, we interpret model personality using our proposed Supernova Event Dataset, a novel dataset with diverse articles spanning biographies, historical events, news, and scientific discoveries. We use this dataset to benchmark LLMs on extracting and ranking key events from text, a subjective and complex challenge that requires reasoning over long-range context and modeling causal chains. We evaluate small models like Phi-4, Orca 2, and Qwen 2.5, and large, stronger models such as Claude 3.7, Gemini 2.5, and OpenAI o3, and propose a framework where another LLM acts as a judge to infer each model's personality based on its selection and classification of events. Our analysis shows distinct personality traits: for instance, Orca 2 demonstrates emotional reasoning focusing on interpersonal dynamics, while Qwen 2.5 displays a more strategic, analytical style. When analyzing scientific discovery events, Claude Sonnet 3.7 emphasizes conceptual framing, Gemini 2.5 Pro prioritizes empirical validation, and o3 favors step-by-step causal reasoning. This analysis improves model interpretability, making them user-friendly for a wide range of diverse applications. Project Page - https://www.supernova-event.ai/

