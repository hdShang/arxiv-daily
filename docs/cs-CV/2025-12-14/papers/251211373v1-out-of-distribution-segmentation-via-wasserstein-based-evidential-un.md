---
layout: default
title: Out-of-Distribution Segmentation via Wasserstein-Based Evidential Uncertainty
---

# Out-of-Distribution Segmentation via Wasserstein-Based Evidential Uncertainty

**arXiv**: [2512.11373v1](https://arxiv.org/abs/2512.11373) | [PDF](https://arxiv.org/pdf/2512.11373.pdf)

**作者**: Arnold Brosch, Abdelrahman Eldesokey, Michael Felsberg, Kira Maag

---

## 💡 一句话要点

**提出基于Wasserstein损失的证据分割框架，以改进开放世界场景中的未知物体分割性能。**

**关键词**: `未知物体分割` `证据分割` `Wasserstein损失` `Kullback-Leibler正则化` `Dice损失` `开放世界场景`

## 📋 核心要点

1. 核心问题：深度神经网络在语义分割中局限于预定义类别，遇到未知物体时易失败，影响自动驾驶等安全关键应用。
2. 方法要点：使用Wasserstein损失捕捉分布距离并尊重概率单纯形几何，结合Kullback-Leibler正则化和Dice结构一致性项。
3. 实验或效果：相比基于不确定性的方法，本方法提升了未知物体分割性能，具体指标未知。

## 📄 摘要（原文）

> Deep neural networks achieve superior performance in semantic segmentation, but are limited to a predefined set of classes, which leads to failures when they encounter unknown objects in open-world scenarios. Recognizing and segmenting these out-of-distribution (OOD) objects is crucial for safety-critical applications such as automated driving. In this work, we present an evidence segmentation framework using a Wasserstein loss, which captures distributional distances while respecting the probability simplex geometry. Combined with Kullback-Leibler regularization and Dice structural consistency terms, our approach leads to improved OOD segmentation performance compared to uncertainty-based approaches.

