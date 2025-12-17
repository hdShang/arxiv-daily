---
layout: default
title: From STLS to Projection-based Dictionary Selection in Sparse Regression for System Identification
---

# From STLS to Projection-based Dictionary Selection in Sparse Regression for System Identification

**arXiv**: [2512.14404v1](https://arxiv.org/abs/2512.14404) | [PDF](https://arxiv.org/pdf/2512.14404.pdf)

**作者**: Hangjun Cho, Fabio V. G. Amaral, Andrei A. Klishin, Cassio M. Oishi, Steven L. Brunton

**分类**: stat.ML, cs.LG, math.OC, physics.comp-ph

**发布日期**: 2025-12-16

**备注**: 34 pages, 11 figures

---

## 💡 一句话要点

**提出基于投影误差评分的字典选择方法，以增强稀疏回归在系统辨识中的准确性和可解释性。**

**关键词**: `稀疏回归` `系统辨识` `SINDy算法` `字典选择` `投影误差评分` `动态系统建模` `数据驱动发现`

## 📋 核心要点

1. 现有稀疏回归方法如STLS在字典选择上缺乏理论指导，影响系统辨识的准确性和可解释性。
2. 提出基于投影误差评分的字典筛选策略，结合STLS算法优化稀疏项选择过程。
3. 数值实验表明该方法在常微分和偏微分方程辨识中提升了准确性和模型可解释性。

## 📝 摘要（中文）

本研究重新审视了基于字典的稀疏回归方法，特别是序列阈值最小二乘法（STLS），并提出了一种基于评分引导的字典选择策略，为数据驱动建模提供实用指导，重点应用于SINDy类算法。STLS是一种解决ℓ0稀疏最小二乘问题的算法，它通过分裂方法高效求解最小二乘部分，同时使用近端方法处理稀疏项。该算法生成的系数向量分量依赖于投影重构误差（称为评分）和字典项之间的互相关性。本文的第一个贡献是对评分和字典选择策略的理论分析，这可以在原始和弱SINDy框架下理解。其次，在常微分方程和偏微分方程上的数值实验突出了基于评分的筛选方法的有效性，提高了动态系统辨识的准确性和可解释性。这些结果表明，在某些情况下，集成评分引导方法来更精确地优化字典可能有助于SINDy用户增强其数据驱动发现控制方程的鲁棒性。

## 🔬 方法详解

论文的核心方法基于STLS算法框架，该算法通过分裂迭代求解ℓ0稀疏最小二乘问题：每次迭代先固定稀疏模式求解最小二乘，再通过阈值处理更新稀疏系数。关键创新在于引入投影重构误差（评分）作为字典项选择的指导指标，结合字典项间的互相关性分析，动态优化字典库。与现有方法的主要区别在于，传统STLS依赖固定阈值，而本文方法利用评分理论分析实现更智能的字典筛选，增强了稀疏回归的适应性和理论可解释性。

## 📊 实验亮点

在常微分方程和偏微分方程的数值实验中，基于评分的字典选择方法显著提高了系统辨识的准确性，同时增强了模型的可解释性，验证了理论分析的有效性。

## 🎯 应用场景

该方法主要应用于动态系统辨识领域，如基于SINDy算法的数据驱动建模，可用于发现常微分方程、偏微分方程等控制方程，在机器人控制、流体力学、生物系统建模等工程和科学计算中具有实际价值。

## 📄 摘要（原文）

> In this work, we revisit dictionary-based sparse regression, in particular, Sequential Threshold Least Squares (STLS), and propose a score-guided library selection to provide practical guidance for data-driven modeling, with emphasis on SINDy-type algorithms. STLS is an algorithm to solve the $\ell_0$ sparse least-squares problem, which relies on splitting to efficiently solve the least-squares portion while handling the sparse term via proximal methods. It produces coefficient vectors whose components depend on both the projected reconstruction errors, here referred to as the scores, and the mutual coherence of dictionary terms. The first contribution of this work is a theoretical analysis of the score and dictionary-selection strategy. This could be understood in both the original and weak SINDy regime. Second, numerical experiments on ordinary and partial differential equations highlight the effectiveness of score-based screening, improving both accuracy and interpretability in dynamical system identification. These results suggest that integrating score-guided methods to refine the dictionary more accurately may help SINDy users in some cases to enhance their robustness for data-driven discovery of governing equations.

