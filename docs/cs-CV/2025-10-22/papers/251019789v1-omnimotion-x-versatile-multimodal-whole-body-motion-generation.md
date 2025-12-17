---
layout: default
title: OmniMotion-X: Versatile Multimodal Whole-Body Motion Generation
---

# OmniMotion-X: Versatile Multimodal Whole-Body Motion Generation

**arXiv**: [2510.19789v1](https://arxiv.org/abs/2510.19789) | [PDF](https://arxiv.org/pdf/2510.19789.pdf)

**作者**: Guowei Xu, Yuxuan Bian, Ailing Zeng, Mingyi Shi, Shaoli Huang, Wen Li, Lixin Duan, Qiang Xu

---

## 💡 一句话要点

**提出OmniMotion-X框架以解决多模态全身运动生成问题**

**关键词**: `多模态运动生成` `自回归扩散变换器` `参考运动条件` `弱到强混合训练` `SMPL-X数据集` `长时程运动控制`

## 📋 核心要点

1. 核心问题：多模态任务中运动生成的一致性与可控性不足
2. 方法要点：采用自回归扩散变换器与参考运动条件增强生成质量
3. 实验或效果：在多个任务中超越现有方法，实现长时程可控运动生成

## 📄 摘要（原文）

> This paper introduces OmniMotion-X, a versatile multimodal framework for
> whole-body human motion generation, leveraging an autoregressive diffusion
> transformer in a unified sequence-to-sequence manner. OmniMotion-X efficiently
> supports diverse multimodal tasks, including text-to-motion, music-to-dance,
> speech-to-gesture, and global spatial-temporal control scenarios (e.g., motion
> prediction, in-betweening, completion, and joint/trajectory-guided synthesis),
> as well as flexible combinations of these tasks. Specifically, we propose the
> use of reference motion as a novel conditioning signal, substantially enhancing
> the consistency of generated content, style, and temporal dynamics crucial for
> realistic animations. To handle multimodal conflicts, we introduce a
> progressive weak-to-strong mixed-condition training strategy. To enable
> high-quality multimodal training, we construct OmniMoCap-X, the largest unified
> multimodal motion dataset to date, integrating 28 publicly available MoCap
> sources across 10 distinct tasks, standardized to the SMPL-X format at 30 fps.
> To ensure detailed and consistent annotations, we render sequences into videos
> and use GPT-4o to automatically generate structured and hierarchical captions,
> capturing both low-level actions and high-level semantics. Extensive
> experimental evaluations confirm that OmniMotion-X significantly surpasses
> existing methods, demonstrating state-of-the-art performance across multiple
> multimodal tasks and enabling the interactive generation of realistic,
> coherent, and controllable long-duration motions.

