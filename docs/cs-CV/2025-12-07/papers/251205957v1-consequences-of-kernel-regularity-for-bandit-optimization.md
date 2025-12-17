---
layout: default
title: Consequences of Kernel Regularity for Bandit Optimization
---

# Consequences of Kernel Regularity for Bandit Optimization

**arXiv**: [2512.05957v1](https://arxiv.org/abs/2512.05957) | [PDF](https://arxiv.org/pdf/2512.05957.pdf)

**作者**: Madison Lee, Tara Javidi

---

## 💡 一句话要点

**通过核谱性质统一分析核正则性与多臂老虎机优化性能，推导多种核的显式遗憾界**

**关键词**: `核正则性` `多臂老虎机优化` `再生核希尔伯特空间` `谱衰减` `遗憾界分析` `混合算法`

## 📋 核心要点

1. 研究核正则性与RKHS函数多臂老虎机优化算法性能的关系
2. 基于各向同性核的谱性质，连接全局核方法与局部平滑方法
3. 推导多种核家族的显式遗憾界，分析混合算法LP-GP-UCB的阶最优性

## 📄 摘要（原文）

> In this work we investigate the relationship between kernel regularity and algorithmic performance in the bandit optimization of RKHS functions. While reproducing kernel Hilbert space (RKHS) methods traditionally rely on global kernel regressors, it is also common to use a smoothness-based approach that exploits local approximations. We show that these perspectives are deeply connected through the spectral properties of isotropic kernels. In particular, we characterize the Fourier spectra of the Matérn, square-exponential, rational-quadratic, $γ$-exponential, piecewise-polynomial, and Dirichlet kernels, and show that the decay rate determines asymptotic regret from both viewpoints. For kernelized bandit algorithms, spectral decay yields upper bounds on the maximum information gain, governing worst-case regret, while for smoothness-based methods, the same decay rates establish Hölder space embeddings and Besov space norm-equivalences, enabling local continuity analysis. These connections show that kernel-based and locally adaptive algorithms can be analyzed within a unified framework. This allows us to derive explicit regret bounds for each kernel family, obtaining novel results in several cases and providing improved analysis for others. Furthermore, we analyze LP-GP-UCB, an algorithm that combines both approaches, augmenting global Gaussian process surrogates with local polynomial estimators. While the hybrid approach does not uniformly dominate specialized methods, it achieves order-optimality across multiple kernel families.

