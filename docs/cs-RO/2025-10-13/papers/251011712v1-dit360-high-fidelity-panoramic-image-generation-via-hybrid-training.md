---
layout: default
title: DiT360: High-Fidelity Panoramic Image Generation via Hybrid Training
---

# DiT360: High-Fidelity Panoramic Image Generation via Hybrid Training

**arXiv**: [2510.11712v1](https://arxiv.org/abs/2510.11712) | [PDF](https://arxiv.org/pdf/2510.11712.pdf)

**作者**: Haoran Feng, Dizhe Zhang, Xiangtai Li, Bo Du, Lu Qi

---

## 💡 一句话要点

**提出DiT360框架，通过混合训练解决全景图像生成中的几何保真度和真实感问题。**

**关键词**: `全景图像生成` `混合训练` `扩散变换器` `几何保真度` `边界连续性` `图像修复`

## 📋 核心要点

1. 核心问题：缺乏大规模高质量真实全景数据，影响生成图像的几何保真度和真实感。
2. 方法要点：在图像和token级别应用跨域变换和域内增强，包括视角图像引导和全景优化。
3. 实验效果：在文本到全景、修复和扩展任务中，边界一致性和图像保真度优于现有方法。

## 📄 摘要（原文）

> In this work, we propose DiT360, a DiT-based framework that performs hybrid
> training on perspective and panoramic data for panoramic image generation. For
> the issues of maintaining geometric fidelity and photorealism in generation
> quality, we attribute the main reason to the lack of large-scale, high-quality,
> real-world panoramic data, where such a data-centric view differs from prior
> methods that focus on model design. Basically, DiT360 has several key modules
> for inter-domain transformation and intra-domain augmentation, applied at both
> the pre-VAE image level and the post-VAE token level. At the image level, we
> incorporate cross-domain knowledge through perspective image guidance and
> panoramic refinement, which enhance perceptual quality while regularizing
> diversity and photorealism. At the token level, hybrid supervision is applied
> across multiple modules, which include circular padding for boundary
> continuity, yaw loss for rotational robustness, and cube loss for distortion
> awareness. Extensive experiments on text-to-panorama, inpainting, and
> outpainting tasks demonstrate that our method achieves better boundary
> consistency and image fidelity across eleven quantitative metrics. Our code is
> available at https://github.com/Insta360-Research-Team/DiT360.

