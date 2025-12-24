---
layout: default
title: "Talk Less, Call Right: Enhancing Role-Play LLM Agents with Automatic Prompt Optimization and Role Prompting"
---

# Talk Less, Call Right: Enhancing Role-Play LLM Agents with Automatic Prompt Optimization and Role Prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00482" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00482v2</a>
  <a href="https://arxiv.org/pdf/2509.00482.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00482v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00482v2', 'Talk Less, Call Right: Enhancing Role-Play LLM Agents with Automatic Prompt Optimization and Role Prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saksorn Ruangtanusak, Pittawat Taveekitworachai, Kunat Pipatanakul

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-08-30 (更新: 2025-10-12)

**备注**: EMNLP 2025 Wordplay Workshop (Spotlight)

**🔗 代码/项目**: [GITHUB](https://github.com/scb-10x/apo)

---

## 💡 一句话要点

**提出角色提示优化方法以解决对话代理过度发言问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `角色扮演` `对话代理` `提示优化` `工具使用` `人工智能`

## 📋 核心要点

1. 现有的对话代理在生成角色内回应时常常过度发言，且未能有效利用工具，导致响应质量下降。
2. 论文提出了四种提示方法，其中基于规则的角色提示（RRP）通过创新设计显著改善了对话代理的表现。
3. 实验结果显示，RRP方法的整体得分为0.571，超越了零样本基线得分0.519，展现了其有效性。

## 📝 摘要（中文）

本报告探讨了增强工具增强的大型语言模型（LLM）作为角色扮演对话代理的提示方法，特别是在2025年常识人格基础对话挑战（CPDC）的API轨道中。在此背景下，对话代理常常产生过长的角色内回应（过度发言），同时未能根据角色有效使用工具（未能行动），例如生成不存在的函数调用或在回答前进行不必要的工具调用。我们探索了四种提示方法：基本角色提示、改进角色提示、自动提示优化（APO）和基于规则的角色提示。基于规则的角色提示（RRP）通过角色卡片/场景合同设计和严格执行函数调用这两种新技术实现了最佳性能，整体得分为0.571，相较于零样本基线得分0.519有显著提升。这些发现表明，RRP设计可以显著提高角色扮演对话代理的有效性和可靠性。我们将开源所有最佳表现的提示和APO工具的源代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决角色扮演对话代理在生成回应时的过度发言和未能有效使用工具的问题。现有方法往往导致生成的回应过长且不符合角色设定，影响对话的自然性和有效性。

**核心思路**：论文提出的解决方案包括四种提示方法，特别是基于规则的角色提示（RRP），通过创新的角色卡片和场景合同设计，严格控制函数调用，以提高对话代理的表现。

**技术框架**：整体架构包括角色提示的设计、函数调用的管理和响应生成三个主要模块。通过对角色信息的结构化处理，确保生成的回应既符合角色设定又简洁有效。

**关键创新**：最重要的技术创新在于RRP方法的设计，通过角色卡片/场景合同的结合和严格的函数调用管理，与现有方法相比，显著提高了对话代理的有效性和可靠性。

**关键设计**：在RRP中，角色卡片提供了角色的背景信息，而场景合同则定义了对话的上下文和预期行为。严格的函数调用规则确保了对话代理在生成回应时能够准确调用必要的工具，避免不必要的调用。

## 📊 实验亮点

实验结果显示，基于规则的角色提示（RRP）方法的整体得分为0.571，显著高于零样本基线得分0.519，提升幅度达到10%。这一结果表明，RRP在提高角色扮演对话代理的有效性和可靠性方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、虚拟助手和游戏中的角色扮演系统等。通过优化对话代理的响应质量和工具使用效率，可以提升用户体验，增强人机交互的自然性和流畅性。未来，该方法还可能推动更复杂的对话系统的发展，促进人工智能在社交场景中的应用。

## 📄 摘要（原文）

> This report investigates approaches for prompting a tool-augmented large language model (LLM) to act as a role-playing dialogue agent in the API track of the Commonsense Persona-grounded Dialogue Challenge (CPDC) 2025. In this setting, dialogue agents often produce overly long in-character responses (over-speaking) while failing to use tools effectively according to the persona (under-acting), such as generating function calls that do not exist or making unnecessary tool calls before answering. We explore four prompting approaches to address these issues: 1) basic role prompting, 2) improved role prompting, 3) automatic prompt optimization (APO), and 4) rule-based role prompting. The rule-based role prompting (RRP) approach achieved the best performance through two novel techniques-character-card/scene-contract design and strict enforcement of function calling-which led to an overall score of 0.571, improving on the zero-shot baseline score of 0.519. These findings demonstrate that RRP design can substantially improve the effectiveness and reliability of role-playing dialogue agents compared with more elaborate methods such as APO. To support future efforts in developing persona prompts, we are open-sourcing all of our best-performing prompts and the APO tool Source code is available at https://github.com/scb-10x/apo

