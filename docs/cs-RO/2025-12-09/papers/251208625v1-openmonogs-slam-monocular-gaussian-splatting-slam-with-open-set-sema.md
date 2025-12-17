---
layout: default
title: OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics
---

# OpenMonoGS-SLAM: Monocular Gaussian Splatting SLAM with Open-set Semantics

**arXiv**: [2512.08625v1](https://arxiv.org/abs/2512.08625) | [PDF](https://arxiv.org/pdf/2512.08625.pdf)

**作者**: Jisang Yoo, Gyeongjin Kang, Hyun-kyu Ko, Hyeonwoo Yu, Eunbyung Park

---

## 💡 一句话要点

**提出OpenMonoGS-SLAM，结合3D高斯溅射与开放集语义，实现单目SLAM在开放世界环境中的智能感知。**

**关键词**: `单目SLAM` `3D高斯溅射` `开放集语义` `视觉基础模型` `自监督学习` `语义特征映射`

## 📋 核心要点

1. 核心问题：现有SLAM方法依赖深度传感器或封闭集语义模型，在开放世界环境中可扩展性和适应性受限。
2. 方法要点：利用视觉基础模型（如MASt3R、SAM、CLIP）进行自监督学习，无需深度输入或3D语义真值，并设计内存机制管理高维语义特征。
3. 实验或效果：在封闭集和开放集分割任务中性能达到或超越基线，不依赖额外传感器或语义标注。

## 📄 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) is a foundational component in robotics, AR/VR, and autonomous systems. With the rising focus on spatial AI in recent years, combining SLAM with semantic understanding has become increasingly important for enabling intelligent perception and interaction. Recent efforts have explored this integration, but they often rely on depth sensors or closed-set semantic models, limiting their scalability and adaptability in open-world environments. In this work, we present OpenMonoGS-SLAM, the first monocular SLAM framework that unifies 3D Gaussian Splatting (3DGS) with open-set semantic understanding. To achieve our goal, we leverage recent advances in Visual Foundation Models (VFMs), including MASt3R for visual geometry and SAM and CLIP for open-vocabulary semantics. These models provide robust generalization across diverse tasks, enabling accurate monocular camera tracking and mapping, as well as a rich understanding of semantics in open-world environments. Our method operates without any depth input or 3D semantic ground truth, relying solely on self-supervised learning objectives. Furthermore, we propose a memory mechanism specifically designed to manage high-dimensional semantic features, which effectively constructs Gaussian semantic feature maps, leading to strong overall performance. Experimental results demonstrate that our approach achieves performance comparable to or surpassing existing baselines in both closed-set and open-set segmentation tasks, all without relying on supplementary sensors such as depth maps or semantic annotations.

