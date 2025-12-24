---
layout: default
title: "TaDA: Training-free recipe for Decoding with Adaptive KV Cache Compression and Mean-centering"
---

# TaDA: Training-free recipe for Decoding with Adaptive KV Cache Compression and Mean-centering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04642" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04642v1</a>
  <a href="https://arxiv.org/pdf/2506.04642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04642v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04642v1', 'TaDA: Training-free recipe for Decoding with Adaptive KV Cache Compression and Mean-centering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vinay Joshi, Pratik Prabhanjan Brahma, Zicheng Liu, Emad Barsoum

**分类**: cs.CL

**发布日期**: 2025-06-05

**备注**: ACL-2025 industry-track accepted

---

## 💡 一句话要点

**提出TaDA以解决KV缓存压缩中的稀疏异常处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `关键值缓存` `量化压缩` `均值中心化` `变换器模型` `内存优化` `深度学习` `语言模型`

## 📋 核心要点

1. 现有KV缓存压缩方法在处理稀疏和不连续异常值时存在显著不足，导致内存需求过高。
2. TaDA通过均值中心化和适应性量化精度，消除了对异常值的单独处理，简化了KV缓存的压缩过程。
3. 实验结果显示，TaDA在多个模型上实现了显著的准确性提升，同时将内存占用降低至27%。

## 📝 摘要（中文）

在变换器模型中，关键值（KV）缓存是高效解码的关键组件，但其内存需求随着序列长度的增加而急剧上升，给大型语言模型的可扩展部署带来了挑战。尽管已有多种KV缓存压缩方法被提出，但大多数仍需单独处理稀疏和不连续的异常值。为此，本文提出了TaDA，一种无需训练的KV缓存压缩方案，通过适应各层的误差敏感性来调整量化精度，并采用均值中心化方法消除对异常值的单独处理。实验表明，该方法在多个模型上显著提高了准确性，同时将KV缓存的内存占用降低至原16位基线的27%。

## 🔬 方法详解

**问题定义**：本文旨在解决变换器模型中KV缓存的内存需求问题，现有方法在处理稀疏和不连续异常值时效率低下，导致内存占用过高。

**核心思路**：TaDA提出了一种无需训练的KV缓存压缩方法，通过均值中心化消除对异常值的单独处理，并根据各层的误差敏感性自适应调整量化精度，从而提高压缩效率。

**技术框架**：该方法的整体架构包括两个主要模块：均值中心化模块和自适应量化模块。均值中心化模块负责对KV缓存进行预处理，而自适应量化模块则根据误差敏感性动态调整量化精度。

**关键创新**：TaDA的主要创新在于其训练自由性和对异常值处理的简化，避免了传统量化方法中对稀疏和不连续异常值的复杂管理，显著提高了压缩效率。

**关键设计**：在设计中，TaDA采用了均值中心化技术来消除异常值的影响，并通过动态调整量化精度来适应不同层的误差敏感性，确保了压缩后的KV缓存在保持准确性的同时，显著降低了内存占用。

## 📊 实验亮点

实验结果表明，TaDA将KV缓存的内存占用降低至原16位基线的27%，同时在多个模型上保持了相当的准确性。这一显著的内存压缩与性能保持的平衡，为大型语言模型的可扩展性提供了新的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的推理和长文本生成等场景。通过降低KV缓存的内存占用，TaDA能够支持更长上下文的推理，提升模型在复杂任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The key-value (KV) cache in transformer models is a critical component for efficient decoding or inference, yet its memory demands scale poorly with sequence length, posing a major challenge for scalable deployment of large language models. Among several approaches to KV cache compression, quantization of key and value activations has been widely explored. Most KV cache quantization methods still need to manage sparse and noncontiguous outliers separately. To address this, we introduce TaDA, a training-free recipe for KV cache compression with quantization precision that adapts to error sensitivity across layers and a mean centering to eliminate separate outlier handling. Our approach yields substantial accuracy improvements for multiple models supporting various context lengths. Moreover, our approach does not need to separately manage outlier elements -- a persistent hurdle in most traditional quantization methods. Experiments on standard benchmarks demonstrate that our technique reduces KV cache memory footprint to 27% of the original 16-bit baseline while achieving comparable accuracy. Our method paves the way for scalable and high-performance reasoning in language models by potentially enabling inference for longer context length models, reasoning models, and longer chain of thoughts.

