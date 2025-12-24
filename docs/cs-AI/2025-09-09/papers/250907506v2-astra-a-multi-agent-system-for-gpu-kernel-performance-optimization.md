---
layout: default
title: "Astra: A Multi-Agent System for GPU Kernel Performance Optimization"
---

# Astra: A Multi-Agent System for GPU Kernel Performance Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07506" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07506v2</a>
  <a href="https://arxiv.org/pdf/2509.07506.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07506v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07506v2', 'Astra: A Multi-Agent System for GPU Kernel Performance Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anjiang Wei, Tianran Sun, Yogesh Seenichamy, Hang Song, Anne Ouyang, Azalia Mirhoseini, Ke Wang, Alex Aiken

**分类**: cs.DC, cs.AI, cs.CL, cs.LG, cs.SE

**发布日期**: 2025-09-09 (更新: 2025-12-02)

**🔗 代码/项目**: [GITHUB](https://github.com/Anjiang-Wei/Astra)

---

## 💡 一句话要点

**Astra：基于多智能体系统的GPU Kernel性能优化方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GPU Kernel优化` `多智能体系统` `大型语言模型` `CUDA` `性能优化`

## 📋 核心要点

1. GPU kernel优化是高性能计算和机器学习交叉领域的核心挑战，现有方法依赖大量手动调整和工程设计。
2. Astra提出一种基于LLM的多智能体系统，从现有CUDA实现出发，通过智能体协作进行kernel优化。
3. 实验表明，Astra在SGLang的kernel上实现了平均1.32倍的加速，证明了LLM在kernel优化方面的潜力。

## 📝 摘要（中文）

本文介绍Astra，一种基于LLM的多智能体系统，用于GPU kernel优化。与以往方法不同，Astra从SGLang（一种广泛部署的LLM服务框架）中提取的现有CUDA实现开始，而不是将PyTorch模块作为规范。在Astra中，专门的LLM智能体通过迭代的代码生成、测试、分析和规划进行协作，以生成既正确又高性能的kernel。在来自SGLang的kernel上，Astra使用带有OpenAI o4-mini的零样本提示实现了平均1.32倍的加速。详细的案例研究进一步表明，LLM可以自主应用循环转换、优化内存访问模式、利用CUDA intrinsics以及利用快速数学运算来产生显著的性能提升。这项工作强调了多智能体LLM系统作为GPU kernel优化的一种有前景的新范例。

## 🔬 方法详解

**问题定义**：GPU kernel的优化对于加速大语言模型（LLM）的训练和推理至关重要。然而，实现高性能通常需要大量的手动调整，这既耗时又需要专业的知识。现有的基于编译器的系统虽然减轻了一些负担，但仍然需要大量的人工设计和工程工作。因此，如何自动化且高效地优化GPU kernel性能是一个关键问题。

**核心思路**：Astra的核心思路是利用大型语言模型（LLM）作为智能体，通过多智能体协作的方式，自动化地探索和优化GPU kernel。与以往将PyTorch模块翻译成CUDA代码的方法不同，Astra直接从现有的、经过实际部署的CUDA代码（例如SGLang中的kernel）入手，避免了从高级抽象到低级实现的转换过程中的信息损失。

**技术框架**：Astra采用多智能体系统架构，包含多个专门的LLM智能体，这些智能体协同工作以优化GPU kernel。主要流程包括：1) 代码生成：LLM智能体根据当前kernel代码生成新的优化版本。2) 测试：对生成的代码进行功能测试，确保正确性。3) 性能分析：使用profiler分析kernel的性能瓶颈。4) 规划：根据测试和分析结果，制定下一步优化策略。这些步骤迭代进行，直到达到预定的性能目标。

**关键创新**：Astra的关键创新在于其多智能体协作的架构和直接从现有CUDA代码出发的优化策略。多智能体系统允许不同的智能体专注于不同的优化方面（例如循环优化、内存访问优化），从而更有效地探索优化空间。直接从现有CUDA代码出发避免了从高级抽象到低级实现的转换过程中的信息损失，使得LLM能够更好地理解和优化代码。

**关键设计**：Astra的关键设计包括：1) 智能体的角色划分和协作机制：不同的智能体负责不同的任务，例如代码生成、测试、性能分析和规划。智能体之间通过共享信息和协作来共同优化kernel。2) LLM的提示工程：设计合适的提示语，引导LLM生成高质量的优化代码。3) 迭代优化策略：通过迭代的代码生成、测试、分析和规划，逐步改进kernel的性能。

## 📊 实验亮点

Astra在来自SGLang的kernel上进行了实验，结果表明，使用带有OpenAI o4-mini的零样本提示，Astra实现了平均1.32倍的加速。此外，案例研究表明，LLM可以自主应用循环转换、优化内存访问模式、利用CUDA intrinsics以及利用快速数学运算来产生显著的性能提升。这些结果表明，多智能体LLM系统在GPU kernel优化方面具有巨大的潜力。

## 🎯 应用场景

Astra具有广泛的应用前景，可用于加速各种GPU加速的应用，特别是大语言模型的训练和推理。通过自动化kernel优化，Astra可以降低开发成本，提高性能，并使得更多开发者能够充分利用GPU的强大计算能力。未来，Astra可以扩展到支持更多的硬件平台和编程语言，进一步提升其通用性和实用性。

## 📄 摘要（原文）

> GPU kernel optimization has long been a central challenge at the intersection of high-performance computing and machine learning. Efficient kernels are crucial for accelerating large language model (LLM) training and serving, yet attaining high performance typically requires extensive manual tuning. Compiler-based systems reduce some of this burden, but still demand substantial manual design and engineering effort. Recently, researchers have explored using LLMs for GPU kernel generation, though prior work has largely focused on translating high-level PyTorch modules into CUDA code. In this work, we introduce Astra, the first LLM-based multi-agent system for GPU kernel optimization. Unlike previous approaches, Astra starts from existing CUDA implementations extracted from SGLang, a widely deployed framework for serving LLMs, rather than treating PyTorch modules as the specification. Within Astra, specialized LLM agents collaborate through iterative code generation, testing, profiling, and planning to produce kernels that are both correct and high-performance. On kernels from SGLang, Astra achieves an average speedup of 1.32x using zero-shot prompting with OpenAI o4-mini. A detailed case study further demonstrates that LLMs can autonomously apply loop transformations, optimize memory access patterns, exploit CUDA intrinsics, and leverage fast math operations to yield substantial performance gains. Our work highlights multi-agent LLM systems as a promising new paradigm for GPU kernel optimization. Our code is publicly available at https://github.com/Anjiang-Wei/Astra.

