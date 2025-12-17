---
layout: default
title: Delta Sum Learning: an approach for fast and global convergence in Gossip Learning
---

# Delta Sum Learning: an approach for fast and global convergence in Gossip Learning

**arXiv**: [2512.01549v1](https://arxiv.org/abs/2512.01549) | [PDF](https://arxiv.org/pdf/2512.01549.pdf)

**作者**: Tom Goethals, Merlijn Sebrechts, Stijn De Schrijver, Filip De Turck, Bruno Volckaert

---

## 💡 一句话要点

**提出Delta Sum Learning以改进Gossip Learning的聚合操作，提升全局收敛性**

**关键词**: `Gossip Learning` `去中心化学习` `聚合优化` `全局收敛` `边缘计算` `编排框架`

## 📋 核心要点

1. 核心问题：联邦学习和Gossip Learning中平均聚合方法在模型精度和全局收敛方面存在不足
2. 方法要点：Delta Sum Learning优化Gossip Learning的基础聚合操作，结合基于Open Application Model的去中心化编排框架
3. 实验或效果：在50节点拓扑中，Delta Sum Learning的全局精度下降比替代方法低58%，显示强全局收敛性

## 📄 摘要（原文）

> Federated Learning is a popular approach for distributed learning due to its security and computational benefits. With the advent of powerful devices in the network edge, Gossip Learning further decentralizes Federated Learning by removing centralized integration and relying fully on peer to peer updates. However, the averaging methods generally used in both Federated and Gossip Learning are not ideal for model accuracy and global convergence. Additionally, there are few options to deploy Learning workloads in the edge as part of a larger application using a declarative approach such as Kubernetes manifests. This paper proposes Delta Sum Learning as a method to improve the basic aggregation operation in Gossip Learning, and implements it in a decentralized orchestration framework based on Open Application Model, which allows for dynamic node discovery and intent-driven deployment of multi-workload applications. Evaluation results show that Delta Sum performance is on par with alternative integration methods for 10 node topologies, but results in a 58% lower global accuracy drop when scaling to 50 nodes. Overall, it shows strong global convergence and a logarithmic loss of accuracy with increasing topology size compared to a linear loss for alternatives under limited connectivity.

