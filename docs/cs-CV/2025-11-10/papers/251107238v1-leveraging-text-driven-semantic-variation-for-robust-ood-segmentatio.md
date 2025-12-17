---
layout: default
title: Leveraging Text-Driven Semantic Variation for Robust OOD Segmentation
---

# Leveraging Text-Driven Semantic Variation for Robust OOD Segmentation

**arXiv**: [2511.07238v1](https://arxiv.org/abs/2511.07238) | [PDF](https://arxiv.org/pdf/2511.07238.pdf)

**作者**: Seungheon Song, Jaekoo Lee

---

## 💡 一句话要点

**提出文本驱动OOD分割方法，利用视觉语言空间提升自动驾驶异常分割鲁棒性**

**关键词**: `OOD分割` `视觉语言模型` `自动驾驶安全` `语义增强` `Transformer解码器`

## 📋 核心要点

1. 核心问题：自动驾驶中OOD分割对安全至关重要，但现有方法未充分利用语言知识
2. 方法要点：结合视觉语言编码器与Transformer解码器，使用距离提示和语义增强
3. 实验效果：在多个数据集上实现SOTA性能，验证了方法的泛化性和鲁棒性

## 📄 摘要（原文）

> In autonomous driving and robotics, ensuring road safety and reliable
> decision-making critically depends on out-of-distribution (OOD) segmentation.
> While numerous methods have been proposed to detect anomalous objects on the
> road, leveraging the vision-language space-which provides rich linguistic
> knowledge-remains an underexplored field. We hypothesize that incorporating
> these linguistic cues can be especially beneficial in the complex contexts
> found in real-world autonomous driving scenarios.
>   To this end, we present a novel approach that trains a Text-Driven OOD
> Segmentation model to learn a semantically diverse set of objects in the
> vision-language space. Concretely, our approach combines a vision-language
> model's encoder with a transformer decoder, employs Distance-Based OOD prompts
> located at varying semantic distances from in-distribution (ID) classes, and
> utilizes OOD Semantic Augmentation for OOD representations. By aligning visual
> and textual information, our approach effectively generalizes to unseen objects
> and provides robust OOD segmentation in diverse driving environments.
>   We conduct extensive experiments on publicly available OOD segmentation
> datasets such as Fishyscapes, Segment-Me-If-You-Can, and Road Anomaly datasets,
> demonstrating that our approach achieves state-of-the-art performance across
> both pixel-level and object-level evaluations. This result underscores the
> potential of vision-language-based OOD segmentation to bolster the safety and
> reliability of future autonomous driving systems.

