---
layout: default
title: "From Monolingual to Bilingual: Investigating Language Conditioning in Large Language Models for Psycholinguistic Tasks"
---

# From Monolingual to Bilingual: Investigating Language Conditioning in Large Language Models for Psycholinguistic Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02502" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02502v1</a>
  <a href="https://arxiv.org/pdf/2508.02502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02502v1', 'From Monolingual to Bilingual: Investigating Language Conditioning in Large Language Models for Psycholinguistic Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuzhou Yuan, Zhan Qu, Mario Tawfelis, Michael Färber

**分类**: cs.CL

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**研究语言条件对大型语言模型心理语言学任务的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心理语言学` `语言身份` `跨语言认知` `声音象征` `词汇效价` `多语言处理`

## 📋 核心要点

1. 现有研究对大型语言模型在跨语言心理语言学反应中的表现了解不足，尤其是在不同语言身份下的表现。
2. 本文通过声音象征和词汇效价任务，探讨LLMs如何在单语和双语提示下调整其输出，揭示语言身份的影响。
3. 实验结果显示，Qwen模型在荷兰语和中文之间的区分能力更强，且中文提示的效价表示更为稳定，提供了新的认知模型视角。

## 📝 摘要（中文）

大型语言模型（LLMs）展现出强大的语言能力，但关于它们如何跨语言编码心理语言学知识的研究仍然较少。本文探讨了LLMs在不同语言身份下是否以及如何表现出类似人类的心理语言学反应，使用了声音象征和词汇效价两个任务。我们评估了Llama-3.3-70B-Instruct和Qwen2.5-72B-Instruct模型在英语、荷兰语和中文的单语和双语提示下的表现。结果表明，两种模型的输出会根据提示的语言身份进行调整，其中Qwen在荷兰语和中文之间的区分更为敏感。探测分析显示，心理语言学信号在更深层次中变得更易解码，中文提示的效价表示比荷兰语更强且更稳定。我们的研究揭示了语言身份如何影响LLMs的输出行为和内部表征，为其作为跨语言认知模型的应用提供了新见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在不同语言身份下的心理语言学反应表现不明确的问题，现有方法未能充分探讨语言身份对模型输出的影响。

**核心思路**：通过对比分析两种大型语言模型在单语和双语提示下的表现，研究语言身份如何影响模型的输出行为和内部表征。

**技术框架**：研究采用声音象征和词汇效价两个任务，评估Llama-3.3-70B-Instruct和Qwen2.5-72B-Instruct模型在英语、荷兰语和中文的表现，分析其输出的语言身份调整。

**关键创新**：本研究的创新点在于揭示了语言身份对LLMs输出行为和内部表示的条件作用，提供了跨语言认知的新视角。

**关键设计**：实验中使用了不同语言的提示，分析了模型在不同层次的心理语言学信号解码能力，特别关注中文提示的效价表示的稳定性和强度。

## 📊 实验亮点

实验结果显示，Qwen模型在荷兰语和中文之间的区分能力显著优于Llama模型，且在中文提示下的效价表示比荷兰语更强，表现出更高的稳定性。这一发现为理解LLMs的跨语言认知提供了重要数据支持。

## 🎯 应用场景

该研究的潜在应用领域包括跨语言教育、翻译系统和多语言对话系统等。通过深入理解语言身份对模型行为的影响，可以提升这些系统的语言适应性和用户体验，推动智能助手和教育工具的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) exhibit strong linguistic capabilities, but little is known about how they encode psycholinguistic knowledge across languages. We investigate whether and how LLMs exhibit human-like psycholinguistic responses under different linguistic identities using two tasks: sound symbolism and word valence. We evaluate two models, Llama-3.3-70B-Instruct and Qwen2.5-72B-Instruct, under monolingual and bilingual prompting in English, Dutch, and Chinese. Behaviorally, both models adjust their outputs based on prompted language identity, with Qwen showing greater sensitivity and sharper distinctions between Dutch and Chinese. Probing analysis reveals that psycholinguistic signals become more decodable in deeper layers, with Chinese prompts yielding stronger and more stable valence representations than Dutch. Our results demonstrate that language identity conditions both output behavior and internal representations in LLMs, providing new insights into their application as models of cross-linguistic cognition.

