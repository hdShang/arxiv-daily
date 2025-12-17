---
layout: default
title: Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge
---

# Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge

**arXiv**: [2510.20819v1](https://arxiv.org/abs/2510.20819) | [PDF](https://arxiv.org/pdf/2510.20819.pdf)

**作者**: Nimrod Berman, Omkar Joglekar, Eitan Kosman, Dotan Di Castro, Omri Azencot

---

## 💡 一句话要点

**提出潜在去噪扩散桥模型以解决跨模态翻译的通用性问题**

**关键词**: `跨模态翻译` `扩散模型` `潜在空间学习` `对比对齐` `噪声预测` `多模态生成`

## 📋 核心要点

1. 现有方法依赖共享维度等假设，限制跨模态翻译的通用性。
2. 在共享潜在空间学习桥接，引入对比对齐和预测损失提升语义一致性。
3. 在多种任务如多视图到3D生成中表现优异，验证框架有效性。

## 📄 摘要（原文）

> Recent advances in generative modeling have positioned diffusion models as
> state-of-the-art tools for sampling from complex data distributions. While
> these models have shown remarkable success across single-modality domains such
> as images and audio, extending their capabilities to Modality Translation (MT),
> translating information across different sensory modalities, remains an open
> challenge. Existing approaches often rely on restrictive assumptions, including
> shared dimensionality, Gaussian source priors, and modality-specific
> architectures, which limit their generality and theoretical grounding. In this
> work, we propose the Latent Denoising Diffusion Bridge Model (LDDBM), a
> general-purpose framework for modality translation based on a latent-variable
> extension of Denoising Diffusion Bridge Models. By operating in a shared latent
> space, our method learns a bridge between arbitrary modalities without
> requiring aligned dimensions. We introduce a contrastive alignment loss to
> enforce semantic consistency between paired samples and design a
> domain-agnostic encoder-decoder architecture tailored for noise prediction in
> latent space. Additionally, we propose a predictive loss to guide training
> toward accurate cross-domain translation and explore several training
> strategies to improve stability. Our approach supports arbitrary modality pairs
> and performs strongly on diverse MT tasks, including multi-view to 3D shape
> generation, image super-resolution, and multi-view scene synthesis.
> Comprehensive experiments and ablations validate the effectiveness of our
> framework, establishing a new strong baseline in general modality translation.
> For more information, see our project page:
> https://sites.google.com/view/lddbm/home.

