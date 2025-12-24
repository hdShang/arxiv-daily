---
layout: default
title: "EvolMathEval: Towards Evolvable Benchmarks for Mathematical Reasoning via Evolutionary Testing"
---

# EvolMathEval: Towards Evolvable Benchmarks for Mathematical Reasoning via Evolutionary Testing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13003" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13003v2</a>
  <a href="https://arxiv.org/pdf/2508.13003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13003v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13003v2', 'EvolMathEval: Towards Evolvable Benchmarks for Mathematical Reasoning via Evolutionary Testing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengbo Wang, Mingwei Liu, Zike Li, Anji Li, Yanlin Wang, Xin Peng, Zibin Zheng

**分类**: cs.AI

**发布日期**: 2025-08-18 (更新: 2025-10-05)

---

## 💡 一句话要点

**提出EvolMathEval以解决数学推理基准评估的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `基准评估` `进化测试` `大型语言模型` `复杂性提升`

## 📋 核心要点

1. 现有数学推理基准随着时间推移变得越来越简单，无法准确评估LLMs的真实能力。
2. 本文提出EvolMathEval，通过进化测试自动生成和演化数学基准，提升问题难度。
3. 实验结果显示，EvolMathEval能显著提高公共数据集的复杂性，降低模型准确率48%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，现有的数学推理基准面临显著挑战。这些基准随着时间推移变得越来越简单，限制了对最先进模型真实能力的准确评估。为了解决这一问题，本文提出了EvolMathEval，一个基于进化测试的自动化数学基准生成与演化框架。实验结果表明，EvolMathEval不仅能够通过持续自我迭代生成大量高难度问题，还能显著提升公共数据集（如GSM8K）的复杂性，平均降低模型准确率48%。深入研究发现，LLMs在解决这些演化问题时，往往依赖简单模糊的条件而绕过复杂的多步骤逻辑推理，导致错误解答。我们将这一现象定义为“伪顿悟时刻”，发现其占目标问题错误的77%至100%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学推理基准在大型语言模型快速发展的背景下变得过于简单的问题。这种简单化导致无法准确评估模型的真实推理能力。

**核心思路**：EvolMathEval的核心思路是通过进化测试自动生成和演化数学问题，以持续提高问题的难度，从而挑战LLMs的推理能力。这样的设计能够确保基准的动态性和适应性。

**技术框架**：EvolMathEval的整体架构包括问题生成模块、问题演化模块和评估模块。问题生成模块负责初步生成数学问题，问题演化模块通过自我迭代提升问题的复杂性，评估模块则用于验证模型在新问题上的表现。

**关键创新**：最重要的技术创新在于引入了进化测试机制，使得基准问题能够随着时间不断演化和提升难度。这与传统静态基准方法形成鲜明对比。

**关键设计**：在技术细节上，EvolMathEval采用了特定的参数设置以控制问题的复杂性，并设计了适应性损失函数，以便更好地评估模型在演化问题上的表现。

## 📊 实验亮点

实验结果显示，EvolMathEval能够生成大量高难度问题，并显著提升公共数据集的复杂性，平均降低模型准确率48%。此外，发现LLMs在解决演化问题时，错误解答的主要原因是依赖简单模糊条件，导致复杂推理的绕过。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、智能辅导系统和自动化测试工具。通过提供更具挑战性的数学问题，EvolMathEval能够帮助教育工作者更好地评估学生的数学推理能力，并推动LLMs在教育领域的应用。未来，该框架还可能扩展到其他领域的基准生成与评估。

## 📄 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) poses a significant challenge to existing mathematical reasoning benchmarks. However, these benchmarks tend to become easier over time as LLMs can learn from the published benchmarks. This limitation hinder the precise evaluation of the true capabilities of SOTA models. To address this challenge, this paper introduces EvolMathEval, an automated mathematical benchmark generation and evolution framework based on evolutionary testing. Experimental results demonstrate that EvolMathEval can not only generate a large volume of high-difficulty problems through continuous self-iteration, but it can also significantly enhance the complexity of public datasets like GSM8K through evolution, reducing model accuracy by an average of 48\%. Deeper investigation reveals that when solving these evolved problems, LLMs tend to bypass complex multi-step logical reasoning by relying on simplistic and fuzzy conditions, consequently leading to incorrect solutions. We define this phenomenon as the ``Pseudo Aha Moment", which we find accounts for 77\% to 100\% of errors on targeted problems. Code and resources are available at: https://anonymous.4open.science/r/EvolMathEval

