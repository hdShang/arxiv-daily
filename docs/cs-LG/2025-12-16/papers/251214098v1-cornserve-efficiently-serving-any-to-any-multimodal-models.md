---
layout: default
title: Cornserve: Efficiently Serving Any-to-Any Multimodal Models
---

# Cornserve: Efficiently Serving Any-to-Any Multimodal Models

**arXiv**: [2512.14098v1](https://arxiv.org/abs/2512.14098) | [PDF](https://arxiv.org/pdf/2512.14098.pdf)

**作者**: Jeff J. Ma, Jae-Won Chung, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury

**分类**: cs.LG, cs.DC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Cornserve系统以高效在线服务任意到任意多模态模型，解决异构计算挑战。**

**关键词**: `多模态模型服务` `任意到任意模型` `异构计算` `在线服务系统` `模型分解` `分布式运行时` `吞吐量优化` `尾部延迟降低`

## 📋 核心要点

1. 现有方法难以处理任意到任意多模态模型的异构性，包括请求类型、计算路径和计算规模差异，导致在线服务效率低下。
2. Cornserve通过描述模型计算图，自动规划优化部署，并利用分布式运行时执行，核心思想是分解模型以匹配工作负载特性。
3. 实验表明，Cornserve显著提升吞吐量（最高3.81倍）和降低尾部延迟（最高5.79倍），优于现有解决方案。

## 📝 摘要（中文）

我们介绍了Cornserve，一个用于新兴任意到任意多模态模型的高效在线服务系统。任意到任意模型接受文本和多模态数据（如图像、视频、音频）的组合作为输入，并生成文本和多模态数据的组合作为输出，在模型服务中引入了请求类型、计算路径和计算规模异构性。Cornserve允许模型开发者描述通用任意到任意模型的计算图，该图由多模态编码器、大型语言模型等自回归模型和扩散变换器等多模态生成器等异构组件组成。基于此，Cornserve的规划器自动为模型找到优化的部署计划，包括是否以及如何根据模型和工作负载特性将模型分解为更小的组件。Cornserve的分布式运行时然后按照计划执行模型，高效处理在线服务中的任意到任意模型异构性。评估显示，Cornserve能够高效服务多样化的任意到任意模型和工作负载，相比现有解决方案，吞吐量提升高达3.81倍，尾部延迟降低高达5.79倍。

## 🔬 方法详解

Cornserve的整体框架包括一个规划器和一个分布式运行时。规划器基于模型开发者提供的计算图描述，自动生成优化的部署计划，关键创新点在于能够根据模型和工作负载特性动态决定是否及如何将模型分解为异构组件（如多模态编码器、LLMs、DiTs）。与现有方法的主要区别在于，Cornserve专门针对任意到任意模型的异构性设计，通过自动规划和分布式执行来高效处理多模态输入输出的复杂计算路径，而传统系统往往假设固定模型结构或忽略这种异构性。

## 📊 实验亮点

最重要的实验结果显示，Cornserve在多样化任意到任意模型和工作负载上，相比现有解决方案，实现了高达3.81倍的吞吐量提升和高达5.79倍的尾部延迟降低，证明了其高效处理异构性的能力。

## 🎯 应用场景

该研究可应用于多模态AI服务场景，如智能助手、内容生成平台和实时交互系统，支持文本、图像、视频、音频的任意组合输入输出，提升服务效率和可扩展性，具有实际部署价值。

## 📄 摘要（原文）

> We present Cornserve, an efficient online serving system for an emerging class of multimodal models called Any-to-Any models. Any-to-Any models accept combinations of text and multimodal data (e.g., image, video, audio) as input and also generate combinations of text and multimodal data as output, introducing request type, computation path, and computation scaling heterogeneity in model serving.
>   Cornserve allows model developers to describe the computation graph of generic Any-to-Any models, which consists of heterogeneous components such as multimodal encoders, autoregressive models like Large Language Models (LLMs), and multimodal generators like Diffusion Transformers (DiTs). Given this, Cornserve's planner automatically finds an optimized deployment plan for the model, including whether and how to disaggregate the model into smaller components based on model and workload characteristics. Cornserve's distributed runtime then executes the model per the plan, efficiently handling Any-to-Any model heterogeneity during online serving. Evaluations show that Cornserve can efficiently serve diverse Any-to-Any models and workloads, delivering up to 3.81$\times$ throughput improvement and up to 5.79$\times$ tail latency reduction over existing solutions.

