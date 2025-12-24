---
layout: default
title: "MobileRAG: Enhancing Mobile Agent with Retrieval-Augmented Generation"
---

# MobileRAG: Enhancing Mobile Agent with Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03891" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03891v1</a>
  <a href="https://arxiv.org/pdf/2509.03891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03891v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03891v1', 'MobileRAG: Enhancing Mobile Agent with Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gowen Loo, Chang Liu, Qinghong Yin, Xiang Chen, Jiawei Chen, Jingyuan Zhang, Yu Tian

**分类**: cs.CL, cs.CV

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/liuxiaojieOutOfWorld/MobileRAG_arxiv)

---

## 💡 一句话要点

**MobileRAG：通过检索增强生成提升移动代理性能，解决任务错误、环境交互和记忆缺失问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动代理` `检索增强生成` `大型语言模型` `人机交互` `知识检索` `移动应用` `任务自动化`

## 📋 核心要点

1. 现有移动代理依赖LLM理解能力，易因误操作出错，缺乏环境交互，且无记忆，无法从错误中学习。
2. MobileRAG框架利用检索增强生成（RAG），包含InterRAG、LocalRAG和MemRAG，提升查询识别和任务完成的准确性。
3. MobileRAG-Eval基准测试表明，MobileRAG能有效处理真实移动任务，性能超越现有方法，操作步骤更少，提升10.3%。

## 📝 摘要（中文）

智能手机已成为人们日常生活中不可或缺的一部分。随着大型语言模型（LLM）的不断发展，涌现出大量基于LLM的移动代理。这些代理能够准确解析各种用户查询，并自动协助用户完成复杂或重复的操作。然而，当前的代理1）严重依赖LLM的理解能力，这可能导致任务执行过程中因误操作或遗漏步骤而产生错误；2）缺乏与外部环境的交互，常常在应用程序无法满足用户查询时终止任务；3）缺乏记忆能力，需要每次指令都重建界面，并且无法从先前的错误中学习和纠正。为了缓解上述问题，我们提出了MobileRAG，这是一个由检索增强生成（RAG）增强的移动代理框架，包括InterRAG、LocalRAG和MemRAG。它利用RAG来更快、更准确地识别用户查询并完成复杂和长序列的移动任务。此外，为了更全面地评估MobileRAG的性能，我们引入了MobileRAG-Eval，这是一个更具挑战性的基准，其特点是需要外部知识辅助的大量复杂、真实的移动任务。在MobileRAG-Eval上的大量实验结果表明，MobileRAG可以轻松处理真实的移动任务，与最先进的方法相比，以更少的操作步骤实现了10.3%的改进。我们的代码已公开发布在：https://github.com/liuxiaojieOutOfWorld/MobileRAG_arxiv

## 🔬 方法详解

**问题定义**：现有基于LLM的移动代理在处理复杂移动任务时存在三个主要痛点：一是过度依赖LLM的理解能力，容易因误操作或步骤遗漏导致任务失败；二是缺乏与外部环境的有效交互，当应用无法直接满足用户需求时，任务容易中断；三是缺乏记忆能力，无法从历史错误中学习和改进，每次都需要重新构建界面。

**核心思路**：MobileRAG的核心思路是通过引入检索增强生成（RAG）机制，为移动代理提供更强的知识获取和推理能力。具体来说，它利用RAG从外部知识库中检索相关信息，辅助LLM理解用户意图，从而减少误操作，并能更好地处理需要外部知识的任务。同时，通过记忆模块，使代理能够记住之前的操作和错误，从而在后续任务中避免重复犯错。

**技术框架**：MobileRAG框架包含三个主要模块：InterRAG、LocalRAG和MemRAG。InterRAG负责与外部环境交互，检索相关信息以辅助任务完成。LocalRAG用于从本地知识库中检索信息，例如应用程序的文档或用户历史操作记录。MemRAG则负责维护代理的记忆，记录之前的操作和错误，以便在后续任务中进行纠正和改进。整个流程是，用户发起任务，代理首先利用RAG检索相关信息，然后根据检索结果生成操作指令，执行操作，并将操作过程和结果记录在记忆中，以便后续任务参考。

**关键创新**：MobileRAG的关键创新在于将RAG机制引入到移动代理中，从而显著提升了代理的知识获取和推理能力。与传统的移动代理相比，MobileRAG不再仅仅依赖LLM自身的知识，而是能够通过检索外部知识来辅助任务完成，从而减少了误操作和任务失败的风险。此外，记忆模块的引入也使得代理能够从历史经验中学习，从而不断提升自身的性能。

**关键设计**：在InterRAG中，关键设计在于如何有效地从外部知识库中检索相关信息。这可能涉及到使用特定的检索算法，例如基于向量相似度的检索。在LocalRAG中，关键设计在于如何构建和维护本地知识库，例如应用程序的文档和用户历史操作记录。在MemRAG中，关键设计在于如何有效地存储和检索记忆，例如使用特定的数据结构和索引方法。

## 📊 实验亮点

实验结果表明，MobileRAG在MobileRAG-Eval基准测试中取得了显著的性能提升，与最先进的方法相比，以更少的操作步骤实现了10.3%的改进。这表明MobileRAG能够更有效地处理真实的移动任务，并且具有更强的鲁棒性和可靠性。实验还验证了InterRAG、LocalRAG和MemRAG三个模块的有效性，证明了RAG机制在移动代理中的应用价值。

## 🎯 应用场景

MobileRAG具有广泛的应用前景，可用于开发更智能、更可靠的移动助手，帮助用户自动完成各种复杂任务，例如预订机票、管理日程、处理邮件等。它还可以应用于智能家居、智能车载等领域，实现更智能的人机交互。该研究的实际价值在于提升了移动代理的可用性和用户体验，未来有望推动移动代理的普及和应用。

## 📄 摘要（原文）

> Smartphones have become indispensable in people's daily lives, permeating nearly every aspect of modern society. With the continuous advancement of large language models (LLMs), numerous LLM-based mobile agents have emerged. These agents are capable of accurately parsing diverse user queries and automatically assisting users in completing complex or repetitive operations. However, current agents 1) heavily rely on the comprehension ability of LLMs, which can lead to errors caused by misoperations or omitted steps during tasks, 2) lack interaction with the external environment, often terminating tasks when an app cannot fulfill user queries, and 3) lack memory capabilities, requiring each instruction to reconstruct the interface and being unable to learn from and correct previous mistakes. To alleviate the above issues, we propose MobileRAG, a mobile agents framework enhanced by Retrieval-Augmented Generation (RAG), which includes InterRAG, LocalRAG, and MemRAG. It leverages RAG to more quickly and accurately identify user queries and accomplish complex and long-sequence mobile tasks. Additionally, to more comprehensively assess the performance of MobileRAG, we introduce MobileRAG-Eval, a more challenging benchmark characterized by numerous complex, real-world mobile tasks that require external knowledge assistance. Extensive experimental results on MobileRAG-Eval demonstrate that MobileRAG can easily handle real-world mobile tasks, achieving 10.3\% improvement over state-of-the-art methods with fewer operational steps. Our code is publicly available at: https://github.com/liuxiaojieOutOfWorld/MobileRAG_arxiv

