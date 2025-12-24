---
layout: default
title: "BestServe: Serving Strategies with Optimal Goodput in Collocation and Disaggregation Architectures"
---

# BestServe: Serving Strategies with Optimal Goodput in Collocation and Disaggregation Architectures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05871" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05871v1</a>
  <a href="https://arxiv.org/pdf/2506.05871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05871v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05871v1', 'BestServe: Serving Strategies with Optimal Goodput in Collocation and Disaggregation Architectures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiannan Hu, Tianyou Zeng, Xiaoming Yuan, Liwei Song, Guangyuan Zhang, Bangzheng He

**分类**: cs.LG, cs.DC, cs.PF

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出BestServe以优化大语言模型的服务策略**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `服务策略` `资源分配` `并行计算` `推理模拟` `大型语言模型` `优化框架` `性能评估`

## 📋 核心要点

1. 现有方法在为大型语言模型提供服务时，资源分配和并行策略的选择往往依赖于繁琐的试错过程，效率低下。
2. BestServe框架通过估计不同操作场景下的良好吞吐量，快速排名服务策略，支持协同和分散架构。
3. 该框架在单个标准CPU上能在几分钟内找到最佳策略，预测误差在20%以内，显著提升了资源利用效率。

## 📝 摘要（中文）

为满足数百万用户对大型语言模型（LLMs）的服务需求，资源分配和并行策略的高效性至关重要。BestServe是一个新颖的框架，通过在不同操作场景下估计良好吞吐量来对服务策略进行排名。该框架支持协同和分散架构，利用基于改进的屋顶线模型和CPU-GPU调度动态构建的推理模拟器。BestServe能够在单个标准CPU上在几分钟内确定最佳策略，消除了高成本基准测试的需求，同时实现了20%的预测误差范围。这一轻量级设计和强大的可扩展性使其在快速部署规划中具有实际应用价值。

## 🔬 方法详解

**问题定义**：论文旨在解决在为大型语言模型提供服务时，如何高效地选择资源分配和并行策略的问题。现有方法通常依赖于耗时的试错过程，导致效率低下。

**核心思路**：BestServe通过构建推理模拟器，基于改进的屋顶线模型和CPU-GPU调度动态，快速评估和排名不同的服务策略，从而找到最佳方案。

**技术框架**：BestServe的整体架构包括推理模拟器、策略评估模块和结果优化模块。推理模拟器负责模拟不同场景下的性能，策略评估模块则根据模拟结果进行排名，最终通过结果优化模块确定最佳策略。

**关键创新**：BestServe的核心创新在于其推理模拟器的设计，能够在不进行昂贵基准测试的情况下，快速预测服务策略的性能，且误差控制在20%以内。

**关键设计**：在设计中，BestServe采用了改进的屋顶线模型来描述系统性能，并结合CPU-GPU调度动态，以确保在不同架构下的适用性和准确性。

## 📊 实验亮点

实验结果表明，BestServe能够在单个标准CPU上在几分钟内确定最佳服务策略，且预测误差控制在20%以内。这一性能显著优于传统的基准测试方法，展示了其在资源分配和并行策略优化方面的实际应用价值。

## 🎯 应用场景

BestServe框架具有广泛的应用潜力，尤其是在需要为大量用户提供高效服务的场景，如在线教育、智能客服和社交媒体等领域。其轻量级和可扩展的特性使得快速部署成为可能，能够有效提升资源利用率和用户体验。

## 📄 摘要（原文）

> Serving large language models (LLMs) to millions of users requires efficient resource allocation and parallelism strategies. It is a labor intensive trial-and-error process to find such a strategy. We present BestServe, a novel framework for ranking serving strategies by estimating goodput under various operating scenarios. Supporting both collocated and disaggregated architectures, BestServe leverages an inference simulator built on an adapted roofline model and CPU-GPU dispatch dynamics. Our framework determines the optimal strategy in minutes on a single standard CPU, eliminating the need for costly benchmarking, while achieving predictions within a $20\%$ error margin. It appeals to be practical for rapid deployment planning because of its lightweight design and strong extensibility.

