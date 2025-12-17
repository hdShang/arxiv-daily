---
layout: default
title: Seeing Clearly and Deeply: An RGBD Imaging Approach with a Bio-inspired Monocentric Design
---

# Seeing Clearly and Deeply: An RGBD Imaging Approach with a Bio-inspired Monocentric Design

**arXiv**: [2510.25314v1](https://arxiv.org/abs/2510.25314) | [PDF](https://arxiv.org/pdf/2510.25314.pdf)

**作者**: Zongxi Yu, Xiaolong Qian, Shaohua Gao, Qi Jiang, Yao Gao, Kailun Yang, Kaiwei Wang

---

## 💡 一句话要点

**提出仿生单中心成像框架，通过光学-算法协同设计实现紧凑RGBD成像。**

**关键词**: `RGBD成像` `仿生光学` `单中心透镜` `深度估计` `图像恢复` `协同设计`

## 📋 核心要点

1. 核心问题：紧凑光学RGB模糊与单目深度估计依赖不可靠语义先验。
2. 方法要点：设计仿生全球面单中心透镜，编码深度至点扩散函数，无需复杂元件。
3. 实验效果：深度估计Abs Rel 0.026，图像恢复SSIM 0.960，优于现有方法。

## 📄 摘要（原文）

> Achieving high-fidelity, compact RGBD imaging presents a dual challenge:
> conventional compact optics struggle with RGB sharpness across the entire
> depth-of-field, while software-only Monocular Depth Estimation (MDE) is an
> ill-posed problem reliant on unreliable semantic priors. While deep optics with
> elements like DOEs can encode depth, they introduce trade-offs in fabrication
> complexity and chromatic aberrations, compromising simplicity. To address this,
> we first introduce a novel bio-inspired all-spherical monocentric lens, around
> which we build the Bionic Monocentric Imaging (BMI) framework, a holistic
> co-design. This optical design naturally encodes depth into its depth-varying
> Point Spread Functions (PSFs) without requiring complex diffractive or freeform
> elements. We establish a rigorous physically-based forward model to generate a
> synthetic dataset by precisely simulating the optical degradation process. This
> simulation pipeline is co-designed with a dual-head, multi-scale reconstruction
> network that employs a shared encoder to jointly recover a high-fidelity
> All-in-Focus (AiF) image and a precise depth map from a single coded capture.
> Extensive experiments validate the state-of-the-art performance of the proposed
> framework. In depth estimation, the method attains an Abs Rel of 0.026 and an
> RMSE of 0.130, markedly outperforming leading software-only approaches and
> other deep optics systems. For image restoration, the system achieves an SSIM
> of 0.960 and a perceptual LPIPS score of 0.082, thereby confirming a superior
> balance between image fidelity and depth accuracy. This study illustrates that
> the integration of bio-inspired, fully spherical optics with a joint
> reconstruction algorithm constitutes an effective strategy for addressing the
> intrinsic challenges in high-performance compact RGBD imaging. Source code will
> be publicly available at https://github.com/ZongxiYu-ZJU/BMI.

