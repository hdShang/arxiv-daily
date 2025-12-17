---
layout: default
title: HQ-DM: Single Hadamard Transformation-Based Quantization-Aware Training for Low-Bit Diffusion Models
---

# HQ-DM: Single Hadamard Transformation-Based Quantization-Aware Training for Low-Bit Diffusion Models

**arXiv**: [2512.05746v1](https://arxiv.org/abs/2512.05746) | [PDF](https://arxiv.org/pdf/2512.05746.pdf)

**作者**: Shizhuo Mao, Hongtao Zou, Qihu Xie, Song Chen, Yi Kang

---

## 💡 一句话要点

**提出HQ-DM框架，通过单哈达玛变换解决低比特扩散模型量化中的激活异常值问题**

**关键词**: `扩散模型` `量化感知训练` `低比特量化` `哈达玛变换` `图像生成` `模型压缩`

## 📋 核心要点

1. 核心问题：现有扩散模型量化方法在低比特场景下因激活矩阵异常值导致性能显著下降
2. 方法要点：采用单哈达玛变换处理激活矩阵，减少异常值同时支持INT卷积并防止权重异常值放大
3. 实验或效果：在ImageNet 256x256数据集上，W4A4和W4A4量化方案相比现有方法提升Inception Score达12.8%和467.73%

## 📄 摘要（原文）

> Diffusion models have demonstrated significant applications in the field of image generation. However, their high computational and memory costs pose challenges for deployment. Model quantization has emerged as a promising solution to reduce storage overhead and accelerate inference. Nevertheless, existing quantization methods for diffusion models struggle to mitigate outliers in activation matrices during inference, leading to substantial performance degradation under low-bit quantization scenarios. To address this, we propose HQ-DM, a novel Quantization-Aware Training framework that applies Single Hadamard Transformation to activation matrices. This approach effectively reduces activation outliers while preserving model performance under quantization. Compared to traditional Double Hadamard Transformation, our proposed scheme offers distinct advantages by seamlessly supporting INT convolution operations while preventing the amplification of weight outliers. For conditional generation on the ImageNet 256x256 dataset using the LDM-4 model, our W4A4 and W4A3 quantization schemes improve the Inception Score by 12.8% and 467.73%, respectively, over the existing state-of-the-art method.

