---
layout: default
title: Matrix: Peer-to-Peer Multi-Agent Synthetic Data Generation Framework
---

# Matrix: Peer-to-Peer Multi-Agent Synthetic Data Generation Framework

**arXiv**: [2511.21686v1](https://arxiv.org/abs/2511.21686) | [PDF](https://arxiv.org/pdf/2511.21686.pdf)

**作者**: Dong Wang, Yang Li, Ansong Ni, Ching-Feng Yeh, Youssef Emad, Xinjie Lei, Liam Robbins, Karthik Padthe, Hu Xu, Xian Li, Asli Celikyilmaz, Ramya Raghavendra, Lifei Huang, Carole-Jean Wu, Shang-Wen Li

---

## 💡 一句话要点

**提出Matrix去中心化框架以解决多Agent合成数据生成的可扩展性与灵活性限制**

**关键词**: `合成数据生成` `多Agent系统` `去中心化框架` `Ray分布式计算` `可扩展工作流` `模块化设计`

## 📋 核心要点

1. 核心问题：集中式编排在多Agent合成数据生成中导致可扩展性瓶颈和领域灵活性不足
2. 方法要点：采用点对点消息传递设计，消除中心协调器，基于Ray实现高并发模块化工作流
3. 实验或效果：在多种场景下，相同硬件资源下数据生成吞吐量提升2-15倍，输出质量未降低

## 📄 摘要（原文）

> Synthetic data has become increasingly important for training large language models, especially when real data is scarce, expensive, or privacy-sensitive. Many such generation tasks require coordinated multi-agent workflows, where specialized agents collaborate to produce data that is higher quality, more diverse, and structurally richer. However, existing frameworks for multi-agent synthesis often depend on a centralized orchestrator, creating scalability bottlenecks, or are hardcoded for specific domains, limiting flexibility. We present \textbf{Matrix}, a decentralized framework that represents both control and data flow as serialized messages passed through distributed queues. This peer-to-peer design eliminates the central orchestrator. Each task progresses independently through lightweight agents, while compute-intensive operations, such as LLM inference or containerized environments, are handled by distributed services. Built on Ray, Matrix scales to tens of thousands of concurrent agentic workflows and provides a modular, configurable design that enables easy adaptation to a wide range of data generation workflows. We evaluate Matrix across diverse synthesis scenarios, such as multi-agent collaborative dialogue, web-based reasoning data extraction, and tool-use trajectory generation in customer service environments. In all cases, Matrix achieves $2$--$15\times$ higher data generation throughput under identical hardware resources, without compromising output quality.

