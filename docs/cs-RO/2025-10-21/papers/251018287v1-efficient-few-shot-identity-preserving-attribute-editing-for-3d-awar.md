---
layout: default
title: Efficient Few-shot Identity Preserving Attribute Editing for 3D-aware Deep Generative Models
---

# Efficient Few-shot Identity Preserving Attribute Editing for 3D-aware Deep Generative Models

**arXiv**: [2510.18287v1](https://arxiv.org/abs/2510.18287) | [PDF](https://arxiv.org/pdf/2510.18287.pdf)

**作者**: Vishal Vinod

---

## 💡 一句话要点

**提出基于潜在空间方向的少样本身份保持属性编辑方法，用于3D感知生成模型**

**关键词**: `3D感知生成模型` `身份保持编辑` `少样本学习` `潜在空间方向` `属性编辑` `多视角一致性`

## 📋 核心要点

1. 核心问题：3D人脸身份保持编辑需处理多视角一致性和高分辨率编辑的挑战
2. 方法要点：利用潜在空间方向估计，结合2D编辑技术实现高效少样本属性编辑
3. 实验或效果：仅需10张或少样本图像即可实现3D一致的身份保持编辑

## 📄 摘要（原文）

> Identity preserving editing of faces is a generative task that enables
> modifying the illumination, adding/removing eyeglasses, face aging, editing
> hairstyles, modifying expression etc., while preserving the identity of the
> face. Recent progress in 2D generative models have enabled photorealistic
> editing of faces using simple techniques leveraging the compositionality in
> GANs. However, identity preserving editing for 3D faces with a given set of
> attributes is a challenging task as the generative model must reason about view
> consistency from multiple poses and render a realistic 3D face. Further, 3D
> portrait editing requires large-scale attribute labelled datasets and presents
> a trade-off between editability in low-resolution and inflexibility to editing
> in high resolution. In this work, we aim to alleviate some of the constraints
> in editing 3D faces by identifying latent space directions that correspond to
> photorealistic edits. To address this, we present a method that builds on
> recent advancements in 3D-aware deep generative models and 2D portrait editing
> techniques to perform efficient few-shot identity preserving attribute editing
> for 3D-aware generative models. We aim to show from experimental results that
> using just ten or fewer labelled images of an attribute is sufficient to
> estimate edit directions in the latent space that correspond to 3D-aware
> attribute editing. In this work, we leverage an existing face dataset with
> masks to obtain the synthetic images for few attribute examples required for
> estimating the edit directions. Further, to demonstrate the linearity of edits,
> we investigate one-shot stylization by performing sequential editing and use
> the (2D) Attribute Style Manipulation (ASM) technique to investigate a
> continuous style manifold for 3D consistent identity preserving face aging.
> Code and results are available at: https://vishal-vinod.github.io/gmpi-edit/

