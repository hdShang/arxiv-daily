---
layout: default
title: Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field
---

# Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field

**arXiv**: [2512.14111v1](https://arxiv.org/abs/2512.14111) | [PDF](https://arxiv.org/pdf/2512.14111.pdf)

**作者**: Chenzui Li, Yiming Chen, Xi Wu, Tao Teng, Sylvain Calinon, Darwin Caldwell, Fei Chen

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**提出基于人机配置空间人因工程场的交互式运动规划方法，以提升工业人机协作的实时性与人因安全性。**

**关键词**: `人机协作` `运动规划` `人因工程` `配置空间优化` `梯度规划` `实时控制` `工业机器人` `肌肉激活分析`

## 📋 核心要点

1. 现有工业人机协作规划方法在实时响应和人因工程优化方面存在不足，难以平衡安全性与效率。
2. 提出配置空间人因工程场（CSEF），通过连续可微场量化人因质量，并集成梯度规划实现实时优化。
3. 实验显示，CSEF规划在成功率和计算速度上优于任务空间方法，硬件测试中显著降低人因评分和肌肉激活。

## 📝 摘要（中文）

工业人机协作需要无碰撞、响应迅速且符合人因工程安全的运动规划，以减少疲劳和肌肉骨骼风险。本文提出配置空间人因工程场（CSEF），这是一种在人体关节空间上连续可微的场，用于量化人因工程质量并提供实时人因感知规划的梯度。我们通过关节加权和任务条件化，从现有指标中高效构建CSEF，并将其集成到与阻抗控制机器人兼容的基于梯度的规划器中。在2自由度基准测试中，基于CSEF的规划比任务空间人因规划器实现了更高的成功率、更低的人因成本和更快的计算速度。硬件实验中，使用双臂机器人进行单臂引导、协作钻孔和双臂协同搬运任务，相比点对点基线，展示了更快的人因成本降低、更接近优化关节目标的跟踪以及更低的肌肉激活水平。基于CSEF的规划方法在协作钻孔任务中平均人因评分降低高达10.31%，在双臂协同搬运任务中降低5.60%，同时减少了关键肌肉群的激活，表明其实用部署的实际效益。

## 🔬 方法详解

论文提出配置空间人因工程场（CSEF）作为核心方法，整体框架包括从现有人因指标构建CSEF，并集成到基于梯度的运动规划器中。关键技术创新在于CSEF的连续可微性，允许在人体关节空间直接计算梯度，实现实时人因优化规划。与现有方法的主要区别在于，传统任务空间规划器可能缺乏关节级精度和实时性，而CSEF通过关节加权和任务条件化，提供了更高效、可微的人因评估，兼容阻抗控制机器人，提升了规划的响应速度和安全性。

## 📊 实验亮点

在2自由度基准测试中，CSEF规划比任务空间方法成功率更高、人因成本更低、计算更快；硬件实验中，协作钻孔任务人因评分降低10.31%，双臂协同搬运降低5.60%，并显著减少肌肉激活，验证了方法的有效性。

## 🎯 应用场景

该研究主要应用于工业人机协作场景，如装配线、制造和物流领域，通过实时人因优化规划，减少工人疲劳和肌肉骨骼风险，提升协作效率和安全性，具有实际部署价值。

## 📄 摘要（原文）

> Industrial human-robot collaboration requires motion planning that is collision-free, responsive, and ergonomically safe to reduce fatigue and musculoskeletal risk. We propose the Configuration Space Ergonomic Field (CSEF), a continuous and differentiable field over the human joint space that quantifies ergonomic quality and provides gradients for real-time ergonomics-aware planning. An efficient algorithm constructs CSEF from established metrics with joint-wise weighting and task conditioning, and we integrate it into a gradient-based planner compatible with impedance-controlled robots. In a 2-DoF benchmark, CSEF-based planning achieves higher success rates, lower ergonomic cost, and faster computation than a task-space ergonomic planner. Hardware experiments with a dual-arm robot in unimanual guidance, collaborative drilling, and bimanual cocarrying show faster ergonomic cost reduction, closer tracking to optimized joint targets, and lower muscle activation than a point-to-point baseline. CSEF-based planning method reduces average ergonomic scores by up to 10.31% for collaborative drilling tasks and 5.60% for bimanual co-carrying tasks while decreasing activation in key muscle groups, indicating practical benefits for real-world deployment.

