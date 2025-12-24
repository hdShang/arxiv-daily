---
layout: default
title: "IMPACT: Inflectional Morphology Probes Across Complex Typologies"
---

# IMPACT: Inflectional Morphology Probes Across Complex Typologies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23929" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23929v1</a>
  <a href="https://arxiv.org/pdf/2506.23929.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23929v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23929v1', 'IMPACT: Inflectional Morphology Probes Across Complex Typologies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammed J. Saeed, Tommi Vehvilainen, Evgeny Fedoseev, Sevil Caliskan, Tatiana Vodolazova

**分类**: cs.CL

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出IMPACT框架以评估大语言模型在形态学上的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `屈折形态学` `多语言处理` `语言评估` `模型性能`

## 📋 核心要点

1. 现有大型语言模型在多语言处理上表现良好，但对形态学复杂性的理解仍存在不足，尤其是在非英语语言中。
2. IMPACT框架通过合成生成的评估案例，专注于屈折形态学，旨在系统评估LLMs在多种语言中的表现。
3. 实验结果显示，尽管LLMs在英语上表现强劲，但在处理其他语言和不常见的形态模式时存在明显的性能下降。

## 📝 摘要（中文）

大型语言模型（LLMs）在多语言基准测试中取得了显著进展，然而它们对非英语语言的形态学复杂性理解仍不明确。为此，本文提出IMPACT，一个专注于屈折形态学的评估框架，旨在评估LLMs在阿拉伯语、俄语、芬兰语、土耳其语和希伯来语等五种形态丰富语言中的表现。IMPACT包含单元测试风格的案例，涵盖基本动词屈折和语言特有现象。我们评估了八种多语言LLMs，发现它们在处理不规则形态模式时表现不佳，尤其是在判断不合语法的例子时。我们的工作揭示了LLMs在语言复杂性处理上的不足，指出了改进的空间，并公开发布IMPACT框架以支持后续研究。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在处理形态学复杂性时的不足，尤其是在多语言环境下的表现不均衡。现有方法未能充分评估模型在不同语言的形态学能力，导致对其理解的误判。

**核心思路**：IMPACT框架通过合成生成的测试案例，专注于评估屈折形态学的表现，涵盖基本动词屈折和语言特有现象，以此来深入分析LLMs的语言理解能力。

**技术框架**：IMPACT框架包括多个模块，首先生成涵盖不同语言现象的测试案例，然后对八种多语言LLMs进行评估，最后分析模型在不同语言和形态现象下的表现差异。

**关键创新**：IMPACT的主要创新在于其合成生成的评估案例，特别是针对形态学特征的细致设计，使得评估更具针对性和有效性，填补了现有评估方法的空白。

**关键设计**：框架设计中，案例涵盖了基本的动词屈折（如时态、数、性别）及独特特征（如阿拉伯语的逆性别一致性和芬兰语的元音和谐），并采用了单元测试风格的结构以便于评估。

## 📊 实验亮点

实验结果表明，尽管评估的八种多语言LLMs在英语上表现优异，但在处理阿拉伯语、俄语、芬兰语、土耳其语和希伯来语时，尤其是在不合语法的例子上，性能显著下降。IMPACT框架揭示了这些模型在形态学处理上的不足，为后续改进提供了明确的方向。

## 🎯 应用场景

IMPACT框架的潜在应用领域包括语言模型的评估和改进，尤其是在多语言处理和形态学研究方面。该框架能够为语言学研究者和AI开发者提供有效的工具，以识别和解决模型在特定语言中的表现不足，从而推动更广泛的语言理解和生成技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown significant progress on various multilingual benchmarks and are increasingly used to generate and evaluate text in non-English languages. However, while they may produce fluent outputs, it remains unclear to what extent these models truly grasp the underlying linguistic complexity of those languages, particularly in morphology. To investigate this, we introduce IMPACT, a synthetically generated evaluation framework focused on inflectional morphology, which we publicly release, designed to evaluate LLM performance across five morphologically rich languages: Arabic, Russian, Finnish, Turkish, and Hebrew. IMPACT includes unit-test-style cases covering both shared and language-specific phenomena, from basic verb inflections (e.g., tense, number, gender) to unique features like Arabic's reverse gender agreement and vowel harmony in Finnish and Turkish. We assess eight multilingual LLMs that, despite strong English performance, struggle with other languages and uncommon morphological patterns, especially when judging ungrammatical examples. We also show that Chain of Thought and Thinking Models can degrade performance. Our work exposes gaps in LLMs' handling of linguistic complexity, pointing to clear room for improvement. To support further research, we publicly release the IMPACT framework.

