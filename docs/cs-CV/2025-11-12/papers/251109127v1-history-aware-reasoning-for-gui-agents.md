---
layout: default
title: History-Aware Reasoning for GUI Agents
---

# History-Aware Reasoning for GUI Agents

**arXiv**: [2511.09127v1](https://arxiv.org/abs/2511.09127) | [PDF](https://arxiv.org/pdf/2511.09127.pdf)

**作者**: Ziwei Wang, Leyang Yang, Xiaoxuan Tang, Sheng Zhou, Dajun Chen, Wei Jiang, Yong Li

---

## 💡 一句话要点

**提出历史感知推理框架以增强GUI代理在长视野任务中的短期记忆**

**关键词**: `GUI自动化` `历史感知推理` `强化学习` `短期记忆增强` `反思学习` `端到端模型`

## 📋 核心要点

1. 核心问题：现有GUI代理在显式推理中短期记忆弱，忽视历史交互，影响自动化性能。
2. 方法要点：构建反思学习场景、合成定制校正指南、设计混合RL奖励函数。
3. 实验或效果：在多个GUI基准测试中验证方法的有效性和泛化能力。

## 📄 摘要（原文）

> Advances in Multimodal Large Language Models have significantly enhanced Graphical User Interface (GUI) automation. Equipping GUI agents with reliable episodic reasoning capabilities is essential for bridging the gap between users' concise task descriptions and the complexities of real-world execution. Current methods integrate Reinforcement Learning (RL) with System-2 Chain-of-Thought, yielding notable gains in reasoning enhancement. For long-horizon GUI tasks, historical interactions connect each screen to the goal-oriented episode chain, and effectively leveraging these clues is crucial for the current decision. However, existing native GUI agents exhibit weak short-term memory in their explicit reasoning, interpreting the chained interactions as discrete screen understanding, i.e., unawareness of the historical interactions within the episode. This history-agnostic reasoning challenges their performance in GUI automation. To alleviate this weakness, we propose a History-Aware Reasoning (HAR) framework, which encourages an agent to reflect on its own errors and acquire episodic reasoning knowledge from them via tailored strategies that enhance short-term memory in long-horizon interaction. The framework mainly comprises constructing a reflective learning scenario, synthesizing tailored correction guidelines, and designing a hybrid RL reward function. Using the HAR framework, we develop a native end-to-end model, HAR-GUI-3B, which alters the inherent reasoning mode from history-agnostic to history-aware, equipping the GUI agent with stable short-term memory and reliable perception of screen details. Comprehensive evaluations across a range of GUI-related benchmarks demonstrate the effectiveness and generalization of our method.

