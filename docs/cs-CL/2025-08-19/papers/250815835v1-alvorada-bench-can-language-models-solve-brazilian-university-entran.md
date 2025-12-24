---
layout: default
title: "Alvorada-Bench: Can Language Models Solve Brazilian University Entrance Exams?"
---

# Alvorada-Bench: Can Language Models Solve Brazilian University Entrance Exams?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15835" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15835v1</a>
  <a href="https://arxiv.org/pdf/2508.15835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15835v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15835v1', 'Alvorada-Bench: Can Language Models Solve Brazilian University Entrance Exams?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Henrique Godoy

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出Alvorada-Bench以评估语言模型在巴西大学入学考试中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `教育评估` `巴西大学入学考试` `多步推理` `基准测试`

## 📋 核心要点

1. 现有的语言模型评估主要集中在英语，缺乏针对巴西教育体系的专门基准，导致模型在本地考试中的表现未知。
2. 论文提出Alvorada-Bench基准，包含来自五个巴西大学入学考试的4,515道题目，评估模型在不同提示策略下的表现。
3. 实验结果显示，顶尖模型在语言科目上取得完美分数，但在数学方面仍表现不佳，揭示了多步推理的不足。

## 📝 摘要（中文）

语言模型在巴西的应用日益增加，但大多数评估仍以英语为中心。本文提出了Alvorada-Bench，这是一个由五个巴西大学入学考试提取的4,515道题目的文本基准。在零-shot、角色扮演和链式思维提示下评估了二十个模型，生成了270,900个响应，并进行了结构化的自我报告，包括信心、感知难度和布鲁姆等级。尽管顶尖模型整体准确率超过94%，但在数学和工程导向的IME和ITA考试中准确率下降，显示出多步推理的持续弱点。信心与感知难度良好校准，表明模型能够准确评估自身的确定性能力。

## 🔬 方法详解

**问题定义**：本文旨在评估语言模型在巴西大学入学考试中的表现，现有方法主要集中于英语，缺乏对巴西本土教育内容的评估，导致模型在实际应用中的有效性未知。

**核心思路**：通过构建Alvorada-Bench基准，论文提供了一个专门针对巴西大学入学考试的评估工具，采用多种提示策略来测试模型的推理能力和文化适应性。

**技术框架**：整体架构包括题库构建、模型选择、提示策略设计和结果分析四个主要模块。题库由五个不同的巴西大学入学考试题目组成，模型在零-shot、角色扮演和链式思维提示下进行评估。

**关键创新**：Alvorada-Bench的构建是本研究的核心创新，填补了现有语言模型评估中缺乏针对巴西教育体系的空白，提供了一个多维度的评估框架。

**关键设计**：在实验中，模型的信心、感知难度和布鲁姆等级被系统记录，采用结构化自我报告的方式，确保评估结果的可靠性和可解释性。

## 📊 实验亮点

实验结果显示，顶尖模型在语言科目上取得了完美分数，整体准确率超过94%。然而，在数学和工程导向的考试中，准确率有所下降，揭示了多步推理的不足，尤其是在IME和ITA考试中表现不佳。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和语言模型的本地化开发。通过评估模型在巴西教育体系中的表现，能够为教育决策提供数据支持，推动教育公平和质量提升。

## 📄 摘要（原文）

> Language models are increasingly used in Brazil, but most evaluation remains English-centric. This paper presents Alvorada-Bench, a 4,515-question, text-only benchmark drawn from five Brazilian university entrance examinations. Evaluating twenty models under zero-shot, role-playing, and chain-of-thought prompting, producing 270,900 responses with structured self-reports of confidence, perceived difficulty, and Bloom level. The top models exceed 94% accuracy overall, but accuracy declines on Mathematics and on the engineering oriented IME and ITA exams, indicating persistent weaknesses in multi-step reasoning. Confidence is well calibrated and correlates with perceived difficulty, revealing that models can accurately assess their own certainty capabilities. A cost accuracy analysis shows that high accuracy is achievable at under $2 per 1K tokens. On ENEM 2024 the top model (O3) achieved perfect scores in Languages subject questions while even the weakest system (GPT-4.1 Nano) only underperforms humans in Mathematics. Through exams that distill decades of Brazilian educational priorities and assess millions of students yearly, Alvorada-Bench establishes whether language models can navigate the intersection of language, culture, and reasoning that defines academic readiness in Brazil.

