---
layout: default
title: Optimizing the Training Diet: Data Mixture Search for Robust Time Series Forecasting
---

# Optimizing the Training Diet: Data Mixture Search for Robust Time Series Forecasting

**arXiv**: [2512.11546v1](https://arxiv.org/abs/2512.11546) | [PDF](https://arxiv.org/pdf/2512.11546.pdf)

**作者**: Federico Pennino, Maurizio Gabbrielli

---

## 💡 一句话要点

**提出数据混合搜索框架以优化时间序列预测模型的训练数据组成**

**关键词**: `时间序列预测` `数据选择优化` `聚类分析` `Optuna优化` `传感器数据`

## 📋 核心要点

1. 核心问题：标准训练范式假设数据越多越好，但传感器数据常不平衡且冗余，影响模型泛化。
2. 方法要点：使用编码器和聚类划分数据为行为一致簇，通过Optuna优化搜索最佳数据混合比例。
3. 实验或效果：在PMSM数据集上，MSE从1.70提升至1.37，性能改善19.41%。

## 📄 摘要（原文）

> The standard paradigm for training deep learning models on sensor data assumes that more data is always better. However, raw sensor streams are often imbalanced and contain significant redundancy, meaning that not all data points contribute equally to model generalization. In this paper, we show that, in some cases, "less is more" when considering datasets. We do this by reframing the data selection problem: rather than tuning model hyperparameters, we fix the model and optimize the composition of the training data itself. We introduce a framework for discovering the optimal "training diet" from a large, unlabeled time series corpus. Our framework first uses a large-scale encoder and k-means clustering to partition the dataset into distinct, behaviorally consistent clusters. These clusters represent the fundamental 'ingredients' available for training. We then employ the Optuna optimization framework to search the high-dimensional space of possible data mixtures. For each trial, Optuna proposes a specific sampling ratio for each cluster, and a new training set is constructed based on this recipe. A smaller target model is then trained and evaluated. Our experiments reveal that this data-centric search consistently discovers data mixtures that yield models with significantly higher performance compared to baselines trained on the entire dataset. Specifically - evaluated on PMSM dataset - our method improved performance from a baseline MSE of 1.70 to 1.37, a 19.41% improvement.

