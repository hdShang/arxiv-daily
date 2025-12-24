---
layout: default
title: "Large Language Models for Security Operations Centers: A Comprehensive Survey"
---

# Large Language Models for Security Operations Centers: A Comprehensive Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10858" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10858v2</a>
  <a href="https://arxiv.org/pdf/2509.10858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10858v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10858v2', 'Large Language Models for Security Operations Centers: A Comprehensive Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Habibzadeh, Farid Feyzi, Reza Ebrahimi Atani

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-13 (更新: 2025-09-19)

---

## 💡 一句话要点

**综述：大型语言模型在安全运营中心的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全运营中心` `网络安全` `事件响应` `威胁情报`

## 📋 核心要点

1. 安全运营中心面临海量警报、专家资源短缺、响应迟缓和威胁情报利用不足等挑战。
2. 利用大型语言模型自动化日志分析、简化事件分流、提升检测精度并加速知识获取。
3. 本综述全面探讨LLM在SOC工作流程中的集成，分析其能力、挑战和未来发展方向。

## 📝 摘要（中文）

大型语言模型（LLM）作为一种能够理解和生成类人文本的强大工具，在各个领域都展现出变革潜力。安全运营中心（SOC）负责保护数字基础设施，是其中一个重要领域。SOC是网络安全的第一道防线，负责持续监控、检测和响应安全事件。然而，SOC面临着高警报量、资源有限、对具备高级知识的专家需求高、响应时间延迟以及难以有效利用威胁情报等持续挑战。在此背景下，LLM可以通过自动化日志分析、简化事件分流、提高检测准确性以及在更短时间内提供所需知识来提供有希望的解决方案。本综述系统地探讨了生成式AI，特别是LLM集成到SOC工作流程中的情况，提供了对其能力、挑战和未来方向的结构化视角。我们相信，本综述为研究人员和SOC管理人员提供了LLM在学术研究中集成应用的广泛概述。据我们所知，这是第一个详细检查LLM在SOC中应用的综合性研究。

## 🔬 方法详解

**问题定义**：安全运营中心（SOC）面临着日益严峻的网络安全威胁，需要持续监控、检测和响应安全事件。然而，SOC普遍存在警报疲劳、专家资源不足、响应时间过长以及威胁情报利用率低等问题。现有方法难以有效应对这些挑战，导致安全事件的检测和响应效率低下。

**核心思路**：本综述的核心思路是探索如何利用大型语言模型（LLM）的强大能力来解决SOC面临的挑战。LLM在自然语言处理方面表现出色，可以用于自动化日志分析、简化事件分流、提高检测准确性，并为安全分析师提供快速的知识支持。通过将LLM集成到SOC工作流程中，可以显著提高安全运营效率和响应速度。

**技术框架**：本综述没有提出新的技术框架，而是对现有研究进行了系统性的整理和分析。它探讨了LLM在SOC中的各种应用，包括：日志分析自动化、事件分流优化、威胁检测增强、威胁情报利用以及安全知识问答。综述分析了每种应用的优势和局限性，并讨论了未来的研究方向。

**关键创新**：本综述的关键创新在于它是第一个全面系统地研究LLM在SOC中应用的综述。它整合了来自不同领域的学术研究，为研究人员和SOC管理人员提供了一个关于LLM在安全运营领域应用的全面视角。

**关键设计**：本综述没有涉及具体的技术细节，而是侧重于对现有研究的分析和总结。它讨论了LLM在SOC中的各种应用，并分析了每种应用的优势和局限性。综述还探讨了LLM在SOC中应用面临的挑战，例如数据隐私、模型安全和可解释性。

## 📊 实验亮点

本综述是首个全面考察LLM在SOC应用的综合研究，系统性地分析了LLM在日志分析、事件分流和威胁检测等方面的潜力，为研究人员和SOC管理者提供了宝贵的参考，并指出了未来研究方向。

## 🎯 应用场景

该研究成果对网络安全领域具有重要应用价值。通过将大型语言模型应用于安全运营中心，可以显著提高安全事件的检测和响应效率，降低安全风险。该研究为未来的研究方向提供了指导，例如开发更安全、更可解释的LLM模型，以及探索LLM在其他安全领域的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have emerged as powerful tools capable of understanding and generating human-like text, offering transformative potential across diverse domains. The Security Operations Center (SOC), responsible for safeguarding digital infrastructure, represents one of these domains. SOCs serve as the frontline of defense in cybersecurity, tasked with continuous monitoring, detection, and response to incidents. However, SOCs face persistent challenges such as high alert volumes, limited resources, high demand for experts with advanced knowledge, delayed response times, and difficulties in leveraging threat intelligence effectively. In this context, LLMs can offer promising solutions by automating log analysis, streamlining triage, improving detection accuracy, and providing the required knowledge in less time. This survey systematically explores the integration of generative AI and more specifically LLMs into SOC workflow, providing a structured perspective on its capabilities, challenges, and future directions. We believe that this survey offers researchers and SOC managers a broad overview of the current state of LLM integration within academic study. To the best of our knowledge, this is the first comprehensive study to examine LLM applications in SOCs in details.

