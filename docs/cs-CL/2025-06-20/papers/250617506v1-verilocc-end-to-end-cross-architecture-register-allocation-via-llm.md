---
layout: default
title: "VeriLocc: End-to-End Cross-Architecture Register Allocation via LLM"
---

# VeriLocc: End-to-End Cross-Architecture Register Allocation via LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17506" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17506v1</a>
  <a href="https://arxiv.org/pdf/2506.17506.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17506v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17506v1', 'VeriLocc: End-to-End Cross-Architecture Register Allocation via LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lesheng Jin, Zhenyuan Ruan, Haohui Mai, Jingbo Shang

**分类**: cs.CL, cs.OS

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出VeriLocc以解决GPU架构间寄存器分配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `寄存器分配` `大型语言模型` `GPU架构` `编译器技术` `性能优化` `深度学习` `高性能计算`

## 📋 核心要点

1. 现有的寄存器分配方法依赖于手工设计的启发式算法，难以适应快速发展的GPU架构，且需要频繁调优。
2. VeriLocc框架结合了大型语言模型和正式编译技术，通过微调LLM实现跨架构的寄存器分配，提升了分配的准确性和通用性。
3. 在矩阵乘法和多头注意力的实验中，VeriLocc的单次准确率达到85-99%，并且在性能上超越了现有的专家调优库。

## 📝 摘要（中文）

现代GPU快速发展，但现有编译器仍依赖手工设计的寄存器分配启发式方法，这些方法需要针对每一代硬件进行大量重新调优。本文提出了VeriLocc框架，将大型语言模型（LLMs）与正式编译器技术相结合，实现跨GPU架构的通用和可验证的寄存器分配。VeriLocc通过微调LLM，将中间表示（MIRs）转换为特定目标的寄存器分配，并借助静态分析进行跨架构的归一化和泛化，同时通过验证器引导的再生循环确保正确性。在矩阵乘法（GEMM）和多头注意力（MHA）上的评估显示，VeriLocc实现了85-99%的单次准确率和接近100%的通过率。案例研究表明，VeriLocc发现的寄存器分配性能优于专家调优的库，运行时间比rocBLAS提升超过10%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有GPU架构间寄存器分配方法的局限性，特别是手工设计的启发式算法在面对新硬件时的适应性不足和调优成本高的问题。

**核心思路**：VeriLocc通过结合大型语言模型（LLMs）与正式编译器技术，利用LLM的强大生成能力，将中间表示（MIRs）转换为特定目标的寄存器分配，从而实现跨架构的通用性和可验证性。

**技术框架**：VeriLocc的整体架构包括三个主要模块：首先是LLM的微调模块，用于生成寄存器分配；其次是静态分析模块，负责进行跨架构的归一化和泛化；最后是验证器引导的再生循环，确保生成的寄存器分配的正确性。

**关键创新**：VeriLocc的创新在于将LLM与正式编译技术结合，形成了一种新的寄存器分配方法，能够在不同GPU架构间实现高效的寄存器分配，显著提高了分配的准确性和性能。

**关键设计**：在设计中，VeriLocc采用了特定的损失函数来优化寄存器分配的准确性，并通过静态分析确保生成的分配在不同架构间的有效性。

## 📊 实验亮点

VeriLocc在矩阵乘法和多头注意力任务中表现出色，单次准确率达到85-99%，并且在性能上超越了专家调优的库，运行时间比rocBLAS提升超过10%。这些结果表明，VeriLocc在寄存器分配方面具有显著的优势和实用价值。

## 🎯 应用场景

VeriLocc的研究成果在高性能计算、深度学习和图形处理等领域具有广泛的应用潜力。通过实现更高效的寄存器分配，能够显著提升GPU程序的运行效率，降低开发和维护成本，推动相关技术的进一步发展。

## 📄 摘要（原文）

> Modern GPUs evolve rapidly, yet production compilers still rely on hand-crafted register allocation heuristics that require substantial re-tuning for each hardware generation. We introduce VeriLocc, a framework that combines large language models (LLMs) with formal compiler techniques to enable generalizable and verifiable register allocation across GPU architectures. VeriLocc fine-tunes an LLM to translate intermediate representations (MIRs) into target-specific register assignments, aided by static analysis for cross-architecture normalization and generalization and a verifier-guided regeneration loop to ensure correctness. Evaluated on matrix multiplication (GEMM) and multi-head attention (MHA), VeriLocc achieves 85-99% single-shot accuracy and near-100% pass@100. Case study shows that VeriLocc discovers more performant assignments than expert-tuned libraries, outperforming rocBLAS by over 10% in runtime.

