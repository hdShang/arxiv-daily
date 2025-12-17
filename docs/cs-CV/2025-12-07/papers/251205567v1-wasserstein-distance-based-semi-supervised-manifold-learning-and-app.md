---
layout: default
title: Wasserstein distance based semi-supervised manifold learning and application to GNSS multi-path detection
---

# Wasserstein distance based semi-supervised manifold learning and application to GNSS multi-path detection

**arXiv**: [2512.05567v1](https://arxiv.org/abs/2512.05567) | [PDF](https://arxiv.org/pdf/2512.05567.pdf)

**作者**: Antoine Blais, Nicolas Couëllan

---

## 💡 一句话要点

**提出基于Wasserstein距离的半监督流形学习方法，应用于GNSS多径干扰检测。**

**关键词**: `半监督学习` `Wasserstein距离` `最优传输` `GNSS多径检测` `图像分类` `流形学习`

## 📋 核心要点

1. 核心问题：利用稀缺标注图像数据学习，解决GNSS多径干扰检测问题。
2. 方法要点：基于最优传输，使用Wasserstein距离作为图像相似性度量，进行隐式图半监督学习。
3. 实验或效果：在多种信号条件下实验，特定超参数下分类准确率显著优于全监督方法。

## 📄 摘要（原文）

> The main objective of this study is to propose an optimal transport based semi-supervised approach to learn from scarce labelled image data using deep convolutional networks. The principle lies in implicit graph-based transductive semi-supervised learning where the similarity metric between image samples is the Wasserstein distance. This metric is used in the label propagation mechanism during learning. We apply and demonstrate the effectiveness of the method on a GNSS real life application. More specifically, we address the problem of multi-path interference detection. Experiments are conducted under various signal conditions. The results show that for specific choices of hyperparameters controlling the amount of semi-supervision and the level of sensitivity to the metric, the classification accuracy can be significantly improved over the fully supervised training method.

