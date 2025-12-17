---
layout: default
title: Non-negative DAG Learning from Time-Series Data
---

# Non-negative DAG Learning from Time-Series Data

**arXiv**: [2512.07267v1](https://arxiv.org/abs/2512.07267) | [PDF](https://arxiv.org/pdf/2512.07267.pdf)

**作者**: Samuel Rey, Gonzalo Mateos

---

## 💡 一句话要点

**提出非负有向无环图学习方法，从时间序列数据中恢复因果结构。**

**关键词**: `有向无环图学习` `时间序列分析` `凸优化` `因果推断` `结构向量自回归模型`

## 📋 核心要点

1. 核心问题：从多元时间序列中学习有向无环图以捕捉瞬时依赖关系。
2. 方法要点：假设边权重非负，通过凸约束保证无环性，实现凸优化求解。
3. 实验或效果：在合成数据上评估，性能优于现有方法，凸公式保证全局最优性。

## 📄 摘要（原文）

> This work aims to learn the directed acyclic graph (DAG) that captures the instantaneous dependencies underlying a multivariate time series. The observed data follow a linear structural vector autoregressive model (SVARM) with both instantaneous and time-lagged dependencies, where the instantaneous structure is modeled by a DAG to reflect potential causal relationships. While recent continuous relaxation approaches impose acyclicity through smooth constraint functions involving powers of the adjacency matrix, they lead to non-convex optimization problems that are challenging to solve. In contrast, we assume that the underlying DAG has only non-negative edge weights, and leverage this additional structure to impose acyclicity via a convex constraint. This enables us to cast the problem of non-negative DAG recovery from multivariate time-series data as a convex optimization problem in abstract form, which we solve using the method of multipliers. Crucially, the convex formulation guarantees global optimality of the solution. Finally, we assess the performance of the proposed method on synthetic time-series data, where it outperforms existing alternatives.

