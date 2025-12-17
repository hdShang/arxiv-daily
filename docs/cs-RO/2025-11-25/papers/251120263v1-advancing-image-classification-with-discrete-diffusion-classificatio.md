---
layout: default
title: Advancing Image Classification with Discrete Diffusion Classification Modeling
---

# Advancing Image Classification with Discrete Diffusion Classification Modeling

**arXiv**: [2511.20263v1](https://arxiv.org/abs/2511.20263) | [PDF](https://arxiv.org/pdf/2511.20263.pdf)

**作者**: Omer Belhasin, Shelly Golan, Ran El-Yaniv, Michael Elad

---

## 💡 一句话要点

**提出离散扩散分类建模以提升高不确定性图像分类性能**

**关键词**: `图像分类` `扩散模型` `后验分布建模` `高不确定性处理` `ImageNet基准`

## 📋 核心要点

1. 核心问题：图像分类在高不确定性场景下性能不佳，如图像损坏或数据有限。
2. 方法要点：利用扩散过程建模类标签后验分布，支持概率或离散标签预测。
3. 实验或效果：在ImageNet上优于基线，扩散迭代少且挑战越大增益越高。

## 📄 摘要（原文）

> Image classification is a well-studied task in computer vision, and yet it remains challenging under high-uncertainty conditions, such as when input images are corrupted or training data are limited. Conventional classification approaches typically train models to directly predict class labels from input images, but this might lead to suboptimal performance in such scenarios. To address this issue, we propose Discrete Diffusion Classification Modeling (DiDiCM), a novel framework that leverages a diffusion-based procedure to model the posterior distribution of class labels conditioned on the input image. DiDiCM supports diffusion-based predictions either on class probabilities or on discrete class labels, providing flexibility in computation and memory trade-offs. We conduct a comprehensive empirical study demonstrating the superior performance of DiDiCM over standard classifiers, showing that a few diffusion iterations achieve higher classification accuracy on the ImageNet dataset compared to baselines, with accuracy gains increasing as the task becomes more challenging. We release our code at https://github.com/omerb01/didicm .

