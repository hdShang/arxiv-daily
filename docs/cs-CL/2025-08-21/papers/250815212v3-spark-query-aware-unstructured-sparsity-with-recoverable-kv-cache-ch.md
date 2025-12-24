---
layout: default
title: "SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning"
---

# SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15212" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15212v3</a>
  <a href="https://arxiv.org/pdf/2508.15212.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15212v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15212v3', 'SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huanxuan Liao, Yixing Xu, Shizhu He, Guanchen Li, Xuanwu Yin, Dong Li, Emad Barsoum, Jun Zhao, Kang Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-21 (更新: 2025-11-12)

**备注**: accepted to AAAI 2026

**🔗 代码/项目**: [GITHUB](https://github.com/Xnhyacinth/SparK)

---

## 💡 一句话要点

**提出SparK以解决长上下文推理中的KV缓存瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文推理` `KV缓存` `通道级修剪` `非结构化稀疏性` `大型语言模型` `计算效率` `模型准确性`

## 📋 核心要点

1. 现有方法在处理长上下文推理时，KV缓存的内存使用与序列长度成线性关系，导致计算效率低下。
2. SparK通过在通道级别修剪KV缓存，动态恢复修剪条目，解决了特征维度重要性变化的问题。
3. 实验表明，SparK在80%的修剪比率下，性能下降小于5%，并且KV缓存存储减少超过30%。

## 📝 摘要（中文）

在大型语言模型（LLMs）中，长上下文推理受到KV缓存瓶颈的限制：内存使用随序列长度线性增长，而注意力计算则呈二次增长。现有方法通过在时间轴上压缩KV缓存来应对这一问题，但往往忽视了特征维度上的细粒度重要性变化。为此，本文提出了一种名为SparK的训练无关的即插即用方法，通过在通道级别修剪KV实现非结构化稀疏性，并在注意力分数计算过程中动态恢复修剪的条目。SparK能够在相同内存预算下处理更长的序列，并在保持或提高模型准确性的同时，较基于驱逐的方法减少超过30%的KV缓存存储。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中长上下文推理的KV缓存瓶颈问题。现有方法通过时间轴压缩KV缓存，未能有效利用特征维度上的重要性变化，导致效率与准确性之间的平衡受限。

**核心思路**：SparK的核心思路是通过在通道级别进行KV修剪，利用动态恢复机制，在保持模型性能的同时，减少内存使用。该方法不依赖于训练过程，便于快速集成。

**技术框架**：SparK的整体架构包括KV缓存的通道级修剪模块和动态恢复模块。在推理过程中，首先对KV缓存进行修剪，然后在计算注意力分数时动态恢复必要的通道信息。

**关键创新**：SparK的主要创新在于其在通道级别的非结构化稀疏性处理，区别于传统的时间轴压缩方法，能够更灵活地应对特征维度的变化。

**关键设计**：在设计中，SparK采用了动态恢复机制，确保在注意力计算时能够有效利用修剪后的信息。此外，参数设置和损失函数的选择经过精心设计，以优化模型性能和内存使用。

## 📊 实验亮点

实验结果显示，SparK在80%的修剪比率下，性能下降小于5%，相比于基于驱逐的方法，KV缓存存储减少超过30%。这一结果表明SparK在保持模型准确性的同时，显著提升了计算效率，展示了其强大的实用性和有效性。

## 🎯 应用场景

SparK的研究成果在自然语言处理、对话系统和文本生成等领域具有广泛的应用潜力。通过提高长上下文推理的效率，该方法能够支持更复杂的任务，提升用户体验，并在资源受限的环境中实现更高效的模型部署。

## 📄 摘要（原文）

> Long-context inference in large language models (LLMs) is increasingly constrained by the KV cache bottleneck: memory usage grows linearly with sequence length, while attention computation scales quadratically. Existing approaches address this issue by compressing the KV cache along the temporal axis through strategies such as token eviction or merging to reduce memory and computational overhead. However, these methods often neglect fine-grained importance variations across feature dimensions (i.e., the channel axis), thereby limiting their ability to effectively balance efficiency and model accuracy. In reality, we observe that channel saliency varies dramatically across both queries and positions: certain feature channels carry near-zero information for a given query, while others spike in relevance. To address this oversight, we propose SPARK, a training-free plug-and-play method that applies unstructured sparsity by pruning KV at the channel level, while dynamically restoring the pruned entries during attention score computation. Notably, our approach is orthogonal to existing KV compression and quantization techniques, making it compatible for integration with them to achieve further acceleration. By reducing channel-level redundancy, SPARK enables processing of longer sequences within the same memory budget. For sequences of equal length, SPARK not only preserves or improves model accuracy but also reduces KV cache storage by over 30% compared to eviction-based methods. Furthermore, even with an aggressive pruning ratio of 80%, SPARK maintains performance with less degradation than 5% compared to the baseline eviction method, demonstrating its robustness and effectiveness. Our code will be available at https://github.com/Xnhyacinth/SparK.

