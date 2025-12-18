---
layout: default
title: CTkvr: KV Cache Retrieval for Long-Context LLMs via Centroid then Token Indexing
---

# CTkvr: KV Cache Retrieval for Long-Context LLMs via Centroid then Token Indexing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15550" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15550v1</a>
  <a href="https://arxiv.org/pdf/2512.15550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15550v1" onclick="toggleFavorite(this, '2512.15550v1', 'CTkvr: KV Cache Retrieval for Long-Context LLMs via Centroid then Token Indexing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kuan Lu, Shuhang Lin, Sai Wu, Yichen Yao, Junhan Yang, Huan Li, Wei Chu, Xu Yinghui, Yuan Qi, Gang Chen

**分类**: cs.CL

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出CTKVR：一种基于质心和Token索引的长文本LLM的KV缓存检索方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本LLM` `KV缓存检索` `质心索引` `Token索引` `推理加速`

## 📋 核心要点

1. 现有动态KV选择方法在长文本LLM中面临准确性和效率的权衡，块级索引牺牲准确性，token级索引效率低。
2. CTKVR利用RoPE后相邻查询向量的相似性，提出质心-token两阶段检索，先用质心索引，再进行token级细化。
3. 实验表明，CTKVR在保证准确性的前提下，显著提升了Llama-3-8B和Yi-9B在长文本场景下的推理吞吐量。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地应用于多轮对话等长文本场景。然而，长文本对推理效率提出了重大挑战，包括来自键值（KV）缓存的高内存开销以及由于过度内存访问而导致的延迟增加。现有的动态KV选择方法难以权衡：块级索引通过检索不相关的KV条目来降低准确性，而token级索引由于低效的检索机制而导致高延迟。本文提出了一种新颖的质心-token KV检索方案CTKVR，以解决这些限制。CTKVR利用了一个关键观察结果：位置相邻的查询向量在旋转位置嵌入（RoPE）之后表现出高度相似性，并共享其大部分top-k KV缓存条目。基于此，CTKVR采用两阶段检索策略：在预填充期间预先计算轻量级质心以进行质心粒度索引，然后进行token级细化以进行精确的KV检索。这种方法平衡了检索效率和准确性。为了进一步提高性能，我们实现了一个优化的系统，用于使用CPU-GPU协同执行来构建和搜索索引。实验表明，CTKVR在多个基准测试中实现了卓越的性能，且准确性降低不到1%。同时，在不同的GPU硬件上，CTKVR在96K上下文长度下，Llama-3-8B和Yi-9B的吞吐量分别提高了3倍和4倍。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本LLM推理过程中，由于KV缓存过大和频繁访问导致的效率瓶颈问题。现有方法，如块级索引，会引入不相关的KV条目，降低准确性；而token级索引，则因检索机制效率低下而导致高延迟。

**核心思路**：论文的核心思路是利用RoPE后相邻位置的查询向量具有高度相似性这一特性，设计一种两阶段的检索策略。首先使用轻量级的质心进行粗粒度的索引，快速定位候选KV条目，然后进行token级别的精细检索，以提高准确性。这种方法旨在平衡检索效率和准确性。

**技术框架**：CTKVR包含两个主要阶段：质心索引构建阶段和KV检索阶段。在质心索引构建阶段，预先计算每个质心的KV表示。在KV检索阶段，首先使用查询向量检索最相关的质心，然后基于检索到的质心，进行token级别的KV检索。整个过程利用CPU-GPU协同执行来加速索引构建和搜索。

**关键创新**：CTKVR的关键创新在于其两阶段的检索策略，即先通过质心进行粗略筛选，再进行token级别的精细检索。这种方法避免了传统token级索引的全局搜索，提高了检索效率，同时通过token级别的细化保证了准确性。与现有方法相比，CTKVR在效率和准确性之间取得了更好的平衡。

**关键设计**：CTKVR的关键设计包括：1) 质心的选择和计算方法，需要保证质心能够代表其所包含的token的特征；2) 两阶段检索的阈值设置，需要在效率和准确性之间进行权衡；3) CPU-GPU协同执行的优化策略，需要充分利用CPU和GPU的计算能力，加速索引构建和搜索过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15550v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15550v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15550v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CTKVR在多个基准测试中表现出色，准确性降低不到1%。在Llama-3-8B和Yi-9B模型上，96K上下文长度下，CTKVR在不同GPU硬件上实现了3倍和4倍的吞吐量提升。这些结果表明CTKVR在长文本推理效率方面具有显著优势。

## 🎯 应用场景

CTKVR适用于需要处理长文本的LLM应用，例如多轮对话系统、长文档摘要、代码生成等。通过提高长文本推理的效率，可以降低部署成本，提升用户体验，并推动LLM在更广泛的领域应用。该研究对于优化LLM在资源受限设备上的部署也具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly applied in long-context scenarios such as multi-turn conversations. However, long contexts pose significant challenges for inference efficiency, including high memory overhead from Key-Value (KV) cache and increased latency due to excessive memory accesses. Recent methods for dynamic KV selection struggle with trade-offs: block-level indexing degrades accuracy by retrieving irrelevant KV entries, while token-level indexing incurs high latency from inefficient retrieval mechanisms. In this paper, we propose CTKVR, a novel centroid-then-token KV retrieval scheme that addresses these limitations. CTKVR leverages a key observation: query vectors adjacent in position exhibit high similarity after Rotary Position Embedding (RoPE) and share most of their top-k KV cache entries. Based on this insight, CTKVR employs a two-stage retrieval strategy: lightweight centroids are precomputed during prefilling for centroid-grained indexing, followed by token-level refinement for precise KV retrieval. This approach balances retrieval efficiency and accuracy. To further enhance performance, we implement an optimized system for indexing construction and search using CPU-GPU co-execution. Experimentally, CTKVR achieves superior performance across multiple benchmarks with less than 1% accuracy degradation. Meanwhile, CTKVR delivers 3 times and 4 times throughput speedups on Llama-3-8B and Yi-9B at 96K context length across diverse GPU hardware.

