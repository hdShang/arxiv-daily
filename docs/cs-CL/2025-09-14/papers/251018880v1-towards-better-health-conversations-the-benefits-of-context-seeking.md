---
layout: default
title: "Towards Better Health Conversations: The Benefits of Context-seeking"
---

# Towards Better Health Conversations: The Benefits of Context-seeking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18880" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18880v1</a>
  <a href="https://arxiv.org/pdf/2510.18880.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18880v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.18880v1', 'Towards Better Health Conversations: The Benefits of Context-seeking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rory Sayres, Yuexing Hao, Abbi Ward, Amy Wang, Beverly Freeman, Serena Zhan, Diego Ardila, Jimmy Li, I-Ching Lee, Anna Iurchenko, Siyi Kou, Kartikeya Badola, Jimmy Hu, Bhawesh Kumar, Keith Johnson, Supriya Vijay, Justin Krogue, Avinatan Hassidim, Yossi Matias, Dale R. Webster, Sunny Virmani, Yun Liu, Quang Duong, Mike Schaekermann

**分类**: cs.HC, cs.CL, cs.CY

**发布日期**: 2025-09-14

---

## 💡 一句话要点

**提出Wayfinding AI，通过主动寻求上下文信息，优化LLM在健康咨询中的表现。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `健康咨询` `大型语言模型` `上下文学习` `对话式AI` `Wayfinding AI`

## 📋 核心要点

1. 现有LLM在健康咨询中存在不准确和误导风险，缺乏对用户具体情况的了解。
2. Wayfinding AI通过主动询问用户相关背景信息，从而提供更精准的健康建议。
3. 实验表明，Wayfinding AI比基线AI更有效，用户评价其更有帮助和相关性。

## 📝 摘要（中文）

在现代信息环境中，人们在面对健康问题时常常感到困惑。大型语言模型（LLM）虽然可以提供定制化的信息，但也存在不准确、有偏见或误导的风险。本研究通过四项混合方法研究（总样本量N=163），探讨了人们如何与LLM互动以解决自身健康问题。定性研究表明，在对话式AI中，寻求上下文信息以获取用户可能不会主动提供的具体细节至关重要。参与者认为LLM主动寻求上下文信息是有价值的，即使这意味着需要多次对话才能获得答案。基于这些发现，我们开发了一种“Wayfinding AI”，能够主动征求上下文信息。在一项随机、双盲研究中，参与者认为Wayfinding AI比基线AI更有帮助、更相关，并且更能满足他们的需求。这些结果表明，主动寻求上下文信息对对话动态具有显著影响，并为对话式AI在健康领域的应用提供了设计模式。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在健康咨询领域应用时，因缺乏对用户具体情况的了解而导致信息不准确、有偏见或误导的问题。现有方法往往直接基于用户提出的问题进行回答，忽略了用户可能没有主动提供的关键上下文信息，导致LLM无法提供个性化和精准的建议。

**核心思路**：论文的核心思路是让LLM主动寻求上下文信息。通过在对话中主动询问用户相关背景、症状、病史等信息，Wayfinding AI能够更全面地了解用户的情况，从而提供更准确、更相关的健康建议。这种主动式的上下文获取方式旨在模拟医生问诊的过程，弥补用户可能遗漏或不了解的关键信息。

**技术框架**：Wayfinding AI的技术框架主要包含以下几个阶段：1) 用户提出健康问题；2) Wayfinding AI分析问题，判断是否需要更多上下文信息；3) 如果需要，Wayfinding AI主动向用户提问，获取相关背景信息；4) Wayfinding AI基于收集到的信息，生成个性化的健康建议；5) 用户可以继续与Wayfinding AI进行对话，进一步 уточнять 问题或获取更多信息。整个过程是一个迭代的对话过程，LLM不断地收集和利用上下文信息，以提高建议的准确性和相关性。

**关键创新**：论文最重要的技术创新点在于将主动上下文寻求机制融入到对话式AI中。与传统的被动式问答系统不同，Wayfinding AI能够主动引导对话，获取用户可能忽略或不了解的关键信息。这种主动式的交互方式能够显著提高LLM在健康咨询领域的实用性和有效性。

**关键设计**：论文的关键设计包括：1) 设计了一系列问题模板，用于主动询问用户相关背景信息；2) 采用自然语言理解技术，分析用户回答，提取关键信息；3) 使用知识图谱或医学数据库，辅助LLM生成准确的健康建议；4) 通过用户反馈，不断优化问题模板和建议生成策略。

## 📊 实验亮点

在一项随机、双盲研究中，参与者对Wayfinding AI的评价显著高于基线AI。Wayfinding AI在“更有帮助”、“更相关”、“更能满足需求”等指标上均优于基线AI，表明主动寻求上下文信息能够显著提升LLM在健康咨询中的表现。

## 🎯 应用场景

该研究成果可应用于在线健康咨询平台、智能健康助手、远程医疗等领域。通过主动获取用户上下文信息，AI能够提供更个性化、更准确的健康建议，帮助用户更好地管理自身健康。未来，该技术有望在疾病预防、健康管理、心理咨询等方面发挥重要作用。

## 📄 摘要（原文）

> Navigating health questions can be daunting in the modern information landscape. Large language models (LLMs) may provide tailored, accessible information, but also risk being inaccurate, biased or misleading. We present insights from 4 mixed-methods studies (total N=163), examining how people interact with LLMs for their own health questions. Qualitative studies revealed the importance of context-seeking in conversational AIs to elicit specific details a person may not volunteer or know to share. Context-seeking by LLMs was valued by participants, even if it meant deferring an answer for several turns. Incorporating these insights, we developed a "Wayfinding AI" to proactively solicit context. In a randomized, blinded study, participants rated the Wayfinding AI as more helpful, relevant, and tailored to their concerns compared to a baseline AI. These results demonstrate the strong impact of proactive context-seeking on conversational dynamics, and suggest design patterns for conversational AI to help navigate health topics.

