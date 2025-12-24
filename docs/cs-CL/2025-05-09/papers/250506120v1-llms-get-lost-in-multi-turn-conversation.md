---
layout: default
title: LLMs Get Lost In Multi-Turn Conversation
---

# LLMs Get Lost In Multi-Turn Conversation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06120" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06120v1</a>
  <a href="https://arxiv.org/pdf/2505.06120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06120v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06120v1', 'LLMs Get Lost In Multi-Turn Conversation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville

**分类**: cs.CL, cs.HC

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**揭示LLMs在多轮对话中表现不佳的原因**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多轮对话` `性能评估` `用户指令` `对话系统`

## 📋 核心要点

1. 现有研究主要集中在单轮、明确指令的设置，忽视了多轮对话中用户指令的不明确性及其对LLMs性能的影响。
2. 本文通过大规模模拟实验，比较LLMs在单轮与多轮对话中的表现，揭示其在多轮对话中的性能下降原因。
3. 实验结果显示，所有测试的LLMs在多轮对话中性能下降，平均下降39%，并分析了性能下降的两个主要因素。

## 📝 摘要（中文）

大型语言模型（LLMs）作为对话接口，能够在用户明确任务时提供帮助，但在多轮对话中，LLMs的表现显著低于单轮对话。本文通过大规模模拟实验，比较了LLMs在单轮和多轮设置下的性能，发现所有测试的LLMs在多轮对话中表现下降，平均下降幅度达到39%。分析表明，性能下降主要源于早期对话中的假设错误和最终解决方案的过早生成，导致模型在对话中迷失方向，难以恢复。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多轮对话中表现不佳的问题。现有方法主要关注单轮对话，未能有效应对用户指令的不明确性和多轮交互的复杂性。

**核心思路**：通过大规模模拟实验，比较LLMs在单轮和多轮对话中的性能，分析其表现下降的原因，特别是模型在对话早期的假设和生成最终解决方案的倾向。

**技术框架**：整体架构包括数据收集、模拟对话生成、性能评估和结果分析四个主要模块。数据收集阶段获取200,000+对话样本，模拟对话生成阶段设计多轮交互场景，性能评估阶段通过多项生成任务评估模型表现，最后进行结果分析。

**关键创新**：本文的创新在于系统性地分析了LLMs在多轮对话中的性能下降，揭示了模型在对话早期的假设错误和过早生成最终答案的倾向，这与现有方法的单轮对话评估形成鲜明对比。

**关键设计**：在实验中，设置了多种生成任务，采用了不同的评估指标来量化模型的表现，特别关注了模型在多轮对话中的可靠性和适应性。

## 📊 实验亮点

实验结果显示，所有测试的LLMs在多轮对话中表现显著下降，平均下降幅度达到39%。通过分析200,000+模拟对话，发现性能下降主要由早期假设错误和过早生成最终答案导致，揭示了LLMs在多轮对话中的不可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、虚拟助手和教育辅导等多轮对话系统。通过理解LLMs在多轮对话中的局限性，可以为未来的模型设计提供指导，提升用户交互体验和系统的实用性。随着对话系统的普及，该研究将对人机交互的未来发展产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are conversational interfaces. As such, LLMs have the potential to assist their users not only when they can fully specify the task at hand, but also to help them define, explore, and refine what they need through multi-turn conversational exchange. Although analysis of LLM conversation logs has confirmed that underspecification occurs frequently in user instructions, LLM evaluation has predominantly focused on the single-turn, fully-specified instruction setting. In this work, we perform large-scale simulation experiments to compare LLM performance in single- and multi-turn settings. Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks. Analysis of 200,000+ simulated conversations decomposes the performance degradation into two components: a minor loss in aptitude and a significant increase in unreliability. We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely. In simpler terms, we discover that *when LLMs take a wrong turn in a conversation, they get lost and do not recover*.

