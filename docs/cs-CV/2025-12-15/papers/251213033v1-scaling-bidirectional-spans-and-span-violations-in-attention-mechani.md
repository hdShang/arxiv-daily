---
layout: default
title: Scaling Bidirectional Spans and Span Violations in Attention Mechanism
---

# Scaling Bidirectional Spans and Span Violations in Attention Mechanism

**arXiv**: [2512.13033v1](https://arxiv.org/abs/2512.13033) | [PDF](https://arxiv.org/pdf/2512.13033.pdf)

**作者**: Jongwook Kim, Sangheon Yun, Sukjin Yoon

---

## 💡 一句话要点

**提出基于非对称投影的注意力梯度优化框架，以提升Transformer训练效率。**

**关键词**: `注意力机制` `梯度优化` `Transformer训练` `非对称投影` `序列建模`

## 📋 核心要点

1. 核心问题：标准注意力梯度在训练中存在几何低效性，导致次优学习信号。
2. 方法要点：通过非对称投影将反向梯度分解为并行跨度和正交违规，保持前向QKV结构不变。
3. 实验或效果：在WikiText-2数据集上验证损失降低0.56%，表明框架有效且具扩展潜力。

## 📄 摘要（原文）

> The canonical $O(N^2)$ Transformer remains the empirical performance frontier in sequence modeling, and its training can be further optimized by addressing geometric inefficiency. We propose an optimization framework that leverages an asymmetric projection to decompose the backward-pass gradients into parallel spans and orthogonal violations, while keeping the canonical forward-pass $QKV$ structure intact. Through consistent experimental validation across various decomposition and projection setups, we provide strong theoretical evidence: the standard attention gradient is suboptimal. We demonstrated that selectively scaling these components, focusing primarily on $0^{th}$ order bidirectional parallel spans, yields the most effective learning signal. On the limited WikiText-2 dataset, and using a crude configuration, this method achieved a $0.56\%$ reduction in validation loss, confirming the framework's fundamental validity and suggesting significant potential gains on larger datasets and deeper training regimes

