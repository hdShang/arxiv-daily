---
layout: default
title: Generalized Denoising Diffusion Codebook Models (gDDCM): Tokenizing images using a pre-trained diffusion model
---

# Generalized Denoising Diffusion Codebook Models (gDDCM): Tokenizing images using a pre-trained diffusion model

**arXiv**: [2511.13387v1](https://arxiv.org/abs/2511.13387) | [PDF](https://arxiv.org/pdf/2511.13387.pdf)

**作者**: Fei Kong

---

## 💡 一句话要点

**提出广义去噪扩散码书模型以扩展图像压缩到主流扩散模型**

**关键词**: `图像压缩` `扩散模型` `码书模型` `去噪过程` `泛化方法`

## 📋 核心要点

1. DDCM无法应用于DDPM以外的扩散模型，限制了图像压缩的通用性。
2. gDDCM通过替换反向过程噪声，兼容DDPM、基于分数的模型等主流扩散模型。
3. 在CIFAR-10和LSUN Bedroom数据集上验证了方法的泛化性和性能提升。

## 📄 摘要（原文）

> Recently, the Denoising Diffusion Codebook Models (DDCM) was proposed. DDCM leverages the Denoising Diffusion Probabilistic Model (DDPM) and replaces the random noise in the backward process with noise sampled from specific sets according to a predefined rule, thereby enabling image compression. However, DDCM cannot be applied to methods other than DDPM. In this paper, we propose the generalized Denoising Diffusion Compression Model (gDDCM), which extends DDCM to mainstream diffusion models and their variants, including DDPM, Score-Based Models, Consistency Models, and Rectified Flow. We evaluate our method on CIFAR-10 and LSUN Bedroom datasets. Experimental results demonstrate that our approach successfully generalizes DDCM to the aforementioned models and achieves improved performance.

