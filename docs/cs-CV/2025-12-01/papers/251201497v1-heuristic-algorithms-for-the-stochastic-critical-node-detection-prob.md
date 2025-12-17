---
layout: default
title: Heuristic algorithms for the stochastic critical node detection problem
---

# Heuristic algorithms for the stochastic critical node detection problem

**arXiv**: [2512.01497v1](https://arxiv.org/abs/2512.01497) | [PDF](https://arxiv.org/pdf/2512.01497.pdf)

**作者**: Tuguldur Bayarsaikhan, Altannar Chinchuluun, Ashwin Arulselvan, Panos Pardalos

---

## 💡 一句话要点

**提出启发式和基于学习的方法以解决随机关键节点检测问题**

**关键词**: `关键节点检测` `随机网络` `启发式算法` `基于学习的方法` `网络连通性`

## 📋 核心要点

1. 核心问题：在边存在概率已知的随机网络中，检测移除后破坏连通性的关键节点子集
2. 方法要点：结合启发式算法和基于学习的方法，优化节点选择策略
3. 实验或效果：在随机图上测试，启发式方法可扩展性强，基于学习的方法推理时间稳定

## 📄 摘要（原文）

> Given a network, the critical node detection problem finds a subset of nodes whose removal disrupts the network connectivity. Since many real-world systems are naturally modeled as graphs, assessing the vulnerability of the network is essential, with applications in transportation systems, traffic forecasting, epidemic control, and biological networks. In this paper, we consider a stochastic version of the critical node detection problem, where the existence of edges is given by certain probabilities. We propose heuristics and learning-based methods for the problem and compare them with existing algorithms. Experimental results performed on random graphs from small to larger scales, with edge-survival probabilities drawn from different distributions, demonstrate the effectiveness of the methods. Heuristic methods often illustrate the strongest results with high scalability, while learning-based methods maintain nearly constant inference time as the network size and density grow.

