---
layout: default
title: TabletopGen: Instance-Level Interactive 3D Tabletop Scene Generation from Text or Single Image
---

# TabletopGen: Instance-Level Interactive 3D Tabletop Scene Generation from Text or Single Image

**arXiv**: [2512.01204v1](https://arxiv.org/abs/2512.01204) | [PDF](https://arxiv.org/pdf/2512.01204.pdf)

**作者**: Ziqian Wang, Yonghao He, Licheng Yang, Wei Zou, Hongxuan Ma, Liu Liu, Wei Sui, Yuxin Guo, Hu Su

---

## 💡 一句话要点

**提出TabletopGen框架，从文本或单图像生成实例级交互式3D桌面场景**

**关键词**: `3D场景生成` `实例级重建` `桌面场景` `交互式模拟` `位姿估计`

## 📋 核心要点

1. 核心问题：现有方法难以生成高密度布局和复杂空间关系的桌面场景
2. 方法要点：基于参考图像进行实例分割与补全，通过解耦的位姿和尺度对齐实现3D重建
3. 实验或效果：在视觉保真度、布局准确性和物理合理性上超越现有方法，支持多样风格

## 📄 摘要（原文）

> Generating high-fidelity, physically interactive 3D simulated tabletop scenes is essential for embodied AI--especially for robotic manipulation policy learning and data synthesis. However, current text- or image-driven 3D scene generation methods mainly focus on large-scale scenes, struggling to capture the high-density layouts and complex spatial relations that characterize tabletop scenes. To address these challenges, we propose TabletopGen, a training-free, fully automatic framework that generates diverse, instance-level interactive 3D tabletop scenes. TabletopGen accepts a reference image as input, which can be synthesized by a text-to-image model to enhance scene diversity. We then perform instance segmentation and completion on the reference to obtain per-instance images. Each instance is reconstructed into a 3D model followed by canonical coordinate alignment. The aligned 3D models then undergo pose and scale estimation before being assembled into a collision-free, simulation-ready tabletop scene. A key component of our framework is a novel pose and scale alignment approach that decouples the complex spatial reasoning into two stages: a Differentiable Rotation Optimizer for precise rotation recovery and a Top-view Spatial Alignment mechanism for robust translation and scale estimation, enabling accurate 3D reconstruction from 2D reference. Extensive experiments and user studies show that TabletopGen achieves state-of-the-art performance, markedly surpassing existing methods in visual fidelity, layout accuracy, and physical plausibility, capable of generating realistic tabletop scenes with rich stylistic and spatial diversity. Our code will be publicly available.

