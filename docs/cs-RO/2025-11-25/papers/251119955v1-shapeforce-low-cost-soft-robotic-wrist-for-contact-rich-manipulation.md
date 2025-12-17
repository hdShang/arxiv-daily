---
layout: default
title: ShapeForce: Low-Cost Soft Robotic Wrist for Contact-Rich Manipulation
---

# ShapeForce: Low-Cost Soft Robotic Wrist for Contact-Rich Manipulation

**arXiv**: [2511.19955v1](https://arxiv.org/abs/2511.19955) | [PDF](https://arxiv.org/pdf/2511.19955.pdf)

**作者**: Jinxuan Zhu, Zihao Yan, Yangyu Xiao, Jingxiang Guo, Chenrui Tie, Xinyi Cao, Yuhang Zheng, Lin Shao

---

## 💡 一句话要点

**提出ShapeForce软体手腕以低成本提供接触反馈，用于接触丰富的机器人操作。**

**关键词**: `软体机器人手腕` `接触反馈` `低成本传感器` `力-力矩估计` `机器人操作`

## 📋 核心要点

1. 核心问题：六轴力-力矩传感器成本高且易碎，限制接触反馈在机器人操作中的应用。
2. 方法要点：通过软体核心变形和标记点姿态跟踪，估计力-力矩变化，无需校准。
3. 实验或效果：在多种接触任务中，性能媲美六轴传感器，成本极低。

## 📄 摘要（原文）

> Contact feedback is essential for contact-rich robotic manipulation, as it allows the robot to detect subtle interaction changes and adjust its actions accordingly. Six- axis force-torque sensors are commonly used to obtain contact feedback, but their high cost and fragility have discouraged many researchers from adopting them in contact-rich tasks. To offer a more cost-efficient and easy-accessible source of contact feedback, we present ShapeForce, a low-cost, plug-and-play soft wrist that provides force-like signals for contact-rich robotic manipulation. Inspired by how humans rely on relative force changes in contact rather than precise force magnitudes, ShapeForce converts external force and torque into measurable deformations of its compliant core, which are then estimated via marker-based pose tracking and converted into force-like signals. Our design eliminates the need for calibration or specialized electronics to obtain exact values, and instead focuses on capturing force and torque changes sufficient for enabling contact-rich manipulation. Extensive experiments across diverse contact-rich tasks and manipulation policies demonstrate that ShapeForce delivers performance comparable to six-axis force-torque sensors at an extremely low cost.

