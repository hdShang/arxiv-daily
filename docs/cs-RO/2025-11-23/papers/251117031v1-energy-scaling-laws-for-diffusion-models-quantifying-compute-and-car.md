---
layout: default
title: Energy Scaling Laws for Diffusion Models: Quantifying Compute and Carbon Emissions in Image Generation
---

# Energy Scaling Laws for Diffusion Models: Quantifying Compute and Carbon Emissions in Image Generation

**arXiv**: [2511.17031v1](https://arxiv.org/abs/2511.17031) | [PDF](https://arxiv.org/pdf/2511.17031.pdf)

**作者**: Aniketh Iyengar, Jiaqi Han, Boris Ruf, Vincent Grari, Marcin Detyniecki, Stefano Ermon

---

## 💡 一句话要点

**提出基于计算复杂度的扩散模型能耗预测方法，以支持可持续AI部署。**

**关键词**: `扩散模型` `能耗预测` `缩放定律` `GPU能耗` `可持续AI`

## 📋 核心要点

1. 扩散模型图像生成能耗高，缺乏跨模型和硬件的预测方法。
2. 采用Kaplan缩放定律，分解推理过程，假设去噪操作主导能耗。
3. 多模型和GPU实验验证预测准确性高，支持跨架构泛化。

## 📄 摘要（原文）

> The rapidly growing computational demands of diffusion models for image generation have raised significant concerns about energy consumption and environmental impact. While existing approaches to energy optimization focus on architectural improvements or hardware acceleration, there is a lack of principled methods to predict energy consumption across different model configurations and hardware setups. We propose an adaptation of Kaplan scaling laws to predict GPU energy consumption for diffusion models based on computational complexity (FLOPs). Our approach decomposes diffusion model inference into text encoding, iterative denoising, and decoding components, with the hypothesis that denoising operations dominate energy consumption due to their repeated execution across multiple inference steps. We conduct comprehensive experiments across four state-of-the-art diffusion models (Stable Diffusion 2, Stable Diffusion 3.5, Flux, and Qwen) on three GPU architectures (NVIDIA A100, A4000, A6000), spanning various inference configurations including resolution (256x256 to 1024x1024), precision (fp16/fp32), step counts (10-50), and classifier-free guidance settings. Our energy scaling law achieves high predictive accuracy within individual architectures (R-squared > 0.9) and exhibits strong cross-architecture generalization, maintaining high rank correlations across models and enabling reliable energy estimation for unseen model-hardware combinations. These results validate the compute-bound nature of diffusion inference and provide a foundation for sustainable AI deployment planning and carbon footprint estimation.

