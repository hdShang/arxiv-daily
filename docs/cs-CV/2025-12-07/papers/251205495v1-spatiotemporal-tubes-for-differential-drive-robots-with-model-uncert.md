---
layout: default
title: Spatiotemporal Tubes for Differential Drive Robots with Model Uncertainty
---

# Spatiotemporal Tubes for Differential Drive Robots with Model Uncertainty

**arXiv**: [2512.05495v1](https://arxiv.org/abs/2512.05495) | [PDF](https://arxiv.org/pdf/2512.05495.pdf)

**作者**: Ratnangshu Das, Ahan Basu, Christos Verginis, Pushpak Jagtap

---

## 💡 一句话要点

**提出时空管控制框架，以保障带模型不确定性的差速机器人满足时序到达-避障-停留规范。**

**关键词**: `差速机器人控制` `时空管` `时序规范` `鲁棒控制` `模型不确定性` `避障导航`

## 📋 核心要点

1. 核心问题：差速移动机器人在动态不确定性和外部干扰下，如何保证满足时序到达-避障-停留规范。
2. 方法要点：采用圆形时空管定义动态安全走廊，结合采样合成算法和闭式控制律，无需模型近似或在线优化。
3. 实验或效果：仿真验证显示，框架在鲁棒性、准确性和计算效率上优于现有方法。

## 📄 摘要（原文）

> This paper presents a Spatiotemporal Tube (STT)-based control framework for differential-drive mobile robots with dynamic uncertainties and external disturbances, guaranteeing the satisfaction of Temporal Reach-Avoid-Stay (T-RAS) specifications. The approach employs circular STT, characterized by smoothly time-varying center and radius, to define dynamic safe corridors that guide the robot from the start region to the goal while avoiding obstacles. In particular, we first develop a sampling-based synthesis algorithm to construct a feasible STT that satisfies the prescribed timing and safety constraints with formal guarantees. To ensure that the robot remains confined within this tube, we then design analytically a closed-form, approximation-free control law. The resulting controller is computationally efficient, robust to disturbances and {model uncertainties}, and requires no model approximations or online optimization. The proposed framework is validated through simulation studies on a differential-drive robot and benchmarked against state-of-the-art methods, demonstrating superior robustness, accuracy, and computational efficiency.

