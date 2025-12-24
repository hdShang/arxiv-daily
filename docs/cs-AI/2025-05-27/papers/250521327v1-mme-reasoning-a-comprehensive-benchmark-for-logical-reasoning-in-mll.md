---
layout: default
title: "MME-Reasoning: A Comprehensive Benchmark for Logical Reasoning in MLLMs"
---

# MME-Reasoning: A Comprehensive Benchmark for Logical Reasoning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21327" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21327v1</a>
  <a href="https://arxiv.org/pdf/2505.21327.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21327v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21327v1', 'MME-Reasoning: A Comprehensive Benchmark for Logical Reasoning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiakang Yuan, Tianshuo Peng, Yilei Jiang, Yiting Lu, Renrui Zhang, Kaituo Feng, Chaoyou Fu, Tao Chen, Lei Bai, Bo Zhang, Xiangyu Yue

**分类**: cs.AI, cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出MME-Reasoning以解决多模态大语言模型逻辑推理评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `多模态大语言模型` `评估基准` `归纳推理` `演绎推理` `溯因推理` `人工智能`

## 📋 核心要点

1. 现有的多模态大语言模型在逻辑推理能力评估上存在不足，缺乏对推理类型的明确分类。
2. 论文提出MME-Reasoning基准，全面评估MLLMs的逻辑推理能力，涵盖归纳、演绎和溯因推理。
3. 实验结果显示，当前最先进的MLLMs在逻辑推理能力上存在显著局限，尤其在不同推理类型间表现不均衡。

## 📝 摘要（中文）

逻辑推理是人类智能的基本方面，也是多模态大语言模型（MLLMs）必备的能力。尽管多模态推理取得了显著进展，现有基准测试未能全面评估其推理能力，主要由于缺乏对逻辑推理类型的明确分类和对推理理解的不清晰。为了解决这些问题，我们提出了MME-Reasoning，这是一个全面的基准，旨在评估MLLMs的推理能力，涵盖归纳、演绎和溯因三种推理类型。我们精心策划数据，确保每个问题有效评估推理能力，而非感知技能或知识广度，并扩展评估协议以涵盖多样化问题。我们的评估揭示了当前最先进的MLLMs在全面逻辑推理能力评估中的显著局限性，甚至最先进的模型在综合逻辑推理中表现有限，且不同推理类型之间存在显著的性能不平衡。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态大语言模型在逻辑推理能力评估中的不足，特别是缺乏对不同推理类型的明确分类和评估标准。

**核心思路**：提出MME-Reasoning基准，通过精心策划的问题设计，确保每个问题有效评估推理能力，而非依赖感知技能或知识广度。

**技术框架**：整体架构包括数据策划、问题分类、评估协议扩展等主要模块，确保全面覆盖归纳、演绎和溯因推理类型。

**关键创新**：最重要的创新点在于全面评估逻辑推理能力，揭示了当前MLLMs在不同推理类型上的性能不平衡，提供了系统的评估框架。

**关键设计**：在数据策划中，确保问题的多样性和针对性，设计了新的评估协议，涵盖多种推理场景，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，当前最先进的多模态大语言模型在MME-Reasoning基准上表现有限，尤其在综合逻辑推理能力评估中，性能差异显著，归纳推理的表现明显优于演绎和溯因推理，揭示了模型在逻辑推理方面的关键短板。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能问答系统和人机交互等。通过提升多模态大语言模型的逻辑推理能力，可以在更复杂的场景中实现更高效的智能决策和交互，未来可能推动人工智能在各个领域的广泛应用。

## 📄 摘要（原文）

> Logical reasoning is a fundamental aspect of human intelligence and an essential capability for multimodal large language models (MLLMs). Despite the significant advancement in multimodal reasoning, existing benchmarks fail to comprehensively evaluate their reasoning abilities due to the lack of explicit categorization for logical reasoning types and an unclear understanding of reasoning. To address these issues, we introduce MME-Reasoning, a comprehensive benchmark designed to evaluate the reasoning ability of MLLMs, which covers all three types of reasoning (i.e., inductive, deductive, and abductive) in its questions. We carefully curate the data to ensure that each question effectively evaluates reasoning ability rather than perceptual skills or knowledge breadth, and extend the evaluation protocols to cover the evaluation of diverse questions. Our evaluation reveals substantial limitations of state-of-the-art MLLMs when subjected to holistic assessments of logical reasoning capabilities. Even the most advanced MLLMs show limited performance in comprehensive logical reasoning, with notable performance imbalances across reasoning types. In addition, we conducted an in-depth analysis of approaches such as ``thinking mode'' and Rule-based RL, which are commonly believed to enhance reasoning abilities. These findings highlight the critical limitations and performance imbalances of current MLLMs in diverse logical reasoning scenarios, providing comprehensive and systematic insights into the understanding and evaluation of reasoning capabilities.

