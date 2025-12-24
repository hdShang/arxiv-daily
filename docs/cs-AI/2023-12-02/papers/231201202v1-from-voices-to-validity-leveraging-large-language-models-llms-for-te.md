---
layout: default
title: "From Voices to Validity: Leveraging Large Language Models (LLMs) for Textual Analysis of Policy Stakeholder Interviews"
---

# From Voices to Validity: Leveraging Large Language Models (LLMs) for Textual Analysis of Policy Stakeholder Interviews

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01202" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01202v1</a>
  <a href="https://arxiv.org/pdf/2312.01202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01202v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01202v1', 'From Voices to Validity: Leveraging Large Language Models (LLMs) for Textual Analysis of Policy Stakeholder Interviews')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex Liu, Min Sun

**分类**: cs.HC, cs.AI, cs.CL

**发布日期**: 2023-12-02

**期刊**: AERA OPEN Volume 11, January-December 2025

**DOI**: [10.1177/23328584251374595](https://doi.org/10.1177/23328584251374595)

---

## 💡 一句话要点

**利用大型语言模型进行政策利益相关者访谈文本分析，提升效率与信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本分析` `政策分析` `利益相关者访谈` `人机协同` `主题建模` `情感分析`

## 📋 核心要点

1. 人工编码利益相关者访谈文本耗时费力，难以快速获取政策反馈，阻碍了及时有效的政策制定。
2. 结合人类专家知识与GPT-4等LLM，设计提示工程，迭代优化LLM在主题和情感分析中的表现。
3. 实验表明，GPT-4在主题编码上超越传统NLP方法25%以上，情感分析更接近专家水平，提升了分析效率和信度。

## 📝 摘要（中文）

本研究探索了将大型语言模型（LLMs），如GPT-4，与人类专业知识相结合，以增强对美国某州K-12教育政策利益相关者访谈文本的分析。通过混合方法，人类专家基于领域知识和无监督主题建模结果，开发了编码手册和编码流程。他们设计了提示来指导GPT-4分析，并迭代评估不同提示的性能。这种人机结合的方法实现了细致的主题和情感分析。结果表明，GPT-4的主题编码在特定主题上与人类编码的对齐度为77.89%，扩展到更广泛的主题时，一致性提高到96.02%，超过了传统自然语言处理（NLP）方法25%以上。此外，GPT-4的情感分析与专家情感分析的匹配度高于基于词典的方法。定量测量和定性评估的结果强调了人类领域专业知识和自动化分析的互补作用，LLM提供了新的视角和编码一致性。人机交互方法提高了教育政策研究的效率、有效性和可解释性。

## 🔬 方法详解

**问题定义**：论文旨在解决政策制定者难以高效分析大量利益相关者访谈文本的问题。现有的人工编码方法耗时费力，且容易受到主观偏差的影响。传统的自然语言处理方法在理解细微语义和领域知识方面存在局限性，无法准确捕捉利益相关者的观点和情感。

**核心思路**：论文的核心思路是将人类专家的领域知识与大型语言模型（LLMs）的强大文本处理能力相结合，构建一个人机协同的分析框架。通过人类专家设计提示（prompts）来引导LLM进行主题和情感分析，并迭代评估和优化提示的性能，从而提高分析的准确性、效率和可解释性。

**技术框架**：该研究采用混合方法，主要包含以下几个阶段：1) 人类专家基于领域知识和无监督主题建模结果，制定编码手册和编码流程。2) 人类专家设计不同的提示，用于指导GPT-4进行主题和情感分析。3) 使用设计的提示，利用GPT-4对访谈文本进行分析。4) 人类专家评估GPT-4的分析结果，并与人工编码结果进行比较。5) 基于评估结果，迭代优化提示，提高GPT-4的分析性能。

**关键创新**：该研究的关键创新在于将大型语言模型（LLMs）应用于政策利益相关者访谈文本的分析，并探索了人机协同的分析模式。通过提示工程，引导LLM进行主题和情感分析，克服了传统NLP方法在理解细微语义和领域知识方面的局限性。

**关键设计**：研究中关键的设计包括：1) 提示的设计：设计不同的提示，以引导GPT-4进行主题和情感分析，并迭代优化提示的性能。2) 评估指标的选择：选择合适的评估指标，用于评估GPT-4的分析结果，并与人工编码结果进行比较。3) 迭代优化：基于评估结果，迭代优化提示，提高GPT-4的分析性能。

## 📊 实验亮点

实验结果表明，GPT-4在主题编码方面与人类编码的对齐度最高可达96.02%，超过传统NLP方法25%以上。GPT-4的情感分析结果与专家情感分析的匹配度也高于基于词典的方法。这些结果表明，LLM在政策文本分析中具有巨大的潜力，可以显著提高分析的效率和准确性。

## 🎯 应用场景

该研究成果可应用于教育政策、公共卫生、社会福利等多个领域，帮助政策制定者快速、准确地了解利益相关者的观点和情感，从而制定更加科学、合理的政策。该方法还可用于分析大规模的文本数据，例如社交媒体评论、在线论坛帖子等，为舆情分析、市场调研等提供支持。

## 📄 摘要（原文）

> Obtaining stakeholders' diverse experiences and opinions about current policy in a timely manner is crucial for policymakers to identify strengths and gaps in resource allocation, thereby supporting effective policy design and implementation. However, manually coding even moderately sized interview texts or open-ended survey responses from stakeholders can often be labor-intensive and time-consuming. This study explores the integration of Large Language Models (LLMs)--like GPT-4--with human expertise to enhance text analysis of stakeholder interviews regarding K-12 education policy within one U.S. state. Employing a mixed-methods approach, human experts developed a codebook and coding processes as informed by domain knowledge and unsupervised topic modeling results. They then designed prompts to guide GPT-4 analysis and iteratively evaluate different prompts' performances. This combined human-computer method enabled nuanced thematic and sentiment analysis. Results reveal that while GPT-4 thematic coding aligned with human coding by 77.89% at specific themes, expanding to broader themes increased congruence to 96.02%, surpassing traditional Natural Language Processing (NLP) methods by over 25%. Additionally, GPT-4 is more closely matched to expert sentiment analysis than lexicon-based methods. Findings from quantitative measures and qualitative reviews underscore the complementary roles of human domain expertise and automated analysis as LLMs offer new perspectives and coding consistency. The human-computer interactive approach enhances efficiency, validity, and interpretability of educational policy research.

