---
layout: default
title: Vision Foundation Models Can Be Good Tokenizers for Latent Diffusion Models
---

# Vision Foundation Models Can Be Good Tokenizers for Latent Diffusion Models

**arXiv**: [2510.18457v1](https://arxiv.org/abs/2510.18457) | [PDF](https://arxiv.org/pdf/2510.18457.pdf)

**作者**: Tianci Bi, Xiaoyi Zhang, Yan Lu, Nanning Zheng

---

## 💡 一句话要点

**提出VFM-VAE以直接集成视觉基础模型到潜在扩散模型，提升语义对齐与效率。**

**关键词**: `视觉基础模型` `潜在扩散模型` `变分自编码器` `语义对齐` `多尺度融合` `扩散训练加速`

## 📋 核心要点

1. 核心问题：现有蒸馏方法导致视觉基础模型语义对齐在分布偏移下减弱。
2. 方法要点：设计VFM-VAE，采用多尺度潜在融合和渐进分辨率重建块。
3. 实验或效果：在80轮训练中gFID达2.20，640轮达1.62，加速10倍。

## 📄 摘要（原文）

> The performance of Latent Diffusion Models (LDMs) is critically dependent on
> the quality of their visual tokenizer. While recent works have explored
> incorporating Vision Foundation Models (VFMs) via distillation, we identify a
> fundamental flaw in this approach: it inevitably weakens the robustness of
> alignment with the original VFM, causing the aligned latents to deviate
> semantically under distribution shifts. In this paper, we bypass distillation
> by proposing a more direct approach: Vision Foundation Model Variational
> Autoencoder (VFM-VAE). To resolve the inherent tension between the VFM's
> semantic focus and the need for pixel-level fidelity, we redesign the VFM-VAE
> decoder with Multi-Scale Latent Fusion and Progressive Resolution
> Reconstruction blocks, enabling high-quality reconstruction from spatially
> coarse VFM features. Furthermore, we provide a comprehensive analysis of
> representation dynamics during diffusion training, introducing the proposed
> SE-CKNNA metric as a more precise tool for this diagnosis. This analysis allows
> us to develop a joint tokenizer-diffusion alignment strategy that dramatically
> accelerates convergence. Our innovations in tokenizer design and training
> strategy lead to superior performance and efficiency: our system reaches a gFID
> (w/o CFG) of 2.20 in merely 80 epochs (a 10x speedup over prior tokenizers).
> With continued training to 640 epochs, it further attains a gFID (w/o CFG) of
> 1.62, establishing direct VFM integration as a superior paradigm for LDMs.

