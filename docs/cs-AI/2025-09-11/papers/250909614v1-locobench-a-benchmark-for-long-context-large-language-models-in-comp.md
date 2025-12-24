---
layout: default
title: "LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Software Engineering"
---

# LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Software Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09614" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09614v1</a>
  <a href="https://arxiv.org/pdf/2509.09614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09614v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09614v1', 'LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Software Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jielin Qiu, Zuxin Liu, Zhiwei Liu, Rithesh Murthy, Jianguo Zhang, Haolin Chen, Shiyu Wang, Ming Zhu, Liangwei Yang, Juntao Tan, Zhepeng Cen, Cheng Qian, Shelby Heinecke, Weiran Yao, Silvio Savarese, Caiming Xiong, Huan Wang

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-11

**备注**: 53 pages

**🔗 代码/项目**: [GITHUB](https://github.com/SalesforceAIResearch/LoCoBench)

---

## 💡 一句话要点

**提出LoCoBench，用于评估长上下文LLM在复杂软件工程中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文LLM` `软件工程` `基准测试` `代码理解` `代码生成` `架构理解` `跨文件推理`

## 📋 核心要点

1. 现有代码评估基准侧重于单函数或短上下文，缺乏对LLM在复杂软件工程中长上下文理解能力的全面评估。
2. LoCoBench通过构建包含8000个跨10种编程语言的复杂场景，系统性地评估LLM在长上下文下的代码理解和推理能力。
3. 实验结果表明，现有长上下文LLM在LoCoBench上表现出显著的性能差距，揭示了复杂软件开发中长上下文理解的挑战。

## 📝 摘要（中文）

本文提出LoCoBench，一个综合性的基准测试，专门用于评估长上下文大型语言模型（LLM）在真实、复杂的软件开发场景中的能力。与现有侧重于单函数补全或短上下文任务的代码评估基准不同，LoCoBench旨在解决长上下文能力的关键评估缺口，这些能力需要理解整个代码库、跨多个文件进行推理，并在大型软件系统中保持架构一致性。该基准测试提供跨10种编程语言系统生成的8000个评估场景，上下文长度跨越10K到1M个token，实现了100倍的变化，从而能够精确评估在实际软件开发环境中长上下文性能的下降。LoCoBench引入了8个任务类别，涵盖了必要的长上下文能力：架构理解、跨文件重构、多会话开发、缺陷调查、功能实现、代码理解、集成测试和安全分析。通过一个五阶段的流程，我们创建了多样化、高质量的场景，挑战LLM以前所未有的规模推理复杂的代码库。我们引入了一个包含17个指标（包括8个新评估指标）的综合评估框架，这些指标分布在4个维度上，并组合成一个LoCoBench Score (LCBS)。对最先进的长上下文模型的评估揭示了巨大的性能差距，表明在复杂软件开发中长上下文理解是一个尚未解决的重大挑战，需要更多关注。LoCoBench已在https://github.com/SalesforceAIResearch/LoCoBench发布。

## 🔬 方法详解

**问题定义**：现有代码评估基准主要关注单函数补全或短上下文任务，无法有效评估LLM在复杂软件工程场景下的长上下文理解和推理能力。在实际软件开发中，理解整个代码库、跨文件推理以及保持架构一致性至关重要，而现有基准测试无法充分覆盖这些能力。

**核心思路**：LoCoBench的核心思路是构建一个包含多样化、高质量、长上下文的软件工程场景的基准测试，以系统性地评估LLM在复杂代码库上的理解和推理能力。通过模拟真实的软件开发任务，例如架构理解、跨文件重构和缺陷调查，来挑战LLM的长上下文处理能力。

**技术框架**：LoCoBench的构建包含一个五阶段的流程：(1) 场景定义：确定8个关键的软件工程任务类别。(2) 数据收集：收集来自开源项目的代码库。(3) 场景生成：基于代码库生成具体的评估场景。(4) 评估指标设计：设计17个评估指标，涵盖代码质量、功能正确性等多个维度。(5) 基准测试执行：使用LLM在生成的场景上执行任务，并使用评估指标进行评估。

**关键创新**：LoCoBench的关键创新在于其对长上下文软件工程场景的系统性构建和评估。它不仅关注代码的语法正确性，更关注LLM对代码架构、跨文件依赖关系和软件工程原则的理解。此外，LoCoBench还引入了新的评估指标，例如架构一致性，以更全面地评估LLM的性能。

**关键设计**：LoCoBench包含8个任务类别，分别是架构理解、跨文件重构、多会话开发、缺陷调查、功能实现、代码理解、集成测试和安全分析。每个任务类别都包含多个评估场景，上下文长度从10K到1M个token不等。评估指标包括代码质量、功能正确性、架构一致性等。LoCoBench Score (LCBS) 是一个综合指标，用于衡量LLM在所有任务上的整体性能。

## 📊 实验亮点

对现有长上下文LLM在LoCoBench上的评估表明，它们在复杂软件工程任务上的性能远未达到理想水平，存在显著的性能差距。例如，在架构理解和跨文件重构等任务上，LLM的准确率和召回率都较低，表明长上下文理解仍然是一个巨大的挑战。LoCoBench的评估结果为未来的研究方向提供了重要参考。

## 🎯 应用场景

LoCoBench可用于评估和改进LLM在软件开发领域的应用，例如自动化代码审查、智能代码补全、缺陷预测和修复、以及软件架构设计。通过LoCoBench的评估，可以推动LLM在软件工程领域的更广泛应用，提高软件开发效率和质量。

## 📄 摘要（原文）

> The emergence of long-context language models with context windows extending to millions of tokens has created new opportunities for sophisticated code understanding and software development evaluation. We propose LoCoBench, a comprehensive benchmark specifically designed to evaluate long-context LLMs in realistic, complex software development scenarios. Unlike existing code evaluation benchmarks that focus on single-function completion or short-context tasks, LoCoBench addresses the critical evaluation gap for long-context capabilities that require understanding entire codebases, reasoning across multiple files, and maintaining architectural consistency across large-scale software systems. Our benchmark provides 8,000 evaluation scenarios systematically generated across 10 programming languages, with context lengths spanning 10K to 1M tokens, a 100x variation that enables precise assessment of long-context performance degradation in realistic software development settings. LoCoBench introduces 8 task categories that capture essential long-context capabilities: architectural understanding, cross-file refactoring, multi-session development, bug investigation, feature implementation, code comprehension, integration testing, and security analysis. Through a 5-phase pipeline, we create diverse, high-quality scenarios that challenge LLMs to reason about complex codebases at unprecedented scale. We introduce a comprehensive evaluation framework with 17 metrics across 4 dimensions, including 8 new evaluation metrics, combined in a LoCoBench Score (LCBS). Our evaluation of state-of-the-art long-context models reveals substantial performance gaps, demonstrating that long-context understanding in complex software development represents a significant unsolved challenge that demands more attention. LoCoBench is released at: https://github.com/SalesforceAIResearch/LoCoBench.

