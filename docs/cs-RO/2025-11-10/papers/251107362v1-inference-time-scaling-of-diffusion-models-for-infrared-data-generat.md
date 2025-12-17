---
layout: default
title: Inference-Time Scaling of Diffusion Models for Infrared Data Generation
---

# Inference-Time Scaling of Diffusion Models for Infrared Data Generation

**arXiv**: [2511.07362v1](https://arxiv.org/abs/2511.07362) | [PDF](https://arxiv.org/pdf/2511.07362.pdf)

**作者**: Kai A. Horstmann, Maxim Clouser, Kia Khezeli

---

## 💡 一句话要点

**提出推理时缩放方法以提升红外图像生成质量**

**关键词**: `红外图像生成` `扩散模型` `推理时引导` `领域适应` `CLIP验证器`

## 📋 核心要点

1. 核心问题：红外图像数据稀缺，阻碍下游视觉模型开发。
2. 方法要点：使用领域适应CLIP验证器在推理时引导扩散模型采样。
3. 实验或效果：在KAIST数据集上FID分数降低10%，生成质量提升。

## 📄 摘要（原文）

> Infrared imagery enables temperature-based scene understanding using passive
> sensors, particularly under conditions of low visibility where traditional RGB
> imaging fails. Yet, developing downstream vision models for infrared
> applications is hindered by the scarcity of high-quality annotated data, due to
> the specialized expertise required for infrared annotation. While synthetic
> infrared image generation has the potential to accelerate model development by
> providing large-scale, diverse training data, training foundation-level
> generative diffusion models in the infrared domain has remained elusive due to
> limited datasets. In light of such data constraints, we explore an
> inference-time scaling approach using a domain-adapted CLIP-based verifier for
> enhanced infrared image generation quality. We adapt FLUX.1-dev, a
> state-of-the-art text-to-image diffusion model, to the infrared domain by
> finetuning it on a small sample of infrared images using parameter-efficient
> techniques. The trained verifier is then employed during inference to guide the
> diffusion sampling process toward higher quality infrared generations that
> better align with input text prompts. Empirically, we find that our approach
> leads to consistent improvements in generation quality, reducing FID scores on
> the KAIST Multispectral Pedestrian Detection Benchmark dataset by 10% compared
> to unguided baseline samples. Our results suggest that inference-time guidance
> offers a promising direction for bridging the domain gap in low-data infrared
> settings.

