---
layout: default
title: Multiclass Graph-Based Large Margin Classifiers: Unified Approach for Support Vectors and Neural Networks
---

# Multiclass Graph-Based Large Margin Classifiers: Unified Approach for Support Vectors and Neural Networks

**arXiv**: [2512.13410v1](https://arxiv.org/abs/2512.13410) | [PDF](https://arxiv.org/pdf/2512.13410.pdf)

**作者**: Vítor M. Hanriot, Luiz C. B. Torres, Antônio P. Braga

---

## 💡 一句话要点

**提出基于Gabriel图的多元大间隔分类器，统一支持向量与神经网络方法**

**关键词**: `Gabriel图分类` `大间隔分类器` `神经网络架构` `图正则化` `多元分类` `支持向量`

## 📋 核心要点

1. 核心问题：Gabriel图在多元分类中的应用扩展与优化，提升分类性能与计算效率
2. 方法要点：引入平滑激活函数、结构支持向量神经元、新子图距离成员函数和高效Gabriel图重计算算法
3. 实验或效果：实验显示方法优于先前Gabriel图分类器，统计等效于树模型

## 📄 摘要（原文）

> While large margin classifiers are originally an outcome of an optimization framework, support vectors (SVs) can be obtained from geometric approaches. This article presents advances in the use of Gabriel graphs (GGs) in binary and multiclass classification problems. For Chipclass, a hyperparameter-less and optimization-less GG-based binary classifier, we discuss how activation functions and support edge (SE)-centered neurons affect the classification, proposing smoother functions and structural SV (SSV)-centered neurons to achieve margins with low probabilities and smoother classification contours. We extend the neural network architecture, which can be trained with backpropagation with a softmax function and a cross-entropy loss, or by solving a system of linear equations. A new subgraph-/distance-based membership function for graph regularization is also proposed, along with a new GG recomputation algorithm that is less computationally expensive than the standard approach. Experimental results with the Friedman test show that our method was better than previous GG-based classifiers and statistically equivalent to tree-based models.

