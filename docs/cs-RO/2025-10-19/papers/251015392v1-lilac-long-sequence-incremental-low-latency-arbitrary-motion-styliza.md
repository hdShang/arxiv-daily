---
layout: default
title: LILAC: Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding
---

# LILAC: Long-sequence Incremental Low-latency Arbitrary Motion Stylization via Streaming VAE-Diffusion with Causal Decoding

**arXiv**: [2510.15392v1](https://arxiv.org/abs/2510.15392) | [PDF](https://arxiv.org/pdf/2510.15392.pdf)

**作者**: Peng Ren, Hai Yang

---

## 💡 一句话要点

**提出LILAC方法以实现长序列实时任意运动风格化**

**关键词**: `运动风格化` `流式生成` `潜在空间扩散` `因果解码` `实时处理`

## 📋 核心要点

1. 现有流式方法在原始运动空间操作，计算开销大且难以保持时间稳定性
2. 采用潜在空间流式架构和因果解码，无需未来帧即可实现低延迟风格化
3. 在基准数据集上验证了风格化质量和响应性的良好平衡

## 📄 摘要（原文）

> Generating long and stylized human motions in real time is critical for
> applications that demand continuous and responsive character control. Despite
> its importance, existing streaming approaches often operate directly in the raw
> motion space, leading to substantial computational overhead and making it
> difficult to maintain temporal stability. In contrast, latent-space
> VAE-Diffusion-based frameworks alleviate these issues and achieve high-quality
> stylization, but they are generally confined to offline processing. To bridge
> this gap, LILAC (Long-sequence Incremental Low-latency Arbitrary Motion
> Stylization via Streaming VAE-Diffusion with Causal Decoding) builds upon a
> recent high-performing offline framework for arbitrary motion stylization and
> extends it to an online setting through a latent-space streaming architecture
> with a sliding-window causal design and the injection of decoded motion
> features to ensure smooth motion transitions. This architecture enables
> long-sequence real-time arbitrary stylization without relying on future frames
> or modifying the diffusion model architecture, achieving a favorable balance
> between stylization quality and responsiveness as demonstrated by experiments
> on benchmark datasets. Supplementary video and examples are available at the
> project page: https://pren1.github.io/lilac/

