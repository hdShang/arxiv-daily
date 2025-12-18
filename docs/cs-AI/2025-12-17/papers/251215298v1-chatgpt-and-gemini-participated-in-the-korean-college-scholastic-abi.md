---
layout: default
title: ChatGPT and Gemini participated in the Korean College Scholastic Ability Test -- Earth Science I
---

# ChatGPT and Gemini participated in the Korean College Scholastic Ability Test -- Earth Science I

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15298" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15298v1</a>
  <a href="https://arxiv.org/pdf/2512.15298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15298v1" onclick="toggleFavorite(this, '2512.15298v1', 'ChatGPT and Gemini participated in the Korean College Scholastic Ability Test -- Earth Science I')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seok-Hyun Ga, Chun-Yen Chang

**分类**: cs.AI, cs.CL, cs.CY

**发布日期**: 2025-12-17

**备注**: 23 pages, 9 tables, 1 figure

---

## 💡 一句话要点

**分析大型语言模型在韩国高考地球科学I科目的表现，揭示其认知局限性，为设计抗AI考题提供依据。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育评估` `科学推理` `多模态理解` `认知局限性`

## 📋 核心要点

1. 现有评估方法难以区分学生真实能力与AI生成答案，对学术诚信构成挑战。
2. 通过分析LLM在高考题中的表现，揭示其认知局限性，为设计抗AI考题提供思路。
3. 实验表明LLM存在感知错误、计算-概念化差异和过程幻觉等问题，为抗AI考题设计提供依据。

## 📝 摘要（中文）

生成式AI的快速发展正在给教育和评估带来创新性变革。随着学生使用AI完成作业的普及，对学术诚信和评估有效性的担忧日益增加。本研究利用2025年韩国高考（CSAT）地球科学I科目，深入分析了包括GPT-4o、Gemini 2.5 Flash和Gemini 2.5 Pro在内的最先进的大型语言模型（LLM）的多模态科学推理能力和认知局限性。设计了三种实验条件（整页输入、单项输入和优化的多模态输入），以评估模型在不同数据结构下的性能。定量结果表明，由于分割和光学字符识别（OCR）失败，非结构化输入导致了显著的性能下降。即使在优化条件下，模型也表现出基本的推理缺陷。定性分析表明，“感知错误”是主要的，突出了“感知-认知差距”，即模型未能解释示意图中的符号意义，尽管它们识别了视觉数据。此外，模型还表现出“计算-概念化差异”，成功地执行计算，但未能应用潜在的科学概念，以及“过程幻觉”，即模型跳过视觉验证，转而使用看似合理但没有根据的背景知识。为了应对在课程作业中未经授权使用AI的挑战，本研究为设计针对这些特定认知漏洞的“抗AI问题”提供了可操作的线索。通过利用AI的弱点，例如感知和认知之间的差距，教育工作者可以将真正的学生能力与AI生成的答案区分开来，从而确保评估的公平性。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型（LLM）在科学推理和多模态理解方面的局限性，特别是在教育评估场景下。现有方法难以区分学生真实能力与AI生成答案，对学术诚信构成威胁。LLM在处理复杂科学问题，尤其是涉及图表和概念理解的问题时，容易出现错误。

**核心思路**：核心思路是通过分析LLM在解决韩国高考地球科学I科目中的表现，揭示其在感知、认知和推理方面的弱点。通过设计不同输入方式的实验，探究LLM在处理非结构化数据和多模态信息时的性能瓶颈，从而为设计“抗AI问题”提供依据。

**技术框架**：研究采用实验方法，主要分为三个阶段：1) 数据准备：使用2025年韩国高考地球科学I科目试题，包括文字描述、图表等；2) 模型测试：使用GPT-4o、Gemini 2.5 Flash和Gemini 2.5 Pro等LLM，分别在整页输入、单项输入和优化的多模态输入三种条件下进行测试；3) 结果分析：对LLM的答案进行定量和定性分析，识别其在感知、认知和推理方面的错误类型。

**关键创新**：本研究的关键创新在于：1) 揭示了LLM在处理科学问题时存在的“感知-认知差距”、“计算-概念化差异”和“过程幻觉”等问题；2) 提出了设计“抗AI问题”的思路，即利用LLM的认知弱点，设计需要深度理解和推理的问题，从而区分学生真实能力与AI生成答案；3) 系统性地分析了不同输入方式对LLM性能的影响，为优化LLM在教育领域的应用提供了参考。

**关键设计**：实验设计了三种输入方式：1) 整页输入：直接输入包含试题的完整页面，考察LLM的OCR和分割能力；2) 单项输入：将试题拆分为单独的题目进行输入，减少OCR和分割带来的干扰；3) 优化的多模态输入：对图表进行预处理，提高LLM对图像信息的理解能力。研究人员对LLM的答案进行人工评估，并根据错误类型进行分类。

## 📊 实验亮点

实验结果表明，非结构化输入（整页输入）导致LLM性能显著下降，主要原因是OCR和分割失败。即使在优化条件下，LLM仍然存在推理缺陷，例如“感知错误”和“计算-概念化差异”。研究发现，LLM在计算方面表现良好，但在概念理解和应用方面存在不足。这些发现为设计“抗AI问题”提供了重要依据。

## 🎯 应用场景

该研究成果可应用于教育评估领域，帮助教师设计更具挑战性和区分度的考题，有效防止学生利用AI作弊，维护学术诚信。同时，研究结果也能为LLM在教育领域的应用提供指导，促进AI辅助教学工具的开发，提升教学质量。

## 📄 摘要（原文）

> The rapid development of Generative AI is bringing innovative changes to education and assessment. As the prevalence of students utilizing AI for assignments increases, concerns regarding academic integrity and the validity of assessments are growing. This study utilizes the Earth Science I section of the 2025 Korean College Scholastic Ability Test (CSAT) to deeply analyze the multimodal scientific reasoning capabilities and cognitive limitations of state-of-the-art Large Language Models (LLMs), including GPT-4o, Gemini 2.5 Flash, and Gemini 2.5 Pro. Three experimental conditions (full-page input, individual item input, and optimized multimodal input) were designed to evaluate model performance across different data structures. Quantitative results indicated that unstructured inputs led to significant performance degradation due to segmentation and Optical Character Recognition (OCR) failures. Even under optimized conditions, models exhibited fundamental reasoning flaws. Qualitative analysis revealed that "Perception Errors" were dominant, highlighting a "Perception-Cognition Gap" where models failed to interpret symbolic meanings in schematic diagrams despite recognizing visual data. Furthermore, models demonstrated a "Calculation-Conceptualization Discrepancy," successfully performing calculations while failing to apply the underlying scientific concepts, and "Process Hallucination," where models skipped visual verification in favor of plausible but unfounded background knowledge. Addressing the challenge of unauthorized AI use in coursework, this study provides actionable cues for designing "AI-resistant questions" that target these specific cognitive vulnerabilities. By exploiting AI's weaknesses, such as the gap between perception and cognition, educators can distinguish genuine student competency from AI-generated responses, thereby ensuring assessment fairness.

