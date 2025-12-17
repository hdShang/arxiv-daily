---
layout: default
title: Physics informed Transformer-VAE for biophysical parameter estimation: PROSAIL model inversion in Sentinel-2 imagery
---

# Physics informed Transformer-VAE for biophysical parameter estimation: PROSAIL model inversion in Sentinel-2 imagery

**arXiv**: [2511.10387v1](https://arxiv.org/abs/2511.10387) | [PDF](https://arxiv.org/pdf/2511.10387.pdf)

**作者**: Prince Mensah, Pelumi Victor Aderinto, Ibrahim Salihu Yusuf, Arnu Pretorius

---

## 💡 一句话要点

**提出物理信息Transformer-VAE以从Sentinel-2影像反演PROSAIL模型，估计植被生物物理参数。**

**关键词**: `植被参数反演` `物理信息深度学习` `PROSAIL模型` `Sentinel-2影像` `自监督学习`

## 📋 核心要点

1. 核心问题：从卫星影像准确反演植被生物物理变量，用于生态系统监测和农业管理。
2. 方法要点：结合Transformer-VAE与PROSAIL模型作为可微分物理解码器，仅用模拟数据训练。
3. 实验或效果：在真实数据集上估计LAI和CCC，性能媲美使用真实影像的先进方法。

## 📄 摘要（原文）

> Accurate retrieval of vegetation biophysical variables from satellite imagery is crucial for ecosystem monitoring and agricultural management. In this work, we propose a physics-informed Transformer-VAE architecture to invert the PROSAIL radiative transfer model for simultaneous estimation of key canopy parameters from Sentinel-2 data. Unlike previous hybrid approaches that require real satellite images for self-supevised training. Our model is trained exclusively on simulated data, yet achieves performance on par with state-of-the-art methods that utilize real imagery. The Transformer-VAE incorporates the PROSAIL model as a differentiable physical decoder, ensuring that inferred latent variables correspond to physically plausible leaf and canopy properties. We demonstrate retrieval of leaf area index (LAI) and canopy chlorophyll content (CCC) on real-world field datasets (FRM4Veg and BelSAR) with accuracy comparable to models trained with real Sentinel-2 data. Our method requires no in-situ labels or calibration on real images, offering a cost-effective and self-supervised solution for global vegetation monitoring. The proposed approach illustrates how integrating physical models with advanced deep networks can improve the inversion of RTMs, opening new prospects for large-scale, physically-constrained remote sensing of vegetation traits.

