---
layout: default
title: Breaking the Compression Ceiling: Data-Free Pipeline for Ultra-Efficient Delta Compression
---

# Breaking the Compression Ceiling: Data-Free Pipeline for Ultra-Efficient Delta Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13563" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13563v3</a>
  <a href="https://arxiv.org/pdf/2505.13563.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13563v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13563v3', 'Breaking the Compression Ceiling: Data-Free Pipeline for Ultra-Efficient Delta Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaohui Wang, Peng Ye, Chenyu Huang, Shenghe Zheng, Bo Zhang, Lei Bai, Wanli Ouyang, Tao Chen

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-05-19 (更新: 2025-10-13)

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/xiaohuiwang000/UltraDelta)

---

## 💡 一句话要点

**提出UltraDelta以解决数据依赖的超高效增量压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增量压缩` `模型压缩` `数据无关` `超高压缩` `自然语言处理` `计算机视觉` `多模态学习`

## 📋 核心要点

1. 现有增量压缩方法在高压缩率与模型性能之间难以取得平衡，并且通常依赖于训练数据。
2. UltraDelta通过数据无关的方式实现超高压缩，采用基于方差的稀疏分配、分布感知压缩和迹范数引导重标定等技术。
3. 在多个模型上进行的实验表明，UltraDelta在压缩率高达224倍的情况下，性能优于现有方法，尤其在语言和视觉模型上表现突出。

## 📝 摘要（中文）

随着微调预训练范式的兴起，存储多个微调模型带来了显著的存储开销。增量压缩通过仅存储预训练模型和高度压缩的增量权重来缓解这一问题。然而，现有方法在高压缩率和性能之间难以平衡，并且通常依赖于数据。为了解决这些挑战，本文提出了UltraDelta，这是首个实现超高压缩和强性能的数据无关增量压缩管道。UltraDelta通过三个关键组件设计来最小化冗余、最大化信息并稳定性能。实验表明，UltraDelta在多种模型上均优于现有方法，尤其是在超高压缩情况下。

## 🔬 方法详解

**问题定义**：本文旨在解决现有增量压缩方法在高压缩率与性能之间的矛盾，尤其是其对数据的依赖性。现有方法往往无法在保持模型性能的同时实现高压缩率。

**核心思路**：UltraDelta的核心思路是通过数据无关的方式实现超高压缩，设计了三大关键组件，分别针对不同层次的信息冗余进行优化，从而提升压缩效果和模型稳定性。

**技术框架**：UltraDelta的整体架构包括三个主要模块：1) 基于方差的混合稀疏分配，2) 分布感知压缩，3) 迹范数引导重标定。每个模块针对不同的压缩需求进行优化，形成一个完整的压缩管道。

**关键创新**：UltraDelta的主要创新在于其数据无关性和针对性设计，尤其是基于方差的稀疏分配和迹范数引导重标定，这些设计使得模型在高压缩率下仍能保持良好的性能。

**关键设计**：在关键设计上，UltraDelta采用了基于方差的稀疏分配策略，确保高方差层保留更多信息；分布感知压缩通过均匀量化和分组修剪来优化参数分布；迹范数引导重标定则通过全局重标定因子来提升模型稳定性。

## 📊 实验亮点

实验结果显示，UltraDelta在大型语言模型（如LLaMA-2）上实现了高达50倍的压缩，在通用NLP模型（如RoBERTa和T5）上达到了224倍的压缩率，而在视觉模型（如ViT）上也实现了132倍的压缩，均显著优于现有方法，尤其在超高压缩情况下表现突出。

## 🎯 应用场景

UltraDelta的研究成果在多个领域具有广泛的应用潜力，尤其是在需要存储和部署多个微调模型的场景中，如自然语言处理、计算机视觉和多模态学习等。其高效的增量压缩方法能够显著降低存储成本，提升模型的可用性和灵活性，推动智能应用的发展。

## 📄 摘要（原文）

> With the rise of the fine-tuned-pretrained paradigm, storing numerous fine-tuned models for multi-tasking creates significant storage overhead. Delta compression alleviates this by storing only the pretrained model and the highly compressed delta weights (the differences between fine-tuned and pretrained model weights). However, existing methods fail to maintain both high compression and performance, and often rely on data. To address these challenges, we propose UltraDelta, the first data-free delta compression pipeline that achieves both ultra-high compression and strong performance. UltraDelta is designed to minimize redundancy, maximize information, and stabilize performance across inter-layer, intra-layer, and global dimensions, using three key components: (1) Variance-Based Mixed Sparsity Allocation assigns sparsity based on variance, giving lower sparsity to high-variance layers to preserve inter-layer information. (2) Distribution-Aware Compression applies uniform quantization and then groups parameters by value, followed by group-wise pruning, to better preserve intra-layer distribution. (3) Trace-Norm-Guided Rescaling uses the trace norm of delta weights to estimate a global rescaling factor, improving model stability under higher compression. Extensive experiments across (a) large language models (fine-tuned on LLaMA-2 7B and 13B) with up to 50x compression, (b) general NLP models (RoBERTa-base, T5-base) with up to 224x compression, (c) vision models (ViT-B/32, ViT-L/14) with up to 132x compression, and (d) multi-modal models (BEiT-3) with 18x compression, demonstrate that UltraDelta consistently outperforms existing methods, especially under ultra-high compression. Code is available at https://github.com/xiaohuiwang000/UltraDelta.

