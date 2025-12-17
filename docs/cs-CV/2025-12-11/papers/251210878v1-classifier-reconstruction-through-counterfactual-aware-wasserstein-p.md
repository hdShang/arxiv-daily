---
layout: default
title: Classifier Reconstruction Through Counterfactual-Aware Wasserstein Prototypes
---

# Classifier Reconstruction Through Counterfactual-Aware Wasserstein Prototypes

**arXiv**: [2512.10878v1](https://arxiv.org/abs/2512.10878) | [PDF](https://arxiv.org/pdf/2512.10878.pdf)

**作者**: Xuan Zhao, Zhuo Cao, Arya Bangun, Hanno Scharr, Ira Assent

---

## 💡 一句话要点

**提出基于反事实感知Wasserstein原型的分类器重建方法，以提升有限数据下的模型复制效果**

**关键词**: `反事实解释` `模型重建` `Wasserstein原型` `决策边界` `有限数据学习` `代理模型`

## 📋 核心要点

1. 核心问题：在有限标注数据下，反事实样本用于模型重建时易导致决策边界偏移，影响代理模型保真度
2. 方法要点：结合原始数据与反事实样本，通过Wasserstein重心近似类原型，保留类分布结构
3. 实验或效果：多数据集实验显示，该方法提高代理与目标模型间保真度，验证其有效性

## 📄 摘要（原文）

> Counterfactual explanations provide actionable insights by identifying minimal input changes required to achieve a desired model prediction. Beyond their interpretability benefits, counterfactuals can also be leveraged for model reconstruction, where a surrogate model is trained to replicate the behavior of a target model. In this work, we demonstrate that model reconstruction can be significantly improved by recognizing that counterfactuals, which typically lie close to the decision boundary, can serve as informative though less representative samples for both classes. This is particularly beneficial in settings with limited access to labeled data. We propose a method that integrates original data samples with counterfactuals to approximate class prototypes using the Wasserstein barycenter, thereby preserving the underlying distributional structure of each class. This approach enhances the quality of the surrogate model and mitigates the issue of decision boundary shift, which commonly arises when counterfactuals are naively treated as ordinary training instances. Empirical results across multiple datasets show that our method improves fidelity between the surrogate and target models, validating its effectiveness.

