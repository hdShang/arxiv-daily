---
layout: default
title: FROMAT: Multiview Material Appearance Transfer via Few-Shot Self-Attention Adaptation
---

# FROMAT: Multiview Material Appearance Transfer via Few-Shot Self-Attention Adaptation

**arXiv**: [2512.09617v1](https://arxiv.org/abs/2512.09617) | [PDF](https://arxiv.org/pdf/2512.09617.pdf)

**作者**: Hubert Kompanowski, Varun Jampani, Aaryaman Vasishta, Binh-Son Hua

---

## 💡 一句话要点

**提出基于少样本自注意力适配的多视角材质外观迁移方法，以增强多视角扩散模型的外观操控能力。**

**关键词**: `多视角扩散模型` `外观迁移` `自注意力适配` `少样本学习` `材质编辑` `生成式3D表示`

## 📋 核心要点

1. 核心问题：多视角扩散模型在外观操控（如材质、纹理）方面受限，难以实现精确指定。
2. 方法要点：通过轻量级适配，结合输入图像的对象身份和参考图像的外观线索，利用自注意力特征聚合实现多视角一致输出。
3. 实验或效果：仅需少量训练样本，即可在预训练模型上实现多样外观的多视角生成，保持几何和视角一致性。

## 📄 摘要（原文）

> Multiview diffusion models have rapidly emerged as a powerful tool for content creation with spatial consistency across viewpoints, offering rich visual realism without requiring explicit geometry and appearance representation. However, compared to meshes or radiance fields, existing multiview diffusion models offer limited appearance manipulation, particularly in terms of material, texture, or style.
>   In this paper, we present a lightweight adaptation technique for appearance transfer in multiview diffusion models. Our method learns to combine object identity from an input image with appearance cues rendered in a separate reference image, producing multi-view-consistent output that reflects the desired materials, textures, or styles. This allows explicit specification of appearance parameters at generation time while preserving the underlying object geometry and view coherence. We leverage three diffusion denoising processes responsible for generating the original object, the reference, and the target images, and perform reverse sampling to aggregate a small subset of layer-wise self-attention features from the object and the reference to influence the target generation. Our method requires only a few training examples to introduce appearance awareness to pretrained multiview models. The experiments show that our method provides a simple yet effective way toward multiview generation with diverse appearance, advocating the adoption of implicit generative 3D representations in practice.

