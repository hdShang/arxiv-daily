---
layout: default
title: Surrogate compliance modeling enables reinforcement learned locomotion gaits for soft robots
---

# Surrogate compliance modeling enables reinforcement learned locomotion gaits for soft robots

**arXiv**: [2512.07114v1](https://arxiv.org/abs/2512.07114) | [PDF](https://arxiv.org/pdf/2512.07114.pdf)

**作者**: Jue Wang, Mingsong Jiang, Luis A. Ramirez, Bilige Yang, Mujun Zhang, Esteban Figueroa, Wenzhong Yan, Rebecca Kramer-Bottiglio

---

## 💡 一句话要点

**提出代理柔顺建模方法，在刚体模拟中实现软机器人强化学习步态**

**关键词**: `软机器人` `强化学习` `模拟到现实` `柔顺建模` `步态控制` `多环境运动`

## 📋 核心要点

1. 软机器人模拟与控制面临精度与计算挑战，刚体模拟无法捕捉软材料动力学。
2. 引入间接变量表示软材料变形，在刚体模拟中通过强化学习训练步态策略。
3. 方法在硬件上实现高保真迁移，提升陆地机动性并显著降低运输成本。

## 📄 摘要（原文）

> Adaptive morphogenetic robots adapt their morphology and control policies to meet changing tasks and environmental conditions. Many such systems leverage soft components, which enable shape morphing but also introduce simulation and control challenges. Soft-body simulators remain limited in accuracy and computational tractability, while rigid-body simulators cannot capture soft-material dynamics. Here, we present a surrogate compliance modeling approach: rather than explicitly modeling soft-body physics, we introduce indirect variables representing soft-material deformation within a rigid-body simulator. We validate this approach using our amphibious robotic turtle, a quadruped with soft morphing limbs designed for multi-environment locomotion. By capturing deformation effects as changes in effective limb length and limb center of mass, and by applying reinforcement learning with extensive randomization of these indirect variables, we achieve reliable policy learning entirely in a rigid-body simulation. The resulting gaits transfer directly to hardware, demonstrating high-fidelity sim-to-real performance on hard, flat substrates and robust, though lower-fidelity, transfer on rheologically complex terrains. The learned closed-loop gaits exhibit unprecedented terrestrial maneuverability and achieve an order-of-magnitude reduction in cost of transport compared to open-loop baselines. Field experiments with the robot further demonstrate stable, multi-gait locomotion across diverse natural terrains, including gravel, grass, and mud.

