---
layout: default
title: Trans-defense: Transformer-based Denoiser for Adversarial Defense with Spatial-Frequency Domain Representation
---

# Trans-defense: Transformer-based Denoiser for Adversarial Defense with Spatial-Frequency Domain Representation

**arXiv**: [2510.27245v1](https://arxiv.org/abs/2510.27245) | [PDF](https://arxiv.org/pdf/2510.27245.pdf)

**作者**: Alik Pramanick, Mayank Bansal, Utkarsh Srivastava, Suklav Ghosh, Arijit Sur

---

## 💡 一句话要点

**提出基于Transformer的空间-频率域去噪方法以防御图像对抗攻击**

**关键词**: `对抗防御` `图像去噪` `Transformer` `空间-频率域` `离散小波变换` `深度神经网络`

## 📋 核心要点

1. 深度神经网络易受对抗攻击，限制其在安全关键系统中的应用
2. 采用两阶段训练：先训练去噪网络，再训练分类器；结合空间和频率域特征
3. 在MNIST等数据集上显著提升分类准确率，优于现有去噪和对抗训练方法

## 📄 摘要（原文）

> In recent times, deep neural networks (DNNs) have been successfully adopted
> for various applications. Despite their notable achievements, it has become
> evident that DNNs are vulnerable to sophisticated adversarial attacks,
> restricting their applications in security-critical systems. In this paper, we
> present two-phase training methods to tackle the attack: first, training the
> denoising network, and second, the deep classifier model. We propose a novel
> denoising strategy that integrates both spatial and frequency domain approaches
> to defend against adversarial attacks on images. Our analysis reveals that
> high-frequency components of attacked images are more severely corrupted
> compared to their lower-frequency counterparts. To address this, we leverage
> Discrete Wavelet Transform (DWT) for frequency analysis and develop a denoising
> network that combines spatial image features with wavelets through a
> transformer layer. Next, we retrain the classifier using the denoised images,
> which enhances the classifier's robustness against adversarial attacks.
> Experimental results across the MNIST, CIFAR-10, and Fashion-MNIST datasets
> reveal that the proposed method remarkably elevates classification accuracy,
> substantially exceeding the performance by utilizing a denoising network and
> adversarial training approaches. The code is available at
> https://github.com/Mayank94/Trans-Defense.

