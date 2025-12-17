---
layout: default
title: Gradient Descent with Provably Tuned Learning-rate Schedules
---

# Gradient Descent with Provably Tuned Learning-rate Schedules

**arXiv**: [2512.05084v1](https://arxiv.org/abs/2512.05084) | [PDF](https://arxiv.org/pdf/2512.05084.pdf)

**作者**: Dravyansh Sharma

---

## 💡 一句话要点

**提出可证明调优学习率调度的方法，适用于非凸非光滑函数，扩展至神经网络优化。**

**关键词**: `梯度下降` `超参数调优` `非凸优化` `学习率调度` `神经网络优化` `样本复杂度`

## 📋 核心要点

1. 核心问题：梯度优化中学习率等超参数通常依赖启发式调优，缺乏理论保证，且现有理论假设过强。
2. 方法要点：开发新分析工具，可证明调优超参数，适用于非凸非光滑函数，匹配先前样本复杂度界限。
3. 实验或效果：应用于神经网络常用激活函数，扩展至多超参数调优，包括学习率调度和动量同步调优。

## 📄 摘要（原文）

> Gradient-based iterative optimization methods are the workhorse of modern machine learning. They crucially rely on careful tuning of parameters like learning rate and momentum. However, one typically sets them using heuristic approaches without formal near-optimality guarantees. Recent work by Gupta and Roughgarden studies how to learn a good step-size in gradient descent. However, like most of the literature with theoretical guarantees for gradient-based optimization, their results rely on strong assumptions on the function class including convexity and smoothness which do not hold in typical applications. In this work, we develop novel analytical tools for provably tuning hyperparameters in gradient-based algorithms that apply to non-convex and non-smooth functions. We obtain matching sample complexity bounds for learning the step-size in gradient descent shown for smooth, convex functions in prior work (up to logarithmic factors) but for a much broader class of functions. Our analysis applies to gradient descent on neural networks with commonly used activation functions (including ReLU, sigmoid and tanh). We extend our framework to tuning multiple hyperparameters, including tuning the learning rate schedule, simultaneously tuning momentum and step-size, and pre-training the initialization vector. Our approach can be used to bound the sample complexity for minimizing both the validation loss as well as the number of gradient descent iterations.

