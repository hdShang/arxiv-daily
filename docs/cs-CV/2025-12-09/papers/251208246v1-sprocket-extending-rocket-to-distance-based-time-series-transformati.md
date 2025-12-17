---
layout: default
title: SPROCKET: Extending ROCKET to Distance-Based Time-Series Transformations With Prototypes
---

# SPROCKET: Extending ROCKET to Distance-Based Time-Series Transformations With Prototypes

**arXiv**: [2512.08246v1](https://arxiv.org/abs/2512.08246) | [PDF](https://arxiv.org/pdf/2512.08246.pdf)

**作者**: Nicholas Harner

---

## 💡 一句话要点

**提出SPROCKET，基于原型的特征变换以增强时间序列分类性能。**

**关键词**: `时间序列分类` `特征工程` `原型学习` `卷积核变换` `集成方法`

## 📋 核心要点

1. 核心问题：传统时间序列分类依赖特征工程，ROCKET等算法使用随机核特征。
2. 方法要点：SPROCKET引入基于原型的特征工程策略，扩展ROCKET的距离变换。
3. 实验或效果：在UCR和UEA数据集上性能可比现有卷积算法，MR-HY-SP集成排名超越HYDRA-MR。

## 📄 摘要（原文）

> Classical Time Series Classification algorithms are dominated by feature engineering strategies. One of the most prominent of these transforms is ROCKET, which achieves strong performance through random kernel features. We introduce SPROCKET (Selected Prototype Random Convolutional Kernel Transform), which implements a new feature engineering strategy based on prototypes. On a majority of the UCR and UEA Time Series Classification archives, SPROCKET achieves performance comparable to existing convolutional algorithms and the new MR-HY-SP ( MultiROCKET-HYDRA-SPROCKET) ensemble's average accuracy ranking exceeds HYDRA-MR, the previous best convolutional ensemble's performance. These experimental results demonstrate that prototype-based feature transformation can enhance both accuracy and robustness in time series classification.

