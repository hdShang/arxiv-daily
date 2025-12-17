---
layout: default
title: FreeControl: Efficient, Training-Free Structural Control via One-Step Attention Extraction
---

# FreeControl: Efficient, Training-Free Structural Control via One-Step Attention Extraction

**arXiv**: [2511.05219v1](https://arxiv.org/abs/2511.05219) | [PDF](https://arxiv.org/pdf/2511.05219.pdf)

**作者**: Jiang Lin, Xinyu Chen, Song Wu, Zhiqiu Zhang, Jizhi Zhang, Ye Wang, Qiang Tang, Qian Wang, Jian Yang, Zili Yi

---

## 💡 一句话要点

**提出FreeControl以解决扩散模型结构控制效率低的问题**

**关键词**: `扩散模型` `结构控制` `注意力机制` `训练免费方法` `图像生成`

## 📋 核心要点

1. 现有方法依赖手工条件图或反演，导致灵活性差和推理成本高
2. 通过单步注意力提取和潜在条件解耦，实现无需训练的结构控制
3. 实验显示在约5%额外成本下，支持组合控制并提升对齐质量

## 📄 摘要（原文）

> Controlling the spatial and semantic structure of diffusion-generated images
> remains a challenge. Existing methods like ControlNet rely on handcrafted
> condition maps and retraining, limiting flexibility and generalization.
> Inversion-based approaches offer stronger alignment but incur high inference
> cost due to dual-path denoising. We present FreeControl, a training-free
> framework for semantic structural control in diffusion models. Unlike prior
> methods that extract attention across multiple timesteps, FreeControl performs
> one-step attention extraction from a single, optimally chosen key timestep and
> reuses it throughout denoising. This enables efficient structural guidance
> without inversion or retraining. To further improve quality and stability, we
> introduce Latent-Condition Decoupling (LCD): a principled separation of the key
> timestep and the noised latent used in attention extraction. LCD provides finer
> control over attention quality and eliminates structural artifacts. FreeControl
> also supports compositional control via reference images assembled from
> multiple sources - enabling intuitive scene layout design and stronger prompt
> alignment. FreeControl introduces a new paradigm for test-time control,
> enabling structurally and semantically aligned, visually coherent generation
> directly from raw images, with the flexibility for intuitive compositional
> design and compatibility with modern diffusion models at approximately 5
> percent additional cost.

