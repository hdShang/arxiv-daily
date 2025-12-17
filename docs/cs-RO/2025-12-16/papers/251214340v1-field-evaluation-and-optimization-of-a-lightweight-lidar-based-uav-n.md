---
layout: default
title: Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments
---

# Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments

**arXiv**: [2512.14340v1](https://arxiv.org/abs/2512.14340) | [PDF](https://arxiv.org/pdf/2512.14340.pdf)

**作者**: Aleksi Karhunen, Teemu Hakala, Väinö Karjalainen, Eija Honkavaara

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出基于轻量级激光雷达的无人机导航系统优化方案，解决稠密北方森林环境下的自主飞行挑战。**

🎯 **匹配领域**: **自动驾驶** **视觉里程计**

**关键词**: `无人机导航` `激光雷达` `森林环境` `自主飞行` `SLAM算法` `路径规划` `系统优化` `实验评估`

## 📋 核心要点

1. 现有方法在稠密森林冠层下自主飞行实验中缺乏严谨性，很少报告森林密度、难度和多次飞行的成功率。
2. 论文基于轻量级激光雷达，采用公开算法（IPC路径规划器和LTA-OM SLAM）实现自主四旋翼无人机，并通过实验优化系统性能。
3. 优化后系统在1 m/s速度下，中密度和稠密森林成功率分别达12/15和15/15，并提出了标准化测试框架以提升可重复性。

## 📝 摘要（中文）

近年来，无人机在森林应用中的使用兴趣日益增长。虽然冠层以上飞行已达到高度自主性，但在冠层下导航仍是一个重大挑战。自主无人机的使用可以减轻数据收集的负担，这推动了众多冠层下自主飞行解决方案的开发。然而，文献中进行的实验及其报告缺乏严谨性。很少报告测试森林的密度和难度，或进行多次飞行并报告这些飞行的成功率。本研究旨在基于轻量级激光雷达，使用公开可用的算法实现自主飞行的四旋翼无人机，并在真实森林环境中测试其行为。利用IPC路径规划器和LTA-OM SLAM算法，对四旋翼原型进行了严格的实验。基于前33次飞行的结果，对原始系统进行了进一步优化。使用优化后的系统进行了60次飞行，总共完成了93次测试飞行。优化后的系统在可靠性和飞行任务完成时间方面表现显著更好，在目标飞行速度为1 m/s时，在中密度森林中实现了12/15的成功率，在稠密森林中实现了15/15的成功率。在目标飞行速度为2 m/s时，成功率分别为12/15和5/15。此外，提出了标准化的测试设置和评估标准，使自主冠层下无人机系统的性能比较具有一致性，增强了可重复性，指导系统改进，并加速了森林机器人技术的进展。

## 🔬 方法详解

论文构建了一个基于轻量级激光雷达的无人机导航系统整体框架，核心包括IPC路径规划器和LTA-OM SLAM算法。关键技术创新点在于结合公开算法实现轻量化系统，并通过实验数据驱动优化，提升在复杂森林环境中的鲁棒性。与现有方法的主要区别在于强调实验严谨性和标准化评估，而非仅提出新算法，这有助于系统性能的客观比较和改进。

## 📊 实验亮点

优化系统在93次测试飞行中表现显著提升：1 m/s速度下，中密度森林成功率80%（12/15），稠密森林成功率100%（15/15）；2 m/s速度下，成功率分别为80%和33%。同时，提出的标准化测试框架增强了实验可重复性和系统比较性。

## 🎯 应用场景

该研究主要应用于森林监测和数据收集领域，如生态调查、资源管理和灾害评估。通过实现稠密森林环境下的自主飞行，可降低人工数据采集成本，提升效率，推动森林机器人技术的实际部署和进步。

## 📄 摘要（原文）

> The interest in the usage of uncrewed aerial vehicles (UAVs) for forest applications has increased in recent years. While above-canopy flight has reached a high level of autonomy, navigating under-canopy remains a significant challenge. The use of autonomous UAVs could reduce the burden of data collection, which has motivated the development of numerous solutions for under-canopy autonomous flight. However, the experiments conducted in the literature and their reporting lack rigor. Very rarely, the density and the difficulty of the test forests are reported, or multiple flights are flown, and the success rate of those flights is reported. The aim of this study was to implement an autonomously flying quadrotor based on a lightweight lidar using openly available algorithms and test its behavior in real forest environments. A set of rigorous experiments was conducted with a quadrotor prototype utilizing the IPC path planner and LTA-OM SLAM algorithm. Based on the results of the first 33 flights, the original system was further enhanced. With the optimized system, 60 flights were performed, resulting in a total of 93 test flights. The optimized system performed significantly better in terms of reliability and flight mission completion times, achieving success rates of 12/15 in a medium-density forest and 15/15 in a dense forest, at a target flight velocity of 1 m/s. At a target flight velocity of 2 m/s, it had a success rate of 12/15 and 5/15, respectively. Furthermore, a standardized testing setup and evaluation criteria were proposed, enabling consistent performance comparisons of autonomous under-canopy UAV systems, enhancing reproducibility, guiding system improvements, and accelerating progress in forest robotics.

