---
layout: default
title: Balanced conic rectified flow
---

# Balanced conic rectified flow

**arXiv**: [2510.25229v1](https://arxiv.org/abs/2510.25229) | [PDF](https://arxiv.org/pdf/2510.25229.pdf)

**作者**: Kim Shin Seong, Mingi Kwon, Jaeseok Jeong, Youngjung Uh

---

## 💡 一句话要点

**提出平衡锥形整流流，通过引入真实图像减少对生成数据的依赖**

**关键词**: `整流流模型` `ODE路径学习` `生成对抗网络` `图像生成` `计算效率优化`

## 📋 核心要点

1. 整流流模型依赖大量生成数据，计算成本高且易偏向生成数据
2. 方法在训练中结合真实图像，保留其ODE路径，减少生成数据需求
3. 在CIFAR-10上FID得分显著提升，路径更直，避免饱和，分布保持更好

## 📄 摘要（原文）

> Rectified flow is a generative model that learns smooth transport mappings
> between two distributions through an ordinary differential equation (ODE).
> Unlike diffusion-based generative models, which require costly numerical
> integration of a generative ODE to sample images with state-of-the-art quality,
> rectified flow uses an iterative process called reflow to learn smooth and
> straight ODE paths. This allows for relatively simple and efficient generation
> of high-quality images. However, rectified flow still faces several challenges.
> 1) The reflow process requires a large number of generative pairs to preserve
> the target distribution, leading to significant computational costs. 2) Since
> the model is typically trained using only generated image pairs, its
> performance heavily depends on the 1-rectified flow model, causing it to become
> biased towards the generated data.
>   In this work, we experimentally expose the limitations of the original
> rectified flow and propose a novel approach that incorporates real images into
> the training process. By preserving the ODE paths for real images, our method
> effectively reduces reliance on large amounts of generated data. Instead, we
> demonstrate that the reflow process can be conducted efficiently using a much
> smaller set of generated and real images. In CIFAR-10, we achieved
> significantly better FID scores, not only in one-step generation but also in
> full-step simulations, while using only of the generative pairs compared to the
> original method. Furthermore, our approach induces straighter paths and avoids
> saturation on generated images during reflow, leading to more robust ODE
> learning while preserving the distribution of real images.

