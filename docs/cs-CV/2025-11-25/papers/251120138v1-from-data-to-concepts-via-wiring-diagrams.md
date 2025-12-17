---
layout: default
title: From data to concepts via wiring diagrams
---

# From data to concepts via wiring diagrams

**arXiv**: [2511.20138v1](https://arxiv.org/abs/2511.20138) | [PDF](https://arxiv.org/pdf/2511.20138.pdf)

**作者**: Jason Lo, Mohammadnima Jafari

---

## 💡 一句话要点

**提出准骨架接线图算法，从序列数据提取概念并分析自主代理行为。**

**关键词**: `接线图提取` `序列数据分析` `Hasse图对应` `自主代理行为` `聚类算法比较`

## 📋 核心要点

1. 核心问题：如何从序列数据中抽象表示概念，如时间过程。
2. 方法要点：定义准骨架接线图，证明其与Hasse图对应，设计提取算法。
3. 实验或效果：应用于游戏代理行为分析，正确识别获胜策略，并与标准聚类算法比较。

## 📄 摘要（原文）

> A wiring diagram is a labeled directed graph that represents an abstract concept such as a temporal process. In this article, we introduce the notion of a quasi-skeleton wiring diagram graph, and prove that quasi-skeleton wiring diagram graphs correspond to Hasse diagrams. Using this result, we designed algorithms that extract wiring diagrams from sequential data. We used our algorithms in analyzing the behavior of an autonomous agent playing a computer game, and the algorithms correctly identified the winning strategies. We compared the performance of our main algorithm with two other algorithms based on standard clustering techniques (DBSCAN and agglomerative hierarchical), including when some of the data was perturbed. Overall, this article brings together techniques in category theory, graph theory, clustering, reinforcement learning, and data engineering.

