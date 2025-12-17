---
layout: default
title: From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors
---

# From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

**arXiv**: [2510.17439v1](https://arxiv.org/abs/2510.17439) | [PDF](https://arxiv.org/pdf/2510.17439.pdf)

**作者**: Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang, Francis E. H. Tay, Sijin Chen, Ziwei Liu, Yuxiao Liu, Xinghang Li, Pan Zhou

---

## 💡 一句话要点

**提出FALCON范式，通过注入3D空间令牌解决VLA模型空间推理不足问题**

**关键词**: `视觉-语言-动作模型` `3D空间推理` `空间基础模型` `模态融合` `动作头增强`

## 📋 核心要点

1. 现有VLA模型基于2D编码器，存在空间推理差距，限制泛化与适应性
2. FALCON利用空间基础模型从RGB提取几何先验，并可选融合深度或姿态
3. 在模拟和真实世界任务中实现SOTA性能，保持鲁棒性

## 📄 摘要（原文）

> Existing vision-language-action (VLA) models act in 3D real-world but are
> typically built on 2D encoders, leaving a spatial reasoning gap that limits
> generalization and adaptability. Recent 3D integration techniques for VLAs
> either require specialized sensors and transfer poorly across modalities, or
> inject weak cues that lack geometry and degrade vision-language alignment. In
> this work, we introduce FALCON (From Spatial to Action), a novel paradigm that
> injects rich 3D spatial tokens into the action head. FALCON leverages spatial
> foundation models to deliver strong geometric priors from RGB alone, and
> includes an Embodied Spatial Model that can optionally fuse depth, or pose for
> higher fidelity when available, without retraining or architectural changes. To
> preserve language reasoning, spatial tokens are consumed by a Spatial-Enhanced
> Action Head rather than being concatenated into the vision-language backbone.
> These designs enable FALCON to address limitations in spatial representation,
> modality transferability, and alignment. In comprehensive evaluations across
> three simulation benchmarks and eleven real-world tasks, our proposed FALCON
> achieves state-of-the-art performance, consistently surpasses competitive
> baselines, and remains robust under clutter, spatial-prompt conditioning, and
> variations in object scale and height.

