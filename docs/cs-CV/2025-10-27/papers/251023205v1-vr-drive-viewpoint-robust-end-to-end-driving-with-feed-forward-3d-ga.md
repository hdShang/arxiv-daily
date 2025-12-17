---
layout: default
title: VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting
---

# VR-Drive: Viewpoint-Robust End-to-End Driving with Feed-Forward 3D Gaussian Splatting

**arXiv**: [2510.23205v1](https://arxiv.org/abs/2510.23205) | [PDF](https://arxiv.org/pdf/2510.23205.pdf)

**作者**: Hoonhee Cho, Jae-Young Kang, Giwon Lee, Hyemin Yang, Heejun Park, Seokwoo Jung, Kuk-Jin Yoon

---

## 💡 一句话要点

**提出VR-Drive以解决端到端自动驾驶中相机视角变化的鲁棒性问题**

**关键词**: `端到端自动驾驶` `3D高斯泼溅` `视角鲁棒性` `视图合成` `蒸馏策略` `基准数据集`

## 📋 核心要点

1. 核心问题：端到端自动驾驶在多样化相机视角下缺乏鲁棒性，影响实际部署。
2. 方法要点：联合学习3D场景重建作为辅助任务，支持前馈推理和视角混合记忆库。
3. 实验或效果：在新型视角基准数据集上验证，提升规划性能并减少合成噪声。

## 📄 摘要（原文）

> End-to-end autonomous driving (E2E-AD) has emerged as a promising paradigm
> that unifies perception, prediction, and planning into a holistic, data-driven
> framework. However, achieving robustness to varying camera viewpoints, a common
> real-world challenge due to diverse vehicle configurations, remains an open
> problem. In this work, we propose VR-Drive, a novel E2E-AD framework that
> addresses viewpoint generalization by jointly learning 3D scene reconstruction
> as an auxiliary task to enable planning-aware view synthesis. Unlike prior
> scene-specific synthesis approaches, VR-Drive adopts a feed-forward inference
> strategy that supports online training-time augmentation from sparse views
> without additional annotations. To further improve viewpoint consistency, we
> introduce a viewpoint-mixed memory bank that facilitates temporal interaction
> across multiple viewpoints and a viewpoint-consistent distillation strategy
> that transfers knowledge from original to synthesized views. Trained in a fully
> end-to-end manner, VR-Drive effectively mitigates synthesis-induced noise and
> improves planning under viewpoint shifts. In addition, we release a new
> benchmark dataset to evaluate E2E-AD performance under novel camera viewpoints,
> enabling comprehensive analysis. Our results demonstrate that VR-Drive is a
> scalable and robust solution for the real-world deployment of end-to-end
> autonomous driving systems.

