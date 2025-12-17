---
layout: default
title: Sliced ReLU attention: Quasi-linear contextual expressivity via sorting
---

# Sliced ReLU attention: Quasi-linear contextual expressivity via sorting

**arXiv**: [2512.11411v1](https://arxiv.org/abs/2512.11411) | [PDF](https://arxiv.org/pdf/2512.11411.pdf)

**作者**: Siwan Boufadène, François-Xavier Vialard

---

## 💡 一句话要点

**提出切片ReLU注意力机制，通过排序实现准线性复杂度，适用于长上下文序列处理。**

**关键词**: `注意力机制` `长上下文处理` `准线性复杂度` `排序算法` `可微核` `序列解耦`

## 📋 核心要点

1. 核心问题：传统注意力机制如softmax和ReLU变体在长上下文序列中计算复杂度高，影响效率。
2. 方法要点：基于键-查询差异的一维投影，利用排序操作构建可微非对称核，实现O(n log(n))复杂度。
3. 实验或效果：理论证明保持强表达力，支持序列解耦任务和上下文通用逼近性质，小规模实验展示实用潜力。

## 📄 摘要（原文）

> We introduce sliced ReLU attention, a new attention mechanism that departs structurally from both softmax and ReLU-based alternatives. Instead of applying a nonlinearity to pairwise dot products, we operate on one-dimensional projections of key--query differences and leverage sorting to obtain quasi-linear complexity. This construction yields a differentiable, non-symmetric kernel that can be computed in O(n log(n)) through a sorting procedure, making it suitable for very long contexts. Beyond computational benefits, the model retains strong theoretical expressive power: we establish two in-context expressivity results, previously known for softmax attention, showing that sliced ReLU attention preserves the ability to perform nontrivial sequence-to-sequence disentangling tasks and satisfies a contextual universal approximation property. Finally, we illustrate the potential practical interest of this kernel in small-scale experiments.

