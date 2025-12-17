---
layout: default
title: DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation
---

# DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation

**arXiv**: [2510.11258v1](https://arxiv.org/abs/2510.11258) | [PDF](https://arxiv.org/pdf/2510.11258.pdf)

**作者**: Yuhui Fu, Feiyang Xie, Chaoyi Xu, Jing Xiong, Haoqi Yuan, Zongqing Lu

---

## 💡 一句话要点

**提出DemoHLM框架，从单次仿真演示实现人形机器人通用化移动操作**

**关键词**: `人形机器人` `移动操作` `仿真到现实迁移` `模仿学习` `全身控制`

## 📋 核心要点

1. 核心问题：人形机器人移动操作依赖硬编码或昂贵数据收集，限制自主性和泛化能力
2. 方法要点：采用分层结构，集成低层全身控制器与高层策略，通过仿真数据生成和模仿学习
3. 实验或效果：在真实机器人上验证了仿真到现实的迁移，在十个任务中表现鲁棒

## 📄 摘要（原文）

> Loco-manipulation is a fundamental challenge for humanoid robots to achieve
> versatile interactions in human environments. Although recent studies have made
> significant progress in humanoid whole-body control, loco-manipulation remains
> underexplored and often relies on hard-coded task definitions or costly
> real-world data collection, which limits autonomy and generalization. We
> present DemoHLM, a framework for humanoid loco-manipulation that enables
> generalizable loco-manipulation on a real humanoid robot from a single
> demonstration in simulation. DemoHLM adopts a hierarchy that integrates a
> low-level universal whole-body controller with high-level manipulation policies
> for multiple tasks. The whole-body controller maps whole-body motion commands
> to joint torques and provides omnidirectional mobility for the humanoid robot.
> The manipulation policies, learned in simulation via our data generation and
> imitation learning pipeline, command the whole-body controller with closed-loop
> visual feedback to execute challenging loco-manipulation tasks. Experiments
> show a positive correlation between the amount of synthetic data and policy
> performance, underscoring the effectiveness of our data generation pipeline and
> the data efficiency of our approach. Real-world experiments on a Unitree G1
> robot equipped with an RGB-D camera validate the sim-to-real transferability of
> DemoHLM, demonstrating robust performance under spatial variations across ten
> loco-manipulation tasks.

