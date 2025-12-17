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

**提出基于轻量激光雷达的无人机导航系统优化与标准化评估方法，以解决稠密北方森林环境下的自主飞行挑战。**

**关键词**: `无人机导航` `激光雷达` `森林机器人学` `自主飞行` `SLAM算法` `路径规划` `稠密环境` `标准化评估`

## 📋 核心要点

1. 现有方法在稠密森林冠层下自主飞行中缺乏严谨实验报告，如森林密度和成功率数据不足。
2. 论文基于轻量激光雷达和公开算法，构建无人机导航系统，并通过优化提升性能。
3. 优化系统在真实森林测试中显著提高成功率，并提出了标准化评估框架以促进领域发展。

## 📝 摘要（中文）

近年来，无人机在森林应用中的使用兴趣日益增长。尽管冠层以上飞行已达到高度自主性，但冠层下导航仍是一个重大挑战。自主无人机的使用可减轻数据收集负担，这推动了众多冠层下自主飞行解决方案的开发。然而，文献中的实验及其报告缺乏严谨性，很少报告测试森林的密度和难度，或进行多次飞行并报告成功率。本研究旨在基于轻量激光雷达，利用公开算法实现自主飞行的四旋翼无人机，并在真实森林环境中测试其行为。使用IPC路径规划器和LTA-OM SLAM算法，对四旋翼原型进行了严格实验。基于前33次飞行结果，进一步优化了原始系统。优化系统进行了60次飞行，总计93次测试飞行。优化系统在可靠性和飞行任务完成时间方面表现显著更好，在目标飞行速度1 m/s下，中等密度森林中成功率为12/15，稠密森林中为15/15；在2 m/s下，成功率分别为12/15和5/15。此外，提出了标准化测试设置和评估标准，以实现自主冠层下无人机系统性能的一致比较，增强可重复性，指导系统改进，并加速森林机器人学进展。

## 🔬 方法详解

论文采用基于轻量激光雷达的四旋翼无人机平台，整体框架结合了IPC路径规划器和LTA-OM SLAM算法。关键技术创新点在于系统优化，通过初始33次飞行结果分析，调整参数或算法以增强可靠性和效率。与现有方法的主要区别在于强调实验严谨性和标准化评估，而非仅依赖算法创新，从而在稠密森林环境中实现更稳定的自主导航。

## 📊 实验亮点

优化系统在目标速度1 m/s下，中等密度森林成功率达12/15，稠密森林达15/15；速度提升至2 m/s时，成功率分别为12/15和5/15。总计93次飞行验证了性能提升，并建立了标准化测试标准。

## 🎯 应用场景

该研究适用于森林监测、生态调查和资源管理等领域，通过自主无人机在稠密冠层下飞行，可高效收集数据，减少人工负担，提升森林机器人学的实际应用价值。

## 📄 摘要（原文）

> The interest in the usage of uncrewed aerial vehicles (UAVs) for forest applications has increased in recent years. While above-canopy flight has reached a high level of autonomy, navigating under-canopy remains a significant challenge. The use of autonomous UAVs could reduce the burden of data collection, which has motivated the development of numerous solutions for under-canopy autonomous flight. However, the experiments conducted in the literature and their reporting lack rigor. Very rarely, the density and the difficulty of the test forests are reported, or multiple flights are flown, and the success rate of those flights is reported. The aim of this study was to implement an autonomously flying quadrotor based on a lightweight lidar using openly available algorithms and test its behavior in real forest environments. A set of rigorous experiments was conducted with a quadrotor prototype utilizing the IPC path planner and LTA-OM SLAM algorithm. Based on the results of the first 33 flights, the original system was further enhanced. With the optimized system, 60 flights were performed, resulting in a total of 93 test flights. The optimized system performed significantly better in terms of reliability and flight mission completion times, achieving success rates of 12/15 in a medium-density forest and 15/15 in a dense forest, at a target flight velocity of 1 m/s. At a target flight velocity of 2 m/s, it had a success rate of 12/15 and 5/15, respectively. Furthermore, a standardized testing setup and evaluation criteria were proposed, enabling consistent performance comparisons of autonomous under-canopy UAV systems, enhancing reproducibility, guiding system improvements, and accelerating progress in forest robotics.

