---
layout: default
title: KVNAND: Efficient On-Device Large Language Model Inference Using DRAM-Free In-Flash Computing
---

# KVNAND: Efficient On-Device Large Language Model Inference Using DRAM-Free In-Flash Computing

**arXiv**: [2512.03608v1](https://arxiv.org/abs/2512.03608) | [PDF](https://arxiv.org/pdf/2512.03608.pdf)

**作者**: Lishuo Deng, Shaojie Xu, Jinwu Chen, Changwei Yan, Jiajie Wang, Zhe Jiang, Weiwei Shan

---

## 💡 一句话要点

**提出KVNAND架构，利用闪存内计算实现无DRAM的大语言模型边缘推理，解决长上下文KV缓存存储瓶颈。**

**关键词**: `闪存内计算` `大语言模型推理` `KV缓存优化` `边缘设备部署` `3D NAND闪存` `长上下文处理`

## 📋 核心要点

1. 核心问题：长上下文下KV缓存超过模型权重，导致DRAM成本高且容量不足，闪存存储性能差。
2. 方法要点：将模型权重和KV缓存全存储在3D NAND闪存，通过闪存内计算、头组并行和页面级映射优化访问性能。
3. 实验或效果：在7B和70B模型上，相比DRAM方案，在128/1K/10K上下文长度下实现1.98×/1.94×/2.05×几何平均加速，支持100K上下文。

## 📄 摘要（原文）

> Deploying large language models (LLMs) on edge devices enables personalized agents with strong privacy and low cost. However, with tens to hundreds of billions of parameters, single-batch autoregressive inference suffers from extremely low arithmetic intensity, creating severe weight-loading and bandwidth pressures on resource-constrained platforms. Recent in-flash computing (IFC) solutions alleviate this bottleneck by co-locating weight-related linear computations in the decode phase with flash, yet still rely on DRAM for the key-value (KV) cache. As context length grows, the KV cache can exceed model weights in size, imposing prohibitive DRAM cost and capacity requirements. Attempts to offload KV cache to flash suffer from severe performance penalties.
>   We propose KVNAND, the first DRAM-free, IFC-based architecture that stores both model weights and KV cache entirely in compute-enabled 3D NAND flash. KVNAND addresses the fundamental performance challenges of flash under intensive KV cache access by leveraging IFC for all memory-bound operations to reduce data transfer overhead, introducing head-group parallelism to boost throughput, and employing page-level KV cache mapping to align token access patterns with flash organization. In addition, we propose a design space exploration framework that evaluates discrete and compact KVNAND variants to balance weight and KV placement, automatically identifying the optimal design trade-off. These techniques mitigate latency, energy, and reliability concerns, turning flash into a practical medium for long-context KV storage. Evaluations on MHA 7B and GQA 70B LLMs show that KVNAND achieves 1.98\(\times\)/1.94\(\times\)/2.05\(\times\) geomean speedup at 128/1K/10K-token contexts compared to DRAM-equipped IFC designs and addresses out-of-memory failures at 100K context length.

