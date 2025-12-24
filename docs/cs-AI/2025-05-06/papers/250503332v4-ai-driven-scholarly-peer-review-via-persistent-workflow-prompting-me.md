---
layout: default
title: AI-Driven Scholarly Peer Review via Persistent Workflow Prompting, Meta-Prompting, and Meta-Reasoning
---

# AI-Driven Scholarly Peer Review via Persistent Workflow Prompting, Meta-Prompting, and Meta-Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03332" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03332v4</a>
  <a href="https://arxiv.org/pdf/2505.03332.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03332v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03332v4', 'AI-Driven Scholarly Peer Review via Persistent Workflow Prompting, Meta-Prompting, and Meta-Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Evgeny Markhasin

**分类**: cs.AI, physics.chem-ph

**发布日期**: 2025-05-06 (更新: 2025-07-08)

**备注**: 23 pages, 37 pages (references and appendixes)

---

## 💡 一句话要点

**提出持久工作流提示以解决科学论文同行评审问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `同行评审` `大型语言模型` `持久工作流提示` `元提示技术` `元推理` `科学论文分析` `多模态评估`

## 📋 核心要点

1. 现有的同行评审方法在处理科学论文时面临数据限制和专家推理复杂性等挑战。
2. 论文提出的持久工作流提示（PWP）方法，通过标准LLM聊天界面实现批判性分析，简化了提示工程过程。
3. 实验结果表明，PWP引导的LLM能够有效识别方法论缺陷，并执行多种复杂分析任务，提升了评审质量。

## 📝 摘要（中文）

科学论文的同行评审对大型语言模型（LLMs）提出了重大挑战，部分原因在于数据限制和专家推理的复杂性。本文介绍了一种名为持久工作流提示（PWP）的提示工程方法，旨在利用标准LLM聊天界面弥补这一差距。我们展示了一个用于实验化学论文批判性分析的PWP提示的概念验证，采用层次化、模块化的架构，通过Markdown结构化定义详细的分析工作流程。通过迭代应用元提示技术和元推理，我们系统化了专家评审工作流程，包括隐性知识。该PWP提示在会话开始时提交，随后触发的查询引导LLM进行系统的多模态评估。演示显示，PWP引导的LLM能够识别测试案例中的主要方法论缺陷，同时减轻LLM输入偏差，执行复杂任务。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在科学论文同行评审中的应用挑战，尤其是数据限制和专家推理的复杂性。现有方法往往无法有效捕捉和应用专家的隐性知识。

**核心思路**：提出持久工作流提示（PWP）作为一种新的提示工程方法，通过标准LLM聊天界面实现批判性分析，系统化专家评审工作流程。该方法通过一次性提交提示，后续查询可触发持久工作流，增强LLM的推理能力。

**技术框架**：PWP的整体架构采用层次化、模块化设计，使用Markdown结构化定义分析工作流程。主要模块包括提示生成、元提示技术应用和元推理过程，确保LLM能够进行系统的多模态评估。

**关键创新**：PWP的最大创新在于其持久性工作流的设计，使得LLM能够在会话中持续利用专家知识，显著提高了评审的系统性和准确性。这与传统方法的单次提示输入形成鲜明对比。

**关键设计**：在PWP中，关键设计包括提示的层次化结构、模块化分析流程以及元提示和元推理的迭代应用，确保了隐性知识的有效编码和利用。

## 📊 实验亮点

实验结果显示，PWP引导的LLM在测试案例中成功识别出主要方法论缺陷，并在多项复杂任务中表现优异，包括区分主张与证据、执行定量可行性检查等，显著提高了评审的准确性和系统性。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、学术出版和教育等。通过提升大型语言模型在同行评审中的表现，PWP方法能够帮助研究人员更高效地进行论文评审，促进科学交流与合作，未来可能影响学术界的评审标准和流程。

## 📄 摘要（原文）

> Critical peer review of scientific manuscripts presents a significant challenge for Large Language Models (LLMs), partly due to data limitations and the complexity of expert reasoning. This report introduces Persistent Workflow Prompting (PWP), a potentially broadly applicable prompt engineering methodology designed to bridge this gap using standard LLM chat interfaces (zero-code, no APIs). We present a proof-of-concept PWP prompt for the critical analysis of experimental chemistry manuscripts, featuring a hierarchical, modular architecture (structured via Markdown) that defines detailed analysis workflows. We develop this PWP prompt through iterative application of meta-prompting techniques and meta-reasoning aimed at systematically codifying expert review workflows, including tacit knowledge. Submitted once at the start of a session, this PWP prompt equips the LLM with persistent workflows triggered by subsequent queries, guiding modern reasoning LLMs through systematic, multimodal evaluations. Demonstrations show the PWP-guided LLM identifying major methodological flaws in a test case while mitigating LLM input bias and performing complex tasks, including distinguishing claims from evidence, integrating text/photo/figure analysis to infer parameters, executing quantitative feasibility checks, comparing estimates against claims, and assessing a priori plausibility. To ensure transparency and facilitate replication, we provide full prompts, detailed demonstration analyses, and logs of interactive chats as supplementary resources. Beyond the specific application, this work offers insights into the meta-development process itself, highlighting the potential of PWP, informed by detailed workflow formalization, to enable sophisticated analysis using readily available LLMs for complex scientific tasks.

