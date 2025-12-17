---
layout: default
title: LEO-RobotAgent: A General-purpose Robotic Agent for Language-driven Embodied Operator
---

# LEO-RobotAgent: A General-purpose Robotic Agent for Language-driven Embodied Operator

**arXiv**: [2512.10605v1](https://arxiv.org/abs/2512.10605) | [PDF](https://arxiv.org/pdf/2512.10605.pdf)

**作者**: Lihuang Chen, Xiangyu Luo, Jun Meng

---

## 💡 一句话要点

**提出LEO-RobotAgent框架，实现语言驱动多类型机器人完成复杂任务**

**关键词**: `语言驱动机器人` `通用智能体框架` `任务规划` `人机交互` `模块化工具集`

## 📋 核心要点

1. 核心问题：现有机器人任务规划研究多针对单任务单机器人，算法复杂且泛化性差
2. 方法要点：设计简洁框架，结合模块化工具集和人机交互机制，支持大模型自主规划与行动
3. 实验或效果：框架适配无人机、机械臂等主流平台，高效执行多复杂度任务

## 📄 摘要（原文）

> We propose LEO-RobotAgent, a general-purpose language-driven intelligent agent framework for robots. Under this framework, LLMs can operate different types of robots to complete unpredictable complex tasks across various scenarios. This framework features strong generalization, robustness, and efficiency. The application-level system built around it can fully enhance bidirectional human-robot intent understanding and lower the threshold for human-robot interaction. Regarding robot task planning, the vast majority of existing studies focus on the application of large models in single-task scenarios and for single robot types. These algorithms often have complex structures and lack generalizability. Thus, the proposed LEO-RobotAgent framework is designed with a streamlined structure as much as possible, enabling large models to independently think, plan, and act within this clear framework. We provide a modular and easily registrable toolset, allowing large models to flexibly call various tools to meet different requirements. Meanwhile, the framework incorporates a human-robot interaction mechanism, enabling the algorithm to collaborate with humans like a partner. Experiments have verified that this framework can be easily adapted to mainstream robot platforms including unmanned aerial vehicles (UAVs), robotic arms, and wheeled robot, and efficiently execute a variety of carefully designed tasks with different complexity levels. Our code is available at https://github.com/LegendLeoChen/LEO-RobotAgent.

