---
layout: default
title: Evaluating Singular Value Thresholds for DNN Weight Matrices based on Random Matrix Theory
---

# Evaluating Singular Value Thresholds for DNN Weight Matrices based on Random Matrix Theory

**arXiv**: [2512.12911v1](https://arxiv.org/abs/2512.12911) | [PDF](https://arxiv.org/pdf/2512.12911.pdf)

**作者**: Kohei Nishikawa, Koki Shimizu, Hashiguchi Hiroki

---

## 💡 一句话要点

**提出基于随机矩阵理论的奇异值阈值评估方法，用于深度神经网络权重矩阵的低秩近似。**

**关键词**: `奇异值分解` `低秩近似` `随机矩阵理论` `深度神经网络` `权重矩阵` `噪声去除`

## 📋 核心要点

1. 核心问题：评估奇异值分解低秩近似中去除噪声相关奇异值的阈值是否合适。
2. 方法要点：将权重矩阵建模为信号与噪声之和，基于随机矩阵理论设定阈值，并引入余弦相似度指标评估阈值。
3. 实验或效果：通过数值实验比较两种阈值估计方法，验证所提评估指标的有效性。

## 📄 摘要（原文）

> This study evaluates thresholds for removing singular values from singular value decomposition-based low-rank approximations of deep neural network weight matrices. Each weight matrix is modeled as the sum of signal and noise matrices. The low-rank approximation is obtained by removing noise-related singular values using a threshold based on random matrix theory. To assess the adequacy of this threshold, we propose an evaluation metric based on the cosine similarity between the singular vectors of the signal and original weight matrices. The proposed metric is used in numerical experiments to compare two threshold estimation methods.

