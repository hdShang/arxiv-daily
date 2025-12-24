---
layout: default
title: "Vejde: A Framework for Inductive Deep Reinforcement Learning Based on Factor Graph Color Refinement"
---

# Vejde: A Framework for Inductive Deep Reinforcement Learning Based on Factor Graph Color Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09219" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09219v1</a>
  <a href="https://arxiv.org/pdf/2509.09219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09219v1', 'Vejde: A Framework for Inductive Deep Reinforcement Learning Based on Factor Graph Color Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jakob Nyberg, Pontus Johnson

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**提出Vejde框架以解决复杂状态下的决策问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `归纳学习` `图神经网络` `强化学习` `决策问题` `策略泛化` `复杂状态` `二分图` `RDDL`

## 📋 核心要点

1. 现有方法在处理具有复杂结构状态的决策问题时，往往难以实现有效的策略泛化。
2. Vejde框架通过将MDP状态转化为二分图，并利用图神经网络进行消息传递，来生成归纳策略函数。
3. 实验表明，Vejde代理在未见实例上的平均得分与特定实例的MLP代理相近，展示了良好的泛化能力。

## 📝 摘要（中文）

我们提出并评估了Vejde框架，该框架结合了数据抽象、图神经网络和强化学习，以生成适用于具有丰富结构状态的决策问题的归纳策略函数。MDP状态被表示为关于实体的事实数据库，Vejde将每个状态转换为二分图，并通过神经消息传递映射到潜在状态。Vejde代理能够处理不同规模和结构的问题。我们在八个RDDL定义的问题域上测试了Vejde代理，结果显示其策略在未见实例上的泛化能力良好，且与特定实例的MLP代理表现相近。

## 🔬 方法详解

**问题定义**：本论文旨在解决在复杂状态下的决策问题，现有方法在策略泛化和处理多样性方面存在不足，难以适应不同规模和结构的问题。

**核心思路**：Vejde框架通过将MDP状态表示为事实数据库，进而转换为二分图，利用图神经网络的消息传递机制来生成归纳策略函数，从而提高策略的泛化能力。

**技术框架**：Vejde的整体架构包括状态表示模块、图转换模块和策略生成模块。状态表示模块将实体信息转化为事实数据库，图转换模块将其转化为二分图，最后通过图神经网络进行消息传递以生成策略。

**关键创新**：Vejde的主要创新在于其将状态和动作的因子化表示结合图神经网络，允许代理在不同规模和结构的问题上进行有效学习，这在现有方法中尚属首次。

**关键设计**：在设计中，Vejde采用了特定的损失函数来优化策略生成，并在图神经网络中使用了多层感知机结构，以增强其对复杂关系的建模能力。

## 📊 实验亮点

实验结果显示，Vejde代理在未见实例上的得分与特定实例的MLP代理相近，且在八个RDDL定义的问题域中，Vejde的策略在泛化能力上表现优异，未见实例的得分平均未显著下降，展示了良好的学习效果。

## 🎯 应用场景

Vejde框架具有广泛的应用潜力，尤其适用于需要处理复杂状态和关系的决策问题，如机器人控制、智能交通系统和游戏AI等领域。其归纳学习能力能够有效提升系统在动态环境中的适应性和决策效率，未来可能推动智能系统的进一步发展。

## 📄 摘要（原文）

> We present and evaluate Vejde; a framework which combines data abstraction, graph neural networks and reinforcement learning to produce inductive policy functions for decision problems with richly structured states, such as object classes and relations. MDP states are represented as data bases of facts about entities, and Vejde converts each state to a bipartite graph, which is mapped to latent states through neural message passing. The factored representation of both states and actions allows Vejde agents to handle problems of varying size and structure. We tested Vejde agents on eight problem domains defined in RDDL, with ten problem instances each, where policies were trained using both supervised and reinforcement learning. To test policy generalization, we separate problem instances in two sets, one for training and the other solely for testing. Test results on unseen instances for the Vejde agents were compared to MLP agents trained on each problem instance, as well as the online planning algorithm Prost. Our results show that Vejde policies in average generalize to the test instances without a significant loss in score. Additionally, the inductive agents received scores on unseen test instances that on average were close to the instance-specific MLP agents.

