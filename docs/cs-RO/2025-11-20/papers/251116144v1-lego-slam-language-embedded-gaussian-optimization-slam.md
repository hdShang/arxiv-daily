---
layout: default
title: LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM
---

# LEGO-SLAM: Language-Embedded Gaussian Optimization SLAM

**arXiv**: [2511.16144v1](https://arxiv.org/abs/2511.16144) | [PDF](https://arxiv.org/pdf/2511.16144.pdf)

**作者**: Sibaek Lee, Seongbo Ha, Kyeongsu Kang, Joonyeol Choi, Seungjun Tak, Hyeonwoo Yu

---

## 💡 一句话要点

**提出LEGO-SLAM以在3D高斯溅射SLAM中实现实时开放词汇语义映射**

**关键词**: `3D高斯溅射` `同时定位与建图` `语言嵌入` `实时映射` `开放词汇语义` `特征蒸馏`

## 📋 核心要点

1. 核心问题：3DGS SLAM缺乏开放词汇语义理解，且高维语言特征存储和渲染开销大。
2. 方法要点：使用场景自适应编码器将语言嵌入压缩至16维，减少内存并加速渲染。
3. 实验或效果：在15 FPS下实现竞争性映射质量和跟踪精度，高斯数量减少超60%。

## 📄 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have enabled Simultaneous Localization and Mapping (SLAM) systems to build photorealistic maps. However, these maps lack the open-vocabulary semantic understanding required for advanced robotic interaction. Integrating language features into SLAM remains a significant challenge, as storing high-dimensional features demands excessive memory and rendering overhead, while existing methods with static models lack adaptability for novel environments. To address these limitations, we propose LEGO-SLAM (Language-Embedded Gaussian Optimization SLAM), the first framework to achieve real-time, open-vocabulary mapping within a 3DGS-based SLAM system. At the core of our method is a scene-adaptive encoder-decoder that distills high-dimensional language embeddings into a compact 16-dimensional feature space. This design reduces the memory per Gaussian and accelerates rendering, enabling real-time performance. Unlike static approaches, our encoder adapts online to unseen scenes. These compact features also enable a language-guided pruning strategy that identifies semantic redundancy, reducing the map's Gaussian count by over 60\% while maintaining rendering quality. Furthermore, we introduce a language-based loop detection approach that reuses these mapping features, eliminating the need for a separate detection model. Extensive experiments demonstrate that LEGO-SLAM achieves competitive mapping quality and tracking accuracy, all while providing open-vocabulary capabilities at 15 FPS.

