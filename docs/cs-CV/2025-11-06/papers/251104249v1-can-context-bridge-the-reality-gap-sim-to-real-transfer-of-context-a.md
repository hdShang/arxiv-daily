---
layout: default
title: Can Context Bridge the Reality Gap? Sim-to-Real Transfer of Context-Aware Policies
---

# Can Context Bridge the Reality Gap? Sim-to-Real Transfer of Context-Aware Policies

**arXiv**: [2511.04249v1](https://arxiv.org/abs/2511.04249) | [PDF](https://arxiv.org/pdf/2511.04249.pdf)

**作者**: Marco Iannotta, Yuxuan Yang, Johannes A. Stork, Erik Schaffernicht, Todor Stoyanov

---

## 💡 一句话要点

**提出上下文感知策略以改进机器人强化学习的模拟到现实迁移**

**关键词**: `模拟到现实迁移` `上下文感知策略` `领域随机化` `强化学习` `机器人控制`

## 📋 核心要点

1. 模拟到现实迁移因环境动态差异导致策略泛化失败
2. 集成上下文估计模块，基于动态参数条件化策略
3. 在控制基准和真实机器人任务中优于上下文无关基线

## 📄 摘要（原文）

> Sim-to-real transfer remains a major challenge in reinforcement learning (RL)
> for robotics, as policies trained in simulation often fail to generalize to the
> real world due to discrepancies in environment dynamics. Domain Randomization
> (DR) mitigates this issue by exposing the policy to a wide range of randomized
> dynamics during training, yet leading to a reduction in performance. While
> standard approaches typically train policies agnostic to these variations, we
> investigate whether sim-to-real transfer can be improved by conditioning the
> policy on an estimate of the dynamics parameters -- referred to as context. To
> this end, we integrate a context estimation module into a DR-based RL framework
> and systematically compare SOTA supervision strategies. We evaluate the
> resulting context-aware policies in both a canonical control benchmark and a
> real-world pushing task using a Franka Emika Panda robot. Results show that
> context-aware policies outperform the context-agnostic baseline across all
> settings, although the best supervision strategy depends on the task.

