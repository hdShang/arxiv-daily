---
layout: default
title: SADCHER: Scheduling using Attention-based Dynamic Coalitions of Heterogeneous Robots in Real-Time
---

# SADCHER: Scheduling using Attention-based Dynamic Coalitions of Heterogeneous Robots in Real-Time

**arXiv**: [2510.14851v1](https://arxiv.org/abs/2510.14851) | [PDF](https://arxiv.org/pdf/2510.14851.pdf)

**作者**: Jakob Bichler, Andreu Matoses Gimenez, Javier Alonso-Mora

---

## 💡 一句话要点

**提出SADCHER框架，用于异构多机器人实时任务分配，结合动态联盟与任务优先级约束。**

**关键词**: `异构多机器人系统` `实时任务分配` `动态联盟形成` `图注意力网络` `模仿学习` `可扩展调度`

## 📋 核心要点

1. 核心问题：异构多机器人团队在实时环境中的任务分配，需处理动态联盟和任务优先级约束。
2. 方法要点：使用模仿学习训练，结合图注意力和变换器预测奖励，并通过松弛二分匹配生成可行调度。
3. 实验或效果：在随机未见问题上优于其他方法，计算时间适合实时操作，并评估了可扩展性。

## 📄 摘要（原文）

> We present Sadcher, a real-time task assignment framework for heterogeneous
> multi-robot teams that incorporates dynamic coalition formation and task
> precedence constraints. Sadcher is trained through Imitation Learning and
> combines graph attention and transformers to predict assignment rewards between
> robots and tasks. Based on the predicted rewards, a relaxed bipartite matching
> step generates high-quality schedules with feasibility guarantees. We
> explicitly model robot and task positions, task durations, and robots'
> remaining processing times, enabling advanced temporal and spatial reasoning
> and generalization to environments with different spatiotemporal distributions
> compared to training. Trained on optimally solved small-scale instances, our
> method can scale to larger task sets and team sizes. Sadcher outperforms other
> learning-based and heuristic baselines on randomized, unseen problems for small
> and medium-sized teams with computation times suitable for real-time operation.
> We also explore sampling-based variants and evaluate scalability across robot
> and task counts. In addition, we release our dataset of 250,000 optimal
> schedules: https://autonomousrobots.nl/paper_websites/sadcher_MRTA/

