---
layout: default
title: Simulating Distribution Dynamics: Liquid Temporal Feature Evolution for Single-Domain Generalized Object Detection
---

# Simulating Distribution Dynamics: Liquid Temporal Feature Evolution for Single-Domain Generalized Object Detection

**arXiv**: [2511.09909v1](https://arxiv.org/abs/2511.09909) | [PDF](https://arxiv.org/pdf/2511.09909.pdf)

**作者**: Zihao Zhang, Yang Li, Aming Wu, Yahong Han

---

## 💡 一句话要点

**提出液态时序特征演化方法以解决单域泛化目标检测中的动态域偏移问题**

**关键词**: `单域泛化目标检测` `时序特征演化` `液态神经网络` `动态域偏移` `高斯噪声注入` `多尺度高斯模糊`

## 📋 核心要点

1. 核心问题：单域泛化目标检测中，离散数据增强无法捕捉连续动态域偏移，如天气变化。
2. 方法要点：引入时序建模和液态神经网络，模拟特征从源域到潜在分布的渐进演化。
3. 实验或效果：在Diverse Weather和Real-to-Art基准上显著提升泛化性和鲁棒性。

## 📄 摘要（原文）

> In this paper, we focus on Single-Domain Generalized Object Detection (Single-DGOD), aiming to transfer a detector trained on one source domain to multiple unknown domains. Existing methods for Single-DGOD typically rely on discrete data augmentation or static perturbation methods to expand data diversity, thereby mitigating the lack of access to target domain data. However, in real-world scenarios such as changes in weather or lighting conditions, domain shifts often occur continuously and gradually. Discrete augmentations and static perturbations fail to effectively capture the dynamic variation of feature distributions, thereby limiting the model's ability to perceive fine-grained cross-domain differences. To this end, we propose a new method, Liquid Temporal Feature Evolution, which simulates the progressive evolution of features from the source domain to simulated latent distributions by incorporating temporal modeling and liquid neural network-driven parameter adjustment. Specifically, we introduce controllable Gaussian noise injection and multi-scale Gaussian blurring to simulate initial feature perturbations, followed by temporal modeling and a liquid parameter adjustment mechanism to generate adaptive modulation parameters, enabling a smooth and continuous adaptation across domains. By capturing progressive cross-domain feature evolution and dynamically regulating adaptation paths, our method bridges the source-unknown domain distribution gap, significantly boosting generalization and robustness to unseen shifts. Significant performance improvements on the Diverse Weather dataset and Real-to-Art benchmark demonstrate the superiority of our method. Our code is available at https://github.com/2490o/LTFE.

