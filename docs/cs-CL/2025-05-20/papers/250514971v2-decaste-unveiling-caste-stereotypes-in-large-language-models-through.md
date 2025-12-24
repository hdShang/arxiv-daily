---
layout: default
title: "DECASTE: Unveiling Caste Stereotypes in Large Language Models through Multi-Dimensional Bias Analysis"
---

# DECASTE: Unveiling Caste Stereotypes in Large Language Models through Multi-Dimensional Bias Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14971" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14971v2</a>
  <a href="https://arxiv.org/pdf/2505.14971.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14971v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14971v2', 'DECASTE: Unveiling Caste Stereotypes in Large Language Models through Multi-Dimensional Bias Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prashanth Vijayaraghavan, Soroush Vosoughi, Lamogha Chiazor, Raya Horesh, Rogerio Abreu de Paula, Ehsan Degan, Vandana Mukherjee

**分类**: cs.CL, cs.CY

**发布日期**: 2025-05-20 (更新: 2025-06-05)

**备注**: 7 (content pages) + 2 (reference pages) + 5 (Appendix pages), 5 figures, 6 Tables, IJCAI 2025

---

## 💡 一句话要点

**提出DECASTE框架以揭示大语言模型中的种姓偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `种姓偏见` `大语言模型` `多维度评估` `自然语言处理` `社会公正` `人工智能伦理`

## 📋 核心要点

1. 现有的大语言模型在处理种姓偏见方面存在显著不足，尤其是对印度边缘化种姓群体的偏见未得到充分关注。
2. DECASTE框架通过多维度评估方法，系统性地检测和分析LLMs中的种姓偏见，涵盖社会文化、经济、教育和政治四个维度。
3. 实验结果显示，主导种姓与被压迫种姓之间的偏见评分存在显著差异，揭示了模型输出中潜在的社会偏见。

## 📝 摘要（中文）

近年来，大语言模型（LLMs）的进步彻底改变了自然语言处理（NLP）领域，并扩展了其在各个领域的应用。然而，尽管这些模型表现出色，但它们也反映并延续了有害的社会偏见，尤其是基于种姓的偏见。本文提出了DECASTE，一个新颖的多维框架，用于检测和评估LLMs中的隐性和显性种姓偏见。该方法从社会文化、经济、教育和政治四个维度评估种姓公平性，并通过多种定制化提示策略进行评估。实验结果表明，当前的LLMs系统性地强化了种姓偏见，尤其是在对待被压迫与主导种姓群体时存在显著差异。这些发现强调了在实际应用中评估此类模型潜在风险的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型中存在的种姓偏见问题，尤其是对印度边缘化种姓群体的偏见。现有方法未能充分评估和揭示这些隐性和显性偏见的影响。

**核心思路**：DECASTE框架通过多维度的评估方法，结合定制化的提示策略，全面检测和分析种姓偏见，力求揭示模型输出中的社会偏见。

**技术框架**：该框架包括四个主要模块：社会文化、经济、教育和政治维度的评估。每个模块通过特定的提示策略进行数据收集和分析，以评估模型的种姓公平性。

**关键创新**：DECASTE的创新之处在于其多维度评估方法，能够系统性地分析和比较不同种姓群体的偏见表现，填补了现有研究的空白。

**关键设计**：在设计中，采用了多种定制化的提示策略，以确保对不同维度的全面覆盖。同时，评估过程中使用了特定的偏见评分机制，以量化不同种姓群体的偏见程度。

## 📊 实验亮点

实验结果表明，当前的LLMs在对待被压迫种姓（如达利特和舒德拉）与主导种姓群体时，偏见评分显著提高，显示出模型输出中潜在的社会偏见。这一发现强调了在实际应用中对模型进行全面偏见评估的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、社会科学研究和人工智能伦理等。通过揭示和评估种姓偏见，DECASTE框架可以帮助开发更公平和包容的语言模型，减少社会偏见在技术应用中的影响，促进社会公正。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have revolutionized natural language processing (NLP) and expanded their applications across diverse domains. However, despite their impressive capabilities, LLMs have been shown to reflect and perpetuate harmful societal biases, including those based on ethnicity, gender, and religion. A critical and underexplored issue is the reinforcement of caste-based biases, particularly towards India's marginalized caste groups such as Dalits and Shudras. In this paper, we address this gap by proposing DECASTE, a novel, multi-dimensional framework designed to detect and assess both implicit and explicit caste biases in LLMs. Our approach evaluates caste fairness across four dimensions: socio-cultural, economic, educational, and political, using a range of customized prompting strategies. By benchmarking several state-of-the-art LLMs, we reveal that these models systematically reinforce caste biases, with significant disparities observed in the treatment of oppressed versus dominant caste groups. For example, bias scores are notably elevated when comparing Dalits and Shudras with dominant caste groups, reflecting societal prejudices that persist in model outputs. These results expose the subtle yet pervasive caste biases in LLMs and emphasize the need for more comprehensive and inclusive bias evaluation methodologies that assess the potential risks of deploying such models in real-world contexts.

