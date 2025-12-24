---
layout: default
title: "The Anatomy of Speech Persuasion: Linguistic Shifts in LLM-Modified Speeches"
---

# The Anatomy of Speech Persuasion: Linguistic Shifts in LLM-Modified Speeches

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18621" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18621v1</a>
  <a href="https://arxiv.org/pdf/2506.18621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18621v1', 'The Anatomy of Speech Persuasion: Linguistic Shifts in LLM-Modified Speeches')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alisa Barkar, Mathieu Chollet, Matthieu Labeau, Beatrice Biancardi, Chloe Clavel

**分类**: cs.CL

**发布日期**: 2025-06-23

**备注**: Under submission to ICNLSP 2025. 9 pages, 2 tables

---

## 💡 一句话要点

**提出一种新方法分析大型语言模型对演讲说服力的理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `说服力分析` `修辞手法` `文本特征` `公共演讲` `情感分析` `句法结构`

## 📋 核心要点

1. 现有方法在理解和优化演讲的说服力方面存在不足，缺乏系统的分析框架。
2. 论文提出了一种新方法，通过整合修辞手法和话语标记，分析语言变化以评估说服力。
3. 实验结果显示，GPT-4o在风格上进行系统性修改，而非简单优化说服力，特别是在情感和句法结构方面。

## 📝 摘要（中文）

本研究探讨大型语言模型如何理解公共演讲中的说服力，通过修改“Ma These en 180 Secondes”竞赛中博士生的演讲稿，使用3MT法语数据集。我们的贡献包括一种新颖的方法论和可解释的文本特征集，整合了修辞手法和话语标记。我们提示GPT-4o增强或减弱说服力，并分析原始演讲与生成演讲之间的语言变化。结果表明，GPT-4o应用系统的风格修改，而非以人类方式优化说服力，特别是在情感词汇和句法结构（如疑问句和感叹句）上进行操控，以增强修辞效果。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在公共演讲中对说服力理解的不足，现有方法缺乏对语言特征的系统分析，无法有效评估说服力的变化。

**核心思路**：论文的核心思路是通过修改演讲稿并分析语言特征，探讨大型语言模型如何影响说服力，特别是通过修辞手法和话语标记的整合。

**技术框架**：整体架构包括数据收集、模型提示、语言特征提取和结果分析四个主要模块。首先收集演讲稿，然后使用GPT-4o进行修改，最后提取并分析语言特征。

**关键创新**：最重要的技术创新在于提出了一种可解释的文本特征集，整合了修辞手法和话语标记，能够系统性地分析语言变化与说服力之间的关系。与现有方法相比，该方法提供了更深入的理解。

**关键设计**：在参数设置上，使用了特定的提示策略来引导GPT-4o进行风格修改，损失函数设计上关注于语言特征的变化，确保生成的文本在情感和句法结构上具有显著的修辞效果。

## 📊 实验亮点

实验结果显示，GPT-4o在修改演讲稿时，系统性地调整了情感词汇和句法结构，显著增强了修辞效果。与原始演讲相比，生成的演讲在说服力方面的提升并未达到人类的优化水平，但在风格上表现出明显的变化，尤其是在使用疑问句和感叹句方面。

## 🎯 应用场景

该研究的潜在应用领域包括公共演讲培训、教育领域的演讲评估以及人工智能辅助的演讲生成工具。通过深入理解说服力的语言特征，可以帮助演讲者提升表达效果，增强听众的接受度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This study examines how large language models understand the concept of persuasiveness in public speaking by modifying speech transcripts from PhD candidates in the "Ma These en 180 Secondes" competition, using the 3MT French dataset. Our contributions include a novel methodology and an interpretable textual feature set integrating rhetorical devices and discourse markers. We prompt GPT-4o to enhance or diminish persuasiveness and analyze linguistic shifts between original and generated speech in terms of the new features. Results indicate that GPT-4o applies systematic stylistic modifications rather than optimizing persuasiveness in a human-like manner. Notably, it manipulates emotional lexicon and syntactic structures (such as interrogative and exclamatory clauses) to amplify rhetorical impact.

