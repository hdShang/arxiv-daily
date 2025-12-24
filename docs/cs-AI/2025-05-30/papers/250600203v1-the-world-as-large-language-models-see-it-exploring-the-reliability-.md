---
layout: default
title: "The World As Large Language Models See It: Exploring the reliability of LLMs in representing geographical features"
---

# The World As Large Language Models See It: Exploring the reliability of LLMs in representing geographical features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00203" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00203v1</a>
  <a href="https://arxiv.org/pdf/2506.00203.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00203v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00203v1', 'The World As Large Language Models See It: Exploring the reliability of LLMs in representing geographical features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omid Reza Abbasi, Franz Welscher, Georg Weinberger, Johannes Scholz

**分类**: cs.CY, cs.AI, cs.IR

**发布日期**: 2025-05-30

**备注**: 9 pages, 4 figures, 2 tables

---

## 💡 一句话要点

**评估大型语言模型在地理特征表示中的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `地理信息` `地理编码` `高程估计` `反向地理编码` `GIS` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在地理信息的准确表示上存在系统性和随机性误差，影响其可信度。
2. 本研究通过评估GPT-4o和Gemini 2.0 Flash在三项地理空间任务中的表现，探讨其在地理信息表示中的有效性。
3. 实验结果表明，Gemini 2.0 Flash在反向地理编码任务中表现优于GPT-4o，但两者在准确重建奥地利联邦州方面均存在不足。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的不断发展，关于其在提供事实信息方面的可信度问题变得愈发重要。本研究评估了GPT-4o和Gemini 2.0 Flash在地理编码、高程估计和反向地理编码三项关键地理空间任务中的表现。结果显示，尽管LLMs能够近似地理信息，但其准确性和可靠性不一致，强调了对地理信息进行微调的必要性，以增强其在地理信息科学和地理信息学中的实用性。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在地理特征表示中的准确性和可靠性问题。现有方法在地理编码和反向地理编码任务中存在系统性误差和不一致性，导致地理信息的表示不够准确。

**核心思路**：通过对比GPT-4o和Gemini 2.0 Flash在三项地理空间任务中的表现，评估其在地理信息表示中的有效性，进而提出对模型进行地理信息微调的建议。

**技术框架**：研究采用了三项主要任务：地理编码、地形高程估计和反向地理编码。每项任务都通过对模型输出与真实地理数据的比较来评估其性能。

**关键创新**：本研究的创新在于系统性地评估了两种大型语言模型在地理空间任务中的表现，揭示了它们在地理信息表示中的局限性，并提出了针对性的改进建议。

**关键设计**：在实验中，使用了真实的地理坐标和高程数据作为基准，评估模型的输出精度，并计算F1分数来衡量反向地理编码的准确性。

## 📊 实验亮点

实验结果显示，Gemini 2.0 Flash在反向地理编码任务中整体准确性和F1分数均优于GPT-4o，尤其在东部地区表现更佳。然而，两者在准确重建奥地利联邦州方面均未达到理想效果，显示出持续的误分类问题。

## 🎯 应用场景

该研究的潜在应用领域包括地理信息系统（GIS）、地理信息科学和相关领域的研究与开发。通过提高大型语言模型在地理信息表示中的准确性，可以增强其在实际应用中的可靠性，推动智能地图、导航系统等技术的发展。

## 📄 摘要（原文）

> As large language models (LLMs) continue to evolve, questions about their trustworthiness in delivering factual information have become increasingly important. This concern also applies to their ability to accurately represent the geographic world. With recent advancements in this field, it is relevant to consider whether and to what extent LLMs' representations of the geographical world can be trusted. This study evaluates the performance of GPT-4o and Gemini 2.0 Flash in three key geospatial tasks: geocoding, elevation estimation, and reverse geocoding. In the geocoding task, both models exhibited systematic and random errors in estimating the coordinates of St. Anne's Column in Innsbruck, Austria, with GPT-4o showing greater deviations and Gemini 2.0 Flash demonstrating more precision but a significant systematic offset. For elevation estimation, both models tended to underestimate elevations across Austria, though they captured overall topographical trends, and Gemini 2.0 Flash performed better in eastern regions. The reverse geocoding task, which involved identifying Austrian federal states from coordinates, revealed that Gemini 2.0 Flash outperformed GPT-4o in overall accuracy and F1-scores, demonstrating better consistency across regions. Despite these findings, neither model achieved an accurate reconstruction of Austria's federal states, highlighting persistent misclassifications. The study concludes that while LLMs can approximate geographic information, their accuracy and reliability are inconsistent, underscoring the need for fine-tuning with geographical information to enhance their utility in GIScience and Geoinformatics.

