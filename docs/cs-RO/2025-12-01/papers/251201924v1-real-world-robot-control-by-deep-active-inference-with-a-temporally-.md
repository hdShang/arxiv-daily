---
layout: default
title: Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model
---

# Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model

**arXiv**: [2512.01924v1](https://arxiv.org/abs/2512.01924) | [PDF](https://arxiv.org/pdf/2512.01924.pdf)

**作者**: Kentaro Fujii, Shingo Murata

---

## 💡 一句话要点

**提出基于时间分层世界模型的深度主动推断框架，以解决真实机器人控制中的不确定性问题。**

**关键词**: `深度主动推断` `时间分层世界模型` `动作抽象` `机器人控制` `不确定性处理`

## 📋 核心要点

1. 核心问题：传统深度学习方法在不确定环境中忽视探索，导致控制困难。
2. 方法要点：构建包含世界模型、动作模型和抽象世界模型的框架，通过时间分层和动作压缩实现高效动作选择。
3. 实验或效果：在真实机器人物体操作任务中验证，实现高成功率并能在不确定设置中切换目标导向与探索动作。

## 📄 摘要（原文）

> Robots in uncertain real-world environments must perform both goal-directed and exploratory actions. However, most deep learning-based control methods neglect exploration and struggle under uncertainty. To address this, we adopt deep active inference, a framework that accounts for human goal-directed and exploratory actions. Yet, conventional deep active inference approaches face challenges due to limited environmental representation capacity and high computational cost in action selection. We propose a novel deep active inference framework that consists of a world model, an action model, and an abstract world model. The world model encodes environmental dynamics into hidden state representations at slow and fast timescales. The action model compresses action sequences into abstract actions using vector quantization, and the abstract world model predicts future slow states conditioned on the abstract action, enabling low-cost action selection. We evaluate the framework on object-manipulation tasks with a real-world robot. Results show that it achieves high success rates across diverse manipulation tasks and switches between goal-directed and exploratory actions in uncertain settings, while making action selection computationally tractable. These findings highlight the importance of modeling multiple timescale dynamics and abstracting actions and state transitions.

