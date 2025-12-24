---
layout: default
title: CHORUS: Zero-shot Hierarchical Retrieval and Orchestration for Generating Linear Programming Code
---

# CHORUS: Zero-shot Hierarchical Retrieval and Orchestration for Generating Linear Programming Code

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01485" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01485v1</a>
  <a href="https://arxiv.org/pdf/2505.01485.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01485v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01485v1', 'CHORUS: Zero-shot Hierarchical Retrieval and Orchestration for Generating Linear Programming Code')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tasnim Ahmed, Salimur Choudhury

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-02

**备注**: This paper has been accepted for presentation at the 19th Learning and Intelligent Optimization Conference (LION 19)

---

## 💡 一句话要点

**提出CHORUS框架以解决线性规划代码生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `线性规划` `代码生成` `增强检索生成` `大型语言模型` `层次化分块` `自动化优化` `自然语言处理`

## 📋 核心要点

1. 现有方法在生成线性规划代码时，往往需要较高的领域知识和编程能力，限制了非专家的使用。
2. CHORUS框架通过层次化的分块策略和增强检索生成技术，能够从自然语言问题中自动生成LP代码。
3. 实验结果表明，CHORUS在多个开源LLMs上显著提升了代码生成性能，甚至超越了更强的基线模型如GPT-3.5和GPT-4。

## 📝 摘要（中文）

线性规划（LP）问题旨在在约束条件下寻找目标的最优解。这些问题通常需要领域知识、数学技能和编程能力，对非专家构成重大挑战。本研究探讨了大型语言模型（LLMs）在生成特定求解器LP代码方面的效率。我们提出了CHORUS，一个增强检索生成（RAG）框架，用于从自然语言问题陈述合成基于Gurobi的LP代码。CHORUS采用了层次树状分块策略，并生成基于文档代码示例的附加元数据，以促进自包含、语义连贯的检索。CHORUS的两阶段检索方法和交叉编码器重排序进一步确保了上下文相关性。经过实验验证，CHORUS显著提升了开源LLMs的代码生成性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决线性规划代码生成中的效率和准确性问题。现有方法通常依赖于专家知识，难以满足非专家用户的需求。

**核心思路**：CHORUS框架结合了增强检索生成（RAG）技术和层次化分块策略，旨在从自然语言描述中自动生成高质量的LP代码。通过这种设计，系统能够更好地理解问题上下文并生成相应代码。

**技术框架**：CHORUS的整体架构包括两个主要模块：首先是基于层次化分块的检索模块，其次是生成模块。检索模块负责从文档中获取相关代码示例，而生成模块则利用这些示例生成最终的LP代码。

**关键创新**：CHORUS的创新之处在于其层次化树状分块策略和两阶段检索方法，这使得生成的代码在语义上更加连贯且上下文相关，显著提升了生成效果。

**关键设计**：在设计中，CHORUS使用了专家提示和结构化解析器，以引导模型生成更为准确的代码。此外，交叉编码器重排序技术确保了检索结果的相关性，进一步提升了生成性能。

## 📊 实验亮点

实验结果显示，CHORUS在NL4Opt-Code基准测试中显著提升了开源LLMs的性能，尤其是Llama3.1（8B）、Llama3.3（70B）等模型，相较于基线和传统RAG方法，性能提升幅度显著，甚至与GPT-3.5和GPT-4相当，同时计算资源需求大幅降低。

## 🎯 应用场景

该研究的潜在应用领域包括优化算法的自动化生成、教育领域的编程辅助工具以及工业界的决策支持系统。通过降低对领域知识的依赖，CHORUS可以帮助更多非专家用户解决复杂的线性规划问题，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Linear Programming (LP) problems aim to find the optimal solution to an objective under constraints. These problems typically require domain knowledge, mathematical skills, and programming ability, presenting significant challenges for non-experts. This study explores the efficiency of Large Language Models (LLMs) in generating solver-specific LP code. We propose CHORUS, a retrieval-augmented generation (RAG) framework for synthesizing Gurobi-based LP code from natural language problem statements. CHORUS incorporates a hierarchical tree-like chunking strategy for theoretical contents and generates additional metadata based on code examples from documentation to facilitate self-contained, semantically coherent retrieval. Two-stage retrieval approach of CHORUS followed by cross-encoder reranking further ensures contextual relevance. Finally, expertly crafted prompt and structured parser with reasoning steps improve code generation performance significantly. Experiments on the NL4Opt-Code benchmark show that CHORUS improves the performance of open-source LLMs such as Llama3.1 (8B), Llama3.3 (70B), Phi4 (14B), Deepseek-r1 (32B), and Qwen2.5-coder (32B) by a significant margin compared to baseline and conventional RAG. It also allows these open-source LLMs to outperform or match the performance of much stronger baselines-GPT3.5 and GPT4 while requiring far fewer computational resources. Ablation studies further demonstrate the importance of expert prompting, hierarchical chunking, and structured reasoning.

