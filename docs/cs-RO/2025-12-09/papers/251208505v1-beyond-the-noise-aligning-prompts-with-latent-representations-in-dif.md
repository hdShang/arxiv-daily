---
layout: default
title: Beyond the Noise: Aligning Prompts with Latent Representations in Diffusion Models
---

# Beyond the Noise: Aligning Prompts with Latent Representations in Diffusion Models

**arXiv**: [2512.08505v1](https://arxiv.org/abs/2512.08505) | [PDF](https://arxiv.org/pdf/2512.08505.pdf)

**作者**: Vasco Ramos, Regev Cohen, Idan Szpektor, Joao Magalhaes

---

## 💡 一句话要点

**提出NoisyCLIP方法，在去噪过程中早期检测文本-图像错位，实现实时对齐评估。**

**关键词**: `扩散模型` `文本-图像对齐` `噪声潜在空间` `实时检测` `计算成本优化`

## 📋 核心要点

1. 核心问题：条件扩散模型中文本-图像错位和幻觉常见，传统后生成对齐检测成本高。
2. 方法要点：在噪声潜在空间使用双编码器测量语义对齐，探索反向扩散过程中的错位检测。
3. 实验或效果：在BoN设置中减少50%计算成本，达到CLIP对齐性能的98%，支持实时评估。

## 📄 摘要（原文）

> Conditional diffusion models rely on language-to-image alignment methods to steer the generation towards semantically accurate outputs. Despite the success of this architecture, misalignment and hallucinations remain common issues and require automatic misalignment detection tools to improve quality, for example by applying them in a Best-of-N (BoN) post-generation setting. Unfortunately, measuring the alignment after the generation is an expensive step since we need to wait for the overall generation to finish to determine prompt adherence. In contrast, this work hypothesizes that text/image misalignments can be detected early in the denoising process, enabling real-time alignment assessment without waiting for the complete generation. In particular, we propose NoisyCLIP a method that measures semantic alignment in the noisy latent space. This work is the first to explore and benchmark prompt-to-latent misalignment detection during image generation using dual encoders in the reverse diffusion process. We evaluate NoisyCLIP qualitatively and quantitatively and find it reduces computational cost by 50% while achieving 98% of CLIP alignment performance in BoN settings. This approach enables real-time alignment assessment during generation, reducing costs without sacrificing semantic fidelity.

