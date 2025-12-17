---
layout: default
title: DepthFocus: Controllable Depth Estimation for See-Through Scenes
---

# DepthFocus: Controllable Depth Estimation for See-Through Scenes

**arXiv**: [2511.16993v1](https://arxiv.org/abs/2511.16993) | [PDF](https://arxiv.org/pdf/2511.16993.pdf)

**作者**: Junhong Min, Jimin Kim, Cheol-Hui Min, Minwook Kim, Youngpil Jeon, Minyong Choi

---

## 💡 一句话要点

**提出DepthFocus可控深度估计模型，以解决透视场景中的多层深度模糊问题。**

**关键词**: `深度估计` `可控视觉` `透视场景` `Vision Transformer` `合成数据集`

## 📋 核心要点

1. 核心问题：真实世界深度多层面，透射材料导致传统系统难以估计动态焦点深度。
2. 方法要点：基于深度偏好标量，使用可引导Vision Transformer实现意图驱动的深度估计。
3. 实验或效果：在BOOSTER等基准上表现优异，并在新多深度数据集上验证意图对齐估计。

## 📄 摘要（原文）

> Depth in the real world is rarely singular. Transmissive materials create layered ambiguities that confound conventional perception systems. Existing models remain passive, attempting to estimate static depth maps anchored to the nearest surface, while humans actively shift focus to perceive a desired depth. We introduce DepthFocus, a steerable Vision Transformer that redefines stereo depth estimation as intent-driven control. Conditioned on a scalar depth preference, the model dynamically adapts its computation to focus on the intended depth, enabling selective perception within complex scenes. The training primarily leverages our newly constructed 500k multi-layered synthetic dataset, designed to capture diverse see-through effects. DepthFocus not only achieves state-of-the-art performance on conventional single-depth benchmarks like BOOSTER, a dataset notably rich in transparent and reflective objects, but also quantitatively demonstrates intent-aligned estimation on our newly proposed real and synthetic multi-depth datasets. Moreover, it exhibits strong generalization capabilities on unseen see-through scenes, underscoring its robustness as a significant step toward active and human-like 3D perception.

