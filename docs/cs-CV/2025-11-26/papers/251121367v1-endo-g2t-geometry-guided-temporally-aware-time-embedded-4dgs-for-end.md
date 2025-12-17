---
layout: default
title: Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes
---

# Endo-G$^{2}$T: Geometry-Guided & Temporally Aware Time-Embedded 4DGS For Endoscopic Scenes

**arXiv**: [2511.21367v1](https://arxiv.org/abs/2511.21367) | [PDF](https://arxiv.org/pdf/2511.21367.pdf)

**作者**: Yangle Liu, Fengze Li, Kan Liu, Jieming Ma

---

## 💡 一句话要点

**提出Endo-G²T方法以解决内窥镜场景中几何漂移与时间一致性问题**

**关键词**: `4D高斯溅射` `几何引导训练` `时间一致性` `内窥镜重建` `单目深度估计` `关键帧优化`

## 📋 核心要点

1. 内窥镜视频存在强视角依赖效应，纯光度监督易导致几何漂移
2. 采用几何引导先验蒸馏和时间嵌入高斯场，提升几何准确性与时间一致性
3. 在EndoNeRF和StereoMIS-P1数据集上实现单目重建最优结果

## 📄 摘要（原文）

> Endoscopic (endo) video exhibits strong view-dependent effects such as specularities, wet reflections, and occlusions. Pure photometric supervision misaligns with geometry and triggers early geometric drift, where erroneous shapes are reinforced during densification and become hard to correct. We ask how to anchor geometry early for 4D Gaussian splatting (4DGS) while maintaining temporal consistency and efficiency in dynamic endoscopic scenes. Thus, we present Endo-G$^{2}$T, a geometry-guided and temporally aware training scheme for time-embedded 4DGS. First, geo-guided prior distillation converts confidence-gated monocular depth into supervision with scale-invariant depth and depth-gradient losses, using a warm-up-to-cap schedule to inject priors softly and avoid early overfitting. Second, a time-embedded Gaussian field represents dynamics in XYZT with a rotor-like rotation parameterization, yielding temporally coherent geometry with lightweight regularization that favors smooth motion and crisp opacity boundaries. Third, keyframe-constrained streaming improves efficiency and long-horizon stability through keyframe-focused optimization under a max-points budget, while non-keyframes advance with lightweight updates. Across EndoNeRF and StereoMIS-P1 datasets, Endo-G$^{2}$T achieves state-of-the-art results among monocular reconstruction baselines.

