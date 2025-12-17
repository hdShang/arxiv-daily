---
layout: default
title: Switchable Token-Specific Codebook Quantization For Face Image Compression
---

# Switchable Token-Specific Codebook Quantization For Face Image Compression

**arXiv**: [2510.22943v1](https://arxiv.org/abs/2510.22943) | [PDF](https://arxiv.org/pdf/2510.22943.pdf)

**作者**: Yongbo Wang, Haonan Wang, Guodong Mu, Ruixin Zhang, Jiaqi Chen, Jingyun Zhang, Jun Wang, Yuan Xie, Zhizhong Zhang, Shouhong Ding

---

## 💡 一句话要点

**提出可切换令牌特定码本量化方法以提升人脸图像压缩性能**

**关键词**: `人脸图像压缩` `码本量化` `令牌特定码本` `图像重构` `低比特率压缩`

## 📋 核心要点

1. 人脸图像压缩中全局码本忽略类别相关性和令牌语义差异，导致低比特率性能不佳
2. 方法为不同图像类别学习码本组，并为每个令牌分配独立码本，减少码本大小损失
3. 在0.05 bpp下重构图像平均识别准确率达93.51%，可集成现有码本方法

## 📄 摘要（原文）

> With the ever-increasing volume of visual data, the efficient and lossless
> transmission, along with its subsequent interpretation and understanding, has
> become a critical bottleneck in modern information systems. The emerged
> codebook-based solution utilize a globally shared codebook to quantize and
> dequantize each token, controlling the bpp by adjusting the number of tokens or
> the codebook size. However, for facial images, which are rich in attributes,
> such global codebook strategies overlook both the category-specific
> correlations within images and the semantic differences among tokens, resulting
> in suboptimal performance, especially at low bpp. Motivated by these
> observations, we propose a Switchable Token-Specific Codebook Quantization for
> face image compression, which learns distinct codebook groups for different
> image categories and assigns an independent codebook to each token. By
> recording the codebook group to which each token belongs with a small number of
> bits, our method can reduce the loss incurred when decreasing the size of each
> codebook group. This enables a larger total number of codebooks under a lower
> overall bpp, thereby enhancing the expressive capability and improving
> reconstruction performance. Owing to its generalizable design, our method can
> be integrated into any existing codebook-based representation learning approach
> and has demonstrated its effectiveness on face recognition datasets, achieving
> an average accuracy of 93.51% for reconstructed images at 0.05 bpp.

