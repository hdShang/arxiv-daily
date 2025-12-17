---
layout: default
title: SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge
---

# SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge

**arXiv**: [2512.01629v1](https://arxiv.org/abs/2512.01629) | [PDF](https://arxiv.org/pdf/2512.01629.pdf)

**作者**: Yumeng He, Ying Jiang, Jiayin Lu, Yin Yang, Chenfanfu Jiang

---

## 💡 一句话要点

**提出SPARK框架，从单张RGB图像重建物理一致的关节化物体，用于仿真和机器人应用。**

**关键词**: `关节化重建` `单图像重建` `仿真就绪资产` `可微渲染` `视觉语言模型` `机器人操作`

## 📋 核心要点

1. 核心问题：关节化3D物体重建需专家建模，劳动密集，难以生成仿真就绪资产。
2. 方法要点：利用VLM提取URDF参数，结合扩散变换器合成部件形状，通过可微运动学优化关节参数。
3. 实验或效果：实验显示SPARK能跨类别生成高质量仿真就绪资产，支持机器人操作等下游应用。

## 📄 摘要（原文）

> Articulated 3D objects are critical for embodied AI, robotics, and interactive scene understanding, yet creating simulation-ready assets remains labor-intensive and requires expert modeling of part hierarchies and motion structures. We introduce SPARK, a framework for reconstructing physically consistent, kinematic part-level articulated objects from a single RGB image. Given an input image, we first leverage VLMs to extract coarse URDF parameters and generate part-level reference images. We then integrate the part-image guidance and the inferred structure graph into a generative diffusion transformer to synthesize consistent part and complete shapes of articulated objects. To further refine the URDF parameters, we incorporate differentiable forward kinematics and differentiable rendering to optimize joint types, axes, and origins under VLM-generated open-state supervision. Extensive experiments show that SPARK produces high-quality, simulation-ready articulated assets across diverse categories, enabling downstream applications such as robotic manipulation and interaction modeling.

