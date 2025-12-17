---
layout: default
title: Depth Anything 3: Recovering the Visual Space from Any Views
---

# Depth Anything 3: Recovering the Visual Space from Any Views

**arXiv**: [2511.10647v1](https://arxiv.org/abs/2511.10647) | [PDF](https://arxiv.org/pdf/2511.10647.pdf)

**作者**: Haotong Lin, Sili Chen, Junhao Liew, Donny Y. Chen, Zhenyu Li, Guang Shi, Jiashi Feng, Bingyi Kang

---

## 💡 一句话要点

**提出Depth Anything 3模型，从任意视图预测空间一致几何，无需已知相机位姿。**

**关键词**: `多视图几何` `深度估计` `Transformer骨干` `师生训练` `相机位姿估计` `视觉渲染`

## 📋 核心要点

1. 核心问题：从任意数量视觉输入中恢复空间一致几何，无需已知相机位姿。
2. 方法要点：使用单一Transformer骨干和深度射线预测目标，避免复杂多任务学习。
3. 实验或效果：在视觉几何基准上超越SOTA，相机位姿精度平均提升44.3%。

## 📄 摘要（原文）

> We present Depth Anything 3 (DA3), a model that predicts spatially consistent geometry from an arbitrary number of visual inputs, with or without known camera poses. In pursuit of minimal modeling, DA3 yields two key insights: a single plain transformer (e.g., vanilla DINO encoder) is sufficient as a backbone without architectural specialization, and a singular depth-ray prediction target obviates the need for complex multi-task learning. Through our teacher-student training paradigm, the model achieves a level of detail and generalization on par with Depth Anything 2 (DA2). We establish a new visual geometry benchmark covering camera pose estimation, any-view geometry and visual rendering. On this benchmark, DA3 sets a new state-of-the-art across all tasks, surpassing prior SOTA VGGT by an average of 44.3% in camera pose accuracy and 25.1% in geometric accuracy. Moreover, it outperforms DA2 in monocular depth estimation. All models are trained exclusively on public academic datasets.

