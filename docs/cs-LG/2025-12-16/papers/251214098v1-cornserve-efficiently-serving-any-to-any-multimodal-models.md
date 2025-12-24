---
layout: default
title: "Cornserve: Efficiently Serving Any-to-Any Multimodal Models"
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14098" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14098v1</a>
  <a href="https://arxiv.org/pdf/2512.14098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14098v1', 'Cornserve: Efficiently Serving Any-to-Any Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury

**分类**: cs.LG, cs.DC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Cornserve：高效服务任意到任意多模态模型的在线服务系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型服务` `Any-to-Any模型` `分布式系统` `模型部署优化` `计算图` `异构计算` `在线服务`

## 📋 核心要点

1. 现有模型服务系统难以有效处理Any-to-Any多模态模型在请求类型、计算路径和计算规模上的异构性。
2. Cornserve通过允许开发者描述模型计算图，并自动规划优化部署方案，从而高效处理Any-to-Any模型的异构性。
3. 实验表明，Cornserve在吞吐量和尾部延迟方面显著优于现有解决方案，证明了其高效性。

## 📝 摘要（中文）

本文提出了Cornserve，一个高效的在线服务系统，专门针对新兴的任意到任意（Any-to-Any）多模态模型。这类模型接受文本和多模态数据（如图像、视频、音频）的任意组合作为输入，并生成文本和多模态数据的任意组合作为输出，这给模型服务带来了请求类型、计算路径和计算规模上的异构性。Cornserve允许模型开发者描述通用Any-to-Any模型的计算图，该计算图由异构组件构成，例如多模态编码器、大型语言模型（LLM）等自回归模型以及扩散Transformer（DiT）等多模态生成器。在此基础上，Cornserve的规划器自动为模型找到优化的部署方案，包括是否以及如何基于模型和工作负载特征将模型分解为更小的组件。然后，Cornserve的分布式运行时按照该方案执行模型，从而在在线服务期间高效地处理Any-to-Any模型的异构性。评估结果表明，Cornserve可以高效地服务各种Any-to-Any模型和工作负载，与现有解决方案相比，吞吐量提高了3.81倍，尾部延迟降低了5.79倍。

## 🔬 方法详解

**问题定义**：现有模型服务系统难以有效处理Any-to-Any多模态模型的异构性。这类模型输入和输出可以是文本、图像、视频、音频等多种模态的任意组合，导致请求类型多样，计算路径复杂，计算规模差异大，给模型部署和服务带来了挑战。现有的模型服务系统通常针对特定类型的模型或任务进行优化，无法很好地适应Any-to-Any模型的这种灵活性和复杂性。

**核心思路**：Cornserve的核心思路是将Any-to-Any模型表示为一个计算图，其中节点表示不同的模型组件（如编码器、LLM、生成器），边表示数据流。通过这种方式，模型开发者可以灵活地描述模型的计算逻辑。然后，Cornserve的规划器会根据模型和工作负载的特性，自动找到一个优化的部署方案，包括如何将模型分解为更小的组件，以及如何在分布式环境中部署这些组件。这样可以充分利用计算资源，并减少延迟。

**技术框架**：Cornserve的整体架构包括以下几个主要模块：1) 模型描述：允许开发者使用一种领域特定语言（DSL）来描述Any-to-Any模型的计算图。2) 规划器：根据模型描述和工作负载特性，自动生成优化的部署方案。3) 分布式运行时：按照规划器生成的方案，在分布式环境中执行模型。运行时负责管理模型组件的部署、数据流的调度以及错误处理等。

**关键创新**：Cornserve的关键创新在于其自动化的模型部署规划能力。与现有的模型服务系统相比，Cornserve不需要人工干预即可找到一个优化的部署方案。这大大简化了模型部署的流程，并提高了资源利用率。此外，Cornserve还支持将模型分解为更小的组件，并根据需要动态地调整组件的部署位置，从而更好地适应不同的工作负载。

**关键设计**：Cornserve的规划器使用了一种基于成本模型的搜索算法来寻找优化的部署方案。成本模型考虑了模型组件的计算成本、数据传输成本以及资源限制等因素。规划器会尝试不同的模型分解和部署策略，并选择成本最低的方案。在分布式运行时中，Cornserve使用了一种基于消息传递的通信机制来实现数据流的调度。每个模型组件都作为一个独立的进程运行，并通过消息队列与其他组件进行通信。这种设计可以提高系统的可扩展性和容错性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14098v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Cornserve在服务Any-to-Any模型时，相比现有解决方案，吞吐量提升高达3.81倍，尾部延迟降低高达5.79倍。这些显著的性能提升证明了Cornserve在处理复杂多模态模型服务方面的有效性。

## 🎯 应用场景

Cornserve适用于各种需要处理多模态输入和输出的场景，例如智能客服、内容创作、机器人交互等。它可以帮助开发者快速部署和高效服务复杂的Any-to-Any模型，从而加速多模态人工智能的应用落地。未来，Cornserve有望成为多模态模型服务的基础设施，推动多模态人工智能的发展。

## 📄 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.
>   Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

