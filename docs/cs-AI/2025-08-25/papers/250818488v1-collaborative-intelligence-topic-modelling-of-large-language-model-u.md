---
layout: default
title: "Collaborative Intelligence: Topic Modelling of Large Language Model use in Live Cybersecurity Operations"
---

# Collaborative Intelligence: Topic Modelling of Large Language Model use in Live Cybersecurity Operations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18488" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18488v1</a>
  <a href="https://arxiv.org/pdf/2508.18488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18488v1', 'Collaborative Intelligence: Topic Modelling of Large Language Model use in Live Cybersecurity Operations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martin Lochner, Keegan Keplinger

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**通过主题建模提升大型语言模型在网络安全操作中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `网络安全` `主题建模` `安全运营中心` `人机协作` `实时操作` `文本理解`

## 📋 核心要点

1. 现有研究对人机协作的探讨较多，但对大型语言模型在实时网络安全中的具体应用尚缺乏深入分析。
2. 本研究通过对SOC操作人员使用GPT-4的10个月数据进行主题建模，探索LLM在安全操作中的实际应用情况。
3. 研究发现，SOC操作人员主要利用LLM来理解复杂指令，表明LLM工具的设计可以有效增强其工作效率。

## 📝 摘要（中文）

本研究描述了安全运营中心（SOC）在实时安全操作中使用大型语言模型（LLM）的主题建模，旨在深入理解这些专家如何自愿使用这一工具。尽管人机协作团队已被广泛研究，但基于变换器的语言模型引发了新的协作浪潮。研究表明，SOC操作人员主要利用LLM来帮助理解复杂文本字符串，约40%的LLM使用情况与此相关。研究结果表明，设计协作LLM工具可以有效支持SOC操作人员的工作流程。

## 🔬 方法详解

**问题定义**：本研究旨在解决SOC操作人员在实时安全操作中如何有效利用大型语言模型（LLM）的问题。现有方法未能充分揭示LLM在此领域的具体应用和效果。

**核心思路**：通过对SOC操作人员使用LLM的实际数据进行主题建模，研究其使用模式和需求，从而为设计更有效的协作工具提供依据。

**技术框架**：研究采用了两种主题建模方法：首先使用了现有的BERTopic模型，其次开发了一种新的主题建模工作流程。数据集来自于SOC操作人员在内部HTTP聊天应用中访问GPT-4的记录。

**关键创新**：本研究的创新点在于通过结合传统和新颖的主题建模方法，深入分析LLM在SOC中的具体应用场景，揭示了操作人员对LLM的依赖程度和使用模式。

**关键设计**：在BERTopic模型中，采用了基于嵌入的聚类方法，而新模型则可能引入了不同的文本处理和主题识别策略，以更好地捕捉SOC操作人员的需求。

## 📊 实验亮点

研究结果表明，SOC操作人员约40%的LLM使用情况与理解复杂文本字符串相关。通过BERTopic分析和新模型的应用，揭示了LLM在实时安全操作中的重要性，为未来工具的设计提供了实证基础。

## 🎯 应用场景

该研究为下一代安全运营中心工具的开发提供了重要参考。通过理解SOC操作人员的常见使用场景，可以设计出更符合实际需求的工作流程，例如在SOC环境中直接执行命令行分析的右键上下文菜单。此类工具将极大提升操作人员的工作效率和准确性。

## 📄 摘要（原文）

> Objective: This work describes the topic modelling of Security Operations Centre (SOC) use of a large language model (LLM), during live security operations. The goal is to better understand how these specialists voluntarily use this tool.
>   Background: Human-automation teams have been extensively studied, but transformer-based language models have sparked a new wave of collaboration. SOC personnel at a major cybersecurity provider used an LLM to support live security operations. This study examines how these specialists incorporated the LLM into their work.
>   Method: Our data set is the result of 10 months of SOC operators accessing GPT-4 over an internally deployed HTTP-based chat application. We performed two topic modelling exercises, first using the established BERTopic model (Grootendorst, 2022), and second, using a novel topic modeling workflow.
>   Results: Both the BERTopic analysis and novel modelling approach revealed that SOC operators primarily used the LLM to facilitate their understanding of complex text strings. Variations on this use-case accounted for ~40% of SOC LLM usage.
>   Conclusion: SOC operators are required to rapidly interpret complex commands and similar information. Their natural tendency to leverage LLMs to support this activity indicates that their workflow can be supported and augmented by designing collaborative LLM tools for use in the SOC.
>   Application: This work can aid in creating next-generation tools for Security Operations Centres. By understanding common use-cases, we can develop workflows supporting SOC task flow. One example is a right-click context menu for executing a command line analysis LLM call directly in the SOC environment.

