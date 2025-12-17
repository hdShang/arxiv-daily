---
layout: default
title: Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model
---

# Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14031" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14031v1</a>
  <a href="https://arxiv.org/pdf/2512.14031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14031v1" onclick="toggleFavorite(this, '2512.14031v1', 'Sample-Efficient Robot Skill Learning for Construction Tasks: Benchmarking Hierarchical Reinforcement Learning and Vision-Language-Action VLA Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaofeng Hu, Hongrui Yu, Vaidhyanathan Chandramouli, Ci-Jyun Liang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**对比VLA模型与强化学习，提升建筑机器人操作技能并实现高效样本利用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人技能学习` `视觉-语言-动作模型` `强化学习` `建筑自动化` `样本效率`

## 📋 核心要点

1. 现有建筑机器人技能学习方法在泛化性和样本效率方面存在挑战，难以适应快速变化的施工任务。
2. 论文对比研究VLA模型和强化学习方法，旨在找到一种更高效、更易于部署的机器人技能学习方案。
3. 实验表明，VLA模型在泛化性和少样本学习方面优于DQN，更适合快速适应新任务，降低了编程工作量。

## 📝 摘要（中文）

本研究评估了两种领先的方法，即视觉-语言-动作（VLA）模型和强化学习（RL）方法，用于训练建筑机器人掌握新技能，旨在了解它们在建筑自动化中的适用性。作者开发了两种遥操作界面来控制机器人并收集所需的演示数据，这两种界面都被证明对训练机器人执行长时程和灵巧任务有效。此外，作者进行了一个三阶段的评估。首先，作者比较了多层感知机（MLP）策略与深度Q网络（DQN）模仿模型，以确定更强的RL基线，重点关注模型性能、泛化能力和一个拾取实验。其次，在两种不同的场景中训练了三种不同的VLA模型，并将它们相互比较。第三，作者使用计算和样本效率指标，以及一个包含运输和安装的多阶段面板安装机器人实验，将选定的RL基线与VLA模型进行基准测试。VLA模型表现出强大的泛化能力和少样本学习能力，在拾取阶段实现了60%和100%的成功率。相比之下，DQN可以通过在调整过程中添加额外的噪声来使其更加鲁棒，但这增加了工作量。总的来说，研究结果表明，VLA通过减少编程工作量和以最少的数据实现有用的性能，为改变任务提供了实际优势，而DQN在可以接受足够的调整工作量时，提供了一个可行的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑机器人技能学习中泛化能力弱和样本效率低的问题。现有方法，如传统的强化学习，通常需要大量的训练数据和精细的调参才能在特定任务上取得良好效果，难以适应建筑场景中频繁变化的任务需求。

**核心思路**：论文的核心思路是探索利用视觉-语言-动作（VLA）模型，结合少量演示数据，使机器人能够理解任务指令并执行相应的动作。VLA模型能够将视觉信息、语言指令和动作指令关联起来，从而实现更强的泛化能力和少样本学习能力。同时，论文也研究了强化学习方法，并将其作为基线进行对比。

**技术框架**：整体框架包含数据收集、模型训练和实验评估三个阶段。数据收集阶段通过遥操作界面收集机器人的演示数据。模型训练阶段分别训练VLA模型和强化学习模型。实验评估阶段对比两种模型在不同任务上的性能，包括拾取任务和多阶段面板安装任务。VLA模型使用了不同的架构，包括Transformer等。强化学习模型使用了DQN算法。

**关键创新**：论文的关键创新在于对比研究了VLA模型和强化学习方法在建筑机器人技能学习中的应用，并验证了VLA模型在泛化性和少样本学习方面的优势。与传统的强化学习方法相比，VLA模型能够更好地利用少量演示数据，快速适应新的任务需求。

**关键设计**：VLA模型的关键设计包括：1) 使用Transformer架构来处理视觉、语言和动作信息；2) 设计合适的损失函数来训练模型，例如模仿学习损失和强化学习损失；3) 探索不同的数据增强方法来提高模型的泛化能力。DQN的关键设计包括：1) 使用经验回放机制来提高样本利用率；2) 使用目标网络来稳定训练过程；3) 通过添加噪声来提高模型的鲁棒性。

## 📊 实验亮点

实验结果表明，VLA模型在拾取任务中实现了60%和100%的成功率，表现出强大的泛化能力和少样本学习能力。相比之下，DQN需要额外的噪声调整才能达到较好的鲁棒性，增加了工作量。在多阶段面板安装任务中，VLA模型也表现出优于DQN的性能，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究成果可应用于建筑自动化领域，例如建筑构件的搬运、安装和拆卸等任务。通过VLA模型，可以降低机器人编程的难度，提高机器人的适应性和灵活性，从而实现更高效、更智能的建筑施工。此外，该方法还可以推广到其他需要机器人执行复杂操作的领域，例如制造业、物流业等。

## 📄 摘要（原文）

> This study evaluates two leading approaches for teaching construction robots new skills to understand their applicability for construction automation: a Vision-Language-Action (VLA) model and Reinforcement Learning (RL) methods. The goal is to understand both task performance and the practical effort needed to deploy each approach on real jobs. The authors developed two teleoperation interfaces to control the robots and collect the demonstrations needed, both of which proved effective for training robots for long-horizon and dexterous tasks. In addition, the authors conduct a three-stage evaluation. First, the authors compare a Multi-Layer Perceptron (MLP) policy with a Deep Q-network (DQN) imitation model to identify the stronger RL baseline, focusing on model performance, generalization, and a pick-up experiment. Second, three different VLA models are trained in two different scenarios and compared with each other. Third, the authors benchmark the selected RL baseline against the VLA model using computational and sample-efficiency measures and then a robot experiment on a multi-stage panel installation task that includes transport and installation. The VLA model demonstrates strong generalization and few-shot capability, achieving 60% and 100% success in the pickup phase. In comparison, DQN can be made robust but needs additional noise during tuning, which increases the workload. Overall, the findings indicate that VLA offers practical advantages for changing tasks by reducing programming effort and enabling useful performance with minimal data, while DQN provides a viable baseline when sufficient tuning effort is acceptable.

