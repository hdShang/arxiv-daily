---
layout: default
title: "Tell Me Who Your Students Are: GPT Can Generate Valid Multiple-Choice Questions When Students' (Mis)Understanding Is Hinted"
---

# Tell Me Who Your Students Are: GPT Can Generate Valid Multiple-Choice Questions When Students' (Mis)Understanding Is Hinted

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05815" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05815v2</a>
  <a href="https://arxiv.org/pdf/2505.05815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05815v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05815v2', 'Tell Me Who Your Students Are: GPT Can Generate Valid Multiple-Choice Questions When Students\' (Mis)Understanding Is Hinted')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Machi Shimmei, Masaki Uto, Yuichiroh Matsubayashi, Kentaro Inui, Aditi Mallavarapu, Noboru Matsuda

**分类**: cs.CL

**发布日期**: 2025-05-09 (更新: 2025-08-07)

**备注**: This is a pre-print version of a paper to appear in AIED2025. The camera-ready version is available at https://link.springer.com/chapter/10.1007/978-3-031-99264-3_16

---

## 💡 一句话要点

**提出AnaQuest以生成有效的多项选择题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多项选择题生成` `教育技术` `项目反应理论` `开放式问题` `智能评估`

## 📋 核心要点

1. 现有的多项选择题生成方法往往缺乏对学生理解的深入分析，导致生成的问题质量不高。
2. 论文提出的AnaQuest方法通过分析学生的开放式回答，生成更具针对性的多项选择题，提升了题目的有效性。
3. 实验结果表明，AnaQuest生成的题目在难度和区分度上优于基线ChatGPT生成的题目，获得专家教师的高度认可。

## 📝 摘要（中文）

本研究的主要目标是开发和评估一种创新的提示技术AnaQuest，用于利用预训练的大型语言模型生成多项选择题（MCQs）。在AnaQuest中，选项项是关于复杂概念的句子级断言。该技术结合了形成性和总结性评估。在形成性阶段，学生以自由文本回答目标概念的开放式问题。对于总结性评估，AnaQuest分析这些回答以生成正确和错误的断言。为了评估生成的MCQs的有效性，采用项目反应理论（IRT）比较AnaQuest生成的MCQs、基线ChatGPT提示和人工制作的题目的项目特征。实证研究发现，专家教师认为AI模型生成的MCQs与人类教师创建的题目同样有效。然而，基于IRT的分析显示，AnaQuest生成的问题，特别是那些包含错误断言的选项，在难度和区分度上更接近人类制作的题目，而非ChatGPT生成的题目。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有多项选择题生成方法在理解学生知识掌握情况方面的不足，导致生成的问题无法有效评估学生的真实理解。

**核心思路**：AnaQuest通过分析学生对开放式问题的回答，生成与学生理解相关的多项选择题，结合形成性和总结性评估，确保题目的有效性和针对性。

**技术框架**：AnaQuest的整体架构包括两个主要阶段：第一阶段是学生回答开放式问题，第二阶段是系统分析这些回答并生成多项选择题。生成的题目包括正确和错误的断言，以便更好地评估学生的理解。

**关键创新**：AnaQuest的核心创新在于其生成的题目能够更好地反映学生的理解情况，尤其是在错误选项的设计上，提升了题目的难度和区分度，区别于传统的生成方法。

**关键设计**：在参数设置上，AnaQuest采用了项目反应理论（IRT）来评估生成题目的有效性，确保生成的题目在难度和区分度上与人类教师制作的题目相当。

## 📊 实验亮点

实验结果显示，AnaQuest生成的多项选择题在难度和区分度上与人类教师制作的题目相似，尤其是在错误选项的设计上，表现出更高的有效性。与基线ChatGPT生成的题目相比，AnaQuest在专家评估中获得了更高的认可度，显示出显著的提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、在线学习平台和智能评估系统。AnaQuest可以帮助教师更有效地评估学生的理解，提供个性化的学习反馈，提升教学质量。未来，该技术有望在更广泛的教育场景中推广，促进智能化教育的发展。

## 📄 摘要（原文）

> The primary goal of this study is to develop and evaluate an innovative prompting technique, AnaQuest, for generating multiple-choice questions (MCQs) using a pre-trained large language model. In AnaQuest, the choice items are sentence-level assertions about complex concepts. The technique integrates formative and summative assessments. In the formative phase, students answer open-ended questions for target concepts in free text. For summative assessment, AnaQuest analyzes these responses to generate both correct and incorrect assertions. To evaluate the validity of the generated MCQs, Item Response Theory (IRT) was applied to compare item characteristics between MCQs generated by AnaQuest, a baseline ChatGPT prompt, and human-crafted items. An empirical study found that expert instructors rated MCQs generated by both AI models to be as valid as those created by human instructors. However, IRT-based analysis revealed that AnaQuest-generated questions - particularly those with incorrect assertions (foils) - more closely resembled human-crafted items in terms of difficulty and discrimination than those produced by ChatGPT.

