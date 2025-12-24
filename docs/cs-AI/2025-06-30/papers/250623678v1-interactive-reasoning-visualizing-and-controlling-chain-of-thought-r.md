---
layout: default
title: "Interactive Reasoning: Visualizing and Controlling Chain-of-Thought Reasoning in Large Language Models"
---

# Interactive Reasoning: Visualizing and Controlling Chain-of-Thought Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23678" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23678v1</a>
  <a href="https://arxiv.org/pdf/2506.23678.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23678v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23678v1', 'Interactive Reasoning: Visualizing and Controlling Chain-of-Thought Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rock Yuren Pang, K. J. Kevin Feng, Shangbin Feng, Chu Li, Weijia Shi, Yulia Tsvetkov, Jeffrey Heer, Katharina Reinecke

**分类**: cs.HC, cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出交互推理以优化大型语言模型的思维链输出**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `思维链推理` `用户交互` `可视化技术` `AI辅助决策`

## 📋 核心要点

1. 现有大型语言模型的推理过程缺乏用户反馈，导致输出冗长且难以组织，影响用户体验。
2. 本文提出交互推理，通过可视化思维链输出，允许用户对内容进行审查和修改，提升模型的响应质量。
3. 用户研究表明，交互推理显著提高了用户识别错误生成的效率，并增强了对模型推理过程的理解。

## 📝 摘要（中文）

大型语言模型（LLMs）的输出质量可以通过“推理”来提升，即生成思维链（CoT）内容片段以进一步条件化模型。然而，这些思维链信息冗长且缺乏明确的组织，审查过程繁琐。此外，用户反馈的机会有限。本文提出交互推理，通过将思维链输出可视化为主题层次结构，允许用户审查和修改。我们在Hippo中实现了交互推理，这是一个用于不确定权衡的AI辅助决策原型。在对16名参与者的用户研究中，我们发现Hippo中的交互推理使用户能够快速识别和中断错误生成，有效引导模型朝向定制化响应，并更好地理解模型推理和输出。我们的工作为将用户监督纳入LLM推理过程开辟了新范式。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成思维链时缺乏用户反馈和组织性的问题，导致输出内容冗长且难以审查。

**核心思路**：交互推理的核心思想是将思维链输出可视化为层次结构，允许用户对内容进行审查和修改，从而提高输出的相关性和准确性。

**技术框架**：整体架构包括思维链生成模块、可视化层次结构模块和用户交互模块。用户可以通过交互界面对思维链进行修改，影响最终输出。

**关键创新**：最重要的创新在于将用户反馈机制整合到推理过程中，使用户能够主动参与到模型的生成过程中，显著改善了输出质量。

**关键设计**：在设计中，采用了层次化的主题结构来组织思维链，用户可以通过简单的界面进行修改，且系统能够实时更新生成的内容。

## 📊 实验亮点

实验结果显示，交互推理显著提高了用户识别错误生成的速度，用户能够更有效地引导模型生成定制化响应。用户对模型推理过程的理解也得到了增强，表明该方法在提升用户体验方面具有显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、教育工具和决策支持系统等。通过引入用户交互，能够提升模型的可用性和用户满意度，未来可能在多种人机交互场景中发挥重要作用。

## 📄 摘要（原文）

> The output quality of large language models (LLMs) can be improved via "reasoning": generating segments of chain-of-thought (CoT) content to further condition the model prior to producing user-facing output. While these chains contain valuable information, they are verbose and lack explicit organization, making them tedious to review. Moreover, they lack opportunities for user feedback, such as to remove unwanted considerations, add desired ones, or clarify unclear assumptions. We introduce Interactive Reasoning, an interaction design that visualizes chain-of-thought outputs as a hierarchy of topics and enables user review and modification. We implement interactive reasoning in Hippo, a prototype for AI-assisted decision making in the face of uncertain trade-offs. In a user study with 16 participants, we find that interactive reasoning in Hippo allows users to quickly identify and interrupt erroneous generations, efficiently steer the model towards customized responses, and better understand both model reasoning and model outputs. Our work contributes to a new paradigm that incorporates user oversight into LLM reasoning processes.

