---
layout: default
title: "Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-level Code Generation Tasks"
---

# Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-level Code Generation Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04125" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04125v1</a>
  <a href="https://arxiv.org/pdf/2508.04125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04125v1', 'Experimental Analysis of Productive Interaction Strategy with ChatGPT: User Study on Function and Project-level Code Generation Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangwon Hyun, Hyunjun Kim, Jinhyuk Jang, Hyojin Choi, M. Ali Babar

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-06

**备注**: The benchmark repository has not been publicly released yet due to the IP policy in our institutions. If you would like to use the benchmark or collaborate on extension, please contact "dr.sangwon.hyun@gmail.com"

---

## 💡 一句话要点

**提出有效的交互策略以提升ChatGPT在代码生成中的生产力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `代码生成` `大型语言模型` `软件工程` `用户研究` `生产力提升` `错误分类`

## 📋 核心要点

1. 现有研究主要集中在功能级别的提示模式，忽视了复杂的多类依赖和人机交互特征对代码生成的影响。
2. 本文设计了一项实验，分析人机交互特征对代码生成生产力的影响，提出了项目级基准任务。
3. 研究结果表明，有3个交互特征显著影响生产力，并提出了5条提升人机交互过程的指导原则。

## 📝 摘要（中文）

大型语言模型（LLMs）在软件工程任务中的应用日益增长。然而，现有研究主要集中在功能级别的提示模式，忽视了更复杂的真实工作流程。为此，本文设计了一项实验，全面分析了人机交互特征对代码生成生产力的影响。研究中提出了两个项目级基准任务，并通过与36名来自不同背景的参与者的用户研究，探讨了特定提示模式下的交互体验。结果显示，15个交互特征中有3个显著影响代码生成的生产力，并提出了5条提升人机交互过程生产力的指导原则，以及29种可能出现的运行时和逻辑错误的分类及缓解方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有研究在代码生成中对人机交互特征关注不足的问题，尤其是在复杂的多类依赖场景下的应用。现有方法主要集中于功能级别，缺乏对项目级别复杂性的考虑。

**核心思路**：通过设计实验，全面分析人机交互特征对代码生成生产力的影响，扩展研究范围至项目级别任务，以更好地反映真实工作流程中的复杂性。

**技术框架**：研究包括两个主要阶段：首先是设计项目级基准任务，其次是进行用户研究，收集参与者与GPT助手交互的屏幕录制和聊天记录进行分析。

**关键创新**：本文的创新在于提出了一个涵盖多类依赖的项目级任务框架，并识别出影响生产力的特定人机交互特征，与传统的功能级别研究形成鲜明对比。

**关键设计**：研究中分析了15个交互特征，确定了3个显著影响生产力的特征，并提出了5条指导原则和29种错误分类及其缓解方案。

## 📊 实验亮点

实验结果显示，15个交互特征中有3个显著影响代码生成的生产力，提供了5条提升人机交互过程的指导原则。此外，研究还分类了29种可能出现的运行时和逻辑错误，并提出了相应的缓解方案。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化代码生成和人机交互设计等。通过优化人机交互策略，可以提升开发者在使用大型语言模型时的生产力，进而推动软件工程领域的创新与效率提升。

## 📄 摘要（原文）

> The application of Large Language Models (LLMs) is growing in the productive completion of Software Engineering tasks. Yet, studies investigating the productive prompting techniques often employed a limited problem space, primarily focusing on well-known prompting patterns and mainly targeting function-level SE practices. We identify significant gaps in real-world workflows that involve complexities beyond class-level (e.g., multi-class dependencies) and different features that can impact Human-LLM Interactions (HLIs) processes in code generation. To address these issues, we designed an experiment that comprehensively analyzed the HLI features regarding the code generation productivity. Our study presents two project-level benchmark tasks, extending beyond function-level evaluations. We conducted a user study with 36 participants from diverse backgrounds, asking them to solve the assigned tasks by interacting with the GPT assistant using specific prompting patterns. We also examined the participants' experience and their behavioral features during interactions by analyzing screen recordings and GPT chat logs. Our statistical and empirical investigation revealed (1) that three out of 15 HLI features significantly impacted the productivity in code generation; (2) five primary guidelines for enhancing productivity for HLI processes; and (3) a taxonomy of 29 runtime and logic errors that can occur during HLI processes, along with suggested mitigation plans.

