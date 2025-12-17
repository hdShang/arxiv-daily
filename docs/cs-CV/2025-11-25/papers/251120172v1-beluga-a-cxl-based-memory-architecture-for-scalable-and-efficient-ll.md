---
layout: default
title: Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management
---

# Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management

**arXiv**: [2511.20172v1](https://arxiv.org/abs/2511.20172) | [PDF](https://arxiv.org/pdf/2511.20172.pdf)

**作者**: Xinjun Yang, Qingda Hu, Junru Li, Feifei Li, Yuqi Zhou, Yicong Zhu, Qiuru Lin, Jian Dai, Yang Kong, Jiayu Zhang, Guoqiang Xu, Qiang Liu

---

## 💡 一句话要点

**提出Beluga CXL内存架构以解决LLM推理中KVCache内存瓶颈问题**

**关键词**: `CXL内存架构` `KVCache管理` `LLM推理优化` `GPU内存扩展` `低延迟访问`

## 📋 核心要点

1. LLM模型规模扩大和长上下文推理需求使GPU内存成为瓶颈，HBM容量有限需依赖CPU DRAM
2. 基于CXL技术构建共享内存池，支持GPU和CPU直接访问，降低延迟和同步开销
3. 实验显示在vLLM引擎中TTFT降低89.6%，吞吐量提升7.35倍，优于RDMA方案

## 📄 摘要（原文）

> The rapid increase in LLM model sizes and the growing demand for long-context inference have made memory a critical bottleneck in GPU-accelerated serving systems. Although high-bandwidth memory (HBM) on GPUs offers fast access, its limited capacity necessitates reliance on host memory (CPU DRAM) to support larger working sets such as the KVCache. However, the maximum DRAM capacity is constrained by the limited number of memory channels per CPU socket. To overcome this limitation, current systems often adopt RDMA-based disaggregated memory pools, which introduce significant challenges including high access latency, complex communication protocols, and synchronization overhead. Fortunately, the emerging CXL technology introduces new opportunities in KVCache design. In this paper, we propose Beluga, a novel memory architecture that enables GPUs and CPUs to access a shared, large-scale memory pool through CXL switches. By supporting native load/store access semantics over the CXL fabric, our design delivers near-local memory latency, while reducing programming complexity and minimizing synchronization overhead. We conduct a systematic characterization of a commercial CXL switch-based memory pool and propose a set of design guidelines. Based on Beluga, we design and implement Beluga-KVCache, a system tailored for managing the large-scale KVCache in LLM inference. Beluga-KVCache achieves an 89.6% reduction in Time-To-First-Token (TTFT) and 7.35x throughput improvement in the vLLM inference engine compared to RDMA-based solutions. To the best of our knowledge, Beluga is the first system that enables GPUs to directly access large-scale memory pools through CXL switches, marking a significant step toward low-latency, shared access to vast memory resources by GPUs.

