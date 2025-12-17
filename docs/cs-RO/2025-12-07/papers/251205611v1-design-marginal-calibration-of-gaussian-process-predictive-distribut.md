---
layout: default
title: Design-marginal calibration of Gaussian process predictive distributions: Bayesian and conformal approaches
---

# Design-marginal calibration of Gaussian process predictive distributions: Bayesian and conformal approaches

**arXiv**: [2512.05611v1](https://arxiv.org/abs/2512.05611) | [PDF](https://arxiv.org/pdf/2512.05611.pdf)

**作者**: Aurélien Pion, Emmanuel Vazquez

---

## 💡 一句话要点

**提出两种高斯过程预测分布设计边际校准方法，用于插值场景的校准控制**

**关键词**: `高斯过程校准` `设计边际校准` `贝叶斯方法` `共形预测` `预测分布` `插值设置`

## 📋 核心要点

1. 研究高斯过程预测分布的设计边际校准问题，基于数据条件和设计测度平均化
2. 引入cps-gp和bcr-gp方法，分别采用标准化留一残差和贝叶斯选择规则
3. 通过数值实验比较校准指标和准确性，评估方法在基准函数上的性能

## 📄 摘要（原文）

> We study the calibration of Gaussian process (GP) predictive distributions in the interpolation setting from a design-marginal perspective. Conditioning on the data and averaging over a design measure μ, we formalize μ-coverage for central intervals and μ-probabilistic calibration through randomized probability integral transforms. We introduce two methods. cps-gp adapts conformal predictive systems to GP interpolation using standardized leave-one-out residuals, yielding stepwise predictive distributions with finite-sample marginal calibration. bcr-gp retains the GP posterior mean and replaces the Gaussian residual by a generalized normal model fitted to cross-validated standardized residuals. A Bayesian selection rule-based either on a posterior upper quantile of the variance for conservative prediction or on a cross-posterior Kolmogorov-Smirnov criterion for probabilistic calibration-controls dispersion and tail behavior while producing smooth predictive distributions suitable for sequential design. Numerical experiments on benchmark functions compare cps-gp, bcr-gp, Jackknife+ for GPs, and the full conformal Gaussian process, using calibration metrics (coverage, Kolmogorov-Smirnov, integral absolute error) and accuracy or sharpness through the scaled continuous ranked probability score.

