---
layout: default
title: RetroInfer: A Vector-Storage Approach for Scalable Long-Context LLM Inference
---

# RetroInfer: A Vector-Storage Approach for Scalable Long-Context LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02922" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02922v2</a>
  <a href="https://arxiv.org/pdf/2505.02922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02922v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02922v2', 'RetroInfer: A Vector-Storage Approach for Scalable Long-Context LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaoqi Chen, Jinkai Zhang, Baotong Lu, Qianxi Zhang, Chengruidong Zhang, Jingjia Luo, Di Liu, Huiqiang Jiang, Qi Chen, Jing Liu, Bailu Ding, Xiao Yan, Jiawei Jiang, Chen Chen, Mingxing Zhang, Yuqing Yang, Fan Yang, Mao Yang

**分类**: cs.LG

**发布日期**: 2025-05-05 (更新: 2025-06-30)

**备注**: 17 pages

---

## 💡 一句话要点

**提出RetroInfer以解决长上下文LLM推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文推理` `大型语言模型` `向量存储` `注意力机制` `GPU优化` `推理加速` `稀疏性方法` `自然语言处理`

## 📋 核心要点

1. 长上下文LLM推理面临GPU内存和带宽限制，现有方法在效率和准确性上存在不足。
2. RetroInfer通过将KV缓存视为向量存储系统，利用注意力稀疏性来加速推理，核心是波动索引和波动缓冲区。
3. 实验结果显示，RetroInfer在GPU内存限制下速度提升4.5倍，在扩展到CPU内存时速度提升10.5倍，且保持高准确性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）上下文长度的增加，推理效率面临显著挑战，主要由于GPU内存和带宽的限制。本文提出了RetroInfer，一个新颖的系统，将关键值（KV）缓存重新概念化为向量存储系统，利用内在的注意力稀疏性加速长上下文LLM推理。其核心是波动索引（wave index），一种注意力感知的向量索引，能够通过三分注意力近似、精度受限的注意力估计和分段聚类等技术高效准确地检索关键标记。此外，波动缓冲区（wave buffer）协调KV缓存的放置，并重叠GPU和CPU之间的计算与数据传输，以维持高吞吐量。与先前的稀疏性方法不同，RetroInfer在不妥协模型准确性的情况下，提供了稳健的性能。实验结果表明，在GPU内存限制下，相比全注意力，速度提升可达4.5倍，而在KV缓存扩展到CPU内存时，相比稀疏注意力基线，速度提升可达10.5倍，同时保持全注意力级别的准确性。

## 🔬 方法详解

**问题定义**：论文旨在解决长上下文LLM推理中的效率问题，现有方法在处理大规模上下文时，往往受到GPU内存和带宽的限制，导致推理速度缓慢和资源浪费。

**核心思路**：RetroInfer的核心思路是将传统的KV缓存重新构建为向量存储系统，利用注意力机制的稀疏性来优化关键标记的检索效率，从而加速推理过程。

**技术框架**：RetroInfer的整体架构包括波动索引和波动缓冲区两个主要模块。波动索引负责高效检索关键标记，而波动缓冲区则优化KV缓存的放置和GPU与CPU之间的计算与数据传输。

**关键创新**：RetroInfer的关键创新在于波动索引的设计，采用了三分注意力近似和精度受限的注意力估计等技术，显著提高了检索效率和准确性，区别于传统稀疏性方法在标记选择和硬件协调上的不足。

**关键设计**：在设计中，波动索引使用了分段聚类技术，确保了高效的标记检索；波动缓冲区则通过重叠计算和数据传输，最大化了资源利用率，提升了整体推理速度。实验中还对参数设置进行了优化，以确保在不同硬件环境下的最佳性能。

## 📊 实验亮点

实验结果显示，RetroInfer在GPU内存限制下，相比全注意力方法实现了高达4.5倍的速度提升，而在KV缓存扩展到CPU内存时，相比稀疏注意力基线实现了高达10.5倍的速度提升，同时保持了全注意力级别的准确性，展示了其优越的性能。

## 🎯 应用场景

RetroInfer的研究成果在多个领域具有潜在应用价值，尤其是在需要处理长文本或上下文的自然语言处理任务中，如对话系统、文本生成和信息检索等。其高效的推理能力能够显著提升这些应用的响应速度和用户体验，未来可能推动更大规模的LLM在实际场景中的应用。

## 📄 摘要（原文）

> The growing context lengths of large language models (LLMs) pose significant challenges for efficient inference, primarily due to GPU memory and bandwidth constraints. We present RetroInfer, a novel system that reconceptualizes the key-value (KV) cache as a vector storage system which exploits the inherent attention sparsity to accelerate long-context LLM inference. At its core is the wave index, an Attention-aWare VEctor index that enables efficient and accurate retrieval of critical tokens through techniques such as tripartite attention approximation, accuracy-bounded attention estimation, and segmented clustering. Complementing this is the wave buffer, which coordinates KV cache placement and overlaps computation and data transfer across GPU and CPU to sustain high throughput. Unlike prior sparsity-based methods that struggle with token selection and hardware coordination, RetroInfer delivers robust performance without compromising model accuracy. Experiments on long-context benchmarks show up to 4.5X speedup over full attention within GPU memory limits and up to 10.5X over sparse attention baselines when KV cache is extended to CPU memory, all while preserving full-attention-level accuracy.

