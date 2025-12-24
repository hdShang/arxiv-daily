---
layout: default
title: "AbsenceBench: Language Models Can't Tell What's Missing"
---

# AbsenceBench: Language Models Can't Tell What's Missing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11440" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11440v1</a>
  <a href="https://arxiv.org/pdf/2506.11440.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11440v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11440v1', 'AbsenceBench: Language Models Can\'t Tell What\'s Missing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harvey Yiyun Fu, Aryan Shrivastava, Jared Moore, Peter West, Chenhao Tan, Ari Holtzman

**分类**: cs.CL

**发布日期**: 2025-06-13

**备注**: 23 pages, 8 figures. Code and data are publicly available at https://github.com/harvey-fin/absence-bench

---

## 💡 一句话要点

**提出AbsenceBench以评估语言模型缺失信息识别能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `缺失信息识别` `AbsenceBench` `Transformer` `自然语言处理` `信息检索` `模型评估`

## 📋 核心要点

1. 现有语言模型在识别缺失信息方面表现不佳，尤其是在处理复杂文档时。
2. 本文提出AbsenceBench，通过提供原始和编辑后的上下文，要求模型识别文档中故意删除的部分。
3. 实验结果显示，当前最先进的模型在该任务上仅达到69.6%的F1-score，揭示了模型在特定任务上的脆弱性。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理长输入和定位特定信息方面越来越强大，但在识别明显缺失的信息时仍面临挑战。本文引入AbsenceBench，评估LLMs在数值序列、诗歌和GitHub拉取请求等三个领域识别缺失信息的能力。尽管任务看似简单，实验结果显示即使是最先进的模型Claude-3.7-Sonnet在平均上下文长度为5K tokens的情况下，仅获得69.6%的F1-score。分析表明，这一低表现源于Transformer注意力机制的根本限制，无法有效关注文档中的“缺口”。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在识别文档中缺失信息的能力不足，现有方法在此类任务中表现不佳，尤其是无法有效处理信息的缺失部分。

**核心思路**：通过设计AbsenceBench，提供原始文档和编辑文档的对比，要求模型识别缺失的信息，旨在评估模型的缺失信息检测能力。

**技术框架**：AbsenceBench的整体架构包括三个主要模块：数值序列、诗歌和GitHub拉取请求。每个模块都要求模型在给定上下文的情况下，识别被删除的内容。

**关键创新**：AbsenceBench的创新之处在于其专注于缺失信息的识别，而不是信息的检索，填补了现有评估方法的空白，揭示了模型在特定任务上的局限性。

**关键设计**：在实验中，使用了Claude-3.7-Sonnet等先进模型，设置了平均上下文长度为5K tokens，采用F1-score作为性能评估指标，以量化模型的表现。

## 📊 实验亮点

实验结果显示，Claude-3.7-Sonnet在AbsenceBench任务上仅获得69.6%的F1-score，尽管在其他任务（如NIAH）中表现超人类。这一结果突显了模型在处理缺失信息时的脆弱性，揭示了Transformer注意力机制的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、信息检索和智能问答系统。通过评估和提升语言模型在缺失信息识别方面的能力，可以增强模型在实际应用中的可靠性和准确性，推动相关技术的发展与应用。未来，AbsenceBench可能成为评估语言模型能力的重要基准。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly capable of processing long inputs and locating specific information within them, as evidenced by their performance on the Needle in a Haystack (NIAH) test. However, while models excel at recalling surprising information, they still struggle to identify clearly omitted information. We introduce AbsenceBench to assesses LLMs' capacity to detect missing information across three domains: numerical sequences, poetry, and GitHub pull requests. AbsenceBench asks models to identify which pieces of a document were deliberately removed, given access to both the original and edited contexts. Despite the apparent straightforwardness of these tasks, our experiments reveal that even state-of-the-art models like Claude-3.7-Sonnet achieve only 69.6% F1-score with a modest average context length of 5K tokens. Our analysis suggests this poor performance stems from a fundamental limitation: Transformer attention mechanisms cannot easily attend to "gaps" in documents since these absences don't correspond to any specific keys that can be attended to. Overall, our results and analysis provide a case study of the close proximity of tasks where models are already superhuman (NIAH) and tasks where models breakdown unexpectedly (AbsenceBench).

