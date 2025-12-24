---
layout: default
title: "FlexLink: Boosting your NVLink Bandwidth by 27% without accuracy concern"
---

# FlexLink: Boosting your NVLink Bandwidth by 27% without accuracy concern

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15882" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15882v1</a>
  <a href="https://arxiv.org/pdf/2510.15882.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15882v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15882v1', 'FlexLink: Boosting your NVLink Bandwidth by 27% without accuracy concern')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ao Shen, Rui Zhang, Junping Zhao

**分类**: cs.AR, cs.AI, cs.DC, cs.LG

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出FlexLink以提升NVLink带宽27%解决通信瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `集体通信` `异构互连` `负载均衡` `大规模训练` `高性能计算`

## 📋 核心要点

1. 现有的通信库如NCCL仅依赖单一互连方式，导致在多节点部署时性能瓶颈明显，特别是在高负载情况下。
2. FlexLink通过聚合NVLink、PCIe和RDMA NIC等异构链接，采用两阶段自适应负载均衡策略，优化通信流量分配。
3. 在8-GPU H800服务器上，FlexLink使得AllReduce和AllGather的带宽分别提升了26%和27%，有效利用了闲置的硬件资源。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的不断扩展，多节点部署已成为必要。因此，通信成为了关键的性能瓶颈。目前的节点内通信库，如NCCL，通常仅使用单一的互连方式，如NVLink。这种方法在H800 GPU等硬件上造成了性能上限，尤其是当主要互连的带宽成为瓶颈时，其他硬件资源如PCIe和支持远程直接内存访问（RDMA）的网络接口卡（NIC）在高负载下大多处于闲置状态。我们提出了FlexLink，这是第一个旨在系统性解决这一问题的集体通信框架，通过将这些异构链接（NVLink、PCIe和RDMA NIC）聚合成一个高性能的通信结构。FlexLink采用有效的两阶段自适应负载均衡策略，动态分配通信流量，确保更快的互连不会被较慢的互连所限制。在8-GPU H800服务器上，我们的设计使得集体操作如AllReduce和AllGather的带宽分别提高了26%和27%。这一提升是通过将2-22%的总通信流量转移到之前未充分利用的PCIe和RDMA NIC上实现的。FlexLink作为无损的、与NCCL API兼容的替代方案，确保了易于采用。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是当前通信库在多节点部署中的性能瓶颈，尤其是当主要互连的带宽成为限制因素时，其他硬件资源未被充分利用。

**核心思路**：论文的核心解决思路是通过聚合多种异构互连（NVLink、PCIe和RDMA NIC），并采用自适应负载均衡策略，动态分配通信流量，以提高整体带宽。

**技术框架**：整体架构包括三个主要模块：异构链接聚合模块、两阶段负载均衡模块和通信流量调度模块。异构链接聚合模块负责整合不同类型的互连，负载均衡模块则根据实时流量情况调整各个链接的负载，最后调度模块确保数据在各个链接间高效传输。

**关键创新**：最重要的技术创新点在于首次提出了将多种异构互连聚合为一个高性能通信结构的框架，并通过自适应策略避免了较慢互连对整体性能的拖累。

**关键设计**：关键设计包括动态流量监控和实时负载均衡算法，确保在不同负载情况下能够灵活调整流量分配，最大化利用所有可用的互连资源。

## 📊 实验亮点

实验结果显示，FlexLink在8-GPU H800服务器上，AllReduce和AllGather的带宽分别提高了26%和27%。这一提升是通过将2-22%的通信流量转移到未充分利用的PCIe和RDMA NIC上实现的，展现了显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括大规模分布式训练、云计算平台和高性能计算（HPC）等场景。通过提升通信效率，FlexLink能够显著加速模型训练过程，降低资源消耗，提升系统整体性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> As large language models (LLMs) continue to scale, multi-node deployment has become a necessity. Consequently, communication has become a critical performance bottleneck. Current intra-node communication libraries, like NCCL, typically make use of a single interconnect such as NVLink. This approach creates performance ceilings, especially on hardware like the H800 GPU where the primary interconnect's bandwidth can become a bottleneck, and leaves other hardware resources like PCIe and Remote Direct Memory Access (RDMA)-capable Network Interface Cards (NICs) largely idle during intensive workloads. We propose FlexLink, the first collective communication framework to the best of our knowledge designed to systematically address this by aggregating these heterogeneous links-NVLink, PCIe, and RDMA NICs-into a single, high-performance communication fabric. FlexLink employs an effective two-stage adaptive load balancing strategy that dynamically partitions communication traffic across all available links, ensuring that faster interconnects are not throttled by slower ones. On an 8-GPU H800 server, our design improves the bandwidth of collective operators such as AllReduce and AllGather by up to 26% and 27% over the NCCL baseline, respectively. This gain is achieved by offloading 2-22% of the total communication traffic to the previously underutilized PCIe and RDMA NICs. FlexLink provides these improvements as a lossless, drop-in replacement compatible with the NCCL API, ensuring easy adoption.

