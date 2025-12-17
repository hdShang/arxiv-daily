---
layout: default
title: NVSim: Novel View Synthesis Simulator for Large Scale Indoor Navigation
---

# NVSim: Novel View Synthesis Simulator for Large Scale Indoor Navigation

**arXiv**: [2510.24335v1](https://arxiv.org/abs/2510.24335) | [PDF](https://arxiv.org/pdf/2510.24335.pdf)

**作者**: Mingyu Jeong, Eunsung Kim, Sehun Park, Andrew Jaeyong Choi

---

## 💡 一句话要点

**提出NVSim框架，从图像序列自动构建大规模室内导航模拟器，解决稀疏观测地面视觉伪影问题。**

**关键词**: `新视角合成` `室内导航模拟` `高斯泼溅` `可通行性检查` `拓扑图构建` `机器人视觉`

## 📋 核心要点

1. 核心问题：传统3D扫描成本高、扩展性差，稀疏观测地面易产生视觉伪影。
2. 方法要点：采用Floor-Aware高斯泼溅确保地面清洁可导航，并开发无网格可通行性检查算法。
3. 实验或效果：在真实数据上生成有效的大规模导航图，视频演示可用。

## 📄 摘要（原文）

> We present NVSim, a framework that automatically constructs large-scale,
> navigable indoor simulators from only common image sequences, overcoming the
> cost and scalability limitations of traditional 3D scanning. Our approach
> adapts 3D Gaussian Splatting to address visual artifacts on sparsely observed
> floors a common issue in robotic traversal data. We introduce Floor-Aware
> Gaussian Splatting to ensure a clean, navigable ground plane, and a novel
> mesh-free traversability checking algorithm that constructs a topological graph
> by directly analyzing rendered views. We demonstrate our system's ability to
> generate valid, large-scale navigation graphs from real-world data. A video
> demonstration is avilable at https://youtu.be/tTiIQt6nXC8

