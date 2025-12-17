---
layout: default
title: Elastic-Net Multiple Kernel Learning: Combining Multiple Data Sources for Prediction
---

# Elastic-Net Multiple Kernel Learning: Combining Multiple Data Sources for Prediction

**arXiv**: [2512.11547v1](https://arxiv.org/abs/2512.11547) | [PDF](https://arxiv.org/pdf/2512.11547.pdf)

**作者**: Janaina Mourão-Miranda, Zakria Hussain, Konstantinos Tsirlis, Christophe Phillips, John Shawe-Taylor

---

## 💡 一句话要点

**提出弹性网多核学习以结合相关核进行稀疏可解释预测，应用于神经影像学。**

**关键词**: `多核学习` `弹性网正则化` `稀疏模型` `神经影像学` `支持向量机` `核岭回归`

## 📋 核心要点

1. 多核学习整合多数据源，弹性网正则化促进稀疏性和相关核选择。
2. 新方法提供核权重的解析更新，支持SVM和核岭回归算法实现。
3. 在神经影像应用中，性能优于或匹配l1正则化，模型更稀疏可解释。

## 📄 摘要（原文）

> Multiple Kernel Learning (MKL) models combine several kernels in supervised and unsupervised settings to integrate multiple data representations or sources, each represented by a different kernel. MKL seeks an optimal linear combination of base kernels that maximizes a generalized performance measure under a regularization constraint. Various norms have been used to regularize the kernel weights, including $l1$, $l2$ and $lp$, as well as the "elastic-net" penalty, which combines $l1$- and $l2$-norm to promote both sparsity and the selection of correlated kernels. This property makes elastic-net regularized MKL (ENMKL) especially valuable when model interpretability is critical and kernels capture correlated information, such as in neuroimaging. Previous ENMKL methods have followed a two-stage procedure: fix kernel weights, train a support vector machine (SVM) with the weighted kernel, and then update the weights via gradient descent, cutting-plane methods, or surrogate functions. Here, we introduce an alternative ENMKL formulation that yields a simple analytical update for the kernel weights. We derive explicit algorithms for both SVM and kernel ridge regression (KRR) under this framework, and implement them in the open-source Pattern Recognition for Neuroimaging Toolbox (PRoNTo). We evaluate these ENMKL algorithms against $l1$-norm MKL and against SVM (or KRR) trained on the unweighted sum of kernels across three neuroimaging applications. Our results show that ENMKL matches or outperforms $l1$-norm MKL in all tasks and only underperforms standard SVM in one scenario. Crucially, ENMKL produces sparser, more interpretable models by selectively weighting correlated kernels.

