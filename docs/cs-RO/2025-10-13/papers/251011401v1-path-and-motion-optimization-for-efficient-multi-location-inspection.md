---
layout: default
title: Path and Motion Optimization for Efficient Multi-Location Inspection with Humanoid Robots
---

# Path and Motion Optimization for Efficient Multi-Location Inspection with Humanoid Robots

**arXiv**: [2510.11401v1](https://arxiv.org/abs/2510.11401) | [PDF](https://arxiv.org/pdf/2510.11401.pdf)

**作者**: Jiayang Wu, Jiongye Li, Shibowen Zhang, Zhicheng He, Zaijin Wang, Xiaokun Leng, Hangxin Liu, Jingwen Zhang, Jiayi Wang, Song-Chun Zhu, Yao Su

---

## 💡 一句话要点

**提出人形机器人多位置检测框架，结合分层规划与MPC实现高效毫米级精度**

**关键词**: `人形机器人` `分层规划` `模型预测控制` `多位置检测` `轨迹优化`

## 📋 核心要点

1. 核心问题：人形机器人在多位置检测任务中需兼顾高效率和毫米级精度，计算复杂度高
2. 方法要点：采用分层规划、MIP优化站立位置和MPC系统，降低复杂度并提升跟踪精度
3. 实验或效果：在Kuavo 4Pro平台上验证，任务完成时间短且成功率高

## 📄 摘要（原文）

> This paper proposes a novel framework for humanoid robots to execute
> inspection tasks with high efficiency and millimeter-level precision. The
> approach combines hierarchical planning, time-optimal standing position
> generation, and integrated \ac{mpc} to achieve high speed and precision. A
> hierarchical planning strategy, leveraging \ac{ik} and \ac{mip}, reduces
> computational complexity by decoupling the high-dimensional planning problem. A
> novel MIP formulation optimizes standing position selection and trajectory
> length, minimizing task completion time. Furthermore, an MPC system with
> simplified kinematics and single-step position correction ensures
> millimeter-level end-effector tracking accuracy. Validated through simulations
> and experiments on the Kuavo 4Pro humanoid platform, the framework demonstrates
> low time cost and a high success rate in multi-location tasks, enabling
> efficient and precise execution of complex industrial operations.

