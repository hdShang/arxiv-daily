---
layout: default
title: Consistent text-to-image generation via scene de-contextualization
---

# Consistent text-to-image generation via scene de-contextualization

**arXiv**: [2510.14553v1](https://arxiv.org/abs/2510.14553) | [PDF](https://arxiv.org/pdf/2510.14553.pdf)

**作者**: Song Tang, Peihao Gong, Kunyu Li, Kai Guo, Boyu Wang, Mao Ye, Jianwei Zhang, Xiatian Zhu

---

## 💡 一句话要点

**提出场景去上下文化方法以解决文本到图像生成中的身份偏移问题**

**关键词**: `文本到图像生成` `身份保持` `场景去上下文化` `提示嵌入编辑` `训练无关方法`

## 📋 核心要点

1. 核心问题：文本到图像生成中身份偏移源于主体与场景上下文的内在相关性
2. 方法要点：通过训练无关的提示嵌入编辑，抑制潜在场景-身份相关性
3. 实验或效果：显著提升身份保持，同时维持场景多样性

## 📄 摘要（原文）

> Consistent text-to-image (T2I) generation seeks to produce
> identity-preserving images of the same subject across diverse scenes, yet it
> often fails due to a phenomenon called identity (ID) shift. Previous methods
> have tackled this issue, but typically rely on the unrealistic assumption of
> knowing all target scenes in advance. This paper reveals that a key source of
> ID shift is the native correlation between subject and scene context, called
> scene contextualization, which arises naturally as T2I models fit the training
> distribution of vast natural images. We formally prove the near-universality of
> this scene-ID correlation and derive theoretical bounds on its strength. On
> this basis, we propose a novel, efficient, training-free prompt embedding
> editing approach, called Scene De-Contextualization (SDeC), that imposes an
> inversion process of T2I's built-in scene contextualization. Specifically, it
> identifies and suppresses the latent scene-ID correlation within the ID
> prompt's embedding by quantifying the SVD directional stability to adaptively
> re-weight the corresponding eigenvalues. Critically, SDeC allows for per-scene
> use (one scene per prompt) without requiring prior access to all target scenes.
> This makes it a highly flexible and general solution well-suited to real-world
> applications where such prior knowledge is often unavailable or varies over
> time. Experiments demonstrate that SDeC significantly enhances identity
> preservation while maintaining scene diversity.

