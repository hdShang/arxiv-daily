---
layout: default
title: FARMER: Flow AutoRegressive Transformer over Pixels
---

# FARMER: Flow AutoRegressive Transformer over Pixels

**arXiv**: [2510.23588v1](https://arxiv.org/abs/2510.23588) | [PDF](https://arxiv.org/pdf/2510.23588.pdf)

**作者**: Guangting Zheng, Qinyu Zhao, Tao Yang, Fei Xiao, Zhijie Lin, Jie Wu, Jiajun Deng, Yanyong Zhang, Rui Zhu

---

## 💡 一句话要点

**提出FARMER框架，结合归一化流与自回归模型以解决像素级图像生成中的似然估计难题。**

**关键词**: `归一化流` `自回归模型` `图像生成` `似然估计` `维度缩减` `推理加速`

## 📋 核心要点

1. 核心问题：连续自回归建模在视觉像素数据中面临序列过长和高维空间挑战。
2. 方法要点：使用可逆自回归流将图像转为隐序列，并通过自回归模型建模其分布。
3. 实验或效果：在像素级生成模型中实现竞争性能，提供精确似然和可扩展训练。

## 📄 摘要（原文）

> Directly modeling the explicit likelihood of the raw data distribution is key
> topic in the machine learning area, which achieves the scaling successes in
> Large Language Models by autoregressive modeling. However, continuous AR
> modeling over visual pixel data suffer from extremely long sequences and
> high-dimensional spaces. In this paper, we present FARMER, a novel end-to-end
> generative framework that unifies Normalizing Flows (NF) and Autoregressive
> (AR) models for tractable likelihood estimation and high-quality image
> synthesis directly from raw pixels. FARMER employs an invertible autoregressive
> flow to transform images into latent sequences, whose distribution is modeled
> implicitly by an autoregressive model. To address the redundancy and complexity
> in pixel-level modeling, we propose a self-supervised dimension reduction
> scheme that partitions NF latent channels into informative and redundant
> groups, enabling more effective and efficient AR modeling. Furthermore, we
> design a one-step distillation scheme to significantly accelerate inference
> speed and introduce a resampling-based classifier-free guidance algorithm to
> boost image generation quality. Extensive experiments demonstrate that FARMER
> achieves competitive performance compared to existing pixel-based generative
> models while providing exact likelihoods and scalable training.

