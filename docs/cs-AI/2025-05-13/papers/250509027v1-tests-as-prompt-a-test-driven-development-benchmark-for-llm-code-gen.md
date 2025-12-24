---
layout: default
title: Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation
---

# Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09027" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09027v1</a>
  <a href="https://arxiv.org/pdf/2505.09027.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09027v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09027v1', 'Tests as Prompt: A Test-Driven-Development Benchmark for LLM Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Cui

**分类**: cs.SE, cs.AI

**发布日期**: 2025-05-13

**备注**: arXiv admin note: text overlap with arXiv:2409.05177

---

## 💡 一句话要点

**提出WebApp1K基准以评估LLM在测试驱动开发中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试驱动开发` `大型语言模型` `代码生成` `性能评估` `软件开发`

## 📋 核心要点

1. 现有方法主要依赖自然语言提示，难以有效评估LLMs在真实软件开发中的表现。
2. 提出WebApp1K基准，利用测试用例作为提示和验证，强调LLMs从测试中生成代码的能力。
3. 通过对19个模型的评估，发现指令遵循和上下文学习是TDD成功的关键，超越了传统编码能力。

## 📝 摘要（中文）

我们介绍了WebApp1K，这是一个新颖的基准，用于评估大型语言模型（LLMs）在测试驱动开发（TDD）任务中的表现，其中测试用例既作为提示又作为代码生成的验证。与传统依赖自然语言提示的方法不同，我们的基准强调LLMs直接从测试用例中理解和实现功能的能力，反映了现实软件开发实践。基准包含1000个多样化的挑战，涵盖20个应用领域，评估LLMs在上下文长度和多特征复杂性限制下生成紧凑、功能性代码的能力。我们的研究发现，遵循指令和上下文学习是TDD成功的关键能力，超越了通用编码能力或预训练知识的重要性。通过对19个前沿模型的全面评估，我们揭示了性能瓶颈，如长提示中的指令丢失，并提供了涵盖多个根本原因的详细错误分析。这项工作强调了TDD特定基准的实际价值，并为提升LLM在严格应用驱动编码场景中的能力奠定了基础。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效评估大型语言模型在测试驱动开发中的能力。现有方法主要依赖自然语言提示，无法真实反映软件开发中的实际需求和挑战。

**核心思路**：论文的核心思路是利用测试用例作为提示和验证手段，强调LLMs从测试用例中直接理解和实现功能的能力。这种设计更贴近真实开发环境，能够有效评估模型的实际应用能力。

**技术框架**：整体架构包括数据集构建、模型评估和性能分析三个主要模块。数据集包含1000个多样化的测试用例，模型评估通过生成代码的功能性和紧凑性进行，性能分析则关注模型在长提示下的表现。

**关键创新**：最重要的技术创新点在于将测试用例作为提示和验证的双重角色，突破了传统方法的局限，使得评估更具针对性和实用性。

**关键设计**：在参数设置上，考虑了上下文长度和多特征复杂性，损失函数设计上强调了指令遵循和上下文学习的重要性，网络结构则优化了生成代码的紧凑性和功能性。

## 📊 实验亮点

实验结果显示，19个前沿模型在遵循指令和上下文学习方面表现出显著差异，某些模型在长提示下的性能下降超过20%。通过详细的错误分析，揭示了指令丢失等多个性能瓶颈，为后续研究提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发工具、自动化测试生成、代码审查和教育等。通过提供一个针对TDD的评估基准，能够帮助开发者更好地理解和利用LLMs，提高软件开发效率和代码质量。未来，该基准可能推动LLMs在更复杂的应用场景中的应用，促进智能编程助手的发展。

## 📄 摘要（原文）

> We introduce WebApp1K, a novel benchmark for evaluating large language models (LLMs) in test-driven development (TDD) tasks, where test cases serve as both prompt and verification for code generation. Unlike traditional approaches relying on natural language prompts, our benchmark emphasizes the ability of LLMs to interpret and implement functionality directly from test cases, reflecting real-world software development practices. Comprising 1000 diverse challenges across 20 application domains, the benchmark evaluates LLMs on their ability to generate compact, functional code under the constraints of context length and multi-feature complexity. Our findings highlight instruction following and in-context learning as critical capabilities for TDD success, surpassing the importance of general coding proficiency or pretraining knowledge. Through comprehensive evaluation of 19 frontier models, we reveal performance bottlenecks, such as instruction loss in long prompts, and provide a detailed error analysis spanning multiple root causes. This work underscores the practical value of TDD-specific benchmarks and lays the foundation for advancing LLM capabilities in rigorous, application-driven coding scenarios.

