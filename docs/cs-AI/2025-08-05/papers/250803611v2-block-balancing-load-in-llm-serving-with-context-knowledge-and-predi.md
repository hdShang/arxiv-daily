---
layout: default
title: "Block: Balancing Load in LLM Serving with Context, Knowledge and Predictive Scheduling"
---

# Block: Balancing Load in LLM Serving with Context, Knowledge and Predictive Scheduling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03611" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03611v2</a>
  <a href="https://arxiv.org/pdf/2508.03611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03611v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03611v2', 'Block: Balancing Load in LLM Serving with Context, Knowledge and Predictive Scheduling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Da, Evangelia Kalyvianaki

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-08-13)

**备注**: 12 pages, 8 figures excluding appendix. V1: Fix some typos and grammar issue

---

## 💡 一句话要点

**提出Block框架以优化大语言模型服务中的负载均衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `负载均衡` `大语言模型` `分布式调度` `预测性调度` `自动配置` `性能优化` `开源`

## 📋 核心要点

1. 现有的模型服务系统通常依赖单体和启发式调度器，导致负载均衡和资源利用效率低下。
2. Block框架通过分布式、无状态和预测性调度，利用请求的上下文信息来优化调度决策。
3. 在实验中，Block在12个GPU集群上提升了服务能力16.7%，并将P99尾延迟降低了49.5%。

## 📝 摘要（中文）

本文提出了Block，一个分布式调度框架，旨在通过利用来自请求的上下文信息来优化大语言模型（LLM）服务中的负载均衡和自动配置。与依赖单体和启发式任务调度器的流行模型服务系统不同，Block作为一个完全分布式、无状态和预测性的调度系统，旨在实现低开销、可靠性和可扩展性。它利用LLM推理的确定性和可预测特性，如主机配置、响应长度和硬件性能，基于准确预测的指标做出调度决策。在12个GPU集群上的评估表明，Block显著优于启发式调度器，服务能力提升高达16.7%，P99尾延迟降低高达49.5%。这些性能提升在不同模型、工作负载和配置中保持一致。代码和数据已开源。

## 🔬 方法详解

**问题定义**：本文解决的是在大语言模型服务中，现有调度方法的负载均衡和资源配置效率低下的问题。现有方法多依赖启发式调度，无法充分利用上下文信息。

**核心思路**：Block框架的核心思想是通过分布式和预测性调度，利用请求的上下文信息和LLM推理的可预测特性，来优化调度决策，从而提高服务效率和降低延迟。

**技术框架**：Block的整体架构包括请求上下文分析模块、预测调度模块和负载均衡模块。请求上下文分析模块负责提取请求特征，预测调度模块基于历史数据和当前上下文进行调度决策，负载均衡模块则确保资源的合理分配。

**关键创新**：Block的主要创新在于其完全分布式和无状态的设计，使得调度过程更加灵活和高效。与传统的单体调度器相比，Block能够实时响应请求变化，显著提高了系统的可扩展性和可靠性。

**关键设计**：在设计中，Block采用了基于上下文的调度策略，结合了主机配置、响应长度和硬件性能等因素进行调度决策。关键参数的设置和损失函数的设计也经过精心调整，以确保调度的准确性和效率。

## 📊 实验亮点

实验结果显示，Block框架在12个GPU集群上显著提升了服务能力，最高可达16.7%的增幅，同时将P99尾延迟降低了49.5%。这些结果表明Block在不同模型和工作负载下均表现出色，具有良好的通用性和适应性。

## 🎯 应用场景

Block框架在大语言模型服务中具有广泛的应用潜力，尤其适用于需要高效负载均衡和低延迟响应的场景，如在线客服、智能助手和内容生成等。其开源特性也为研究人员和开发者提供了便利，促进了相关技术的进一步发展和应用。

## 📄 摘要（原文）

> This paper presents Block, a distributed scheduling framework designed to optimize load balancing and auto-provisioning across instances in large language model serving frameworks by leveraging contextual information from incoming requests. Unlike popular model serving systems that rely on monolithic and heuristic task schedulers, Block operates as a fully distributed, stateless, and predictive scheduling system to achieve low overhead, reliability, and scalability. It leverages the deterministic and predictable characteristics of LLM inferences, such as host configurations, response lengths, and hardware performance, to make scheduling decisions based on accurately predicted metrics. Evaluation on a 12 GPUs cluster shows that Block significantly outperforms heuristic schedulers, boosting serving capacity by up to 16.7\% and reducing P99 tail latency by up to 49.5\%. These performance gains remain consistent across diverse models, workloads and configurations. Code and data are open-sourced.

