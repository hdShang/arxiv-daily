---
layout: default
title: Dynamic VLM-Guided Negative Prompting for Diffusion Models
---

# Dynamic VLM-Guided Negative Prompting for Diffusion Models

**arXiv**: [2510.26052v1](https://arxiv.org/abs/2510.26052) | [PDF](https://arxiv.org/pdf/2510.26052.pdf)

**作者**: Hoyeon Chang, Seungjin Kim, Yoonseok Choi

---

## 💡 一句话要点

**提出动态VLM引导负提示方法以提升扩散模型生成质量**

**关键词**: `扩散模型` `负提示` `视觉语言模型` `动态生成` `文本图像对齐`

## 📋 核心要点

1. 传统负提示方法使用固定提示，无法适应生成过程
2. 在去噪步骤中生成中间图像，利用VLM动态生成上下文相关负提示
3. 在基准数据集上评估，展示负引导强度与文本图像对齐的权衡

## 📄 摘要（原文）

> We propose a novel approach for dynamic negative prompting in diffusion
> models that leverages Vision-Language Models (VLMs) to adaptively generate
> negative prompts during the denoising process. Unlike traditional Negative
> Prompting methods that use fixed negative prompts, our method generates
> intermediate image predictions at specific denoising steps and queries a VLM to
> produce contextually appropriate negative prompts. We evaluate our approach on
> various benchmark datasets and demonstrate the trade-offs between negative
> guidance strength and text-image alignment.

