---
layout: default
title: BoRe-Depth: Self-supervised Monocular Depth Estimation with Boundary Refinement for Embedded Systems
---

# BoRe-Depth: Self-supervised Monocular Depth Estimation with Boundary Refinement for Embedded Systems

**arXiv**: [2511.04388v1](https://arxiv.org/abs/2511.04388) | [PDF](https://arxiv.org/pdf/2511.04388.pdf)

**作者**: Chang Liu, Juan Li, Sheng Zhang, Chang Liu, Jie Li, Xu Zhang

---

## 💡 一句话要点

**提出BoRe-Depth模型以解决嵌入式系统单目深度估计边界模糊问题**

**关键词**: `单目深度估计` `边界细化` `嵌入式系统` `轻量模型` `特征融合` `语义集成`

## 📋 核心要点

1. 核心问题：嵌入式系统单目深度估计性能差、对象边界模糊
2. 方法要点：设计EFAF模块融合深度特征，集成语义知识提升边界感知
3. 实验或效果：模型参数量8.7M，在NVIDIA Jetson Orin上运行50.7 FPS，边界质量显著提升

## 📄 摘要（原文）

> Depth estimation is one of the key technologies for realizing 3D perception
> in unmanned systems. Monocular depth estimation has been widely researched
> because of its low-cost advantage, but the existing methods face the challenges
> of poor depth estimation performance and blurred object boundaries on embedded
> systems. In this paper, we propose a novel monocular depth estimation model,
> BoRe-Depth, which contains only 8.7M parameters. It can accurately estimate
> depth maps on embedded systems and significantly improves boundary quality.
> Firstly, we design an Enhanced Feature Adaptive Fusion Module (EFAF) which
> adaptively fuses depth features to enhance boundary detail representation.
> Secondly, we integrate semantic knowledge into the encoder to improve the
> object recognition and boundary perception capabilities. Finally, BoRe-Depth is
> deployed on NVIDIA Jetson Orin, and runs efficiently at 50.7 FPS. We
> demonstrate that the proposed model significantly outperforms previous
> lightweight models on multiple challenging datasets, and we provide detailed
> ablation studies for the proposed methods. The code is available at
> https://github.com/liangxiansheng093/BoRe-Depth.

