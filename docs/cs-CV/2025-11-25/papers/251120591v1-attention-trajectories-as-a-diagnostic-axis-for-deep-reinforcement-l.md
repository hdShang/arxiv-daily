---
layout: default
title: Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning
---

# Attention Trajectories as a Diagnostic Axis for Deep Reinforcement Learning

**arXiv**: [2511.20591v1](https://arxiv.org/abs/2511.20591) | [PDF](https://arxiv.org/pdf/2511.20591.pdf)

**作者**: Charlotte Beylier, Hannah Selder, Arthur Fleig, Simon M. Hofmann, Nico Scherf

---

## 💡 一句话要点

**提出注意力导向指标以分析强化学习代理在训练中的注意力发展。**

**关键词**: `强化学习` `注意力机制` `学习过程分析` `行为评估` `游戏实验`

## 📋 核心要点

1. 核心问题：强化学习代理的学习过程难以理解，超越算法数学公式。
2. 方法要点：引入注意力导向指标，监控代理注意力模式在训练中的演变。
3. 实验或效果：在Pong游戏变体实验中，指标成功区分注意力模式并关联行为差异。

## 📄 摘要（原文）

> The learning process of a reinforcement learning (RL) agent remains poorly understood beyond the mathematical formulation of its learning algorithm. To address this gap, we introduce attention-oriented metrics (ATOMs) to investigate the development of an RL agent's attention during training. In a controlled experiment, we tested ATOMs on three variations of a Pong game, each designed to teach the agent distinct behaviours, complemented by a behavioural assessment. ATOMs successfully delineate the attention patterns of an agent trained on each game variation, and that these differences in attention patterns translate into differences in the agent's behaviour. Through continuous monitoring of ATOMs during training, we observed that the agent's attention developed in phases, and that these phases were consistent across game variations. Overall, we believe that ATOM could help improve our understanding of the learning processes of RL agents and better understand the relationship between attention and learning.

