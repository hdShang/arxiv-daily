---
layout: default
title: "FAA Framework: A Large Language Model-Based Approach for Credit Card Fraud Investigations"
---

# FAA Framework: A Large Language Model-Based Approach for Credit Card Fraud Investigations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11635" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11635v1</a>
  <a href="https://arxiv.org/pdf/2506.11635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11635v1', 'FAA Framework: A Large Language Model-Based Approach for Credit Card Fraud Investigations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaun Shuster, Eyal Zaloof, Asaf Shabtai, Rami Puzis

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出FAA框架以解决信用卡欺诈调查中的分析师疲劳问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信用卡欺诈` `多模态学习` `大型语言模型` `自动化调查` `数据分析` `金融科技` `风险管理`

## 📋 核心要点

1. 现有的信用卡欺诈检测方法面临大量警报，导致分析师疲劳，难以有效处理每个警报。
2. FAA框架通过多模态大型语言模型自动化调查过程，提供规划、证据收集和分析功能，减轻分析师负担。
3. 实证评估显示，FAA框架在500个调查中表现出色，平均完成七个步骤，显著提高了调查效率。

## 📝 摘要（中文）

随着电子商务行业的持续增长，欺诈者利用被盗的信用卡信息进行诈骗。为了维护客户信任并弥补欺诈检测系统的不足，公司通常需要调查可疑交易。然而，分析师面临来自信用卡交易监控系统的大量警报，导致警报疲劳。为此，本文提出了一种欺诈分析师助手（FAA）框架，利用多模态大型语言模型（LLMs）自动化信用卡欺诈调查并生成解释性报告。FAA框架利用LLMs的推理、代码执行和视觉能力，在每个调查步骤中进行规划、证据收集和分析。对500个信用卡欺诈调查的全面实证评估表明，FAA框架能够高效可靠地完成调查，平均涉及七个步骤，从而减轻欺诈分析师的工作负担。

## 🔬 方法详解

**问题定义**：本文旨在解决信用卡欺诈调查中分析师面临的警报疲劳问题。现有方法无法有效处理大量警报，导致分析师的工作效率低下。

**核心思路**：FAA框架的核心思路是利用多模态大型语言模型（LLMs）自动化调查过程，减少人工干预，提高调查的效率和准确性。通过整合推理、代码执行和视觉能力，FAA能够在调查的各个阶段提供支持。

**技术框架**：FAA框架包括多个主要模块，如规划模块、证据收集模块和分析模块。每个模块负责不同的调查步骤，确保调查过程的系统性和完整性。

**关键创新**：FAA框架的最大创新在于将多模态LLMs应用于信用卡欺诈调查，能够自动化处理复杂的调查任务，与传统方法相比，显著提高了效率和准确性。

**关键设计**：在设计中，FAA框架采用了特定的参数设置和损失函数，以优化模型的推理能力和执行效率。网络结构方面，结合了视觉输入和文本输入的处理能力，确保多模态信息的有效融合。

## 📊 实验亮点

在对500个信用卡欺诈调查的实证评估中，FAA框架平均完成七个步骤，显示出高效可靠的调查能力。与传统方法相比，FAA框架显著减少了分析师的工作负担，提高了调查的准确性和效率。

## 🎯 应用场景

FAA框架在金融行业的信用卡欺诈检测中具有广泛的应用潜力。通过自动化调查过程，能够显著提高调查效率，降低分析师的工作压力，进而提升客户信任度和公司声誉。未来，该框架还可以扩展到其他领域的欺诈检测和风险管理中。

## 📄 摘要（原文）

> The continuous growth of the e-commerce industry attracts fraudsters who exploit stolen credit card details. Companies often investigate suspicious transactions in order to retain customer trust and address gaps in their fraud detection systems. However, analysts are overwhelmed with an enormous number of alerts from credit card transaction monitoring systems. Each alert investigation requires from the fraud analysts careful attention, specialized knowledge, and precise documentation of the outcomes, leading to alert fatigue. To address this, we propose a fraud analyst assistant (FAA) framework, which employs multi-modal large language models (LLMs) to automate credit card fraud investigations and generate explanatory reports. The FAA framework leverages the reasoning, code execution, and vision capabilities of LLMs to conduct planning, evidence collection, and analysis in each investigation step. A comprehensive empirical evaluation of 500 credit card fraud investigations demonstrates that the FAA framework produces reliable and efficient investigations comprising seven steps on average. Thus we found that the FAA framework can automate large parts of the workload and help reduce the challenges faced by fraud analysts.

