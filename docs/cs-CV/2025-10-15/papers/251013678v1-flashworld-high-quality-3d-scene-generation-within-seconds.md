---
layout: default
title: FlashWorld: High-quality 3D Scene Generation within Seconds
---

# FlashWorld: High-quality 3D Scene Generation within Seconds

**arXiv**: [2510.13678v1](https://arxiv.org/abs/2510.13678) | [PDF](https://arxiv.org/pdf/2510.13678.pdf)

**作者**: Xinyang Li, Tengfei Wang, Zixiao Gu, Shengchuan Zhang, Chunchao Guo, Liujuan Cao

---

## 💡 一句话要点

**提出FlashWorld以快速生成高质量3D场景，从单图或文本提示在秒级完成**

**关键词**: `3D场景生成` `扩散模型` `多视图生成` `蒸馏训练` `高斯表示`

## 📋 核心要点

1. 核心问题：传统多视图导向方法生成慢，3D导向方法视觉质量差且缺乏一致性
2. 方法要点：采用双模式预训练和跨模式后训练蒸馏，结合视频扩散先验提升质量与效率
3. 实验或效果：比先前工作快10~100倍，渲染质量优越，泛化能力增强

## 📄 摘要（原文）

> We propose FlashWorld, a generative model that produces 3D scenes from a
> single image or text prompt in seconds, 10~100$\times$ faster than previous
> works while possessing superior rendering quality. Our approach shifts from the
> conventional multi-view-oriented (MV-oriented) paradigm, which generates
> multi-view images for subsequent 3D reconstruction, to a 3D-oriented approach
> where the model directly produces 3D Gaussian representations during multi-view
> generation. While ensuring 3D consistency, 3D-oriented method typically suffers
> poor visual quality. FlashWorld includes a dual-mode pre-training phase
> followed by a cross-mode post-training phase, effectively integrating the
> strengths of both paradigms. Specifically, leveraging the prior from a video
> diffusion model, we first pre-train a dual-mode multi-view diffusion model,
> which jointly supports MV-oriented and 3D-oriented generation modes. To bridge
> the quality gap in 3D-oriented generation, we further propose a cross-mode
> post-training distillation by matching distribution from consistent 3D-oriented
> mode to high-quality MV-oriented mode. This not only enhances visual quality
> while maintaining 3D consistency, but also reduces the required denoising steps
> for inference. Also, we propose a strategy to leverage massive single-view
> images and text prompts during this process to enhance the model's
> generalization to out-of-distribution inputs. Extensive experiments demonstrate
> the superiority and efficiency of our method.

