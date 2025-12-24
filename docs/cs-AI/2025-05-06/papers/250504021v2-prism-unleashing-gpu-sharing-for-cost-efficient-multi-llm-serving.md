---
layout: default
title: "Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving"
---

# Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04021" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04021v2</a>
  <a href="https://arxiv.org/pdf/2505.04021.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04021v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04021v2', 'Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shan Yu, Jiarong Xing, Yifan Qiao, Mingyuan Ma, Yangmin Li, Yang Wang, Shuo Yang, Zhiqiang Xie, Shiyi Cao, Ke Bao, Ion Stoica, Harry Xu, Ying Sheng

**分类**: cs.DC, cs.AI, cs.LG, cs.PF

**发布日期**: 2025-05-06 (更新: 2025-05-12)

---

## 💡 一句话要点

**提出Prism以解决多LLM服务中的GPU共享效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `GPU共享` `成本效益` `服务水平目标` `动态调度` `内存协调` `云计算` `AI服务`

## 📋 核心要点

1. 现有GPU共享系统在动态工作负载下无法实时调整资源分配，导致无法满足延迟服务水平目标（SLO）。
2. Prism通过支持按需内存分配和双层调度策略，实现了跨模型内存协调，灵活共享GPU内存。
3. 实验证明，Prism在成本节约方面超过2倍，SLO达成率提升至3.3倍，相较于最先进的系统表现优异。

## 📝 摘要（中文）

为了解决大型语言模型（LLM）服务的高成本问题，本文提出了Prism，一个多LLM服务系统，旨在通过GPU共享实现成本效益和服务水平目标（SLO）的达成。现有的GPU共享系统在动态工作负载下缺乏资源分配和共享策略的实时调整能力，导致无法满足延迟要求。Prism通过支持按需内存分配和基于运行时需求的双层调度策略，解决了跨模型内存协调的关键限制。实验证明，Prism在成本节约和SLO达成方面均显著优于现有系统。

## 🔬 方法详解

**问题定义**：本文旨在解决多LLM服务中GPU共享效率低下的问题，现有方法无法在动态工作负载下实时调整资源分配和共享策略，导致延迟服务水平目标（SLO）无法满足。

**核心思路**：Prism的核心思路是通过实现跨模型内存协调，支持按需内存分配和动态调度，以提高GPU资源的利用率和服务质量。这样的设计使得在不同模型间能够灵活地共享和重新分配内存资源。

**技术框架**：Prism的整体架构包括两个主要模块：一是按需内存分配模块，负责动态映射物理内存到虚拟内存页；二是双层调度策略模块，根据模型的运行时需求动态调整内存共享策略。

**关键创新**：Prism的关键创新在于实现了跨模型内存协调，解决了现有GPU共享系统在动态工作负载下的资源分配局限性，显著提升了内存利用率和响应速度。

**关键设计**：Prism采用动态内存映射技术，允许在不同模型间灵活分配内存；同时，双层调度策略根据实时需求调整共享策略，确保资源的高效使用。

## 📊 实验亮点

实验结果显示，Prism在成本节约方面实现了超过2倍的提升，同时在服务水平目标（SLO）达成率上提升至3.3倍，显著优于现有最先进的系统，证明了其在多LLM服务中的有效性和优越性。

## 🎯 应用场景

Prism的研究成果在多LLM服务场景中具有广泛的应用潜力，尤其适用于云计算平台和AI服务提供商。通过提高GPU资源的共享效率，能够显著降低运营成本，并提升服务质量，推动AI技术的普及与应用。

## 📄 摘要（原文）

> Serving large language models (LLMs) is expensive, especially for providers hosting many models, making cost reduction essential. The unique workload patterns of serving multiple LLMs (i.e., multi-LLM serving) create new opportunities and challenges for this task. The long-tail popularity of models and their long idle periods present opportunities to improve utilization through GPU sharing. However, existing GPU sharing systems lack the ability to adjust their resource allocation and sharing policies at runtime, making them ineffective at meeting latency service-level objectives (SLOs) under rapidly fluctuating workloads.
>   This paper presents Prism, a multi-LLM serving system that unleashes the full potential of GPU sharing to achieve both cost efficiency and SLO attainment. At its core, Prism tackles a key limitation of existing systems$\unicode{x2014}$the lack of $\textit{cross-model memory coordination}$, which is essential for flexibly sharing GPU memory across models under dynamic workloads. Prism achieves this with two key designs. First, it supports on-demand memory allocation by dynamically mapping physical to virtual memory pages, allowing flexible memory redistribution among models that space- and time-share a GPU. Second, it improves memory efficiency through a two-level scheduling policy that dynamically adjusts sharing strategies based on models' runtime demands. Evaluations on real-world traces show that Prism achieves more than $2\times$ cost savings and $3.3\times$ SLO attainment compared to state-of-the-art systems.

