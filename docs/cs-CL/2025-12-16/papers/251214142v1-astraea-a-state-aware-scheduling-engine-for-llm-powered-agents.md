---
layout: default
title: "Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents"
---

# Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14142" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14142v1</a>
  <a href="https://arxiv.org/pdf/2512.14142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14142v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14142v1', 'Astraea: A State-Aware Scheduling Engine for LLM-Powered Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongqiu Ni, Jiabao Zhang, Guopeng Li, Zilong Wang, Ruiqi Wu, Chi Zhang, Haisheng Tan

**分类**: cs.CL

**发布日期**: 2025-12-16

**备注**: 12 pages, 8 figures

---

## 💡 一句话要点

**Astraea：面向LLM智能体的状态感知调度引擎，优化端到端延迟**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM智能体` `调度引擎` `状态感知` `作业完成时间` `分层调度`

## 📋 核心要点

1. 现有LLM智能体推理系统侧重于局部优化，忽略了全局作业完成时间（JCT），导致端到端延迟较高。
2. Astraea通过状态感知的分层调度算法，结合请求历史状态和未来预测，动态分类请求并优化全局JCT。
3. 实验表明，Astraea相比基线方法，平均JCT降低高达25.5%，并在高负载下表现出强大的鲁棒性和稳定性。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被部署为智能代理。它们的多阶段工作流程在本地计算和调用Web API等外部网络服务之间交替，这导致它们的执行模式与现有推理系统（如vLLM）的调度粒度不匹配。现有系统通常侧重于每个片段的优化，这妨碍了它们最小化完整代理工作流程的端到端延迟，即整个请求生命周期内的全局作业完成时间（JCT）。为了解决这个限制，我们提出了Astraea，一种旨在将优化从本地片段转移到全局请求生命周期的服务引擎。Astraea采用了一种状态感知的分层调度算法，该算法将请求的历史状态与未来预测相结合。它根据请求的I/O和计算密集型特性动态地对请求进行分类，并使用增强的HRRN策略来平衡效率和公平性。Astraea还实现了一个自适应KV缓存管理器，该管理器根据系统内存压力智能地处理I/O等待期间的代理状态。大量实验表明，与基线方法相比，Astraea将平均JCT降低了高达25.5%。此外，我们的方法在各种模型规模的高负载下表现出强大的鲁棒性和稳定性。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM智能体在多阶段工作流程中，由于本地计算和外部网络服务调用交替，导致现有推理系统无法有效优化全局作业完成时间（JCT）的问题。现有系统通常只关注单个片段的优化，而忽略了整个请求生命周期的端到端延迟，造成资源利用率低下和用户体验下降。

**核心思路**：Astraea的核心思路是将优化目标从局部片段转移到全局请求生命周期。通过状态感知的分层调度算法，Astraea能够根据请求的历史状态和未来预测，动态地调整调度策略，从而最小化全局JCT。这种方法能够更好地适应LLM智能体的工作负载特性，提高整体效率。

**技术框架**：Astraea的整体架构包含以下主要模块：1) 请求分类器：根据请求的I/O和计算密集程度进行动态分类。2) 分层调度器：采用状态感知的分层调度算法，结合请求历史状态和未来预测进行调度。3) 自适应KV缓存管理器：根据系统内存压力，智能地管理I/O等待期间的代理状态。整个流程如下：请求到达后，首先由请求分类器进行分类，然后由分层调度器根据分类结果和系统状态进行调度，最后由自适应KV缓存管理器负责管理缓存。

**关键创新**：Astraea的关键创新在于其状态感知的分层调度算法和自适应KV缓存管理器。状态感知的调度算法能够根据请求的历史状态和未来预测，动态地调整调度策略，从而更好地适应LLM智能体的工作负载特性。自适应KV缓存管理器能够根据系统内存压力，智能地管理I/O等待期间的代理状态，从而提高资源利用率。与现有方法相比，Astraea能够更有效地优化全局JCT，提高整体效率。

**关键设计**：Astraea的关键设计包括：1) 增强的HRRN（Highest Response Ratio Next）调度策略，用于平衡效率和公平性。2) 基于系统内存压力的自适应KV缓存管理策略，用于智能地管理I/O等待期间的代理状态。3) 请求分类器的设计，用于根据请求的I/O和计算密集程度进行动态分类。具体的参数设置和损失函数等技术细节在论文中未明确给出，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14142v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Astraea相比于基线方法，平均作业完成时间（JCT）降低了高达25.5%。此外，Astraea在各种模型规模的高负载下表现出强大的鲁棒性和稳定性，证明了其在实际应用中的可行性和有效性。这些结果表明Astraea能够显著提升LLM智能体的性能。

## 🎯 应用场景

Astraea适用于各种需要LLM智能体进行多阶段工作流程处理的场景，例如智能客服、自动化报告生成、智能文档处理等。通过优化端到端延迟，Astraea可以显著提升用户体验，提高工作效率，并降低计算成本。未来，Astraea可以进一步扩展到支持更多类型的LLM智能体和更复杂的应用场景。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly being deployed as intelligent agents. Their multi-stage workflows, which alternate between local computation and calls to external network services like Web APIs, introduce a mismatch in their execution pattern and the scheduling granularity of existing inference systems such as vLLM. Existing systems typically focus on per-segment optimization which prevents them from minimizing the end-to-end latency of the complete agentic workflow, i.e., the global Job Completion Time (JCT) over the entire request lifecycle. To address this limitation, we propose Astraea, a service engine designed to shift the optimization from local segments to the global request lifecycle. Astraea employs a state-aware, hierarchical scheduling algorithm that integrates a request's historical state with future predictions. It dynamically classifies requests by their I/O and compute intensive nature and uses an enhanced HRRN policy to balance efficiency and fairness. Astraea also implements an adaptive KV cache manager that intelligently handles the agent state during I/O waits based on the system memory pressure. Extensive experiments show that Astraea reduces average JCT by up to 25.5\% compared to baseline methods. Moreover, our approach demonstrates strong robustness and stability under high load across various model scales.

