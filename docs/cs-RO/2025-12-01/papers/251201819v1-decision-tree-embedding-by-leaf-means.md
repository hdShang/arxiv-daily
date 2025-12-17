---
layout: default
title: Decision Tree Embedding by Leaf-Means
---

# Decision Tree Embedding by Leaf-Means

**arXiv**: [2512.01819v1](https://arxiv.org/abs/2512.01819) | [PDF](https://arxiv.org/pdf/2512.01819.pdf)

**作者**: Cencheng Shen, Yuexiao Dong, Carey E. Priebe

---

## 💡 一句话要点

**提出决策树嵌入方法，通过叶节点均值构建特征表示以降低方差并提升分类效率。**

**关键词**: `决策树嵌入` `特征表示` `分类算法` `计算效率` `集成学习`

## 📋 核心要点

1. 决策树和随机森林在分类中面临高方差或计算开销大的问题。
2. DTE利用训练树的分区结构，以叶内样本均值为锚点映射输入到嵌入空间。
3. 实验显示DTE在准确性和计算效率上优于或匹配随机森林和浅层神经网络。

## 📄 摘要（原文）

> Decision trees and random forest remain highly competitive for classification on medium-sized, standard datasets due to their robustness, minimal preprocessing requirements, and interpretability. However, a single tree suffers from high estimation variance, while large ensembles reduce this variance at the cost of substantial computational overhead and diminished interpretability. In this paper, we propose Decision Tree Embedding (DTE), a fast and effective method that leverages the leaf partitions of a trained classification tree to construct an interpretable feature representation. By using the sample means within each leaf region as anchor points, DTE maps inputs into an embedding space defined by the tree's partition structure, effectively circumventing the high variance inherent in decision-tree splitting rules. We further introduce an ensemble extension based on additional bootstrap trees, and pair the resulting embedding with linear discriminant analysis for classification. We establish several population-level theoretical properties of DTE, including its preservation of conditional density under mild conditions and a characterization of the resulting classification error. Empirical studies on synthetic and real datasets demonstrate that DTE strikes a strong balance between accuracy and computational efficiency, outperforming or matching random forest and shallow neural networks while requiring only a fraction of their training time in most cases. Overall, the proposed DTE method can be viewed either as a scalable decision tree classifier that improves upon standard split rules, or as a neural network model whose weights are learned from tree-derived anchor points, achieving an intriguing integration of both paradigms.

