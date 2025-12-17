---
layout: default
title: GaussGym: An open-source real-to-sim framework for learning locomotion from pixels
---

# GaussGym: An open-source real-to-sim framework for learning locomotion from pixels

**arXiv**: [2510.15352v1](https://arxiv.org/abs/2510.15352) | [PDF](https://arxiv.org/pdf/2510.15352.pdf)

**作者**: Alejandro Escontrela, Justin Kerr, Arthur Allshire, Jonas Frey, Rocky Duan, Carmelo Sferrazza, Pieter Abbeel

---

## 💡 一句话要点

**提出GaussGym框架，集成3D高斯渲染于物理模拟器，实现高速高保真机器人学习。**

**关键词**: `3D高斯渲染` `机器人模拟` `像素学习` `物理模拟器` `视觉语义` `开源框架`

## 📋 核心要点

1. 核心问题：机器人模拟需平衡高视觉保真度与计算速度，以支持基于像素的学习。
2. 方法要点：使用3D高斯渲染作为插件，结合向量化物理模拟器如IsaacGym。
3. 实验或效果：在消费级GPU上超10万步/秒，提升导航与决策，支持大规模场景生成。

## 📄 摘要（原文）

> We present a novel approach for photorealistic robot simulation that
> integrates 3D Gaussian Splatting as a drop-in renderer within vectorized
> physics simulators such as IsaacGym. This enables unprecedented speed --
> exceeding 100,000 steps per second on consumer GPUs -- while maintaining high
> visual fidelity, which we showcase across diverse tasks. We additionally
> demonstrate its applicability in a sim-to-real robotics setting. Beyond
> depth-based sensing, our results highlight how rich visual semantics improve
> navigation and decision-making, such as avoiding undesirable regions. We
> further showcase the ease of incorporating thousands of environments from
> iPhone scans, large-scale scene datasets (e.g., GrandTour, ARKit), and outputs
> from generative video models like Veo, enabling rapid creation of realistic
> training worlds. This work bridges high-throughput simulation and high-fidelity
> perception, advancing scalable and generalizable robot learning. All code and
> data will be open-sourced for the community to build upon. Videos, code, and
> data available at https://escontrela.me/gauss_gym/.

