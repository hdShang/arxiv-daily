---
layout: default
title: Improved Linear-Time Construction of Minimal Dominating Set via Mobile Agents
---

# Improved Linear-Time Construction of Minimal Dominating Set via Mobile Agents

**arXiv**: [2511.19880v1](https://arxiv.org/abs/2511.19880) | [PDF](https://arxiv.org/pdf/2511.19880.pdf)

**作者**: Prabhat Kumar Chand, Anisur Rahaman Molla

---

## 💡 一句话要点

**提出线性时间算法在同步移动代理模型中构建最小支配集**

**关键词**: `最小支配集` `移动代理` `分布式算法` `线性时间` `匿名图` `同步模型`

## 📋 核心要点

1. 核心问题：在匿名图中使用移动代理计算最小支配集
2. 方法要点：基于最优分散算法，设计两种线性时间算法
3. 实验或效果：在O(n)轮内完成，每代理仅需O(log n)位内存

## 📄 摘要（原文）

> Mobile agents have emerged as a powerful framework for solving fundamental graph problems in distributed settings in recent times. These agents, modelled as autonomous physical or software entities, possess local computation power, finite memory and have the ability to traverse a graph, offering efficient solutions to a range of classical problems. In this work, we focus on the problem of computing a \emph{minimal dominating set} (mDS) in anonymous graphs using mobile agents. Building on the recently proposed optimal dispersion algorithm on the synchronous mobile agent model, we design two new algorithms that achieve a \emph{linear-time} solution for this problem in the synchronous setting. Specifically, given a connected $n$-node graph with $n$ agents initially placed in either rooted or arbitrary configurations, we show that an mDS can be computed in $O(n)$ rounds using only $O(\log n)$ bits of memory per agent, without using any prior knowledge of any global parameters. This improves upon the best-known complexity results in the literature over the same model. In addition, as natural by-products of our methodology, our algorithms also construct a spanning tree and elect a unique leader in $O(n)$ rounds, which are also important results of independent interest in the mobile-agent framework.

