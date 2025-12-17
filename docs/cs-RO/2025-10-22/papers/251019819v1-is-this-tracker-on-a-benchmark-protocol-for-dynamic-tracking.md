---
layout: default
title: Is This Tracker On? A Benchmark Protocol for Dynamic Tracking
---

# Is This Tracker On? A Benchmark Protocol for Dynamic Tracking

**arXiv**: [2510.19819v1](https://arxiv.org/abs/2510.19819) | [PDF](https://arxiv.org/pdf/2510.19819.pdf)

**作者**: Ilona Demler, Saumya Chauhan, Georgia Gkioxari

---

## 💡 一句话要点

**提出ITTO基准套件以评估点跟踪方法在真实世界动态中的性能**

**关键词**: `点跟踪基准` `动态跟踪评估` `遮挡重识别` `真实世界视频` `性能诊断`

## 📋 核心要点

1. 核心问题：现有点跟踪方法在真实世界运动复杂性、遮挡和对象多样性方面存在局限
2. 方法要点：构建基于现有数据集和第一人称视频的基准，采用多阶段流程收集高质量人工标注
3. 实验或效果：分析显示跟踪器在遮挡后重识别方面表现不佳，揭示关键失败模式

## 📄 摘要（原文）

> We introduce ITTO, a challenging new benchmark suite for evaluating and
> diagnosing the capabilities and limitations of point tracking methods. Our
> videos are sourced from existing datasets and egocentric real-world recordings,
> with high-quality human annotations collected through a multi-stage pipeline.
> ITTO captures the motion complexity, occlusion patterns, and object diversity
> characteristic of real-world scenes -- factors that are largely absent in
> current benchmarks. We conduct a rigorous analysis of state-of-the-art tracking
> methods on ITTO, breaking down performance along key axes of motion complexity.
> Our findings reveal that existing trackers struggle with these challenges,
> particularly in re-identifying points after occlusion, highlighting critical
> failure modes. These results point to the need for new modeling approaches
> tailored to real-world dynamics. We envision ITTO as a foundation testbed for
> advancing point tracking and guiding the development of more robust tracking
> algorithms.

