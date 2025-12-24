---
layout: default
title: "Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models"
---

# Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20269" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20269v1</a>
  <a href="https://arxiv.org/pdf/2506.20269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20269v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20269v1', 'Narrative Shift Detection: A Hybrid Approach of Dynamic Topic Models and Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai-Robin Lange, Tobias Schmidt, Matthias Reccius, Henrik Müller, Michael Roos, Carsten Jentsch

**分类**: cs.CL, econ.GN

**发布日期**: 2025-06-25

**备注**: 14 pages, 1 figure

**期刊**: Proceedings of the Text2Story'25 Workshop (2025), 67-80

---

## 💡 一句话要点

**提出动态主题模型与大语言模型结合以检测叙事转变**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `叙事转变` `动态主题模型` `大语言模型` `变更点检测` `媒体分析` `政策研究`

## 📋 核心要点

1. 现有的叙事提取方法在处理整个语料库时面临高财务和计算成本等挑战。
2. 论文提出将大语言模型与主题模型结合，动态建模叙事转变，利用叙事政策框架进行分析。
3. 实验结果显示，大语言模型能够有效识别叙事转变，但在区分内容与叙事转变时效果不佳。

## 📝 摘要（中文）

随着媒体叙事的快速演变，提取叙事并研究其随时间的发展变得愈发重要。尽管现有的叙事提取方法如大语言模型在捕捉叙事元素和结构方面表现良好，但在整个语料库中应用时面临高成本等挑战。本文提出将大语言模型的语言理解能力与主题模型的广泛适用性相结合，利用叙事政策框架动态建模叙事转变。通过主题模型和变更点检测方法，识别特定主题的变化，并利用大语言模型自动解释这些变化，区分内容和叙事转变。我们在2009至2023年的《华尔街日报》文章语料库上应用了这一模型，结果表明大语言模型能够有效提取叙事转变，但在判断内容转变与叙事转变时表现不佳。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效检测叙事转变的问题，现有方法在处理大规模语料时面临高成本和效率低下的挑战。

**核心思路**：通过结合大语言模型的语言理解能力与主题模型的动态分析能力，提出一种新的方法来捕捉叙事随时间的变化。这样的设计旨在提高叙事分析的效率和准确性。

**技术框架**：整体架构包括主题模型用于识别特定主题的变化，变更点检测方法用于定位变化点，最后将相关文档输入大语言模型进行自动解释。

**关键创新**：本研究的创新点在于将大语言模型与主题模型结合，形成一个动态分析框架，能够更好地捕捉叙事转变的细微变化。与传统方法相比，这种方法在处理大规模数据时更具优势。

**关键设计**：在模型设计中，选择了合适的主题模型和变更点检测算法，设置了优化的参数以提高模型的准确性和效率，同时确保大语言模型能够有效处理输入的文档。

## 📊 实验亮点

实验结果表明，所提出的方法能够有效提取叙事转变，尤其是在特定时间点上。然而，在判断内容转变与叙事转变的准确性上，模型的表现相对较弱，提示未来需要进一步优化。具体性能数据和对比基线未在摘要中详细列出，需查阅完整论文以获取更多信息。

## 🎯 应用场景

该研究的潜在应用领域包括新闻分析、社交媒体监测和政策研究等。通过动态检测叙事转变，能够为决策者提供更为精准的信息支持，帮助他们理解公众舆论的变化及其背后的原因，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With rapidly evolving media narratives, it has become increasingly critical to not just extract narratives from a given corpus but rather investigate, how they develop over time. While popular narrative extraction methods such as Large Language Models do well in capturing typical narrative elements or even the complex structure of a narrative, applying them to an entire corpus comes with obstacles, such as a high financial or computational cost. We propose a combination of the language understanding capabilities of Large Language Models with the large scale applicability of topic models to dynamically model narrative shifts across time using the Narrative Policy Framework. We apply a topic model and a corresponding change point detection method to find changes that concern a specific topic of interest. Using this model, we filter our corpus for documents that are particularly representative of that change and feed them into a Large Language Model that interprets the change that happened in an automated fashion and distinguishes between content and narrative shifts. We employ our pipeline on a corpus of The Wall Street Journal news paper articles from 2009 to 2023. Our findings indicate that a Large Language Model can efficiently extract a narrative shift if one exists at a given point in time, but does not perform as well when having to decide whether a shift in content or a narrative shift took place.

