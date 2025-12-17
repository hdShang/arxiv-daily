---
layout: default
title: Human-Centered Cooperative Control Coupling Autonomous and Haptic Shared Control via Control Barrier Function
---

# Human-Centered Cooperative Control Coupling Autonomous and Haptic Shared Control via Control Barrier Function

**arXiv**: [2511.19869v1](https://arxiv.org/abs/2511.19869) | [PDF](https://arxiv.org/pdf/2511.19869.pdf)

**作者**: Eito Sato, Takahiro Wada

---

## 💡 一句话要点

**提出人机协同控制框架，结合自主与触觉共享控制以提升遥操作性能**

**关键词**: `触觉共享控制` `控制屏障函数` `人机协同` `遥操作` `自主控制`

## 📋 核心要点

1. 核心问题：触觉共享控制受限于操纵杆和人体动力学，影响机器人行为
2. 方法要点：使用控制屏障函数实时忽略安全区域内操纵杆输入，耦合自主控制器
3. 实验或效果：虚拟环境实验显示精度提高、时间减少，优于传统方法

## 📄 摘要（原文）

> Haptic shared control (HSC) is effective in teleoperation when full autonomy is limited by uncertainty or sensing constraints. However, autonomous control performance achieved by maximizing HSC strength is limited because the dynamics of the joystick and human arm affect the robot's behavior. We propose a cooperative framework coupling a joystick-independent autonomous controller with HSC. A control barrier function ignores joystick inputs within a safe region determined by the human operator in real-time, while HSC is engaged otherwise. A pilot experiment on simulated tasks with tele-operated underwater robot in virtual environment demonstrated improved accuracy and reduced required time over conventional HSC.

