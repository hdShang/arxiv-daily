---
layout: default
title: Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration
---

# Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration

**arXiv**: [2512.09833v1](https://arxiv.org/abs/2512.09833) | [PDF](https://arxiv.org/pdf/2512.09833.pdf)

**作者**: Elias Krantz, Ngai Nam Chan, Gunnar Tibert, Huina Mao, Christer Fuglesang

---

## 💡 一句话要点

**提出轻量级开源通信桥接器，连接Basilisk航天动力学模拟器与ROS 2，支持模块化航天器自主开发。**

**关键词**: `航天器模拟` `ROS 2集成` `模块化自主系统` `硬件在环测试` `编队飞行控制`

## 📋 核心要点

1. 核心问题：高保真航天器模拟器与模块化机器人框架集成困难，阻碍自主性开发。
2. 方法要点：无需修改Basilisk核心，实现实时双向数据交换，无缝集成ROS 2节点。
3. 实验或效果：在领航-跟随编队飞行场景中验证，支持仿真与硬件测试的平滑过渡。

## 📄 摘要（原文）

> Integrating high-fidelity spacecraft simulators with modular robotics frameworks remains a challenge for autonomy development. This paper presents a lightweight, open-source communication bridge between the Basilisk astrodynamics simulator and the Robot Operating System 2 (ROS 2), enabling real-time, bidirectional data exchange for spacecraft control. The bridge requires no changes to Basilisk's core and integrates seamlessly with ROS 2 nodes. We demonstrate its use in a leader-follower formation flying scenario using nonlinear model predictive control, deployed identically in both simulation and on the ATMOS planar microgravity testbed. This setup supports rapid development, hardware-in-the-loop testing, and seamless transition from simulation to hardware. The bridge offers a flexible and scalable platform for modular spacecraft autonomy and reproducible research workflows.

