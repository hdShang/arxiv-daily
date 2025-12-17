---
layout: default
title: Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits
---

# Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits

**arXiv**: [2511.20273v1](https://arxiv.org/abs/2511.20273) | [PDF](https://arxiv.org/pdf/2511.20273.pdf)

**作者**: Areeb Ahmad, Abhinav Joshi, Ashutosh Modi

---

## 💡 一句话要点

**提出基于奇异向量的Transformer组件分解方法，以揭示内部计算子结构。**

**关键词**: `Transformer解释性` `奇异向量分解` `机制可解释性` `计算图分析` `功能子结构`

## 📋 核心要点

1. 核心问题：Transformer模型内部计算复杂且分布，现有方法忽略组件内功能子结构。
2. 方法要点：将注意力头和MLP分解为正交奇异方向，识别叠加和独立计算。
3. 实验或效果：在IOI、GP和GT任务中验证，发现功能头编码多个重叠子功能。

## 📄 摘要（原文）

> Transformer-based language models exhibit complex and distributed behavior, yet their internal computations remain poorly understood. Existing mechanistic interpretability methods typically treat attention heads and multilayer perceptron layers (MLPs) (the building blocks of a transformer architecture) as indivisible units, overlooking possibilities of functional substructure learned within them. In this work, we introduce a more fine-grained perspective that decomposes these components into orthogonal singular directions, revealing superposed and independent computations within a single head or MLP. We validate our perspective on widely used standard tasks like Indirect Object Identification (IOI), Gender Pronoun (GP), and Greater Than (GT), showing that previously identified canonical functional heads, such as the name mover, encode multiple overlapping subfunctions aligned with distinct singular directions. Nodes in a computational graph, that are previously identified as circuit elements show strong activation along specific low-rank directions, suggesting that meaningful computations reside in compact subspaces. While some directions remain challenging to interpret fully, our results highlight that transformer computations are more distributed, structured, and compositional than previously assumed. This perspective opens new avenues for fine-grained mechanistic interpretability and a deeper understanding of model internals.

