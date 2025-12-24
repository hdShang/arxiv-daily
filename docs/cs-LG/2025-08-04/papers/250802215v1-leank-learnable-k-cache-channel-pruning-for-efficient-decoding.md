---
layout: default
title: "LeanK: Learnable K Cache Channel Pruning for Efficient Decoding"
---

# LeanK: Learnable K Cache Channel Pruning for Efficient Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02215" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02215v1</a>
  <a href="https://arxiv.org/pdf/2508.02215.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02215v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02215v1', 'LeanK: Learnable K Cache Channel Pruning for Efficient Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yike Zhang, Zhiyuan He, Huiqiang Jiang, Chengruidong Zhang, Yuqing Yang, Jianyong Wang, Lili Qiu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出LeanK以解决大语言模型解码效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文处理` `键值缓存` `通道稀疏性` `解码优化` `大语言模型`

## 📋 核心要点

1. 现有的大语言模型在处理长上下文时，因键值缓存的增长而面临显著的效率问题。
2. LeanK通过学习不重要的键缓存通道，利用静态通道稀疏性来优化解码过程。
3. 实验表明，LeanK能够实现K缓存最多减少70%，并加速注意力计算1.3倍，且不影响模型准确性。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理长上下文任务时面临效率挑战，尤其是随着键值（KV）缓存的增长。本文提出LeanK，一种基于学习的方法，通过利用静态通道稀疏性来修剪不重要的键（K）缓存通道。LeanK采用新颖的两阶段训练过程，学习通道级静态掩码，以满足特定的稀疏率和硬件对齐要求。LeanK在不牺牲准确性的情况下，减少了GPU内存并加速了解码过程。实验结果表明，K缓存减少了多达70%，V缓存减少了16%-18%。定制解码内核使得注意力计算加速达到1.3倍。我们还通过分析学习到的重要性分布，提供了对长上下文推理中模型通道和注意力头的深入见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长上下文任务中因键值缓存增长导致的解码效率低下问题。现有方法在处理大规模数据时，往往无法有效利用内存和计算资源，导致性能瓶颈。

**核心思路**：LeanK的核心思路是通过学习不重要的键缓存通道，利用静态通道稀疏性来优化解码过程。通过这种方式，LeanK能够在保持模型准确性的同时，显著减少内存占用和加速计算。

**技术框架**：LeanK的整体架构包括两个主要阶段：第一阶段是学习通道级静态掩码，以满足特定的稀疏率；第二阶段是根据学习到的掩码进行解码优化。该方法结合了静态通道稀疏性与硬件对齐需求，确保了高效的资源利用。

**关键创新**：LeanK的主要创新在于其学习机制，通过静态掩码的方式实现了通道的有效修剪。这一方法与传统的手动稀疏化方法相比，能够更灵活地适应不同的硬件环境和任务需求。

**关键设计**：在设计上，LeanK采用了特定的损失函数来优化通道掩码的学习过程，并在网络结构中引入了定制的解码内核，以提升注意力计算的效率。

## 📊 实验亮点

实验结果显示，LeanK在K缓存方面实现了最高70%的内存减少，同时V缓存也减少了16%-18%。此外，定制的解码内核使得注意力计算速度提升了1.3倍，显著提高了模型的解码效率。

## 🎯 应用场景

LeanK的研究成果在多个领域具有潜在应用价值，尤其是在需要处理长文本或长序列数据的自然语言处理任务中。通过提高解码效率，LeanK能够帮助开发更高效的对话系统、文本生成模型和机器翻译系统，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Large language models (LLMs) enable long-context tasks but face efficiency challenges due to the growing key-value (KV) cache. We propose LeanK, a learning-based method that prunes unimportant key (K) cache channels by leveraging static channel sparsity. With a novel two-stage training process, LeanK learns channel-wise static mask that could satisfy specific sparsity ratio and hardware alignment requirement. LeanK reduces GPU memory and accelerates decoding without sacrificing accuracy. Experiments demonstrate up to 70% K cache and 16%-18% V cache memory reduction. Custom decoding kernel enables 1.3x speedup for attention computation. We also provide insights into model channels and attention heads during long-context inference by analyzing the learned importance distribution. Our code is available at https://aka.ms/LeanK.

