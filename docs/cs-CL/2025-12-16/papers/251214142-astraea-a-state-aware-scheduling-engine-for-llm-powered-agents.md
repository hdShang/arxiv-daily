---
layout: default
title: Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents
---

# Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14142" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14142</a>
  <a href="https://arxiv.org/pdf/2512.14142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14142" onclick="toggleFavorite(this, '2512.14142', 'Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongqiu Ni, Jiabao Zhang, Guopeng Li, Zilong Wang, Ruiqi Wu, Chi Zhang, Haisheng Tan

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Astraea：面向LLM智能体的状态感知调度引擎，优化端到端延迟**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM智能体` `状态感知调度` `全局优化` `作业完成时间` `KV缓存管理`

## 📋 核心要点

1. 现有LLM推理系统侧重于片段优化，忽略了智能体工作流的全局作业完成时间（JCT），导致端到端延迟较高。
2. Astraea通过状态感知的分层调度算法，结合请求历史状态和未来预测，动态分类请求并优化全局JCT。
3. 实验表明，Astraea相比基线方法，平均JCT降低高达25.5%，并在高负载下表现出强大的鲁棒性和稳定性。

## 📝 摘要（中文）

大型语言模型（LLM）越来越多地被部署为智能代理。它们的多阶段工作流程在本地计算和诸如Web API之类的外部网络服务调用之间交替，这导致它们的执行模式与现有推理系统（如vLLM）的调度粒度不匹配。现有系统通常侧重于每个片段的优化，这阻碍了它们最小化完整代理工作流程的端到端延迟，即整个请求生命周期内的全局作业完成时间（JCT）。为了解决这个限制，我们提出了Astraea，一种旨在将优化从本地片段转移到全局请求生命周期的服务引擎。Astraea采用了一种状态感知的分层调度算法，该算法将请求的历史状态与未来预测相结合。它根据请求的I/O和计算密集程度动态地对请求进行分类，并使用增强的HRRN策略来平衡效率和公平性。Astraea还实现了一个自适应KV缓存管理器，该管理器根据系统内存压力智能地处理I/O等待期间的代理状态。大量的实验表明，与基线方法相比，Astraea将平均JCT降低了高达25.5％。此外，我们的方法在各种模型规模的高负载下表现出强大的鲁棒性和稳定性。

## 🔬 方法详解

**问题定义**：现有LLM智能体推理系统，如vLLM，主要关注单个推理片段的优化，而忽略了智能体工作流中多个阶段之间的依赖关系和整体执行效率。这导致在处理包含I/O密集型任务（例如，调用Web API）的复杂智能体任务时，全局作业完成时间（JCT）较长，用户体验不佳。现有方法的痛点在于缺乏对请求状态的感知和全局调度优化。

**核心思路**：Astraea的核心思路是将优化目标从局部片段转移到全局请求生命周期。通过引入状态感知的调度机制，Astraea能够根据请求的历史状态（例如，已完成的计算量、I/O等待时间）和未来预测（例如，预计的计算量、I/O请求）来动态调整调度策略，从而最小化全局JCT。这种全局优化能够更好地平衡计算和I/O资源，提高整体效率。

**技术框架**：Astraea的整体架构包含以下主要模块：1) **状态跟踪器**：负责记录每个请求的历史状态信息，包括已完成的计算量、I/O等待时间等。2) **请求分类器**：根据请求的状态信息和未来预测，将请求动态地分类为I/O密集型或计算密集型。3) **分层调度器**：采用分层调度算法，根据请求的类型和优先级进行调度。顶层调度器负责全局资源分配，底层调度器负责单个计算节点的任务调度。4) **自适应KV缓存管理器**：在I/O等待期间，根据系统内存压力智能地管理代理状态，避免不必要的内存占用。

**关键创新**：Astraea最重要的技术创新点在于其状态感知的分层调度算法。与传统的基于片段的调度方法不同，Astraea能够感知请求的全局状态，并根据状态信息动态调整调度策略。此外，Astraea还引入了自适应KV缓存管理器，能够有效地管理I/O等待期间的代理状态，进一步提高资源利用率。

**关键设计**：Astraea的关键设计包括：1) **增强的HRRN（Highest Response Ratio Next）策略**：在调度过程中，Astraea使用增强的HRRN策略来平衡效率和公平性。HRRN策略会考虑请求的等待时间和预计的服务时间，优先调度响应比最高的请求。2) **自适应KV缓存管理**：Astraea根据系统内存压力动态调整KV缓存的大小，避免内存溢出。3) **请求分类阈值**：请求分类器使用阈值来区分I/O密集型和计算密集型请求。阈值的设置会影响调度策略的选择，需要根据实际应用场景进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Astraea相比于基线方法，平均作业完成时间（JCT）降低了高达25.5%。此外，在高负载情况下，Astraea表现出强大的鲁棒性和稳定性，能够有效地处理大量的并发请求。实验还验证了Astraea在不同模型规模下的有效性，表明其具有良好的可扩展性。

## 🎯 应用场景

Astraea适用于各种需要LLM作为智能代理的场景，例如智能客服、自动化报告生成、智能家居控制等。通过优化端到端延迟，Astraea可以显著提升用户体验，并提高系统的整体效率。未来，Astraea可以进一步扩展到支持更复杂的智能体工作流，并与其他推理优化技术相结合，以实现更高的性能。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly being deployed as intelligent agents. Their multi-stage workflows, which alternate between local computation and calls to external network services like Web APIs, introduce a mismatch in their execution pattern and the scheduling granularity of existing inference systems such as vLLM. Existing systems typically focus on per-segment optimization which prevents them from minimizing the end-to-end latency of the complete agentic workflow, i.e., the global Job Completion Time (JCT) over the entire request lifecycle. To address this limitation, we propose Astraea, a service engine designed to shift the optimization from local segments to the global request lifecycle. Astraea employs a state-aware, hierarchical scheduling algorithm that integrates a request's historical state with future predictions. It dynamically classifies requests by their I/O and compute intensive nature and uses an enhanced HRRN policy to balance efficiency and fairness. Astraea also implements an adaptive KV cache manager that intelligently handles the agent state during I/O waits based on the system memory pressure. Extensive experiments show that Astraea reduces average JCT by up to 25.5\% compared to baseline methods. Moreover, our approach demonstrates strong robustness and stability under high load across various model scales.

