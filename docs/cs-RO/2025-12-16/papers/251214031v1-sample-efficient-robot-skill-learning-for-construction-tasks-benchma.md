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

**评估VLA模型与强化学习方法在建筑机器人技能学习中的样本效率与实用性**

**关键词**: `建筑机器人` `视觉-语言-动作模型` `强化学习` `样本效率` `多模态融合` `遥操作接口` `技能学习` `自动化部署`

## 📋 核心要点

1. 核心问题：建筑自动化中机器人技能学习面临样本效率低、泛化能力差和部署工作量大的挑战，现有方法如传统RL需要大量数据和复杂调优。
2. 方法要点：提出基于视觉-语言-动作（VLA）模型的端到端学习框架，结合遥操作接口收集演示，实现少样本学习和任务适应。
3. 实验或效果：VLA模型在拾取任务中达到60%-100%成功率，优于DQN基线，显著减少数据需求和编程工作量。

## 📝 摘要（中文）

本研究评估了两种领先方法——视觉-语言-动作（VLA）模型和强化学习（RL）方法——用于教授建筑机器人新技能，以理解它们在建筑自动化中的适用性。目标是了解任务性能以及在真实工作中部署每种方法所需的实际努力。作者开发了两个遥操作接口来控制机器人并收集所需的演示，这两种接口都被证明对训练机器人执行长期和灵巧任务有效。此外，作者进行了三阶段评估。首先，作者比较了多层感知器（MLP）策略和深度Q网络（DQN）模仿模型，以确定更强的RL基线，重点关注模型性能、泛化能力和拾取实验。其次，在两种不同场景下训练了三种不同的VLA模型，并相互比较。第三，作者使用计算和样本效率指标，以及一个包括运输和安装的多阶段面板安装任务的机器人实验，对选定的RL基线与VLA模型进行了基准测试。VLA模型表现出强大的泛化和少样本能力，在拾取阶段实现了60%和100%的成功率。相比之下，DQN可以变得鲁棒，但需要在调优期间添加额外噪声，这增加了工作量。总体而言，研究结果表明，VLA通过减少编程努力和用最少数据实现有用性能，为任务变更提供了实际优势，而DQN在可接受足够调优努力时提供了一个可行的基线。

## 🔬 方法详解

论文采用分层评估框架，核心方法包括VLA模型和RL方法。整体框架基于遥操作接口收集机器人演示数据，用于训练和比较。关键技术创新点在于VLA模型的多模态融合，结合视觉输入、语言指令和动作输出，实现端到端技能学习。与现有方法的主要区别在于VLA模型强调少样本能力和泛化性，而传统RL方法如DQN依赖更多数据和调优噪声来提升鲁棒性。

## 📊 实验亮点

VLA模型在拾取实验中实现60%和100%成功率，展示强泛化和少样本能力；DQN基线虽可鲁棒化，但需额外噪声调优增加工作量；整体上VLA在样本效率和实用性上优于RL方法。

## 🎯 应用场景

该研究主要应用于建筑自动化领域，如机器人面板安装、运输和灵巧操作任务，可推广到其他需要高效技能学习的工业机器人场景，提升自动化系统的适应性和部署效率。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

