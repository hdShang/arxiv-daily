---
layout: default
title: Lie Group Control Architectures for UAVs: a Comparison of SE2(3)-Based Approaches in Simulation and Hardware
---

# Lie Group Control Architectures for UAVs: a Comparison of SE2(3)-Based Approaches in Simulation and Hardware

**arXiv**: [2511.15023v1](https://arxiv.org/abs/2511.15023) | [PDF](https://arxiv.org/pdf/2511.15023.pdf)

**作者**: Dimitria Silveria, Kleber Cabral, Peter Jardine, Sidney Givigi

---

## 💡 一句话要点

**提出SE2(3)模型预测控制器，用于四旋翼无人机控制，在仿真和硬件中验证性能。**

**关键词**: `李群控制` `模型预测控制` `四旋翼无人机` `轨迹跟踪` `SE2(3)控制器`

## 📋 核心要点

1. 核心问题：基于李群的无人机控制器在真实环境中的性能验证与比较。
2. 方法要点：结合SE2(3)几何性质与模型预测控制，处理约束并优化轨迹。
3. 实验或效果：在Quanser QDrone平台上测试，SE2(3) MPC在轨迹跟踪和鲁棒性上表现优越。

## 📄 摘要（原文）

> This paper presents the integration and experimental validation of advanced control strategies for quadcopters based on Lie groups. We build upon recent theoretical developments on SE2(3)-based controllers and introduce a novel SE2(3) model predictive controller (MPC) that combines the predictive capabilities and constraint-handling of optimal control with the geometric properties of Lie group formulations. We evaluated this MPC against a state-of-the-art SE2(3)-based LQR approach and obtained comparable performance in simulation. Both controllers where also deployed on the Quanser QDrone platform and compared to each other and an industry standard control architecture. Results show that the SE_2(3) MPC achieves superior trajectory tracking performance and robustness across a range of scenarios. This work demonstrates the practical effectiveness of Lie group-based controllers and offers comparative insights into their impact on system behaviour and real-time performance

