---
layout: default
title: Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion
---

# Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion

**arXiv**: [2510.14947v1](https://arxiv.org/abs/2510.14947) | [PDF](https://arxiv.org/pdf/2510.14947.pdf)

**作者**: Blake Werner, Lizhi Yang, Aaron D. Ames

---

## 💡 一句话要点

**提出分层控制架构以提升人形机器人在非结构化环境中的鲁棒运动能力**

**关键词**: `人形机器人运动` `分层控制架构` `鲁棒性` `感知策略` `训练课程`

## 📋 核心要点

1. 核心问题：人形机器人在非结构化环境中需要平衡快速低层稳定与慢速感知决策
2. 方法要点：采用分层控制架构，结合高速本体感知稳定器和低速感知策略
3. 实验或效果：在仿真和硬件上优于单阶段策略，成功应对楼梯和边缘任务

## 📄 摘要（原文）

> Robust humanoid locomotion in unstructured environments requires
> architectures that balance fast low-level stabilization with slower perceptual
> decision-making. We show that a simple layered control architecture (LCA), a
> proprioceptive stabilizer running at high rate, coupled with a compact low-rate
> perceptual policy, enables substantially more robust performance than
> monolithic end-to-end designs, even when using minimal perception encoders.
> Through a two-stage training curriculum (blind stabilizer pretraining followed
> by perceptual fine-tuning), we demonstrate that layered policies consistently
> outperform one-stage alternatives in both simulation and hardware. On a Unitree
> G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage
> perceptual policies fail. These results highlight that architectural separation
> of timescales, rather than network scale or complexity, is the key enabler for
> robust perception-conditioned locomotion.

