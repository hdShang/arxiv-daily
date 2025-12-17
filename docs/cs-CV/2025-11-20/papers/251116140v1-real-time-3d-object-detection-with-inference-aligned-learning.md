---
layout: default
title: Real-Time 3D Object Detection with Inference-Aligned Learning
---

# Real-Time 3D Object Detection with Inference-Aligned Learning

**arXiv**: [2511.16140v1](https://arxiv.org/abs/2511.16140) | [PDF](https://arxiv.org/pdf/2511.16140.pdf)

**作者**: Chenyu Zhao, Xianwei Zheng, Zimin Xia, Linwei Yue, Nan Xue

---

## 💡 一句话要点

**提出SR3D框架以解决室内点云实时3D检测中的训练-推理差距问题**

**关键词**: `3D物体检测` `点云处理` `训练-推理对齐` `最优传输` `自蒸馏` `实时系统`

## 📋 核心要点

1. 核心问题：训练与推理间存在空间可靠性和排序感知差距，影响模型性能。
2. 方法要点：采用空间优先最优传输分配和排序感知自适应自蒸馏方案。
3. 实验或效果：在ScanNet V2和SUN RGB-D上精度显著提升，保持实时速度。

## 📄 摘要（原文）

> Real-time 3D object detection from point clouds is essential for dynamic scene understanding in applications such as augmented reality, robotics and navigation. We introduce a novel Spatial-prioritized and Rank-aware 3D object detection (SR3D) framework for indoor point clouds, to bridge the gap between how detectors are trained and how they are evaluated. This gap stems from the lack of spatial reliability and ranking awareness during training, which conflicts with the ranking-based prediction selection used as inference. Such a training-inference gap hampers the model's ability to learn representations aligned with inference-time behavior. To address the limitation, SR3D consists of two components tailored to the spatial nature of point clouds during training: a novel spatial-prioritized optimal transport assignment that dynamically emphasizes well-located and spatially reliable samples, and a rank-aware adaptive self-distillation scheme that adaptively injects ranking perception via a self-distillation paradigm. Extensive experiments on ScanNet V2 and SUN RGB-D show that SR3D effectively bridges the training-inference gap and significantly outperforms prior methods in accuracy while maintaining real-time speed.

