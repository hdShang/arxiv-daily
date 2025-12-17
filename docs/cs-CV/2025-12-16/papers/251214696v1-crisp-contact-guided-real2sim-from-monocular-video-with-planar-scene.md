---
layout: default
title: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives
---

# CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives

**arXiv**: [2512.14696v1](https://arxiv.org/abs/2512.14696) | [PDF](https://arxiv.org/pdf/2512.14696.pdf)

**作者**: Zihan Wang, Jiashun Wang, Jeff Tan, Yiwen Zhao, Jessica Hodgins, Shubham Tulsiani, Deva Ramanan

**分类**: cs.CV, cs.GR, cs.RO

**发布日期**: 2025-12-16

**备注**: Project page: https://crisp-real2sim.github.io/CRISP-Real2Sim/

---

## 💡 一句话要点

**提出CRISP方法，通过平面基元拟合和接触引导，从单目视频重建可仿真的运动与场景几何，解决物理交互失败问题。**

🎯 **匹配领域**: **人形机器人** **动作生成** **强化学习**

**关键词**: `单目视频重建` `人-场景交互` `平面基元拟合` `接触建模` `强化学习仿真` `物理合理性` `真实到仿真` `机器人学应用`

## 📋 核心要点

1. 现有方法依赖数据先验或无物理优化，导致几何噪声和交互失败，难以实现仿真就绪的重建。
2. CRISP通过平面基元拟合点云和接触建模，恢复干净几何，并利用强化学习确保物理合理性。
3. 实验显示，运动跟踪失败率从55.2%降至6.9%，RL仿真吞吐量提升43%，并在多种视频上验证有效性。

## 📝 摘要（中文）

我们介绍了CRISP方法，它能够从单目视频中恢复可仿真的人类运动和场景几何。先前关于人-场景联合重建的工作依赖于数据驱动的先验和无物理约束的联合优化，或者恢复带有伪影的噪声几何，导致场景交互的运动跟踪策略失败。相比之下，我们的关键见解是通过对场景点云重建进行平面基元拟合，利用深度、法线和光流的简单聚类流程，恢复凸面、干净且仿真就绪的几何。为了重建在交互过程中可能被遮挡的场景几何，我们利用人-场景接触建模（例如，使用人体姿态重建被遮挡的椅子座位）。最后，我们通过强化学习驱动人形控制器，确保人类和场景重建在物理上是合理的。我们的方法在以人为本的视频基准（EMDB、PROX）上将运动跟踪失败率从55.2%降低到6.9%，同时提供43%更快的RL仿真吞吐量。我们进一步在野外视频上验证了它，包括随意拍摄的视频、互联网视频，甚至Sora生成的视频。这展示了CRISP大规模生成物理有效的人类运动和交互环境的能力，极大地推进了机器人学和AR/VR的真实到仿真应用。

## 🔬 方法详解

CRISP的整体框架包括从单目视频重建点云，然后通过基于深度、法线和光流的聚类流程拟合平面基元，以生成凸面、干净的场景几何。关键创新在于结合人-场景接触建模来重建遮挡区域（如利用人体姿态推断椅子座位），并通过强化学习驱动人形控制器来优化物理合理性。与现有方法的主要区别在于：它不依赖复杂的数据驱动先验，而是采用简单聚类和物理约束，直接生成仿真就绪的几何，避免了噪声和伪影导致的交互失败。

## 📊 实验亮点

在EMDB和PROX基准上，运动跟踪失败率从55.2%显著降低至6.9%，RL仿真吞吐量提升43%，并在随意拍摄、互联网和Sora生成视频中验证了方法的鲁棒性和可扩展性。

## 🎯 应用场景

该研究在机器人学和AR/VR领域有广泛应用，例如用于训练机器人交互策略、创建虚拟环境的物理模拟内容，以及增强现实中的真实场景重建，能够大规模生成物理有效的运动和交互环境。

## 📄 摘要（原文）

> We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

