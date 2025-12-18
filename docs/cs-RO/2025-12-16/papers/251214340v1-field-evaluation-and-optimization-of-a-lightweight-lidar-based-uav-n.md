---
layout: default
title: Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments
---

# Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14340" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14340v1</a>
  <a href="https://arxiv.org/pdf/2512.14340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14340v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14340v1', 'Field evaluation and optimization of a lightweight lidar-based UAV navigation system for dense boreal forest environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksi Karhunen, Teemu Hakala, Väinö Karjalainen, Eija Honkavaara

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出一种轻量级激光雷达无人机导航系统，并优化其在稠密北方森林环境中的性能**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `无人机导航` `激光雷达` `SLAM` `路径规划` `森林环境` `自主飞行` `环境感知`

## 📋 核心要点

1. 林下环境无人机自主导航面临挑战，现有研究缺乏对测试环境的严谨描述和飞行成功率的充分报告。
2. 论文提出一种基于轻量级激光雷达的四旋翼无人机自主导航方案，采用IPC路径规划器和LTA-OM SLAM算法。
3. 通过93次飞行实验，优化系统显著提升了可靠性和任务完成时间，并在不同密度森林中取得了较高的成功率。

## 📝 摘要（中文）

近年来，无人机（UAV）在森林应用中的使用兴趣日益增加。虽然在林冠上方飞行已经达到了很高的自主水平，但在林冠下导航仍然是一个重大挑战。自主无人机的使用可以减轻数据收集的负担，这促使人们开发了许多用于林冠下自主飞行的解决方案。然而，文献中进行的实验及其报告缺乏严谨性。很少报告测试森林的密度和难度，或者进行多次飞行并报告这些飞行的成功率。本研究的目的是实施一种基于轻量级激光雷达并使用公开算法的自主飞行四旋翼飞行器，并在真实的森林环境中测试其行为。使用四旋翼原型进行了严格的实验，该原型采用了IPC路径规划器和LTA-OM SLAM算法。根据前33次飞行的结果，对原始系统进行了进一步的增强。通过优化的系统，进行了60次飞行，总共进行了93次测试飞行。优化后的系统在可靠性和飞行任务完成时间方面表现明显更好，在中等密度森林中的成功率为12/15，在稠密森林中的成功率为15/15，目标飞行速度为1米/秒。在2米/秒的目标飞行速度下，成功率分别为12/15和5/15。此外，还提出了一种标准化的测试设置和评估标准，可以对自主林冠下无人机系统进行一致的性能比较，从而提高可重复性，指导系统改进并加速森林机器人技术的发展。

## 🔬 方法详解

**问题定义**：论文旨在解决无人机在稠密北方森林林冠下自主导航的问题。现有方法的痛点在于缺乏在真实复杂环境下的充分测试和性能评估，导致算法的鲁棒性和可靠性难以保证。此外，缺乏标准化的测试流程和评估指标，使得不同算法之间的比较和改进变得困难。

**核心思路**：论文的核心思路是利用轻量级激光雷达获取环境信息，结合SLAM算法进行定位和建图，并使用路径规划算法实现自主导航。通过大量的飞行实验，对系统进行迭代优化，并提出标准化的测试和评估方法，以提高系统的可靠性和可重复性。

**技术框架**：该系统主要包含以下几个模块：1) 激光雷达数据采集模块，负责获取周围环境的点云数据；2) LTA-OM SLAM模块，用于同时定位和建图，估计无人机的位置和姿态，并构建环境地图；3) IPC路径规划模块，根据环境地图和无人机的当前状态，生成安全可行的飞行路径；4) 飞行控制模块，负责控制无人机的飞行，使其按照规划的路径运动。整个流程是闭环的，SLAM模块的输出会反馈给路径规划模块，从而实现实时的导航和避障。

**关键创新**：论文的关键创新在于：1) 提出了一个完整的、可实际部署的林下自主导航系统，并进行了大量的真实环境测试；2) 通过实验数据驱动的优化，显著提升了系统的性能和可靠性；3) 提出了标准化的测试设置和评估标准，为该领域的研究提供了参考。

**关键设计**：论文中没有详细描述关键参数设置、损失函数或网络结构等技术细节。主要关注的是系统层面的集成和优化，以及实验验证和评估。LTA-OM SLAM和IPC路径规划器是已有的开源算法，论文主要的工作在于将它们集成到一个完整的系统中，并针对林下环境进行优化。

## 📊 实验亮点

优化后的系统在中等密度森林中以1m/s的速度飞行时，成功率为12/15，在稠密森林中为15/15。当速度提升到2m/s时，成功率分别为12/15和5/15。这些结果表明，该系统在不同密度的森林环境中都具有较高的可靠性，并且可以通过优化参数来适应不同的飞行速度。

## 🎯 应用场景

该研究成果可应用于森林资源调查、病虫害监测、火灾预警等领域。通过自主导航无人机，可以高效、安全地获取林下环境的数据，减少人工成本和风险。未来，该技术有望进一步推广到其他复杂环境下的自主导航应用，如矿山勘探、灾害救援等。

## 📄 摘要（原文）

> The interest in the usage of uncrewed aerial vehicles (UAVs) for forest applications has increased in recent years. While above-canopy flight has reached a high level of autonomy, navigating under-canopy remains a significant challenge. The use of autonomous UAVs could reduce the burden of data collection, which has motivated the development of numerous solutions for under-canopy autonomous flight. However, the experiments conducted in the literature and their reporting lack rigor. Very rarely, the density and the difficulty of the test forests are reported, or multiple flights are flown, and the success rate of those flights is reported. The aim of this study was to implement an autonomously flying quadrotor based on a lightweight lidar using openly available algorithms and test its behavior in real forest environments. A set of rigorous experiments was conducted with a quadrotor prototype utilizing the IPC path planner and LTA-OM SLAM algorithm. Based on the results of the first 33 flights, the original system was further enhanced. With the optimized system, 60 flights were performed, resulting in a total of 93 test flights. The optimized system performed significantly better in terms of reliability and flight mission completion times, achieving success rates of 12/15 in a medium-density forest and 15/15 in a dense forest, at a target flight velocity of 1 m/s. At a target flight velocity of 2 m/s, it had a success rate of 12/15 and 5/15, respectively. Furthermore, a standardized testing setup and evaluation criteria were proposed, enabling consistent performance comparisons of autonomous under-canopy UAV systems, enhancing reproducibility, guiding system improvements, and accelerating progress in forest robotics.

