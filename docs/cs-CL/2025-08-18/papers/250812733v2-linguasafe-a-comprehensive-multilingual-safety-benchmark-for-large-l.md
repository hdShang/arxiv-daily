---
layout: default
title: "LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models"
---

# LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12733" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12733v2</a>
  <a href="https://arxiv.org/pdf/2508.12733.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12733v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12733v2', 'LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Ning, Tianle Gu, Jiaxin Song, Shixin Hong, Lingyu Li, Huacan Liu, Jie Li, Yixu Wang, Meng Lingyu, Yan Teng, Yingchun Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-18 (更新: 2025-08-27)

**备注**: 7pages, 5 figures

---

## 💡 一句话要点

**提出LinguaSafe以解决多语言安全评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言模型` `安全评估` `数据集构建` `评估框架` `低资源语言` `大型语言模型` `多维度评估`

## 📋 核心要点

1. 现有多语言安全评估缺乏全面性和多样性，限制了大型语言模型的安全性研究。
2. LinguaSafe通过构建包含12种语言的45,000条数据集，提供了多维度的安全评估框架，解决了现有评估的不足。
3. 实验结果显示，不同领域和语言的安全性和有用性评估存在显著差异，强调了多语言安全评估的重要性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在全球技术中的广泛应用，确保其在多样语言和文化背景下的安全性变得至关重要。然而，现有的多语言安全评估缺乏全面性和多样性，限制了其有效性。为此，本文提出了LinguaSafe，一个全面的多语言安全基准，包含12种语言的45,000条数据，旨在填补多语言安全评估的空白。LinguaSafe提供了多维度的细粒度评估框架，涵盖直接和间接的安全评估，强调了在不同领域和语言中的安全性和有用性评估的重要性。我们的数据集和代码已公开发布，以促进多语言LLM安全领域的进一步研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多语言安全评估缺乏全面性和多样性的问题，限制了大型语言模型在不同语言和文化背景下的安全性研究。

**核心思路**：LinguaSafe通过构建一个包含12种语言的综合性数据集，结合翻译、再创作和本土数据，提供多维度的安全评估框架，以填补多语言安全评估的空白。

**技术框架**：LinguaSafe的数据集由45,000条数据组成，涵盖直接和间接的安全评估，设计了细粒度的评估指标，确保对多语言模型的全面评估。

**关键创新**：LinguaSafe的创新在于其多语言数据集的构建和多维度评估框架，特别是在对低资源语言的安全性评估上，与现有方法相比具有显著的优势。

**关键设计**：数据集的构建采用了翻译、再创作和本土数据的组合，确保了语言的真实性和多样性，同时设计了多种评估指标以全面评估模型的安全性和有用性。

## 📊 实验亮点

实验结果表明，LinguaSafe在不同领域和语言的安全性和有用性评估中存在显著差异，尤其是在低资源语言的评估上，提供了全面的评估指标，强调了多语言安全评估的重要性。

## 🎯 应用场景

LinguaSafe的研究成果在多语言大型语言模型的安全性评估中具有广泛的应用潜力，能够帮助开发者和研究人员更好地理解和改进模型在不同语言和文化背景下的表现。未来，该基准有望推动多语言模型的安全性研究，促进更平衡的安全对齐。

## 📄 摘要（原文）

> The widespread adoption and increasing prominence of large language models (LLMs) in global technologies necessitate a rigorous focus on ensuring their safety across a diverse range of linguistic and cultural contexts. The lack of a comprehensive evaluation and diverse data in existing multilingual safety evaluations for LLMs limits their effectiveness, hindering the development of robust multilingual safety alignment. To address this critical gap, we introduce LinguaSafe, a comprehensive multilingual safety benchmark crafted with meticulous attention to linguistic authenticity. The LinguaSafe dataset comprises 45k entries in 12 languages, ranging from Hungarian to Malay. Curated using a combination of translated, transcreated, and natively-sourced data, our dataset addresses the critical need for multilingual safety evaluations of LLMs, filling the void in the safety evaluation of LLMs across diverse under-represented languages from Hungarian to Malay. LinguaSafe presents a multidimensional and fine-grained evaluation framework, with direct and indirect safety assessments, including further evaluations for oversensitivity. The results of safety and helpfulness evaluations vary significantly across different domains and different languages, even in languages with similar resource levels. Our benchmark provides a comprehensive suite of metrics for in-depth safety evaluation, underscoring the critical importance of thoroughly assessing multilingual safety in LLMs to achieve more balanced safety alignment. Our dataset and code are released to the public to facilitate further research in the field of multilingual LLM safety.

