---
layout: default
title: Sparse Attention Remapping with Clustering for Efficient LLM Decoding on PIM
---

# Sparse Attention Remapping with Clustering for Efficient LLM Decoding on PIM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05772" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05772v1</a>
  <a href="https://arxiv.org/pdf/2505.05772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05772v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05772v1', 'Sparse Attention Remapping with Clustering for Efficient LLM Decoding on PIM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zehao Fan, Garrett Gagnon, Zhenyu Liu, Liu Liu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**提出STARC以解决PIM架构下LLM解码效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `处理内存计算` `长上下文推理` `深度学习优化` `内存映射` `KV缓存` `Transformer模型`

## 📋 核心要点

1. 现有的LLM解码方法在长上下文情况下对内存带宽造成瓶颈，导致效率低下。
2. STARC通过语义聚类KV对并优化内存映射，实现了选择性注意力和并行处理，减少了数据移动开销。
3. 实验表明，STARC在延迟和能耗方面分别降低了19%-31%和19%-27%，在KV缓存预算下更是显著提升。

## 📝 摘要（中文）

基于Transformer的模型在自回归解码过程中对内存系统造成了显著压力，尤其是在长上下文情况下。处理内存中的计算（PIM）架构提供了高带宽和并行计算能力，但现有设计主要针对密集注意力，难以应对现代键值缓存的稀疏性带来的动态访问模式。本文提出了一种名为STARC的新型稀疏优化数据映射方案，通过语义相似性对KV对进行聚类，并将其映射到与PIM银行结构对齐的连续内存区域，从而实现高效的LLM解码。实验结果表明，STARC在降低延迟和能耗方面表现优异，同时保持了与最先进稀疏注意力方法相当的模型准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决在PIM架构下，LLM解码过程中由于频繁内存访问和KV缓存稀疏性导致的性能瓶颈。现有方法在处理动态、非规则的访问模式时，面临工作负载不均衡的问题，影响了吞吐量和资源利用率。

**核心思路**：STARC的核心思路是通过语义相似性对KV对进行聚类，并将其映射到连续的内存区域，从而优化内存访问模式，减少频繁的重聚类和数据移动开销。

**技术框架**：STARC的整体架构包括数据聚类模块、内存映射模块和查询处理模块。数据聚类模块负责根据语义相似性对KV对进行聚类，内存映射模块将聚类结果映射到PIM结构中，查询处理模块则在解码过程中根据预计算的质心进行相关token的检索。

**关键创新**：STARC的主要创新在于其稀疏优化的数据映射方案，能够有效应对现代KV缓存的稀疏性，提升了内存访问的效率，与传统的基于token的稀疏方法相比，显著提高了性能。

**关键设计**：在设计中，STARC采用了聚类算法来确定KV对的质心，并通过对齐PIM银行结构来优化内存布局。此外，系统在KV缓存预算下的性能优化策略也为实现高效解码提供了保障。

## 📊 实验亮点

实验结果显示，STARC在HBM-PIM系统上相较于常见的token级稀疏方法，注意力层延迟降低了19%-31%，能耗减少了19%-27%。在KV缓存预算为1024的情况下，延迟和能耗分别降低了54%-74%和45%-67%，同时保持了与最先进稀疏注意力方法相当的模型准确性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等需要高效LLM解码的场景。STARC的设计不仅提升了LLM的推理效率，还为未来在PIM架构上实现更复杂的深度学习任务提供了基础，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Transformer-based models are the foundation of modern machine learning, but their execution, particularly during autoregressive decoding in large language models (LLMs), places significant pressure on memory systems due to frequent memory accesses and growing key-value (KV) caches. This creates a bottleneck in memory bandwidth, especially as context lengths increase. Processing-in-memory (PIM) architectures are a promising solution, offering high internal bandwidth and compute parallelism near memory. However, current PIM designs are primarily optimized for dense attention and struggle with the dynamic, irregular access patterns introduced by modern KV cache sparsity techniques. Consequently, they suffer from workload imbalance, reducing throughput and resource utilization. In this work, we propose STARC, a novel sparsity-optimized data mapping scheme tailored specifically for efficient LLM decoding on PIM architectures. STARC clusters KV pairs by semantic similarity and maps them to contiguous memory regions aligned with PIM bank structures. During decoding, queries retrieve relevant tokens at cluster granularity by matching against precomputed centroids, enabling selective attention and parallel processing without frequent reclustering or data movement overhead. Experiments on the HBM-PIM system show that, compared to common token-wise sparsity methods, STARC reduces attention-layer latency by 19%--31% and energy consumption by 19%--27%. Under a KV cache budget of 1024, it achieves up to 54%--74% latency reduction and 45%--67% energy reduction compared to full KV cache retrieval. Meanwhile, STARC maintains model accuracy comparable to state-of-the-art sparse attention methods, demonstrating its effectiveness in enabling efficient and hardware-friendly long-context LLM inference on PIM architectures.

