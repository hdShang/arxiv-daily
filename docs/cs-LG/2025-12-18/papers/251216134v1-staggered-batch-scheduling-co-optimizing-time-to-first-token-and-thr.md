---
layout: default
title: Staggered Batch Scheduling: Co-optimizing Time-to-First-Token and Throughput for High-Efficiency LLM Inference
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

**关键词**: `大语言模型` `LLM推理` `分布式训练` `数据并行` `模型并行` `调度算法` `负载均衡` `首Token延迟`

## 📋 核心要点

1. DP+EP架构下LLM服务面临内部同步成本高、即时调度导致引擎内排队和并行化气泡的问题，严重影响首Token延迟。
2. 提出交错批调度(SBS)，通过缓冲请求形成最佳执行批次，消除内部排队气泡，并利用调度窗口进行负载均衡。
3. 在H800集群上，SBS将Deepseek-V3的TTFT降低30%-40%，吞吐量提高15%-20%，显著优于现有即时调度方法。

## 📝 摘要（中文）

针对大规模分布式架构（特别是P/D分离的DP+EP范式）下LLM服务面临的调度挑战，本文提出交错批调度(SBS)。与传统调度器将实例视为黑盒不同，DP+EP架构具有较高的内部同步成本。直接请求调度会导致严重的引擎内排队和并行化气泡，从而降低首Token延迟(TTFT)。SBS通过缓冲请求以形成最佳执行批次来解决此问题，这种时间解耦消除了内部排队气泡，且不影响吞吐量。此外，利用缓冲创建的调度窗口，引入负载感知全局分配策略，平衡Prefill和Decode阶段的DP单元上的计算负载。在服务Deepseek-V3的生产H800集群上部署，与最先进的即时调度基线相比，该系统将TTFT降低了30%-40%，吞吐量提高了15%-20%。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模分布式LLM服务中，特别是采用DP+EP架构时，由于高内部同步成本和即时调度策略导致的Time-to-First-Token (TTFT) 延迟过高以及吞吐量下降的问题。现有方法通常将LLM实例视为黑盒，忽略了DP+EP架构内部的复杂性，导致引擎内部出现排队和并行化气泡，降低了效率。

**核心思路**：论文的核心思路是通过引入时间上的解耦，即不立即调度请求，而是将请求缓冲一段时间，形成更优的执行批次。这种“交错”的批调度方式，能够有效地消除引擎内部的排队气泡，从而降低TTFT。同时，利用缓冲带来的调度窗口，可以进行全局的负载感知分配，进一步提升整体性能。

**技术框架**：整体框架包含两个主要部分：交错批调度(Staggered Batch Scheduling)和负载感知全局分配(Load-Aware Global Allocation)。首先，请求会被缓冲在一个队列中，等待形成合适的批次。然后，SBS会根据一定的策略选择合适的请求组成批次，并将其发送到DP单元进行处理。同时，利用缓冲窗口，LGA会根据各个DP单元的负载情况，动态地调整请求的分配，以实现负载均衡。Prefill和Decode阶段都采用LGA策略。

**关键创新**：论文的关键创新在于将时间维度引入到LLM的调度中，通过缓冲请求来优化批次形成，从而避免了即时调度带来的排队问题。此外，负载感知的全局分配策略，能够充分利用DP单元的计算资源，进一步提升整体性能。与现有方法的本质区别在于，SBS不再将LLM实例视为黑盒，而是充分考虑了DP+EP架构内部的同步成本和负载情况。

**关键设计**：关于关键设计，论文提到了负载感知全局分配策略。具体来说，LGA会监控各个DP单元的负载情况，并根据负载情况动态地调整请求的分配。具体的负载指标和分配策略在论文中可能没有详细展开，属于实现细节，但整体思路是尽量保证各个DP单元的负载均衡，避免出现某些单元过载而其他单元空闲的情况。具体的参数设置和损失函数等细节未知。

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

实验结果表明，在生产H800集群上服务Deepseek-V3时，与最先进的即时调度基线相比，SBS将首Token延迟(TTFT)降低了30%-40%，吞吐量提高了15%-20%。这些数据表明SBS在实际应用中具有显著的性能优势。

## 🎯 应用场景

该研究成果可广泛应用于大规模语言模型的在线服务场景，尤其是在采用DP+EP等分布式架构的系统中。通过降低首Token延迟和提高吞吐量，可以显著提升用户体验，并降低服务成本。未来，该方法可以进一步扩展到支持更多类型的LLM架构和更复杂的调度策略。

## 📄 摘要（原文）

> The evolution of Large Language Model (LLM) serving towards complex, distributed architectures--specifically the P/D-separated, large-scale DP+EP paradigm--introduces distinct scheduling challenges. Unlike traditional deployments where schedulers can treat instances as black boxes, DP+EP architectures exhibit high internal synchronization costs. We identify that immediate request dispatching in such systems leads to severe in-engine queuing and parallelization bubbles, degrading Time-to-First-Token (TTFT). To address this, we propose Staggered Batch Scheduling (SBS), a mechanism that deliberately buffers requests to form optimal execution batches. This temporal decoupling eliminates internal queuing bubbles without compromising throughput. Furthermore, leveraging the scheduling window created by buffering, we introduce a Load-Aware Global Allocation strategy that balances computational load across DP units for both Prefill and Decode phases. Deployed on a production H800 cluster serving Deepseek-V3, our system reduces TTFT by 30%-40% and improves throughput by 15%-20% compared to state-of-the-art immediate scheduling baselines.

