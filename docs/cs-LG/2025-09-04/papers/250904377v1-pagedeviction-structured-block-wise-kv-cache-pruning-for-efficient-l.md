---
layout: default
title: "PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference"
---

# PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04377" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04377v1</a>
  <a href="https://arxiv.org/pdf/2509.04377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04377v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04377v1', 'PagedEviction: Structured Block-wise KV Cache Pruning for Efficient Large Language Model Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Krishna Teja Chitty-Venkata, Jie Ye, Xian-He Sun, Anthony Kougkas, Murali Emani, Venkatram Vishwanath, Bogdan Nicolae

**分类**: cs.LG

**发布日期**: 2025-09-04

**备注**: Preprint

---

## 💡 一句话要点

**PagedEviction：用于高效大语言模型推理的结构化块级KV缓存剪枝**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `KV缓存` `内存优化` `PagedAttention` `推理加速` `长文本处理` `块级驱逐` `分页内存`

## 📋 核心要点

1. 现有KV缓存方法在长序列场景下内存消耗巨大，成为LLM推理的瓶颈。
2. PagedEviction提出了一种块级KV缓存剪枝策略，专为分页内存布局设计，提升内存效率。
3. 实验表明，PagedEviction在长文本任务中，相比基线方法，能提升内存利用率并保持或提升精度。

## 📝 摘要（中文）

KV缓存通过存储先前处理的token的注意力状态，显著提高了大型语言模型（LLM）推理的效率，从而能够更快地生成后续token。然而，随着序列长度的增加，KV缓存迅速成为主要的内存瓶颈。为了解决这个问题，我们提出了PagedEviction，一种新颖的细粒度、结构化的KV缓存剪枝策略，它增强了vLLM的PagedAttention的内存效率。与依赖于基于注意力的token重要性或跨不同vLLM页面驱逐token的现有方法不同，PagedEviction引入了一种专为分页内存布局设计的有效块级驱逐算法。我们的方法与PagedAttention无缝集成，无需对其CUDA注意力内核进行任何修改。我们在LongBench基准测试套件上评估了Llama-3.1-8B-Instruct、Llama-3.2-1B-Instruct和Llama-3.2-3B-Instruct模型上的PagedEviction，证明了在长上下文任务中，与基线相比，提高了内存使用率并具有更好的准确性。

## 🔬 方法详解

**问题定义**：大型语言模型推理过程中，KV缓存随着序列长度增加迅速膨胀，成为内存瓶颈。现有方法要么基于注意力重要性进行token级别的驱逐，要么跨vLLM页面进行驱逐，效率较低，且可能影响模型精度。

**核心思路**：PagedEviction的核心在于利用vLLM的PagedAttention机制，在分页内存布局上进行结构化的块级驱逐。通过精细控制每个页面的缓存使用，避免不必要的内存占用，同时尽量减少对模型性能的影响。

**技术框架**：PagedEviction与vLLM的PagedAttention无缝集成，无需修改现有的CUDA注意力内核。它主要包含一个块级驱逐算法，该算法根据某种策略（例如，最少使用原则）选择要驱逐的页面块。整体流程是：在生成每个token时，检查KV缓存的使用情况，如果超过阈值，则触发块级驱逐算法，释放部分缓存空间。

**关键创新**：PagedEviction的关键创新在于其结构化的块级驱逐策略，它充分利用了PagedAttention的分页内存布局。与传统的token级别驱逐相比，块级驱逐可以减少驱逐操作的频率，提高效率。与跨页面驱逐相比，PagedEviction在单个页面内进行驱逐，可以更好地控制缓存的局部性，减少对模型性能的影响。

**关键设计**：PagedEviction的关键设计在于块级驱逐算法的选择。论文中可能采用了某种启发式算法，例如最少使用（LRU）或最不常用（LFU）的变体，来选择要驱逐的页面块。具体的参数设置可能包括每个页面的大小、驱逐的阈值等。这些参数需要根据具体的模型和任务进行调整，以达到最佳的性能。

## 📊 实验亮点

论文在Llama-3.1-8B-Instruct、Llama-3.2-1B-Instruct和Llama-3.2-3B-Instruct模型上，使用LongBench基准测试套件进行了评估。实验结果表明，PagedEviction在长上下文任务中，相比基线方法，提高了内存使用率，并且在保证或提升模型准确性的前提下，有效降低了KV缓存的内存占用。

## 🎯 应用场景

PagedEviction可应用于各种需要处理长序列的大型语言模型推理场景，例如长文本生成、文档摘要、代码生成等。通过降低内存需求，该方法可以使更大的模型能够在资源受限的设备上运行，或者在相同的硬件资源下支持更高的并发用户数，从而提高LLM的实际应用价值。

## 📄 摘要（原文）

> KV caching significantly improves the efficiency of Large Language Model (LLM) inference by storing attention states from previously processed tokens, enabling faster generation of subsequent tokens. However, as sequence length increases, the KV cache quickly becomes a major memory bottleneck. To address this, we propose PagedEviction, a novel fine-grained, structured KV cache pruning strategy that enhances the memory efficiency of vLLM's PagedAttention. Unlike existing approaches that rely on attention-based token importance or evict tokens across different vLLM pages, PagedEviction introduces an efficient block-wise eviction algorithm tailored for paged memory layouts. Our method integrates seamlessly with PagedAttention without requiring any modifications to its CUDA attention kernels. We evaluate PagedEviction across Llama-3.1-8B-Instruct, Llama-3.2-1B-Instruct, and Llama-3.2-3B-Instruct models on the LongBench benchmark suite, demonstrating improved memory usage with better accuracy than baselines on long context tasks.

