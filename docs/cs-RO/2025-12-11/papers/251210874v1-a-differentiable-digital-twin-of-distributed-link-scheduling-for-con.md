---
layout: default
title: A Differentiable Digital Twin of Distributed Link Scheduling for Contention-Aware Networking
---

# A Differentiable Digital Twin of Distributed Link Scheduling for Contention-Aware Networking

**arXiv**: [2512.10874v1](https://arxiv.org/abs/2512.10874) | [PDF](https://arxiv.org/pdf/2512.10874.pdf)

**作者**: Zhongyuan Zhao, Yujun Ming, Kevin Chan, Ananthram Swami, Santiago Segarra

---

## 💡 一句话要点

**提出可微分网络数字孪生模型，以解决无线多跳网络中链路调度优化问题。**

**关键词**: `无线网络调度` `数字孪生` `链路占空比` `冲突图` `梯度下降优化`

## 📋 核心要点

1. 核心问题：无线网络链路容量受竞争影响，传统最小成本流方法失效。
2. 方法要点：基于加权Luby算法建模冲突图，推导链路占空比解析模型。
3. 实验或效果：数字孪生预测准确，比包级仿真快5000倍，支持梯度下降优化。

## 📄 摘要（原文）

> Many routing and flow optimization problems in wired networks can be solved efficiently using minimum cost flow formulations. However, this approach does not extend to wireless multi-hop networks, where the assumptions of fixed link capacity and linear cost structure collapse due to contention for shared spectrum resources. The key challenge is that the long-term capacity of a wireless link becomes a non-linear function of its network context, including network topology, link quality, and the traffic assigned to neighboring links. In this work, we pursue a new direction of modeling wireless network under randomized medium access control by developing an analytical network digital twin (NDT) that predicts link duty cycles from network context. We generalize randomized contention as finding a Maximal Independent Set (MIS) on the conflict graph using weighted Luby's algorithm, derive an analytical model of link duty cycles, and introduce an iterative procedure that resolves the circular dependency among duty cycle, link capacity, and contention probability. Our numerical experiments show that the proposed NDT accurately predicts link duty cycles and congestion patterns with up to a 5000x speedup over packet-level simulation, and enables us to optimize link scheduling using gradient descent for reduced congestion and radio footprint.

