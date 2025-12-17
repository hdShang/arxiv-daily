---
layout: default
title: Dynamic Weight-based Temporal Aggregation for Low-light Video Enhancement
---

# Dynamic Weight-based Temporal Aggregation for Low-light Video Enhancement

**arXiv**: [2510.09450v1](https://arxiv.org/abs/2510.09450) | [PDF](https://arxiv.org/pdf/2510.09450.pdf)

**作者**: Ruirui Lin, Guoxi Huang, Nantheera Anantrasirichai

---

## 💡 一句话要点

**提出DWTA-Net框架以解决低光视频增强中的噪声和伪影问题**

**关键词**: `低光视频增强` `时序聚合` `动态权重` `光流引导` `纹理自适应损失`

## 📋 核心要点

1. 核心问题：低光视频存在噪声、低对比度和颜色退化，现有方法难以有效利用时序信息。
2. 方法要点：采用两阶段框架，结合短长期时序线索，通过动态权重聚合和光流引导优化。
3. 实验或效果：在真实低光视频上验证，有效抑制噪声和伪影，视觉质量优于先进方法。

## 📄 摘要（原文）

> Low-light video enhancement (LLVE) is challenging due to noise, low contrast,
> and color degradations. Learning-based approaches offer fast inference but
> still struggle with heavy noise in real low-light scenes, primarily due to
> limitations in effectively leveraging temporal information. In this paper, we
> address this issue with DWTA-Net, a novel two-stage framework that jointly
> exploits short- and long-term temporal cues. Stage I employs Visual State-Space
> blocks for multi-frame alignment, recovering brightness, color, and structure
> with local consistency. Stage II introduces a recurrent refinement module with
> dynamic weight-based temporal aggregation guided by optical flow, adaptively
> balancing static and dynamic regions. A texture-adaptive loss further preserves
> fine details while promoting smoothness in flat areas. Experiments on
> real-world low-light videos show that DWTA-Net effectively suppresses noise and
> artifacts, delivering superior visual quality compared with state-of-the-art
> methods.

