---
layout: default
title: Free-Grained Hierarchical Recognition
---

# Free-Grained Hierarchical Recognition

**arXiv**: [2510.14737v1](https://arxiv.org/abs/2510.14737) | [PDF](https://arxiv.org/pdf/2510.14737.pdf)

**作者**: Seulki Park, Zilin Wang, Stella X. Yu

---

## 💡 一句话要点

**提出自由粒度学习以解决混合粒度监督下的层次图像分类问题**

**关键词**: `层次图像分类` `混合粒度监督` `自由粒度学习` `ImageNet-F基准` `CLIP模型` `半监督学习`

## 📋 核心要点

1. 核心问题：现实世界图像标注粒度不一，现有方法依赖完整细粒度标注，难以实用。
2. 方法要点：引入ImageNet-F基准，利用CLIP模拟混合粒度标签，开发伪属性和半监督方法。
3. 实验或效果：在混合监督下，所提方法显著提升层次分类性能，优于强基线。

## 📄 摘要（原文）

> Hierarchical image classification predicts labels across a semantic taxonomy,
> but existing methods typically assume complete, fine-grained annotations, an
> assumption rarely met in practice. Real-world supervision varies in
> granularity, influenced by image quality, annotator expertise, and task
> demands; a distant bird may be labeled Bird, while a close-up reveals Bald
> eagle. We introduce ImageNet-F, a large-scale benchmark curated from ImageNet
> and structured into cognitively inspired basic, subordinate, and fine-grained
> levels. Using CLIP as a proxy for semantic ambiguity, we simulate realistic,
> mixed-granularity labels reflecting human annotation behavior. We propose
> free-grain learning, with heterogeneous supervision across instances. We
> develop methods that enhance semantic guidance via pseudo-attributes from
> vision-language models and visual guidance via semi-supervised learning. These,
> along with strong baselines, substantially improve performance under mixed
> supervision. Together, our benchmark and methods advance hierarchical
> classification under real-world constraints.

