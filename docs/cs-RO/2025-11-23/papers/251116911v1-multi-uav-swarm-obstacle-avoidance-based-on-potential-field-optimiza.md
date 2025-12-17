---
layout: default
title: Multi-UAV Swarm Obstacle Avoidance Based on Potential Field Optimization
---

# Multi-UAV Swarm Obstacle Avoidance Based on Potential Field Optimization

**arXiv**: [2511.16911v1](https://arxiv.org/abs/2511.16911) | [PDF](https://arxiv.org/pdf/2511.16911.pdf)

**作者**: Yendo Hu, Yiliang Wu, Weican Chen

---

## 💡 一句话要点

**提出混合算法以解决多无人机编队避障中的路径冗余和碰撞问题**

**关键词**: `多无人机编队` `人工势场优化` `避障算法` `路径规划` `碰撞风险评估`

## 📋 核心要点

1. 传统人工势场法导致路径冗余、航向突变和无人机间碰撞
2. 结合改进编队避障算法与单机路径优化，引入交互力和辅助子目标策略
3. 仿真显示路径长度和航向稳定性显著提升，有效避障并快速恢复编队

## 📄 摘要（原文）

> In multi UAV scenarios,the traditional Artificial Potential Field (APF) method often leads to redundant flight paths and frequent abrupt heading changes due to unreasonable obstacle avoidance path planning,and is highly prone to inter UAV collisions during the obstacle avoidance process.To address these issues,this study proposes a novel hybrid algorithm that combines the improved Multi-Robot Formation Obstacle Avoidance (MRF IAPF) algorithm with an enhanced APF optimized for single UAV path planning.Its core ideas are as follows:first,integrating three types of interaction forces from MRF IAPF obstacle repulsion force,inter UAV interaction force,and target attraction force;second,incorporating a refined single UAV path optimization mechanism,including collision risk assessment and an auxiliary sub goal strategy.When a UAV faces a high collision threat,temporary waypoints are generated to guide obstacle avoidance,ensuring eventual precise arrival at the actual target.Simulation results demonstrate that compared with traditional APF based formation algorithms,the proposed algorithm achieves significant improvements in path length optimization and heading stability,can effectively avoid obstacles and quickly restore the formation configuration,thus verifying its applicability and effectiveness in static environments with unknown obstacles.

