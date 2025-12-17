---
layout: default
title: Supervised learning pays attention
---

# Supervised learning pays attention

**arXiv**: [2512.09912v1](https://arxiv.org/abs/2512.09912) | [PDF](https://arxiv.org/pdf/2512.09912.pdf)

**作者**: Erin Craig, Robert Tibshirani

---

## 💡 一句话要点

**提出注意力加权方法，将监督学习适配于表格数据以提升预测性能与可解释性。**

**关键词**: `注意力加权` `监督学习` `表格数据` `可解释性` `局部模型` `异质数据`

## 📋 核心要点

1. 核心问题：传统监督学习在异质数据中难以灵活拟合个性化模型，且缺乏可解释性。
2. 方法要点：通过注意力加权训练数据，为每个测试点拟合局部模型，强调预测性特征和交互。
3. 实验或效果：在真实和模拟数据集中，该方法提高预测性能，理论证明在已知子群结构下降低均方误差。

## 📄 摘要（原文）

> In-context learning with attention enables large neural networks to make context-specific predictions by selectively focusing on relevant examples. Here, we adapt this idea to supervised learning procedures such as lasso regression and gradient boosting, for tabular data. Our goals are to (1) flexibly fit personalized models for each prediction point and (2) retain model simplicity and interpretability.
>   Our method fits a local model for each test observation by weighting the training data according to attention, a supervised similarity measure that emphasizes features and interactions that are predictive of the outcome. Attention weighting allows the method to adapt to heterogeneous data in a data-driven way, without requiring cluster or similarity pre-specification. Further, our approach is uniquely interpretable: for each test observation, we identify which features are most predictive and which training observations are most relevant. We then show how to use attention weighting for time series and spatial data, and we present a method for adapting pretrained tree-based models to distributional shift using attention-weighted residual corrections. Across real and simulated datasets, attention weighting improves predictive performance while preserving interpretability, and theory shows that attention-weighting linear models attain lower mean squared error than the standard linear model under mixture-of-models data-generating processes with known subgroup structure.

