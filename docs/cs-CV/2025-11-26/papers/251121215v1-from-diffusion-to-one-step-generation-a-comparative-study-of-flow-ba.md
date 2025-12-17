---
layout: default
title: From Diffusion to One-Step Generation: A Comparative Study of Flow-Based Models with Application to Image Inpainting
---

# From Diffusion to One-Step Generation: A Comparative Study of Flow-Based Models with Application to Image Inpainting

**arXiv**: [2511.21215v1](https://arxiv.org/abs/2511.21215) | [PDF](https://arxiv.org/pdf/2511.21215.pdf)

**作者**: Umang Agarwal, Rudraksh Sangore, Sumit Laddha

---

## 💡 一句话要点

**比较扩散与流模型，提出单步生成方法并应用于图像修复**

**关键词**: `生成模型比较` `单步图像生成` `图像修复` `条件流匹配` `扩散模型优化` `小参数架构`

## 📋 核心要点

1. 核心问题：扩散模型迭代采样慢，需高效单步生成方法。
2. 方法要点：比较DDPM、CFM和MeanFlow，后者建模平均速度实现单步生成。
3. 实验效果：MeanFlow单步FID 29.15，推理时间减少50倍；修复模型PSNR提升73%。

## 📄 摘要（原文）

> We present a comprehensive comparative study of three generative modeling paradigms: Denoising Diffusion Probabilistic Models (DDPM), Conditional Flow Matching (CFM), and MeanFlow. While DDPM and CFM require iterative sampling, MeanFlow enables direct one-step generation by modeling the average velocity over time intervals. We implement all three methods using a unified TinyUNet architecture (<1.5M parameters) on CIFAR-10, demonstrating that CFM achieves an FID of 24.15 with 50 steps, significantly outperforming DDPM (FID 402.98). MeanFlow achieves FID 29.15 with single-step sampling -- a 50X reduction in inference time. We further extend CFM to image inpainting, implementing mask-guided sampling with four mask types (center, random bbox, irregular, half). Our fine-tuned inpainting model achieves substantial improvements: PSNR increases from 4.95 to 8.57 dB on center masks (+73%), and SSIM improves from 0.289 to 0.418 (+45%), demonstrating the effectiveness of inpainting-aware training.

