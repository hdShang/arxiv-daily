---
layout: default
title: "Digging Into the Internal: Causality-Based Analysis of LLM Function Calling"
---

# Digging Into the Internal: Causality-Based Analysis of LLM Function Calling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16268" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16268v1</a>
  <a href="https://arxiv.org/pdf/2509.16268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16268v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16268v1', 'Digging Into the Internal: Causality-Based Analysis of LLM Function Calling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenlan Ji, Daoyuan Wu, Wenxuan Wang, Pingchuan Ma, Shuai Wang, Lei Ma

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**基于因果分析的大语言模型函数调用机制研究，显著提升LLM安全性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `函数调用` `因果分析` `安全鲁棒性` `恶意输入检测`

## 📋 核心要点

1. 当前对函数调用如何影响LLM内部行为的机制理解不足，限制了其更广泛的应用。
2. 利用因果分析方法，通过层级和token级的干预，深入剖析函数调用对LLM计算逻辑的影响。
3. 实验表明，函数调用在提高LLM安全鲁棒性方面表现出色，恶意输入检测性能平均提升135%。

## 📝 摘要（中文）

函数调用(FC)已成为一种强大的技术，能够促进大型语言模型(LLM)与外部系统交互并执行结构化任务。然而，它影响模型行为的机制在很大程度上仍未被充分探索。此外，我们发现除了FC的常规用法外，该技术还可以显著提高LLM对用户指令的依从性。这些观察促使我们利用因果关系这一经典分析方法来研究FC在LLM内部的工作原理。特别地，我们进行了层级和token级的因果干预，以剖析FC在响应用户查询时对模型内部计算逻辑的影响。我们的分析证实了FC的巨大影响，并揭示了对其机制的几个深入见解。为了进一步验证我们的发现，我们进行了广泛的实验，比较了基于FC的指令与传统提示方法的有效性。我们专注于增强LLM安全鲁棒性这一关键的LLM应用场景，并在两个基准数据集上评估了四个主流LLM。结果非常显著：在检测恶意输入方面，FC显示出比传统提示方法平均约135%的性能提升，证明了其在提高LLM在实际应用中的可靠性和能力方面的巨大潜力。

## 🔬 方法详解

**问题定义**：论文旨在深入理解函数调用（Function Calling, FC）技术如何影响大型语言模型（LLM）的内部运作机制，特别是在响应用户查询时。现有方法缺乏对FC在LLM内部计算逻辑中作用的细粒度分析，导致无法充分发挥FC的潜力，尤其是在安全性和可靠性至关重要的应用场景中。

**核心思路**：论文的核心思路是利用因果分析方法，通过对LLM内部状态进行干预，观察FC对模型行为的影响。通过这种方式，可以揭示FC在不同层级和token级别上的作用，从而更深入地理解其工作原理。这种因果分析方法能够克服传统黑盒分析的局限性，提供更具解释性的结果。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 设计实验，使用户查询包含或不包含函数调用；2) 对LLM的不同层级和token进行因果干预，例如，改变特定层级的激活值或屏蔽某些token；3) 观察干预后LLM的输出变化，并分析这些变化与FC之间的因果关系；4) 通过对比实验，验证FC在提高LLM安全鲁棒性方面的有效性。

**关键创新**：论文最重要的技术创新点在于将因果分析方法应用于研究LLM的函数调用机制。与传统的黑盒分析方法相比，因果分析能够更清晰地揭示FC对LLM内部计算逻辑的影响，从而为优化FC的使用提供更可靠的依据。此外，论文还发现FC不仅可以用于与外部系统交互，还可以显著提高LLM对用户指令的依从性。

**关键设计**：论文的关键设计包括：1) 选择合适的因果干预方法，例如，使用Do-calculus进行因果推断；2) 设计细粒度的干预策略，例如，在不同的层级和token级别进行干预；3) 使用合适的评估指标，例如，准确率、召回率和F1值，来衡量LLM的安全鲁棒性；4) 选择具有代表性的LLM和数据集进行实验，以确保结果的泛化能力。

## 📊 实验亮点

实验结果表明，基于函数调用的指令在检测恶意输入方面，比传统提示方法平均提升了约135%。这一显著的性能提升表明，函数调用在提高LLM安全鲁棒性方面具有巨大的潜力。该研究在四个主流LLM和两个基准数据集上进行了验证，结果具有较强的说服力。

## 🎯 应用场景

该研究成果可应用于提升大语言模型在各种实际场景中的安全性和可靠性，例如：恶意代码检测、虚假信息识别、有害内容过滤等。通过优化函数调用机制，可以使LLM更好地理解用户意图，并避免产生不安全或不适当的输出。此外，该研究还可以为开发更安全、更可靠的LLM提供理论指导。

## 📄 摘要（原文）

> Function calling (FC) has emerged as a powerful technique for facilitating large language models (LLMs) to interact with external systems and perform structured tasks. However, the mechanisms through which it influences model behavior remain largely under-explored. Besides, we discover that in addition to the regular usage of FC, this technique can substantially enhance the compliance of LLMs with user instructions. These observations motivate us to leverage causality, a canonical analysis method, to investigate how FC works within LLMs. In particular, we conduct layer-level and token-level causal interventions to dissect FC's impact on the model's internal computational logic when responding to user queries. Our analysis confirms the substantial influence of FC and reveals several in-depth insights into its mechanisms. To further validate our findings, we conduct extensive experiments comparing the effectiveness of FC-based instructions against conventional prompting methods. We focus on enhancing LLM safety robustness, a critical LLM application scenario, and evaluate four mainstream LLMs across two benchmark datasets. The results are striking: FC shows an average performance improvement of around 135% over conventional prompting methods in detecting malicious inputs, demonstrating its promising potential to enhance LLM reliability and capability in practical applications.

