---
layout: default
title: "The SMeL Test: A simple benchmark for media literacy in language models"
---

# The SMeL Test: A simple benchmark for media literacy in language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02074" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02074v2</a>
  <a href="https://arxiv.org/pdf/2508.02074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02074v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02074v2', 'The SMeL Test: A simple benchmark for media literacy in language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gustaf Ahdritz, Anat Kleiman

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-04 (更新: 2025-08-07)

---

## 💡 一句话要点

**提出SMeL测试以评估语言模型的媒体素养能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `媒体素养` `语言模型` `信息过滤` `合成测试` `幻觉率` `基准评估` `模型评估`

## 📋 核心要点

1. 当前语言模型在过滤不可信信息方面的能力尚不明确，现有方法未能有效解决这一问题。
2. 本文提出了合成媒体素养测试（SMeL测试），旨在评估语言模型在复杂信息环境中的过滤能力。
3. 实验结果显示，所有测试的模型都未能持续成功，最佳模型的幻觉率高达70%。

## 📝 摘要（中文）

互联网充斥着未标注、故意误导或不可信的信息。尽管大型语言模型（LLMs）常被用于自主网络浏览，但它们在过滤不可信信息方面的能力尚不明确。本文提出了合成媒体素养测试（SMeL测试），这是一个简单的基准，旨在测试语言模型在上下文中主动过滤不可信信息的能力。我们对多种常用的指令调优LLMs进行了基准测试，发现没有模型能够持续成功；尽管推理能力与更高的得分相关，但即使是表现最佳的API模型也有高达70%的幻觉率。值得注意的是，较大且更强大的模型并不一定优于较小的模型。我们希望这项工作能为这一重要的幻觉形式提供更多见解，并指导新方法的开发。

## 🔬 方法详解

**问题定义**：本文旨在解决语言模型在面对不可信信息时的过滤能力不足的问题。现有方法未能有效评估和提升这一能力，导致模型在实际应用中可能产生误导性信息。

**核心思路**：论文提出的SMeL测试通过设计一系列基准任务，评估语言模型在复杂信息环境中的媒体素养能力，旨在揭示模型的局限性并推动改进。

**技术框架**：SMeL测试包括多个阶段，首先生成合成的媒体内容，然后通过不同的语言模型进行评估，最后对模型的表现进行量化分析。主要模块包括内容生成、模型评估和结果分析。

**关键创新**：SMeL测试的最大创新在于其针对媒体素养的专门设计，填补了现有评估方法的空白，能够更准确地反映模型在处理不可信信息时的表现。

**关键设计**：测试中采用了多种内容生成策略，确保生成的信息具有多样性和复杂性。同时，评估过程中设置了明确的评分标准，以量化模型的过滤能力和幻觉率。

## 📊 实验亮点

实验结果显示，所有测试的语言模型在过滤不可信信息方面均未能持续成功，最佳模型的幻觉率高达70%。尽管推理能力与得分相关，但更大的模型并不一定表现更好，这一发现为模型设计提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括教育、信息检索和社交媒体等。通过提升语言模型的媒体素养能力，可以帮助用户更有效地识别和过滤不可信信息，从而提高信息消费的质量和安全性。未来，该测试还可能推动新一代语言模型的开发，使其在复杂信息环境中表现更佳。

## 📄 摘要（原文）

> The internet is rife with unattributed, deliberately misleading, or otherwise untrustworthy content. Though large language models (LLMs) are often tasked with autonomous web browsing, the extent to which they have learned the simple heuristics human researchers use to navigate this noisy environment is not currently known. In this paper, we introduce the Synthetic Media Literacy Test (SMeL Test), a minimal benchmark that tests the ability of language models to actively filter out untrustworthy information in context. We benchmark a variety of commonly used instruction-tuned LLMs, including reasoning models, and find that no model consistently succeeds; while reasoning in particular is associated with higher scores, even the best API model we test hallucinates up to 70% of the time. Remarkably, larger and more capable models do not necessarily outperform their smaller counterparts. We hope our work sheds more light on this important form of hallucination and guides the development of new methods to combat it.

