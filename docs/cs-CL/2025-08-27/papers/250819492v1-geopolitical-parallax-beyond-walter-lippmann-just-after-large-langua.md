---
layout: default
title: "Geopolitical Parallax: Beyond Walter Lippmann Just After Large Language Models"
---

# Geopolitical Parallax: Beyond Walter Lippmann Just After Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19492" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19492v1</a>
  <a href="https://arxiv.org/pdf/2508.19492.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19492v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19492v1', 'Geopolitical Parallax: Beyond Walter Lippmann Just After Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehmet Can Yavuz, Humza Gohar Kabir, Aylin Özkan

**分类**: cs.CY, cs.CL

**发布日期**: 2025-08-27

**备注**: 7 pages, 4 figures, 7 tables

---

## 💡 一句话要点

**提出地缘政治视差分析以解决大语言模型偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `新闻质量评估` `文化偏见` `地缘政治` `主观性分析` `算法系统` `媒体偏见`

## 📋 核心要点

1. 现有的新闻报道评估方法未能有效识别和消除模型训练数据中的文化或意识形态偏见。
2. 本文通过比较中西方大语言模型的文章嵌入，提出了一种新的评估框架，旨在揭示模型偏见对新闻质量的影响。
3. 实验结果表明，西方模型在巴勒斯坦相关报道中表现出更高的主观性和积极情感分数，而中国模型则更注重新颖性和描述性。

## 📝 摘要（中文）

新闻报道中的客观性长期以来备受争议，面临中立与主观框架之间的张力。随着大语言模型（LLMs）的出现，这些张力通过算法系统得以调解。本文研究了中西方模型在新闻质量和主观性评估上的系统性差异，发现模型来源与评估结果存在一致的非随机偏差，强调了文化校准在LLM媒体评估中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在新闻报道中引入的文化和意识形态偏见问题。现有方法未能充分考虑模型训练数据的多样性和偏见，导致评估结果的不准确性。

**核心思路**：通过比较中西方模型在新闻质量和主观性评估上的表现，本文提出了一种新的评估框架，强调文化背景对模型输出的影响。

**技术框架**：研究使用了人类标注的新闻质量基准，涵盖了十五个风格、信息和情感维度，并通过逻辑回归探测器和匹配主题评估来量化模型间的差异。

**关键创新**：最重要的创新在于系统性地揭示了中西方模型在新闻报道中的偏见差异，扩展了LLM偏见文献，强调了地缘政治框架对质量评估的影响。

**关键设计**：研究中使用了逻辑回归探测器来分析模型输出，并设计了多维度的评估标准，以确保对不同模型的全面比较。

## 📊 实验亮点

实验结果显示，西方模型在巴勒斯坦相关报道中赋予更高的主观性和积极情感分数，而中国模型则在流畅性、简洁性和整体质量上显著低于西方模型，表明模型来源对新闻质量评估的显著影响。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体、社交媒体内容审核和信息传播等。通过文化校准的LLM评估管道，可以提高新闻报道的客观性和准确性，减少模型偏见对公众舆论的影响。

## 📄 摘要（原文）

> Objectivity in journalism has long been contested, oscillating between ideals of neutral, fact-based reporting and the inevitability of subjective framing. With the advent of large language models (LLMs), these tensions are now mediated by algorithmic systems whose training data and design choices may themselves embed cultural or ideological biases. This study investigates geopolitical parallax-systematic divergence in news quality and subjectivity assessments-by comparing article-level embeddings from Chinese-origin (Qwen, BGE, Jina) and Western-origin (Snowflake, Granite) model families. We evaluate both on a human-annotated news quality benchmark spanning fifteen stylistic, informational, and affective dimensions, and on parallel corpora covering politically sensitive topics, including Palestine and reciprocal China-United States coverage. Using logistic regression probes and matched-topic evaluation, we quantify per-metric differences in predicted positive-class probabilities between model families. Our findings reveal consistent, non-random divergences aligned with model origin. In Palestine-related coverage, Western models assign higher subjectivity and positive emotion scores, while Chinese models emphasize novelty and descriptiveness. Cross-topic analysis shows asymmetries in structural quality metrics Chinese-on-US scoring notably lower in fluency, conciseness, technicality, and overall quality-contrasted by higher negative emotion scores. These patterns align with media bias theory and our distinction between semantic, emotional, and relational subjectivity, and extend LLM bias literature by showing that geopolitical framing effects persist in downstream quality assessment tasks. We conclude that LLM-based media evaluation pipelines require cultural calibration to avoid conflating content differences with model-induced bias.

