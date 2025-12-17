---
layout: default
title: Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model
---

# Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model

**arXiv**: [2512.14031v1](https://arxiv.org/abs/2512.14031) | [PDF](https://arxiv.org/pdf/2512.14031.pdf)

**作者**: Zhaofeng Hu, Hongrui Yu, Vaidhyanathan Chandramouli, Ci-Jyun Liang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**评估VLA模型与分层强化学习在建筑机器人技能学习中的样本效率与实用性**

🎯 **匹配领域**: **强化学习**

**关键词**: `建筑机器人` `视觉-语言-动作模型` `分层强化学习` `样本效率` `少样本学习` `机器人技能学习` `多阶段任务` `泛化能力`

## 📋 核心要点

1. 核心问题：建筑自动化中机器人技能学习面临样本效率低、泛化能力差和部署工作量大的挑战，现有方法难以平衡性能与实用性。
2. 方法要点：通过系统评估VLA模型与分层RL方法，结合遥操作接口收集演示，比较其在样本效率、泛化和实际部署中的表现。
3. 实验或效果：VLA在少样本场景下实现高成功率（60%-100%），而DQN需额外调优但提供稳健基线，为实际应用提供指导。

## 📝 摘要（中文）

本研究评估了两种用于教授建筑机器人新技能的主流方法——视觉-语言-动作（VLA）模型和强化学习（RL）方法，以理解它们在建筑自动化中的适用性。目标是了解任务性能以及在真实工作中部署每种方法所需的实际工作量。作者开发了两个遥操作接口来控制机器人并收集所需的演示，这两种接口都被证明对训练机器人执行长期和灵巧任务有效。此外，作者进行了三阶段评估。首先，比较多层感知器（MLP）策略与深度Q网络（DQN）模仿模型，以确定更强的RL基线，重点关注模型性能、泛化能力和拾取实验。其次，在两种不同场景中训练三种不同的VLA模型并进行比较。第三，使用计算和样本效率指标对选定的RL基线与VLA模型进行基准测试，然后进行包括运输和安装在内的多阶段面板安装任务的机器人实验。VLA模型表现出强大的泛化和少样本能力，在拾取阶段实现了60%和100%的成功率。相比之下，DQN可以变得稳健，但需要在调优期间添加额外噪声，这增加了工作量。总体而言，研究结果表明，VLA通过减少编程工作量和用最少数据实现有用性能，为任务变更提供了实际优势，而DQN在可接受足够调优工作量的情况下提供了可行的基线。

## 🔬 方法详解

论文采用系统评估框架，核心方法包括：1）开发两种遥操作接口收集机器人演示数据，支持长期和灵巧任务训练；2）三阶段评估流程：首先比较MLP与DQN作为RL基线，其次训练三种VLA模型在不同场景下对比，最后通过计算和样本效率指标及多阶段面板安装实验基准测试VLA与DQN。关键创新点在于将VLA模型与分层RL方法在建筑任务中直接对比，突出样本效率和泛化能力。与现有方法的主要区别在于综合评估了VLA的少样本学习优势和RL的调优需求，为实际部署提供实用指南。

## 📊 实验亮点

VLA模型在拾取实验中展现出色泛化能力，少样本下实现60%和100%成功率；DQN虽稳健但需额外噪声调优增加工作量；整体上VLA在样本效率和实用性上优于RL基线。

## 🎯 应用场景

该研究主要应用于建筑自动化领域，如机器人面板安装、运输和灵巧操作任务，可减少人工编程工作量，提升机器人技能学习的效率和适应性，推动智能建造和工业机器人发展。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

