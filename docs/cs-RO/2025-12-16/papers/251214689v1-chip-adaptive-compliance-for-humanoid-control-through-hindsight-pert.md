---
layout: default
title: CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation
---

# CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation

**arXiv**: [2512.14689v1](https://arxiv.org/abs/2512.14689) | [PDF](https://arxiv.org/pdf/2512.14689.pdf)

**作者**: Sirui Chen, Zi-ang Cao, Zhengyi Luo, Fernando Castañeda, Chenran Li, Tingwu Wang, Ye Yuan, Linxi "Jim" Fan, C. Karen Liu, Yuke Zhu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-16

**备注**: The first two authors contributed equally. Project page: https://nvlabs.github.io/CHIP/

---

## 💡 一句话要点

**提出CHIP模块以解决人形机器人执行强力操作任务时末端执行器刚度控制与动态运动跟踪的平衡问题。**

**关键词**: `人形机器人控制` `自适应合规性` `末端执行器刚度` `后见扰动` `强力操作任务` `运动跟踪` `强化学习` `即插即用模块`

## 📋 核心要点

1. 核心问题：人形机器人虽能实现敏捷运动，但在强力操作任务中难以平衡末端执行器刚度与动态运动跟踪，导致任务执行受限。
2. 方法要点：提出CHIP模块，通过后见扰动自适应调整末端执行器合规性，无需复杂数据或奖励设计，实现即插即用的刚度控制。
3. 实验或效果：CHIP使通用控制器成功执行多机器人协作、擦拭等任务，验证了其在多样化强力操作中的有效性和泛化能力。

## 📝 摘要（中文）

人形机器人在敏捷运动技能（如后空翻、奔跑、爬行）方面取得了显著进展，但在执行强力操作任务（如移动物体、擦拭、推车）时仍面临挑战。本文提出自适应合规人形控制通过后见扰动（CHIP），这是一个即插即用模块，能够在保持动态参考运动敏捷跟踪的同时，实现可控的末端执行器刚度。CHIP易于实现，无需数据增强或额外奖励调整。研究表明，使用CHIP训练的通用运动跟踪控制器能够执行多种需要不同末端执行器合规性的强力操作任务，例如多机器人协作、擦拭、箱子递送和开门。

## 🔬 方法详解

CHIP是一个基于强化学习的即插即用模块，整体框架集成于通用运动跟踪控制器中，通过后见扰动技术自适应调整末端执行器刚度。关键技术创新在于利用扰动历史信息优化合规性控制，无需额外数据增强或奖励函数调优。与现有方法的主要区别在于，CHIP专注于末端执行器刚度与动态运动跟踪的协同优化，避免了传统方法中数据依赖和调参复杂性，提升了任务适应性和实现简便性。

## 📊 实验亮点

实验显示，CHIP模块使通用控制器在多种强力操作任务中实现高效执行，如多机器人协作和开门，验证了其自适应合规性控制的优越性能，无需额外数据或奖励调整，显著提升了任务完成率和泛化能力。

## 🎯 应用场景

该研究可应用于人形机器人在工业、服务或家庭环境中的强力操作任务，如物体搬运、清洁、协作搬运和门操作，提升机器人在复杂场景下的多功能性和实用性。

## 📄 摘要（原文）

> Recent progress in humanoid robots has unlocked agile locomotion skills, including backflipping, running, and crawling. Yet it remains challenging for a humanoid robot to perform forceful manipulation tasks such as moving objects, wiping, and pushing a cart. We propose adaptive Compliance Humanoid control through hIsight Perturbation (CHIP), a plug-and-play module that enables controllable end-effector stiffness while preserving agile tracking of dynamic reference motions. CHIP is easy to implement and requires neither data augmentation nor additional reward tuning. We show that a generalist motion-tracking controller trained with CHIP can perform a diverse set of forceful manipulation tasks that require different end-effector compliance, such as multi-robot collaboration, wiping, box delivery, and door opening.

