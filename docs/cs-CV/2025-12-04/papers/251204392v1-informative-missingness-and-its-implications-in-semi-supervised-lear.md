---
layout: default
title: Informative missingness and its implications in semi-supervised learning
---

# Informative missingness and its implications in semi-supervised learning

**arXiv**: [2512.04392v1](https://arxiv.org/abs/2512.04392) | [PDF](https://arxiv.org/pdf/2512.04392.pdf)

**作者**: Jinran Wu, You-Gan Wang, Geoffrey J. McLachlan

---

## 💡 一句话要点

**提出建模信息性缺失机制以在半监督学习中提升分类器性能**

**关键词**: `半监督学习` `信息性缺失` `期望最大化算法` `有限混合模型` `分类器性能`

## 📋 核心要点

1. 核心问题：标签缺失机制依赖特征或类别时，缺失指示符包含有用信息
2. 方法要点：在有限混合模型似然框架中，用EM算法拟合信息性缺失机制
3. 实验或效果：在类别重叠适中、标签稀疏时，建模缺失机制可降低预期误差

## 📄 摘要（原文）

> Semi-supervised learning (SSL) constructs classifiers using both labelled and unlabelled data. It leverages information from labelled samples, whose acquisition is often costly or labour-intensive, together with unlabelled data to enhance prediction performance. This defines an incomplete-data problem, which statistically can be formulated within the likelihood framework for finite mixture models that can be fitted using the expectation-maximisation (EM) algorithm. Ideally, one would prefer a completely labelled sample, as one would anticipate that a labelled observation provides more information than an unlabelled one. However, when the mechanism governing label absence depends on the observed features or the class labels or both, the missingness indicators themselves contain useful information. In certain situations, the information gained from modelling the missing-label mechanism can even outweigh the loss due to missing labels, yielding a classifier with a smaller expected error than one based on a completely labelled sample analysed. This improvement arises particularly when class overlap is moderate, labelled data are sparse, and the missingness is informative. Modelling such informative missingness thus offers a coherent statistical framework that unifies likelihood-based inference with the behaviour of empirical SSL methods.

