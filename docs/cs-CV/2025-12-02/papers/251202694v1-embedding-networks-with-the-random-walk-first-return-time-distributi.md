---
layout: default
title: Embedding networks with the random walk first return time distribution
---

# Embedding networks with the random walk first return time distribution

**arXiv**: [2512.02694v1](https://arxiv.org/abs/2512.02694) | [PDF](https://arxiv.org/pdf/2512.02694.pdf)

**作者**: Vedanta Thapar, Renaud Lambiotte, George T. Cantwell

---

## 💡 一句话要点

**提出随机游走首次返回时间分布作为可解释的节点嵌入方法，用于复杂网络分析。**

**关键词**: `随机游走` `节点嵌入` `网络对齐` `首次返回时间分布` `图结构分析`

## 📋 核心要点

1. 核心问题：传统节点嵌入方法缺乏数学基础或可解释性，需更优嵌入以捕获网络结构。
2. 方法要点：利用随机游走首次返回时间分布为每个节点分配概率质量函数，定义节点间距离。
3. 实验或效果：在节点对齐任务中优于手动设计指标，且匹配分布能保留网络关键特征。

## 📄 摘要（原文）

> We propose the first return time distribution (FRTD) of a random walk as an interpretable and mathematically grounded node embedding. The FRTD assigns a probability mass function to each node, allowing us to define a distance between any pair of nodes using standard metrics for discrete distributions. We present several arguments to motivate the FRTD embedding. First, we show that FRTDs are strictly more informative than eigenvalue spectra, yet insufficient for complete graph identification, thus placing FRTD equivalence between cospectrality and isomorphism. Second, we argue that FRTD equivalence between nodes captures structural similarity. Third, we empirically demonstrate that the FRTD embedding outperforms manually designed graph metrics in network alignment tasks. Finally, we show that random networks that approximately match the FRTD of a desired target also preserve other salient features. Together these results demonstrate the FRTD as a simple and mathematically principled embedding for complex networks.

