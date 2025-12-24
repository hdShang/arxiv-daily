---
layout: default
title: "Projected Compression: Trainable Projection for Efficient Transformer Compression"
---

# Projected Compression: Trainable Projection for Efficient Transformer Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22255" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22255v1</a>
  <a href="https://arxiv.org/pdf/2506.22255.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22255v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22255v1', 'Projected Compression: Trainable Projection for Efficient Transformer Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maciej Stefaniak, Michał Krutul, Jan Małaśnicki, Maciej Pióro, Jakub Krajewski, Sebastian Jaszczur, Marek Cygan, Kamil Adamczewski, Jan Ludziejewski

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出Projected Compression以解决Transformer模型压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型压缩` `Transformer` `投影模块` `深度学习` `自然语言处理` `计算效率` `可训练参数`

## 📋 核心要点

1. 大型语言模型的规模不断增加，导致推理时间和计算需求显著上升，现有的压缩方法难以有效解决这一问题。
2. 本文提出的Projected Compression方法通过训练可学习的投影权重，保留原始模型参数的同时实现模型压缩，避免了额外的计算开销。
3. 实验结果显示，Projected Compression在高质量模型上优于传统的硬剪枝和重训练方法，且性能提升与token数量呈正相关。

## 📝 摘要（中文）

大型语言模型的规模不断增加以提升性能，但这也导致了推理时间和计算需求的增加。因此，模型大小减少的方法受到越来越多的关注。为此，我们提出了一种新颖的模型压缩技术——Projected Compression，通过利用投影模块来减少模型权重。具体而言，我们首先训练额外的可训练投影权重，并保留对所有原始模型参数的访问。随后，这些投影被合并为一个低维的乘积矩阵，从而形成一个标准的、尺寸减小的基于Transformer的模型。与需要额外计算开销的替代方法不同，我们的方法在每个token的计算步骤中与基础模型的FLOPs相匹配。实验结果表明，Projected Compression在高质量模型上优于可比较的硬剪枝和重训练方法。此外，性能提升与token数量的增加呈良好扩展。

## 🔬 方法详解

**问题定义**：本文旨在解决大型Transformer模型在推理时的计算效率问题。现有的模型压缩方法往往需要额外的计算开销，导致实际应用中效率低下。

**核心思路**：提出的Projected Compression方法通过训练可学习的投影权重，将模型权重压缩为低维乘积矩阵，从而在保留原始模型参数的同时减少模型大小。

**技术框架**：该方法的整体架构包括两个主要阶段：首先训练可学习的投影权重，然后将这些权重合并为低维矩阵，最终形成一个压缩的Transformer模型。

**关键创新**：最重要的创新在于通过投影模块实现模型压缩，而不增加额外的计算开销，这与传统的剪枝和重训练方法形成鲜明对比。

**关键设计**：在设计中，重点关注投影权重的训练过程和合并策略，确保在压缩过程中尽可能保留模型的性能和准确性。

## 📊 实验亮点

实验结果表明，Projected Compression在高质量模型上相较于传统的硬剪枝和重训练方法具有显著优势，具体性能提升幅度在多个token数量下均表现良好，验证了该方法的有效性和可扩展性。

## 🎯 应用场景

Projected Compression方法具有广泛的应用潜力，特别是在需要高效推理的大型语言模型场景中，如实时翻译、智能助手和自然语言处理等领域。通过降低模型的计算需求，该技术可以使得在资源受限的设备上运行复杂模型成为可能，推动AI技术的普及和应用。

## 📄 摘要（原文）

> Large language models have steadily increased in size to achieve improved performance; however, this growth has also led to greater inference time and computational demands. Consequently, there is rising interest in model size reduction methods. To address this issue, we propose Projected Compression, a novel model compression technique, that reduces model weights by utilizing projection modules. Specifically, we first train additional trainable projections weights and preserve access to all the original model parameters. Subsequently, these projections are merged into a lower-dimensional product matrix, resulting in a reduced-size standard Transformer-based model. Unlike alternative approaches that require additional computational overhead, our method matches the base model's per-token computation step in FLOPs. Experimental results show that Projected Compression outperforms the comparable hard pruning and retraining approach on higher quality models. Moreover, the performance margin scales well with the number of tokens.

