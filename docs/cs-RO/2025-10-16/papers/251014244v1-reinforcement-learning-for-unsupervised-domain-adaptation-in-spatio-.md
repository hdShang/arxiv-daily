---
layout: default
title: Reinforcement Learning for Unsupervised Domain Adaptation in Spatio-Temporal Echocardiography Segmentation
---

# Reinforcement Learning for Unsupervised Domain Adaptation in Spatio-Temporal Echocardiography Segmentation

**arXiv**: [2510.14244v1](https://arxiv.org/abs/2510.14244) | [PDF](https://arxiv.org/pdf/2510.14244.pdf)

**作者**: Arnaud Judge, Nicolas Duchateau, Thierry Judge, Roman A. Sandler, Joseph Z. Sokol, Christian Desrosiers, Olivier Bernard, Pierre-Marc Jodoin

---

## 💡 一句话要点

**提出RL4Seg3D框架，用于无监督领域自适应的心动图时空分割，提升精度与一致性。**

**关键词**: `无监督领域自适应` `心动图分割` `强化学习` `时空一致性` `不确定性估计`

## 📋 核心要点

1. 核心问题：心动图分割中领域差异导致精度低、时空不一致，且噪声干扰严重。
2. 方法要点：结合强化学习、新奖励函数和融合方案，增强关键地标精度与不确定性估计。
3. 实验或效果：在3万+心动图视频上验证，优于标准方法，无需目标域标签。

## 📄 摘要（原文）

> Domain adaptation methods aim to bridge the gap between datasets by enabling
> knowledge transfer across domains, reducing the need for additional expert
> annotations. However, many approaches struggle with reliability in the target
> domain, an issue particularly critical in medical image segmentation, where
> accuracy and anatomical validity are essential. This challenge is further
> exacerbated in spatio-temporal data, where the lack of temporal consistency can
> significantly degrade segmentation quality, and particularly in
> echocardiography, where the presence of artifacts and noise can further hinder
> segmentation performance. To address these issues, we present RL4Seg3D, an
> unsupervised domain adaptation framework for 2D + time echocardiography
> segmentation. RL4Seg3D integrates novel reward functions and a fusion scheme to
> enhance key landmark precision in its segmentations while processing full-sized
> input videos. By leveraging reinforcement learning for image segmentation, our
> approach improves accuracy, anatomical validity, and temporal consistency while
> also providing, as a beneficial side effect, a robust uncertainty estimator,
> which can be used at test time to further enhance segmentation performance. We
> demonstrate the effectiveness of our framework on over 30,000 echocardiographic
> videos, showing that it outperforms standard domain adaptation techniques
> without the need for any labels on the target domain. Code is available at
> https://github.com/arnaudjudge/RL4Seg3D.

