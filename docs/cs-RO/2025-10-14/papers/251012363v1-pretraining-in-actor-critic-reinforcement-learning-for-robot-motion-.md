---
layout: default
title: Pretraining in Actor-Critic Reinforcement Learning for Robot Motion Control
---

# Pretraining in Actor-Critic Reinforcement Learning for Robot Motion Control

**arXiv**: [2510.12363v1](https://arxiv.org/abs/2510.12363) | [PDF](https://arxiv.org/pdf/2510.12363.pdf)

**作者**: Jiale Fan, Andrei Cramariuc, Tifanny Portela, Marco Hutter

---

## 💡 一句话要点

**提出基于预训练的演员-评论家强化学习方法，以提升机器人运动控制的样本效率和性能**

**关键词**: `强化学习` `机器人运动控制` `预训练` `演员-评论家算法` `样本效率` `PIDM模型`

## 📋 核心要点

1. 核心问题：机器人运动控制中强化学习常从零开始学习，缺乏跨任务通用知识共享。
2. 方法要点：通过任务无关探索收集数据，训练PIDM模型，预训练权重用于初始化演员-评论家网络。
3. 实验或效果：在七项任务中，样本效率平均提升40.1%，任务性能平均提升7.5%。

## 📄 摘要（原文）

> The pretraining-finetuning paradigm has facilitated numerous transformative
> advancements in artificial intelligence research in recent years. However, in
> the domain of reinforcement learning (RL) for robot motion control, individual
> skills are often learned from scratch despite the high likelihood that some
> generalizable knowledge is shared across all task-specific policies belonging
> to a single robot embodiment. This work aims to define a paradigm for
> pretraining neural network models that encapsulate such knowledge and can
> subsequently serve as a basis for warm-starting the RL process in classic
> actor-critic algorithms, such as Proximal Policy Optimization (PPO). We begin
> with a task-agnostic exploration-based data collection algorithm to gather
> diverse, dynamic transition data, which is then used to train a Proprioceptive
> Inverse Dynamics Model (PIDM) through supervised learning. The pretrained
> weights are loaded into both the actor and critic networks to warm-start the
> policy optimization of actual tasks. We systematically validated our proposed
> method on seven distinct robot motion control tasks, showing significant
> benefits to this initialization strategy. Our proposed approach on average
> improves sample efficiency by 40.1% and task performance by 7.5%, compared to
> random initialization. We further present key ablation studies and empirical
> analyses that shed light on the mechanisms behind the effectiveness of our
> method.

