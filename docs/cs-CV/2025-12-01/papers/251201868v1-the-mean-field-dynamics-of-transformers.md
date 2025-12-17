---
layout: default
title: The Mean-Field Dynamics of Transformers
---

# The Mean-Field Dynamics of Transformers

**arXiv**: [2512.01868v1](https://arxiv.org/abs/2512.01868) | [PDF](https://arxiv.org/pdf/2512.01868.pdf)

**作者**: Philippe Rigollet

---

## 💡 一句话要点

**提出Transformer注意力作为交互粒子系统的平均场动力学框架，分析其连续极限与聚类现象。**

**关键词**: `Transformer动力学` `平均场极限` `Wasserstein梯度流` `聚类分析` `注意力机制` `长上下文处理`

## 📋 核心要点

1. 核心问题：将Transformer注意力建模为交互粒子系统，研究其平均场极限下的动力学行为。
2. 方法要点：通过球面连续化连接Wasserstein梯度流、Kuramoto同步模型和均值漂移聚类。
3. 实验或效果：揭示全局聚类现象，分析聚类速率、归一化影响和长上下文注意力的相变。

## 📄 摘要（原文）

> We develop a mathematical framework that interprets Transformer attention as an interacting particle system and studies its continuum (mean-field) limits. By idealizing attention continuous on the sphere, we connect Transformer dynamics to Wasserstein gradient flows, synchronization models (Kuramoto), and mean-shift clustering. Central to our results is a global clustering phenomenon whereby tokens cluster asymptotically after long metastable states where they are arranged into multiple clusters. We further analyze a tractable equiangular reduction to obtain exact clustering rates, show how commonly used normalization schemes alter contraction speeds, and identify a phase transition for long-context attention. The results highlight both the mechanisms that drive representation collapse and the regimes that preserve expressive, multi-cluster structure in deep attention architectures.

