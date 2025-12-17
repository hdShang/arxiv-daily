---
layout: default
title: BalLOT: Balanced $k$-means clustering with optimal transport
---

# BalLOT: Balanced $k$-means clustering with optimal transport

**arXiv**: [2512.05926v1](https://arxiv.org/abs/2512.05926) | [PDF](https://arxiv.org/pdf/2512.05926.pdf)

**作者**: Wenyan Luo, Dustin G. Mixon

---

## 💡 一句话要点

**提出BalLOT方法，基于最优传输解决平衡k均值聚类问题。**

**关键词**: `平衡聚类` `最优传输` `k均值` `交替最小化` `理论保证` `数值实验`

## 📋 核心要点

1. 核心问题：平衡k均值聚类，即聚类时要求各簇大小均衡。
2. 方法要点：结合最优传输与交替最小化，实现快速有效求解。
3. 实验或效果：通过数值实验验证性能，并提供理论保证如积分耦合和恢复分析。

## 📄 摘要（原文）

> We consider the fundamental problem of balanced $k$-means clustering. In particular, we introduce an optimal transport approach to alternating minimization called BalLOT, and we show that it delivers a fast and effective solution to this problem. We establish this with a variety of numerical experiments before proving several theoretical guarantees. First, we prove that for generic data, BalLOT produces integral couplings at each step. Next, we perform a landscape analysis to provide theoretical guarantees for both exact and partial recoveries of planted clusters under the stochastic ball model. Finally, we propose initialization schemes that achieve one-step recovery of planted clusters.

