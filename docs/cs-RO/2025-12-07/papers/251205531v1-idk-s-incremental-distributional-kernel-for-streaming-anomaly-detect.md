---
layout: default
title: IDK-S: Incremental Distributional Kernel for Streaming Anomaly Detection
---

# IDK-S: Incremental Distributional Kernel for Streaming Anomaly Detection

**arXiv**: [2512.05531v1](https://arxiv.org/abs/2512.05531) | [PDF](https://arxiv.org/pdf/2512.05531.pdf)

**作者**: Yang Xu, Yixiao Ma, Kaifeng Zhang, Zuliang Yang, Kai Ming Ting

---

## 💡 一句话要点

**提出IDK-S以解决数据流异常检测中分布演化与实时效率的挑战。**

**关键词**: `数据流异常检测` `核均值嵌入` `增量学习` `隔离分布核` `实时效率`

## 📋 核心要点

1. 核心问题：数据流异常检测需在分布演化下保持高精度与实时效率。
2. 方法要点：基于核均值嵌入框架，采用轻量级增量更新机制，继承隔离分布核优势。
3. 实验或效果：在13个基准测试中，IDK-S实现更高检测精度，速度比现有方法快一个数量级。

## 📄 摘要（原文）

> Anomaly detection on data streams presents significant challenges, requiring methods to maintain high detection accuracy among evolving distributions while ensuring real-time efficiency. Here we introduce $\mathcal{IDK}$-$\mathcal{S}$, a novel $\mathbf{I}$ncremental $\mathbf{D}$istributional $\mathbf{K}$ernel for $\mathbf{S}$treaming anomaly detection that effectively addresses these challenges by creating a new dynamic representation in the kernel mean embedding framework. The superiority of $\mathcal{IDK}$-$\mathcal{S}$ is attributed to two key innovations. First, it inherits the strengths of the Isolation Distributional Kernel, an offline detector that has demonstrated significant performance advantages over foundational methods like Isolation Forest and Local Outlier Factor due to the use of a data-dependent kernel. Second, it adopts a lightweight incremental update mechanism that significantly reduces computational overhead compared to the naive baseline strategy of performing a full model retraining. This is achieved without compromising detection accuracy, a claim supported by its statistical equivalence to the full retrained model. Our extensive experiments on thirteen benchmarks demonstrate that $\mathcal{IDK}$-$\mathcal{S}$ achieves superior detection accuracy while operating substantially faster, in many cases by an order of magnitude, than existing state-of-the-art methods.

