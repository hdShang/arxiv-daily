---
layout: default
title: "Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model"
---

# Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14031" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14031v1</a>
  <a href="https://arxiv.org/pdf/2512.14031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14031v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14031v1', 'Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaofeng Hu, Hongrui Yu, Vaidhyanathan Chandramouli, Ci-Jyun Liang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**对比VLA模型与强化学习，提升建筑机器人操作技能并实现高效样本利用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑机器人` `技能学习` `视觉-语言-动作模型` `强化学习` `样本效率`

## 📋 核心要点

1. 现有建筑机器人技能学习方法在泛化性和样本效率方面存在不足，难以适应快速变化的施工任务。
2. 本研究对比VLA模型和强化学习方法，探索利用少量样本数据高效训练机器人完成复杂建筑任务的策略。
3. 实验表明，VLA模型在泛化性和少样本学习方面优于DQN，能以更少的编程工作量实现较好的性能。

## 📝 摘要（中文）

本研究评估了两种领先的方法，即视觉-语言-动作（VLA）模型和强化学习（RL）方法，用于训练建筑机器人掌握新技能，旨在了解它们在建筑自动化中的适用性。作者开发了两种遥操作界面来控制机器人并收集所需的演示数据，这两种界面都被证明对训练机器人执行长时程和灵巧任务有效。此外，作者进行了一个三阶段的评估。首先，作者比较了多层感知机（MLP）策略与深度Q网络（DQN）模仿模型，以确定更强的RL基线，重点关注模型性能、泛化能力和一个拾取实验。其次，在两种不同的场景中训练了三种不同的VLA模型，并将它们相互比较。第三，作者使用计算和样本效率指标，以及一个包含运输和安装的多阶段面板安装机器人实验，将选定的RL基线与VLA模型进行基准测试。VLA模型表现出强大的泛化能力和少样本学习能力，在拾取阶段实现了60%和100%的成功率。相比之下，DQN可以通过在调整过程中添加额外的噪声来使其更加鲁棒，但这增加了工作量。总的来说，研究结果表明，VLA通过减少编程工作量和以最少的数据实现有用的性能，为更改任务提供了实际优势，而DQN在可以接受足够的调整工作量时，提供了一个可行的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑机器人技能学习中泛化能力弱和样本效率低的问题。现有方法通常需要大量的训练数据和精细的调参，难以适应建筑场景中任务的快速变化。因此，如何利用少量样本数据，使机器人快速掌握新的操作技能，是本研究要解决的核心问题。

**核心思路**：论文的核心思路是对比研究视觉-语言-动作（VLA）模型和强化学习（RL）方法在建筑机器人技能学习中的表现。VLA模型通过结合视觉信息、自然语言指令和动作指令，使机器人能够理解任务目标并执行相应的动作。强化学习方法则通过与环境交互，学习最优的策略。通过对比两种方法的性能，可以找到更适合建筑机器人技能学习的方法。

**技术框架**：本研究的技术框架主要包括以下几个部分：1) 两种遥操作界面，用于收集机器人操作的演示数据；2) 三种VLA模型，用于学习视觉、语言和动作之间的关系；3) 基于DQN的强化学习模型，作为基线方法；4) 一个三阶段的评估流程，包括模型性能评估、泛化能力评估和机器人实验。

**关键创新**：本研究的关键创新在于对比了VLA模型和强化学习方法在建筑机器人技能学习中的表现，并验证了VLA模型在泛化性和少样本学习方面的优势。此外，本研究还开发了两种遥操作界面，用于收集机器人操作的演示数据，为VLA模型的训练提供了数据支持。

**关键设计**：在VLA模型方面，论文采用了三种不同的模型结构，并探索了不同的训练策略。在强化学习方面，论文采用了DQN算法，并针对建筑机器人的特点进行了优化。此外，论文还设计了一个多阶段的面板安装任务，用于评估VLA模型和强化学习方法的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VLA模型在拾取阶段实现了60%和100%的成功率，表现出强大的泛化能力和少样本学习能力。相比之下，DQN需要额外的噪声调整才能达到较好的鲁棒性，增加了工作量。在多阶段面板安装任务中，VLA模型也表现出优于DQN的性能，验证了VLA模型在建筑机器人技能学习中的优势。

## 🎯 应用场景

该研究成果可应用于建筑自动化领域，例如建筑构件的搬运、安装和拆卸等任务。通过使用VLA模型，可以减少人工编程的工作量，提高机器人的自主性和适应性，从而提高建筑施工的效率和质量。此外，该研究还可以推广到其他需要机器人执行复杂操作的领域，例如制造业、物流等。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

