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

**对比VLA模型与强化学习，提升建筑机器人操作技能并实现高效样本利用**

🎯 **匹配领域**: **具身智能 (Embodied AI)**

**关键词**: `建筑机器人` `技能学习` `视觉-语言-动作模型` `强化学习` `样本效率`

## 📋 核心要点

1. 现有建筑机器人技能学习方法在泛化性和样本效率方面存在挑战，难以适应快速变化的施工任务。
2. 论文对比研究VLA模型和强化学习方法，旨在找到一种更高效、泛化性更强的机器人技能学习方案。
3. 实验结果表明，VLA模型在泛化性和少样本学习方面表现出色，而DQN在经过充分调整后也能达到较好的效果。

## 📝 摘要（中文）

本研究评估了两种领先的方法，即视觉-语言-动作（VLA）模型和强化学习（RL）方法，用于训练建筑机器人掌握新技能，旨在了解它们在建筑自动化中的适用性。作者开发了两种遥操作界面来控制机器人并收集所需的演示数据，这两种界面都被证明对训练机器人执行长时程和灵巧任务有效。此外，作者进行了三个阶段的评估。首先，将多层感知器（MLP）策略与深度Q网络（DQN）模仿模型进行比较，以确定更强的RL基线，重点关注模型性能、泛化能力和拾取实验。其次，在两种不同的场景中训练了三种不同的VLA模型，并将它们相互比较。第三，作者使用计算和样本效率指标，以及一个包含运输和安装的多阶段面板安装机器人实验，来评估选定的RL基线与VLA模型。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑机器人技能学习中样本效率低和泛化能力差的问题。现有方法，如传统的强化学习，通常需要大量的训练数据和精细的调参才能在复杂环境中取得良好的效果，这在实际的建筑场景中是难以实现的。此外，任务的快速变化也对机器人的适应性提出了更高的要求。

**核心思路**：论文的核心思路是探索利用视觉-语言-动作（VLA）模型和强化学习方法，并对比分析它们在建筑机器人技能学习中的性能。VLA模型通过结合视觉信息和自然语言指令，使机器人能够理解任务目标并执行相应的动作，从而提高泛化能力和少样本学习能力。强化学习则通过与环境的交互学习最优策略，但需要更多的样本和调参。

**技术框架**：论文的整体框架包括数据采集、模型训练和实验评估三个阶段。首先，通过遥操作界面收集机器人的演示数据。然后，分别训练VLA模型和强化学习模型。最后，通过一系列的实验，包括拾取实验和多阶段面板安装实验，对两种模型的性能进行评估和比较。VLA模型使用了不同的架构，包括Transformer等，而强化学习则使用了DQN作为基线。

**关键创新**：论文的关键创新在于对比研究了VLA模型和强化学习方法在建筑机器人技能学习中的性能，并揭示了它们各自的优缺点。VLA模型在泛化性和少样本学习方面表现出色，而强化学习在经过充分调整后也能达到较好的效果。这为建筑机器人技能学习提供了新的思路和方法。

**关键设计**：在VLA模型中，使用了Transformer架构来处理视觉信息和自然语言指令，并生成相应的动作。在强化学习中，使用了DQN作为基线，并探索了不同的噪声添加方法来提高模型的鲁棒性。此外，论文还设计了两种遥操作界面来收集机器人的演示数据，并设计了多阶段面板安装实验来评估模型的性能。

## 📊 实验亮点

VLA模型在拾取阶段表现出强大的泛化能力和少样本学习能力，成功率分别达到60%和100%。相比之下，DQN需要额外的噪声调整才能变得鲁棒，这增加了工作量。在多阶段面板安装任务中，VLA模型也表现出良好的性能，证明了其在复杂任务中的潜力。

## 🎯 应用场景

该研究成果可应用于建筑自动化领域，例如建筑构件的搬运、安装和装配等任务。通过利用VLA模型或强化学习方法，可以提高建筑机器人的智能化水平和工作效率，降低人工成本，并提高施工质量和安全性。此外，该研究还可以推广到其他需要机器人执行复杂任务的领域，如制造业、物流等。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

