---
layout: default
title: Contrastive Learning for Semi-Supervised Deep Regression with Generalized Ordinal Rankings from Spectral Seriation
---

# Contrastive Learning for Semi-Supervised Deep Regression with Generalized Ordinal Rankings from Spectral Seriation

**arXiv**: [2512.09267v1](https://arxiv.org/abs/2512.09267) | [PDF](https://arxiv.org/pdf/2512.09267.pdf)

**作者**: Ce Wang, Weihang Dai, Hanru Bai, Xiaomeng Li

---

## 💡 一句话要点

**提出基于谱排序的对比学习半监督深度回归方法，利用广义序关系减少标注依赖。**

**关键词**: `对比学习` `半监督回归` `谱排序` `序关系恢复` `特征表示学习`

## 📋 核心要点

1. 核心问题：对比回归方法依赖标签信息恢复特征序关系，限制半监督应用。
2. 方法要点：结合标记与未标记样本构建相似矩阵，通过谱排序恢复序关系用于对比学习。
3. 实验或效果：理论保证与多数据集实验验证，超越现有半监督深度回归方法。

## 📄 摘要（原文）

> Contrastive learning methods enforce label distance relationships in feature space to improve representation capability for regression models. However, these methods highly depend on label information to correctly recover ordinal relationships of features, limiting their applications to semi-supervised regression. In this work, we extend contrastive regression methods to allow unlabeled data to be used in the semi-supervised setting, thereby reducing the dependence on costly annotations. Particularly we construct the feature similarity matrix with both labeled and unlabeled samples in a mini-batch to reflect inter-sample relationships, and an accurate ordinal ranking of involved unlabeled samples can be recovered through spectral seriation algorithms if the level of error is within certain bounds. The introduction of labeled samples above provides regularization of the ordinal ranking with guidance from the ground-truth label information, making the ranking more reliable. To reduce feature perturbations, we further utilize the dynamic programming algorithm to select robust features for the matrix construction. The recovered ordinal relationship is then used for contrastive learning on unlabeled samples, and we thus allow more data to be used for feature representation learning, thereby achieving more robust results. The ordinal rankings can also be used to supervise predictions on unlabeled samples, serving as an additional training signal. We provide theoretical guarantees and empirical verification through experiments on various datasets, demonstrating that our method can surpass existing state-of-the-art semi-supervised deep regression methods. Our code have been released on https://github.com/xmed-lab/CLSS.

