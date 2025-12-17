---
layout: default
title: GFix: Perceptually Enhanced Gaussian Splatting Video Compression
---

# GFix: Perceptually Enhanced Gaussian Splatting Video Compression

**arXiv**: [2511.06953v1](https://arxiv.org/abs/2511.06953) | [PDF](https://arxiv.org/pdf/2511.06953.pdf)

**作者**: Siyue Teng, Ge Gao, Duolikun Danier, Yuxuan Jiang, Fan Zhang, Thomas Davis, Zoe Liu, David Bull

---

## 💡 一句话要点

**提出GFix框架以增强基于3D高斯泼溅的视频压缩感知质量**

**关键词**: `3D高斯泼溅` `视频压缩` `感知增强` `扩散模型` `LoRA调制` `神经增强器`

## 📋 核心要点

1. 核心问题：现有3DGS视频压缩存在明显视觉伪影和低压缩比。
2. 方法要点：使用内容自适应扩散模型作为神经增强器，结合调制LoRA提升压缩效率。
3. 实验效果：在LPIPS和FID指标上优于GSVC，BD-rate节省分别达72.1%和21.4%。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) enhances 3D scene reconstruction through
> explicit representation and fast rendering, demonstrating potential benefits
> for various low-level vision tasks, including video compression. However,
> existing 3DGS-based video codecs generally exhibit more noticeable visual
> artifacts and relatively low compression ratios. In this paper, we specifically
> target the perceptual enhancement of 3DGS-based video compression, based on the
> assumption that artifacts from 3DGS rendering and quantization resemble noisy
> latents sampled during diffusion training. Building on this premise, we propose
> a content-adaptive framework, GFix, comprising a streamlined, single-step
> diffusion model that serves as an off-the-shelf neural enhancer. Moreover, to
> increase compression efficiency, We propose a modulated LoRA scheme that
> freezes the low-rank decompositions and modulates the intermediate hidden
> states, thereby achieving efficient adaptation of the diffusion backbone with
> highly compressible updates. Experimental results show that GFix delivers
> strong perceptual quality enhancement, outperforming GSVC with up to 72.1%
> BD-rate savings in LPIPS and 21.4% in FID.

