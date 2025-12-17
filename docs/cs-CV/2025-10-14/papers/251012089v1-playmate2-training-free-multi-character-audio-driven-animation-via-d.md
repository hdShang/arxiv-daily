---
layout: default
title: Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback
---

# Playmate2: Training-Free Multi-Character Audio-Driven Animation via Diffusion Transformer with Reward Feedback

**arXiv**: [2510.12089v1](https://arxiv.org/abs/2510.12089) | [PDF](https://arxiv.org/pdf/2510.12089.pdf)

**作者**: Xingpei Ma, Shenneng Huang, Jiaran Cai, Yuansheng Guan, Shen Zheng, Hanfeng Zhao, Qiang Zhang, Shunsi Zhang

---

## 💡 一句话要点

**提出基于扩散变换器的训练免费多角色音频驱动动画方法，以提升唇同步和长视频生成质量。**

**关键词**: `扩散变换器` `音频驱动动画` `多角色生成` `训练免费方法` `长视频生成` `唇同步增强`

## 📋 核心要点

1. 核心问题：现有方法在唇同步精度、长视频时序一致性和多角色动画方面存在挑战。
2. 方法要点：采用LoRA训练与位置偏移推理，结合奖励反馈增强唇同步和身体运动自然性。
3. 实验效果：在实验中超越现有方法，实现高质量、时序一致的多角色音频驱动视频生成。

## 📄 摘要（原文）

> Recent advances in diffusion models have significantly improved audio-driven
> human video generation, surpassing traditional methods in both quality and
> controllability. However, existing approaches still face challenges in lip-sync
> accuracy, temporal coherence for long video generation, and multi-character
> animation. In this work, we propose a diffusion transformer (DiT)-based
> framework for generating lifelike talking videos of arbitrary length, and
> introduce a training-free method for multi-character audio-driven animation.
> First, we employ a LoRA-based training strategy combined with a position shift
> inference approach, which enables efficient long video generation while
> preserving the capabilities of the foundation model. Moreover, we combine
> partial parameter updates with reward feedback to enhance both lip
> synchronization and natural body motion. Finally, we propose a training-free
> approach, Mask Classifier-Free Guidance (Mask-CFG), for multi-character
> animation, which requires no specialized datasets or model modifications and
> supports audio-driven animation for three or more characters. Experimental
> results demonstrate that our method outperforms existing state-of-the-art
> approaches, achieving high-quality, temporally coherent, and multi-character
> audio-driven video generation in a simple, efficient, and cost-effective
> manner.

