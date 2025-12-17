---
layout: default
title: Finding 3D Scene Analogies with Multimodal Foundation Models
---

# Finding 3D Scene Analogies with Multimodal Foundation Models

**arXiv**: [2510.23184v1](https://arxiv.org/abs/2510.23184) | [PDF](https://arxiv.org/pdf/2510.23184.pdf)

**作者**: Junho Kim, Young Min Kim

---

## 💡 一句话要点

**提出基于多模态基础模型的3D场景类比方法，实现零样本开放词汇场景对应**

**关键词**: `3D场景类比` `多模态基础模型` `零样本学习` `开放词汇` `轨迹转移` `混合神经表示`

## 📋 核心要点

1. 核心问题：现有3D场景类比方法需额外训练和固定对象词汇，限制泛化能力。
2. 方法要点：使用混合神经表示，结合视觉语言模型图和3D形状模型特征场，进行粗到精对齐。
3. 实验或效果：能建立复杂场景间准确对应，应用于轨迹和路径点转移。

## 📄 摘要（原文）

> Connecting current observations with prior experiences helps robots adapt and
> plan in new, unseen 3D environments. Recently, 3D scene analogies have been
> proposed to connect two 3D scenes, which are smooth maps that align scene
> regions with common spatial relationships. These maps enable detailed transfer
> of trajectories or waypoints, potentially supporting demonstration transfer for
> imitation learning or task plan transfer across scenes. However, existing
> methods for the task require additional training and fixed object vocabularies.
> In this work, we propose to use multimodal foundation models for finding 3D
> scene analogies in a zero-shot, open-vocabulary setting. Central to our
> approach is a hybrid neural representation of scenes that consists of a sparse
> graph based on vision-language model features and a feature field derived from
> 3D shape foundation models. 3D scene analogies are then found in a
> coarse-to-fine manner, by first aligning the graph and refining the
> correspondence with feature fields. Our method can establish accurate
> correspondences between complex scenes, and we showcase applications in
> trajectory and waypoint transfer.

