---
layout: default
title: "Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC"
---

# Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24045" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24045v1</a>
  <a href="https://arxiv.org/pdf/2506.24045.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24045v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24045v1', 'Agent.xpu: Efficient Scheduling of Agentic LLM Workloads on Heterogeneous SoC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinming Wei, Jiahao Zhang, Haoran Li, Jiayu Chen, Rui Qu, Maoliang Li, Xiang Chen, Guojie Luo

**分类**: cs.DC, cs.LG

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出Agent.xpu以高效调度异构SoC上的智能LLM工作负载**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `智能语言模型` `异构计算` `任务调度` `低延迟响应` `吞吐量优化`

## 📋 核心要点

1. 现有的设备端LLM引擎无法有效管理反应性和主动性任务的并发请求，导致性能瓶颈。
2. Agent.xpu通过构建异构执行图和在线调度器，优化了反应性和主动性任务的调度策略。
3. 在Intel Core Ultra SoC上，Agent.xpu在反应性任务上降低了4.6倍延迟，并在主动任务上提高了1.6到6.8倍的吞吐量。

## 📝 摘要（中文）

随着智能大型语言模型（LLM）在个人设备上的普及，出现了一类新工作负载，其特点是目标的二分性。用户发起的反应性任务需要即时、低延迟的响应，而主动任务则在后台运行，优先考虑吞吐量。现有的设备端LLM引擎设计用于孤立推理，无法有效管理这些在消费级异构系统芯片（SoC）上并发且相互冲突的请求。本文提出了Agent.xpu，一个高效的服务系统，旨在内存统一的异构SoC上处理智能LLM工作负载。通过专门的离线分析，Agent.xpu首先构建异构执行图，融合和分块模型内核，以实现基于亲和性的弹性加速器映射和预测内核注释。在运行时，其在线调度器支持细粒度的内核级抢占，以保证反应性任务的响应性。为了最大化SoC利用率，采用了基于松弛的内核回填策略，机会性地附加主动任务，并通过带宽感知调度来缓解NPU与iGPU之间的竞争。对Intel Core Ultra SoC的评估表明，Agent.xpu在反应性任务上实现了4.6倍的延迟降低，并在主动任务上维持了1.6到6.8倍的吞吐量提升。

## 🔬 方法详解

**问题定义**：本文旨在解决在消费级异构SoC上，智能LLM工作负载中反应性任务与主动性任务并发调度的效率问题。现有方法无法有效管理这类任务的冲突，导致响应性和吞吐量的下降。

**核心思路**：Agent.xpu的核心思想是通过构建异构执行图和实施细粒度的内核级抢占，来优化反应性和主动性任务的调度，从而提高系统的整体性能。

**技术框架**：Agent.xpu的整体架构包括离线分析模块、异构执行图构建模块、在线调度器和任务调度策略。离线分析用于生成执行图，在线调度器则负责动态调度任务。

**关键创新**：最重要的创新点在于引入了基于亲和性的弹性加速器映射和带宽感知调度策略，显著提升了反应性任务的响应性和主动性任务的吞吐量。

**关键设计**：在设计中，Agent.xpu采用了松弛感知的内核回填策略，并实现了在线调度器的细粒度内核级抢占，以确保反应性任务的及时响应。

## 📊 实验亮点

实验结果显示，Agent.xpu在反应性任务上实现了4.6倍的延迟降低，同时在主动任务上维持了1.6到6.8倍的吞吐量提升，显著优于现有的推理引擎，展示了其在实际应用中的强大性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能手机、边缘计算设备和其他个人智能设备，能够有效提升用户体验，尤其是在需要快速响应的应用场景中，如智能助手和实时翻译等。未来，Agent.xpu可能会推动更多智能应用的普及，提升设备的计算效率。

## 📄 摘要（原文）

> The proliferation of agentic Large Language Models (LLMs) on personal devices introduces a new class of workloads characterized by a dichotomy of objectives. Reactive tasks, initiated by users, demand immediate, low-latency responses, while proactive tasks operate invisibly and prioritize throughput. Existing on-device LLM engines, designed for isolated inferences, fail to efficiently manage these concurrent and conflicting requests on consumer-grade heterogeneous SoCs with CPU, integrated GPU, and NPU. This paper introduces Agent.xpu, an efficient serving system for agentic LLM workloads on memory-unified heterogeneous SoCs. With dedicated offline profiling, Agent.xpu first constructs a heterogeneous execution graph, which fuses and chunks model kernels for affinity-guided, elastic accelerator mapping with predictive kernel annotation. At runtime, its online scheduler enables fine-grained, kernel-level preemption to guarantee the responsiveness of reactive tasks. To maximize SoC utilization, it adopts slack-aware kernel backfill to opportunistically append proactive tasks, and mitigates NPU-iGPU contention via bandwidth-aware dispatch. Evaluation on an Intel Core Ultra SoC shows that Agent.xpu achieves 4.6$\times$ lower latency for reactive tasks and sustains 1.6$\times$-6.8$\times$ higher throughput for proactive tasks compared to state-of-the-art inference engines.

