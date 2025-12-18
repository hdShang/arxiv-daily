---
layout: default
title: Evaluating LLMs for Zeolite Synthesis Event Extraction (ZSEE): A Systematic Analysis of Prompting Strategies
---

# Evaluating LLMs for Zeolite Synthesis Event Extraction (ZSEE): A Systematic Analysis of Prompting Strategies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15312" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15312v1</a>
  <a href="https://arxiv.org/pdf/2512.15312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15312v1" onclick="toggleFavorite(this, '2512.15312v1', 'Evaluating LLMs for Zeolite Synthesis Event Extraction (ZSEE): A Systematic Analysis of Prompting Strategies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charan Prakash Rathore, Saumi Ray, Dhruv Kumar

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-17

**备注**: Under Review

---

## 💡 一句话要点

**系统评估LLM在沸石合成事件抽取（ZSEE）中的提示策略有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信息抽取` `沸石合成` `提示工程` `科学文本挖掘`

## 📋 核心要点

1. 现有方法在沸石合成实验信息抽取方面存在不足，缺乏对大型语言模型（LLM）的系统评估。
2. 论文核心在于评估不同提示策略下LLM在沸石合成事件抽取任务中的性能，并分析其局限性。
3. 实验结果表明，LLM在事件类型分类上表现良好，但在细粒度信息提取方面仍有提升空间，高级提示策略提升有限。

## 📝 摘要（中文）

从沸石合成实验流程中提取结构化信息对于材料发现至关重要，但现有方法尚未系统地评估大型语言模型（LLM）在此领域特定任务中的应用。本文旨在解决一个根本问题：将LLM应用于科学信息提取时，不同提示策略的有效性如何？我们关注四个关键子任务：事件类型分类（识别合成步骤）、触发词识别（定位事件提及）、论元角色提取（识别参数类型）和论元文本提取（提取参数值）。我们使用包含1530个标注句子的ZSEE数据集，在六个先进的LLM（Gemma-3-12b-it, GPT-5-mini, O4-mini, Claude-Haiku-3.5, DeepSeek reasoning and non-reasoning）上评估了四种提示策略——零样本、少样本、事件特定和基于反思。结果表明，LLM在事件类型分类上表现出色（80-90% F1），但在细粒度提取任务上表现一般，尤其是在论元角色和论元文本提取方面（50-65% F1）。GPT-5-mini表现出极高的提示敏感性，F1值变化范围为11-79%。值得注意的是，高级提示策略相对于零样本方法几乎没有提供改进，揭示了潜在的架构限制。错误分析表明存在系统性幻觉、过度泛化以及无法捕捉合成特定细微之处的问题。我们的研究结果表明，虽然LLM可以实现高层次的理解，但精确提取实验参数需要领域自适应模型，并为科学信息提取提供定量基准。

## 🔬 方法详解

**问题定义**：论文旨在解决从沸石合成实验流程文本中自动提取结构化信息的问题。现有方法，尤其是基于传统自然语言处理的方法，在处理复杂的科学文本和捕捉领域特定知识方面存在局限性。此外，缺乏对大型语言模型（LLM）在此任务上的系统性评估，无法充分利用LLM的强大能力。

**核心思路**：论文的核心思路是系统性地评估不同的提示策略对LLM在沸石合成事件抽取任务中的影响。通过比较零样本、少样本、事件特定和基于反思等提示策略，分析LLM在不同子任务上的表现，并识别其优势和不足。这种方法旨在为LLM在科学信息提取领域的应用提供指导。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 数据集准备：使用ZSEE数据集，该数据集包含1530个标注句子，涵盖沸石合成实验流程的各个方面。2) 模型选择：选择六个先进的LLM，包括Gemma-3-12b-it, GPT-5-mini, O4-mini, Claude-Haiku-3.5, DeepSeek reasoning and non-reasoning。3) 提示策略设计：设计四种不同的提示策略，包括零样本、少样本、事件特定和基于反思。4) 实验评估：在四个关键子任务上评估LLM的性能，包括事件类型分类、触发词识别、论元角色提取和论元文本提取。5) 错误分析：分析LLM的错误类型，识别其局限性。

**关键创新**：论文最重要的技术创新点在于对LLM在沸石合成事件抽取任务中的系统性评估。与以往的研究不同，该论文不仅关注LLM的整体性能，还深入分析了不同提示策略的影响，并识别了LLM在细粒度信息提取方面的局限性。此外，论文还提供了详细的错误分析，为未来研究提供了指导。

**关键设计**：论文的关键设计包括：1) 提示策略的设计：针对不同的子任务，设计了不同的提示策略，例如，事件特定提示策略利用了领域知识，而基于反思的提示策略则试图引导LLM进行更深入的推理。2) 评估指标的选择：使用了F1值等常用的评估指标，以衡量LLM在不同子任务上的性能。3) 错误分析的方法：通过人工分析LLM的错误输出，识别了系统性幻觉、过度泛化等问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15312v1/flow-chart.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLM在事件类型分类任务上表现出色，F1值达到80-90%。然而，在细粒度提取任务（论元角色和论元文本提取）上，性能相对较低，F1值在50-65%之间。GPT-5-mini对提示词非常敏感，F1值变化范围为11-79%。高级提示策略并没有显著提升性能，表明LLM在处理领域特定任务时存在局限性。

## 🎯 应用场景

该研究成果可应用于材料科学领域，加速新材料的发现和合成。通过自动提取沸石合成实验信息，可以减少人工阅读文献的时间，提高科研效率。此外，该研究为LLM在其他科学领域的应用提供了借鉴，例如药物研发、化学反应预测等。

## 📄 摘要（原文）

> Extracting structured information from zeolite synthesis experimental procedures is critical for materials discovery, yet existing methods have not systematically evaluated Large Language Models (LLMs) for this domain-specific task. This work addresses a fundamental question: what is the efficacy of different prompting strategies when applying LLMs to scientific information extraction? We focus on four key subtasks: event type classification (identifying synthesis steps), trigger text identification (locating event mentions), argument role extraction (recognizing parameter types), and argument text extraction (extracting parameter values). We evaluate four prompting strategies - zero-shot, few-shot, event-specific, and reflection-based - across six state-of-the-art LLMs (Gemma-3-12b-it, GPT-5-mini, O4-mini, Claude-Haiku-3.5, DeepSeek reasoning and non-reasoning) using the ZSEE dataset of 1,530 annotated sentences. Results demonstrate strong performance on event type classification (80-90\% F1) but modest performance on fine-grained extraction tasks, particularly argument role and argument text extraction (50-65\% F1). GPT-5-mini exhibits extreme prompt sensitivity with 11-79\% F1 variation. Notably, advanced prompting strategies provide minimal improvements over zero-shot approaches, revealing fundamental architectural limitations. Error analysis identifies systematic hallucination, over-generalization, and inability to capture synthesis-specific nuances. Our findings demonstrate that while LLMs achieve high-level understanding, precise extraction of experimental parameters requires domain-adapted models, providing quantitative benchmarks for scientific information extraction.

