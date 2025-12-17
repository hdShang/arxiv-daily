---
layout: default
title: NoisePrints: Distortion-Free Watermarks for Authorship in Private Diffusion Models
---

# NoisePrints: Distortion-Free Watermarks for Authorship in Private Diffusion Models

**arXiv**: [2510.13793v1](https://arxiv.org/abs/2510.13793) | [PDF](https://arxiv.org/pdf/2510.13793.pdf)

**作者**: Nir Goren, Oren Katzir, Abhinav Nakarmi, Eyal Ronen, Mahmood Sharif, Or Patashnik

---

## 💡 一句话要点

**提出NoisePrints水印方案，利用随机种子在私有扩散模型中实现无失真作者认证**

**关键词**: `扩散模型水印` `作者身份认证` `零知识证明` `私有模型保护` `轻量级验证`

## 📋 核心要点

1. 核心问题：私有扩散模型难以证明作者身份，现有水印方法需模型权重且计算复杂
2. 方法要点：通过哈希函数嵌入种子到噪声采样，无需修改生成过程，实现轻量级水印
3. 实验或效果：在图像和视频扩散模型上验证，仅需种子和输出即可高效验证，无需模型权重

## 📄 摘要（原文）

> With the rapid adoption of diffusion models for visual content generation,
> proving authorship and protecting copyright have become critical. This
> challenge is particularly important when model owners keep their models private
> and may be unwilling or unable to handle authorship issues, making third-party
> verification essential. A natural solution is to embed watermarks for later
> verification. However, existing methods require access to model weights and
> rely on computationally heavy procedures, rendering them impractical and
> non-scalable. To address these challenges, we propose , a lightweight
> watermarking scheme that utilizes the random seed used to initialize the
> diffusion process as a proof of authorship without modifying the generation
> process. Our key observation is that the initial noise derived from a seed is
> highly correlated with the generated visual content. By incorporating a hash
> function into the noise sampling process, we further ensure that recovering a
> valid seed from the content is infeasible. We also show that sampling an
> alternative seed that passes verification is infeasible, and demonstrate the
> robustness of our method under various manipulations. Finally, we show how to
> use cryptographic zero-knowledge proofs to prove ownership without revealing
> the seed. By keeping the seed secret, we increase the difficulty of watermark
> removal. In our experiments, we validate NoisePrints on multiple
> state-of-the-art diffusion models for images and videos, demonstrating
> efficient verification using only the seed and output, without requiring access
> to model weights.

