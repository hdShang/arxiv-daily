---
layout: default
title: PSTF-AttControl: Per-Subject-Tuning-Free Personalized Image Generation with Controllable Face Attributes
---

# PSTF-AttControl: Per-Subject-Tuning-Free Personalized Image Generation with Controllable Face Attributes

**arXiv**: [2510.25084v1](https://arxiv.org/abs/2510.25084) | [PDF](https://arxiv.org/pdf/2510.25084.pdf)

**作者**: Xiang liu, Zhaoxiang Liu, Huan Hu, Zipeng Wang, Ping Chen, Zezhou Chen, Kai Wang, Shiguo Lian

---

## 💡 一句话要点

**提出PSTF-AttControl方法，实现免调优个性化图像生成与可控面部属性。**

**关键词**: `个性化图像生成` `面部属性控制` `免调优方法` `StyleGAN2` `人脸识别` `UNet架构`

## 📋 核心要点

1. 现有方法难以在免调优下精确控制面部属性，限制个性化图像生成。
2. 使用人脸识别模型提取身份特征，结合Triplet-Decoupled Cross-Attention模块分离身份与属性。
3. 在FFHQ数据集上训练，生成图像保留身份并控制属性，无需额外调优。

## 📄 摘要（原文）

> Recent advancements in personalized image generation have significantly
> improved facial identity preservation, particularly in fields such as
> entertainment and social media. However, existing methods still struggle to
> achieve precise control over facial attributes in a per-subject-tuning-free
> (PSTF) way. Tuning-based techniques like PreciseControl have shown promise by
> providing fine-grained control over facial features, but they often require
> extensive technical expertise and additional training data, limiting their
> accessibility. In contrast, PSTF approaches simplify the process by enabling
> image generation from a single facial input, but they lack precise control over
> facial attributes. In this paper, we introduce a novel, PSTF method that
> enables both precise control over facial attributes and high-fidelity
> preservation of facial identity. Our approach utilizes a face recognition model
> to extract facial identity features, which are then mapped into the $W^+$
> latent space of StyleGAN2 using the e4e encoder. We further enhance the model
> with a Triplet-Decoupled Cross-Attention module, which integrates facial
> identity, attribute features, and text embeddings into the UNet architecture,
> ensuring clean separation of identity and attribute information. Trained on the
> FFHQ dataset, our method allows for the generation of personalized images with
> fine-grained control over facial attributes, while without requiring additional
> fine-tuning or training data for individual identities. We demonstrate that our
> approach successfully balances personalization with precise facial attribute
> control, offering a more efficient and user-friendly solution for high-quality,
> adaptable facial image synthesis. The code is publicly available at
> https://github.com/UnicomAI/PSTF-AttControl.

