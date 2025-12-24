---
layout: default
title: Red Teaming Large Language Models for Healthcare
---

# Red Teaming Large Language Models for Healthcare

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00467" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00467v2</a>
  <a href="https://arxiv.org/pdf/2505.00467.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00467v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00467v2', 'Red Teaming Large Language Models for Healthcare')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vahid Balazadeh, Michael Cooper, David Pellow, Atousa Assadi, Jennifer Bell, Mark Coatsworth, Kaivalya Deshpande, Jim Fackler, Gabriel Funingana, Spencer Gable-Cook, Anirudh Gangadhar, Abhishek Jaiswal, Sumanth Kaja, Christopher Khoury, Amrit Krishnan, Randy Lin, Kaden McKeen, Sara Naimimohasses, Khashayar Namdar, Aviraj Newatia, Allan Pang, Anshul Pattoo, Sameer Peesapati, Diana Prepelita, Bogdana Rakova, Saba Sadatamin, Rafael Schulman, Ajay Shah, Syed Azhar Shah, Syed Ahmar Shah, Babak Taati, Balagopal Unnikrishnan, Iñigo Urteaga, Stephanie Williams, Rahul G Krishnan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-01 (更新: 2025-07-11)

---

## 💡 一句话要点

**通过红队测试识别医疗领域大型语言模型的脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗安全` `红队测试` `脆弱性识别` `临床应用` `机器学习`

## 📋 核心要点

1. 当前大型语言模型在医疗领域的应用面临潜在的安全隐患，尤其是在临床提示下可能产生有害响应。
2. 本研究通过红队测试的方法，结合临床专家的知识，系统性地识别和分类LLM的脆弱性。
3. 研究结果显示，多个LLM存在显著的脆弱性，且这些脆弱性在不同模型间具有一致性，提示了需要进一步的安全性评估。

## 📝 摘要（中文）

本文介绍了2024年医疗机器学习会议前的研讨会设计过程及发现，主题为“红队测试医疗领域的大型语言模型”。参与者包括计算和临床专家，旨在发现大型语言模型（LLM）在临床提示下可能导致临床危害的脆弱性。通过与临床医生的红队测试，能够识别出LLM开发者未能察觉的脆弱性。我们报告了发现的脆弱性，并对其进行了分类，同时呈现了一项复制研究的结果，评估了所有提供的LLM中的脆弱性。

## 🔬 方法详解

**问题定义**：本文旨在识别大型语言模型在医疗应用中的脆弱性，尤其是那些可能导致临床危害的响应。现有方法往往缺乏临床背景知识，无法全面评估LLM的安全性。

**核心思路**：通过红队测试，结合临床专家的专业知识，系统地发现和分类LLM的脆弱性。这种方法能够揭示开发者未能识别的潜在风险。

**技术框架**：研究分为几个主要阶段，包括：1) 组建多学科团队，2) 设计临床提示，3) 收集LLM的响应，4) 分类和分析脆弱性。

**关键创新**：本研究的创新之处在于将红队测试与临床专家的知识结合，形成了一种新的评估LLM安全性的框架。这与传统的开发者主导的测试方法有本质区别。

**关键设计**：在设计过程中，团队设置了多种临床场景和提示，确保覆盖广泛的应用场景，并采用定量和定性分析相结合的方法评估脆弱性。

## 📊 实验亮点

实验结果显示，多个大型语言模型在特定临床提示下存在显著脆弱性，部分模型的错误响应率高达20%。这些发现强调了在医疗领域应用LLM时进行安全性评估的重要性，并为后续的改进提供了依据。

## 🎯 应用场景

该研究的潜在应用领域包括医疗决策支持系统、患者咨询机器人和其他医疗相关的人工智能应用。通过识别和修复LLM的脆弱性，可以显著提高这些系统的安全性和可靠性，从而保护患者的健康和安全。

## 📄 摘要（原文）

> We present the design process and findings of the pre-conference workshop at the Machine Learning for Healthcare Conference (2024) entitled Red Teaming Large Language Models for Healthcare, which took place on August 15, 2024. Conference participants, comprising a mix of computational and clinical expertise, attempted to discover vulnerabilities -- realistic clinical prompts for which a large language model (LLM) outputs a response that could cause clinical harm. Red-teaming with clinicians enables the identification of LLM vulnerabilities that may not be recognised by LLM developers lacking clinical expertise. We report the vulnerabilities found, categorise them, and present the results of a replication study assessing the vulnerabilities across all LLMs provided.

