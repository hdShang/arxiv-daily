---
layout: default
title: Data-Driven Dynamic Parameter Learning of manipulator robots
---

# Data-Driven Dynamic Parameter Learning of manipulator robots

**arXiv**: [2512.08767v1](https://arxiv.org/abs/2512.08767) | [PDF](https://arxiv.org/pdf/2512.08767.pdf)

**作者**: Mohammed Elseiagy, Tsige Tadesse Alemayoh, Ranulfo Bezerra, Shotaro Kojima, Kazunori Ohno

---

## 💡 一句话要点

**提出基于Transformer的动态参数估计方法，结合自动化数据生成，以提升机器人仿真到现实的迁移能力。**

**关键词**: `动态参数估计` `Transformer模型` `仿真到现实迁移` `自动化数据生成` `机器人控制`

## 📋 核心要点

1. 核心问题：机器人动态参数估计对模型控制至关重要，但传统方法难以处理复杂结构，数据驱动方法面临长依赖捕获挑战。
2. 方法要点：采用Transformer模型，利用注意力机制捕捉时空依赖，并通过自动化管道生成多样化机器人模型和轨迹数据。
3. 实验或效果：最佳配置在验证集上R2达0.8633，质量和惯性估计准确，摩擦和质心估计更具挑战性，证明方法可扩展且准确。

## 📄 摘要（原文）

> Bridging the sim-to-real gap remains a fundamental challenge in robotics, as accurate dynamic parameter estimation is essential for reliable model-based control, realistic simulation, and safe deployment of manipulators. Traditional analytical approaches often fall short when faced with complex robot structures and interactions. Data-driven methods offer a promising alternative, yet conventional neural networks such as recurrent models struggle to capture long-range dependencies critical for accurate estimation. In this study, we propose a Transformer-based approach for dynamic parameter estimation, supported by an automated pipeline that generates diverse robot models and enriched trajectory data using Jacobian-derived features. The dataset consists of 8,192 robots with varied inertial and frictional properties. Leveraging attention mechanisms, our model effectively captures both temporal and spatial dependencies. Experimental results highlight the influence of sequence length, sampling rate, and architecture, with the best configuration (sequence length 64, 64 Hz, four layers, 32 heads) achieving a validation R2 of 0.8633. Mass and inertia are estimated with near-perfect accuracy, Coulomb friction with moderate-to-high accuracy, while viscous friction and distal link center-of-mass remain more challenging. These results demonstrate that combining Transformers with automated dataset generation and kinematic enrichment enables scalable, accurate dynamic parameter estimation, contributing to improved sim-to-real transfer in robotic systems

