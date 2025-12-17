---
layout: default
title: Joint 3D Geometry Reconstruction and Motion Generation for 4D Synthesis from a Single Image
---

# Joint 3D Geometry Reconstruction and Motion Generation for 4D Synthesis from a Single Image

**arXiv**: [2512.05044v1](https://arxiv.org/abs/2512.05044) | [PDF](https://arxiv.org/pdf/2512.05044.pdf)

**作者**: Yanran Zhang, Ziyi Wang, Wenzhao Zheng, Zheng Zhu, Jie Zhou, Jiwen Lu

---

## 💡 一句话要点

**提出MoRe4D框架，通过联合几何重建与运动生成从单图像合成高质量4D场景**

**关键词**: `4D场景合成` `单图像重建` `运动生成` `扩散模型` `点轨迹生成` `多视角渲染`

## 📋 核心要点

1. 核心问题：现有方法解耦几何与运动，导致时空不一致和泛化差，单图像生成动态4D场景困难
2. 方法要点：基于TrajScene-60K数据集，使用4D-STraG扩散模型联合生成几何一致的运动轨迹，并设计深度引导归一化和运动感知模块
3. 实验或效果：MoRe4D从单图像生成多视角一致、动态细节丰富的4D场景，实验验证其高质量合成能力

## 📄 摘要（原文）

> Generating interactive and dynamic 4D scenes from a single static image remains a core challenge. Most existing generate-then-reconstruct and reconstruct-then-generate methods decouple geometry from motion, causing spatiotemporal inconsistencies and poor generalization. To address these, we extend the reconstruct-then-generate framework to jointly perform Motion generation and geometric Reconstruction for 4D Synthesis (MoRe4D). We first introduce TrajScene-60K, a large-scale dataset of 60,000 video samples with dense point trajectories, addressing the scarcity of high-quality 4D scene data. Based on this, we propose a diffusion-based 4D Scene Trajectory Generator (4D-STraG) to jointly generate geometrically consistent and motion-plausible 4D point trajectories. To leverage single-view priors, we design a depth-guided motion normalization strategy and a motion-aware module for effective geometry and dynamics integration. We then propose a 4D View Synthesis Module (4D-ViSM) to render videos with arbitrary camera trajectories from 4D point track representations. Experiments show that MoRe4D generates high-quality 4D scenes with multi-view consistency and rich dynamic details from a single image. Code: https://github.com/Zhangyr2022/MoRe4D.

