---
layout: default
title: Learning Spatiotemporal Tubes for Temporal Reach-Avoid-Stay Tasks using Physics-Informed Neural Networks
---

# Learning Spatiotemporal Tubes for Temporal Reach-Avoid-Stay Tasks using Physics-Informed Neural Networks

**arXiv**: [2512.08248v1](https://arxiv.org/abs/2512.08248) | [PDF](https://arxiv.org/pdf/2512.08248.pdf)

**作者**: Ahan Basu, Ratnangshu Das, Pushpak Jagtap

---

## 💡 一句话要点

**提出基于时空管的控制框架，利用物理信息神经网络满足未知非线性系统的时间到达-避障-停留任务。**

**关键词**: `时空管控制` `物理信息神经网络` `非线性系统控制` `时间到达-避障-停留任务` `形式验证`

## 📋 核心要点

1. 针对未知动态的控制仿射非线性系统，在外部扰动下满足时间到达-避障-停留任务。
2. 使用物理信息神经网络近似时空管的中心和半径，通过损失函数和训练算法最小化约束违反。
3. 通过移动机器人和飞行器案例验证框架的有效性和可扩展性。

## 📄 摘要（原文）

> This paper presents a Spatiotemporal Tube (STT)-based control framework for general control-affine MIMO nonlinear pure-feedback systems with unknown dynamics to satisfy prescribed time reach-avoid-stay tasks under external disturbances. The STT is defined as a time-varying ball, whose center and radius are jointly approximated by a Physics-Informed Neural Network (PINN). The constraints governing the STT are first formulated as loss functions of the PINN, and a training algorithm is proposed to minimize the overall violation. The PINN being trained on certain collocation points, we propose a Lipschitz-based validity condition to formally verify that the learned PINN satisfies the conditions over the continuous time horizon. Building on the learned STT representation, an approximation-free closed-form controller is defined to guarantee satisfaction of the T-RAS specification. Finally, the effectiveness and scalability of the framework are validated through two case studies involving a mobile robot and an aerial vehicle navigating through cluttered environments.

