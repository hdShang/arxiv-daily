---
layout: default
title: ACE-G: Improving Generalization of Scene Coordinate Regression Through Query Pre-Training
---

# ACE-G: Improving Generalization of Scene Coordinate Regression Through Query Pre-Training

**arXiv**: [2510.11605v1](https://arxiv.org/abs/2510.11605) | [PDF](https://arxiv.org/pdf/2510.11605.pdf)

**作者**: Leonard Bruns, Axel Barroso-Laguna, Tommaso Cavallari, Áron Monszpart, Sowmya Munukutla, Victor Adrian Prisacariu, Eric Brachmann

---

## 💡 一句话要点

**提出ACE-G方法，通过查询预训练提升场景坐标回归的泛化能力**

**关键词**: `场景坐标回归` `视觉重定位` `Transformer预训练` `泛化能力` `地图表示分离`

## 📋 核心要点

1. 核心问题：传统场景坐标回归方法在查询图像条件差异大时泛化能力不足，易过拟合训练视图
2. 方法要点：分离坐标回归器和地图表示，使用通用Transformer预训练于多场景，增强泛化性
3. 实验或效果：在多个挑战性重定位数据集上验证，ACE-G显著提升鲁棒性，保持计算效率

## 📄 摘要（原文）

> Scene coordinate regression (SCR) has established itself as a promising
> learning-based approach to visual relocalization. After mere minutes of
> scene-specific training, SCR models estimate camera poses of query images with
> high accuracy. Still, SCR methods fall short of the generalization capabilities
> of more classical feature-matching approaches. When imaging conditions of query
> images, such as lighting or viewpoint, are too different from the training
> views, SCR models fail. Failing to generalize is an inherent limitation of
> previous SCR frameworks, since their training objective is to encode the
> training views in the weights of the coordinate regressor itself. The regressor
> essentially overfits to the training views, by design. We propose to separate
> the coordinate regressor and the map representation into a generic transformer
> and a scene-specific map code. This separation allows us to pre-train the
> transformer on tens of thousands of scenes. More importantly, it allows us to
> train the transformer to generalize from mapping images to unseen query images
> during pre-training. We demonstrate on multiple challenging relocalization
> datasets that our method, ACE-G, leads to significantly increased robustness
> while keeping the computational footprint attractive.

