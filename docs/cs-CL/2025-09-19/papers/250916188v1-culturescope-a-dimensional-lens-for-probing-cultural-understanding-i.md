---
layout: default
title: "CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs"
---

# CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16188" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16188v1</a>
  <a href="https://arxiv.org/pdf/2509.16188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16188v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16188v1', 'CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinghao Zhang, Sihang Jiang, Shiwei Guo, Shisong Chen, Yanghua Xiao, Hongwei Feng, Jiaqing Liang, Minggui HE, Shimin Tao, Hongxia Ma

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19

**🔗 代码/项目**: [GITHUB](https://github.com/HoganZinger/Culture)

---

## 💡 一句话要点

**提出 CultureScope，通过多维度文化知识分类评估LLM的文化理解能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化理解` `大型语言模型` `评估框架` `文化冰山理论` `知识库构建`

## 📋 核心要点

1. 现有文化理解评估基准缺乏理论指导，依赖人工标注，难以扩展到不同文化背景。
2. CultureScope 借鉴文化冰山理论，构建多维度文化知识分类体系，自动生成评估数据集。
3. 实验表明，现有LLM文化理解能力不足，简单引入多语言数据无法有效提升文化理解。

## 📝 摘要（中文）

随着大型语言模型（LLMs）越来越多地部署在不同的文化环境中，评估其文化理解能力对于确保可信和文化对齐的应用至关重要。然而，现有的大多数基准缺乏全面性，并且难以在不同的文化背景下进行扩展和调整，因为它们的框架通常缺乏完善的文化理论的指导，并且倾向于依赖专家驱动的手动注释。为了解决这些问题，我们提出了 CultureScope，这是迄今为止最全面的评估框架，用于评估LLMs中的文化理解。受到文化冰山理论的启发，我们设计了一种新颖的文化知识分类维度模式，包括3层和140个维度，该模式指导自动构建特定于文化的知识库以及针对任何给定语言和文化的相应评估数据集。实验结果表明，我们的方法可以有效地评估文化理解。它们还表明，现有的大型语言模型缺乏全面的文化能力，并且仅仅包含多语言数据并不一定能提高文化理解。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在跨文化应用中面临挑战，缺乏对不同文化的深入理解。现有的评估方法依赖专家标注，成本高昂且难以扩展，缺乏系统性的文化理论支撑，导致评估结果不够全面和客观。因此，如何构建一个全面、可扩展且基于文化理论的评估框架，成为了一个亟待解决的问题。

**核心思路**：CultureScope 的核心思路是借鉴文化冰山理论，将文化知识分为表层、中间层和深层三个层次，并在此基础上构建一个多维度的文化知识分类体系。通过这个体系，可以系统地组织和评估 LLM 对不同文化层面的理解程度。这种分层和多维度的设计，旨在更全面地捕捉文化知识的复杂性，从而更准确地评估 LLM 的文化理解能力。

**技术框架**：CultureScope 的整体框架包括以下几个主要模块：1) 文化知识分类体系构建：基于文化冰山理论，设计包含3层和140个维度的文化知识分类体系。2) 文化知识库自动构建：利用设计的分类体系，自动从各种来源（如维基百科、新闻报道等）抽取特定文化的知识。3) 评估数据集生成：基于知识库，生成包含选择题、问答题等多种形式的评估数据集。4) 模型评估：使用生成的数据集评估 LLM 的文化理解能力，并分析其在不同文化维度上的表现。

**关键创新**：CultureScope 的关键创新在于其基于文化理论的维度化文化知识分类体系。与以往依赖专家标注或简单统计的方法不同，CultureScope 能够系统地组织和评估 LLM 对不同文化层面的理解。此外，CultureScope 实现了文化知识库和评估数据集的自动构建，大大降低了评估成本，提高了可扩展性。

**关键设计**：CultureScope 的关键设计包括：1) 文化知识分类体系的维度划分，需要仔细考虑不同文化层面的特征和关系。2) 知识库自动构建过程中，需要设计有效的抽取算法，以保证知识的准确性和完整性。3) 评估数据集的生成需要保证题目的多样性和难度，以全面评估 LLM 的文化理解能力。4) 评估指标的设计需要能够反映 LLM 在不同文化维度上的表现，例如可以设计针对特定文化价值观的评估指标。

## 📊 实验亮点

实验结果表明，现有 LLM 在 CultureScope 评估框架下的文化理解能力普遍不足，尤其是在深层文化维度上表现较差。即使是经过多语言数据训练的 LLM，其文化理解能力也未得到显著提升。CultureScope 能够有效区分不同 LLM 在文化理解方面的差异，并为进一步提升 LLM 的文化能力提供指导。

## 🎯 应用场景

CultureScope 可应用于评估和提升 LLM 在跨文化交流、智能客服、内容生成等领域的表现。通过 CultureScope，可以帮助开发者了解 LLM 在不同文化背景下的优势和不足，从而有针对性地进行优化，避免文化误解和冲突，提升用户体验。此外，CultureScope 还可以用于文化教育和研究，帮助人们更好地理解和学习不同文化。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly deployed in diverse cultural environments, evaluating their cultural understanding capability has become essential for ensuring trustworthy and culturally aligned applications. However, most existing benchmarks lack comprehensiveness and are challenging to scale and adapt across different cultural contexts, because their frameworks often lack guidance from well-established cultural theories and tend to rely on expert-driven manual annotations. To address these issues, we propose CultureScope, the most comprehensive evaluation framework to date for assessing cultural understanding in LLMs. Inspired by the cultural iceberg theory, we design a novel dimensional schema for cultural knowledge classification, comprising 3 layers and 140 dimensions, which guides the automated construction of culture-specific knowledge bases and corresponding evaluation datasets for any given languages and cultures. Experimental results demonstrate that our method can effectively evaluate cultural understanding. They also reveal that existing large language models lack comprehensive cultural competence, and merely incorporating multilingual data does not necessarily enhance cultural understanding. All code and data files are available at https://github.com/HoganZinger/Culture

