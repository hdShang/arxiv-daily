---
layout: default
title: XD-RCDepth: Lightweight Radar-Camera Depth Estimation with Explainability-Aligned and Distribution-Aware Distillation
---

# XD-RCDepth: Lightweight Radar-Camera Depth Estimation with Explainability-Aligned and Distribution-Aware Distillation

**arXiv**: [2510.13565v1](https://arxiv.org/abs/2510.13565) | [PDF](https://arxiv.org/pdf/2510.13565.pdf)

**作者**: Huawei Sun, Zixu Wang, Xiangyuan Peng, Julius Ott, Georg Stettinger, Lorenzo Servadei, Robert Wille

---

## 💡 一句话要点

**提出XD-RCDepth轻量雷达-相机深度估计方法，通过可解释性对齐和分布感知蒸馏提升性能。**

**关键词**: `深度估计` `雷达-相机融合` `知识蒸馏` `轻量架构` `自动驾驶` `可解释性`

## 📋 核心要点

1. 核心问题：自动驾驶中深度估计需在恶劣条件下保持鲁棒性，雷达-相机融合提供互补几何线索。
2. 方法要点：引入可解释性对齐蒸馏和深度分布蒸馏，将深度回归转化为软分类问题。
3. 实验效果：参数减少29.7%，MAE降低7.97%，在nuScenes和ZJU-4DRadarCam数据集上实现实时高效。

## 📄 摘要（原文）

> Depth estimation remains central to autonomous driving, and radar-camera
> fusion offers robustness in adverse conditions by providing complementary
> geometric cues. In this paper, we present XD-RCDepth, a lightweight
> architecture that reduces the parameters by 29.7% relative to the
> state-of-the-art lightweight baseline while maintaining comparable accuracy. To
> preserve performance under compression and enhance interpretability, we
> introduce two knowledge-distillation strategies: an explainability-aligned
> distillation that transfers the teacher's saliency structure to the student,
> and a depth-distribution distillation that recasts depth regression as soft
> classification over discretized bins. Together, these components reduce the MAE
> compared with direct training with 7.97% and deliver competitive accuracy with
> real-time efficiency on nuScenes and ZJU-4DRadarCam datasets.

