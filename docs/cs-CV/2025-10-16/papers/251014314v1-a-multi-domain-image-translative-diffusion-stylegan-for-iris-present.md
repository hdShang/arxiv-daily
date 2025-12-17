---
layout: default
title: A Multi-domain Image Translative Diffusion StyleGAN for Iris Presentation Attack Detection
---

# A Multi-domain Image Translative Diffusion StyleGAN for Iris Presentation Attack Detection

**arXiv**: [2510.14314v1](https://arxiv.org/abs/2510.14314) | [PDF](https://arxiv.org/pdf/2510.14314.pdf)

**作者**: Shivangi Yadav, Arun Ross

---

## 💡 一句话要点

**提出MID-StyleGAN以解决虹膜呈现攻击检测中数据稀缺问题**

**关键词**: `虹膜呈现攻击检测` `合成数据生成` `多领域图像翻译` `扩散模型` `生成对抗网络`

## 📋 核心要点

1. 核心问题：虹膜生物识别系统易受呈现攻击，但缺乏训练数据。
2. 方法要点：结合扩散模型与GAN，生成多领域合成眼部图像。
3. 实验或效果：在LivDet2020数据集上，真检测率从93.41%提升至98.72%。

## 📄 摘要（原文）

> An iris biometric system can be compromised by presentation attacks (PAs)
> where artifacts such as artificial eyes, printed eye images, or cosmetic
> contact lenses are presented to the system. To counteract this, several
> presentation attack detection (PAD) methods have been developed. However, there
> is a scarcity of datasets for training and evaluating iris PAD techniques due
> to the implicit difficulties in constructing and imaging PAs. To address this,
> we introduce the Multi-domain Image Translative Diffusion StyleGAN
> (MID-StyleGAN), a new framework for generating synthetic ocular images that
> captures the PA and bonafide characteristics in multiple domains such as
> bonafide, printed eyes and cosmetic contact lens. MID-StyleGAN combines the
> strengths of diffusion models and generative adversarial networks (GANs) to
> produce realistic and diverse synthetic data. Our approach utilizes a
> multi-domain architecture that enables the translation between bonafide ocular
> images and different PA domains. The model employs an adaptive loss function
> tailored for ocular data to maintain domain consistency. Extensive experiments
> demonstrate that MID-StyleGAN outperforms existing methods in generating
> high-quality synthetic ocular images. The generated data was used to
> significantly enhance the performance of PAD systems, providing a scalable
> solution to the data scarcity problem in iris and ocular biometrics. For
> example, on the LivDet2020 dataset, the true detect rate at 1% false detect
> rate improved from 93.41% to 98.72%, showcasing the impact of the proposed
> method.

