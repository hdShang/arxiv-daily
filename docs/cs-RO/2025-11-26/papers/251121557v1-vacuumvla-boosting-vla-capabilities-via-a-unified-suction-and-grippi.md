---
layout: default
title: VacuumVLA: Boosting VLA Capabilities via a Unified Suction and Gripping Tool for Complex Robotic Manipulation
---

# VacuumVLA: Boosting VLA Capabilities via a Unified Suction and Gripping Tool for Complex Robotic Manipulation

**arXiv**: [2511.21557v1](https://arxiv.org/abs/2511.21557) | [PDF](https://arxiv.org/pdf/2511.21557.pdf)

**作者**: Hui Zhou, Siyuan Huang, Minxing Li, Hao Zhang, Lue Fan, Shaoshuai Shi

---

## 💡 一句话要点

**提出集成吸盘与夹爪的混合末端执行器，以扩展VLA模型在复杂机器人操作中的任务范围。**

**关键词**: `机器人操作` `混合末端执行器` `视觉语言动作模型` `硬件设计` `任务扩展`

## 📋 核心要点

1. 核心问题：传统两指夹爪在擦拭玻璃或无把手抽屉等任务中接触面积不足或缺乏粘附力。
2. 方法要点：设计低成本硬件，结合机械夹爪与真空吸盘，支持双模式灵活切换或协同使用。
3. 实验或效果：在DexVLA和Pi0框架中验证，机器人能完成传统夹爪无法实现的复杂任务。

## 📄 摘要（原文）

> Vision Language Action models have significantly advanced general purpose robotic manipulation by harnessing large scale pretrained vision and language representations. Among existing approaches, a majority of current VLA systems employ parallel two finger grippers as their default end effectors. However, such grippers face inherent limitations in handling certain real world tasks such as wiping glass surfaces or opening drawers without handles due to insufficient contact area or lack of adhesion. To overcome these challenges, we present a low cost, integrated hardware design that combines a mechanical two finger gripper with a vacuum suction unit, enabling dual mode manipulation within a single end effector. Our system supports flexible switching or synergistic use of both modalities, expanding the range of feasible tasks. We validate the efficiency and practicality of our design within two state of the art VLA frameworks: DexVLA and Pi0. Experimental results demonstrate that with the proposed hybrid end effector, robots can successfully perform multiple complex tasks that are infeasible for conventional two finger grippers alone. All hardware designs and controlling systems will be released.

