---
layout: default
title: CoD: A Diffusion Foundation Model for Image Compression
---

# CoD: A Diffusion Foundation Model for Image Compression

**arXiv**: [2511.18706v1](https://arxiv.org/abs/2511.18706) | [PDF](https://arxiv.org/pdf/2511.18706.pdf)

**作者**: Zhaoyang Jia, Zihan Zheng, Naifu Xue, Jiahao Li, Bin Li, Zongyu Guo, Xiaoyi Zhang, Houqiang Li, Yan Lu

---

## 💡 一句话要点

**提出CoD扩散基础模型以优化图像压缩，提升超低码率性能**

**关键词**: `图像压缩` `扩散模型` `基础模型` `超低码率` `端到端优化`

## 📋 核心要点

1. 现有扩散编解码器依赖文本条件，压缩效率受限，尤其在超低码率下
2. CoD从零训练，专为压缩设计，支持端到端优化，训练成本低且可复现
3. 实验显示CoD在超低码率下达到SOTA，像素扩散可媲美VTM并优于GAN

## 📄 摘要（原文）

> Existing diffusion codecs typically build on text-to-image diffusion foundation models like Stable Diffusion. However, text conditioning is suboptimal from a compression perspective, hindering the potential of downstream diffusion codecs, particularly at ultra-low bitrates. To address it, we introduce \textbf{CoD}, the first \textbf{Co}mpression-oriented \textbf{D}iffusion foundation model, trained from scratch to enable end-to-end optimization of both compression and generation. CoD is not a fixed codec but a general foundation model designed for various diffusion-based codecs. It offers several advantages: \textbf{High compression efficiency}, replacing Stable Diffusion with CoD in downstream codecs like DiffC achieves SOTA results, especially at ultra-low bitrates (e.g., 0.0039 bpp); \textbf{Low-cost and reproducible training}, 300$\times$ faster training than Stable Diffusion ($\sim$ 20 vs. $\sim$ 6,250 A100 GPU days) on entirely open image-only datasets; \textbf{Providing new insights}, e.g., We find pixel-space diffusion can achieve VTM-level PSNR with high perceptual quality and can outperform GAN-based codecs using fewer parameters. We hope CoD lays the foundation for future diffusion codec research. Codes will be released.

