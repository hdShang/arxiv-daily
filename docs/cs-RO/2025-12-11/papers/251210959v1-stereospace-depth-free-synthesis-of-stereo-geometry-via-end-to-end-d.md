---
layout: default
title: StereoSpace: Depth-Free Synthesis of Stereo Geometry via End-to-End Diffusion in a Canonical Space
---

# StereoSpace: Depth-Free Synthesis of Stereo Geometry via End-to-End Diffusion in a Canonical Space

**arXiv**: [2512.10959v1](https://arxiv.org/abs/2512.10959) | [PDF](https://arxiv.org/pdf/2512.10959.pdf)

**作者**: Tjark Behrens, Anton Obukhov, Bingxin Ke, Fabio Tosi, Matteo Poggi, Konrad Schindler

---

## 💡 一句话要点

**提出StereoSpace，通过端到端扩散在规范空间中实现无深度的立体几何合成。**

**关键词**: `立体合成` `扩散模型` `视点条件` `无深度估计` `端到端评估`

## 📋 核心要点

1. 核心问题：单目到立体合成需处理视差和遮挡，传统方法依赖深度估计或变形。
2. 方法要点：基于扩散模型，在规范矫正空间中通过视点条件建模几何，无需显式深度或变形。
3. 实验或效果：引入无泄漏评估协议，在感知舒适度和几何一致性上超越现有方法，适用于分层和非朗伯场景。

## 📄 摘要（原文）

> We introduce StereoSpace, a diffusion-based framework for monocular-to-stereo synthesis that models geometry purely through viewpoint conditioning, without explicit depth or warping. A canonical rectified space and the conditioning guide the generator to infer correspondences and fill disocclusions end-to-end. To ensure fair and leakage-free evaluation, we introduce an end-to-end protocol that excludes any ground truth or proxy geometry estimates at test time. The protocol emphasizes metrics reflecting downstream relevance: iSQoE for perceptual comfort and MEt3R for geometric consistency. StereoSpace surpasses other methods from the warp & inpaint, latent-warping, and warped-conditioning categories, achieving sharp parallax and strong robustness on layered and non-Lambertian scenes. This establishes viewpoint-conditioned diffusion as a scalable, depth-free solution for stereo generation.

