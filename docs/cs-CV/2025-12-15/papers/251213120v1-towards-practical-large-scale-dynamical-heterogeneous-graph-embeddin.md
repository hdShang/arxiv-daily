---
layout: default
title: Towards Practical Large-scale Dynamical Heterogeneous Graph Embedding: Cold-start Resilient Recommendation
---

# Towards Practical Large-scale Dynamical Heterogeneous Graph Embedding: Cold-start Resilient Recommendation

**arXiv**: [2512.13120v1](https://arxiv.org/abs/2512.13120) | [PDF](https://arxiv.org/pdf/2512.13120.pdf)

**作者**: Mabiao Long, Jiaxi Liu, Yufeng Li, Hao Xiong, Junchi Yan, Kefan Wang, Yi Cao, Jiandong Ding

---

## 💡 一句话要点

**提出两阶段动态异构图嵌入框架，以解决大规模生产环境中的可扩展性、数据新鲜度和冷启动问题。**

**关键词**: `动态异构图嵌入` `冷启动推荐` `增量学习` `图变换器` `实时更新` `生产部署`

## 📋 核心要点

1. 核心问题：动态异构图嵌入在生产部署中面临可扩展性、数据新鲜度和冷启动挑战。
2. 方法要点：结合HetSGFormer进行静态全局学习，使用ILLE进行轻量级实时增量更新，避免全图重训练。
3. 实验或效果：在十亿级图上，A/B测试显示HetSGFormer提升广告价值6.11%，ILLE额外提升3.22%，刷新时效性提高83.2%。

## 📄 摘要（原文）

> Deploying dynamic heterogeneous graph embeddings in production faces key challenges of scalability, data freshness, and cold-start. This paper introduces a practical, two-stage solution that balances deep graph representation with low-latency incremental updates. Our framework combines HetSGFormer, a scalable graph transformer for static learning, with Incremental Locally Linear Embedding (ILLE), a lightweight, CPU-based algorithm for real-time updates. HetSGFormer captures global structure with linear scalability, while ILLE provides rapid, targeted updates to incorporate new data, thus avoiding costly full retraining. This dual approach is cold-start resilient, leveraging the graph to create meaningful embeddings from sparse data. On billion-scale graphs, A/B tests show HetSGFormer achieved up to a 6.11% lift in Advertiser Value over previous methods, while the ILLE module added another 3.22% lift and improved embedding refresh timeliness by 83.2%. Our work provides a validated framework for deploying dynamic graph learning in production environments.

