---
layout: default
title: End-to-End Design and Validation of a Low-Cost Stewart Platform with Nonlinear Estimation and Control
---

# End-to-End Design and Validation of a Low-Cost Stewart Platform with Nonlinear Estimation and Control

**arXiv**: [2510.22949v1](https://arxiv.org/abs/2510.22949) | [PDF](https://arxiv.org/pdf/2510.22949.pdf)

**作者**: Benedictus C. G. Cinun, Tua A. Tamba, Immanuel R. Santjoko, Xiaofeng Wang, Michael A. Gunarso, Bin Hu

---

## 💡 一句话要点

**提出低成本Stewart平台，结合非线性估计与控制，用于研究和教育。**

**关键词**: `Stewart平台` `非线性控制` `状态估计` `低成本机器人` `实时控制`

## 📋 核心要点

1. 核心问题：开发低成本六自由度Stewart平台，作为研究和教育测试平台。
2. 方法要点：集成反馈线性化与LQR控制，使用扩展卡尔曼滤波融合IMU和编码器数据。
3. 实验或效果：通过仿真和实验验证轨迹跟踪和状态估计，展示平台成本效益和多功能性。

## 📄 摘要（原文）

> This paper presents the complete design, control, and experimental validation
> of a low-cost Stewart platform prototype developed as an affordable yet capable
> robotic testbed for research and education. The platform combines off the shelf
> components with 3D printed and custom fabricated parts to deliver full six
> degrees of freedom motions using six linear actuators connecting a moving
> platform to a fixed base. The system software integrates dynamic modeling, data
> acquisition, and real time control within a unified framework. A robust
> trajectory tracking controller based on feedback linearization, augmented with
> an LQR scheme, compensates for the platform's nonlinear dynamics to achieve
> precise motion control. In parallel, an Extended Kalman Filter fuses IMU and
> actuator encoder feedback to provide accurate and reliable state estimation
> under sensor noise and external disturbances. Unlike prior efforts that
> emphasize only isolated aspects such as modeling or control, this work delivers
> a complete hardware-software platform validated through both simulation and
> experiments on static and dynamic trajectories. Results demonstrate effective
> trajectory tracking and real-time state estimation, highlighting the platform's
> potential as a cost effective and versatile tool for advanced research and
> educational applications.

