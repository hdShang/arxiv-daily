---
layout: default
title: Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization
---

# Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization

**arXiv**: [2512.14263v1](https://arxiv.org/abs/2512.14263) | [PDF](https://arxiv.org/pdf/2512.14263.pdf)

**作者**: Nick Leenders, Thomas Quadt, Boris Cule, Roy Lindelauf, Herman Monsuur, Joost van Oijen, Mark Voskuijl

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于决策树的可解释偏好学习模型，以解决高斯过程在偏好贝叶斯优化中可解释性差、处理分类数据困难及计算复杂的问题。**

**关键词**: `偏好学习` `贝叶斯优化` `决策树模型` `可解释人工智能` `分类数据处理` `大规模优化` `个性化推荐`

## 📋 核心要点

1. 现有高斯过程模型可解释性差、处理分类数据困难且计算复杂，限制了偏好贝叶斯优化的实际应用。
2. 提出基于决策树的代理模型，具有固有可解释性，能处理混合数据类型，并实现大规模扩展。
3. 在尖峰函数上性能优于高斯过程模型，在非尖峰函数上性能接近，并成功应用于真实偏好学习任务。

## 📝 摘要（中文）

当前的偏好贝叶斯优化方法依赖于高斯过程作为代理模型，这些模型难以解释、处理分类数据困难且计算复杂，限制了其实际应用。本文引入了一种基于决策树的固有可解释代理模型，能够处理分类和连续数据，并可扩展到大型数据集。在八个逐渐尖峰的优化函数上进行的大量数值实验表明，该模型在尖峰函数上优于基于高斯过程的替代方法，在非尖峰函数上性能仅略低。此外，我们将模型应用于真实世界的寿司数据集，展示了其学习个人寿司偏好的能力。最后，我们展示了利用历史偏好数据加速新用户优化过程的初步工作。

## 🔬 方法详解

论文提出了一种基于决策树的代理模型框架，用于替代传统的高斯过程在偏好贝叶斯优化中的角色。关键技术创新点在于利用决策树的固有可解释性，通过构建树结构来建模用户偏好，支持分类和连续数据的混合输入，并采用高效算法实现大规模数据扩展。与现有方法的主要区别在于，该模型避免了高斯过程的黑盒特性，提供了更直观的决策路径解释，同时降低了计算复杂度，提高了处理复杂数据类型的灵活性。

## 📊 实验亮点

在八个尖峰优化函数实验中，模型在尖峰函数上显著优于高斯过程基准，在非尖峰函数上性能仅略低；在寿司数据集上成功学习个人偏好，验证了实际应用潜力。

## 🎯 应用场景

该研究可应用于个性化推荐系统、产品设计优化和用户偏好建模等领域，通过可解释的偏好学习提升决策透明度和效率，具有实际商业和科研价值。

## 📄 摘要（原文）

> Current Preferential Bayesian Optimization methods rely on Gaussian Processes (GPs) as surrogate models. These models are hard to interpret, struggle with handling categorical data, and are computationally complex, limiting their real-world usability. In this paper, we introduce an inherently interpretable decision tree-based surrogate model capable of handling both categorical and continuous data, and scalable to large datasets. Extensive numerical experiments on eight increasingly spiky optimization functions show that our model outperforms GP-based alternatives on spiky functions and has only marginally lower performance for non-spiky functions. Moreover, we apply our model to the real-world Sushi dataset and show its ability to learn an individual's sushi preferences. Finally, we show some initial work on using historical preference data to speed up the optimization process for new unseen users.

