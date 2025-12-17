---
layout: default
title: What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models
---

# What Is The Best 3D Scene Representation for Robotics? From Geometric to Foundation Models

**arXiv**: [2512.03422v1](https://arxiv.org/abs/2512.03422) | [PDF](https://arxiv.org/pdf/2512.03422.pdf)

**作者**: Tianchen Deng, Yue Pan, Shenghai Yuan, Dong Li, Chen Wang, Mingrui Li, Long Chen, Lihua Xie, Danwei Wang, Jingchuan Wang, Javier Civera, Hesheng Wang, Weidong Chen

---

## 💡 一句话要点

**综述机器人学中3D场景表示方法，从几何到基础模型，探讨最佳表示方案**

**关键词**: `3D场景表示` `机器人学` `神经表示` `基础模型` `SLAM` `导航`

## 📋 核心要点

1. 核心问题：探讨机器人学中最佳3D场景表示方法，涵盖传统与神经表示。
2. 方法要点：分类机器人核心模块，比较不同表示在感知、导航等任务中的优缺点。
3. 实验或效果：提出3D基础模型作为未来统一解决方案，并讨论剩余挑战。

## 📄 摘要（原文）

> In this paper, we provide a comprehensive overview of existing scene representation methods for robotics, covering traditional representations such as point clouds, voxels, signed distance functions (SDF), and scene graphs, as well as more recent neural representations like Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and the emerging Foundation Models. While current SLAM and localization systems predominantly rely on sparse representations like point clouds and voxels, dense scene representations are expected to play a critical role in downstream tasks such as navigation and obstacle avoidance. Moreover, neural representations such as NeRF, 3DGS, and foundation models are well-suited for integrating high-level semantic features and language-based priors, enabling more comprehensive 3D scene understanding and embodied intelligence. In this paper, we categorized the core modules of robotics into five parts (Perception, Mapping, Localization, Navigation, Manipulation). We start by presenting the standard formulation of different scene representation methods and comparing the advantages and disadvantages of scene representation across different modules. This survey is centered around the question: What is the best 3D scene representation for robotics? We then discuss the future development trends of 3D scene representations, with a particular focus on how the 3D Foundation Model could replace current methods as the unified solution for future robotic applications. The remaining challenges in fully realizing this model are also explored. We aim to offer a valuable resource for both newcomers and experienced researchers to explore the future of 3D scene representations and their application in robotics. We have published an open-source project on GitHub and will continue to add new works and technologies to this project.

