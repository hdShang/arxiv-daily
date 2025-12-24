---
layout: default
title: "Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference"
---

# Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16134" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16134v1</a>
  <a href="https://arxiv.org/pdf/2512.16134.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16134v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16134v1', 'Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Tian, Shuailong Li, Yang Cao, Wenbo Cui, Minghan Zhu, Wenkang Wu, Jianming Zhang, Yanpeng Wang, Zhiwen Xiao, Zhenyu Hou, Dou Shen

**分类**: cs.DC, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出交错批调度(SBS)，优化DP+EP架构下LLM推理的首Token延迟和吞吐量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型推理` `分布式系统` `调度算法` `首Token延迟` `吞吐量优化`

## 📋 核心要点

1. DP+EP架构下LLM服务中，立即调度请求导致引擎内排队和并行化气泡，严重影响首Token延迟。
2. 提出交错批调度（SBS），通过缓冲请求形成最佳批次，消除内部排队气泡，并利用调度窗口进行负载均衡。
3. 在生产H800集群上，SBS将TTFT降低30%-40%，吞吐量提高15%-20%，显著优于现有调度方法。

## 📝 摘要（中文）

针对大规模分布式架构（特别是P/D分离的DP+EP范式）下LLM服务面临的调度挑战，本文提出交错批调度（Staggered Batch Scheduling, SBS）。与传统调度器将实例视为黑盒不同，DP+EP架构具有较高的内部同步成本。研究发现，在此类系统中立即调度请求会导致严重的引擎内排队和并行化气泡，从而降低首Token延迟（TTFT）。SBS通过有意缓冲请求以形成最佳执行批次来解决此问题，这种时间解耦消除了内部排队气泡，且不影响吞吐量。此外，利用缓冲创建的调度窗口，引入负载感知全局分配策略，以平衡Prefill和Decode阶段跨DP单元的计算负载。在服务Deepseek-V3的生产H800集群上部署后，与最先进的立即调度基线相比，该系统将TTFT降低了30%-40%，并将吞吐量提高了15%-20%。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模分布式LLM服务中，特别是采用DP+EP架构时，由于高内部同步成本导致的调度效率低下问题。现有立即调度方法在DP+EP架构下会产生严重的引擎内排队和并行化气泡，导致首Token延迟（TTFT）增加，影响用户体验。同时，简单的增加batch size又会影响TTFT。

**核心思路**：论文的核心思路是通过时间解耦的方式，即交错批调度（SBS），来优化请求的调度。SBS并非立即调度请求，而是有意识地缓冲请求，形成更优的执行批次。这种缓冲创造了一个调度窗口，允许进行全局负载感知的资源分配，从而平衡不同DP单元上的计算负载，最终降低TTFT并提高吞吐量。

**技术框架**：SBS包含两个主要阶段：请求缓冲和全局负载感知分配。首先，请求被缓冲在一个调度队列中，等待形成合适的批次。然后，利用缓冲窗口，采用负载感知的全局分配策略，将批次分配到不同的DP单元上。该策略考虑了Prefill和Decode阶段的计算负载，力求在各个DP单元之间实现负载均衡，避免出现资源闲置或拥塞。

**关键创新**：论文的关键创新在于将时间维度引入LLM推理调度中。传统的调度方法通常是基于即时可用资源进行调度，而SBS则通过缓冲请求，创造了一个时间窗口，从而能够进行更全局的优化。这种时间解耦的思想是与现有方法的本质区别。

**关键设计**：SBS的关键设计包括：1) 缓冲队列的长度，需要根据实际负载和系统资源进行调整，以平衡TTFT和吞吐量；2) 负载感知的全局分配策略，需要精确估计Prefill和Decode阶段的计算负载，并根据DP单元的计算能力进行合理分配；3) 调度窗口大小的确定，需要在TTFT和调度优化空间之间进行权衡。论文中可能还涉及一些具体的负载预测模型或启发式算法，用于实现负载均衡。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/schedule_unit_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/schedule_unit_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16134v1/figures/queue_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在服务Deepseek-V3的生产H800集群上，与最先进的立即调度基线相比，SBS将首Token延迟（TTFT）降低了30%-40%，并将吞吐量提高了15%-20%。这些数据表明SBS在实际应用中具有显著的性能优势。

## 🎯 应用场景

该研究成果可广泛应用于大规模语言模型的在线推理服务，特别是在需要高并发、低延迟的场景下，例如智能客服、AI助手、搜索引擎等。通过优化调度策略，可以显著提升用户体验，并提高计算资源的利用率，降低运营成本。未来，该方法可以进一步扩展到其他类型的AI模型和服务中。

## 📄 摘要（原文）

> The evolution of Large Language Model (LLM) serving towards complex, distributed architectures--specifically the P/D-separated, large-scale DP+EP paradigm--introduces distinct scheduling challenges. Unlike traditional deployments where schedulers can treat instances as black boxes, DP+EP architectures exhibit high internal synchronization costs. We identify that immediate request dispatching in such systems leads to severe in-engine queuing and parallelization bubbles, degrading Time-to-First-Token (TTFT). To address this, we propose Staggered Batch Scheduling (SBS), a mechanism that deliberately buffers requests to form optimal execution batches. This temporal decoupling eliminates internal queuing bubbles without compromising throughput. Furthermore, leveraging the scheduling window created by buffering, we introduce a Load-Aware Global Allocation strategy that balances computational load across DP units for both Prefill and Decode phases. Deployed on a production H800 cluster serving Deepseek-V3, our system reduces TTFT by 30%-40% and improves throughput by 15%-20% compared to state-of-the-art immediate scheduling baselines.

