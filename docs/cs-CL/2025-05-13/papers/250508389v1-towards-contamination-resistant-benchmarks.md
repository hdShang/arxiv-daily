---
layout: default
title: Towards Contamination Resistant Benchmarks
---

# Towards Contamination Resistant Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08389" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08389v1</a>
  <a href="https://arxiv.org/pdf/2505.08389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08389v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08389v1', 'Towards Contamination Resistant Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rahmatullah Musawi, Sheng Lu

**分类**: cs.CL

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出抗污染基准以解决LLM评估可靠性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `评估方法` `抗污染基准` `凯撒密码` `自然语言处理` `模型能力`

## 📋 核心要点

1. 现有的LLM评估方法受到污染问题的严重影响，导致评估结果的可靠性下降。
2. 本文提出了一种基于凯撒密码的抗污染基准，旨在提高LLM评估的有效性。
3. 实验结果表明，当前的LLMs在面对控制污染的基准时表现不佳，揭示了其潜在的局限性。

## 📝 摘要（中文）

大型语言模型（LLMs）的快速发展改变了自然语言处理的格局。正确评估LLMs对于理解其潜力和解决安全性等问题至关重要。然而，LLM评估面临多种因素的挑战，其中污染问题尤为突出，严重影响评估的可靠性。本文引入抗污染的概念，提出了一种基于凯撒密码的基准，尽管其简单，但却是抗污染基准的优秀示例。我们在不同设置下对广泛使用的LLMs进行了测试，发现这些模型在控制污染时难以应对该基准。我们的研究揭示了当前LLMs存在的问题，并提出了关于其真实能力的重要问题。本文为抗污染基准的发展做出了贡献，使LLM评估更加严格，并提供了对LLMs真实能力和局限性的深入见解。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM评估中的污染问题，现有方法在评估过程中容易受到外部信息的干扰，导致结果不可靠。

**核心思路**：通过引入抗污染的概念，设计了一种基于凯撒密码的基准，利用其简单性和有效性来测试LLMs的真实能力。

**技术框架**：整体架构包括基准设计、模型测试和结果分析三个主要阶段。首先设计抗污染基准，然后在不同的LLMs上进行测试，最后分析模型的表现。

**关键创新**：最重要的技术创新在于提出了抗污染基准的概念，并通过凯撒密码的形式实现了这一目标，与现有评估方法相比，更加注重评估的可靠性。

**关键设计**：在实验中，设置了不同的凯撒密码偏移量，控制污染的程度，确保评估结果的有效性。

## 📊 实验亮点

实验结果显示，当前的LLMs在面对控制污染的凯撒密码基准时表现不佳，揭示了其在真实应用场景中的潜在局限性。这一发现为LLM的改进提供了重要的参考依据。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理模型的评估、模型安全性分析以及模型能力的真实测量。通过提供更可靠的评估基准，研究成果将推动LLM的进一步发展和应用，尤其是在安全性和可靠性要求较高的场景中。

## 📄 摘要（原文）

> The rapid development of large language models (LLMs) has transformed the landscape of natural language processing. Evaluating LLMs properly is crucial for understanding their potential and addressing concerns such as safety. However, LLM evaluation is confronted by various factors, among which contamination stands out as a key issue that undermines the reliability of evaluations. In this work, we introduce the concept of contamination resistance to address this challenge. We propose a benchmark based on Caesar ciphers (e.g., "ab" to "bc" when the shift is 1), which, despite its simplicity, is an excellent example of a contamination resistant benchmark. We test this benchmark on widely used LLMs under various settings, and we find that these models struggle with this benchmark when contamination is controlled. Our findings reveal issues in current LLMs and raise important questions regarding their true capabilities. Our work contributes to the development of contamination resistant benchmarks, enabling more rigorous LLM evaluation and offering insights into the true capabilities and limitations of LLMs.

