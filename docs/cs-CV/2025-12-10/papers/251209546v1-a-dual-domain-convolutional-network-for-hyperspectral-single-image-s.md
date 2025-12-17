---
layout: default
title: A Dual-Domain Convolutional Network for Hyperspectral Single-Image Super-Resolution
---

# A Dual-Domain Convolutional Network for Hyperspectral Single-Image Super-Resolution

**arXiv**: [2512.09546v1](https://arxiv.org/abs/2512.09546) | [PDF](https://arxiv.org/pdf/2512.09546.pdf)

**作者**: Murat Karayaka, Usman Muhammad, Jorma Laaksonen, Md Ziaul Hoque, Tapio Seppänen

---

## 💡 一句话要点

**提出轻量级双域卷积网络DDSRNet，结合空间域与离散小波变换，用于高光谱单图像超分辨率。**

**关键词**: `高光谱图像超分辨率` `双域学习` `离散小波变换` `轻量级网络` `空间域增强` `频率域分解`

## 📋 核心要点

1. 核心问题：高光谱图像超分辨率需平衡性能与计算成本，传统方法可能效率不足。
2. 方法要点：设计Spatial-Net提取浅层特征，利用DWT分解低频结构，共享CNN增强高频子带。
3. 实验或效果：在三个高光谱数据集上实现竞争性性能，计算成本低，验证了双域学习的有效性。

## 📄 摘要（原文）

> This study presents a lightweight dual-domain super-resolution network (DDSRNet) that combines Spatial-Net with the discrete wavelet transform (DWT). Specifically, our proposed model comprises three main components: (1) a shallow feature extraction module, termed Spatial-Net, which performs residual learning and bilinear interpolation; (2) a low-frequency enhancement branch based on the DWT that refines coarse image structures; and (3) a shared high-frequency refinement branch that simultaneously enhances the LH (horizontal), HL (vertical), and HH (diagonal) wavelet subbands using a single CNN with shared weights. As a result, the DWT enables subband decomposition, while the inverse DWT reconstructs the final high-resolution output. By doing so, the integration of spatial- and frequency-domain learning enables DDSRNet to achieve highly competitive performance with low computational cost on three hyperspectral image datasets, demonstrating its effectiveness for hyperspectral image super-resolution.

