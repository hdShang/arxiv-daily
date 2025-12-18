---
layout: default
title: Dynamics-Decoupled Trajectory Alignment for Sim-to-Real Transfer in Reinforcement Learning for Autonomous Driving
---

# Dynamics-Decoupled Trajectory Alignment for Sim-to-Real Transfer in Reinforcement Learning for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07155" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07155v1</a>
  <a href="https://arxiv.org/pdf/2511.07155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.07155v1', 'Dynamics-Decoupled Trajectory Alignment for Sim-to-Real Transfer in Reinforcement Learning for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Steinecker, Alexander Bienemann, Denis Trescher, Thorsten Luettel, Mirko Maehlisch

**分类**: cs.RO, cs.LG

**发布日期**: 2025-11-10

---

## 💡 一句话要点

**提出动力学解耦的轨迹对齐方法，实现自动驾驶RL Sim-to-Real零样本迁移**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `自动驾驶` `Sim-to-Real` `轨迹对齐` `运动规划`

## 📋 核心要点

1. 真实车辆动力学建模困难，导致仿真训练的RL智能体难以直接迁移到真实环境。
2. 通过空间和时间上的轨迹对齐，将运动规划与车辆控制解耦，实现Sim-to-Real迁移。
3. 在真实车辆上验证了该方法，实现了RL运动规划的零样本迁移，有效解耦了高低层控制。

## 📝 摘要（中文）

强化学习(RL)在机器人领域展现了潜力，但由于车辆动力学的复杂性和仿真与现实之间的差异，在真实车辆上部署RL仍然具有挑战性。轮胎特性、路面状况、空气动力扰动和车辆负载等因素使得准确建模真实世界动力学变得不可行，这阻碍了在仿真中训练的RL智能体的直接迁移。本文提出了一种框架，通过虚拟车辆和真实系统之间的空间和时间对齐策略，将运动规划与车辆控制解耦。首先，在仿真中使用运动学自行车模型训练RL智能体以输出连续控制动作。然后，将其行为提炼成轨迹预测智能体，生成有限范围的自车轨迹，从而实现虚拟车辆和真实车辆之间的同步。在部署时，Stanley控制器控制横向动力学，而纵向对齐通过自适应更新机制来维持，以补偿虚拟轨迹和真实轨迹之间的偏差。我们在真实车辆上验证了该方法，并证明所提出的对齐策略能够实现基于RL的运动规划从仿真到现实的鲁棒零样本迁移，成功地将高层轨迹生成与低层车辆控制解耦。

## 🔬 方法详解

**问题定义**：论文旨在解决强化学习在自动驾驶领域中，由于仿真环境与真实环境存在差异，导致在仿真环境中训练的RL智能体无法直接迁移到真实车辆上的问题。现有方法难以准确建模真实车辆的复杂动力学特性，例如轮胎特性、路面状况等，这使得Sim-to-Real的迁移变得困难。

**核心思路**：论文的核心思路是将运动规划与车辆控制解耦。具体来说，首先在仿真环境中使用RL训练一个智能体，该智能体输出连续的控制动作。然后，将该智能体的行为提炼成一个轨迹预测器，该预测器生成有限范围内的车辆轨迹。通过对齐虚拟车辆和真实车辆的轨迹，实现Sim-to-Real的迁移。这种解耦的方式降低了对精确动力学模型的依赖，从而提高了迁移的鲁棒性。

**技术框架**：整体框架包含以下几个主要模块：1) 在仿真环境中使用RL训练轨迹生成器；2) 将训练好的轨迹生成器部署到真实车辆上；3) 使用Stanley控制器控制车辆的横向运动；4) 使用自适应更新机制来对齐虚拟轨迹和真实轨迹，补偿两者之间的偏差。该框架将高层轨迹生成与低层车辆控制分离，简化了控制策略的复杂性。

**关键创新**：论文的关键创新在于提出了动力学解耦的轨迹对齐方法。与传统的直接将RL智能体部署到真实车辆上的方法不同，该方法通过轨迹对齐的方式，将运动规划与车辆控制解耦，降低了对精确动力学模型的依赖。此外，使用自适应更新机制来补偿虚拟轨迹和真实轨迹之间的偏差，进一步提高了迁移的鲁棒性。

**关键设计**：在仿真环境中，使用运动学自行车模型来简化车辆动力学。RL智能体使用连续控制动作作为输出。轨迹预测器生成有限范围的自车轨迹。在真实车辆上，使用Stanley控制器控制横向运动，自适应更新机制根据虚拟轨迹和真实轨迹之间的偏差来调整控制参数。具体的损失函数和网络结构等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

该论文在真实车辆上验证了所提出的方法，实现了基于RL的运动规划从仿真到现实的零样本迁移。实验结果表明，该方法能够有效地解耦高层轨迹生成与低层车辆控制，并能够鲁棒地应对真实环境中的各种不确定性。具体的性能数据和提升幅度在论文中未详细说明，属于未知信息。

## 🎯 应用场景

该研究成果可应用于自动驾驶车辆的运动规划和控制，特别是在需要快速部署和适应新环境的场景中。通过Sim-to-Real迁移，可以降低开发成本和风险，加速自动驾驶技术的落地。此外，该方法还可以扩展到其他机器人领域，例如无人机和移动机器人。

## 📄 摘要（原文）

> Reinforcement learning (RL) has shown promise in robotics, but deploying RL on real vehicles remains challenging due to the complexity of vehicle dynamics and the mismatch between simulation and reality. Factors such as tire characteristics, road surface conditions, aerodynamic disturbances, and vehicle load make it infeasible to model real-world dynamics accurately, which hinders direct transfer of RL agents trained in simulation. In this paper, we present a framework that decouples motion planning from vehicle control through a spatial and temporal alignment strategy between a virtual vehicle and the real system. An RL agent is first trained in simulation using a kinematic bicycle model to output continuous control actions. Its behavior is then distilled into a trajectory-predicting agent that generates finite-horizon ego-vehicle trajectories, enabling synchronization between virtual and real vehicles. At deployment, a Stanley controller governs lateral dynamics, while longitudinal alignment is maintained through adaptive update mechanisms that compensate for deviations between virtual and real trajectories. We validate our approach on a real vehicle and demonstrate that the proposed alignment strategy enables robust zero-shot transfer of RL-based motion planning from simulation to reality, successfully decoupling high-level trajectory generation from low-level vehicle control.

