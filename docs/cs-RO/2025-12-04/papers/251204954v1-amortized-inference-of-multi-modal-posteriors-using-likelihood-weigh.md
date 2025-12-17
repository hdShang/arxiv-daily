---
layout: default
title: Amortized Inference of Multi-Modal Posteriors using Likelihood-Weighted Normalizing Flows
---

# Amortized Inference of Multi-Modal Posteriors using Likelihood-Weighted Normalizing Flows

**arXiv**: [2512.04954v1](https://arxiv.org/abs/2512.04954) | [PDF](https://arxiv.org/pdf/2512.04954.pdf)

**作者**: Rajneil Baruah

---

## 💡 一句话要点

**提出基于似然加权归一化流的摊销后验估计方法，以解决高维逆问题中多模态后验推断的挑战。**

**关键词**: `归一化流` `摊销推断` `多模态后验` `似然加权采样` `高斯混合模型` `高维逆问题`

## 📋 核心要点

1. 核心问题：高维逆问题中理论参数的后验推断，传统方法依赖后验训练样本且难以处理多模态分布。
2. 方法要点：使用似然加权重要性采样训练归一化流，实现摊销后验估计，无需后验样本；引入高斯混合模型初始化以匹配目标模态基数，改善多模态捕获。
3. 实验或效果：在2D和3D多模态基准任务中验证方法有效性，通过距离和散度度量显示重建保真度显著提升。

## 📄 摘要（原文）

> We present a novel technique for amortized posterior estimation using Normalizing Flows trained with likelihood-weighted importance sampling. This approach allows for the efficient inference of theoretical parameters in high-dimensional inverse problems without the need for posterior training samples. We implement the method on multi-modal benchmark tasks in 2D and 3D to check for the efficacy. A critical observation of our study is the impact of the topology of the base distributions on the modelled posteriors. We find that standard unimodal base distributions fail to capture disconnected support, resulting in spurious probability bridges between modes. We demonstrate that initializing the flow with a Gaussian Mixture Model that matches the cardinality of the target modes significantly improves reconstruction fidelity, as measured by some distance and divergence metrics.

