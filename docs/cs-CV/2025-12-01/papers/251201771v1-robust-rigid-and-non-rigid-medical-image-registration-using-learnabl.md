---
layout: default
title: Robust Rigid and Non-Rigid Medical Image Registration Using Learnable Edge Kernels
---

# Robust Rigid and Non-Rigid Medical Image Registration Using Learnable Edge Kernels

**arXiv**: [2512.01771v1](https://arxiv.org/abs/2512.01771) | [PDF](https://arxiv.org/pdf/2512.01771.pdf)

**作者**: Ahsan Raza Siyal, Markus Haltmeier, Ruth Steiger, Malik Galijasevic, Elke Ruth Gizewski, Astrid Ellen Grams

---

## 💡 一句话要点

**提出可学习边缘核方法以增强医学图像刚性及非刚性配准的鲁棒性**

**关键词**: `医学图像配准` `可学习边缘核` `刚性配准` `非刚性配准` `多模态对齐`

## 📋 核心要点

1. 医学图像配准面临对比度差异和模态变化等挑战，传统方法效果有限
2. 通过预定义边缘检测核加随机扰动，训练中学习优化边缘特征以提升配准精度
3. 在多个数据集上评估，包括刚性及非刚性场景，均优于现有技术

## 📄 摘要（原文）

> Medical image registration is crucial for various clinical and research applications including disease diagnosis or treatment planning which require alignment of images from different modalities, time points, or subjects. Traditional registration techniques often struggle with challenges such as contrast differences, spatial distortions, and modality-specific variations. To address these limitations, we propose a method that integrates learnable edge kernels with learning-based rigid and non-rigid registration techniques. Unlike conventional layers that learn all features without specific bias, our approach begins with a predefined edge detection kernel, which is then perturbed with random noise. These kernels are learned during training to extract optimal edge features tailored to the task. This adaptive edge detection enhances the registration process by capturing diverse structural features critical in medical imaging. To provide clearer insight into the contribution of each component in our design, we introduce four variant models for rigid registration and four variant models for non-rigid registration. We evaluated our approach using a dataset provided by the Medical University across three setups: rigid registration without skull removal, with skull removal, and non-rigid registration. Additionally, we assessed performance on two publicly available datasets. Across all experiments, our method consistently outperformed state-of-the-art techniques, demonstrating its potential to improve multi-modal image alignment and anatomical structure analysis.

