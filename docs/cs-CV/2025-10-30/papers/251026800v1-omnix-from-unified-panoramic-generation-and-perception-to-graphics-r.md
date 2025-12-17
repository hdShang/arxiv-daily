---
layout: default
title: OmniX: From Unified Panoramic Generation and Perception to Graphics-Ready 3D Scenes
---

# OmniX: From Unified Panoramic Generation and Perception to Graphics-Ready 3D Scenes

**arXiv**: [2510.26800v1](https://arxiv.org/abs/2510.26800) | [PDF](https://arxiv.org/pdf/2510.26800.pdf)

**作者**: Yukun Huang, Jiwen Yu, Yanning Zhou, Jianan Wang, Xintao Wang, Pengfei Wan, Xihui Liu

---

## 💡 一句话要点

**提出OmniX框架，从全景生成与感知生成图形就绪3D场景**

**关键词**: `全景生成` `3D场景生成` `跨模态适配器` `物理渲染` `合成数据集`

## 📋 核心要点

1. 核心问题：现有2D提升方法忽略内在属性感知，无法生成适合物理渲染的3D场景。
2. 方法要点：基于跨模态适配器，复用2D生成先验，统一处理全景感知、生成与补全。
3. 实验或效果：构建大规模合成全景数据集，实验验证模型在感知与生成中的有效性。

## 📄 摘要（原文）

> There are two prevalent ways to constructing 3D scenes: procedural generation
> and 2D lifting. Among them, panorama-based 2D lifting has emerged as a
> promising technique, leveraging powerful 2D generative priors to produce
> immersive, realistic, and diverse 3D environments. In this work, we advance
> this technique to generate graphics-ready 3D scenes suitable for physically
> based rendering (PBR), relighting, and simulation. Our key insight is to
> repurpose 2D generative models for panoramic perception of geometry, textures,
> and PBR materials. Unlike existing 2D lifting approaches that emphasize
> appearance generation and ignore the perception of intrinsic properties, we
> present OmniX, a versatile and unified framework. Based on a lightweight and
> efficient cross-modal adapter structure, OmniX reuses 2D generative priors for
> a broad range of panoramic vision tasks, including panoramic perception,
> generation, and completion. Furthermore, we construct a large-scale synthetic
> panorama dataset containing high-quality multimodal panoramas from diverse
> indoor and outdoor scenes. Extensive experiments demonstrate the effectiveness
> of our model in panoramic visual perception and graphics-ready 3D scene
> generation, opening new possibilities for immersive and physically realistic
> virtual world generation.

