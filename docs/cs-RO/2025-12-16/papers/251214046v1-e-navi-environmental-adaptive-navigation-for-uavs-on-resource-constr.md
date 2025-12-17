---
layout: default
title: E-Navi: Environmental Adaptive Navigation for UAVs on Resource Constrained Platforms
---

# E-Navi: Environmental Adaptive Navigation for UAVs on Resource Constrained Platforms

**arXiv**: [2512.14046v1](https://arxiv.org/abs/2512.14046) | [PDF](https://arxiv.org/pdf/2512.14046.pdf)

**作者**: Boyang Li, Zhongpeng Jin, Shuai Zhao, Jiahui Liao, Tian Liu, Han Liu, Yuanhai Zhang, Kai Huang

**分类**: cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出E-Navi环境自适应导航系统，为资源受限无人机平台解决动态环境适应性问题**

**关键词**: `无人机导航` `环境自适应` `资源受限平台` `动态任务调度` `感知-规划流程` `硬件在环实验` `计算效率优化` `自主飞行系统`

## 📋 核心要点

1. 现有无人机导航系统采用固定配置，无法根据环境动态调整计算资源，导致飞行策略僵化和性能下降。
2. E-Navi通过量化环境复杂度，动态调整地图分辨率和执行频率，实现感知-规划流程的自适应优化。
3. 实验显示系统显著降低任务负载和飞行时间，提升速度控制稳定性，支持跨硬件平台部署。

## 📝 摘要（中文）

适应变化环境的能力对无人机自主导航系统至关重要。然而，现有导航系统采用固定的执行配置，未基于可用计算资源考虑环境动态性，例如采用高执行频率和任务负载。这种静态方法导致飞行策略僵化和计算过度，最终降低飞行性能甚至导致无人机故障。尽管自适应系统具有必要性，但由于量化环境复杂性和建模环境与系统配置关系的困难，动态调整工作负载仍然具有挑战性。为适应动态环境，本文提出E-Navi，一种面向无人机的环境自适应导航系统，基于可用计算资源动态调整CPU上的任务执行以响应环境变化。具体而言，通过定量环境复杂度评估驱动，重新设计了无人机导航系统的感知-规划流程，实现地图分辨率和执行频率的动态自适应。此外，E-Navi支持在不同计算能力水平的硬件平台上灵活部署。广泛的硬件在环和真实世界实验表明，所提系统在各种硬件平台上显著优于基线方法，实现高达53.9%的导航任务负载减少、高达63.8%的飞行时间节省，并提供更稳定的速度控制。

## 🔬 方法详解

E-Navi的整体框架是一个环境自适应的无人机导航系统，核心基于感知-规划流程的动态重构。关键技术创新点包括：1) 开发了环境复杂度量化方法，能够实时评估飞行环境的动态性和复杂性；2) 建立了环境复杂度与系统配置（如地图分辨率、执行频率）的映射模型，实现任务负载的动态调整；3) 设计了资源感知的调度机制，根据可用计算资源优化CPU任务执行。与现有方法的主要区别在于：传统系统采用静态配置，而E-Navi通过环境驱动实现动态自适应，避免了过度计算和资源浪费，同时支持跨平台部署，提升了系统的灵活性和鲁棒性。

## 📊 实验亮点

硬件在环和真实世界实验表明，E-Navi相比基线方法实现高达53.9%的导航任务负载减少和高达63.8%的飞行时间节省，同时提供更稳定的速度控制，验证了系统在多种硬件平台上的优越性能。

## 🎯 应用场景

该研究适用于无人机在资源受限平台上的自主导航任务，如农业监测、灾害救援、物流配送和基础设施巡检等领域。通过动态适应环境变化，E-Navi能提高飞行效率和安全性，降低计算开销，促进无人机在复杂或动态环境中的广泛应用。

## 📄 摘要（原文）

> The ability to adapt to changing environments is crucial for the autonomous navigation systems of Unmanned Aerial Vehicles (UAVs). However, existing navigation systems adopt fixed execution configurations without considering environmental dynamics based on available computing resources, e.g., with a high execution frequency and task workload. This static approach causes rigid flight strategies and excessive computations, ultimately degrading flight performance or even leading to failures in UAVs. Despite the necessity for an adaptive system, dynamically adjusting workloads remains challenging, due to difficulties in quantifying environmental complexity and modeling the relationship between environment and system configuration. Aiming at adapting to dynamic environments, this paper proposes E-Navi, an environmental-adaptive navigation system for UAVs that dynamically adjusts task executions on the CPUs in response to environmental changes based on available computational resources. Specifically, the perception-planning pipeline of UAVs navigation system is redesigned through dynamic adaptation of mapping resolution and execution frequency, driven by the quantitative environmental complexity evaluations. In addition, E-Navi supports flexible deployment across hardware platforms with varying levels of computing capability. Extensive Hardware-In-the-Loop and real-world experiments demonstrate that the proposed system significantly outperforms the baseline method across various hardware platforms, achieving up to 53.9% navigation task workload reduction, up to 63.8% flight time savings, and delivering more stable velocity control.

