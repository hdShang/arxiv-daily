---
layout: default
title: Physics-Informed Graph Neural Network with Frequency-Aware Learning for Optical Aberration Correction
---

# Physics-Informed Graph Neural Network with Frequency-Aware Learning for Optical Aberration Correction

**arXiv**: [2512.05683v1](https://arxiv.org/abs/2512.05683) | [PDF](https://arxiv.org/pdf/2512.05683.pdf)

**作者**: Yong En Kok, Bowen Deng, Alexander Bentley, Andrew J. Parkes, Michael G. Somekh, Amanda J. Wright, Michael P. Pound

---

## 💡 一句话要点

**提出ZRNet框架，结合物理先验与频域学习，用于显微图像的光学像差校正与Zernike系数预测。**

**关键词**: `光学像差校正` `物理信息图神经网络` `Zernike多项式` `频域学习` `显微图像恢复`

## 📋 核心要点

1. 核心问题：显微成像中光学像差严重降低图像质量，现有方法常忽略波前畸变的物理原理，难以处理复杂大振幅像差。
2. 方法要点：设计Zernike图模块建模Zernike多项式间物理关系，并引入频域对齐损失确保图像恢复与系数预测的物理一致性。
3. 实验或效果：在CytoImageNet数据集上验证，在多种显微模态和生物样本中，图像恢复与Zernike系数预测均达到先进性能。

## 📄 摘要（原文）

> Optical aberrations significantly degrade image quality in microscopy, particularly when imaging deeper into samples. These aberrations arise from distortions in the optical wavefront and can be mathematically represented using Zernike polynomials. Existing methods often address only mild aberrations on limited sample types and modalities, typically treating the problem as a black-box mapping without leveraging the underlying optical physics of wavefront distortions. We propose ZRNet, a physics-informed framework that jointly performs Zernike coefficient prediction and optical image Restoration. We contribute a Zernike Graph module that explicitly models physical relationships between Zernike polynomials based on their azimuthal degrees-ensuring that learned corrections align with fundamental optical principles. To further enforce physical consistency between image restoration and Zernike prediction, we introduce a Frequency-Aware Alignment (FAA) loss, which better aligns Zernike coefficient prediction and image features in the Fourier domain. Extensive experiments on CytoImageNet demonstrates that our approach achieves state-of-the-art performance in both image restoration and Zernike coefficient prediction across diverse microscopy modalities and biological samples with complex, large-amplitude aberrations. Code is available at https://github.com/janetkok/ZRNet.

