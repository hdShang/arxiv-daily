---
layout: default
title: "Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction"
---

# Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02558" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02558v2</a>
  <a href="https://arxiv.org/pdf/2508.02558.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02558v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02558v2', 'Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuerong Song, Xiaoran Liu, Ruixiao Li, Zhigeng Liu, Zengfeng Huang, Qipeng Guo, Ziwei He, Xipeng Qiu

**分类**: cs.CL

**发布日期**: 2025-08-04 (更新: 2025-11-05)

**备注**: 12 pages, 7 figures

**🔗 代码/项目**: [GITHUB](https://github.com/OpenMOSS/Sparse-dLLM)

---

## 💡 一句话要点

**提出Sparse-dLLM以解决扩散大语言模型的计算复杂性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散大语言模型` `动态缓存` `稀疏注意力` `计算复杂性` `内存优化` `自然语言处理` `解码效率`

## 📋 核心要点

1. 现有的扩散大语言模型在推理时面临二次计算复杂性和内存开销问题，限制了其在长上下文中的应用。
2. Sparse-dLLM通过动态缓存驱逐和稀疏注意力的结合，选择性地保留重要token并驱逐不重要的token，从而提高解码效率。
3. 实验结果显示，Sparse-dLLM在LLaDA和Dream系列上实现了高达10倍的吞吐量提升，同时保持了与传统dLLMs相似的性能和内存使用。

## 📝 摘要（中文）

扩散大语言模型（dLLMs）在推理和并行解码方面取得了突破，但在推理过程中面临着巨大的二次计算复杂性和内存开销。现有的缓存技术通过存储全层状态来加速解码，但导致了显著的内存使用，限制了长上下文的应用。本文分析了dLLMs中的注意力模式，发现跨层稀疏性持续存在，关键token在解码步骤中保持显著性，而低相关token则保持不重要，从而激励了选择性缓存驱逐。我们提出了Sparse-dLLM，这是第一个将动态缓存驱逐与稀疏注意力结合的无训练框架。通过利用token显著性在步骤中的稳定性，Sparse-dLLM保留关键token，并使用注意力引导策略动态驱逐不重要的前缀/后缀条目。大量实验表明，Sparse-dLLM在LLaDA和Dream系列上实现了比传统dLLMs高出10倍的吞吐量，同时性能相当且峰值内存成本相似，超越了以往方法的效率和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散大语言模型在推理过程中面临的高计算复杂性和内存开销问题。现有方法通过全层状态缓存加速解码，但导致内存使用过高，限制了长上下文的应用。

**核心思路**：Sparse-dLLM的核心思路是利用注意力模式中的稀疏性，通过动态缓存驱逐策略选择性地保留重要token，驱逐不重要的token，从而降低内存使用并提高解码效率。

**技术框架**：Sparse-dLLM的整体架构包括动态缓存管理模块和稀疏注意力机制。动态缓存管理模块负责根据token的显著性动态调整缓存内容，而稀疏注意力机制则优化了计算过程，减少了不必要的计算。

**关键创新**：Sparse-dLLM的主要创新在于首次提出了无训练的动态缓存驱逐与稀疏注意力相结合的方法，显著提高了解码效率和内存使用效率，与传统方法相比具有本质区别。

**关键设计**：在设计中，Sparse-dLLM采用了延迟双向稀疏缓存策略，利用token显著性在解码步骤中的稳定性，确保关键token的保留，同时动态驱逐不重要的前缀和后缀条目。

## 📊 实验亮点

Sparse-dLLM在LLaDA和Dream系列上的实验结果显示，其吞吐量比传统dLLMs高出10倍，同时在性能和峰值内存成本上保持相似，展现了显著的效率提升，超越了以往的相关方法。

## 🎯 应用场景

Sparse-dLLM的研究成果在自然语言处理、对话系统和长文本生成等领域具有广泛的应用潜力。通过提高解码效率和降低内存开销，该方法能够支持更复杂的应用场景，推动大语言模型在实际应用中的普及和发展。

## 📄 摘要（原文）

> Diffusion Large Language Models (dLLMs) enable breakthroughs in reasoning and parallel decoding but suffer from prohibitive quadratic computational complexity and memory overhead during inference. Current caching techniques accelerate decoding by storing full-layer states, yet impose substantial memory usage that limit long-context applications. Our analysis of attention patterns in dLLMs reveals persistent cross-layer sparsity, with pivotal tokens remaining salient across decoding steps and low-relevance tokens staying unimportant, motivating selective cache eviction. We propose Sparse-dLLM, the first training-free framework integrating dynamic cache eviction with sparse attention via delayed bidirectional sparse caching. By leveraging the stability of token saliency over steps, it retains critical tokens and dynamically evicts unimportant prefix/suffix entries using an attention-guided strategy. Extensive experiments on LLaDA and Dream series demonstrate Sparse-dLLM achieves up to 10$\times$ higher throughput than vanilla dLLMs, with comparable performance and similar peak memory costs, outperforming previous methods in efficiency and effectiveness. The code is available at https://github.com/OpenMOSS/Sparse-dLLM.

