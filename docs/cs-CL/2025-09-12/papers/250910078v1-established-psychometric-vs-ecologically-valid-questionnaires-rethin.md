---
layout: default
title: "Established Psychometric vs. Ecologically Valid Questionnaires: Rethinking Psychological Assessments in Large Language Models"
---

# Established Psychometric vs. Ecologically Valid Questionnaires: Rethinking Psychological Assessments in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10078" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10078v1</a>
  <a href="https://arxiv.org/pdf/2509.10078.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10078v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10078v1', 'Established Psychometric vs. Ecologically Valid Questionnaires: Rethinking Psychological Assessments in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongmin Choi, Woojung Song, Jongwook Han, Eun-Ju Lee, Yohan Jo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-12

**备注**: 17 pages, 4 figures

---

## 💡 一句话要点

**对比心理测量问卷与生态效度问卷，重新评估大语言模型中的心理评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `心理测量` `生态效度` `问卷评估` `人格特质`

## 📋 核心要点

1. 现有研究直接将人类心理测量问卷应用于LLM，忽略了LLM与人类在行为模式上的差异。
2. 本研究对比分析了传统心理测量问卷与更符合LLM实际应用场景的生态效度问卷。
3. 实验结果表明，传统问卷在评估LLM时存在偏差，可能导致对LLM能力和特性的误判。

## 📝 摘要（中文）

研究人员已应用既定的心理测量问卷（如BFI、PVQ）来测量大语言模型（LLM）响应中反映的性格特征和价值观。然而，将这些人为设计的问卷应用于LLM引起了一些担忧。其中一个担忧是它们的生态效度不足——即调查问题在多大程度上充分反映和类似于LLM响应用户查询生成文本的真实世界环境。然而，既定问卷和生态效度问卷在结果上有何不同，以及这些差异可能提供哪些见解，目前尚不清楚。在本文中，我们对这两种类型的问卷进行了全面的比较分析。我们的分析表明，既定问卷（1）产生与生态效度问卷截然不同的LLM概况，偏离了用户查询上下文中表达的心理特征，（2）缺乏足够的项目来进行稳定测量，（3）造成LLM具有稳定结构的误导性印象，以及（4）夸大了人物角色提示LLM的概况。总的来说，我们的工作警告不要对LLM使用既定的心理问卷。我们的代码将在发布后发布。

## 🔬 方法详解

**问题定义**：现有研究直接将为人类设计的心理测量问卷（如BFI、PVQ）应用于评估大语言模型（LLM）的性格和价值观。这种做法忽略了LLM与人类在行为模式和认知机制上的根本差异。传统问卷的生态效度不足，即问卷内容与LLM实际应用场景（例如，响应用户查询）的关联性较弱。这导致评估结果可能无法准确反映LLM的真实特性，并可能产生误导性结论。

**核心思路**：本研究的核心思路是通过对比分析传统心理测量问卷和生态效度问卷，揭示传统问卷在评估LLM时存在的偏差。生态效度问卷的设计更贴近LLM的实际应用场景，例如，模拟用户查询并分析LLM的响应。通过比较两种问卷的评估结果，可以更清晰地了解传统问卷的局限性，并为设计更适合LLM的评估方法提供指导。

**技术框架**：本研究的技术框架主要包括以下几个步骤：1) 选择或设计合适的传统心理测量问卷和生态效度问卷。2) 使用这些问卷对多个LLM进行评估，收集评估数据。3) 对比分析两种问卷的评估结果，例如，LLM在不同维度上的得分差异、问卷的信度和效度指标等。4) 分析导致评估结果差异的原因，例如，问卷内容与LLM应用场景的关联性、LLM的生成机制等。

**关键创新**：本研究的关键创新在于：1) 首次系统性地对比分析了传统心理测量问卷和生态效度问卷在评估LLM时的差异。2) 揭示了传统问卷在评估LLM时存在的偏差，例如，夸大LLM的性格特征、无法稳定测量LLM的价值观等。3) 强调了生态效度在LLM评估中的重要性，为设计更适合LLM的评估方法提供了理论依据。

**关键设计**：研究中关键的设计包括：1) 生态效度问卷的设计，需要根据LLM的实际应用场景进行定制，例如，模拟用户查询并分析LLM的响应。2) 问卷评估指标的选择，需要考虑LLM的特殊性，例如，使用信息熵来衡量LLM响应的多样性。3) 对比分析方法的选择，需要能够有效揭示两种问卷评估结果的差异，例如，使用统计检验来比较LLM在不同维度上的得分差异。

## 📊 实验亮点

研究表明，传统心理测量问卷对LLM的评估结果与生态效度问卷存在显著差异。传统问卷倾向于夸大LLM的性格特征，且无法稳定测量LLM的价值观。例如，在人格特质评估中，传统问卷可能将LLM评估为具有高度责任感，而生态效度问卷则显示其责任感水平较低。

## 🎯 应用场景

该研究成果可应用于大语言模型的安全性和可靠性评估，帮助开发者更准确地了解模型的行为模式和潜在风险。通过改进评估方法，可以更好地控制LLM的输出，避免生成有害或不准确的内容。此外，该研究也为开发更符合人类价值观的LLM提供了指导。

## 📄 摘要（原文）

> Researchers have applied established psychometric questionnaires (e.g., BFI, PVQ) to measure the personality traits and values reflected in the responses of Large Language Models (LLMs). However, concerns have been raised about applying these human-designed questionnaires to LLMs. One such concern is their lack of ecological validity--the extent to which survey questions adequately reflect and resemble real-world contexts in which LLMs generate texts in response to user queries. However, it remains unclear how established questionnaires and ecologically valid questionnaires differ in their outcomes, and what insights these differences may provide. In this paper, we conduct a comprehensive comparative analysis of the two types of questionnaires. Our analysis reveals that established questionnaires (1) yield substantially different profiles of LLMs from ecologically valid ones, deviating from the psychological characteristics expressed in the context of user queries, (2) suffer from insufficient items for stable measurement, (3) create misleading impressions that LLMs possess stable constructs, and (4) yield exaggerated profiles for persona-prompted LLMs. Overall, our work cautions against the use of established psychological questionnaires for LLMs. Our code will be released upon publication.

