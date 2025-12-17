---
layout: default
title: Local Path Planning with Dynamic Obstacle Avoidance in Unstructured Environments
---

# Local Path Planning with Dynamic Obstacle Avoidance in Unstructured Environments

**arXiv**: [2511.07927v1](https://arxiv.org/abs/2511.07927) | [PDF](https://arxiv.org/pdf/2511.07927.pdf)

**作者**: Okan Arif Guvenkaya, Selim Ahmet Iz, Mustafa Unel

---

## 💡 一句话要点

**提出基于切线和外推的局部路径规划算法，用于UGV在动态障碍物环境中的避障。**

**关键词**: `局部路径规划` `动态避障` `无人地面车辆` `非结构化环境` `切线规划` `外推方法`

## 📋 核心要点

1. 核心问题：UGV在动态障碍物密集的非结构化环境中需安全导航并避免碰撞。
2. 方法要点：结合切线路径规划和外推方法，开发新决策算法处理动态障碍物。
3. 实验或效果：模拟测试显示算法能逐步生成无碰撞路径，确保机器人安全到达目标。

## 📄 摘要（原文）

> Obstacle avoidance and path planning are essential for guiding unmanned ground vehicles (UGVs) through environments that are densely populated with dynamic obstacles. This paper develops a novel approach that combines tangentbased path planning and extrapolation methods to create a new decision-making algorithm for local path planning. In the assumed scenario, a UGV has a prior knowledge of its initial and target points within the dynamic environment. A global path has already been computed, and the robot is provided with waypoints along this path. As the UGV travels between these waypoints, the algorithm aims to avoid collisions with dynamic obstacles. These obstacles follow polynomial trajectories, with their initial positions randomized in the local map and velocities randomized between O and the allowable physical velocity limit of the robot, along with some random accelerations. The developed algorithm is tested in several scenarios where many dynamic obstacles move randomly in the environment. Simulation results show the effectiveness of the proposed local path planning strategy by gradually generating a collision free path which allows the robot to navigate safely between initial and the target locations.

