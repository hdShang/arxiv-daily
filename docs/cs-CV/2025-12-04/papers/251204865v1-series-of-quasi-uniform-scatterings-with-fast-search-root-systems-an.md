---
layout: default
title: Series of quasi-uniform scatterings with fast search, root systems and neural network classifications
---

# Series of quasi-uniform scatterings with fast search, root systems and neural network classifications

**arXiv**: [2512.04865v1](https://arxiv.org/abs/2512.04865) | [PDF](https://arxiv.org/pdf/2512.04865.pdf)

**作者**: Igor V. Netay

---

## 💡 一句话要点

**提出基于半单李群表示构造向量集合的方法，以支持神经网络分类任务中的潜在空间配置与扩展。**

**关键词**: `神经网络分类` `潜在空间配置` `向量集合构造` `半单李群表示` `类别扩展` `最近邻搜索`

## 📋 核心要点

1. 核心问题：处理大规模或未知类别数的分类任务时，传统分类层需重训练，效率低下。
2. 方法要点：利用半单李群不可约表示的组合与几何结构，构建高维空间中均匀分布的向量集合。
3. 实验或效果：该方法允许在潜在空间中动态扩展类别数，无需从头训练，并简化最近邻搜索问题。

## 📄 摘要（原文）

> In this paper we describe an approach to construct large extendable collections of vectors in predefined spaces of given dimensions. These collections are useful for neural network latent space configuration and training. For classification problem with large or unknown number of classes this allows to construct classifiers without classification layer and extend the number of classes without retraining of network from the very beginning. The construction allows to create large well-spaced vector collections in spaces of minimal possible dimension. If the number of classes is known or approximately predictable, one can choose sufficient enough vector collection size. If one needs to significantly extend the number of classes, one can extend the collection in the same latent space, or to incorporate the collection into collection of higher dimensions with same spacing between vectors. Also, regular symmetric structure of constructed vector collections can significantly simplify problems of search for nearest cluster centers or embeddings in the latent space. Construction of vector collections is based on combinatorics and geometry of semi-simple Lie groups irreducible representations with highest weight.

