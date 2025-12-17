---
layout: default
title: Warm Diffusion: Recipe for Blur-Noise Mixture Diffusion Models
---

# Warm Diffusion: Recipe for Blur-Noise Mixture Diffusion Models

**arXiv**: [2511.16904v1](https://arxiv.org/abs/2511.16904) | [PDF](https://arxiv.org/pdf/2511.16904.pdf)

**作者**: Hao-Chien Hsueh, Chi-En Yen, Wen-Hsiao Peng, Ching-Chun Huang

---

## 💡 一句话要点

**提出Warm Diffusion以结合噪声与模糊扩散优势，提升图像生成质量**

**关键词**: `扩散模型` `图像生成` `模糊噪声混合` `谱分析` `去噪去模糊`

## 📋 核心要点

1. 核心问题：热扩散忽略图像相关性，冷扩散缺乏噪声导致数据流形问题
2. 方法要点：联合控制模糊和噪声，利用谱依赖简化去噪与去模糊过程
3. 实验或效果：在多个基准测试中验证模型有效性，改善生成性能

## 📄 摘要（原文）

> Diffusion probabilistic models have achieved remarkable success in generative tasks across diverse data types. While recent studies have explored alternative degradation processes beyond Gaussian noise, this paper bridges two key diffusion paradigms: hot diffusion, which relies entirely on noise, and cold diffusion, which uses only blurring without noise. We argue that hot diffusion fails to exploit the strong correlation between high-frequency image detail and low-frequency structures, leading to random behaviors in the early steps of generation. Conversely, while cold diffusion leverages image correlations for prediction, it neglects the role of noise (randomness) in shaping the data manifold, resulting in out-of-manifold issues and partially explaining its performance drop. To integrate both strengths, we propose Warm Diffusion, a unified Blur-Noise Mixture Diffusion Model (BNMD), to control blurring and noise jointly. Our divide-and-conquer strategy exploits the spectral dependency in images, simplifying score model estimation by disentangling the denoising and deblurring processes. We further analyze the Blur-to-Noise Ratio (BNR) using spectral analysis to investigate the trade-off between model learning dynamics and changes in the data manifold. Extensive experiments across benchmarks validate the effectiveness of our approach for image generation.

