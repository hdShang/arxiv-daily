---
layout: default
title: Bounded Graph Clustering with Graph Neural Networks
---

# Bounded Graph Clustering with Graph Neural Networks

**arXiv**: [2512.05623v1](https://arxiv.org/abs/2512.05623) | [PDF](https://arxiv.org/pdf/2512.05623.pdf)

**作者**: Kibidi Neocosmos, Diego Baptista, Nicole Ludwig

---

## 💡 一句话要点

**提出有界图聚类框架，通过GNNs在指定范围内控制社区数量**

**关键词**: `图神经网络` `社区检测` `有界聚类` `图聚类` `聚类数量控制`

## 📋 核心要点

1. 核心问题：GNNs在社区检测中难以精确控制或返回指定聚类数量
2. 方法要点：引入灵活框架，允许用户指定聚类数量范围或精确值，并在训练中强制执行
3. 实验或效果：未知

## 📄 摘要（原文）

> In community detection, many methods require the user to specify the number of clusters in advance since an exhaustive search over all possible values is computationally infeasible. While some classical algorithms can infer this number directly from the data, this is typically not the case for graph neural networks (GNNs): even when a desired number of clusters is specified, standard GNN-based methods often fail to return the exact number due to the way they are designed. In this work, we address this limitation by introducing a flexible and principled way to control the number of communities discovered by GNNs. Rather than assuming the true number of clusters is known, we propose a framework that allows the user to specify a plausible range and enforce these bounds during training. However, if the user wants an exact number of clusters, it may also be specified and reliably returned.

