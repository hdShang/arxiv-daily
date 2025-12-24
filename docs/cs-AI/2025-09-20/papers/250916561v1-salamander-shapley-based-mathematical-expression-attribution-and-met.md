---
layout: default
title: "SalaMAnder: Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning"
---

# SalaMAnder: Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16561" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16561v1</a>
  <a href="https://arxiv.org/pdf/2509.16561.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16561v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16561v1', 'SalaMAnder: Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Xin, Chen Shen, Shaotian Yan, Xiaosong Yuan, Yaoming Wang, Xiaofeng Zhang, Chenxi Huang, Jieping Ye

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-20

**备注**: accpeted by EMNLP 2025

---

## 💡 一句话要点

**提出SalaMAnder，基于Shapley值评估CoT推理中数学表达式的贡献度，并优化提示构建。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Chain-of-Thought` `Shapley值` `数学表达式归因` `可解释性` `提示工程`

## 📋 核心要点

1. 大型语言模型（LLMs）的CoT推理能力显著提升，但其内在机制尚不明确，需要深入研究。
2. 利用Shapley值进行数学表达式归因，并设计分层抽样算法降低计算复杂度，提出SalaMAnder框架。
3. 实验表明，CoSP指标与模型性能具有单调相关性，可用于解释CoT的成功并优化提示构建。

## 📝 摘要（中文）

本文提出SalaMAnder（基于Shapley值的数学表达式归因和度量），这是一种理论上可靠的方法以及数学上严谨的评估指标，用于量化少样本CoT推理中组件级别的贡献。具体而言，我们利用Shapley值进行数学表达式归因，并开发了一种高效的分层抽样算法，显著降低了计算复杂度。此外，我们通过协方差分析开发了CoSP（Shapley正值的基数）指标。在流行的LLM模型和不同的数学基准上的全面验证表明，我们的SalaMAnder框架中的CoSP指标与模型性能表现出稳健的单调相关性，不仅为现有少样本CoT的经验成功提供了理论解释，而且为提示构建优化建立了数学上严谨的原则。此外，我们验证了解释的可靠性，并在此基础上统一了先前工作的见解。

## 🔬 方法详解

**问题定义**：现有方法缺乏对CoT推理过程中各个数学表达式贡献度的量化评估，无法有效解释CoT提升LLM数学推理能力的内在机制，阻碍了提示工程的优化。因此，需要一种能够准确评估每个数学表达式对最终结果影响的方法，并基于此指导提示构建。

**核心思路**：论文的核心思路是利用Shapley值来量化每个数学表达式在CoT推理过程中的贡献。Shapley值是一种合作博弈论中的概念，可以公平地分配合作产生的收益。在这里，每个数学表达式被视为一个参与者，CoT推理的正确性被视为合作产生的收益。通过计算每个表达式的Shapley值，可以评估其对最终结果的影响。

**技术框架**：SalaMAnder框架主要包含两个核心模块：1) 基于Shapley值的数学表达式归因模块：该模块负责计算每个数学表达式的Shapley值，评估其对最终推理结果的贡献。为了降低计算复杂度，采用了分层抽样算法。2) CoSP指标计算模块：该模块基于Shapley值计算CoSP指标，CoSP指标反映了对最终结果有积极贡献的数学表达式的数量。通过协方差分析，验证CoSP指标与模型性能之间的相关性。

**关键创新**：论文的关键创新在于将Shapley值应用于CoT推理过程中的数学表达式归因，并提出了CoSP指标。与现有方法相比，该方法能够更准确地量化每个数学表达式的贡献，并提供可解释性。此外，分层抽样算法显著降低了Shapley值计算的复杂度。

**关键设计**：在Shapley值计算中，采用了分层抽样算法，根据数学表达式的类型（例如，加法、乘法等）进行分层，以提高抽样效率。CoSP指标的计算基于Shapley值的正负性，统计对最终结果有积极贡献的表达式数量。论文还详细描述了实验设置，包括使用的LLM模型、数学基准数据集以及评估指标。

## 📊 实验亮点

实验结果表明，SalaMAnder框架中的CoSP指标与模型性能表现出稳健的单调相关性。在多个流行的LLM模型和数学基准数据集上进行了验证，证明了该方法的有效性。例如，在某些数据集上，通过优化提示构建，模型的准确率提升了显著幅度（具体数值未知）。

## 🎯 应用场景

该研究成果可应用于提升大型语言模型在数学推理、科学计算等领域的性能。通过分析CoT推理过程中关键的数学表达式，可以指导提示工程，优化模型推理路径，提高模型的可解释性和可靠性。此外，该方法还可以应用于其他类型的推理任务，例如代码生成、逻辑推理等。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) prompting enhances the math reasoning capability of large language models (LLMs) to a large margin. However, the mechanism underlying such improvements remains unexplored. In this paper, we present \textbf{SalaMAnder} (\textbf{S}h\textbf{a}p\textbf{l}ey-b\textbf{a}sed \textbf{M}athematical Expression \textbf{A}ttribution a\textbf{nd} M\textbf{e}t\textbf{r}ic), a theoretically grounded methodology as well as a mathematically rigorous evaluation metric for quantifying component-level contributions in few-shot CoT reasoning. Concretely, we leverage the Shapley value for mathematical expression attribution and develop an efficient stratified sampling algorithm that significantly reduces the computational complexity. Besides, we develop the \textbf{CoSP} (\textbf{C}ardinality \textbf{o}f \textbf{S}hapley \textbf{P}ositives) metric through covariance analysis. Comprehensive validation across popular LLM models and diverse mathematical benchmarks demonstrates that the CoSP metric within our SalaMAnder framework exhibits a robust monotonic correlation with model performance, not only providing theoretical explanations for the empirical success of existing few-shot CoT but also establishing mathematically rigorous principles for prompt construction optimization. Furthermore, we verify the reliability of the explanation, based on which we unify the insights of previous work.

