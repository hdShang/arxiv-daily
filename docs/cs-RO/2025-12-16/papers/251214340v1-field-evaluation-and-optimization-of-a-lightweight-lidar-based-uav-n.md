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

🎯 **匹配领域**: **自动驾驶** **视觉里程计**

**关键词**: `无人机导航` `激光雷达SLAM` `森林机器人` `路径规划` `自主飞行` `实地测试` `系统优化` `标准化评估`

## 📋 核心要点

1. 现有方法在稠密森林冠层下自主飞行中缺乏严谨的实验评估，如森林密度报告不足和成功率统计不完整。
2. 论文基于轻量激光雷达和开源算法构建无人机系统，通过优化提升在真实森林环境中的导航可靠性和效率。
3. 优化后系统在1 m/s速度下实现高成功率，并提出了标准化测试框架，促进森林机器人领域的可重复研究和系统改进。

## 📝 摘要（中文）

近年来，无人机在森林应用中的使用兴趣日益增长。虽然冠层以上飞行已达到高度自主性，但在冠层下导航仍是一个重大挑战。自主无人机的使用可以减轻数据收集的负担，这推动了众多冠层下自主飞行解决方案的开发。然而，文献中进行的实验及其报告缺乏严谨性。很少报告测试森林的密度和难度，或进行多次飞行并报告其成功率。本研究旨在基于轻量激光雷达，使用公开可用的算法实现自主飞行的四旋翼无人机，并在真实森林环境中测试其行为。利用IPC路径规划器和LTA-OM SLAM算法，对四旋翼原型进行了严格的实验。基于前33次飞行的结果，对原始系统进行了进一步优化。使用优化后的系统进行了60次飞行，总共完成了93次测试飞行。优化后的系统在可靠性和飞行任务完成时间方面表现显著更好，在目标飞行速度为1 m/s时，在中密度森林中实现了12/15的成功率，在稠密森林中实现了15/15的成功率。在目标飞行速度为2 m/s时，其成功率分别为12/15和5/15。此外，提出了标准化的测试设置和评估标准，使自主冠层下无人机系统的性能比较具有一致性，增强了可重复性，指导系统改进，并加速了森林机器人学的进展。

## 🔬 方法详解

**问题定义**：论文旨在解决无人机在稠密北方森林冠层下自主导航的挑战，现有方法实验评估不严谨，缺乏标准化测试和成功率报告，导致系统性能难以比较和优化。

**核心思路**：采用轻量激光雷达结合公开算法，构建低成本、易复现的无人机导航系统，通过大量真实环境飞行测试进行迭代优化，并引入标准化评估框架以提升实验严谨性和可重复性。

**技术框架**：整体架构包括四旋翼无人机平台、轻量激光雷达传感器、LTA-OM SLAM算法用于实时定位与建图，以及IPC路径规划器用于动态路径生成。流程分为原型开发、初步测试（33次飞行）、系统优化和最终验证（60次飞行）四个阶段。

**关键创新**：最重要的技术创新在于将开源算法集成到轻量系统中，并通过大规模实地测试驱动优化，同时提出标准化测试设置，这在现有研究中较少见，本质区别在于强调实验严谨性和系统可重复性。

**关键设计**：关键参数包括目标飞行速度设置为1 m/s和2 m/s以测试性能极限，使用LTA-OM SLAM确保在稠密环境中的鲁棒定位，IPC规划器适应动态障碍，实验设计覆盖不同森林密度（中密度和稠密）以全面评估系统可靠性。

## 📊 实验亮点

优化后系统在目标速度1 m/s下，中密度森林成功率12/15，稠密森林成功率15/15；速度提升至2 m/s时，成功率分别降至12/15和5/15。通过93次飞行测试，系统可靠性和任务完成时间显著改善，并建立了标准化评估标准，为后续研究提供了可比较的性能基准。

## 🎯 应用场景

该研究在森林监测、生态调查和资源管理等领域具有潜在应用价值，通过提升无人机在复杂环境下的自主飞行能力，可降低数据收集成本并提高效率。未来可能推动森林机器人学的标准化发展，加速相关技术的实际部署和商业化进程。

## 📄 摘要（原文）

> The interest in the usage of uncrewed aerial vehicles (UAVs) for forest applications has increased in recent years. While above-canopy flight has reached a high level of autonomy, navigating under-canopy remains a significant challenge. The use of autonomous UAVs could reduce the burden of data collection, which has motivated the development of numerous solutions for under-canopy autonomous flight. However, the experiments conducted in the literature and their reporting lack rigor. Very rarely, the density and the difficulty of the test forests are reported, or multiple flights are flown, and the success rate of those flights is reported. The aim of this study was to implement an autonomously flying quadrotor based on a lightweight lidar using openly available algorithms and test its behavior in real forest environments. A set of rigorous experiments was conducted with a quadrotor prototype utilizing the IPC path planner and LTA-OM SLAM algorithm. Based on the results of the first 33 flights, the original system was further enhanced. With the optimized system, 60 flights were performed, resulting in a total of 93 test flights. The optimized system performed significantly better in terms of reliability and flight mission completion times, achieving success rates of 12/15 in a medium-density forest and 15/15 in a dense forest, at a target flight velocity of 1 m/s. At a target flight velocity of 2 m/s, it had a success rate of 12/15 and 5/15, respectively. Furthermore, a standardized testing setup and evaluation criteria were proposed, enabling consistent performance comparisons of autonomous under-canopy UAV systems, enhancing reproducibility, guiding system improvements, and accelerating progress in forest robotics.

