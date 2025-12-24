---
layout: default
title: "Search Arena: Analyzing Search-Augmented LLMs"
---

# Search Arena: Analyzing Search-Augmented LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05334" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05334v1</a>
  <a href="https://arxiv.org/pdf/2506.05334.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05334v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05334v1', 'Search Arena: Analyzing Search-Augmented LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mihran Miroyan, Tsung-Han Wu, Logan King, Tianle Li, Jiayi Pan, Xinyan Hu, Wei-Lin Chiang, Anastasios N. Angelopoulos, Trevor Darrell, Narges Norouzi, Joseph E. Gonzalez

**分类**: cs.CL, cs.IR, cs.LG

**发布日期**: 2025-06-05

**备注**: Preprint. Code: https://github.com/lmarena/search-arena. Dataset: https://huggingface.co/datasets/lmarena-ai/search-arena-24k

**🔗 代码/项目**: [GITHUB](https://github.com/lmarena/search-arena)

---

## 💡 一句话要点

**提出Search Arena以分析搜索增强型大语言模型的用户偏好**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `搜索增强型模型` `大语言模型` `用户偏好分析` `众包数据集` `自然语言处理` `信息检索` `多轮交互`

## 📋 核心要点

1. 现有的搜索增强型语言模型分析面临数据集规模小、范围窄等挑战，限制了对其性能的全面理解。
2. 本文提出了Search Arena，一个包含24,000对多轮用户交互的众包数据集，以便更好地分析用户偏好。
3. 实验结果表明，搜索增强型LLMs在非搜索环境中表现良好，但在搜索环境中仅依赖模型的参数知识会显著影响质量。

## 📝 摘要（中文）

搜索增强型语言模型结合了网络搜索与大语言模型（LLMs），以提高响应的基础性和新鲜度。然而，分析这些系统仍然具有挑战性：现有数据集在规模和范围上都有限，通常局限于静态的、单轮的事实核查问题。本文介绍了Search Arena，这是一个众包的大规模人类偏好数据集，包含超过24,000对多轮用户与搜索增强型LLMs的交互。数据集涵盖多种意图和语言，并包含约12,000个用户偏好投票的完整系统跟踪。我们的分析揭示，用户偏好受到引用数量的影响，即使被引用的内容并不直接支持所归属的主张，揭示了感知与实际可信度之间的差距。此外，用户偏好在引用来源之间存在差异，表明社区驱动的平台通常更受欢迎，而静态的百科全书来源并不总是合适和可靠。我们开源了该数据集，以支持未来在这一方向的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有搜索增强型语言模型分析中数据集规模小、范围窄的问题，限制了对用户偏好的深入理解。

**核心思路**：通过构建一个大规模的众包数据集Search Arena，收集多轮用户交互数据，以全面分析用户在使用搜索增强型LLMs时的偏好和行为。

**技术框架**：数据集包含超过24,000对用户交互，涵盖多种意图和语言，记录了完整的系统跟踪和用户偏好投票。分析过程中，比较了搜索增强型LLMs与传统LLMs在不同环境下的表现。

**关键创新**：最重要的创新在于引入了一个大规模的多轮交互数据集，填补了现有研究中对用户偏好分析的空白，特别是在搜索增强型LLMs的应用场景中。

**关键设计**：数据集设计中考虑了多种用户意图和语言，确保了数据的多样性和代表性，同时记录了用户的偏好投票，以便后续分析。

## 📊 实验亮点

实验结果显示，在非搜索环境中，搜索增强型LLMs的性能未受损，甚至有所提升；而在搜索环境中，若仅依赖模型的参数知识，质量显著下降。这一发现强调了在不同应用场景下选择合适模型的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能助手和信息检索等。通过深入理解用户偏好，开发者可以优化搜索增强型LLMs的设计，提高用户体验和系统的响应质量，未来可能推动更智能的对话系统和信息获取工具的进步。

## 📄 摘要（原文）

> Search-augmented language models combine web search with Large Language Models (LLMs) to improve response groundedness and freshness. However, analyzing these systems remains challenging: existing datasets are limited in scale and narrow in scope, often constrained to static, single-turn, fact-checking questions. In this work, we introduce Search Arena, a crowd-sourced, large-scale, human-preference dataset of over 24,000 paired multi-turn user interactions with search-augmented LLMs. The dataset spans diverse intents and languages, and contains full system traces with around 12,000 human preference votes. Our analysis reveals that user preferences are influenced by the number of citations, even when the cited content does not directly support the attributed claims, uncovering a gap between perceived and actual credibility. Furthermore, user preferences vary across cited sources, revealing that community-driven platforms are generally preferred and static encyclopedic sources are not always appropriate and reliable. To assess performance across different settings, we conduct cross-arena analyses by testing search-augmented LLMs in a general-purpose chat environment and conventional LLMs in search-intensive settings. We find that web search does not degrade and may even improve performance in non-search settings; however, the quality in search settings is significantly affected if solely relying on the model's parametric knowledge. We open-sourced the dataset to support future research in this direction. Our dataset and code are available at: https://github.com/lmarena/search-arena.

