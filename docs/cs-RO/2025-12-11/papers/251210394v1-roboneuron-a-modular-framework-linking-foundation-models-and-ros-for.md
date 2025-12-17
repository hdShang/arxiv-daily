---
layout: default
title: RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI
---

# RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI

**arXiv**: [2512.10394v1](https://arxiv.org/abs/2512.10394) | [PDF](https://arxiv.org/pdf/2512.10394.pdf)

**作者**: Weifan Guan, Huasen Xi, Chenxiao Zhang, Aosheng Li, Qinghao Hu, Jian Cheng

---

## 💡 一句话要点

**提出RoboNeuron框架，通过集成大模型与ROS解决具身AI的工程障碍。**

**关键词**: `具身AI` `机器人操作系统` `大语言模型` `模块化框架` `模型上下文协议`

## 📋 核心要点

1. 当前具身AI系统存在跨场景适应性差、模块耦合度高和推理加速碎片化问题。
2. 利用MCP作为语义桥梁，实现LLM动态编排机器人工具，并基于ROS建立模块化架构。
3. 框架提升跨场景适应性和组件灵活性，为可扩展应用奠定基础。

## 📄 摘要（原文）

> Current embodied AI systems face severe engineering impediments, primarily characterized by poor cross-scenario adaptability, rigid inter-module coupling, and fragmented inference acceleration. To overcome these limitations, we propose RoboNeuron, a universal deployment framework for embodied intelligence. RoboNeuron is the first framework to deeply integrate the cognitive capabilities of Large Language Models (LLMs) and Vision-Language-Action (VLA) models with the real-time execution backbone of the Robot Operating System (ROS). We utilize the Model Context Protocol (MCP) as a semantic bridge, enabling the LLM to dynamically orchestrate underlying robotic tools. The framework establishes a highly modular architecture that strictly decouples sensing, reasoning, and control by leveraging ROS's unified communication interfaces. Crucially, we introduce an automated tool to translate ROS messages into callable MCP functions, significantly streamlining development. RoboNeuron significantly enhances cross-scenario adaptability and component flexibility, while establishing a systematic platform for horizontal performance benchmarking, laying a robust foundation for scalable real-world embodied applications.

