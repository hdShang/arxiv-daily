---
layout: default
title: Agile Flight Emerges from Multi-Agent Competitive Racing
---

# Agile Flight Emerges from Multi-Agent Competitive Racing

**arXiv**: [2512.11781v1](https://arxiv.org/abs/2512.11781) | [PDF](https://arxiv.org/pdf/2512.11781.pdf)

**作者**: Vineet Pasumarti, Lorenzo Bianchi, Antonio Loquercio

---

## 💡 一句话要点

**提出多智能体竞争强化学习以训练无人机实现敏捷飞行与策略，超越单智能体训练范式。**

**关键词**: `多智能体强化学习` `敏捷飞行` `仿真到真实迁移` `无人机控制` `竞争训练` `稀疏奖励`

## 📋 核心要点

1. 核心问题：传统单智能体训练依赖行为奖励，难以在复杂环境中实现高效敏捷飞行与策略。
2. 方法要点：通过多智能体竞争和稀疏高层目标（赢得比赛），训练强化学习智能体，无需详细行为奖励。
3. 实验或效果：在仿真和真实世界中验证，多智能体方法在复杂环境、仿真到真实迁移和泛化性方面表现更优。

## 📄 摘要（原文）

> Through multi-agent competition and the sparse high-level objective of winning a race, we find that both agile flight (e.g., high-speed motion pushing the platform to its physical limits) and strategy (e.g., overtaking or blocking) emerge from agents trained with reinforcement learning. We provide evidence in both simulation and the real world that this approach outperforms the common paradigm of training agents in isolation with rewards that prescribe behavior, e.g., progress on the raceline, in particular when the complexity of the environment increases, e.g., in the presence of obstacles. Moreover, we find that multi-agent competition yields policies that transfer more reliably to the real world than policies trained with a single-agent progress-based reward, despite the two methods using the same simulation environment, randomization strategy, and hardware. In addition to improved sim-to-real transfer, the multi-agent policies also exhibit some degree of generalization to opponents unseen at training time. Overall, our work, following in the tradition of multi-agent competitive game-play in digital domains, shows that sparse task-level rewards are sufficient for training agents capable of advanced low-level control in the physical world.
>   Code: https://github.com/Jirl-upenn/AgileFlight_MultiAgent

