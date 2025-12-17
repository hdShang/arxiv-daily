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

**E-Navi：面向资源受限平台，环境自适应无人机导航系统**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `无人机导航` `环境自适应` `资源受限平台` `动态规划` `环境复杂度评估`

## 📋 核心要点

1. 现有无人机导航系统采用固定配置，无法根据环境动态调整，导致资源浪费和性能下降。
2. E-Navi通过量化环境复杂度，动态调整感知和规划流程，实现环境自适应导航。
3. 实验表明，E-Navi在资源受限平台上显著降低了计算负载，节省了飞行时间，并提升了控制稳定性。

## 📝 摘要（中文）

本文提出了一种名为E-Navi的环境自适应无人机导航系统，旨在解决无人机在动态环境中自主导航的问题。现有导航系统通常采用固定的执行配置，忽略了环境变化和计算资源可用性，导致飞行策略僵化和计算资源浪费，甚至导致飞行失败。E-Navi通过量化环境复杂度，动态调整地图分辨率和执行频率，从而重新设计了无人机导航系统的感知-规划流程。此外，E-Navi支持在不同计算能力的硬件平台上灵活部署。硬件在环和真实环境实验表明，与基线方法相比，该系统在各种硬件平台上均表现出显著优势，导航任务工作负载降低高达53.9%，飞行时间节省高达63.8%，并实现了更稳定的速度控制。

## 🔬 方法详解

**问题定义**：无人机在复杂动态环境中导航时，传统方法采用固定的计算资源分配策略，无法根据环境变化进行调整。这导致在简单环境中浪费计算资源，而在复杂环境中计算资源不足，最终影响导航性能甚至导致失败。现有方法的痛点在于缺乏环境感知和自适应调整机制。

**核心思路**：E-Navi的核心思路是根据环境的复杂程度动态调整无人机导航系统的计算资源分配。通过量化环境复杂度，系统能够自适应地调整地图分辨率和执行频率，从而在保证导航性能的前提下，最大限度地减少计算资源的消耗。这种自适应调整使得无人机能够在不同的环境条件下保持高效稳定的导航。

**技术框架**：E-Navi系统主要包含环境复杂度评估模块、自适应感知模块和自适应规划模块。首先，环境复杂度评估模块通过传感器数据分析环境的复杂程度。然后，自适应感知模块根据环境复杂度调整地图的分辨率，降低不必要的计算量。最后，自适应规划模块根据环境复杂度和可用计算资源，动态调整规划算法的执行频率，以保证导航的实时性和准确性。

**关键创新**：E-Navi最重要的创新点在于提出了环境复杂度量化方法，并将其与无人机导航系统的感知和规划流程相结合，实现了环境自适应的计算资源分配。与现有方法相比，E-Navi能够根据环境变化动态调整计算资源，从而在保证导航性能的同时，显著降低计算负载。

**关键设计**：环境复杂度评估模块使用图像处理和特征提取技术，量化环境的纹理、障碍物密度等特征。自适应感知模块采用动态分辨率调整策略，根据环境复杂度调整地图的分辨率。自适应规划模块使用基于模型预测控制（MPC）的规划算法，并根据可用计算资源动态调整MPC的迭代次数和优化范围。

## 📊 实验亮点

实验结果表明，E-Navi在各种硬件平台上均优于基线方法。在导航任务中，E-Navi能够降低高达53.9%的计算工作负载，节省高达63.8%的飞行时间，并提供更稳定的速度控制。这些结果验证了E-Navi在资源受限平台上实现高效自主导航的有效性。

## 🎯 应用场景

E-Navi技术可广泛应用于资源受限平台上的无人机自主导航，例如在农业植保、物流配送、灾害救援等领域。通过自适应调整计算资源，E-Navi能够提高无人机的续航能力和环境适应性，使其在复杂多变的环境中执行任务。未来，该技术有望进一步扩展到其他移动机器人平台，提升其自主性和智能化水平。

## 📄 摘要（原文）

> The ability to adapt to changing environments is crucial for the autonomous navigation systems of Unmanned Aerial Vehicles (UAVs). However, existing navigation systems adopt fixed execution configurations without considering environmental dynamics based on available computing resources, e.g., with a high execution frequency and task workload. This static approach causes rigid flight strategies and excessive computations, ultimately degrading flight performance or even leading to failures in UAVs. Despite the necessity for an adaptive system, dynamically adjusting workloads remains challenging, due to difficulties in quantifying environmental complexity and modeling the relationship between environment and system configuration. Aiming at adapting to dynamic environments, this paper proposes E-Navi, an environmental-adaptive navigation system for UAVs that dynamically adjusts task executions on the CPUs in response to environmental changes based on available computational resources. Specifically, the perception-planning pipeline of UAVs navigation system is redesigned through dynamic adaptation of mapping resolution and execution frequency, driven by the quantitative environmental complexity evaluations. In addition, E-Navi supports flexible deployment across hardware platforms with varying levels of computing capability. Extensive Hardware-In-the-Loop and real-world experiments demonstrate that the proposed system significantly outperforms the baseline method across various hardware platforms, achieving up to 53.9% navigation task workload reduction, up to 63.8% flight time savings, and delivering more stable velocity control.

