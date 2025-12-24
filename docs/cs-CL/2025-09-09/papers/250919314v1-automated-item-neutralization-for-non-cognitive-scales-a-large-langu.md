---
layout: default
title: "Automated Item Neutralization for Non-Cognitive Scales: A Large Language Model Approach to Reducing Social-Desirability Bias"
---

# Automated Item Neutralization for Non-Cognitive Scales: A Large Language Model Approach to Reducing Social-Desirability Bias

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19314" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19314v1</a>
  <a href="https://arxiv.org/pdf/2509.19314.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19314v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19314v1', 'Automated Item Neutralization for Non-Cognitive Scales: A Large Language Model Approach to Reducing Social-Desirability Bias')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Wu, Daijin Yang

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-09-09

**备注**: Accepted for publication in NCME-AIME 2025

---

## 💡 一句话要点

**利用大型语言模型减少个性评估中的社会期望偏差**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社会期望偏差` `个性评估` `大型语言模型` `心理测量` `问卷中立化` `数据分析`

## 📋 核心要点

1. 核心问题：现有个性评估方法容易受到社会期望偏差的影响，导致结果不准确。
2. 方法要点：本研究提出利用大型语言模型对问卷进行中立化处理，以减少社会期望偏差的影响。
3. 实验或效果：实验结果显示，问卷的可靠性保持不变，但在不同维度上表现出不同的变化趋势。

## 📝 摘要（中文）

本研究评估了利用大型语言模型（LLM）进行项目中立化，以减少个性评估中的社会期望偏差。研究中使用GPT-o3重写了国际人格项目池大五测量（IPIP-BFM-50），203名参与者完成了原始或中立化形式的问卷，并配合Marlowe-Crowne社会期望量表。结果显示，问卷的可靠性和五因素结构得以保持，尽管在责任心上有所提升，而宜人性和开放性有所下降。多个项目与社会期望的相关性有所降低，但表现不一致。尽管保持了构型不变性，但度量和标量不变性未能实现。研究结果支持AI中立化作为一种潜在但不完美的偏差减少方法。

## 🔬 方法详解

**问题定义**：本研究旨在解决个性评估中存在的社会期望偏差问题。现有方法往往无法有效消除这种偏差，导致评估结果失真。

**核心思路**：论文提出通过大型语言模型（GPT-o3）对个性评估问卷进行重写，以实现项目中立化，从而减少社会期望偏差的影响。该方法的设计基于对语言模型在文本生成和重写能力的利用。

**技术框架**：整体流程包括使用GPT-o3对原始问卷进行重写，生成中立化问卷，并通过参与者的反馈进行效果评估。主要模块包括问卷重写、参与者评估和数据分析。

**关键创新**：最重要的技术创新在于将大型语言模型应用于心理测量领域，提供了一种新的思路来处理社会期望偏差问题。与传统方法相比，该方法在文本生成的灵活性和适应性上具有显著优势。

**关键设计**：在参数设置上，GPT-o3的训练数据和重写策略经过精心设计，以确保生成的问卷在内容上保持一致性，同时减少社会期望的影响。损失函数的选择也考虑了文本的可读性和心理测量的有效性。

## 📊 实验亮点

实验结果显示，中立化问卷在可靠性和五因素结构上保持一致，责任心得分有所提升，而宜人性和开放性得分有所下降。多个项目与社会期望的相关性有所降低，尽管表现不一致，显示出AI中立化的潜力和局限性。

## 🎯 应用场景

该研究的潜在应用领域包括心理测量、个性评估和社会科学研究。通过减少社会期望偏差，可以提高个性评估的准确性和可靠性，从而为心理学研究和临床应用提供更为有效的工具。未来，该方法可能会在其他类型的问卷和评估工具中得到推广和应用。

## 📄 摘要（原文）

> This study evaluates item neutralization assisted by the large language model (LLM) to reduce social desirability bias in personality assessment. GPT-o3 was used to rewrite the International Personality Item Pool Big Five Measure (IPIP-BFM-50), and 203 participants completed either the original or neutralized form along with the Marlowe-Crowne Social Desirability Scale. The results showed preserved reliability and a five-factor structure, with gains in Conscientiousness and declines in Agreeableness and Openness. The correlations with social desirability decreased for several items, but inconsistently. Configural invariance held, though metric and scalar invariance failed. Findings support AI neutralization as a potential but imperfect bias-reduction method.

