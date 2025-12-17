---
layout: default
title: Post-Processing Methods for Improving Accuracy in MRI Inpainting
---

# Post-Processing Methods for Improving Accuracy in MRI Inpainting

**arXiv**: [2510.15282v1](https://arxiv.org/abs/2510.15282) | [PDF](https://arxiv.org/pdf/2510.15282.pdf)

**作者**: Nishad Kulkarni, Krithika Iyer, Austin Tapp, Abhijeet Parida, Daniel Capellán-Martín, Zhifan Jiang, María J. Ledesma-Carbayo, Syed Muhammad Anwar, Marius George Linguraru

---

## 💡 一句话要点

**提出结合模型集成与后处理的方法，提升MRI肿瘤区域修复精度。**

**关键词**: `MRI修复` `模型集成` `后处理策略` `U-Net增强` `脑肿瘤分析`

## 📋 核心要点

1. 核心问题：MRI分析工具对健康解剖结构优化，难以处理大病变如肿瘤。
2. 方法要点：集成先进修复模型，应用后处理策略和轻量U-Net增强。
3. 实验或效果：评估显示提高修复区域解剖合理性和视觉保真度。

## 📄 摘要（原文）

> Magnetic Resonance Imaging (MRI) is the primary imaging modality used in the
> diagnosis, assessment, and treatment planning for brain pathologies. However,
> most automated MRI analysis tools, such as segmentation and registration
> pipelines, are optimized for healthy anatomies and often fail when confronted
> with large lesions such as tumors. To overcome this, image inpainting
> techniques aim to locally synthesize healthy brain tissues in tumor regions,
> enabling the reliable application of general-purpose tools. In this work, we
> systematically evaluate state-of-the-art inpainting models and observe a
> saturation in their standalone performance. In response, we introduce a
> methodology combining model ensembling with efficient post-processing
> strategies such as median filtering, histogram matching, and pixel averaging.
> Further anatomical refinement is achieved via a lightweight U-Net enhancement
> stage. Comprehensive evaluation demonstrates that our proposed pipeline
> improves the anatomical plausibility and visual fidelity of inpainted regions,
> yielding higher accuracy and more robust outcomes than individual baseline
> models. By combining established models with targeted post-processing, we
> achieve improved and more accessible inpainting outcomes, supporting broader
> clinical deployment and sustainable, resource-conscious research. Our 2025
> BraTS inpainting docker is available at
> https://hub.docker.com/layers/aparida12/brats2025/inpt.

