---
layout: default
title: "Orchid: Orchestrating Context Across Creative Workflows with Generative AI"
---

# Orchid: Orchestrating Context Across Creative Workflows with Generative AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19517" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19517v1</a>
  <a href="https://arxiv.org/pdf/2508.19517.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19517v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19517v1', 'Orchid: Orchestrating Context Across Creative Workflows with Generative AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Srishti Palani, Gonzalo Ramos

**分类**: cs.HC, cs.AI

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出Orchid以解决创意工作流中的上下文管理问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `生成式人工智能` `上下文管理` `创意工作流` `用户体验` `系统设计`

## 📋 核心要点

1. 现有工具在跨多个交互和会话的创意工作流中，无法有效管理上下文，导致用户创造力受限。
2. Orchid系统通过允许用户指定、引用和监控上下文，解决了上下文管理的挑战，增强了创意工作流的连贯性。
3. 实验结果显示，使用Orchid的用户在创意任务中产生了更具新颖性和可行性的结果，且感知控制感和透明度显著提高。

## 📝 摘要（中文）

上下文对于人类与生成式人工智能（GenAI）之间的有意义互动至关重要。然而，现有工具在跨多个交互、会话和模型的工作流中，提供的上下文管理手段有限，尤其是在创意项目中。用户在重新指定先前细节、处理多样化的工件和应对上下文漂移时，常常感到不堪重负，模糊了意图并限制了创造力。为了解决这些挑战，本文提出了Orchid系统，帮助用户在不断演变的工作流中指定、引用和监控上下文。研究表明，使用Orchid的参与者在创意任务中产生了更具新颖性和可行性的结果，且与AI的响应之间的意图一致性更高，感知控制感和透明度也有所提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何在创意工作流中有效管理上下文。现有方法在多次交互中无法保持上下文一致性，导致用户意图模糊和创造力受限。

**核心思路**：Orchid的核心思路是提供一个系统，使用户能够在工作流中指定、引用和监控上下文信息，从而增强用户与AI之间的互动质量。这样的设计旨在减少上下文漂移，提高用户的创造力和控制感。

**技术框架**：Orchid系统的整体架构包括三个主要模块：上下文指定模块、上下文引用模块和上下文监控模块。用户可以通过这些模块在不同的交互中管理上下文信息。

**关键创新**：Orchid的关键创新在于其上下文管理的灵活性，用户可以通过显式提及、内联选择或隐式基础来引用上下文，这与现有工具的单一引用方式形成了鲜明对比。

**关键设计**：在设计上，Orchid允许用户根据项目、个人和不同风格来指定上下文，并通过直观的界面进行管理。具体的参数设置和交互设计细节在论文中进行了详细描述。

## 📊 实验亮点

在一项包含12名参与者的实验中，使用Orchid的用户在创意任务中产生的结果比基线工具（如网络搜索、基于LLM的聊天和数字笔记本）更具新颖性和可行性。参与者报告称，他们的意图与AI的响应之间的对齐度更高，感知控制感和透明度也显著提升。

## 🎯 应用场景

Orchid系统在创意产业、设计、艺术创作等领域具有广泛的应用潜力。通过有效管理上下文，Orchid能够帮助创作者在复杂的工作流中保持一致性，从而提升创作效率和质量。未来，Orchid的设计理念也可以扩展到其他需要上下文管理的领域，如教育和协作工具。

## 📄 摘要（原文）

> Context is critical for meaningful interactions between people and Generative AI (GenAI). Yet mainstream tools offer limited means to orchestrate it, particularly across workflows that span multiple interactions, sessions, and models, as often occurs in creative projects. Re specifying prior details, juggling diverse artifacts, and dealing with context drift overwhelm users, obscure intent, and curtail creativity. To address these challenges, we present Orchid, a system that gives its users affordances to specify, reference, and monitor context throughout evolving workflows. Specifically, Orchid enables users to (1) specify context related to the project, themselves, and different styles, (2) reference these via explicit mentions, inline selection, or implicit grounding, and (3) monitor context assigned to different interactions across the workflow. In a within-subjects study (n=12), participants using Orchid to execute creative tasks (compared to a baseline toolkit of web search, LLM-based chat, and digital notebooks) produced more novel and feasible outcomes, reporting greater alignment between their intent and the AI's responses, higher perceived control, and increased transparency. By prioritizing context orchestration, Orchid offers an actionable step toward next generation GenAI tools that support complex, iterative workflows - enabling creators and AI to stay aligned and augment their creative potential.

