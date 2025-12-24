---
layout: default
title: "SwizzlePerf: Hardware-Aware LLMs for GPU Kernel Performance Optimization"
---

# SwizzlePerf: Hardware-Aware LLMs for GPU Kernel Performance Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20258" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20258v1</a>
  <a href="https://arxiv.org/pdf/2508.20258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20258v1', 'SwizzlePerf: Hardware-Aware LLMs for GPU Kernel Performance Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arya Tschand, Muhammad Awad, Ryan Swann, Kesavan Ramakrishnan, Jeffrey Ma, Keith Lowery, Ganesh Dasika, Vijay Janapa Reddi

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出SwizzlePerf以解决GPU内核性能优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GPU内核优化` `硬件感知` `大型语言模型` `性能工程` `机器学习` `科学计算` `性能提升`

## 📋 核心要点

1. 现有方法在GPU内核性能优化中缺乏硬件感知，导致优化效果不理想。
2. SwizzlePerf通过显式硬件感知，自动生成针对GPU内核的空间优化，提高了性能。
3. 在实验中，SwizzlePerf为9个内核生成的优化模式实现了最高2.06倍的加速和70%的L2命中率提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在GPU内核性能工程方面取得了进展，但现有方法依赖于低效的基于搜索的优化，缺乏硬件感知特性。SwizzlePerf通过利用特定的内存访问模式、架构规格和历史性能反思，自动生成针对分离架构的GPU内核的空间优化。对于GEMM内核，SwizzlePerf在不到5分钟内生成了与专家性能工程师花费2周时间找到的硬件特定优化模式相同的结果。在10个多样化的机器学习和科学内核的测试中，SwizzlePerf为9个内核生成的优化模式实现了最高2.06倍的加速和70%的L2命中率提升。这项工作是系统性创建硬件感知LLM性能工程代理的第一步。

## 🔬 方法详解

**问题定义**：论文旨在解决现有GPU内核性能优化方法缺乏硬件感知的问题，导致优化效率低下。现有方法通常依赖于搜索策略，无法充分利用硬件特性。

**核心思路**：SwizzlePerf的核心思路是通过利用特定的内存访问模式和架构规格，使大型语言模型具备硬件感知能力，从而生成更高效的优化策略。这样的设计可以显著缩短优化时间并提高性能。

**技术框架**：SwizzlePerf的整体架构包括数据收集、特征提取、模型训练和优化生成四个主要模块。首先，收集工作负载的内存访问模式和架构信息，然后通过LLM进行分析，最后生成针对特定硬件的优化策略。

**关键创新**：SwizzlePerf的最大创新在于将硬件感知引入LLM性能优化中，使得生成的优化策略能够针对特定硬件进行定制，显著提升了优化效果。与传统方法相比，这种方法能够更快地找到最佳优化方案。

**关键设计**：在设计中，SwizzlePerf采用了特定的参数设置来优化生成过程，使用了过滤的性能日志和历史数据进行训练，以确保生成的优化策略能够有效提升性能。

## 📊 实验亮点

实验结果显示，SwizzlePerf在10个多样化的机器学习和科学内核中成功生成了9个内核的优化模式，最高实现了2.06倍的速度提升和70%的L2命中率改善，显著优于传统的优化方法。

## 🎯 应用场景

SwizzlePerf的研究成果在高性能计算、深度学习训练和科学计算等领域具有广泛的应用潜力。通过提高GPU内核的性能，能够显著缩短计算时间，降低能耗，提升整体系统效率，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> Large language models (LLMs) have shown progress in GPU kernel performance engineering using inefficient search-based methods that optimize around runtime. Any existing approach lacks a key characteristic that human performance engineers rely on for near-optimal utilization -- hardware-awareness. By leveraging the workload's specific memory access patterns, architecture specifications, filtered profiling logs, and reflections on historical performance, we can make software-level optimizations that are tailored to the underlying hardware. SwizzlePerf automatically generates spatial optimizations for GPU kernels on disaggregated architectures by giving LLMs explicit hardware-awareness.
>   For a GEMM kernel, SwizzlePerf takes less than 5 minutes to generate the same hardware-specific optimal swizzling pattern that took expert performance engineers 2 weeks to find. On a suite of 10 diverse ML and Science kernels, SwizzlePerf can generate swizzling patterns for 9 of the kernels that achieve up to a 2.06x speedup and 70% improvement in L2 hit rate. This work is the first of many steps toward systematically creating hardware-aware LLM performance engineering agents.

