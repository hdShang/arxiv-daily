---
layout: default
title: GaussDetect-LiNGAM:Causal Direction Identification without Gaussianity test
---

# GaussDetect-LiNGAM:Causal Direction Identification without Gaussianity test

**arXiv**: [2512.03428v1](https://arxiv.org/abs/2512.03428) | [PDF](https://arxiv.org/pdf/2512.03428.pdf)

**作者**: Ziyi Ding, Xiao-Ping Zhang

---

## 💡 一句话要点

**提出GaussDetect-LiNGAM以消除高斯性测试，提升双变量因果发现的效率与鲁棒性。**

**关键词**: `因果发现` `LiNGAM` `高斯性测试` `独立性测试` `双变量分析` `因果推断`

## 📋 核心要点

1. 核心问题：传统LiNGAM方法依赖高斯性测试，易受样本影响且脆弱。
2. 方法要点：利用前向模型噪声高斯性与反向模型残差独立的等价性，替换为核独立性测试。
3. 实验效果：验证等价性，在多样噪声和样本量下保持高一致性，减少测试次数。

## 📄 摘要（原文）

> We propose GaussDetect-LiNGAM, a novel approach for bivariate causal discovery that eliminates the need for explicit Gaussianity tests by leveraging a fundamental equivalence between noise Gaussianity and residual independence in the reverse regression. Under the standard LiNGAM assumptions of linearity, acyclicity, and exogeneity, we prove that the Gaussianity of the forward-model noise is equivalent to the independence between the regressor and residual in the reverse model. This theoretical insight allows us to replace fragile and sample-sensitive Gaussianity tests with robust kernel-based independence tests. Experimental results validate the equivalence and demonstrate that GaussDetect-LiNGAM maintains high consistency across diverse noise types and sample sizes, while reducing the number of tests per decision (TPD). Our method enhances both the efficiency and practical applicability of causal inference, making LiNGAM more accessible and reliable in real-world scenarios.

