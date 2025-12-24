---
layout: default
title: "ClusterFusion: Expanding Operator Fusion Scope for LLM Inference via Cluster-Level Collective Primitive"
---

# ClusterFusion: Expanding Operator Fusion Scope for LLM Inference via Cluster-Level Collective Primitive

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18850" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18850v1</a>
  <a href="https://arxiv.org/pdf/2508.18850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18850v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18850v1', 'ClusterFusion: Expanding Operator Fusion Scope for LLM Inference via Cluster-Level Collective Primitive')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinhao Luo, Zihan Liu, Yangjie Zhou, Shihan Fang, Ziyu Huang, Yu Feng, Chen Zhang, Shixuan Sun, Zhenzhe Zheng, Jingwen Leng, Minyi Guo

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-26

**🔗 代码/项目**: [GITHUB](https://github.com/xinhao-luo/ClusterFusion)

---

## 💡 一句话要点

**提出ClusterFusion以解决LLM推理中的延迟问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理优化` `集群通信` `操作符融合` `深度学习框架` `高效计算` `内存管理`

## 📋 核心要点

1. 现有的LLM推理方法由于操作符执行碎片化和对外部内存的依赖，导致高延迟和性能瓶颈。
2. 本文提出ClusterReduce和ClusterGather两种集群级通信原语，优化集群内的数据交换和归约，进而设计ClusterFusion框架实现操作符融合。
3. 在H100 GPU上的实验结果表明，ClusterFusion在不同模型和配置下的端到端延迟平均提升了1.61倍，显著优于现有推理框架。

## 📝 摘要（中文）

大型语言模型（LLM）解码由于操作符之间的碎片化执行和对外部内存的重度依赖，导致高延迟。这种执行模型限制了融合的机会，并造成显著的内存流量和内核启动开销。尽管现代架构如NVIDIA Hopper提供了分布式共享内存和低延迟的集群内部互连，但它们仅暴露低级数据移动指令，缺乏结构化的集成通信抽象。为了解决这一软件与硬件之间的差距，本文提出了两种集群级通信原语ClusterReduce和ClusterGather，能够抽象常见的通信模式，实现集群内线程块之间的高效数据交换和归约。基于这些抽象，设计了ClusterFusion执行框架，通过将解码阶段如QKV投影、注意力机制和输出投影组合成单个融合内核，扩展了操作符融合的范围。H100 GPU上的评估显示，ClusterFusion在不同模型和配置下的端到端延迟平均提升了1.61倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型推理中的高延迟问题，现有方法因操作符执行的碎片化和对外部内存的重度依赖，导致性能下降和内存开销增加。

**核心思路**：通过引入ClusterReduce和ClusterGather两种集群级通信原语，本文实现了集群内线程块之间的高效数据交换和归约，从而减少对外部内存的依赖，提升了数据处理效率。

**技术框架**：ClusterFusion框架将通信与计算调度结合，允许将多个解码阶段（如QKV投影、注意力机制和输出投影）合并为单个融合内核，优化了执行流程。

**关键创新**：ClusterReduce和ClusterGather的提出是本文的核心创新，它们提供了高效的集群内通信抽象，显著提升了数据处理速度，并扩展了操作符融合的范围。

**关键设计**：在设计中，ClusterFusion框架通过优化内核调度和数据流动，减少了内存流量和内核启动开销，确保了中间结果能够在芯片内处理，避免了外部内存的干扰。

## 📊 实验亮点

在H100 GPU上的实验结果显示，ClusterFusion在不同模型和配置下的端到端延迟平均提升了1.61倍，显著优于现有的推理框架，展示了其在实际应用中的强大性能和优势。

## 🎯 应用场景

ClusterFusion的研究成果在大型语言模型推理、深度学习训练和实时数据处理等领域具有广泛的应用潜力。通过提升推理效率，该技术可以加速自然语言处理、机器翻译和对话系统等应用的响应速度，进而提升用户体验和系统性能。未来，该框架可能会推动更多高效的深度学习模型的开发与应用。

## 📄 摘要（原文）

> Large language model (LLM) decoding suffers from high latency due to fragmented execution across operators and heavy reliance on off-chip memory for data exchange and reduction. This execution model limits opportunities for fusion and incurs significant memory traffic and kernel launch overhead. While modern architectures such as NVIDIA Hopper provide distributed shared memory and low-latency intra-cluster interconnects, they expose only low-level data movement instructions, lacking structured abstractions for collective on-chip communication. To bridge this software-hardware gap, we introduce two cluster-level communication primitives, ClusterReduce and ClusterGather, which abstract common communication patterns and enable structured, high-speed data exchange and reduction between thread blocks within a cluster, allowing intermediate results to be on-chip without involving off-chip memory. Building on these abstractions, we design ClusterFusion, an execution framework that schedules communication and computation jointly to expand operator fusion scope by composing decoding stages such as QKV Projection, Attention, and Output Projection into a single fused kernels. Evaluations on H100 GPUs show that ClusterFusion outperforms state-of-the-art inference frameworks by 1.61x on average in end-to-end latency across different models and configurations. The source code is available at https://github.com/xinhao-luo/ClusterFusion.

