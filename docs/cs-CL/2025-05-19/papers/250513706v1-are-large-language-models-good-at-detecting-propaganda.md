---
layout: default
title: Are Large Language Models Good at Detecting Propaganda?
---

# Are Large Language Models Good at Detecting Propaganda?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13706" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13706v1</a>
  <a href="https://arxiv.org/pdf/2505.13706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13706v1', 'Are Large Language Models Good at Detecting Propaganda?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julia Jose, Rachel Greenstadt

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19

**期刊**: Workshop Proceedings of the 18th International AAAI Conference on Web and Social Media (5th International Workshop on Cyber Social Threats, CySoc 2024). AAAI Press

**DOI**: [10.36190/2024.06](https://doi.org/10.36190/2024.06)

---

## 💡 一句话要点

**评估大型语言模型在宣传检测中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `宣传检测` `自然语言处理` `情感分析` `逻辑谬误`

## 📋 核心要点

1. 现有方法在识别宣传技术方面存在不足，尤其是在复杂的情感和逻辑操控内容的检测上。
2. 本研究通过比较不同大型语言模型的性能，探索其在检测新闻文章中宣传技术的有效性。
3. 实验结果表明，GPT-4的F1分数为0.16，虽然优于其他模型，但仍低于RoBERTa-CRF的0.67基线。

## 📝 摘要（中文）

宣传者利用逻辑谬误和情感诉求的修辞手法来推动其议程。识别这些技术对于做出明智决策至关重要。随着自然语言处理（NLP）的进步，开发出能够检测操控内容的系统成为可能。本研究考察了几种大型语言模型在新闻文章中检测宣传技术的表现，并将其与基于变换器的模型进行比较。结果显示，尽管GPT-4在F1分数上优于GPT-3.5和Claude 3 Opus，但仍未能超越RoBERTa-CRF基线。此外，所有三种LLM在检测六种宣传技术中的一种（抨击）时表现优于多粒度网络（MGN）基线，GPT-3.5和GPT-4在检测恐惧诉求和旗帜挥舞方面也表现更佳。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在检测新闻文章中的宣传技术时的有效性问题。现有方法在处理复杂的宣传手法时表现不佳，尤其是在逻辑谬误和情感操控的识别上存在挑战。

**核心思路**：论文通过比较多种大型语言模型（如GPT-4、GPT-3.5和Claude 3 Opus）与传统模型（如RoBERTa-CRF）的表现，评估其在识别宣传技术方面的能力，旨在找出最有效的检测方法。

**技术框架**：研究设计了一个实验框架，包含数据集的构建、模型的训练与评估，主要模块包括数据预处理、模型训练、性能评估和结果分析。

**关键创新**：论文的创新点在于系统性地比较了多种大型语言模型与传统模型在宣传检测中的表现，揭示了大型语言模型在特定宣传技术（如抨击、恐惧诉求等）检测中的优势与局限。

**关键设计**：在模型训练中，采用了标准的F1分数作为性能评估指标，重点关注不同模型在多种宣传技术识别中的表现差异。

## 📊 实验亮点

实验结果显示，GPT-4在F1分数上为0.16，优于GPT-3.5和Claude 3 Opus，但未能超越RoBERTa-CRF的0.67基线。此外，所有三种LLM在检测抨击技术时表现优于MGN基线，GPT-3.5和GPT-4在恐惧诉求和旗帜挥舞的检测中也表现更佳。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体、社交网络和信息验证平台。通过提高对宣传内容的检测能力，可以帮助用户做出更明智的决策，减少误导信息的传播，增强公众对信息的批判性思维能力。

## 📄 摘要（原文）

> Propagandists use rhetorical devices that rely on logical fallacies and emotional appeals to advance their agendas. Recognizing these techniques is key to making informed decisions. Recent advances in Natural Language Processing (NLP) have enabled the development of systems capable of detecting manipulative content. In this study, we look at several Large Language Models and their performance in detecting propaganda techniques in news articles. We compare the performance of these LLMs with transformer-based models. We find that, while GPT-4 demonstrates superior F1 scores (F1=0.16) compared to GPT-3.5 and Claude 3 Opus, it does not outperform a RoBERTa-CRF baseline (F1=0.67). Additionally, we find that all three LLMs outperform a MultiGranularity Network (MGN) baseline in detecting instances of one out of six propaganda techniques (name-calling), with GPT-3.5 and GPT-4 also outperforming the MGN baseline in detecting instances of appeal to fear and flag-waving.

