---
layout: default
title: JoyAvatar: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion
---

# JoyAvatar: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion

**arXiv**: [2512.11423v1](https://arxiv.org/abs/2512.11423) | [PDF](https://arxiv.org/pdf/2512.11423.pdf)

**作者**: Chaochao Li, Ruikui Wang, Liangbo Zhou, Jinheng Feng, Huaishao Luo, Huan Zhang, Youzheng Wu, Xiaodong He

---

## 💡 一句话要点

**提出JoyAvatar以解决音频驱动虚拟人生成中的实时性和长视频合成问题**

**关键词**: `音频驱动虚拟人生成` `自回归扩散模型` `实时推理` `长视频合成` `时间一致性` `唇同步`

## 📋 核心要点

1. 现有DiT方法计算开销高且无法生成长视频，自回归方法存在误差累积和质量下降问题
2. 引入渐进步引导、运动条件注入和缓存重置无界RoPE，提升稳定性和时间一致性
3. 1.3B参数模型在单GPU上实现16 FPS实时推理，视觉质量、时间一致性和唇同步效果竞争性强

## 📄 摘要（原文）

> Existing DiT-based audio-driven avatar generation methods have achieved considerable progress, yet their broader application is constrained by limitations such as high computational overhead and the inability to synthesize long-duration videos. Autoregressive methods address this problem by applying block-wise autoregressive diffusion methods. However, these methods suffer from the problem of error accumulation and quality degradation. To address this, we propose JoyAvatar, an audio-driven autoregressive model capable of real-time inference and infinite-length video generation with the following contributions: (1) Progressive Step Bootstrapping (PSB), which allocates more denoising steps to initial frames to stabilize generation and reduce error accumulation; (2) Motion Condition Injection (MCI), enhancing temporal coherence by injecting noise-corrupted previous frames as motion condition; and (3) Unbounded RoPE via Cache-Resetting (URCR), enabling infinite-length generation through dynamic positional encoding. Our 1.3B-parameter causal model achieves 16 FPS on a single GPU and achieves competitive results in visual quality, temporal consistency, and lip synchronization.

