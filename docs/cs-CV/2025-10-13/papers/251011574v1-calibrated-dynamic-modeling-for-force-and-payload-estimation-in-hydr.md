---
layout: default
title: Calibrated Dynamic Modeling for Force and Payload Estimation in Hydraulic Machinery
---

# Calibrated Dynamic Modeling for Force and Payload Estimation in Hydraulic Machinery

**arXiv**: [2510.11574v1](https://arxiv.org/abs/2510.11574) | [PDF](https://arxiv.org/pdf/2510.11574.pdf)

**作者**: Lennart Werner, Pol Eyschen, Sean Costello, Pierluigi Micarelli, Marco Hutter

---

## 💡 一句话要点

**提出高精度动态建模方法，用于液压机械的力和载荷估计，实现自动化操作。**

**关键词**: `液压机械` `动态建模` `力估计` `载荷估计` `实时估计` `自动化控制`

## 📋 核心要点

1. 核心问题：液压挖掘机末端执行器交互力的实时精确估计是重型机械自动化的关键。
2. 方法要点：基于优化的动态模型识别，无需额外轨迹要求或机器特定动态知识。
3. 实验或效果：在25吨挖掘机上，载荷估计精度达1%，力测量方向精度13度。

## 📄 摘要（原文）

> Accurate real-time estimation of end effector interaction forces in hydraulic
> excavators is a key enabler for advanced automation in heavy machinery.
> Accurate knowledge of these forces allows improved, precise grading and digging
> maneuvers. To address these challenges, we introduce a high-accuracy,
> retrofittable 2D force- and payload estimation algorithm that does not impose
> additional requirements on the operator regarding trajectory, acceleration or
> the use of the slew joint. The approach is designed for retrofittability,
> requires minimal calibration and no prior knowledge of machine-specific dynamic
> characteristics. Specifically, we propose a method for identifying a dynamic
> model, necessary to estimate both end effector interaction forces and bucket
> payload during normal operation. Our optimization-based payload estimation
> achieves a full-scale payload accuracy of 1%. On a standard 25 t excavator, the
> online force measurement from pressure and inertial measurements achieves a
> direction accuracy of 13 degree and a magnitude accuracy of 383 N. The method's
> accuracy and generalization capability are validated on two excavator platforms
> of different type and weight classes. We benchmark our payload estimation
> against a classical quasistatic method and a commercially available system. Our
> system outperforms both in accuracy and precision.

