---
layout: default
title: PlugTrack: Multi-Perceptive Motion Analysis for Adaptive Fusion in Multi-Object Tracking
---

# PlugTrack: Multi-Perceptive Motion Analysis for Adaptive Fusion in Multi-Object Tracking

**arXiv**: [2511.13105v1](https://arxiv.org/abs/2511.13105) | [PDF](https://arxiv.org/pdf/2511.13105.pdf)

**作者**: Seungjae Kim, SeungJoon Lee, MyeongAh Cho

---

## 💡 一句话要点

**提出PlugTrack框架，通过自适应融合运动预测器解决多目标跟踪中线性与非线性运动模式问题**

**关键词**: `多目标跟踪` `运动预测` `自适应融合` `卡尔曼滤波器` `数据驱动方法` `多感知分析`

## 📋 核心要点

1. 核心问题：多目标跟踪中，卡尔曼滤波器无法处理非线性运动，而数据驱动预测器泛化差且计算开销大
2. 方法要点：使用多感知运动分析生成自适应融合因子，结合卡尔曼滤波器和数据驱动预测器
3. 实验或效果：在MOT17/MOT20上性能显著提升，在DanceTrack上达到最先进水平，无需修改现有预测器

## 📄 摘要（原文）

> Multi-object tracking (MOT) predominantly follows the tracking-by-detection paradigm, where Kalman filters serve as the standard motion predictor due to computational efficiency but inherently fail on non-linear motion patterns. Conversely, recent data-driven motion predictors capture complex non-linear dynamics but suffer from limited domain generalization and computational overhead. Through extensive analysis, we reveal that even in datasets dominated by non-linear motion, Kalman filter outperforms data-driven predictors in up to 34\% of cases, demonstrating that real-world tracking scenarios inherently involve both linear and non-linear patterns. To leverage this complementarity, we propose PlugTrack, a novel framework that adaptively fuses Kalman filter and data-driven motion predictors through multi-perceptive motion understanding. Our approach employs multi-perceptive motion analysis to generate adaptive blending factors. PlugTrack achieves significant performance gains on MOT17/MOT20 and state-of-the-art on DanceTrack without modifying existing motion predictors. To the best of our knowledge, PlugTrack is the first framework to bridge classical and modern motion prediction paradigms through adaptive fusion in MOT.

