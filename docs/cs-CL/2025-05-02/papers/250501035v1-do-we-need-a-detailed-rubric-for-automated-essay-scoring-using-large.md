---
layout: default
title: Do We Need a Detailed Rubric for Automated Essay Scoring using Large Language Models?
---

# Do We Need a Detailed Rubric for Automated Essay Scoring using Large Language Models?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01035" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01035v1</a>
  <a href="https://arxiv.org/pdf/2505.01035.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01035v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01035v1', 'Do We Need a Detailed Rubric for Automated Essay Scoring using Large Language Models?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lui Yoshida

**分类**: cs.CL

**发布日期**: 2025-05-02

**备注**: Accepted in AIED 2025. This preprint has not undergone any post-submission improvements or corrections

---

## 💡 一句话要点

**探讨简化评分标准在自动化作文评分中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化作文评分` `大型语言模型` `评分标准` `教育技术` `机器学习`

## 📋 核心要点

1. 现有的基于LLM的自动化作文评分方法通常依赖详细的评分标准，但创建这些标准既耗时又增加了计算成本。
2. 本研究提出通过比较不同细节水平的评分标准，评估其对评分准确性的影响，以寻找更高效的评分方法。
3. 实验结果表明，简化评分标准在大多数情况下能够保持评分准确性，同时显著降低令牌使用，表明其在实际应用中的潜力。

## 📝 摘要（中文）

本研究探讨了在使用大型语言模型（LLMs）进行自动化作文评分（AES）时，详细评分标准的必要性和影响。尽管在基于LLM的AES中使用评分标准是常规做法，但创建详细评分标准需要大量的努力并增加了令牌使用量。我们使用TOEFL11数据集，考察了不同评分标准细节水平对多种LLM评分准确性的影响。实验比较了完整评分标准、简化评分标准和无评分标准三种条件，使用了四种不同的LLM（Claude 3.5 Haiku、Gemini 1.5 Flash、GPT-4o-mini和Llama 3 70B Instruct）。结果显示，四种模型中有三种在使用简化评分标准时保持了与详细评分标准相似的评分准确性，同时显著减少了令牌使用。然而，一种模型（Gemini 1.5 Flash）在使用更详细评分标准时表现下降。研究结果表明，简化评分标准可能足以满足大多数基于LLM的AES应用，提供了一种更高效的替代方案而不影响评分准确性。

## 🔬 方法详解

**问题定义**：本研究旨在解决在自动化作文评分中，详细评分标准的必要性及其对评分准确性的影响。现有方法在创建详细评分标准时面临高成本和复杂性的问题。

**核心思路**：本研究通过比较完整、简化和无评分标准的三种条件，探讨不同评分标准细节对多种LLM评分准确性的影响，以寻找一种更高效的评分方式。

**技术框架**：研究使用TOEFL11数据集，选取四种不同的LLM进行实验，分别在三种评分标准条件下进行评分，比较其准确性和令牌使用情况。

**关键创新**：本研究的主要创新在于提出了简化评分标准的有效性，发现其在保持评分准确性的同时，显著降低了计算资源的消耗，这与传统依赖详细评分标准的方法形成了鲜明对比。

**关键设计**：实验中使用了四种不同的LLM（Claude 3.5 Haiku、Gemini 1.5 Flash、GPT-4o-mini和Llama 3 70B Instruct），并通过对比分析不同评分标准下的评分结果，评估其性能差异。

## 📊 实验亮点

实验结果显示，三种模型在使用简化评分标准时，评分准确性与使用详细评分标准相当，同时令牌使用量显著减少，表明简化评分标准在大多数情况下是有效的。然而，Gemini 1.5 Flash模型在使用详细评分标准时表现下降，强调了模型特异性评估的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线写作评估和语言学习等。通过优化评分标准的设计，可以提高自动化作文评分系统的效率，降低教育机构的运营成本，同时保持评分的准确性。这一研究为未来基于LLM的教育应用提供了重要的理论基础和实践指导。

## 📄 摘要（原文）

> This study investigates the necessity and impact of a detailed rubric in automated essay scoring (AES) using large language models (LLMs). While using rubrics are standard in LLM-based AES, creating detailed rubrics requires substantial ef-fort and increases token usage. We examined how different levels of rubric detail affect scoring accuracy across multiple LLMs using the TOEFL11 dataset. Our experiments compared three conditions: a full rubric, a simplified rubric, and no rubric, using four different LLMs (Claude 3.5 Haiku, Gemini 1.5 Flash, GPT-4o-mini, and Llama 3 70B Instruct). Results showed that three out of four models maintained similar scoring accuracy with the simplified rubric compared to the detailed one, while significantly reducing token usage. However, one model (Gemini 1.5 Flash) showed decreased performance with more detailed rubrics. The findings suggest that simplified rubrics may be sufficient for most LLM-based AES applications, offering a more efficient alternative without compromis-ing scoring accuracy. However, model-specific evaluation remains crucial as per-formance patterns vary across different LLMs.

