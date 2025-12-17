---
layout: default
title: Model-Based Lookahead Reinforcement Learning for in-hand manipulation
---

# Model-Based Lookahead Reinforcement Learning for in-hand manipulation

**arXiv**: [2510.08884v1](https://arxiv.org/abs/2510.08884) | [PDF](https://arxiv.org/pdf/2510.08884.pdf)

**作者**: Alexandre Lopes, Catarina Barata, Plinio Moreno

---

## 💡 一句话要点

**提出混合强化学习框架以提升机器人灵巧操作性能**

**关键词**: `强化学习` `灵巧操作` `模型预测控制` `机器人仿真` `动态模型`

## 📋 核心要点

1. 核心问题：机器人灵巧操作任务复杂，涉及动态系统与多对象控制挑战。
2. 方法要点：结合无模型与基于模型的强化学习，通过轨迹评估指导策略。
3. 实验或效果：在模拟手部测试中，多数情况下性能提升，但计算成本增加。

## 📄 摘要（原文）

> In-Hand Manipulation, as many other dexterous tasks, remains a difficult
> challenge in robotics by combining complex dynamic systems with the capability
> to control and manoeuvre various objects using its actuators. This work
> presents the application of a previously developed hybrid Reinforcement
> Learning (RL) Framework to In-Hand Manipulation task, verifying that it is
> capable of improving the performance of the task. The model combines concepts
> of both Model-Free and Model-Based Reinforcement Learning, by guiding a trained
> policy with the help of a dynamic model and value-function through trajectory
> evaluation, as done in Model Predictive Control. This work evaluates the
> performance of the model by comparing it with the policy that will be guided.
> To fully explore this, various tests are performed using both fully-actuated
> and under-actuated simulated robotic hands to manipulate different objects for
> a given task. The performance of the model will also be tested for
> generalization tests, by changing the properties of the objects in which both
> the policy and dynamic model were trained, such as density and size, and
> additionally by guiding a trained policy in a certain object to perform the
> same task in a different one. The results of this work show that, given a
> policy with high average reward and an accurate dynamic model, the hybrid
> framework improves the performance of in-hand manipulation tasks for most test
> cases, even when the object properties are changed. However, this improvement
> comes at the expense of increasing the computational cost, due to the
> complexity of trajectory evaluation.

