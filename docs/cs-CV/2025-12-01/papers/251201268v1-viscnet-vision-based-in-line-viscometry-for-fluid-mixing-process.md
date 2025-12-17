---
layout: default
title: ViscNet: Vision-Based In-line Viscometry for Fluid Mixing Process
---

# ViscNet: Vision-Based In-line Viscometry for Fluid Mixing Process

**arXiv**: [2512.01268v1](https://arxiv.org/abs/2512.01268) | [PDF](https://arxiv.org/pdf/2512.01268.pdf)

**作者**: Jongwon Sohn, Juhyeon Moon, Hyunjoon Jung, Jaewook Nam

---

## 💡 一句话要点

**提出基于视觉的在线粘度计ViscNet，通过光折射分析流体混合过程，实现非侵入式粘度测量。**

**关键词**: `视觉粘度测量` `非侵入式传感器` `流体混合过程` `光学畸变分析` `不确定性量化`

## 📋 核心要点

1. 核心问题：传统粘度计侵入性强，需实验室环境，难以适应实际过程条件。
2. 方法要点：利用固定背景图案在混合流体自由表面光折射下的光学畸变，推断粘度。
3. 实验或效果：在多种光照下，回归误差为0.113 log m² s⁻¹，分类准确率达81%，并集成不确定性量化。

## 📄 摘要（原文）

> Viscosity measurement is essential for process monitoring and autonomous laboratory operation, yet conventional viscometers remain invasive and require controlled laboratory environments that differ substantially from real process conditions. We present a computer-vision-based viscometer that infers viscosity by exploiting how a fixed background pattern becomes optically distorted as light refracts through the mixing-driven, continuously deforming free surface. Under diverse lighting conditions, the system achieves a mean absolute error of 0.113 in log m2 s^-1 units for regression and reaches up to 81% accuracy in viscosity-class prediction. Although performance declines for classes with closely clustered viscosity values, a multi-pattern strategy improves robustness by providing enriched visual cues. To ensure sensor reliability, we incorporate uncertainty quantification, enabling viscosity predictions with confidence estimates. This stand-off viscometer offers a practical, automation-ready alternative to existing viscometry methods.

