---
layout: default
title: vEDGAR - Can CARLA Do HiL?
---

# vEDGAR - Can CARLA Do HiL?

**arXiv**: [2512.08541v1](https://arxiv.org/abs/2512.08541) | [PDF](https://arxiv.org/pdf/2512.08541.pdf)

**作者**: Nils Gehrke, David Brecht, Dominik Kulmer, Dheer Patel, Frank Diermeyer

---

## 💡 一句话要点

**提出vEDGAR框架以评估CARLA在硬件在环测试中的适用性**

**关键词**: `硬件在环测试` `自动驾驶仿真` `CARLA扩展` `实时仿真` `开源框架`

## 📋 核心要点

1. 核心问题：CARLA缺乏实时全传感器与执行器堆栈的硬件在环测试能力
2. 方法要点：基于需求推导，设计并实现vEDGAR仿真架构，集成专用硬件
3. 实验或效果：评估vEDGAR软件，得出CARLA用于自动驾驶硬件在环测试的适用性结论

## 📄 摘要（原文）

> Simulation offers advantages throughout the development process of automated driving functions, both in research and product development. Common open-source simulators like CARLA are extensively used in training, evaluation, and software-in-the-loop testing of new automated driving algorithms. However, the CARLA simulator lacks an evaluation where research and automated driving vehicles are simulated with their entire sensor and actuation stack in real time. The goal of this work is therefore to create a simulation framework for testing the automation software on its dedicated hardware and identifying its limits. Achieving this goal would greatly benefit the open-source development workflow of automated driving functions, designating CARLA as a consistent evaluation tool along the entire development process. To achieve this goal, in a first step, requirements are derived, and a simulation architecture is specified and implemented. Based on the formulated requirements, the proposed vEDGAR software is evaluated, resulting in a final conclusion on the applicability of CARLA for HiL testing of automated vehicles. The tool is available open source: Modified CARLA fork: https://github.com/TUMFTM/carla, vEDGAR Framework: https://github.com/TUMFTM/vEDGAR

