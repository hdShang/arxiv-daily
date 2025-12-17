---
layout: default
title: ControlVP: Interactive Geometric Refinement of AI-Generated Images with Consistent Vanishing Points
---

# ControlVP: Interactive Geometric Refinement of AI-Generated Images with Consistent Vanishing Points

**arXiv**: [2512.07504v1](https://arxiv.org/abs/2512.07504) | [PDF](https://arxiv.org/pdf/2512.07504.pdf)

**作者**: Ryota Okumura, Kaede Shiohara, Toshihiko Yamasaki

---

## 💡 一句话要点

**提出ControlVP框架，通过用户引导修正AI生成图像中的灭点不一致问题**

**关键词**: `灭点校正` `几何一致性` `扩散模型` `用户引导框架` `图像生成`

## 📋 核心要点

1. 核心问题：文本到图像模型常产生几何不一致，如灭点不一致，影响场景结构真实感
2. 方法要点：扩展预训练扩散模型，结合建筑轮廓结构指导和几何约束，增强全局几何一致性
3. 实验或效果：在保持视觉保真度下提升几何一致性，适用于图像到3D重建等应用

## 📄 摘要（原文）

> Recent text-to-image models, such as Stable Diffusion, have achieved impressive visual quality, yet they often suffer from geometric inconsistencies that undermine the structural realism of generated scenes. One prominent issue is vanishing point inconsistency, where projections of parallel lines fail to converge correctly in 2D space. This leads to structurally implausible geometry that degrades spatial realism, especially in architectural scenes. We propose ControlVP, a user-guided framework for correcting vanishing point inconsistencies in generated images. Our approach extends a pre-trained diffusion model by incorporating structural guidance derived from building contours. We also introduce geometric constraints that explicitly encourage alignment between image edges and perspective cues. Our method enhances global geometric consistency while maintaining visual fidelity comparable to the baselines. This capability is particularly valuable for applications that require accurate spatial structure, such as image-to-3D reconstruction. The dataset and source code are available at https://github.com/RyotaOkumura/ControlVP .

