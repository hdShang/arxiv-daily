---
layout: default
title: Universality of high-dimensional scaling limits of stochastic gradient descent
---

# Universality of high-dimensional scaling limits of stochastic gradient descent

**arXiv**: [2512.13634v1](https://arxiv.org/abs/2512.13634) | [PDF](https://arxiv.org/pdf/2512.13634.pdf)

**作者**: Reza Gheissari, Aukosh Jagannath

---

## 💡 一句话要点

**证明高维随机梯度下降的ODE极限在数据分布满足矩匹配和初始化去局部化时具有普适性**

**关键词**: `高维统计` `随机梯度下降` `ODE极限` `普适性` `乘积测度` `摘要统计量`

## 📋 核心要点

1. 研究高维统计任务中，损失仅依赖于数据在参数向量和真实向量张成子空间上的投影
2. 证明当数据来自满足前两矩匹配的高斯混合分布时，SGD的摘要统计量演化收敛到自治ODE，且该极限在数据为乘积测度混合时仍成立
3. 通过反例展示初始化坐标对齐时ODE极限非普适，且摘要统计量围绕ODE固定点的SDE极限也非普适

## 📄 摘要（原文）

> We consider statistical tasks in high dimensions whose loss depends on the data only through its projection into a fixed-dimensional subspace spanned by the parameter vectors and certain ground truth vectors. This includes classifying mixture distributions with cross-entropy loss with one and two-layer networks, and learning single and multi-index models with one and two-layer networks. When the data is drawn from an isotropic Gaussian mixture distribution, it is known that the evolution of a finite family of summary statistics under stochastic gradient descent converges to an autonomous ordinary differential equation (ODE), as the dimension and sample size go to $\infty$ and the step size goes to $0$ commensurately. Our main result is that these ODE limits are universal in that this convergence occurs even when the data is drawn from mixtures of product measures provided the first two moments match the corresponding Gaussian distribution and the initialization and ground truth vectors are sufficiently coordinate-delocalized. We complement this by proving two corresponding non-universality results. We provide a simple example where the ODE limits are non-universal if the initialization is coordinate aligned. We also show that the stochastic differential equation limits arising as fluctuations of the summary statistics around their ODE's fixed points are not universal.

