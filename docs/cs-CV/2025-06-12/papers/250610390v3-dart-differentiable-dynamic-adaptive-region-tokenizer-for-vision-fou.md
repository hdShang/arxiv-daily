---
layout: default
title: "DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models"
---

# DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10390" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10390v3</a>
  <a href="https://arxiv.org/pdf/2506.10390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10390v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10390v3', 'DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shicheng Yin, Kaixuan Yin, Yang Liu, Weixing Chen, Liang Lin

**分类**: cs.CV

**发布日期**: 2025-06-12 (更新: 2025-09-29)

**备注**: Code is available at https://github.com/HCPLab-SYSU/DART

**🔗 代码/项目**: [GITHUB](https://github.com/HCPLab-SYSU/DART)

---

## 💡 一句话要点

**提出DART以解决固定网格分块的性能瓶颈问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态自适应分块` `视觉模型` `内容感知` `高效推理` `多模态AI`

## 📋 核心要点

1. 现有的固定网格分块器在捕捉细节和计算效率之间存在权衡，限制了视觉模型的性能。
2. DART通过可学习的区域评分和分位数分区方法，动态生成内容感知的补丁，优化令牌密度分配。
3. 实验表明，DART显著提高了模型的推理速度和性能，展示了其在多模态AI和机器人领域的潜力。

## 📝 摘要（中文）

标准大规模视觉模型（如Vision Transformer和Vision Mamba）使用的内容无关固定网格分块器存在性能瓶颈，导致在捕捉细节与冗余计算之间的权衡。为了解决这一问题，本文提出了DART，一个完全可微的动态自适应区域分块器。DART利用可学习的区域评分和基于分位数的分区方法，创建内容感知的不同大小的补丁，智能地将更高的令牌密度分配给信息丰富的区域。实验结果表明，配备DART的DeiT-Small（2200万参数）在推理速度几乎翻倍的情况下，性能达到了DeiT-Base（8600万参数）的水平。此外，自适应分块的原则在密集预测和时空视频任务中也展现了其通用性。

## 🔬 方法详解

**问题定义**：现有的视觉模型通常使用固定网格分块器，这种方法无法根据内容的不同而灵活调整，导致在细节捕捉和计算效率之间的权衡，成为性能瓶颈。

**核心思路**：DART的核心思路是通过可学习的区域评分和基于分位数的分区方法，动态生成不同大小的内容感知补丁，从而智能地分配令牌密度，特别是在信息丰富的区域。

**技术框架**：DART的整体架构包括三个主要模块：可学习的区域评分模块、分位数分区模块和动态补丁生成模块。这些模块协同工作，实现了自适应的令牌生成。

**关键创新**：DART的关键创新在于其完全可微的设计，使得分块过程能够通过反向传播进行优化，与传统的固定网格方法相比，DART能够根据内容动态调整补丁大小，从而提高了模型的效率和性能。

**关键设计**：在DART中，区域评分通过神经网络进行学习，分位数分区则依据区域评分的分布进行动态调整。此外，损失函数设计上考虑了信息密度和计算效率的平衡，确保模型在训练过程中能够有效学习。

## 📊 实验亮点

实验结果显示，配备DART的DeiT-Small在推理速度上几乎翻倍，同时性能达到了DeiT-Base的水平，展现出显著的效率提升。这一成果为未来的视觉模型设计提供了新的思路和方向。

## 🎯 应用场景

DART的研究成果在多个领域具有广泛的应用潜力，包括多模态AI、机器人技术和内容生成等。通过提高视觉模型的效率和性能，DART可以帮助实现更智能的视觉理解和交互，推动相关技术的发展和应用。

## 📄 摘要（原文）

> The content-agnostic, fixed-grid tokenizers used by standard large-scale vision models like Vision Transformer (ViT) and Vision Mamba (Vim) represent a fundamental performance bottleneck, creating a trade-off between capturing fine-grained detail and suffering from redundant computation. To resolve this dilemma, we introduce DART, a fully differentiable Dynamic Adaptive Region Tokenizer. DART employs learnable region scores and quantile-based partitioning to create content-aware patches of varying sizes, intelligently allocating a higher token density to information-rich regions. The impact of this approach is profound: it unlocks a more intelligent scaling paradigm, where a DART-equipped DeiT-Small (22M parameters) matches the performance of a DeiT-Base (86M) with nearly double the inference speed by efficiently capturing high-resolution details in key regions. Furthermore, the principle of adaptive tokenization proves its generality with clear benefits in dense prediction and spatiotemporal video tasks. We argue that by resolving the tokenizer bottleneck at its source, adaptive tokenization is a key component for building the next generation of more efficient and capable foundation models for multimodal AI, robotics, and content generation. Code is available at https://github.com/HCPLab-SYSU/DART.

