---
layout: default
title: A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis
---

# A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16063" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16063v1</a>
  <a href="https://arxiv.org/pdf/2512.16063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16063v1', 'A Multi-Agent Large Language Model Framework for Automated Qualitative Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qidi Xu, Nuzha Amjad, Grace Giles, Alexa Cumming, De'angelo Hermesky, Alexander Wen, Min Ji Kwak, Yejin Kim

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

**备注**: 42 pages, 5 figures

---

## 💡 一句话要点

**提出CoTI多智能体LLM框架，自动化定性分析，提升患者体验研究效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `大型语言模型` `定性分析` `主题分析` `患者体验` `自然语言处理`

## 📋 核心要点

1. 定性主题分析在患者体验研究中至关重要，但其劳动密集、主观且难以扩展的特性限制了其应用。
2. 论文提出CoTI框架，利用多智能体LLM协同工作，自动化主题识别、代码本生成等定性分析流程。
3. 实验表明，CoTI在心力衰竭患者访谈分析中，结果与资深研究员更接近，优于初级研究员和基线模型。

## 📝 摘要（中文）

理解患者体验对于提升以患者为中心的护理至关重要，尤其是在需要持续沟通的慢性疾病中。然而，定性主题分析是探索这些体验的主要方法，但仍然劳动密集、主观且难以扩展。本研究开发了一个多智能体大型语言模型框架，通过三个智能体（指导者、主题化者、代码本生成器）自动化定性主题分析，命名为协同主题识别智能体（CoTI）。我们将CoTI应用于12个心力衰竭患者访谈，以分析他们对药物强度的看法。CoTI识别的关键短语、主题和代码本与资深研究员的结果更相似，优于初级研究员和基线NLP模型。我们还将CoTI集成到面向用户的应用程序中，以实现AI人机交互的定性分析。然而，CoTI与初级研究员之间的协作仅提供了边际收益，表明他们可能过度依赖CoTI并限制了他们的独立批判性思维。

## 🔬 方法详解

**问题定义**：论文旨在解决定性研究中主题分析耗时费力、主观性强、难以规模化的问题。现有方法依赖人工分析，效率低下且结果易受研究者个人经验影响。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大自然语言处理能力，构建多智能体协同框架，模拟人工分析过程中的不同角色，从而实现定性分析的自动化和客观化。通过智能体间的协作，降低主观偏差，提高分析效率。

**技术框架**：CoTI框架包含三个主要智能体：Instructor（指导者）、Thematizer（主题化者）和 CodebookGenerator（代码本生成器）。Instructor负责引导整个分析流程，Thematizer负责从文本中提取主题，CodebookGenerator负责生成代码本。整个流程包括数据预处理、智能体协同分析、结果整合等步骤。用户可以通过用户界面与CoTI进行交互，调整参数和查看结果。

**关键创新**：CoTI的关键创新在于其多智能体协同架构，通过模拟人工分析中的不同角色，实现了更全面、客观的分析结果。与传统的单模型方法相比，CoTI能够更好地捕捉文本中的细微差别和复杂关系。此外，CoTI还提供了一个用户友好的界面，方便研究人员使用和定制分析流程。

**关键设计**：论文中没有明确说明关键参数设置、损失函数或网络结构等技术细节。但可以推断，每个智能体都基于预训练的LLM进行微调，并可能使用了特定的提示工程（Prompt Engineering）技术来指导智能体的行为。智能体之间的通信机制和协作策略也是CoTI的关键设计要素，但具体实现细节未知。

## 📊 实验亮点

实验结果表明，CoTI在分析心力衰竭患者访谈数据时，识别的关键短语、主题和代码本与资深研究员的结果更相似，优于初级研究员和基线NLP模型。这表明CoTI能够有效降低主观偏差，提高分析结果的客观性和准确性。然而，CoTI与初级研究员的协作收益有限，提示需要关注人机协作模式的设计。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，自动化患者访谈、病历记录等文本数据的定性分析，帮助医生和研究人员更好地理解患者体验，优化治疗方案，提升医疗服务质量。此外，该框架还可扩展到其他需要定性分析的领域，如社会科学、市场调研等，具有广泛的应用前景。

## 📄 摘要（原文）

> Understanding patients experiences is essential for advancing patient centered care, especially in chronic diseases that require ongoing communication. However, qualitative thematic analysis, the primary approach for exploring these experiences, remains labor intensive, subjective, and difficult to scale. In this study, we developed a multi agent large language model framework that automates qualitative thematic analysis through three agents (Instructor, Thematizer, CodebookGenerator), named Collaborative Theme Identification Agent (CoTI). We applied CoTI to 12 heart failure patient interviews to analyze their perceptions of medication intensity. CoTI identified key phrases, themes, and codebook that were more similar to those of the senior investigator than both junior investigators and baseline NLP models. We also implemented CoTI into a user-facing application to enable AI human interaction in qualitative analysis. However, collaboration between CoTI and junior investigators provided only marginal gains, suggesting they may overrely on CoTI and limit their independent critical thinking.

