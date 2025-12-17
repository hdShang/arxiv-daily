---
layout: default
title: PhySIC: Physically Plausible 3D Human-Scene Interaction and Contact from a Single Image
---

# PhySIC: Physically Plausible 3D Human-Scene Interaction and Contact from a Single Image

**arXiv**: [2510.11649v1](https://arxiv.org/abs/2510.11649) | [PDF](https://arxiv.org/pdf/2510.11649.pdf)

**作者**: Pradyumna Yalandur Muralidhar, Yuxuan Xue, Xianghui Xie, Margaret Kostyrko, Gerard Pons-Moll

---

## 💡 一句话要点

**提出PhySIC框架，从单张图像重建物理合理的人类-场景交互与接触**

**关键词**: `3D人体重建` `场景理解` `物理合理性` `单图像重建` `接触检测`

## 📋 核心要点

1. 核心问题：单图像重建存在深度模糊、遮挡和物理不一致接触，导致3D人类与场景不准确
2. 方法要点：通过遮挡感知修复、深度融合和置信优化，恢复SMPL-X人体网格与场景表面
3. 实验或效果：在基准测试中显著降低场景误差和姿态误差，提升接触检测F1分数

## 📄 摘要（原文）

> Reconstructing metrically accurate humans and their surrounding scenes from a
> single image is crucial for virtual reality, robotics, and comprehensive 3D
> scene understanding. However, existing methods struggle with depth ambiguity,
> occlusions, and physically inconsistent contacts. To address these challenges,
> we introduce PhySIC, a framework for physically plausible Human-Scene
> Interaction and Contact reconstruction. PhySIC recovers metrically consistent
> SMPL-X human meshes, dense scene surfaces, and vertex-level contact maps within
> a shared coordinate frame from a single RGB image. Starting from coarse
> monocular depth and body estimates, PhySIC performs occlusion-aware inpainting,
> fuses visible depth with unscaled geometry for a robust metric scaffold, and
> synthesizes missing support surfaces like floors. A confidence-weighted
> optimization refines body pose, camera parameters, and global scale by jointly
> enforcing depth alignment, contact priors, interpenetration avoidance, and 2D
> reprojection consistency. Explicit occlusion masking safeguards invisible
> regions against implausible configurations. PhySIC is efficient, requiring only
> 9 seconds for joint human-scene optimization and under 27 seconds end-to-end.
> It naturally handles multiple humans, enabling reconstruction of diverse
> interactions. Empirically, PhySIC outperforms single-image baselines, reducing
> mean per-vertex scene error from 641 mm to 227 mm, halving PA-MPJPE to 42 mm,
> and improving contact F1 from 0.09 to 0.51. Qualitative results show realistic
> foot-floor interactions, natural seating, and plausible reconstructions of
> heavily occluded furniture. By converting a single image into a physically
> plausible 3D human-scene pair, PhySIC advances scalable 3D scene understanding.
> Our implementation is publicly available at https://yuxuan-xue.com/physic.

