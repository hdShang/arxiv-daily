---
layout: default
title: UMIGen: A Unified Framework for Egocentric Point Cloud Generation and Cross-Embodiment Robotic Imitation Learning
---

# UMIGen: A Unified Framework for Egocentric Point Cloud Generation and Cross-Embodiment Robotic Imitation Learning

**arXiv**: [2511.09302v1](https://arxiv.org/abs/2511.09302) | [PDF](https://arxiv.org/pdf/2511.09302.pdf)

**作者**: Yan Huang, Shoujie Li, Xingting Li, Wenbo Ding

---

## 💡 一句话要点

**提出UMIGen框架以解决机器人模仿学习中数据收集困难与跨具身泛化问题**

**关键词**: `点云生成` `机器人模仿学习` `跨具身泛化` `数据收集` `可见性优化`

## 📋 核心要点

1. 核心问题：机器人学习依赖大规模高质量演示数据，但收集成本高且空间泛化能力有限
2. 方法要点：结合手持点云采集设备和可见性优化机制，生成对齐真实观察的点云数据
3. 实验或效果：在仿真和真实环境中验证了跨具身泛化能力并加速了数据收集

## 📄 摘要（原文）

> Data-driven robotic learning faces an obvious dilemma: robust policies demand large-scale, high-quality demonstration data, yet collecting such data remains a major challenge owing to high operational costs, dependence on specialized hardware, and the limited spatial generalization capability of current methods. The Universal Manipulation Interface (UMI) relaxes the strict hardware requirements for data collection, but it is restricted to capturing only RGB images of a scene and omits the 3D geometric information on which many tasks rely. Inspired by DemoGen, we propose UMIGen, a unified framework that consists of two key components: (1) Cloud-UMI, a handheld data collection device that requires no visual SLAM and simultaneously records point cloud observation-action pairs; and (2) a visibility-aware optimization mechanism that extends the DemoGen pipeline to egocentric 3D observations by generating only points within the camera's field of view. These two components enable efficient data generation that aligns with real egocentric observations and can be directly transferred across different robot embodiments without any post-processing. Experiments in both simulated and real-world settings demonstrate that UMIGen supports strong cross-embodiment generalization and accelerates data collection in diverse manipulation tasks.

