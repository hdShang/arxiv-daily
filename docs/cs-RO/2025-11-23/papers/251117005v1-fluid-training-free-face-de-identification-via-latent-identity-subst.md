---
layout: default
title: FLUID: Training-Free Face De-identification via Latent Identity Substitution
---

# FLUID: Training-Free Face De-identification via Latent Identity Substitution

**arXiv**: [2511.17005v1](https://arxiv.org/abs/2511.17005) | [PDF](https://arxiv.org/pdf/2511.17005.pdf)

**作者**: Jinhyeong Park, Shaheryar Muhammad, Seangmin Lee, Jong Taek Lee, Soon Ki Jung

---

## 💡 一句话要点

**提出FLUID框架，通过潜在身份替换实现免训练人脸去识别。**

**关键词**: `人脸去识别` `潜在空间编辑` `扩散模型` `身份抑制` `属性保留`

## 📋 核心要点

1. 核心问题：人脸去识别需平衡身份抑制与属性保留。
2. 方法要点：在预训练扩散模型潜在空间优化身份编辑方向。
3. 实验效果：在CelebA-HQ和FFHQ上优于现有方法。

## 📄 摘要（原文）

> We present FLUID (Face de-identification in the Latent space via Utility-preserving Identity Displacement), a training-free framework that directly substitutes identity in the latent space of pretrained diffusion models. Inspired by substitution mechanisms in chemistry, we reinterpret identity editing as semantic displacement in the latent h-space of a pretrained unconditional diffusion model. Our framework discovers identity-editing directions through optimization guided by novel reagent losses, which supervise for attribute preservation and identity suppression. We further propose both linear and geodesic (tangent-based) editing schemes to effectively navigate the latent manifold. Experimental results on CelebA-HQ and FFHQ demonstrate that FLUID achieves a superior trade-off between identity suppression and attribute preservation, outperforming state-of-the-art de-identification methods in both qualitative and quantitative metrics.

