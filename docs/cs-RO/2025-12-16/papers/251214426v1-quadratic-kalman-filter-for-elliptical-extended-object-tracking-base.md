---
layout: default
title: Quadratic Kalman Filter for Elliptical Extended Object Tracking based on Decoupling State Components
---

# Quadratic Kalman Filter for Elliptical Extended Object Tracking based on Decoupling State Components

**arXiv**: [2512.14426v1](https://arxiv.org/abs/2512.14426) | [PDF](https://arxiv.org/pdf/2512.14426.pdf)

**作者**: Simon Steuernagel, Marcus Baum

**分类**: eess.SP, cs.RO

**发布日期**: 2025-12-16

**备注**: 13 pages, 8 figures, submitted to IEEE Transactions on Aerospace and Electronic Systems

---

## 💡 一句话要点

**提出基于状态分量解耦的二次卡尔曼滤波器，用于椭圆扩展目标跟踪，实现高效高精度估计。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `扩展目标跟踪` `椭圆目标跟踪` `卡尔曼滤波器` `状态解耦` `汽车雷达` `自动驾驶` `高效计算` `确定性算法`

## 📋 核心要点

1. 现有扩展目标跟踪方法通常需要复杂近似或采样，计算成本高且难以平衡精度与效率。
2. 论文提出将状态分解为运动学、方向和轴长分量，分别估计以简化计算并减少近似需求。
3. 算法在仿真和真实雷达数据上验证，达到采样方法精度，批处理变体计算高效且超越现有方法。

## 📝 摘要（中文）

扩展目标跟踪涉及同时估计目标物体的物理尺寸和运动学参数，通常每个时间步会观测到多个测量值。本文提出了一种基于运动学、方向和轴长分量解耦的确定性闭式椭圆扩展目标跟踪器。通过忽略这些状态分量之间的潜在相关性，相比整体联合解决方案，各个估计器所需的近似更少。所得算法优于现有算法，达到了基于采样方法的精度水平。此外，还引入了基于批处理的变体，实现了高效计算，同时超越了所有可比较的最先进算法。这通过使用文献中常见模型的仿真研究，以及对真实汽车雷达数据的广泛定量评估得到了验证。

## 🔬 方法详解

论文提出一种基于二次卡尔曼滤波器的椭圆扩展目标跟踪框架，核心创新在于将状态向量解耦为运动学、方向和轴长三个独立分量，分别进行估计。通过忽略分量间的相关性，减少了整体联合估计所需的近似步骤，从而简化了计算复杂度。关键技术创新包括设计确定性闭式解和引入批处理变体以提高效率。与现有方法相比，该方法避免了复杂的采样过程，同时保持了高精度，实现了精度与效率的更好平衡。

## 📊 实验亮点

在仿真和真实汽车雷达数据上验证，算法精度达到基于采样方法的水平，批处理变体计算效率高，在性能上超越了所有可比较的最先进算法，显示出显著的性能提升。

## 🎯 应用场景

该研究主要应用于自动驾驶和智能交通系统中的目标跟踪，如汽车雷达对车辆、行人等扩展目标的实时监测与状态估计。其高效高精度的特性可提升环境感知能力，支持更安全的决策和控制，具有实际工程价值。

## 📄 摘要（原文）

> Extended object tracking involves estimating both the physical extent and kinematic parameters of a target object, where typically multiple measurements are observed per time step. In this article, we propose a deterministic closed-form elliptical extended object tracker, based on decoupling of the kinematics, orientation, and axis lengths. By disregarding potential correlations between these state components, fewer approximations are required for the individual estimators than for an overall joint solution. The resulting algorithm outperforms existing algorithms, reaching the accuracy of sampling-based procedures. Additionally, a batch-based variant is introduced, yielding highly efficient computation while outperforming all comparable state-of-the-art algorithms. This is validated both by a simulation study using common models from literature, as well as an extensive quantitative evaluation on real automotive radar data.

