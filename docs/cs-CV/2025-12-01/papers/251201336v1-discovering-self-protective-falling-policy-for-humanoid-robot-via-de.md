---
layout: default
title: Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning
---

# Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning

**arXiv**: [2512.01336v1](https://arxiv.org/abs/2512.01336) | [PDF](https://arxiv.org/pdf/2512.01336.pdf)

**作者**: Diyuan Shi, Shangke Lyu, Donglin Wang

---

## 💡 一句话要点

**提出基于深度强化学习和课程学习的人形机器人自保护摔倒策略，以减少硬件损伤。**

**关键词**: `人形机器人` `深度强化学习` `摔倒保护` `课程学习` `策略迁移`

## 📋 核心要点

1. 核心问题：人形机器人因形态和动力学易摔倒，失控摔倒可能导致严重硬件损坏。
2. 方法要点：使用深度强化学习和课程学习，设计奖励函数和领域多样化课程，探索自保护行为。
3. 实验或效果：发现形成三角形结构可显著减少损伤，通过实验量化性能并成功迁移到真实平台。

## 📄 摘要（原文）

> Humanoid robots have received significant research interests and advancements in recent years. Despite many successes, due to their morphology, dynamics and limitation of control policy, humanoid robots are prone to fall as compared to other embodiments like quadruped or wheeled robots. And its large weight, tall Center of Mass, high Degree-of-Freedom would cause serious hardware damages when falling uncontrolled, to both itself and surrounding objects. Existing researches in this field mostly focus on using control based methods that struggle to cater diverse falling scenarios and may introduce unsuitable human prior. On the other hand, large-scale Deep Reinforcement Learning and Curriculum Learning could be employed to incentivize humanoid agent discovering falling protection policy that fits its own nature and property. In this work, with carefully designed reward functions and domain diversification curriculum, we successfully train humanoid agent to explore falling protection behaviors and discover that by forming a `triangle' structure, the falling damages could be significantly reduced with its rigid-material body. With comprehensive metrics and experiments, we quantify its performance with comparison to other methods, visualize its falling behaviors and successfully transfer it to real world platform.

