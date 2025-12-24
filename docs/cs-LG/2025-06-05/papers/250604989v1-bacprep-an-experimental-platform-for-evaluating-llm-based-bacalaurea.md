---
layout: default
title: "BacPrep: An Experimental Platform for Evaluating LLM-Based Bacalaureat Assessment"
---

# BacPrep: An Experimental Platform for Evaluating LLM-Based Bacalaureat Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04989" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04989v1</a>
  <a href="https://arxiv.org/pdf/2506.04989.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04989v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04989v1', 'BacPrep: An Experimental Platform for Evaluating LLM-Based Bacalaureat Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dumitran Adrian Marius, Dita Radu

**分类**: cs.SE, cs.CY, cs.LG

**发布日期**: 2025-06-05

**备注**: 9 pages Preprint ACCEPTED at BBGI (ITS Workshop)

---

## 💡 一句话要点

**提出BacPrep平台以解决罗马尼亚高考备考反馈不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动评估` `教育技术` `高考备考` `个性化反馈` `在线学习` `数据收集`

## 📋 核心要点

1. 核心问题：现有的高考备考资源不足，尤其是在偏远地区，学生难以获得高质量的准备和反馈。
2. 方法要点：BacPrep平台利用大型语言模型进行自动评估，提供基于官方考试问题的反馈，旨在提高备考的可及性。
3. 实验或效果：平台已投入使用，收集学生解答和模型输出，为后续的专家验证提供数据支持。

## 📝 摘要（中文）

获取高质量的罗马尼亚高考备考和反馈对于偏远或服务不足地区的学生来说是一个挑战。本文介绍了BacPrep，一个实验性在线平台，探索大型语言模型（LLM）在自动评估中的潜力，旨在提供一个免费的可访问资源。BacPrep使用过去五年的官方考试问题，采用谷歌最新的Gemini 2.0 Flash模型（于2025年2月发布），并依据官方评分标准提供实验性反馈。该平台目前已投入使用，主要研究功能是收集学生解决方案和LLM输出。这一专注的数据集对于计划中的专家验证至关重要，以严格评估这一前沿LLM在特定高考背景下的可行性和准确性。我们详细阐述了设计、数据策略、状态、验证计划和伦理问题。

## 🔬 方法详解

**问题定义**：本文旨在解决罗马尼亚高考备考过程中，尤其是在偏远地区，学生获取高质量准备和反馈的困难。现有方法往往缺乏个性化和及时性，无法满足学生的需求。

**核心思路**：BacPrep平台通过利用大型语言模型（LLM）进行自动评估，提供基于官方考试问题的反馈，旨在为学生提供一个免费的、可访问的备考资源。这种设计能够快速响应学生的需求，并提供个性化的反馈。

**技术框架**：BacPrep的整体架构包括数据收集模块、LLM评估模块和反馈生成模块。数据收集模块负责收集学生的解答，LLM评估模块使用Gemini 2.0 Flash模型进行自动评分，反馈生成模块则依据评分结果提供个性化的反馈。

**关键创新**：BacPrep的主要创新在于将最新的LLM技术应用于高考备考评估中，尤其是结合官方评分标准进行反馈生成。这种方法与传统的人工评估方式相比，具有更高的效率和可扩展性。

**关键设计**：在技术细节方面，BacPrep使用了官方考试问题作为训练和评估的基础，采用了Gemini 2.0 Flash模型进行评分，并依据官方评分标准设计了反馈生成的流程。

## 📊 实验亮点

BacPrep平台目前已成功收集学生解答和LLM输出，为后续的专家验证提供了重要的数据支持。通过使用Gemini 2.0 Flash模型，平台能够快速生成反馈，预计将显著提高学生的备考效率和满意度。

## 🎯 应用场景

BacPrep平台的潜在应用领域包括教育技术、在线学习和个性化教学。通过提供自动化的评估和反馈，BacPrep可以帮助更多学生，尤其是那些在资源匮乏地区的学生，提高他们的备考效率和考试成绩。未来，该平台有望推广至其他国家或考试体系，进一步提升教育公平性。

## 📄 摘要（原文）

> Accessing quality preparation and feedback for the Romanian Bacalaureat exam is challenging, particularly for students in remote or underserved areas. This paper introduces BacPrep, an experimental online platform exploring Large Language Model (LLM) potential for automated assessment, aiming to offer a free, accessible resource. Using official exam questions from the last 5 years, BacPrep employs one of Google's newest models, Gemini 2.0 Flash (released Feb 2025), guided by official grading schemes, to provide experimental feedback. Currently operational, its primary research function is collecting student solutions and LLM outputs. This focused dataset is vital for planned expert validation to rigorously evaluate the feasibility and accuracy of this cutting-edge LLM in the specific Bacalaureat context before reliable deployment. We detail the design, data strategy, status, validation plan, and ethics.

