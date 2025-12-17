---
layout: default
title: QCFace: Image Quality Control for boosting Face Representation & Recognition
---

# QCFace: Image Quality Control for boosting Face Representation & Recognition

**arXiv**: [2510.15289v1](https://arxiv.org/abs/2510.15289) | [PDF](https://arxiv.org/pdf/2510.15289.pdf)

**作者**: Duc-Phuong Doan-Ngo, Thanh-Dang Diep, Thanh Nguyen-Duc, Thanh-Sach LE, Nam Thoai

---

## 💡 一句话要点

**提出QCFace硬边界策略以解决人脸识别中可识别性与身份表示耦合问题**

**关键词**: `人脸识别` `可识别性控制` `硬边界损失` `特征表示` `超球面规划` `质量增强`

## 📋 核心要点

1. 核心问题：软边界约束部分捕获可识别性，导致特征表示弱、梯度重叠和泛化差
2. 方法要点：引入硬边界策略，分离可识别性与身份表示，优化超球面规划
3. 实验或效果：在验证和识别基准上实现SOTA，提供鲁棒可识别性编码

## 📄 摘要（原文）

> Recognizability, a key perceptual factor in human face processing, strongly
> affects the performance of face recognition (FR) systems in both verification
> and identification tasks. Effectively using recognizability to enhance feature
> representation remains challenging. In deep FR, the loss function plays a
> crucial role in shaping how features are embedded. However, current methods
> have two main drawbacks: (i) recognizability is only partially captured through
> soft margin constraints, resulting in weaker quality representation and lower
> discrimination, especially for low-quality or ambiguous faces; (ii) mutual
> overlapping gradients between feature direction and magnitude introduce
> undesirable interactions during optimization, causing instability and confusion
> in hypersphere planning, which may result in poor generalization, and entangled
> representations where recognizability and identity are not cleanly separated.
> To address these issues, we introduce a hard margin strategy - Quality Control
> Face (QCFace), which overcomes the mutual overlapping gradient problem and
> enables the clear decoupling of recognizability from identity representation.
> Based on this strategy, a novel hard-margin-based loss function employs a
> guidance factor for hypersphere planning, simultaneously optimizing for
> recognition ability and explicit recognizability representation. Extensive
> experiments confirm that QCFace not only provides robust and quantifiable
> recognizability encoding but also achieves state-of-the-art performance in both
> verification and identification benchmarks compared to existing
> recognizability-based losses.

