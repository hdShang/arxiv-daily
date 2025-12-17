---
layout: default
title: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
---

# Efficiently Reconstructing Dynamic Scenes One D4RT at a Time

**arXiv**: [2512.08924v1](https://arxiv.org/abs/2512.08924) | [PDF](https://arxiv.org/pdf/2512.08924.pdf)

**作者**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi SM Sajjadi

---

## 💡 一句话要点

**提出D4RT前馈模型，通过统一Transformer架构高效重建动态场景的4D几何与运动。**

**关键词**: `动态场景重建` `4D重建` `Transformer架构` `深度估计` `相机参数估计` `时空对应`

## 📋 核心要点

1. 核心问题：从视频中高效重建动态场景的复杂几何和运动仍具挑战。
2. 方法要点：采用统一Transformer架构，通过新颖查询机制联合推断深度、时空对应和相机参数。
3. 实验或效果：在多种4D重建任务中超越先前方法，实现轻量级、可扩展的高效训练与推理。

## 📄 摘要（原文）

> Understanding and reconstructing the complex geometry and motion of dynamic scenes from video remains a formidable challenge in computer vision. This paper introduces D4RT, a simple yet powerful feedforward model designed to efficiently solve this task. D4RT utilizes a unified transformer architecture to jointly infer depth, spatio-temporal correspondence, and full camera parameters from a single video. Its core innovation is a novel querying mechanism that sidesteps the heavy computation of dense, per-frame decoding and the complexity of managing multiple, task-specific decoders. Our decoding interface allows the model to independently and flexibly probe the 3D position of any point in space and time. The result is a lightweight and highly scalable method that enables remarkably efficient training and inference. We demonstrate that our approach sets a new state of the art, outperforming previous methods across a wide spectrum of 4D reconstruction tasks. We refer to the project webpage for animated results: https://d4rt-paper.github.io/.

