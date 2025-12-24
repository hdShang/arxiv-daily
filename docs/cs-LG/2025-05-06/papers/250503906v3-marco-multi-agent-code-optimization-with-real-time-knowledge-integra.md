---
layout: default
title: MARCO: Multi-Agent Code Optimization with Real-Time Knowledge Integration for High-Performance Computing
---

# MARCO: Multi-Agent Code Optimization with Real-Time Knowledge Integration for High-Performance Computing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03906" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03906v3</a>
  <a href="https://arxiv.org/pdf/2505.03906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03906v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03906v3', 'MARCO: Multi-Agent Code Optimization with Real-Time Knowledge Integration for High-Performance Computing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Asif Rahman, Veljko Cvetkovic, Kathleen Reece, Aidan Walters, Yasir Hassan, Aneesh Tummeti, Bryan Torres, Denise Cooney, Margaret Ellis, Dimitrios S. Nikolopoulos

**分类**: cs.DC, cs.LG, cs.SE

**发布日期**: 2025-05-06 (更新: 2025-06-25)

**备注**: 9 pages, 4 figures, 2 tables

---

## 💡 一句话要点

**提出MARCO框架以解决高性能计算中的代码优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高性能计算` `代码优化` `多智能体系统` `实时知识集成` `大型语言模型`

## 📋 核心要点

1. 现有的通用大型语言模型在高性能计算代码生成中未能满足并行性和内存效率等专业需求。
2. MARCO框架通过多智能体架构，结合代码生成和性能评估，利用反馈机制逐步优化代码。
3. 实验结果显示，MARCO在LeetCode 75问题集上实现了14.6%的运行时间减少，集成网络搜索组件后性能提升达30.9%。

## 📝 摘要（中文）

大型语言模型（LLMs）在软件开发中通过代码生成能力带来了变革，但在高性能计算（HPC）领域的有效性仍然有限。HPC代码需要针对并行性、内存效率和架构特定考虑的专业优化，而通用LLMs往往忽视这些需求。本文提出MARCO（多智能体反应式代码优化器），通过专门的多智能体架构增强LLM生成的HPC代码。MARCO采用独立的代理进行代码生成和性能评估，通过反馈循环逐步优化。其关键创新在于MARCO的网络搜索组件，能够从最新的会议论文和研究出版物中检索实时优化技术，弥补预训练LLMs的知识缺口。我们的广泛评估表明，MARCO在LeetCode 75问题集上实现了比Claude 3.5 Sonnet平均减少14.6%的运行时间，而集成网络搜索组件则使基础MARCO系统的性能提升了30.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决高性能计算中代码优化的不足，现有的通用大型语言模型未能有效处理HPC代码的并行性和内存效率等特定需求。

**核心思路**：MARCO框架通过多智能体系统设计，分别负责代码生成和性能评估，利用反馈机制不断优化生成的代码，以满足HPC的特殊要求。

**技术框架**：MARCO的整体架构包括多个独立的智能体，分别负责代码生成和性能评估，并通过反馈循环进行信息交互和优化。网络搜索组件实时检索最新的优化技术，增强了系统的知识基础。

**关键创新**：MARCO的主要创新在于引入了网络搜索组件，能够实时获取最新的优化技术，弥补了传统LLMs在特定领域知识上的不足。这一设计使得MARCO在处理HPC代码时具有更高的灵活性和适应性。

**关键设计**：在设计中，MARCO的智能体之间通过反馈机制进行信息传递，确保生成的代码能够根据性能评估结果进行调整。此外，网络搜索组件的集成使得系统能够动态更新其优化策略，提升了整体性能。

## 📊 实验亮点

实验结果表明，MARCO在LeetCode 75问题集上实现了14.6%的平均运行时间减少，相较于Claude 3.5 Sonnet的表现显著提升。此外，集成网络搜索组件后，MARCO系统的性能提升达30.9%，显示出多智能体系统在高性能代码生成中的巨大潜力。

## 🎯 应用场景

MARCO框架在高性能计算领域具有广泛的应用潜力，能够为科学计算、数据分析和机器学习等领域提供高效的代码优化解决方案。其实时知识集成能力使得开发者能够快速适应不断变化的技术要求，提升代码性能和运行效率。未来，MARCO有望推动HPC领域的代码生成和优化技术的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) have transformed software development through code generation capabilities, yet their effectiveness for high-performance computing (HPC) remains limited. HPC code requires specialized optimizations for parallelism, memory efficiency, and architecture-specific considerations that general-purpose LLMs often overlook. We present MARCO (Multi-Agent Reactive Code Optimizer), a novel framework that enhances LLM-generated code for HPC through a specialized multi-agent architecture. MARCO employs separate agents for code generation and performance evaluation, connected by a feedback loop that progressively refines optimizations. A key innovation is MARCO's web-search component that retrieves real-time optimization techniques from recent conference proceedings and research publications, bridging the knowledge gap in pre-trained LLMs. Our extensive evaluation on the LeetCode 75 problem set demonstrates that MARCO achieves a 14.6\% average runtime reduction compared to Claude 3.5 Sonnet alone, while the integration of the web-search component yields a 30.9\% performance improvement over the base MARCO system. These results highlight the potential of multi-agent systems to address the specialized requirements of high-performance code generation, offering a cost-effective alternative to domain-specific model fine-tuning.

