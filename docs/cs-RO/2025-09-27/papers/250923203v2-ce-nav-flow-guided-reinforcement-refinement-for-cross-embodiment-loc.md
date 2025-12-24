---
layout: default
title: "CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation"
---

# CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23203" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23203v2</a>
  <a href="https://arxiv.org/pdf/2509.23203.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23203v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23203v2', 'CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Yang, Tianlin Zhang, Zhengbo Wang, Zedong Chu, Xiaolong Wu, Yang Cai, Mu Xu

**分类**: cs.RO

**发布日期**: 2025-09-27 (更新: 2025-10-23)

**备注**: Project Page: https://ce-nav.github.io/. Code is available at https://github.com/amap-cvlab/CE-Nav

**🔗 代码/项目**: [GITHUB](https://github.com/amap-cvlab/CE-Nav)

---

## 💡 一句话要点

**CE-Nav：面向跨形态机器人局部导航的流引导强化精炼方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人导航` `强化学习` `模仿学习` `跨形态泛化` `条件归一化流`

## 📋 核心要点

1. 现有方法需要大量特定形态的数据，规划与控制紧密耦合，且确定性模型难以捕捉多模态决策，阻碍了跨形态机器人局部导航策略的泛化。
2. CE-Nav通过模仿学习训练通用专家，学习运动学合理的动作分布，再利用强化学习训练动态感知精炼器，补偿特定机器人的动力学特性。
3. 实验表明，CE-Nav在多种机器人上实现了最先进的性能，并显著降低了适应成本，真实世界的部署验证了其有效性和可扩展性。

## 📝 摘要（中文）

本文提出CE-Nav，一种新颖的两阶段（IL-then-RL）框架，旨在系统地解耦通用几何推理和特定形态的动态适应，从而解决跨多种机器人形态泛化局部导航策略的难题。首先，我们使用模仿学习离线训练一个与形态无关的通用专家，该专家是一个名为VelFlow的条件归一化流模型，从经典规划器生成的大规模数据集中学习运动学上合理的动作的完整分布，完全避免了真实机器人数据，并解决了多模态问题。其次，对于新的机器人，我们冻结专家，并将其用作指导先验，通过在线强化学习训练一个轻量级的、动态感知的精炼器。该精炼器能够以最小的环境交互快速学习补偿目标机器人的特定动力学和控制器缺陷。在四足机器人、双足机器人和四旋翼飞行器上的大量实验表明，CE-Nav实现了最先进的性能，同时大大降低了适应成本。成功的真实世界部署进一步验证了我们的方法是构建可泛化导航系统的有效且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决跨多种机器人形态泛化局部导航策略的问题。现有方法的痛点在于需要大量特定形态的数据，规划与控制紧密耦合，以及“灾难性平均”问题，即确定性模型无法捕捉多模态决策（例如，向左或向右转）。

**核心思路**：论文的核心思路是将通用几何推理与特定形态的动态适应解耦。首先，学习一个与形态无关的通用专家，负责学习通用的运动学约束和几何推理。然后，针对特定机器人，通过强化学习训练一个轻量级的精炼器，负责补偿该机器人的特定动力学特性和控制器缺陷。这样可以避免为每种机器人单独训练导航策略，并提高泛化能力。

**技术框架**：CE-Nav框架包含两个主要阶段：1) 模仿学习阶段：离线训练通用专家VelFlow。VelFlow是一个条件归一化流模型，输入是当前状态和目标位置，输出是动作的概率分布。训练数据由经典规划器生成，避免了真实机器人数据。2) 强化学习阶段：在线训练动态感知精炼器。精炼器以VelFlow的输出作为先验，通过强化学习学习补偿目标机器人的特定动力学特性和控制器缺陷。

**关键创新**：最重要的技术创新点在于将导航策略分解为通用几何推理和特定形态的动态适应两个部分，并分别使用模仿学习和强化学习进行训练。这种解耦的方式可以显著提高导航策略的泛化能力和适应性。此外，使用条件归一化流模型VelFlow学习动作的概率分布，可以有效解决多模态问题。

**关键设计**：VelFlow使用条件归一化流模型，可以学习动作的概率分布。精炼器使用轻量级的神经网络结构，以减少训练成本。强化学习算法使用PPO或其他合适的算法。损失函数包括模仿学习损失和强化学习奖励函数。具体参数设置未知。

## 📊 实验亮点

CE-Nav在四足机器人、双足机器人和四旋翼飞行器上进行了大量实验，结果表明，CE-Nav实现了最先进的性能，同时大大降低了适应成本。与现有方法相比，CE-Nav在导航成功率和效率方面均有显著提升。此外，CE-Nav还在真实世界中进行了部署，验证了其有效性和可扩展性。具体性能数据未知。

## 🎯 应用场景

CE-Nav具有广泛的应用前景，可用于各种机器人的自主导航，例如服务机器人、物流机器人、搜救机器人等。该方法可以降低机器人导航系统的开发成本，提高机器人的适应性和鲁棒性，并促进机器人在复杂环境中的应用。

## 📄 摘要（原文）

> Generalizing local navigation policies across diverse robot morphologies is a critical challenge. Progress is often hindered by the need for costly and embodiment-specific data, the tight coupling of planning and control, and the "disastrous averaging" problem where deterministic models fail to capture multi-modal decisions (e.g., turning left or right). We introduce CE-Nav, a novel two-stage (IL-then-RL) framework that systematically decouples universal geometric reasoning from embodiment-specific dynamic adaptation. First, we train an embodiment-agnostic General Expert offline using imitation learning. This expert, a conditional normalizing flow model named VelFlow, learns the full distribution of kinematically-sound actions from a large-scale dataset generated by a classical planner, completely avoiding real robot data and resolving the multi-modality issue. Second, for a new robot, we freeze the expert and use it as a guiding prior to train a lightweight, Dynamics-Aware Refiner via online reinforcement learning. This refiner rapidly learns to compensate for the target robot's specific dynamics and controller imperfections with minimal environmental interaction. Extensive experiments on quadrupeds, bipeds, and quadrotors show that CE-Nav achieves state-of-the-art performance while drastically reducing adaptation cost. Successful real-world deployments further validate our approach as an efficient and scalable solution for building generalizable navigation systems. Code is available at https://github.com/amap-cvlab/CE-Nav.

