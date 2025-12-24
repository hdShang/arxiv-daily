---
layout: default
title: "OJBench: A Competition Level Code Benchmark For Large Language Models"
---

# OJBench: A Competition Level Code Benchmark For Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16395" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16395v1</a>
  <a href="https://arxiv.org/pdf/2506.16395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16395v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16395v1', 'OJBench: A Competition Level Code Benchmark For Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhexu Wang, Yiping Liu, Yejie Wang, Wenyang He, Bofei Gao, Muxi Diao, Yanxu Chen, Kelin Fu, Flood Sung, Zhilin Yang, Tianyu Liu, Weiran Xu

**分类**: cs.CL

**发布日期**: 2025-06-19

**备注**: 9 pages, 5 figures

---

## 💡 一句话要点

**提出OJBench以评估大型语言模型的代码推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码推理` `OJBench` `编程竞赛` `模型评估` `人工智能`

## 📋 核心要点

1. 现有的代码基准测试无法全面评估大型语言模型在竞争级别的代码推理能力，存在明显的局限性。
2. OJBench是一个新提出的基准，专门设计用于评估LLMs在编程竞赛中的推理能力，包含232个竞赛问题。
3. 对37个模型的评估结果显示，当前最先进的推理导向模型在解决高难度竞赛问题时仍面临显著挑战。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在数学和代码推理能力方面取得了显著进展。然而，现有的代码基准测试在评估这些能力的全面性，尤其是在竞争级别方面存在局限。为了解决这一问题，本文提出了OJBench，一个旨在评估LLMs竞争级别代码推理能力的新基准。OJBench包含来自NOI和ICPC的232个编程竞赛问题，为模型的推理能力提供了更严格的测试。我们对37个模型进行了全面评估，包括封闭源和开放源模型，推理导向和非推理导向模型。结果表明，即使是最先进的推理导向模型，如o4-mini和Gemini-2.5-pro-exp，在面对高度挑战的竞赛级别问题时也表现不佳，这突显了模型在竞争级别代码推理中面临的重大挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决现有代码基准测试无法有效评估大型语言模型在竞争级别代码推理能力的问题，现有方法在测试深度和广度上存在不足。

**核心思路**：OJBench通过引入232个编程竞赛问题，提供了一个更具挑战性的测试环境，旨在全面评估模型的推理能力，尤其是在复杂问题上的表现。

**技术框架**：OJBench的整体架构包括问题选择、模型评估和结果分析三个主要模块。问题选择从NOI和ICPC中提取，模型评估则涵盖了多种类型的语言模型，最后通过对比分析得出结论。

**关键创新**：OJBench的最大创新在于其针对竞争级别的设计，填补了现有基准测试在评估深度和广度上的空白，特别是在高难度问题的选择上。

**关键设计**：在设计OJBench时，选择了具有挑战性的编程问题，并确保覆盖不同类型的推理能力，评估过程中采用了多种模型进行对比，确保结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，尽管使用了最先进的推理导向模型，如o4-mini和Gemini-2.5-pro-exp，但在解决OJBench中的高难度竞赛问题时，这些模型的表现仍然不尽如人意，表明当前技术在竞争级别代码推理方面仍存在显著挑战。

## 🎯 应用场景

OJBench的提出为大型语言模型的评估提供了一个新的标准，特别是在编程和算法领域。其潜在应用包括教育、自动化编程助手和代码审查工具等，能够帮助开发者和研究人员更好地理解和提升模型的推理能力，推动人工智能在编程领域的应用和发展。

## 📄 摘要（原文）

> Recent advancements in large language models (LLMs) have demonstrated significant progress in math and code reasoning capabilities. However, existing code benchmark are limited in their ability to evaluate the full spectrum of these capabilities, particularly at the competitive level. To bridge this gap, we introduce OJBench, a novel and challenging benchmark designed to assess the competitive-level code reasoning abilities of LLMs. OJBench comprises 232 programming competition problems from NOI and ICPC, providing a more rigorous test of models' reasoning skills. We conducted a comprehensive evaluation using OJBench on 37 models, including both closed-source and open-source models, reasoning-oriented and non-reasoning-oriented models. Our results indicate that even state-of-the-art reasoning-oriented models, such as o4-mini and Gemini-2.5-pro-exp, struggle with highly challenging competition-level problems. This highlights the significant challenges that models face in competitive-level code reasoning.

