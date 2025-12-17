---
layout: default
title: Coordinated Strategies in Realistic Air Combat by Hierarchical Multi-Agent Reinforcement Learning
---

# Coordinated Strategies in Realistic Air Combat by Hierarchical Multi-Agent Reinforcement Learning

**arXiv**: [2510.11474v1](https://arxiv.org/abs/2510.11474) | [PDF](https://arxiv.org/pdf/2510.11474.pdf)

**作者**: Ardian Selmonaj, Giacomo Del Rio, Adrian Schneider, Alessandro Antonucci

---

## 💡 一句话要点

**提出分层多智能体强化学习框架以解决真实空战模拟中的复杂决策问题**

**关键词**: `分层强化学习` `多智能体系统` `空战模拟` `课程学习` `联盟训练`

## 📋 核心要点

1. 核心问题：真实空战模拟中，不完美态势感知和非线性飞行动力学使任务目标达成困难。
2. 方法要点：采用分层决策，低层学习精确控制，高层基于任务目标发布战术命令。
3. 实验或效果：实证显示，该方法在复杂狗斗场景中提升学习效率和战斗性能。

## 📄 摘要（原文）

> Achieving mission objectives in a realistic simulation of aerial combat is
> highly challenging due to imperfect situational awareness and nonlinear flight
> dynamics. In this work, we introduce a novel 3D multi-agent air combat
> environment and a Hierarchical Multi-Agent Reinforcement Learning framework to
> tackle these challenges. Our approach combines heterogeneous agent dynamics,
> curriculum learning, league-play, and a newly adapted training algorithm. To
> this end, the decision-making process is organized into two abstraction levels:
> low-level policies learn precise control maneuvers, while high-level policies
> issue tactical commands based on mission objectives. Empirical results show
> that our hierarchical approach improves both learning efficiency and combat
> performance in complex dogfight scenarios.

