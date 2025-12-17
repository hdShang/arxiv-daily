---
layout: default
title: DreamMakeup: Face Makeup Customization using Latent Diffusion Models
---

# DreamMakeup: Face Makeup Customization using Latent Diffusion Models

**arXiv**: [2510.10918v1](https://arxiv.org/abs/2510.10918) | [PDF](https://arxiv.org/pdf/2510.10918.pdf)

**作者**: Geon Yeong Park, Inhwa Han, Serin Yang, Yeobin Hong, Seongmin Jeong, Heechan Jeon, Myeongjin Goh, Sung Won Yi, Jin Nam, Jong Chul Ye

---

## 💡 一句话要点

**提出DreamMakeup基于潜在扩散模型实现免训练面部化妆定制，提升可控性和编辑精度。**

**关键词**: `面部化妆定制` `潜在扩散模型` `DDIM反演` `多条件输入` `身份保持` `虚拟化妆模拟`

## 📋 核心要点

1. GAN在虚拟化妆模拟中存在训练不稳定和定制能力有限的问题。
2. 采用早期停止DDIM反演保护面部结构和身份，支持多条件输入如参考图、颜色和文本。
3. 实验显示在定制、颜色匹配、身份保持和文本兼容性方面优于现有方法，计算成本低。

## 📄 摘要（原文）

> The exponential growth of the global makeup market has paralleled
> advancements in virtual makeup simulation technology. Despite the progress led
> by GANs, their application still encounters significant challenges, including
> training instability and limited customization capabilities. Addressing these
> challenges, we introduce DreamMakup - a novel training-free Diffusion model
> based Makeup Customization method, leveraging the inherent advantages of
> diffusion models for superior controllability and precise real-image editing.
> DreamMakeup employs early-stopped DDIM inversion to preserve the facial
> structure and identity while enabling extensive customization through various
> conditioning inputs such as reference images, specific RGB colors, and textual
> descriptions. Our model demonstrates notable improvements over existing
> GAN-based and recent diffusion-based frameworks - improved customization,
> color-matching capabilities, identity preservation and compatibility with
> textual descriptions or LLMs with affordable computational costs.

