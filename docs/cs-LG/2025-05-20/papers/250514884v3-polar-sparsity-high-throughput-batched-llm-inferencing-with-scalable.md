---
layout: default
title: Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity
---

# Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14884" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14884v3</a>
  <a href="https://arxiv.org/pdf/2505.14884.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14884v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14884v3', 'Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Susav Shrestha, Brad Settlemyer, Nikoli Dryden, Narasimha Reddy

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-11-11)

**备注**: NeurIPS 2025, 10 pages, 7 figures

**🔗 代码/项目**: [GITHUB](https://github.com/susavlsh10/Polar-Sparsity)

---

## 💡 一句话要点

**提出Polar Sparsity以解决大规模LLM推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理加速` `上下文稀疏性` `选择性头注意力` `GPU优化` `高吞吐量` `低延迟`

## 📋 核心要点

1. 现有方法在大批量推理时，MLP层的稀疏性消失，导致计算效率低下。
2. 提出Polar Sparsity，通过选择性头注意力和稀疏感知GPU内核，优化注意力层的计算效率。
3. 实验结果显示，在不同批量和序列长度下，推理速度提升高达2.2倍，且保持了模型的准确性。

## 📝 摘要（中文）

加速大型语言模型（LLM）推理对于需要高吞吐量和低延迟的实际应用至关重要。上下文稀疏性允许每个token动态激活模型参数的一个小子集，但在大批量情况下无法扩展。本文提出Polar Sparsity，强调在批量大小和序列长度扩展时，稀疏性的重要性从MLP层转向注意力层。我们开发了选择性头注意力和硬件高效的稀疏感知GPU内核，实现了在不同批量大小和序列长度下，对OPT、LLaMA-2 & 3、Qwen、Mistral等模型的端到端速度提升高达2.2倍，而不影响准确性。这是首次证明上下文稀疏性可以有效扩展到大批量，显著加速推理，极大地提高了大规模高吞吐量LLM部署系统的实用性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型推理中的计算效率问题，现有方法在大批量情况下，MLP层的稀疏性消失，导致计算资源浪费和延迟增加。

**核心思路**：通过引入Polar Sparsity，强调在扩展批量大小和序列长度时，注意力层的稀疏性相对稳定，而MLP层的稀疏性则迅速消失。选择性头注意力的设计使得在保持模型性能的同时，显著提高计算效率。

**技术框架**：整体架构包括选择性头注意力模块和稀疏感知GPU内核。选择性头注意力模块根据上下文动态选择激活的注意力头，而稀疏感知GPU内核则优化了计算过程，减少了不必要的计算。

**关键创新**：最重要的创新在于首次展示了上下文稀疏性在大批量推理中的有效扩展，特别是在注意力层的应用，使得推理速度显著提升。

**关键设计**：在选择性头注意力中，设计了动态激活机制，确保只有必要的注意力头被激活。同时，GPU内核的设计考虑了稀疏性，优化了内存和计算效率。

## 📊 实验亮点

实验结果表明，Polar Sparsity在不同批量大小和序列长度下，能够实现高达2.2倍的端到端速度提升。与传统方法相比，该方法在保持模型准确性的同时，显著提高了推理效率，展示了其在大规模部署中的实际价值。

## 🎯 应用场景

该研究的潜在应用领域包括大规模自然语言处理任务，如机器翻译、对话系统和文本生成等。通过提高推理效率，Polar Sparsity能够支持实时应用，满足高吞吐量和低延迟的需求，推动大型语言模型在实际场景中的广泛应用。

## 📄 摘要（原文）

> Accelerating large language model (LLM) inference is critical for real-world deployments requiring high throughput and low latency. Contextual sparsity, where each token dynamically activates only a small subset of the model parameters, shows promise but does not scale to large batch sizes due to union of active neurons quickly approaching dense computation. We introduce Polar Sparsity, highlighting a key shift in sparsity importance from MLP to Attention layers as we scale batch size and sequence length. While MLP layers become more compute-efficient under batching, their sparsity vanishes. In contrast, attention becomes increasingly more expensive at scale, while their head sparsity remains stable and batch-invariant. We develop Selective Head Attention with hardware-efficient, sparsity-aware GPU kernels, delivering up to \(2.2\times\) end-to-end speedups for models like OPT, LLaMA-2 \& 3, Qwen, Mistral across various batch sizes and sequence lengths without compromising accuracy. To our knowledge, this is the first work to demonstrate that contextual sparsity can scale effectively to large batch sizes, delivering substantial inference acceleration with minimal changes, making Polar Sparsity practical for large-scale, high-throughput LLM deployment systems. Our code is available at: https://github.com/susavlsh10/Polar-Sparsity.

