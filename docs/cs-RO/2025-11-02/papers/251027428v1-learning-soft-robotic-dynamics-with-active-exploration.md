---
layout: default
title: Learning Soft Robotic Dynamics with Active Exploration
---

# Learning Soft Robotic Dynamics with Active Exploration

**arXiv**: [2510.27428v1](https://arxiv.org/abs/2510.27428) | [PDF](https://arxiv.org/pdf/2510.27428.pdf)

**作者**: Hehui Zheng, Bhavya Sukhija, Chenhao Li, Klemens Iten, Andreas Krause, Robert K. Katzschmann

---

## 💡 一句话要点

**提出SoftAE框架以解决软体机器人动力学建模困难问题**

**关键词**: `软体机器人` `主动探索` `动力学建模` `不确定性估计` `零样本控制`

## 📋 核心要点

1. 软体机器人动力学高维非线性，现有数据驱动方法泛化性差
2. 采用概率集成模型估计不确定性，主动探索状态-动作空间未覆盖区域
3. 在仿真和真实平台上验证，模型更准确，零样本控制性能优越

## 📄 摘要（原文）

> Soft robots offer unmatched adaptability and safety in unstructured
> environments, yet their compliant, high-dimensional, and nonlinear dynamics
> make modeling for control notoriously difficult. Existing data-driven
> approaches often fail to generalize, constrained by narrowly focused task
> demonstrations or inefficient random exploration. We introduce SoftAE, an
> uncertainty-aware active exploration framework that autonomously learns
> task-agnostic and generalizable dynamics models of soft robotic systems. SoftAE
> employs probabilistic ensemble models to estimate epistemic uncertainty and
> actively guides exploration toward underrepresented regions of the state-action
> space, achieving efficient coverage of diverse behaviors without task-specific
> supervision. We evaluate SoftAE on three simulated soft robotic platforms -- a
> continuum arm, an articulated fish in fluid, and a musculoskeletal leg with
> hybrid actuation -- and on a pneumatically actuated continuum soft arm in the
> real world. Compared with random exploration and task-specific model-based
> reinforcement learning, SoftAE produces more accurate dynamics models, enables
> superior zero-shot control on unseen tasks, and maintains robustness under
> sensing noise, actuation delays, and nonlinear material effects. These results
> demonstrate that uncertainty-driven active exploration can yield scalable,
> reusable dynamics models across diverse soft robotic morphologies, representing
> a step toward more autonomous, adaptable, and data-efficient control in
> compliant robots.

