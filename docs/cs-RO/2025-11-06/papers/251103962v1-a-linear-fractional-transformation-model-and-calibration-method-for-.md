---
layout: default
title: A Linear Fractional Transformation Model and Calibration Method for Light Field Camera
---

# A Linear Fractional Transformation Model and Calibration Method for Light Field Camera

**arXiv**: [2511.03962v1](https://arxiv.org/abs/2511.03962) | [PDF](https://arxiv.org/pdf/2511.03962.pdf)

**作者**: Zhong Chen, Changfeng Chen

---

## 💡 一句话要点

**提出线性分式变换模型以解决光场相机内部参数标定问题**

**关键词**: `光场相机标定` `线性分式变换` `3D重建` `最小二乘法` `非线性优化`

## 📋 核心要点

1. 核心问题：光场相机内部参数标定对3D重建至关重要但具挑战性
2. 方法要点：引入LFT参数α解耦主镜头与微透镜阵列，采用最小二乘解析解和非线性优化
3. 实验或效果：在物理和模拟数据上验证性能，并加速原始光场图像模拟

## 📄 摘要（原文）

> Accurate calibration of internal parameters is a crucial yet challenging
> prerequisite for 3D reconstruction using light field cameras. In this paper, we
> propose a linear fractional transformation(LFT) parameter $\alpha$ to decoupled
> the main lens and micro lens array (MLA). The proposed method includes an
> analytical solution based on least squares, followed by nonlinear refinement.
> The method for detecting features from the raw images is also introduced.
> Experimental results on both physical and simulated data have verified the
> performance of proposed method. Based on proposed model, the simulation of raw
> light field images becomes faster, which is crucial for data-driven deep
> learning methods. The corresponding code can be obtained from the author's
> website.

