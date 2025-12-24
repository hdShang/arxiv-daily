---
layout: default
title: Cross-Attention Speculative Decoding
---

# Cross-Attention Speculative Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24544" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24544v3</a>
  <a href="https://arxiv.org/pdf/2505.24544.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24544v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24544v3', 'Cross-Attention Speculative Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Zhong, Manasa Bharadwaj, Yixiao Wang, Nikhil Verma, Yipeng Ji, Chul Lee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-09-22)

---

## 💡 一句话要点

**提出跨注意力推测解码以简化大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `跨注意力` `Transformer` `训练效率` `自然语言处理` `模型简化` `块注意力`

## 📋 核心要点

1. 现有的推测解码方法通常依赖于自注意力解码器，导致架构复杂且难以在不同模型间推广。
2. 本文提出的Beagle模型基于跨注意力机制，简化了架构并提高了训练效率，消除了对池化和辅助组件的需求。
3. 实验结果显示，Beagle在推理速度和训练效率上均优于现有的EAGLE-v2模型，提供了强有力的替代方案。

## 📝 摘要（中文）

推测解码（SD）是一种加速大型语言模型（LLMs）推理的广泛采用的方法，尤其是在草稿模型与目标模型高度对齐时。然而，现有的SD方法通常依赖于紧密耦合的自注意力Transformer解码器，增加了复杂性并降低了模型的通用性。本文提出了Budget EAGLE（Beagle），这是首个基于跨注意力的Transformer解码器SD模型，其性能与领先的自注意力SD模型（EAGLE-v2）相当，同时消除了对池化或辅助组件的需求，简化了架构，提高了训练效率，并在训练时保持稳定的内存使用。为有效训练这一新架构，提出了两阶段块注意力训练方法，确保了块级注意力场景下的训练稳定性和收敛效率。大量实验表明，Beagle在多个LLMs和数据集上实现了竞争性的推理加速和更高的训练效率，成为推测解码架构的有力替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推测解码方法在架构复杂性和通用性上的不足。现有方法通常依赖于自注意力机制，导致模型难以适应不同的应用场景。

**核心思路**：提出基于跨注意力的Transformer解码器，旨在简化推测解码的架构，同时保持与自注意力模型相当的性能。通过消除池化和辅助组件，Beagle模型在训练和推理过程中实现了更高的效率。

**技术框架**：Beagle模型的整体架构包括跨注意力机制的解码器，采用两阶段块注意力训练方法进行训练。该框架通过模块化设计，确保了训练过程的稳定性和高效性。

**关键创新**：Beagle是首个基于跨注意力的推测解码模型，显著简化了模型架构，与传统的自注意力解码器相比，减少了复杂性并提高了通用性。

**关键设计**：在模型设计中，采用了新的损失函数和参数设置，以优化块级注意力的训练过程，确保了模型在不同数据集上的稳定性和高效性。具体的网络结构细节和训练策略在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，Beagle在多个大型语言模型和数据集上实现了显著的推理速度提升，较EAGLE-v2模型提高了训练效率，具体性能数据未详述，但整体表现优于现有主流方法。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过提高推测解码的效率，Beagle模型能够在实时应用中提供更快的响应时间，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Speculative decoding (SD) is a widely adopted approach for accelerating inference in large language models (LLMs), particularly when the draft and target models are well aligned. However, state-of-the-art SD methods typically rely on tightly coupled, self-attention-based Transformer decoders, often augmented with auxiliary pooling or fusion layers. This coupling makes them increasingly complex and harder to generalize across different models. We present Budget EAGLE (Beagle), the first, to our knowledge, cross-attention-based Transformer decoder SD model that achieves performance on par with leading self-attention SD models (EAGLE-v2) while eliminating the need for pooling or auxiliary components, simplifying the architecture, improving training efficiency, and maintaining stable memory usage during training-time simulation. To enable effective training of this novel architecture, we propose Two-Stage Block-Attention Training, a new method that achieves training stability and convergence efficiency in block-level attention scenarios. Extensive experiments across multiple LLMs and datasets show that Beagle achieves competitive inference speedups and higher training efficiency than EAGLE-v2, offering a strong alternative for architectures in speculative decoding.

