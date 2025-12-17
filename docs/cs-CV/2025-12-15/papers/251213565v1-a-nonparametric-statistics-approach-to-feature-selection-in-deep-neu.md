---
layout: default
title: A Nonparametric Statistics Approach to Feature Selection in Deep Neural Networks with Theoretical Guarantees
---

# A Nonparametric Statistics Approach to Feature Selection in Deep Neural Networks with Theoretical Guarantees

**arXiv**: [2512.13565v1](https://arxiv.org/abs/2512.13565) | [PDF](https://arxiv.org/pdf/2512.13565.pdf)

**作者**: Junye Du, Zhenghao Li, Zhutong Gu, Long Feng

---

## 💡 一句话要点

**提出基于非参数统计的深度神经网络特征选择方法，在非线性高维场景下保证理论一致性。**

**关键词**: `特征选择` `非参数统计` `深度神经网络` `理论保证` `高维数据` `非线性模型`

## 📋 核心要点

1. 核心问题：在未知非线性函数下，从高维特征中识别相关特征集，满足E(y\|x)=G(x_S0)。
2. 方法要点：将神经网络重构为索引模型，利用二阶Stein公式进行无梯度特征选择，结合筛选机制处理高维稀疏性。
3. 实验或效果：通过模拟和真实数据分析验证方法性能，即使在复杂特征交互下也表现优异。

## 📄 摘要（原文）

> This paper tackles the problem of feature selection in a highly challenging setting: $\mathbb{E}(y \| \boldsymbol{x}) = G(\boldsymbol{x}_{\mathcal{S}_0})$, where $\mathcal{S}_0$ is the set of relevant features and $G$ is an unknown, potentially nonlinear function subject to mild smoothness conditions. Our approach begins with feature selection in deep neural networks, then generalizes the results to H{ö}lder smooth functions by exploiting the strong approximation capabilities of neural networks. Unlike conventional optimization-based deep learning methods, we reformulate neural networks as index models and estimate $\mathcal{S}_0$ using the second-order Stein's formula. This gradient-descent-free strategy guarantees feature selection consistency with a sample size requirement of $n = Ω(p^2)$, where $p$ is the feature dimension. To handle high-dimensional scenarios, we further introduce a screening-and-selection mechanism that achieves nonlinear selection consistency when $n = Ω(s \log p)$, with $s$ representing the sparsity level. Additionally, we refit a neural network on the selected features for prediction and establish performance guarantees under a relaxed sparsity assumption. Extensive simulations and real-data analyses demonstrate the strong performance of our method even in the presence of complex feature interactions.

