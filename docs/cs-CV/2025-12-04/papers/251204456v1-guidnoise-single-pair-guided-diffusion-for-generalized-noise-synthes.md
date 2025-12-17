---
layout: default
title: GuidNoise: Single-Pair Guided Diffusion for Generalized Noise Synthesis
---

# GuidNoise: Single-Pair Guided Diffusion for Generalized Noise Synthesis

**arXiv**: [2512.04456v1](https://arxiv.org/abs/2512.04456) | [PDF](https://arxiv.org/pdf/2512.04456.pdf)

**作者**: Changjin Kim, HyeokJun Lee, YoungJoon Yoo

---

## 💡 一句话要点

**提出GuidNoise，利用单对图像引导扩散模型实现广义噪声合成，以解决真实噪声数据获取成本高的问题。**

**关键词**: `噪声合成` `扩散模型` `图像去噪` `数据增强` `单对引导` `广义噪声`

## 📋 核心要点

1. 核心问题：现有噪声合成方法依赖相机元数据和大量噪声-干净图像对，泛化能力有限且数据获取成本高。
2. 方法要点：引入GuidNoise，基于单对图像引导，采用GAFM和噪声感知细化损失优化扩散模型，无需额外元数据。
3. 实验或效果：GuidNoise能合成高质量噪声图像，增强训练数据，提升去噪性能，尤其在轻量模型和有限数据场景下。

## 📄 摘要（原文）

> Recent image denoising methods have leveraged generative modeling for real noise synthesis to address the costly acquisition of real-world noisy data. However, these generative models typically require camera metadata and extensive target-specific noisy-clean image pairs, often showing limited generalization between settings. In this paper, to mitigate the prerequisites, we propose a Single-Pair Guided Diffusion for generalized noise synthesis GuidNoise, which uses a single noisy/clean pair as the guidance, often easily obtained by itself within a training set. To train GuidNoise, which generates synthetic noisy images from the guidance, we introduce a guidance-aware affine feature modification (GAFM) and a noise-aware refine loss to leverage the inherent potential of diffusion models. This loss function refines the diffusion model's backward process, making the model more adept at generating realistic noise distributions. The GuidNoise synthesizes high-quality noisy images under diverse noise environments without additional metadata during both training and inference. Additionally, GuidNoise enables the efficient generation of noisy-clean image pairs at inference time, making synthetic noise readily applicable for augmenting training data. This self-augmentation significantly improves denoising performance, especially in practical scenarios with lightweight models and limited training data. The code is available at https://github.com/chjinny/GuidNoise.

