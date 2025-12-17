---
layout: default
title: U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching
---

# U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

**arXiv**: [2510.25210v1](https://arxiv.org/abs/2510.25210) | [PDF](https://arxiv.org/pdf/2510.25210.pdf)

**作者**: Junsheng Zhou, Xingyu Shi, Haichuan Song, Yi Fang, Yu-Shen Liu, Zhizhong Han

---

## 💡 一句话要点

**提出U-CAN无监督点云去噪框架，利用一致性感知噪声匹配解决噪声问题**

**关键词**: `点云去噪` `无监督学习` `噪声匹配` `几何一致性` `图像去噪`

## 📋 核心要点

1. 点云扫描常受噪声干扰，影响下游任务如表面重建和形状理解
2. 采用无监督方法，通过噪声到噪声匹配和多步去噪路径推断，无需干净数据
3. 在点云去噪、上采样和图像去噪基准测试中，优于无监督方法，与监督方法相当

## 📄 摘要（原文）

> Point clouds captured by scanning sensors are often perturbed by noise, which
> have a highly negative impact on downstream tasks (e.g. surface reconstruction
> and shape understanding). Previous works mostly focus on training neural
> networks with noisy-clean point cloud pairs for learning denoising priors,
> which requires extensively manual efforts. In this work, we introduce U-CAN, an
> Unsupervised framework for point cloud denoising with Consistency-Aware
> Noise2Noise matching. Specifically, we leverage a neural network to infer a
> multi-step denoising path for each point of a shape or scene with a noise to
> noise matching scheme. We achieve this by a novel loss which enables
> statistical reasoning on multiple noisy point cloud observations. We further
> introduce a novel constraint on the denoised geometry consistency for learning
> consistency-aware denoising patterns. We justify that the proposed constraint
> is a general term which is not limited to 3D domain and can also contribute to
> the area of 2D image denoising. Our evaluations under the widely used
> benchmarks in point cloud denoising, upsampling and image denoising show
> significant improvement over the state-of-the-art unsupervised methods, where
> U-CAN also produces comparable results with the supervised methods.

