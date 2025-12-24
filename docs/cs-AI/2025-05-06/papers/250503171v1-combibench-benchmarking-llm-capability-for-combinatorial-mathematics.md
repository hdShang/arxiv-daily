---
layout: default
title: CombiBench: Benchmarking LLM Capability for Combinatorial Mathematics
---

# CombiBench: Benchmarking LLM Capability for Combinatorial Mathematics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03171" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03171v1</a>
  <a href="https://arxiv.org/pdf/2505.03171.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03171v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03171v1', 'CombiBench: Benchmarking LLM Capability for Combinatorial Mathematics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junqi Liu, Xiaohan Lin, Jonas Bayer, Yael Dillies, Weijie Jiang, Xiaodan Liang, Roman Soletskyi, Haiming Wang, Yunzhou Xie, Beibei Xiong, Zhengfeng Yang, Jujian Zhang, Lihong Zhi, Jia Li, Zhengying Liu

**分类**: cs.AI

**发布日期**: 2025-05-06

**🔗 代码/项目**: [GITHUB](https://github.com/MoonshotAI/CombiBench/)

---

## 💡 一句话要点

**提出CombiBench以解决组合数学基准测试不足问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组合数学` `基准测试` `大型语言模型` `形式推理` `神经符号方法` `Fine-Eval` `数学竞赛` `自动化定理证明`

## 📋 核心要点

1. 组合数学缺乏适当的基准和定理库，现有方法在该领域表现不佳。
2. 提出CombiBench基准，包含100个组合问题，并引入Fine-Eval评估框架，支持填空题评估。
3. 在CombiBench上测试多种大型语言模型，Kimina-Prover在100个问题中解决了7个，表现最佳。

## 📝 摘要（中文）

神经符号方法将大型语言模型与形式推理相结合，最近在代数、几何和数论的数学竞赛问题上达到了人类水平的表现。然而，组合数学仍然是一个具有挑战性的领域，缺乏适当的基准和定理库。为了解决这一问题，本文提出了CombiBench，一个包含100个组合问题的综合基准，每个问题都在Lean~4中形式化，并配有相应的非正式陈述。问题集涵盖了从中学到国际数学奥林匹克（IMO）和大学水平的广泛难度，并涉及十个组合主题。我们还提供了一个全面的标准化评估框架Fine-Eval，首次支持填空题的评估。通过Fine-Eval评估方法，我们对多种大型语言模型进行了基准测试，发现它们在形式解决组合问题的能力上仍然有限。

## 🔬 方法详解

**问题定义**：本文旨在解决组合数学领域缺乏有效基准测试的问题，现有方法在该领域的表现普遍较弱，缺乏系统性评估。

**核心思路**：通过构建CombiBench基准，提供100个组合问题的标准化测试，并引入Fine-Eval评估框架，以支持多种类型的数学问题评估。

**技术框架**：整体架构包括问题集的构建、Lean~4形式化、非正式陈述配对以及Fine-Eval评估模块。问题集涵盖不同难度和主题，Fine-Eval则用于评估模型的解题能力。

**关键创新**：CombiBench是首个针对组合数学的综合基准，Fine-Eval框架首次支持填空题的评估，填补了现有研究的空白。

**关键设计**：在问题设计上，涵盖了从中学到大学的多种难度，Fine-Eval的设计考虑了不同类型问题的评估需求，确保评估的全面性和准确性。

## 📊 实验亮点

在CombiBench基准测试中，Kimina-Prover模型在100个组合问题中解决了7个问题，表现最佳。这一结果显示了当前大型语言模型在组合数学领域的能力仍然有限，为未来的研究提供了重要的参考。

## 🎯 应用场景

该研究的潜在应用领域包括教育、数学竞赛准备以及自动化定理证明等。CombiBench为组合数学的研究提供了标准化的评估工具，能够帮助研究人员和教育工作者更好地理解和提升大型语言模型在数学推理方面的能力，推动相关领域的发展。

## 📄 摘要（原文）

> Neurosymbolic approaches integrating large language models with formal reasoning have recently achieved human-level performance on mathematics competition problems in algebra, geometry and number theory. In comparison, combinatorics remains a challenging domain, characterized by a lack of appropriate benchmarks and theorem libraries. To address this gap, we introduce CombiBench, a comprehensive benchmark comprising 100 combinatorial problems, each formalized in Lean~4 and paired with its corresponding informal statement. The problem set covers a wide spectrum of difficulty levels, ranging from middle school to IMO and university level, and span over ten combinatorial topics. CombiBench is suitable for testing IMO solving capabilities since it includes all IMO combinatorial problems since 2000 (except IMO 2004 P3 as its statement contain an images). Furthermore, we provide a comprehensive and standardized evaluation framework, dubbed Fine-Eval (for $\textbf{F}$ill-in-the-blank $\textbf{in}$ L$\textbf{e}$an Evaluation), for formal mathematics. It accommodates not only proof-based problems but also, for the first time, the evaluation of fill-in-the-blank questions. Using Fine-Eval as the evaluation method and Kimina Lean Server as the backend, we benchmark several LLMs on CombiBench and observe that their capabilities for formally solving combinatorial problems remain limited. Among all models tested (none of which has been trained for this particular task), Kimina-Prover attains the best results, solving 7 problems (out of 100) under both ``with solution'' and ``without solution'' scenarios. We open source the benchmark dataset alongside with the code of the proposed evaluation method at https://github.com/MoonshotAI/CombiBench/.

