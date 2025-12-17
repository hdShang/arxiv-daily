---
layout: default
title: A Bootstrap Perspective on Stochastic Gradient Descent
---

# A Bootstrap Perspective on Stochastic Gradient Descent

**arXiv**: [2512.07676v1](https://arxiv.org/abs/2512.07676) | [PDF](https://arxiv.org/pdf/2512.07676.pdf)

**作者**: Hongjian Lan, Yucong Liu, Florian Schäfer

---

## 💡 一句话要点

**提出基于统计自助法的视角解释SGD泛化优势，通过梯度协方差矩阵正则化控制算法变异性。**

**关键词**: `随机梯度下降` `泛化能力` `统计自助法` `梯度协方差` `算法变异性` `正则化`

## 📋 核心要点

1. 核心问题：SGD相比确定性梯度下降为何能提升机器学习模型的泛化能力。
2. 方法要点：将SGD视为数据收集随机性的自助法代理，正则化梯度协方差矩阵迹以降低采样噪声敏感性。
3. 实验或效果：在经验风险最小化中验证SGD避免伪解，神经网络训练中显式正则化提升测试性能。

## 📄 摘要（原文）

> Machine learning models trained with \emph{stochastic} gradient descent (SGD) can generalize better than those trained with deterministic gradient descent (GD). In this work, we study SGD's impact on generalization through the lens of the statistical bootstrap: SGD uses gradient variability under batch sampling as a proxy for solution variability under the randomness of the data collection process. We use empirical results and theoretical analysis to substantiate this claim. In idealized experiments on empirical risk minimization, we show that SGD is drawn to parameter choices that are robust under resampling and thus avoids spurious solutions even if they lie in wider and deeper minima of the training loss. We prove rigorously that by implicitly regularizing the trace of the gradient covariance matrix, SGD controls the algorithmic variability. This regularization leads to solutions that are less sensitive to sampling noise, thereby improving generalization. Numerical experiments on neural network training show that explicitly incorporating the estimate of the algorithmic variability as a regularizer improves test performance. This fact supports our claim that bootstrap estimation underpins SGD's generalization advantages.

