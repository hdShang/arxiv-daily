---
layout: default
title: Latent Diffusion Model without Variational Autoencoder
---

# Latent Diffusion Model without Variational Autoencoder

**arXiv**: [2510.15301v1](https://arxiv.org/abs/2510.15301) | [PDF](https://arxiv.org/pdf/2510.15301.pdf)

**作者**: Minglei Shi, Haolin Wang, Wenzhao Zheng, Ziyang Yuan, Xiaoshi Wu, Xintao Wang, Pengfei Wan, Jie Zhou, Jiwen Lu

---

## 💡 一句话要点

**提出SVG模型以解决潜在扩散模型中VAE导致的效率与语义问题**

**关键词**: `潜在扩散模型` `自监督表示` `视觉生成` `语义空间` `高效训练`

## 📋 核心要点

1. 核心问题：VAE潜在空间缺乏语义分离和判别结构，影响训练效率和任务迁移。
2. 方法要点：利用冻结DINO特征构建语义空间，轻量残差分支补充细节，直接训练扩散模型。
3. 实验或效果：SVG加速训练、支持少步采样、提升生成质量，并保留语义判别能力。

## 📄 摘要（原文）

> Recent progress in diffusion-based visual generation has largely relied on
> latent diffusion models with variational autoencoders (VAEs). While effective
> for high-fidelity synthesis, this VAE+diffusion paradigm suffers from limited
> training efficiency, slow inference, and poor transferability to broader vision
> tasks. These issues stem from a key limitation of VAE latent spaces: the lack
> of clear semantic separation and strong discriminative structure. Our analysis
> confirms that these properties are crucial not only for perception and
> understanding tasks, but also for the stable and efficient training of latent
> diffusion models. Motivated by this insight, we introduce SVG, a novel latent
> diffusion model without variational autoencoders, which leverages
> self-supervised representations for visual generation. SVG constructs a feature
> space with clear semantic discriminability by leveraging frozen DINO features,
> while a lightweight residual branch captures fine-grained details for
> high-fidelity reconstruction. Diffusion models are trained directly on this
> semantically structured latent space to facilitate more efficient learning. As
> a result, SVG enables accelerated diffusion training, supports few-step
> sampling, and improves generative quality. Experimental results further show
> that SVG preserves the semantic and discriminative capabilities of the
> underlying self-supervised representations, providing a principled pathway
> toward task-general, high-quality visual representations.

