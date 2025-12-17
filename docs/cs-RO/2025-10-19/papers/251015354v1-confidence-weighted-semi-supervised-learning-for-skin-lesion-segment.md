---
layout: default
title: Confidence-Weighted Semi-Supervised Learning for Skin Lesion Segmentation Using Hybrid CNN-Transformer Networks
---

# Confidence-Weighted Semi-Supervised Learning for Skin Lesion Segmentation Using Hybrid CNN-Transformer Networks

**arXiv**: [2510.15354v1](https://arxiv.org/abs/2510.15354) | [PDF](https://arxiv.org/pdf/2510.15354.pdf)

**作者**: Saqib Qamar

---

## 💡 一句话要点

**提出MIRA-U半监督框架，结合不确定性伪标签和混合CNN-Transformer网络，以解决皮肤病变分割中标注数据不足的问题。**

**关键词**: `皮肤病变分割` `半监督学习` `CNN-Transformer混合网络` `不确定性伪标签` `师生模型` `医学图像分析`

## 📋 核心要点

1. 核心问题：皮肤病变自动分割因标注数据有限而具挑战性，影响早期皮肤癌检测。
2. 方法要点：采用不确定性感知师生伪标签和U形CNN-Transformer架构，提升伪标签质量和边界分割。
3. 实验或效果：在ISIC-2016和PH2数据集上，仅用50%标注数据，DSC达0.9153，IoU达0.8552。

## 📄 摘要（原文）

> Automated skin lesion segmentation through dermoscopic analysis is essential
> for early skin cancer detection, yet remains challenging due to limited
> annotated training data. We present MIRA-U, a semi-supervised framework that
> combines uncertainty-aware teacher-student pseudo-labeling with a hybrid
> CNN-Transformer architecture. Our approach employs a teacher network
> pre-trained via masked image modeling to generate confidence-weighted soft
> pseudo-labels, which guide a U-shaped CNN-Transformer student network featuring
> cross-attention skip connections. This design enhances pseudo-label quality and
> boundary delineation, surpassing reconstruction-based and CNN-only baselines,
> particularly in low-annotation regimes. Extensive evaluation on ISIC-2016 and
> PH2 datasets demonstrates superior performance, achieving a Dice Similarity
> Coefficient (DSC) of 0.9153 and Intersection over Union (IoU) of 0.8552 using
> only 50% labeled data. Code is publicly available on GitHub.

