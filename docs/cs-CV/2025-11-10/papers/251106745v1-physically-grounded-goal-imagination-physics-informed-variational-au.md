---
layout: default
title: Physically-Grounded Goal Imagination: Physics-Informed Variational Autoencoder for Self-Supervised Reinforcement Learning
---

# Physically-Grounded Goal Imagination: Physics-Informed Variational Autoencoder for Self-Supervised Reinforcement Learning

**arXiv**: [2511.06745v1](https://arxiv.org/abs/2511.06745) | [PDF](https://arxiv.org/pdf/2511.06745.pdf)

**作者**: Lan Thi Ha Nguyen, Kien Ton Manh, Anh Do Duc, Nam Pham Hai

---

## 💡 一句话要点

**提出物理信息变分自编码器以解决机器人自监督强化学习中的目标生成问题**

**关键词**: `自监督强化学习` `变分自编码器` `物理约束` `目标生成` `机器人操作`

## 📋 核心要点

1. 核心问题：现有方法生成物理不可行目标，影响学习效率
2. 方法要点：分离潜在空间，施加物理约束确保目标可行性
3. 实验或效果：在视觉机器人操作任务中提升探索和技能获取效果

## 📄 摘要（原文）

> Self-supervised goal-conditioned reinforcement learning enables robots to
> autonomously acquire diverse skills without human supervision. However, a
> central challenge is the goal setting problem: robots must propose feasible and
> diverse goals that are achievable in their current environment. Existing
> methods like RIG (Visual Reinforcement Learning with Imagined Goals) use
> variational autoencoder (VAE) to generate goals in a learned latent space but
> have the limitation of producing physically implausible goals that hinder
> learning efficiency. We propose Physics-Informed RIG (PI-RIG), which integrates
> physical constraints directly into the VAE training process through a novel
> Enhanced Physics-Informed Variational Autoencoder (Enhanced p3-VAE), enabling
> the generation of physically consistent and achievable goals. Our key
> innovation is the explicit separation of the latent space into physics
> variables governing object dynamics and environmental factors capturing visual
> appearance, while enforcing physical consistency through differential equation
> constraints and conservation laws. This enables the generation of physically
> consistent and achievable goals that respect fundamental physical principles
> such as object permanence, collision constraints, and dynamic feasibility.
> Through extensive experiments, we demonstrate that this physics-informed goal
> generation significantly improves the quality of proposed goals, leading to
> more effective exploration and better skill acquisition in visual robotic
> manipulation tasks including reaching, pushing, and pick-and-place scenarios.

