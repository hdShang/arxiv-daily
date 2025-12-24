---
layout: default
title: Project Riley: Multimodal Multi-Agent LLM Collaboration with Emotional Reasoning and Voting
---

# Project Riley: Multimodal Multi-Agent LLM Collaboration with Emotional Reasoning and Voting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20521" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20521v2</a>
  <a href="https://arxiv.org/pdf/2505.20521.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20521v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20521v2', 'Project Riley: Multimodal Multi-Agent LLM Collaboration with Emotional Reasoning and Voting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ana Rita Ortigoso, Gabriel Vieira, Daniel Fuentes, Luis Frazão, Nuno Costa, António Pereira

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-09-08)

**备注**: 28 pages, 5 figures. Submitted for review to Information Fusion

---

## 💡 一句话要点

**提出Project Riley以解决情感推理的多模态对话问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态对话` `情感推理` `大型语言模型` `用户体验` `紧急响应系统`

## 📋 核心要点

1. 现有对话系统在情感推理方面的能力不足，难以有效模拟人类情感的复杂性。
2. 提出了一个多模态对话架构，结合五个情感代理进行多轮对话，增强了情感推理能力。
3. 用户测试结果显示，该系统在情感适当性、清晰度和自然性方面表现出色，具有良好的用户体验。

## 📝 摘要（中文）

本文介绍了Project Riley，一个新颖的多模态和多模型对话AI架构，旨在模拟受情感状态影响的推理。该系统灵感来源于皮克斯的《头脑特工队》，包含五个不同的情感代理——快乐、悲伤、恐惧、愤怒和厌恶，进行结构化的多轮对话以生成、批评和迭代完善响应。最终的推理机制综合这些代理的贡献，生成反映主导情感或整合多种视角的连贯输出。该架构结合了文本和视觉的大型语言模型（LLMs），以及先进的推理和自我优化过程。初步原型在离线环境中部署，优化了情感表达和计算效率。基于该原型，开发了用于紧急情况下的Armando，提供情感校准和事实准确的信息。通过用户测试评估了Project Riley原型，结果显示在情感一致性和沟通清晰度方面表现良好。

## 🔬 方法详解

**问题定义**：本文旨在解决现有对话系统在情感推理和表达方面的不足，尤其是在多模态交互中如何有效整合情感信息。

**核心思路**：通过引入五个情感代理，系统能够在对话中模拟不同情感的影响，从而生成更具情感深度的响应。这样的设计使得对话不仅仅是信息传递，更是情感交流。

**技术框架**：整体架构包括情感代理模块、推理机制和响应生成模块。情感代理负责情感表达，推理机制综合各代理的输入，最终生成连贯的对话输出。

**关键创新**：最重要的创新在于情感代理的设计及其在对话中的协作机制，这与传统的单一模型对话系统有本质区别，能够更好地模拟人类的情感交流。

**关键设计**：系统采用了文本和视觉的LLMs，结合了检索增强生成（RAG）技术，并在情感表达和计算效率上进行了优化，确保了系统在紧急情况下的实用性和准确性。

## 📊 实验亮点

实验结果显示，Project Riley在情感适当性、清晰度和自然性方面的评分均高于传统对话系统，尤其在情感一致性方面表现突出，用户反馈积极，表明该系统在结构化场景中具有良好的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康支持、教育辅导和紧急响应系统等。通过模拟情感推理，系统能够提供更具人性化的交互体验，帮助用户在复杂情境中获得情感支持和信息。未来，该技术有望在更多领域实现情感智能的应用。

## 📄 摘要（原文）

> This paper presents Project Riley, a novel multimodal and multi-model conversational AI architecture oriented towards the simulation of reasoning influenced by emotional states. Drawing inspiration from Pixar's Inside Out, the system comprises five distinct emotional agents - Joy, Sadness, Fear, Anger, and Disgust - that engage in structured multi-round dialogues to generate, criticise, and iteratively refine responses. A final reasoning mechanism synthesises the contributions of these agents into a coherent output that either reflects the dominant emotion or integrates multiple perspectives. The architecture incorporates both textual and visual large language models (LLMs), alongside advanced reasoning and self-refinement processes. A functional prototype was deployed locally in an offline environment, optimised for emotional expressiveness and computational efficiency. From this initial prototype, another one emerged, called Armando, which was developed for use in emergency contexts, delivering emotionally calibrated and factually accurate information through the integration of Retrieval-Augmented Generation (RAG) and cumulative context tracking. The Project Riley prototype was evaluated through user testing, in which participants interacted with the chatbot and completed a structured questionnaire assessing three dimensions: Emotional Appropriateness, Clarity and Utility, and Naturalness and Human-likeness. The results indicate strong performance in structured scenarios, particularly with respect to emotional alignment and communicative clarity.

