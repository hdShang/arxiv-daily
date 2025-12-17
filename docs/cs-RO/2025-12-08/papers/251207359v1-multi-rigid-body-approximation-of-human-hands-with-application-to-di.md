---
layout: default
title: Multi-Rigid-Body Approximation of Human Hands with Application to Digital Twin
---

# Multi-Rigid-Body Approximation of Human Hands with Application to Digital Twin

**arXiv**: [2512.07359v1](https://arxiv.org/abs/2512.07359) | [PDF](https://arxiv.org/pdf/2512.07359.pdf)

**作者**: Bin Zhao, Yiwen Lu, Haohua Zhu, Xiao Li, Sheng Yi

---

## 💡 一句话要点

**提出多刚体手部近似方法，结合MANO与URDF，实现数字孪生中的实时物理模拟。**

**关键词**: `数字孪生` `手部模拟` `多刚体模型` `MANO模型` `URDF转换` `旋转映射`

## 📋 核心要点

1. 核心问题：在数字孪生中平衡手部解剖保真度与计算效率，需处理MANO无约束旋转到刚体约束关节的映射。
2. 方法要点：从运动捕捉构建个性化MANO模型，转换为URDF表示，使用闭式解和BCH校正迭代法处理单/双自由度关节旋转。
3. 实验或效果：通过强化学习控制手部重放演示，验证了亚厘米级重建误差和多样化抓取任务的成功执行。

## 📄 摘要（原文）

> Human hand simulation plays a critical role in digital twin applications, requiring models that balance anatomical fidelity with computational efficiency. We present a complete pipeline for constructing multi-rigid-body approximations of human hands that preserve realistic appearance while enabling real-time physics simulation. Starting from optical motion capture of a specific human hand, we construct a personalized MANO (Multi-Abstracted hand model with Neural Operations) model and convert it to a URDF (Unified Robot Description Format) representation with anatomically consistent joint axes. The key technical challenge is projecting MANO's unconstrained SO(3) joint rotations onto the kinematically constrained joints of the rigid-body model. We derive closed-form solutions for single degree-of-freedom joints and introduce a Baker-Campbell-Hausdorff (BCH)-corrected iterative method for two degree-of-freedom joints that properly handles the non-commutativity of rotations. We validate our approach through digital twin experiments where reinforcement learning policies control the multi-rigid-body hand to replay captured human demonstrations. Quantitative evaluation shows sub-centimeter reconstruction error and successful grasp execution across diverse manipulation tasks.

