---
layout: default
title: AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving
---

# AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04013" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04013</a>
  <a href="https://arxiv.org/pdf/2512.04013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04013" onclick="toggleFavorite(this, '2512.04013', 'AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ying Wang, Zhen Jin, Jiexiong Xu, Wenhai Lin, Yiquan Chen, Wenzhi Chen

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AugServe：用于增强型大语言模型推理服务的自适应请求调度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增强型大语言模型` `推理服务` `请求调度` `自适应调度` `动态批处理`

## 📋 核心要点

1. 现有增强型LLM推理服务依赖FCFS调度，易产生队头阻塞，导致排队延迟超标。
2. AugServe采用两阶段自适应请求调度，结合推理特征和运行时信息优化调度决策。
3. 实验表明，AugServe有效吞吐量显著高于vLLM和InferCept，并大幅降低TTFT。

## 📝 摘要（中文）

随着集成外部工具的增强型大语言模型（LLM）在Web应用中日益普及，提升增强型LLM推理服务效率和优化服务级别目标（SLO）对于改善用户体验至关重要。为了实现这一目标，推理系统必须在延迟约束内最大化请求处理量，即提高有效吞吐量。然而，现有系统面临两个主要挑战：（i）依赖先进先出（FCFS）调度导致严重的队头阻塞，使得许多请求的排队延迟超过SLO；（ii）静态批处理token限制无法适应波动的负载和硬件条件。这两个因素都会降低有效吞吐量和服务质量。本文提出了AugServe，一个旨在减少排队延迟并提高增强型LLM推理服务有效吞吐量的高效推理框架。AugServe的核心思想是两阶段自适应请求调度策略。具体来说，AugServe结合了增强型LLM请求的推理特征来优化调度决策的顺序（阶段I）。这些决策通过运行时信息不断完善（阶段II），从而适应请求特征和系统能力。此外，AugServe根据硬件状态和实时负载动态调整token批处理机制，进一步提高吞吐量性能。实验结果表明，AugServe的有效吞吐量比vLLM和InferCept分别高4.7倍和3.3倍，同时将首个token生成时间（TTFT）分别降低高达96.3%和95.0%。

## 🔬 方法详解

**问题定义**：论文旨在解决增强型大语言模型推理服务中，由于传统的先进先出（FCFS）调度策略和静态token批处理机制导致的排队延迟过高和有效吞吐量不足的问题。现有方法无法有效适应请求特征和系统状态的变化，导致服务质量下降。

**核心思路**：AugServe的核心思路是采用两阶段自适应请求调度策略，并结合动态token批处理机制。通过分析请求的推理特征和利用运行时信息，优化请求的调度顺序，从而减少排队延迟。同时，根据硬件状态和实时负载动态调整token批处理大小，以提高资源利用率和吞吐量。

**技术框架**：AugServe框架包含两个主要阶段：第一阶段是基于推理特征的请求排序，利用请求的元数据（例如，请求所需的工具类型、预计的计算复杂度等）来预测请求的优先级，并据此进行排序。第二阶段是基于运行时信息的调度优化，根据系统负载、硬件资源利用率等实时信息，动态调整请求的调度顺序。此外，AugServe还包含一个动态token批处理模块，根据硬件状态和实时负载调整批处理大小。

**关键创新**：AugServe的关键创新在于其两阶段自适应请求调度策略和动态token批处理机制。与传统的静态调度策略相比，AugServe能够更好地适应请求特征和系统状态的变化，从而提高有效吞吐量和服务质量。动态token批处理机制能够根据硬件状态和实时负载动态调整批处理大小，从而更好地利用硬件资源。

**关键设计**：在第一阶段，AugServe使用一个轻量级的预测模型来估计请求的优先级。该模型可以基于请求的元数据进行训练，例如，请求所需的工具类型、预计的计算复杂度等。在第二阶段，AugServe使用一个反馈控制机制来动态调整请求的调度顺序。该机制根据系统负载、硬件资源利用率等实时信息，调整请求的优先级。动态token批处理模块使用一个简单的启发式算法来调整批处理大小，该算法根据硬件状态和实时负载来调整批处理大小。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04013/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04013/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.04013/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AugServe在有效吞吐量方面显著优于现有系统。与vLLM相比，AugServe的有效吞吐量提高了4.7倍；与InferCept相比，提高了3.3倍。同时，AugServe还显著降低了首个token生成时间（TTFT），与vLLM和InferCept相比，分别降低了高达96.3%和95.0%。这些结果表明，AugServe能够有效提高增强型LLM推理服务的效率和质量。

## 🎯 应用场景

AugServe可应用于各种需要高效增强型大语言模型推理服务的场景，例如智能客服、自动化报告生成、代码生成等。通过提高推理效率和优化服务质量，AugServe可以显著提升用户体验，并降低服务成本。未来，该技术有望进一步推广到其他类型的AI推理服务中。

## 📄 摘要（原文）

> As augmented large language models (LLMs) with external tools become increasingly popular in web applications, improving augmented LLM inference serving efficiency and optimizing service-level objectives (SLOs) are critical for enhancing user experience. To achieve this, inference systems must maximize request handling within latency constraints, referred to as increasing effective throughput. However, existing systems face two major challenges: (i) reliance on first-come-first-served (FCFS) scheduling causes severe head-of-line blocking, leading to queuing delays exceeding the SLOs for many requests; and (ii) static batch token limit, which fails to adapt to fluctuating loads and hardware conditions. Both of these factors degrade effective throughput and service quality.This paper presents AugServe, an efficient inference framework designed to reduce queueing latency and enhance effective throughput for augmented LLM inference services. The core idea of AugServe is a two-stage adaptive request scheduling strategy. Specifically, AugServe combines the inference features of augmented LLM requests to optimize the order of scheduling decisions (stage I). These decisions are continuously refined with runtime information (stage II), adapting to both request characteristics and system capabilities. In addition, AugServe dynamically adjusts the token batching mechanism based on hardware status and real-time load, further enhancing throughput performance. Experimental results show that AugServe achieves 4.7x and 3.3x higher effective throughput than vLLM and InferCept, while reducing time-to-first-token (TTFT) by up to 96.3% and 95.0%, respectively.

