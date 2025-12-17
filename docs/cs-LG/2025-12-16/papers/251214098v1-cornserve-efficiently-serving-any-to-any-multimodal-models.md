---
layout: default
title: Cornserve: Efficiently Serving Any-to-Any Multimodal Models
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14098" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14098v1</a>
  <a href="https://arxiv.org/pdf/2512.14098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14098v1" onclick="toggleFavorite(this, '2512.14098v1', 'Cornserve: Efficiently Serving Any-to-Any Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury

**分类**: cs.LG, cs.DC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Cornserve：高效服务任意到任意多模态模型的在线服务系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型服务` `任意到任意模型` `在线服务系统` `异构计算` `分布式运行时`

## 📋 核心要点

1. 现有模型服务系统难以有效处理任意到任意多模态模型中存在的请求类型、计算路径和计算规模的异构性。
2. Cornserve通过允许开发者描述计算图，并自动规划优化部署方案，从而高效处理多模态模型的异构性。
3. 实验结果表明，Cornserve在吞吐量和尾部延迟方面显著优于现有解决方案，验证了其高效性。

## 📝 摘要（中文）

本文提出了Cornserve，一个高效的在线服务系统，专门用于新兴的任意到任意多模态模型。这类模型接受文本和多模态数据（例如，图像、视频、音频）的组合作为输入，并生成文本和多模态数据的组合作为输出，从而在模型服务中引入了请求类型、计算路径和计算规模的异构性。Cornserve允许模型开发者描述通用任意到任意模型的计算图，该计算图由异构组件组成，例如多模态编码器、大型语言模型（LLM）等自回归模型以及扩散Transformer（DiT）等多模态生成器。在此基础上，Cornserve的规划器自动为模型找到优化的部署方案，包括是否以及如何基于模型和工作负载特征将模型分解为更小的组件。然后，Cornserve的分布式运行时按照该方案执行模型，从而在在线服务期间有效地处理任意到任意模型的异构性。评估表明，Cornserve可以高效地服务各种任意到任意模型和工作负载，与现有解决方案相比，吞吐量提高了3.81倍，尾部延迟降低了5.79倍。

## 🔬 方法详解

**问题定义**：现有模型服务系统在处理任意到任意多模态模型时面临挑战。这些模型接受和生成多种模态的数据，导致计算路径和资源需求高度异构。传统服务系统难以有效应对这种异构性，导致资源利用率低、延迟高。

**核心思路**：Cornserve的核心思路是将多模态模型分解为更小的、可独立部署的组件，并根据模型和工作负载的特性，自动规划最优的部署方案。通过这种方式，可以灵活地调整资源分配，从而高效地处理异构的计算需求。

**技术框架**：Cornserve包含两个主要组件：规划器和分布式运行时。规划器接收模型开发者定义的计算图，并根据模型和工作负载特征，生成优化的部署方案。该方案指定了如何将模型分解为组件、以及每个组件应该部署在哪里。分布式运行时则按照规划器生成的方案执行模型，负责组件之间的通信和数据传输。

**关键创新**：Cornserve的关键创新在于其自动规划能力。它可以根据模型和工作负载的特性，动态地调整部署方案，从而最大化资源利用率和降低延迟。此外，Cornserve还支持多种异构计算组件，包括多模态编码器、大型语言模型和多模态生成器。

**关键设计**：Cornserve的规划器使用基于成本模型的优化算法，来寻找最优的部署方案。该成本模型考虑了各种因素，例如组件的计算复杂度、数据传输成本和资源可用性。分布式运行时使用基于gRPC的通信机制，来实现组件之间的高效数据传输。此外，Cornserve还支持动态资源分配，可以根据实际负载情况调整每个组件的资源。

## 📊 实验亮点

实验结果表明，Cornserve在服务各种任意到任意模型和工作负载时，与现有解决方案相比，吞吐量提高了高达3.81倍，尾部延迟降低了高达5.79倍。这些结果证明了Cornserve在处理多模态模型异构性方面的有效性，并展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

Cornserve可应用于各种需要处理多模态数据的场景，例如智能客服、多模态内容生成、智能医疗诊断等。通过高效地服务任意到任意多模态模型，Cornserve可以加速这些应用的开发和部署，并提升用户体验。未来，Cornserve可以进一步扩展到支持更多的模型类型和计算平台。

## 📄 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.
>   Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

