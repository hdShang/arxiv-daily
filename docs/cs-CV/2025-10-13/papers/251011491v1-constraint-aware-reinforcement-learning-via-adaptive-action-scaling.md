---
layout: default
title: Constraint-Aware Reinforcement Learning via Adaptive Action Scaling
---

# Constraint-Aware Reinforcement Learning via Adaptive Action Scaling

**arXiv**: [2510.11491v1](https://arxiv.org/abs/2510.11491) | [PDF](https://arxiv.org/pdf/2510.11491.pdf)

**作者**: Murad Dawood, Usama Ahmed Siddiquie, Shahram Khorshidi, Maren Bennewitz

---

## 💡 一句话要点

**提出自适应动作缩放方法以解决安全强化学习中的约束冲突问题**

**关键词**: `安全强化学习` `动作缩放` `约束优化` `模块化调节器` `稀疏成本`

## 📋 核心要点

1. 核心问题：现有方法因目标冲突或需先验知识，导致训练不稳定或约束违反
2. 方法要点：使用模块化成本感知调节器，平滑缩放动作以最小化约束违反
3. 实验效果：在Safety Gym任务中，约束违反减少126倍，回报提升超10倍

## 📄 摘要（原文）

> Safe reinforcement learning (RL) seeks to mitigate unsafe behaviors that
> arise from exploration during training by reducing constraint violations while
> maintaining task performance. Existing approaches typically rely on a single
> policy to jointly optimize reward and safety, which can cause instability due
> to conflicting objectives, or they use external safety filters that override
> actions and require prior system knowledge. In this paper, we propose a modular
> cost-aware regulator that scales the agent's actions based on predicted
> constraint violations, preserving exploration through smooth action modulation
> rather than overriding the policy. The regulator is trained to minimize
> constraint violations while avoiding degenerate suppression of actions. Our
> approach integrates seamlessly with off-policy RL methods such as SAC and TD3,
> and achieves state-of-the-art return-to-cost ratios on Safety Gym locomotion
> tasks with sparse costs, reducing constraint violations by up to 126 times
> while increasing returns by over an order of magnitude compared to prior
> methods.

