---
layout: default
title: Mixup Helps Understanding Multimodal Video Better
---

# Mixup Helps Understanding Multimodal Video Better

**arXiv**: [2510.10986v1](https://arxiv.org/abs/2510.10986) | [PDF](https://arxiv.org/pdf/2510.10986.pdf)

**作者**: Xiaoyu Ma, Ding Ding, Hao Chen

---

## 💡 一句话要点

**提出平衡多模态混合方法以解决多模态视频理解中的模态不平衡问题**

**关键词**: `多模态视频理解` `模态不平衡` `混合策略` `泛化性提升` `鲁棒性增强`

## 📋 核心要点

1. 核心问题：多模态模型易过拟合强模态，抑制弱模态贡献。
2. 方法要点：先引入多模态混合，再基于模态贡献动态调整混合比例。
3. 实验或效果：在多个数据集上验证方法提升泛化性和鲁棒性。

## 📄 摘要（原文）

> Multimodal video understanding plays a crucial role in tasks such as action
> recognition and emotion classification by combining information from different
> modalities. However, multimodal models are prone to overfitting strong
> modalities, which can dominate learning and suppress the contributions of
> weaker ones. To address this challenge, we first propose Multimodal Mixup (MM),
> which applies the Mixup strategy at the aggregated multimodal feature level to
> mitigate overfitting by generating virtual feature-label pairs. While MM
> effectively improves generalization, it treats all modalities uniformly and
> does not account for modality imbalance during training. Building on MM, we
> further introduce Balanced Multimodal Mixup (B-MM), which dynamically adjusts
> the mixing ratios for each modality based on their relative contributions to
> the learning objective. Extensive experiments on several datasets demonstrate
> the effectiveness of our methods in improving generalization and multimodal
> robustness.

