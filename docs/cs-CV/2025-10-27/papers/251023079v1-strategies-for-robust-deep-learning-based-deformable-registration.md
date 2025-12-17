---
layout: default
title: Strategies for Robust Deep Learning Based Deformable Registration
---

# Strategies for Robust Deep Learning Based Deformable Registration

**arXiv**: [2510.23079v1](https://arxiv.org/abs/2510.23079) | [PDF](https://arxiv.org/pdf/2510.23079.pdf)

**作者**: Joel Honkamaa, Pekka Marttinen

---

## 💡 一句话要点

**提出MIND特征空间变换和集成策略以提升深度学习形变配准的鲁棒性**

**关键词**: `深度学习形变配准` `鲁棒性提升` `MIND特征空间` `图像配准挑战` `集成策略`

## 📋 核心要点

1. 核心问题：深度学习形变配准方法泛化能力差，难以处理训练数据分布外的图像对比度和模态
2. 方法要点：将图像转换到MIND特征空间后输入模型，并采用特殊集成策略
3. 实验或效果：在LUMIR脑配准挑战中验证，显著提升鲁棒性，集成策略带来小幅稳定改进

## 📄 摘要（原文）

> Deep learning based deformable registration methods have become popular in
> recent years. However, their ability to generalize beyond training data
> distribution can be poor, significantly hindering their usability. LUMIR brain
> registration challenge for Learn2Reg 2025 aims to advance the field by
> evaluating the performance of the registration on contrasts and modalities
> different from those included in the training set. Here we describe our
> submission to the challenge, which proposes a very simple idea for
> significantly improving robustness by transforming the images into MIND feature
> space before feeding them into the model. In addition, a special ensembling
> strategy is proposed that shows a small but consistent improvement.

