---
layout: default
title: DeepRFTv2: Kernel-level Learning for Image Deblurring
---

# DeepRFTv2: Kernel-level Learning for Image Deblurring

**arXiv**: [2511.21132v1](https://arxiv.org/abs/2511.21132) | [PDF](https://arxiv.org/pdf/2511.21132.pdf)

**作者**: Xintian Mao, Haofei Song, Yin-Nian Liu, Qingli Li, Yan Wang

---

## 💡 一句话要点

**提出傅里叶核估计器以改进图像去模糊，实现核级学习**

**关键词**: `图像去模糊` `核估计` `傅里叶变换` `多尺度架构` `特征卷积`

## 📋 核心要点

1. 核心问题：现有去模糊网络多为像素级学习，无法理解模糊本质。
2. 方法要点：在傅里叶空间激活，将卷积转为乘法，估计核并卷积特征。
3. 实验或效果：在运动去模糊上达到SOTA，核估计器可学习物理意义核。

## 📄 摘要（原文）

> It is well-known that if a network aims to learn how to deblur, it should understand the blur process. Blurring is naturally caused by the convolution of the sharp image with the blur kernel. Thus, allowing the network to learn the blur process in the kernel-level can significantly improve the image deblurring performance. But, current deep networks are still at the pixel-level learning stage, either performing end-to-end pixel-level restoration or stage-wise pseudo kernel-level restoration, failing to enable the deblur model to understand the essence of the blur. To this end, we propose Fourier Kernel Estimator (FKE), which considers the activation operation in Fourier space and converts the convolution problem in the spatial domain to a multiplication problem in Fourier space. Our FKE, jointly optimized with the deblur model, enables the network to learn the kernel-level blur process with low complexity and without any additional supervision. Furthermore, we change the convolution object of the kernel from ``image" to network extracted ``feature", whose rich semantic and structural information is more suitable to blur process learning. With the convolution of the feature and the estimated kernel, our model can learn the essence of blur in kernel-level. To further improve the efficiency of feature extraction, we design a decoupled multi-scale architecture with multiple hierarchical sub-unets with a reversible strategy, which allows better multi-scale encoding and decoding in low training memory. Extensive experiments indicate that our method achieves state-of-the-art motion deblurring results and show potential for handling other kernel-related problems. Analysis also shows our kernel estimator is able to learn physically meaningful kernels. The code will be available at https://github.com/DeepMed-Lab-ECNU/Single-Image-Deblur.

