---
layout: default
title: Generative Modeling with Manifold Percolation
---

# Generative Modeling with Manifold Percolation

**arXiv**: [2511.20503v1](https://arxiv.org/abs/2511.20503) | [PDF](https://arxiv.org/pdf/2511.20503.pdf)

**作者**: Rui Tong

---

## 💡 一句话要点

**提出基于连续渗流的生成建模方法，以解决数据流形结构分析问题。**

**关键词**: `生成建模` `连续渗流` `数据流形` `拓扑相变` `超泛化` `损失函数`

## 📋 核心要点

1. 核心问题：生成建模需从观测视角解耦数据流形几何支撑与概率分布。
2. 方法要点：利用连续渗流将高维密度估计映射为几何计数问题。
3. 实验效果：防止流形收缩，实现超泛化，提升保真度和拓扑扩展。

## 📄 摘要（原文）

> Generative modeling is typically framed as learning mapping rules, but from an observer's perspective without access to these rules, the task manifests as disentangling the geometric support from the probability distribution. We propose that Continuum Percolation is uniquely suited for this support analysis, as the sampling process effectively projects high-dimensional density estimation onto a geometric counting problem on the support. In this work, we establish a rigorous isomorphism between the topological phase transitions of Random Geometric Graphs and the underlying data manifold in high-dimensional space. By analyzing the relationship between our proposed Percolation Shift metric and FID, we demonstrate that our metric captures structural pathologies (such as implicit mode collapse) where statistical metrics fail. Finally, we translate this topological phenomenon into a differentiable loss function to guide training. Experimental results confirm that this approach not only prevents manifold shrinkage but drives the model toward a state of "Hyper-Generalization," achieving good fidelity and verified topological expansion.

