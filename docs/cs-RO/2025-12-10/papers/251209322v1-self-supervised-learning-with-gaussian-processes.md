---
layout: default
title: Self-Supervised Learning with Gaussian Processes
---

# Self-Supervised Learning with Gaussian Processes

**arXiv**: [2512.09322v1](https://arxiv.org/abs/2512.09322) | [PDF](https://arxiv.org/pdf/2512.09322.pdf)

**作者**: Yunshan Duan, Sinead Williamson

---

## 💡 一句话要点

**提出高斯过程自监督学习以解决表示空间平滑性和不确定性量化问题**

**关键词**: `自监督学习` `高斯过程` `表示学习` `不确定性量化` `核方法`

## 📋 核心要点

1. 核心问题：自监督学习中生成相似样本对困难，且缺乏不确定性量化。
2. 方法要点：利用高斯过程先验，通过协方差函数自然聚合相似表示，无需显式正样本。
3. 实验或效果：在分类和回归任务中，GPSSL在准确性、不确定性量化和误差控制方面优于传统方法。

## 📄 摘要（原文）

> Self supervised learning (SSL) is a machine learning paradigm where models learn to understand the underlying structure of data without explicit supervision from labeled samples. The acquired representations from SSL have demonstrated useful for many downstream tasks including clustering, and linear classification, etc. To ensure smoothness of the representation space, most SSL methods rely on the ability to generate pairs of observations that are similar to a given instance. However, generating these pairs may be challenging for many types of data. Moreover, these methods lack consideration of uncertainty quantification and can perform poorly in out-of-sample prediction settings. To address these limitations, we propose Gaussian process self supervised learning (GPSSL), a novel approach that utilizes Gaussian processes (GP) models on representation learning. GP priors are imposed on the representations, and we obtain a generalized Bayesian posterior minimizing a loss function that encourages informative representations. The covariance function inherent in GPs naturally pulls representations of similar units together, serving as an alternative to using explicitly defined positive samples. We show that GPSSL is closely related to both kernel PCA and VICReg, a popular neural network-based SSL method, but unlike both allows for posterior uncertainties that can be propagated to downstream tasks. Experiments on various datasets, considering classification and regression tasks, demonstrate that GPSSL outperforms traditional methods in terms of accuracy, uncertainty quantification, and error control.

