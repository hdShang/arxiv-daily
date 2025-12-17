---
layout: default
title: Simultaneous Image Quality Improvement and Artefacts Correction in Accelerated MRI
---

# Simultaneous Image Quality Improvement and Artefacts Correction in Accelerated MRI

**arXiv**: [2511.23274v1](https://arxiv.org/abs/2511.23274) | [PDF](https://arxiv.org/pdf/2511.23274.pdf)

**作者**: Georgia Kanli, Daniele Perlo, Selma Boudissa, Radovan Jirik, Olivier Keunen

---

## 💡 一句话要点

**提出USArt模型以同时加速MRI重建并校正噪声与运动伪影**

**关键词**: `MRI加速重建` `伪影校正` `深度学习模型` `欠采样策略` `图像质量恢复`

## 📋 核心要点

1. 核心问题：加速MRI采集导致图像质量下降，且真实场景中图像易受噪声和运动伪影影响，现有方法未同时处理这两类退化。
2. 方法要点：采用双子模型架构，针对笛卡尔采样的2D脑解剖图像，从欠采样数据中恢复高质量图像并校正伪影。
3. 实验或效果：在多种欠采样策略和退化水平下测试，梯度欠采样策略效果最佳，实现最高5倍加速且图像信噪比和对比度显著提升。

## 📄 摘要（原文）

> MR data are acquired in the frequency domain, known as k-space. Acquiring high-quality and high-resolution MR images can be time-consuming, posing a significant challenge when multiple sequences providing complementary contrast information are needed or when the patient is unable to remain in the scanner for an extended period of time. Reducing k-space measurements is a strategy to speed up acquisition, but often leads to reduced quality in reconstructed images. Additionally, in real-world MRI, both under-sampled and full-sampled images are prone to artefacts, and correcting these artefacts is crucial for maintaining diagnostic accuracy. Deep learning methods have been proposed to restore image quality from under-sampled data, while others focused on the correction of artefacts that result from the noise or motion. No approach has however been proposed so far that addresses both acceleration and artefacts correction, limiting the performance of these models when these degradation factors occur simultaneously. To address this gap, we present a method for recovering high-quality images from under-sampled data with simultaneously correction for noise and motion artefact called USArt (Under-Sampling and Artifact correction model). Customized for 2D brain anatomical images acquired with Cartesian sampling, USArt employs a dual sub-model approach. The results demonstrate remarkable increase of signal-to-noise ratio (SNR) and contrast in the images restored. Various under-sampling strategies and degradation levels were explored, with the gradient under-sampling strategy yielding the best outcomes. We achieved up to 5x acceleration and simultaneously artefacts correction without significant degradation, showcasing the model's robustness in real-world settings.

