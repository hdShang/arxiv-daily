---
layout: default
title: "KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache"
---

# KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21354" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21354v2</a>
  <a href="https://arxiv.org/pdf/2509.21354.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21354v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21354v2', 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanshun Xu, Long Zhuang, Lianlei Shan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-20 (更新: 2025-11-23)

---

## 💡 一句话要点

**KV-Efficient VLA：利用RNN门控分块KV缓存加速视觉语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `机器人控制` `KV缓存压缩` `RNN门控` `推理加速`

## 📋 核心要点

1. VLA模型在长时程任务中面临高计算成本和KV缓存大内存需求的挑战，限制了其在实际机器人应用中的扩展性。
2. KV-Efficient VLA通过RNN门控机制，对KV缓存进行分块和选择性过滤，保留高实用性上下文，降低计算和内存开销。
3. 实验结果表明，该方法在FLOPs、推理速度和KV内存占用方面均有显著提升，且易于集成到现有VLA框架中。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型为机器人感知和控制提供了一个统一的框架，但其扩展到真实世界、长时程任务的能力受到注意力机制的高计算成本以及推理过程中存储键值(KV)对所需的大量内存的限制，尤其是在保留历史图像tokens作为上下文时。最近的方法主要集中在扩展骨干架构以提高泛化能力，而较少强调解决实时使用必不可少的推理效率问题。本文提出了KV-Efficient VLA，这是一种与模型无关的内存压缩方法，旨在通过引入轻量级机制来选择性地保留高实用性的上下文来解决这些限制。我们的方法将KV缓存划分为固定大小的块，并采用循环门控模块来根据学习到的效用分数总结和过滤历史上下文。这种设计旨在保留最近的细粒度细节，同时积极地修剪陈旧的、低相关性的内存。实验表明，我们的方法平均可以节省24.6%的FLOPs，提高1.34倍的推理速度，并减少1.87倍的KV内存。我们的方法可以无缝集成到最新的VLA堆栈中，从而实现可扩展的推理，而无需修改下游控制逻辑。

## 🔬 方法详解

**问题定义**：VLA模型在处理长时程机器人任务时，需要存储大量的历史图像tokens作为上下文信息，导致KV缓存占用大量内存，推理速度慢，难以满足实时性要求。现有方法主要关注提升模型本身的泛化能力，而忽略了推理效率的优化。

**核心思路**：核心思想是通过一种轻量级的机制，选择性地保留高实用性的上下文信息，从而减少KV缓存的大小，降低计算复杂度，提高推理速度。该方法旨在在不显著影响模型性能的前提下，尽可能地压缩KV缓存。

**技术框架**：KV-Efficient VLA主要包含以下几个模块：1) KV缓存分块：将KV缓存划分为固定大小的块。2) RNN门控模块：使用循环神经网络（RNN）对每个KV缓存块进行编码，并学习一个效用分数，用于衡量该块的重要性。3) 上下文过滤：根据学习到的效用分数，选择性地保留高实用性的KV缓存块，丢弃低实用性的块。

**关键创新**：关键创新在于使用RNN门控机制来动态地评估和过滤KV缓存块。与传统的静态压缩方法相比，该方法能够根据上下文信息自适应地选择保留哪些信息，从而更好地平衡模型性能和推理效率。

**关键设计**：RNN门控模块的具体实现细节包括：RNN的类型（例如GRU或LSTM）、隐藏层大小、效用分数的计算方式（例如使用sigmoid函数将RNN的输出映射到0-1之间）以及选择保留的KV缓存块的比例。损失函数的设计需要考虑如何平衡模型性能和KV缓存压缩率。

## 📊 实验亮点

实验结果表明，KV-Efficient VLA在VLA模型上实现了显著的性能提升。具体来说，该方法平均节省了24.6%的FLOPs，提高了1.34倍的推理速度，并减少了1.87倍的KV内存占用。这些提升是在没有显著降低模型性能的前提下实现的，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可广泛应用于需要长时间上下文信息的机器人任务中，例如自主导航、长期规划和复杂操作。通过降低VLA模型的计算和内存需求，可以使其更容易部署在资源受限的机器人平台上，并提高其在真实世界环境中的实用性。此外，该方法也可以应用于其他基于Transformer的视觉语言模型，以提高其推理效率。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

