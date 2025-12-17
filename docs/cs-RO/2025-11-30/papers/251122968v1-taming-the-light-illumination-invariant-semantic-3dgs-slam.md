---
layout: default
title: Taming the Light: Illumination-Invariant Semantic 3DGS-SLAM
---

# Taming the Light: Illumination-Invariant Semantic 3DGS-SLAM

**arXiv**: [2511.22968v1](https://arxiv.org/abs/2511.22968) | [PDF](https://arxiv.org/pdf/2511.22968.pdf)

**作者**: Shouhe Zhang, Dayong Ren, Sensen Song, Yurong Qian, Zhenhong Jia

---

## 💡 一句话要点

**提出语义SLAM框架以解决极端光照下3D重建与语义分割退化问题**

**关键词**: `语义SLAM` `光照不变性` `3D高斯溅射` `外观归一化` `动态辐射平衡损失`

## 📋 核心要点

1. 核心问题：极端光照导致3D地图重建和语义分割精度下降，影响紧耦合系统性能。
2. 方法要点：设计IAN模块主动解耦场景固有属性，结合DRB-Loss反应性处理极端曝光帧。
3. 实验或效果：在公开数据集上实现相机跟踪、地图质量及语义几何精度的先进性能。

## 📄 摘要（原文）

> Extreme exposure degrades both the 3D map reconstruction and semantic segmentation accuracy, which is particularly detrimental to tightly-coupled systems. To achieve illumination invariance, we propose a novel semantic SLAM framework with two designs. First, the Intrinsic Appearance Normalization (IAN) module proactively disentangles the scene's intrinsic properties, such as albedo, from transient lighting. By learning a standardized, illumination-invariant appearance model, it assigns a stable and consistent color representation to each Gaussian primitive. Second, the Dynamic Radiance Balancing Loss (DRB-Loss) reactively handles frames with extreme exposure. It activates only when an image's exposure is poor, operating directly on the radiance field to guide targeted optimization. This prevents error accumulation from extreme lighting without compromising performance under normal conditions. The synergy between IAN's proactive invariance and DRB-Loss's reactive correction endows our system with unprecedented robustness. Evaluations on public datasets demonstrate state-of-the-art performance in camera tracking, map quality, and semantic and geometric accuracy.

