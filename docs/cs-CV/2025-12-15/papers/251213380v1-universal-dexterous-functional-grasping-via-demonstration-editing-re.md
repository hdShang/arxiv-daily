---
layout: default
title: Universal Dexterous Functional Grasping via Demonstration-Editing Reinforcement Learning
---

# Universal Dexterous Functional Grasping via Demonstration-Editing Reinforcement Learning

**arXiv**: [2512.13380v1](https://arxiv.org/abs/2512.13380) | [PDF](https://arxiv.org/pdf/2512.13380.pdf)

**作者**: Chuan Mao, Haoqi Yuan, Ziye Huang, Chaoyi Xu, Kai Ma, Zongqing Lu

---

## 💡 一句话要点

**提出DemoFunGrasp，通过演示编辑强化学习实现通用灵巧功能抓取**

**关键词**: `灵巧抓取` `强化学习` `演示编辑` `功能抓取` `仿真到现实迁移` `视觉语言模型`

## 📋 核心要点

1. 核心问题：灵巧抓取中细粒度功能抓取的目标与奖励函数设计复杂，多任务探索困难，仿真到现实迁移挑战大。
2. 方法要点：将功能抓取条件分解为抓取风格和可供性，集成到强化学习框架，利用单次演示进行一步编辑优化。
3. 实验或效果：在仿真和现实中泛化至未见对象、可供性和抓取风格组合，成功率和功能抓取准确率优于基线，具备自主指令跟随能力。

## 📄 摘要（原文）

> Reinforcement learning (RL) has achieved great success in dexterous grasping, significantly improving grasp performance and generalization from simulation to the real world. However, fine-grained functional grasping, which is essential for downstream manipulation tasks, remains underexplored and faces several challenges: the complexity of specifying goals and reward functions for functional grasps across diverse objects, the difficulty of multi-task RL exploration, and the challenge of sim-to-real transfer. In this work, we propose DemoFunGrasp for universal dexterous functional grasping. We factorize functional grasping conditions into two complementary components - grasping style and affordance - and integrate them into an RL framework that can learn to grasp any object with any functional grasping condition. To address the multi-task optimization challenge, we leverage a single grasping demonstration and reformulate the RL problem as one-step demonstration editing, substantially enhancing sample efficiency and performance. Experimental results in both simulation and the real world show that DemoFunGrasp generalizes to unseen combinations of objects, affordances, and grasping styles, outperforming baselines in both success rate and functional grasping accuracy. In addition to strong sim-to-real capability, by incorporating a vision-language model (VLM) for planning, our system achieves autonomous instruction-following grasp execution.

