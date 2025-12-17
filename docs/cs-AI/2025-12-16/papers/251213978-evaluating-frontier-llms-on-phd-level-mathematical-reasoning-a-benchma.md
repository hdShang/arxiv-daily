---
layout: default
title: Evaluating Frontier LLMs on PhD-Level Mathematical Reasoning: A Benchmark on a Textbook in Theoretical Computer Science about Randomized Algorithms
---

# Evaluating Frontier LLMs on PhD-Level Mathematical Reasoning: A Benchmark on a Textbook in Theoretical Computer Science about Randomized Algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13978" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13978</a>
  <a href="https://arxiv.org/pdf/2512.13978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13978" onclick="toggleFavorite(this, '2512.13978', 'Evaluating Frontier LLMs on PhD-Level Mathematical Reasoning: A Benchmark on a Textbook in Theoretical Computer Science about Randomized Algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Cao, Yubin Chen, Xuyang Guo, Zhao Song, Song Yue, Jiahao Zhang, Jiale Zhao

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**评估前沿LLM在博士级数学推理能力：基于随机算法教材的基准测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学推理` `基准测试` `随机算法` `LaTeX证明`

## 📋 核心要点

1. 现有LLM在数学推理和科学发现中展现潜力，但缺乏在研究生水平数学理论上的严格评估。
2. 构建基于《随机算法》教材的基准测试，评估LLM生成LaTeX证明的能力，考察其数学推理水平。
3. 实验表明，Gemini和Claude等顶级模型准确率较高，但一致性存在差异，表明可靠性仍需提升。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展在自动数学推理和科学发现方面取得了显著突破。本文旨在对这些模型在规范的、研究生水平的数学理论上的推理能力进行严格评估。我们针对四种前沿模型：GPT-5-Thinking、Gemini-3-Pro、Claude-Sonnet-4.5-Thinking 和 Grok-4，构建了一个综合基准，该基准基于 Motwani 和 Raghavan 的经典教材《随机算法》。我们要求每个模型为教材中的一系列引理和练习生成正式的 LaTeX 证明。结果表明，顶级模型（Gemini 和 Claude）达到了较高的准确率（约 66%），展示了对概率方法和形式逻辑的良好掌握，而其他模型在一致性方面明显落后（约 40%）。我们对生成的证明进行了定性分析，突出了在简洁性、幻觉率和逻辑结构方面的差异。我们的结果表明，前沿模型已经达到了适合研究生水平教学辅助和形式化的熟练程度，但在严格的数学推导方面，它们的可靠性存在显著差异。代码和完整的 LLM 生成的响应已开源并公开。

## 🔬 方法详解

**问题定义**：论文旨在评估当前前沿大型语言模型（LLM）在解决博士级别数学推理问题上的能力。现有方法缺乏对LLM在研究生级别数学理论上的严格评估，无法准确衡量其数学推理的可靠性和一致性。

**核心思路**：论文的核心思路是构建一个基于经典教材《随机算法》的基准测试，通过要求LLM生成书中引理和练习的LaTeX证明，来评估其在概率方法和形式逻辑方面的掌握程度。这种方法能够更直接地考察LLM在数学理论方面的推理能力。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 选择合适的基准教材：《随机算法》；2) 选取四个前沿LLM：GPT-5-Thinking、Gemini-3-Pro、Claude-Sonnet-4.5-Thinking 和 Grok-4；3) 要求LLM为教材中的一系列引理和练习生成LaTeX证明；4) 对生成的证明进行定量和定性分析，包括准确率、一致性、简洁性、幻觉率和逻辑结构等方面。

**关键创新**：该研究的关键创新在于构建了一个专门针对博士级别数学推理的基准测试，并使用LaTeX格式的证明作为评估标准。这种方法能够更准确地评估LLM在数学理论方面的推理能力，并为未来的研究提供了一个可靠的评估工具。

**关键设计**：论文的关键设计包括：1) 选择《随机算法》作为基准教材，因为它涵盖了概率方法和形式逻辑等重要的数学概念；2) 使用LaTeX格式的证明作为评估标准，因为它能够更准确地反映LLM的数学推理能力；3) 对生成的证明进行定量和定性分析，以全面评估LLM的性能。

## 📊 实验亮点

实验结果表明，Gemini和Claude等顶级模型在准确率方面表现出色，达到了约66%，展示了对概率方法和形式逻辑的良好掌握。然而，其他模型在一致性方面表现较差，仅为约40%。这表明，尽管前沿模型在数学推理方面取得了进展，但在可靠性方面仍有提升空间。定性分析表明，不同模型在简洁性、幻觉率和逻辑结构方面存在差异。

## 🎯 应用场景

该研究成果可应用于开发研究生级别的数学教学辅助工具，帮助学生理解和掌握复杂的数学概念。此外，该基准测试可用于评估和改进LLM的数学推理能力，推动其在科学发现和自动化数学证明等领域的应用。未来，该研究可扩展到其他数学领域，构建更全面的数学推理评估体系。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has led to significant breakthroughs in automated mathematical reasoning and scientific discovery. Georgiev, G${ó}$mez-Serrano, Tao, and Wagner [GGSTW+25] demonstrate that AI systems can explore new constructions and improve existing bounds, illustrating the growing potential of LLMs to accelerate mathematical discovery. Similarly, Bubeck et al. [BCE+25] show that GPT-5 can meaningfully contribute to scientific workflows, from proposing hypotheses to generating proofs and analyses. Despite these advances, a rigorous evaluation of these models on canonical, graduate-level mathematical theory remains necessary to understand their baseline reasoning capabilities. In this paper, we present a comprehensive benchmark of four frontier models: GPT-5-Thinking, Gemini-3-Pro, Claude-Sonnet-4.5-Thinking, and Grok-4 against the classic curriculum of Randomized Algorithms by Motwani and Raghavan [MR95].We tasked each model with generating formal LaTeX proofs for a series of lemmas and exercises spanning the textbook. We find that while the top-tier models (Gemini, and Claude) achieve a high accuracy rate (approx. 66%), demonstrating a robust grasp of probabilistic method and formal logic, other models lag significantly in consistency (approx. 40%). We provide a qualitative analysis of the generated proofs, highlighting differences in conciseness, hallucination rates, and logical structure. Our results suggest that while frontier models have reached a threshold of proficiency suitable for graduate-level pedagogical assistance and formalization, significant variance exists in their reliability for rigorous mathematical derivation. The code and the full set of LLM-generated responses are open-sourced and publicly available atthis https URL.

