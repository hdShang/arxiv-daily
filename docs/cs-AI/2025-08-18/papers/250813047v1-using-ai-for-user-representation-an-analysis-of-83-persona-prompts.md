---
layout: default
title: "Using AI for User Representation: An Analysis of 83 Persona Prompts"
---

# Using AI for User Representation: An Analysis of 83 Persona Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13047" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13047v1</a>
  <a href="https://arxiv.org/pdf/2508.13047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13047v1', 'Using AI for User Representation: An Analysis of 83 Persona Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joni Salminen, Danial Amin, Bernard Jansen

**分类**: cs.HC, cs.AI

**发布日期**: 2025-08-18

**备注**: Accepted at AICCSA-2025

---

## 💡 一句话要点

**分析83个用户角色提示以优化AI用户表示**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户角色生成` `大型语言模型` `结构化输出` `人口统计属性` `AI用户表示`

## 📋 核心要点

1. 现有方法主要生成单一用户角色，且角色描述往往过于简短，缺乏深度和信息量。
2. 论文通过分析现有的83个提示，揭示了生成用户角色的常见模式和偏好，提出了对生成内容的结构化要求。
3. 研究表明，超过一半的提示要求输出为结构化格式，且大多数生成的角色包含人口统计信息，显示出对角色生成的系统性需求。

## 📝 摘要（中文）

本研究分析了27篇研究文章中的83个用户角色提示，这些文章利用大型语言模型（LLMs）生成用户角色。研究发现，提示主要生成单一角色，且许多提示倾向于简短的角色描述，这与传统的丰富、全面的角色档案相悖。生成的角色属性中，文本格式最为常见，其次是数字，且大多数生成的角色都包含人口统计属性。研究者在单个研究中使用多达12个提示，但大多数研究仅使用少量提示。对多个LLM的比较和测试较为罕见。超过一半的提示要求角色输出为结构化格式，如JSON，且74%的提示插入数据或动态变量。我们讨论了计算角色在用户表示中使用增加的影响。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前用户角色生成中存在的单一角色生成和描述简短的问题，现有方法往往无法提供丰富的用户画像。

**核心思路**：通过分析83个用户角色提示，论文揭示了生成用户角色的常见模式，强调了对结构化输出的需求，以便更好地满足研究者的使用场景。

**技术框架**：研究通过对27篇文献的提示进行分类和分析，构建了一个包含角色生成属性、格式要求和使用频率的框架，帮助理解用户角色生成的现状。

**关键创新**：论文的创新在于系统性分析了用户角色生成的提示，揭示了生成内容的结构化需求和多样性，填补了现有研究的空白。

**关键设计**：研究中强调了生成角色时的文本和数字格式的结合，且对人口统计属性的包含进行了详细探讨，提出了在提示设计中应考虑的关键因素。

## 📊 实验亮点

研究结果显示，超过一半的提示要求生成结构化的角色输出，且74%的提示中包含动态变量。这表明在用户角色生成中，系统性和灵活性是关键需求，推动了对多样化生成策略的探索。

## 🎯 应用场景

该研究的潜在应用领域包括用户体验设计、市场调研和个性化推荐系统。通过优化用户角色生成，研究者可以更准确地理解目标用户群体，从而提升产品设计和服务质量，未来可能对AI驱动的用户研究产生深远影响。

## 📄 摘要（原文）

> We analyzed 83 persona prompts from 27 research articles that used large language models (LLMs) to generate user personas. Findings show that the prompts predominantly generate single personas. Several prompts express a desire for short or concise persona descriptions, which deviates from the tradition of creating rich, informative, and rounded persona profiles. Text is the most common format for generated persona attributes, followed by numbers. Text and numbers are often generated together, and demographic attributes are included in nearly all generated personas. Researchers use up to 12 prompts in a single study, though most research uses a small number of prompts. Comparison and testing multiple LLMs is rare. More than half of the prompts require the persona output in a structured format, such as JSON, and 74% of the prompts insert data or dynamic variables. We discuss the implications of increased use of computational personas for user representation.

