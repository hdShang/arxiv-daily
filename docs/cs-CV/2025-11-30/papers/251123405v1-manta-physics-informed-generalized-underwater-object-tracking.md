---
layout: default
title: MANTA: Physics-Informed Generalized Underwater Object Tracking
---

# MANTA: Physics-Informed Generalized Underwater Object Tracking

**arXiv**: [2511.23405v1](https://arxiv.org/abs/2511.23405) | [PDF](https://arxiv.org/pdf/2511.23405.pdf)

**作者**: Suhas Srinath, Hemang Jamadagni, Aditya Chadrasekar, Prathosh AP

---

## 💡 一句话要点

**提出MANTA框架，通过物理信息增强表示学习和跟踪设计，解决水下物体跟踪的泛化问题。**

**关键词**: `水下物体跟踪` `物理信息学习` `对比学习` `多阶段跟踪` `几何一致性评估` `泛化性能`

## 📋 核心要点

1. 核心问题：水下波长依赖衰减和散射导致外观失真，现有陆地数据训练的跟踪器泛化能力差。
2. 方法要点：采用双正对比学习结合Beer-Lambert增强，以及多阶段物理信息关联算法，提升对时空扭曲的鲁棒性。
3. 实验或效果：在四个水下基准测试中实现SOTA，成功AUC提升最高6%，确保稳定长期跟踪和高效运行。

## 📄 摘要（原文）

> Underwater object tracking is challenging due to wavelength dependent attenuation and scattering, which severely distort appearance across depths and water conditions. Existing trackers trained on terrestrial data fail to generalize to these physics-driven degradations. We present MANTA, a physics-informed framework integrating representation learning with tracking design for underwater scenarios. We propose a dual-positive contrastive learning strategy coupling temporal consistency with Beer-Lambert augmentations to yield features robust to both temporal and underwater distortions. We further introduce a multi-stage pipeline augmenting motion-based tracking with a physics-informed secondary association algorithm that integrates geometric consistency and appearance similarity for re-identification under occlusion and drift. To complement standard IoU metrics, we propose Center-Scale Consistency (CSC) and Geometric Alignment Score (GAS) to assess geometric fidelity. Experiments on four underwater benchmarks (WebUOT-1M, UOT32, UTB180, UWCOT220) show that MANTA achieves state-of-the-art performance, improving Success AUC by up to 6 percent, while ensuring stable long-term generalized underwater tracking and efficient runtime.

