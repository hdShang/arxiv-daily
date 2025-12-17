---
layout: default
title: Tensor Network Based Feature Learning Model
---

# Tensor Network Based Feature Learning Model

**arXiv**: [2512.02547v1](https://arxiv.org/abs/2512.02547) | [PDF](https://arxiv.org/pdf/2512.02547.pdf)

**作者**: Albert Saiapin, Kim Batselier

---

## 💡 一句话要点

**提出基于张量网络的特征学习模型，通过可学习CPD优化特征超参数，提升大规模核方法训练效率。**

**关键词**: `张量网络` `特征学习` `核方法` `超参数优化` `交替最小二乘法`

## 📋 核心要点

1. 核心问题：核方法中特征超参数优化依赖交叉验证，效率低且未自动化。
2. 方法要点：将张量积特征表示为可学习CPD，使用ALS联合优化模型与超参数。
3. 实验或效果：在真实数据上训练快3-5倍，预测质量与标准模型相当。

## 📄 摘要（原文）

> Many approximations were suggested to circumvent the cubic complexity of kernel-based algorithms, allowing their application to large-scale datasets. One strategy is to consider the primal formulation of the learning problem by mapping the data to a higher-dimensional space using tensor-product structured polynomial and Fourier features. The curse of dimensionality due to these tensor-product features was effectively solved by a tensor network reparameterization of the model parameters. However, another important aspect of model training - identifying optimal feature hyperparameters - has not been addressed and is typically handled using the standard cross-validation approach. In this paper, we introduce the Feature Learning (FL) model, which addresses this issue by representing tensor-product features as a learnable Canonical Polyadic Decomposition (CPD). By leveraging this CPD structure, we efficiently learn the hyperparameters associated with different features alongside the model parameters using an Alternating Least Squares (ALS) optimization method. We prove the effectiveness of the FL model through experiments on real data of various dimensionality and scale. The results show that the FL model can be consistently trained 3-5 times faster than and have the prediction quality on par with a standard cross-validated model.

