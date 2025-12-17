---
layout: default
title: A2G-QFL: Adaptive Aggregation with Two Gains in Quantum Federated learning
---

# A2G-QFL: Adaptive Aggregation with Two Gains in Quantum Federated learning

**arXiv**: [2512.03363v1](https://arxiv.org/abs/2512.03363) | [PDF](https://arxiv.org/pdf/2512.03363.pdf)

**作者**: Shanika Iroshi Nanayakkara, Shiva Raj Pokhrel

---

## 💡 一句话要点

**提出A2G-QFL框架以解决量子联邦学习中的异构与噪声问题**

**关键词**: `量子联邦学习` `自适应聚合` `双增益框架` `异构网络` `模型几何匹配` `量子隐形传态`

## 📋 核心要点

1. 核心问题：量子联邦学习因客户端质量不均、量子隐形传态保真度随机、设备不稳定及模型几何不匹配导致性能下降
2. 方法要点：引入双增益框架，通过几何增益调节模型融合，QoS增益基于保真度、延迟和不稳定性调整客户端重要性
3. 实验或效果：在量子经典混合测试床上验证，在异构和噪声条件下提高了稳定性和准确性

## 📄 摘要（原文）

> Federated learning (FL) deployed over quantum enabled and heterogeneous classical networks faces significant performance degradation due to uneven client quality, stochastic teleportation fidelity, device instability, and geometric mismatch between local and global models. Classical aggregation rules assume euclidean topology and uniform communication reliability, limiting their suitability for emerging quantum federated systems. This paper introduces A2G (Adaptive Aggregation with Two Gains), a dual gain framework that jointly regulates geometric blending through a geometry gain and modulates client importance using a QoS gain derived from teleportation fidelity, latency, and instability. We develop the A2G update rule, establish convergence guarantees under smoothness and bounded variance assumptions, and show that A2G recovers FedAvg, QoS aware averaging, and manifold based aggregation as special cases. Experiments on a quantum classical hybrid testbed demonstrate improved stability and higher accuracy under heterogeneous and noisy conditions.

