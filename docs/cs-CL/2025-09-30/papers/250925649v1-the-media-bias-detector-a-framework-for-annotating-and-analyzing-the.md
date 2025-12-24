---
layout: default
title: "The Media Bias Detector: A Framework for Annotating and Analyzing the News at Scale"
---

# The Media Bias Detector: A Framework for Annotating and Analyzing the News at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25649" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25649v1</a>
  <a href="https://arxiv.org/pdf/2509.25649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25649v1', 'The Media Bias Detector: A Framework for Annotating and Analyzing the News at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samar Haider, Amir Tohidi, Jenny S. Wang, Timothy Dörr, David M. Rothschild, Chris Callison-Burch, Duncan J. Watts

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出Media Bias Detector框架，用于大规模标注和分析新闻媒体的偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `媒体偏见检测` `大型语言模型` `新闻分析` `自然语言处理` `情感分析`

## 📋 核心要点

1. 现有方法难以大规模测量媒体在选题和框架上的微妙偏见，阻碍了对媒体偏见的系统性研究。
2. 利用大型语言模型和实时新闻抓取，自动提取政治倾向、语气等结构化标注，实现多层次的偏见量化。
3. 构建了包含大量新闻文章的数据集和交互式平台，揭示了新闻报道中的偏见模式，并促进媒体问责。

## 📝 摘要（中文）

本文介绍了一个大型的、持续更新的（从2024年1月1日至今）、近乎实时的数据集和计算框架，旨在系统地研究新闻报道中的选择性偏见和框架性偏见。该流程将大型语言模型（LLM）与可扩展的、近实时的新闻抓取相结合，以提取结构化的标注信息，包括政治倾向、语气、主题、文章类型和重大事件，每天处理数百篇文章。我们在多个层面（句子层面、文章层面和出版商层面）量化这些报道维度，从而扩展了研究人员在现代新闻环境中分析媒体偏见的方式。除了精心策划的数据集外，我们还发布了一个交互式网络平台，方便用户探索这些数据。这些贡献共同建立了一种可重用的方法，用于大规模研究媒体偏见，为未来的研究提供实证资源。利用语料库在时间和出版商之间的广度，我们还展示了一些例子（重点关注2024年审查的15万多篇文章），说明了这种新颖的数据集如何揭示新闻报道和偏见中的深刻模式，从而支持学术研究和改善媒体问责制的实际工作。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模新闻报道中媒体偏见难以检测和量化的问题。现有方法在处理海量数据、捕捉细微偏见以及提供结构化分析方面存在不足，使得系统性研究和媒体问责变得困难。

**核心思路**：核心思路是结合大型语言模型（LLM）的语义理解能力和实时新闻抓取技术，构建一个自动化、可扩展的框架，用于提取新闻文章的结构化标注信息，从而量化和分析媒体偏见。通过在句子、文章和出版商等多个层面进行分析，可以更全面地理解媒体偏见的表现形式。

**技术框架**：该框架包含以下主要模块：1) 近实时新闻抓取模块，负责从多个新闻来源抓取文章；2) LLM标注模块，利用LLM提取文章的政治倾向、语气、主题、文章类型和重大事件等信息；3) 多层次分析模块，在句子、文章和出版商层面量化和分析媒体偏见；4) 交互式网络平台，用于展示和探索数据集。

**关键创新**：关键创新在于将LLM应用于大规模新闻偏见分析，并构建了一个端到端的自动化流程。与传统的人工标注或基于规则的方法相比，该方法具有更高的效率、可扩展性和准确性。此外，多层次分析方法能够更全面地揭示媒体偏见的表现形式。

**关键设计**：LLM标注模块是关键，需要选择合适的LLM模型，并设计有效的提示工程（prompt engineering）来指导LLM提取所需的信息。此外，还需要设计合适的指标来量化不同层面的媒体偏见，例如，可以使用情感分析来衡量文章的语气，使用主题模型来识别文章的主题。

## 📊 实验亮点

该研究构建了一个包含2024年15万多篇文章的大型数据集，并展示了如何利用该数据集揭示新闻报道中的偏见模式。例如，研究发现不同出版商在报道同一事件时，可能存在政治倾向和框架上的差异。此外，交互式网络平台为研究人员提供了一个方便的工具，用于探索和分析媒体偏见。

## 🎯 应用场景

该研究成果可应用于多个领域，包括：媒体素养教育，帮助公众识别和理解媒体偏见；新闻推荐系统，减少用户接触偏见信息的可能性；媒体问责机制，促进新闻报道的客观性和公正性；以及社会科学研究，深入分析媒体偏见对社会舆论和政治生态的影响。

## 📄 摘要（原文）

> Mainstream news organizations shape public perception not only directly through the articles they publish but also through the choices they make about which topics to cover (or ignore) and how to frame the issues they do decide to cover. However, measuring these subtle forms of media bias at scale remains a challenge. Here, we introduce a large, ongoing (from January 1, 2024 to present), near real-time dataset and computational framework developed to enable systematic study of selection and framing bias in news coverage. Our pipeline integrates large language models (LLMs) with scalable, near-real-time news scraping to extract structured annotations -- including political lean, tone, topics, article type, and major events -- across hundreds of articles per day. We quantify these dimensions of coverage at multiple levels -- the sentence level, the article level, and the publisher level -- expanding the ways in which researchers can analyze media bias in the modern news landscape. In addition to a curated dataset, we also release an interactive web platform for convenient exploration of these data. Together, these contributions establish a reusable methodology for studying media bias at scale, providing empirical resources for future research. Leveraging the breadth of the corpus over time and across publishers, we also present some examples (focused on the 150,000+ articles examined in 2024) that illustrate how this novel data set can reveal insightful patterns in news coverage and bias, supporting academic research and real-world efforts to improve media accountability.

