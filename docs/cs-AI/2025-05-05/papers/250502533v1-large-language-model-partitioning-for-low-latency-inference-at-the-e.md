---
layout: default
title: Large Language Model Partitioning for Low-Latency Inference at the Edge
---

# Large Language Model Partitioning for Low-Latency Inference at the Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02533" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02533v1</a>
  <a href="https://arxiv.org/pdf/2505.02533.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02533v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02533v1', 'Large Language Model Partitioning for Low-Latency Inference at the Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dimitrios Kafetzis, Ramin Khalili, Iordanis Koutsopoulos

**分类**: cs.DC, cs.AI

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出资源感知的Transformer分区算法以降低边缘推理延迟**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `边缘计算` `Transformer` `推理优化` `动态分区` `注意力机制` `资源管理`

## 📋 核心要点

1. 现有的基于层的分区方法在边缘环境中容易导致内存过载和高推理延迟，难以满足实时应用需求。
2. 本文提出了一种资源感知的Transformer分区算法，通过在标记生成过程中动态更新分区决策，优化资源利用。
3. 实验结果显示，该方法在小规模设备上实现了接近最优解的延迟，并在大规模测试中显著提高了推理速度和内存效率。

## 📝 摘要（中文）

大型语言模型（LLMs）基于自回归的解码器Transformer逐个生成文本标记，随着生成的标记数量增加，内存和计算负载也随之上升。现有的基于层的分区方法在资源受限的边缘环境中常常导致内存过载或高推理延迟。为了解决这一问题，本文提出了一种资源感知的Transformer架构分区算法，该算法在标记生成过程中定期更新分区决策。通过在注意力头级别进行分区，允许动态迁移，显著降低推理延迟。实验结果表明，在小规模设置下，该方法的延迟在最优解的15%到20%之内，并在大规模测试中相比于现有的分层分区方法显著提高了推理速度和内存使用效率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在边缘设备上推理时的内存过载和高延迟问题。现有的层级分区方法在资源受限环境中表现不佳，无法有效应对动态变化的资源需求。

**核心思路**：提出了一种基于即时设备资源可用性和网络带宽的动态分区算法，通过在注意力头级别进行分区，允许在资源紧张时进行动态迁移，以降低推理延迟。

**技术框架**：整体架构包括分区决策模块、动态迁移模块和推理执行模块。分区决策模块定期评估设备资源，动态调整注意力头的分配，迁移模块负责在设备间迁移计算负载，推理执行模块则负责实际的推理过程。

**关键创新**：最重要的创新在于在注意力头级别进行分区，并允许动态迁移，这与传统的层级分区方法有本质区别，能够更灵活地应对资源变化。

**关键设计**：算法在初次执行时将注意力头分配到不同设备，后续执行中根据资源情况调整分配，确保迁移延迟和推理延迟之和保持在较低水平。

## 📊 实验亮点

实验结果表明，在小规模设置（3-5个设备）下，提出的方法的推理延迟在最优解的15%到20%之间，而在大规模测试中，相比于现有的分层分区方法，推理速度和内存使用效率显著提高，展示了该方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括边缘计算、移动设备上的自然语言处理和实时智能助手等场景。通过降低推理延迟和内存使用，该方法能够提升用户体验，支持更复杂的实时应用，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) based on autoregressive, decoder-only Transformers generate text one token at a time, where a token represents a discrete unit of text. As each newly produced token is appended to the partial output sequence, the length grows and so does the memory and compute load, due to the expanding key-value caches, which store intermediate representations of all previously generated tokens in the multi-head attention (MHA) layer. As this iterative process steadily increases memory and compute demands, layer-based partitioning in resource-constrained edge environments often results in memory overload or high inference latency. To address this and reduce inference latency, we propose a resource-aware Transformer architecture partitioning algorithm, where the partitioning decision is updated at regular intervals during token generation. The approach is myopic in that it is based on instantaneous information about device resource availability and network link bandwidths. When first executed, the algorithm places blocks on devices, and in later executions, it migrates these blocks among devices so that the sum of migration delay and inference delay remains low. Our approach partitions the decoder at the attention head level, co-locating each attention head with its key-value cache and allowing dynamic migrations whenever resources become tight. By allocating different attention heads to different devices, we exploit parallel execution of attention heads and thus achieve substantial reductions in inference delays. Our experiments show that in small-scale settings (3-5 devices), the proposed method achieves within 15 to 20 percent of an exact optimal solver's latency, while in larger-scale tests it achieves notable improvements in inference speed and memory usage compared to state-of-the-art layer-based partitioning approaches.

