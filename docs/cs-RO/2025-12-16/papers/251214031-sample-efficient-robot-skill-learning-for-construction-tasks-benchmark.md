---
layout: default
title: Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model
---

# Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14031" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14031</a>
  <a href="https://arxiv.org/pdf/2512.14031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14031" onclick="toggleFavorite(this, '2512.14031', 'Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaofeng Hu, Hongrui Yu, Vaidhyanathan Chandramouli, Ci-Jyun Liang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**对比VLA模型与强化学习，提升建筑机器人操作技能并实现高效样本利用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `建筑机器人` `技能学习` `视觉-语言-动作模型` `强化学习` `样本效率` `泛化能力` `遥操作` `DQN`

## 📋 核心要点

1. 建筑机器人技能学习面临挑战，传统方法编程复杂且泛化性差，难以适应多变的任务需求。
2. 论文对比VLA模型和强化学习，利用遥操作数据训练机器人，旨在提升样本效率和泛化能力。
3. 实验表明，VLA模型在少样本学习和泛化方面优于DQN，但在充分调优下DQN也是可行的基线。

## 📝 摘要（中文）

本研究评估了两种领先的方法，即视觉-语言-动作（VLA）模型和强化学习（RL）方法，用于训练建筑机器人掌握新技能，旨在了解它们在建筑自动化中的适用性。作者开发了两种遥操作界面来控制机器人并收集所需的演示数据，这两种界面都被证明对训练机器人执行长时程和灵巧任务有效。此外，作者进行了一个三阶段的评估。首先，作者比较了多层感知器（MLP）策略与深度Q网络（DQN）模仿模型，以确定更强的RL基线，重点关注模型性能、泛化能力和一个拾取实验。其次，在两种不同的场景中训练了三种不同的VLA模型，并将它们相互比较。第三，作者使用计算和样本效率指标，以及一个包含运输和安装的多阶段面板安装机器人实验，将选定的RL基线与VLA模型进行基准测试。VLA模型表现出强大的泛化能力和少样本学习能力，在拾取阶段实现了60%和100%的成功率。相比之下，DQN可以通过在调整过程中添加额外的噪声来使其更加鲁棒，但这增加了工作量。总的来说，研究结果表明，VLA通过减少编程工作量和以最少的数据实现有用的性能，为改变任务提供了实际优势，而DQN在可以接受足够的调整工作量时，提供了一个可行的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑机器人技能学习中样本效率低和泛化能力差的问题。现有方法通常需要大量的训练数据和精细的手动调整，难以适应建筑工地多变的环境和任务需求。因此，如何利用少量样本快速训练出具有良好泛化能力的机器人技能是本研究的核心问题。

**核心思路**：论文的核心思路是对比研究视觉-语言-动作（VLA）模型和强化学习（RL）方法在建筑机器人技能学习中的表现。VLA模型通过结合视觉信息、语言指令和动作控制，使机器人能够理解任务目标并执行相应的动作。强化学习则通过试错学习，使机器人能够自主地探索环境并优化策略。通过对比两种方法的性能，可以了解它们在样本效率、泛化能力和实际部署方面的优劣。

**技术框架**：论文的整体框架包括数据收集、模型训练和实验评估三个阶段。首先，通过遥操作界面收集机器人的演示数据。然后，分别训练VLA模型和RL模型。VLA模型采用不同的架构，包括MLP等。RL模型则采用DQN算法。最后，通过一系列实验评估两种模型的性能，包括拾取实验和多阶段面板安装实验。

**关键创新**：论文的关键创新在于对比研究了VLA模型和RL模型在建筑机器人技能学习中的表现，并提出了基于遥操作数据的训练方法。VLA模型能够利用语言指令和视觉信息，实现更强的泛化能力和少样本学习能力。与传统的RL方法相比，VLA模型能够更快地适应新的任务。

**关键设计**：在VLA模型中，采用了不同的网络结构，包括MLP等，以提取视觉特征和语言特征，并将它们融合到动作控制中。在RL模型中，采用了DQN算法，并添加了噪声来提高鲁棒性。此外，论文还设计了两种遥操作界面，用于收集机器人的演示数据。损失函数的设计也至关重要，需要平衡模仿学习和强化学习的目标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14031/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VLA模型在拾取阶段实现了60%和100%的成功率，表现出强大的泛化能力和少样本学习能力。相比之下，DQN需要额外的噪声调整才能达到较好的鲁棒性。在多阶段面板安装实验中，VLA模型也表现出优于DQN的性能。这些结果表明，VLA模型在建筑机器人技能学习中具有实际优势。

## 🎯 应用场景

该研究成果可应用于建筑自动化领域，例如建筑构件的搬运、安装和装配。通过VLA模型或强化学习，机器人可以自主地完成各种建筑任务，提高施工效率和质量，降低人工成本和安全风险。此外，该研究方法也可以推广到其他机器人应用领域，例如物流、医疗和农业。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

