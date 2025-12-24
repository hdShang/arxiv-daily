---
layout: default
title: "Breaking the MoE LLM Trilemma: Dynamic Expert Clustering with Structured Compression"
---

# Breaking the MoE LLM Trilemma: Dynamic Expert Clustering with Structured Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02345" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02345v1</a>
  <a href="https://arxiv.org/pdf/2510.02345.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02345v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02345v1', 'Breaking the MoE LLM Trilemma: Dynamic Expert Clustering with Structured Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peijun Zhu, Ning Yang, Jiayu Wei, Jinghang Wu, Haijun Zhang

**分类**: cs.CL, cs.AI, cs.DC, cs.LG, cs.NE

**发布日期**: 2025-09-27

**备注**: 12 pages, 2 figures, 3 tables. Under review as a conference paper at ICLR 2026

---

## 💡 一句话要点

**提出基于动态专家聚类与结构化压缩的MoE LLM优化框架，解决负载不均、参数冗余和通信开销问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `动态聚类` `结构化压缩` `低秩分解` `模型优化` `大语言模型`

## 📋 核心要点

1. MoE LLM面临负载不均衡、参数冗余和通信开销的三重困境，现有方法难以同时有效解决这些问题。
2. 论文提出动态专家聚类和结构化压缩的统一框架，通过在线聚类和权重分解，优化模型结构和参数。
3. 实验结果表明，该框架在保持模型质量的同时，显著降低了参数量、提高了吞吐量，并降低了负载方差。

## 📝 摘要（中文）

本文提出了一种统一的框架，该框架基于动态专家聚类和结构化压缩，旨在解决MoE LLM中负载不平衡、参数冗余和通信开销这三大难题。该方法采用在线聚类程序，定期使用参数和激活相似度的融合指标对专家进行重组，从而稳定专家利用率。据我们所知，这是首批利用路由器的语义嵌入能力在训练期间动态重构模型架构以实现显著效率提升的框架之一。在每个集群中，我们将专家权重分解为共享的基础矩阵和极低秩的残差适配器，从而在每个组中实现高达五倍的参数缩减，同时保持专业化。这种结构支持两阶段分层路由策略：token首先被分配到一个集群，然后分配到该集群内的特定专家，从而大大减少了路由搜索空间和全互连通信量。此外，异构精度方案（将共享基础存储在FP16中，将残差因子存储在INT4中）与非活动集群的动态卸载相结合，将峰值内存消耗降低到与密集模型相当的水平。在GLUE和WikiText-103上的评估表明，我们的框架在匹配标准MoE模型质量的同时，将总参数减少了约80%，将吞吐量提高了10%到20%，并将专家负载方差降低了三倍以上。我们的工作表明，结构重组是实现可扩展、高效和内存高效的MoE LLM的一条可行路径。

## 🔬 方法详解

**问题定义**：MoE LLM在扩展模型容量的同时，面临着负载不均衡、参数冗余和通信开销三大挑战。负载不均衡导致部分专家利用率低，参数冗余增加了存储和计算成本，而全互连通信则带来了巨大的通信开销。现有方法往往只能解决其中一个或两个问题，难以实现整体优化。

**核心思路**：论文的核心思路是通过动态调整专家结构和压缩专家权重，实现负载均衡、参数高效和通信优化的统一。具体来说，首先通过在线聚类算法将专家动态分组，使得相似的专家聚集在一起，从而提高专家利用率。然后，对每个专家组内的专家权重进行结构化压缩，减少参数冗余。最后，采用两阶段分层路由策略，降低通信开销。

**技术框架**：该框架包含三个主要模块：动态专家聚类、结构化权重压缩和分层路由。动态专家聚类模块使用在线聚类算法，定期根据参数和激活相似度对专家进行重组。结构化权重压缩模块将专家权重分解为共享的基础矩阵和低秩残差适配器。分层路由模块首先将token分配到集群，然后分配到集群内的特定专家。

**关键创新**：该论文的关键创新在于提出了一个统一的框架，能够同时解决MoE LLM的负载不均衡、参数冗余和通信开销三大问题。此外，该框架还利用了路由器的语义嵌入能力，在训练期间动态重构模型架构，从而实现显著的效率提升。

**关键设计**：动态专家聚类采用在线K-means算法，使用参数和激活相似度的加权融合作为距离度量。结构化权重压缩将专家权重分解为共享基础矩阵（FP16）和低秩残差适配器（INT4），并采用异构精度存储。分层路由采用两阶段路由策略，并动态卸载非活跃集群以减少内存消耗。

## 📊 实验亮点

实验结果表明，该框架在GLUE和WikiText-103数据集上，在匹配标准MoE模型质量的同时，将总参数减少了约80%，将吞吐量提高了10%到20%，并将专家负载方差降低了三倍以上。这些结果表明，该框架在提高MoE模型的效率和可扩展性方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种需要大规模语言模型的场景，例如自然语言处理、机器翻译、文本生成等。通过降低MoE模型的参数量和计算成本，该方法有望推动MoE LLM在资源受限环境下的部署和应用，并加速AI技术的普及。

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) Large Language Models (LLMs) face a trilemma of load imbalance, parameter redundancy, and communication overhead. We introduce a unified framework based on dynamic expert clustering and structured compression to address these issues cohesively. Our method employs an online clustering procedure that periodically regroups experts using a fused metric of parameter and activation similarity, which stabilizes expert utilization. To our knowledge, this is one of the first frameworks to leverage the semantic embedding capability of the router to dynamically reconfigure the model's architecture during training for substantial efficiency gains. Within each cluster, we decompose expert weights into a shared base matrix and extremely low-rank residual adapters, achieving up to fivefold parameter reduction per group while preserving specialization. This structure enables a two-stage hierarchical routing strategy: tokens are first assigned to a cluster, then to specific experts within it, drastically reducing the routing search space and the volume of all-to-all communication. Furthermore, a heterogeneous precision scheme, which stores shared bases in FP16 and residual factors in INT4, coupled with dynamic offloading of inactive clusters, reduces peak memory consumption to levels comparable to dense models. Evaluated on GLUE and WikiText-103, our framework matches the quality of standard MoE models while reducing total parameters by approximately 80%, improving throughput by 10% to 20%, and lowering expert load variance by a factor of over three. Our work demonstrates that structural reorganization is a principled path toward scalable, efficient, and memory-effective MoE LLMs.

