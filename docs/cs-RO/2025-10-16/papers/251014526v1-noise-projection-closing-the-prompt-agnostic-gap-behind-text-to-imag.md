---
layout: default
title: Noise Projection: Closing the Prompt-Agnostic Gap Behind Text-to-Image Misalignment in Diffusion Models
---

# Noise Projection: Closing the Prompt-Agnostic Gap Behind Text-to-Image Misalignment in Diffusion Models

**arXiv**: [2510.14526v1](https://arxiv.org/abs/2510.14526) | [PDF](https://arxiv.org/pdf/2510.14526.pdf)

**作者**: Yunze Tong, Didi Zhu, Zijing Hu, Jinluan Yang, Ziyu Zhao

---

## 💡 一句话要点

**提出噪声投影器以解决扩散模型中文本-图像不对齐问题**

**关键词**: `文本到图像生成` `扩散模型` `噪声投影` `文本-图像对齐` `偏好优化`

## 📋 核心要点

1. 核心问题：训练与推理噪声分布不匹配导致文本-图像对齐差
2. 方法要点：使用噪声投影器将初始噪声映射为提示感知版本
3. 实验或效果：通过VLM反馈优化，提升多样提示下的对齐效果

## 📄 摘要（原文）

> In text-to-image generation, different initial noises induce distinct
> denoising paths with a pretrained Stable Diffusion (SD) model. While this
> pattern could output diverse images, some of them may fail to align well with
> the prompt. Existing methods alleviate this issue either by altering the
> denoising dynamics or by drawing multiple noises and conducting post-selection.
> In this paper, we attribute the misalignment to a training-inference mismatch:
> during training, prompt-conditioned noises lie in a prompt-specific subset of
> the latent space, whereas at inference the noise is drawn from a
> prompt-agnostic Gaussian prior. To close this gap, we propose a noise projector
> that applies text-conditioned refinement to the initial noise before denoising.
> Conditioned on the prompt embedding, it maps the noise to a prompt-aware
> counterpart that better matches the distribution observed during SD training,
> without modifying the SD model. Our framework consists of these steps: we first
> sample some noises and obtain token-level feedback for their corresponding
> images from a vision-language model (VLM), then distill these signals into a
> reward model, and finally optimize the noise projector via a quasi-direct
> preference optimization. Our design has two benefits: (i) it requires no
> reference images or handcrafted priors, and (ii) it incurs small inference
> cost, replacing multi-sample selection with a single forward pass. Extensive
> experiments further show that our prompt-aware noise projection improves
> text-image alignment across diverse prompts.

