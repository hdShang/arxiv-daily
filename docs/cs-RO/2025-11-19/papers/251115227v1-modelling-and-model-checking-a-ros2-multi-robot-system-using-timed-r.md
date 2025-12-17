---
layout: default
title: Modelling and Model-Checking a ROS2 Multi-Robot System using Timed Rebeca
---

# Modelling and Model-Checking a ROS2 Multi-Robot System using Timed Rebeca

**arXiv**: [2511.15227v1](https://arxiv.org/abs/2511.15227) | [PDF](https://arxiv.org/pdf/2511.15227.pdf)

**作者**: Hiep Hong Trinh, Marjan Sirjani, Federico Ciccozzi, Abu Naser Masud, Mikael Sjödin

---

## 💡 一句话要点

**提出使用Timed Rebeca建模和模型检查ROS2多机器人系统的方法**

**关键词**: `多机器人系统` `模型检查` `Timed Rebeca` `ROS2` `离散化策略` `形式验证`

## 📋 核心要点

1. 核心问题：多机器人系统异步交互和并发复杂性，离散模型与连续系统间的差距。
2. 方法要点：开发离散化策略和优化技术，使用Timed Rebeca语言建模ROS2节点和定时行为。
3. 实验或效果：实现高效模型检查，验证系统属性，并展示模型与实现间的工程流程。

## 📄 摘要（原文）

> Model-based development enables quicker prototyping, earlier experimentation and validation of design intents. For a multi-agent system with complex asynchronous interactions and concurrency, formal verification, model-checking in particular, offers an automated mechanism for verifying desired properties. Timed Rebeca is an actor-based modelling language supporting reactive, concurrent and time semantics, accompanied with a model-checking compiler. These capabilities allow using Timed Rebeca to correctly model ROS2 node topographies, recurring physical signals, motion primitives and other timed and time-convertible behaviors. The biggest challenges in modelling and verifying a multi-robot system lie in abstracting complex information, bridging the gap between a discrete model and a continuous system and compacting the state space, while maintaining the model's accuracy. We develop different discretization strategies for different kinds of information, identifying the 'enough' thresholds of abstraction, and applying efficient optimization techniques to boost computations. With this work we demonstrate how to use models to design and verify a multi-robot system, how to discretely model a continuous system to do model-checking efficiently, and the round-trip engineering flow between the model and the implementation. The released Rebeca and ROS2 codes can serve as a foundation for modelling multiple autonomous robots systems.

