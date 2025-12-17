---
layout: default
title: Cornserve: Efficiently Serving Any-to-Any Multimodal Models
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14098" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14098</a>
  <a href="https://arxiv.org/pdf/2512.14098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14098" onclick="toggleFavorite(this, '2512.14098', 'Cornserve: Efficiently Serving Any-to-Any Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury

**分类**: cs.LG, cs.DC

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Cornserve：高效服务任意到任意多模态模型，提升吞吐和降低延迟。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型服务` `Any-to-Any模型` `计算图` `模型部署优化` `分布式系统` `异构计算` `大型语言模型` `扩散模型`

## 📋 核心要点

1. 现有模型服务系统难以有效处理Any-to-Any多模态模型的异构性，导致资源利用率低和延迟高。
2. Cornserve通过计算图描述Any-to-Any模型，并自动规划优化部署方案，从而高效处理模型异构性。
3. 实验结果表明，Cornserve在吞吐量和尾部延迟方面显著优于现有解决方案，提升效果明显。

## 📝 摘要（中文）

本文提出了Cornserve，一个高效的在线服务系统，专门针对新兴的任意到任意（Any-to-Any）多模态模型。这类模型接受文本和多模态数据（如图像、视频、音频）的组合作为输入，并生成文本和多模态数据的组合作为输出，从而在模型服务中引入了请求类型、计算路径和计算规模的异构性。Cornserve允许模型开发者描述通用Any-to-Any模型的计算图，该计算图由异构组件构成，例如多模态编码器、大型语言模型（LLM）等自回归模型以及扩散Transformer（DiT）等多模态生成器。在此基础上，Cornserve的规划器自动为模型找到优化的部署方案，包括是否以及如何基于模型和工作负载特征将模型分解为更小的组件。然后，Cornserve的分布式运行时按照该方案执行模型，从而在在线服务期间高效地处理Any-to-Any模型的异构性。评估表明，Cornserve可以高效地服务各种Any-to-Any模型和工作负载，与现有解决方案相比，吞吐量提高了3.81倍，尾部延迟降低了5.79倍。

## 🔬 方法详解

**问题定义**：现有模型服务系统难以有效处理Any-to-Any多模态模型的异构性。Any-to-Any模型输入输出均为多种模态数据的组合，导致请求类型、计算路径和计算规模差异巨大，传统模型服务方法难以有效应对这种异构性，造成资源浪费和延迟增加。

**核心思路**：Cornserve的核心思路是允许模型开发者描述Any-to-Any模型的计算图，然后由系统自动规划和执行优化的部署方案。通过显式地表示模型的计算流程和组件，系统可以更好地理解模型的异构性，并根据模型和工作负载的特性进行优化。

**技术框架**：Cornserve包含两个主要组件：规划器（Planner）和分布式运行时（Distributed Runtime）。规划器接收模型开发者定义的计算图，并根据模型和工作负载的特征，自动生成优化的部署方案，包括模型分解策略、组件放置策略等。分布式运行时按照规划器生成的方案执行模型，负责组件之间的通信、数据传输和资源管理。

**关键创新**：Cornserve的关键创新在于其自动化的模型部署规划能力。与传统的手动部署方式相比，Cornserve可以根据模型和工作负载的动态变化，自动调整部署方案，从而实现更高的资源利用率和更低的延迟。此外，Cornserve还支持将模型分解为更小的组件，并根据组件的计算特性进行优化部署，进一步提升了性能。

**关键设计**：Cornserve的规划器使用基于成本模型的优化算法，综合考虑模型的计算复杂度、数据传输开销、资源可用性等因素，选择最优的部署方案。分布式运行时采用基于Actor模型的并发编程框架，实现高效的组件间通信和数据传输。具体的参数设置和网络结构细节在论文中未详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Cornserve在服务各种Any-to-Any模型和工作负载时，与现有解决方案相比，吞吐量提高了高达3.81倍，尾部延迟降低了高达5.79倍。这些显著的性能提升证明了Cornserve在处理多模态模型异构性方面的有效性。

## 🎯 应用场景

Cornserve可广泛应用于需要处理多模态数据输入输出的AI应用，例如智能客服、多模态内容生成、跨模态检索等。它能够提升这些应用的响应速度和用户体验，并降低部署和维护成本。未来，Cornserve有望成为构建下一代多模态AI应用的关键基础设施。

## 📄 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

