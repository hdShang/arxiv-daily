---
layout: default
title: Obstacle Avoidance using Dynamic Movement Primitives and Reinforcement Learning
---

# Obstacle Avoidance using Dynamic Movement Primitives and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09254" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09254v1</a>
  <a href="https://arxiv.org/pdf/2510.09254.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09254v1" onclick="toggleFavorite(this, '2510.09254v1', 'Obstacle Avoidance using Dynamic Movement Primitives and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dominik Urbaniak, Alejandro Agostini, Pol Ramon, Jan Rosell, Raúl Suárez, Michael Suppa

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-10

**备注**: 8 pages, 7 figures

**🔗 代码/项目**: [GITHUB](https://github.com/DominikUrbaniak/obst-avoid-dmp-pi2)

---

## 💡 一句话要点

**提出基于DMP和强化学习的避障方法，仅需单次演示即可快速生成平滑轨迹。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人避障` `动态运动原语` `强化学习` `运动规划` `神经网络`

## 📋 核心要点

1. 现有学习型运动规划方法依赖大量训练数据或昂贵的人工示教，限制了其应用。
2. 该方法利用单次人工示教编码为DMP，通过强化学习迭代优化，生成多样化轨迹数据集。
3. 实验结果表明，该方法在计算效率、轨迹质量和多模态适应性方面优于传统方法。

## 📝 摘要（中文）

本文提出了一种基于学习的运动规划方法，能够快速生成近乎最优的轨迹。该方法避免了对大量训练数据或昂贵的人工示教的依赖，仅需单次人工示教即可生成平滑、近乎最优且无碰撞的3D笛卡尔轨迹。该示教被编码为动态运动原语(DMP)，并使用基于策略的强化学习进行迭代重塑，从而为不同的障碍物配置创建多样化的轨迹数据集。该数据集用于训练一个神经网络，该网络以描述障碍物尺寸和位置的任务参数（自动从点云中提取）作为输入，并输出生成轨迹的DMP参数。在仿真和真实机器人实验中验证了该方法的有效性，在计算和执行时间以及轨迹长度方面均优于RRT-Connect基线，同时支持针对不同障碍物几何形状和末端执行器尺寸的多模态轨迹生成。代码和视频可在https://github.com/DominikUrbaniak/obst-avoid-dmp-pi2 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人运动规划中的避障问题，现有方法如RRT-Connect等计算成本高，学习型方法则需要大量训练数据或人工示教，难以快速适应新环境。

**核心思路**：利用动态运动原语(DMP)对轨迹进行参数化表示，降低学习难度；通过强化学习对DMP参数进行优化，使其能够适应不同的障碍物配置，从而实现快速、高效的避障。

**技术框架**：整体流程包括：1)单次人工示教，编码为DMP；2)使用强化学习(PI2)迭代优化DMP参数，生成多样化的轨迹数据集；3)训练神经网络，输入障碍物参数（从点云提取），输出DMP参数；4)机器人执行生成的轨迹。

**关键创新**：该方法的核心创新在于将DMP与强化学习相结合，仅需单次人工示教即可生成高质量的避障轨迹，显著降低了对大量训练数据的依赖。同时，使用神经网络学习障碍物参数到DMP参数的映射，实现了快速适应新环境的能力。

**关键设计**：DMP使用高斯核函数进行基函数扩展，强化学习采用PI2算法进行策略优化。神经网络的输入是障碍物的尺寸和位置参数，输出是DMP的权重参数。损失函数的设计旨在最小化轨迹长度和碰撞风险。

## 📊 实验亮点

实验结果表明，该方法在仿真和真实机器人实验中均优于RRT-Connect基线。在计算和执行时间上，该方法显著降低；在轨迹长度上，该方法也更优。此外，该方法还支持针对不同障碍物几何形状和末端执行器尺寸的多模态轨迹生成。

## 🎯 应用场景

该研究成果可应用于各种需要机器人自主避障的场景，如工业自动化、物流搬运、家庭服务机器人等。通过快速学习和适应新环境，提高机器人的工作效率和安全性，降低人工干预的需求，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Learning-based motion planning can quickly generate near-optimal trajectories. However, it often requires either large training datasets or costly collection of human demonstrations. This work proposes an alternative approach that quickly generates smooth, near-optimal collision-free 3D Cartesian trajectories from a single artificial demonstration. The demonstration is encoded as a Dynamic Movement Primitive (DMP) and iteratively reshaped using policy-based reinforcement learning to create a diverse trajectory dataset for varying obstacle configurations. This dataset is used to train a neural network that takes as inputs the task parameters describing the obstacle dimensions and location, derived automatically from a point cloud, and outputs the DMP parameters that generate the trajectory. The approach is validated in simulation and real-robot experiments, outperforming a RRT-Connect baseline in terms of computation and execution time, as well as trajectory length, while supporting multi-modal trajectory generation for different obstacle geometries and end-effector dimensions. Videos and the implementation code are available at https://github.com/DominikUrbaniak/obst-avoid-dmp-pi2.

