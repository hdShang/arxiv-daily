---
layout: default
title: VessShape: Few-shot 2D blood vessel segmentation by leveraging shape priors from synthetic images
---

# VessShape: Few-shot 2D blood vessel segmentation by leveraging shape priors from synthetic images

**arXiv**: [2510.27646v1](https://arxiv.org/abs/2510.27646) | [PDF](https://arxiv.org/pdf/2510.27646.pdf)

**作者**: Cesar H. Comin, Wesley N. Galvão

---

## 💡 一句话要点

**提出VessShape方法，利用合成图像形状先验解决血管分割数据稀缺问题**

**关键词**: `血管分割` `少样本学习` `形状先验` `合成数据生成` `零样本泛化`

## 📋 核心要点

1. 核心问题：血管语义分割受限于标注数据稀缺和模型跨模态泛化能力差
2. 方法要点：生成大规模合成数据集，强调血管管状和分支形状，减少纹理依赖
3. 实验或效果：预训练模型在少样本和零样本场景下，在真实数据集表现优异

## 📄 摘要（原文）

> Semantic segmentation of blood vessels is an important task in medical image
> analysis, but its progress is often hindered by the scarcity of large annotated
> datasets and the poor generalization of models across different imaging
> modalities. A key aspect is the tendency of Convolutional Neural Networks
> (CNNs) to learn texture-based features, which limits their performance when
> applied to new domains with different visual characteristics. We hypothesize
> that leveraging geometric priors of vessel shapes, such as their tubular and
> branching nature, can lead to more robust and data-efficient models. To
> investigate this, we introduce VessShape, a methodology for generating
> large-scale 2D synthetic datasets designed to instill a shape bias in
> segmentation models. VessShape images contain procedurally generated tubular
> geometries combined with a wide variety of foreground and background textures,
> encouraging models to learn shape cues rather than textures. We demonstrate
> that a model pre-trained on VessShape images achieves strong few-shot
> segmentation performance on two real-world datasets from different domains,
> requiring only four to ten samples for fine-tuning. Furthermore, the model
> exhibits notable zero-shot capabilities, effectively segmenting vessels in
> unseen domains without any target-specific training. Our results indicate that
> pre-training with a strong shape bias can be an effective strategy to overcome
> data scarcity and improve model generalization in blood vessel segmentation.

