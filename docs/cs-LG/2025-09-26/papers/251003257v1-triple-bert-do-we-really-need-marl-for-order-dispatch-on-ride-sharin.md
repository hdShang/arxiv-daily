---
layout: default
title: "Triple-BERT: Do We Really Need MARL for Order Dispatch on Ride-Sharing Platforms?"
---

# Triple-BERT: Do We Really Need MARL for Order Dispatch on Ride-Sharing Platforms?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03257" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03257v1</a>
  <a href="https://arxiv.org/pdf/2510.03257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03257v1', 'Triple-BERT: Do We Really Need MARL for Order Dispatch on Ride-Sharing Platforms?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zijian Zhao, Sen Li

**分类**: cs.LG, cs.AI, cs.MA

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/RS2002/Triple-BERT)

---

## 💡 一句话要点

**Triple-BERT：用于网约车订单调度的单智能体强化学习方法，性能优于多智能体强化学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `网约车调度` `强化学习` `单智能体强化学习` `BERT网络` `动作分解` `大规模状态空间` `大规模动作空间`

## 📋 核心要点

1. 现有MARL方法在网约车订单调度中存在不足，独立MARL无法获取全局信息，CTDE MARL面临维度灾难。
2. 提出Triple-BERT，一种中心化的单智能体强化学习方法，通过动作分解和BERT网络处理大规模动作和观察空间。
3. 在真实数据集上验证，Triple-BERT在服务订单和接送时间上均优于现有方法，提升显著。

## 📝 摘要（中文）

在Uber和Lyft等按需网约车平台上，面临着复杂的实时挑战，即如何将具有不同起点和终点的乘客与可用的车辆进行捆绑和匹配，同时应对重大的系统不确定性。由于大量司机和订单导致了庞大的观察空间，订单调度通常使用多智能体强化学习（MARL）来解决，尽管它本质上是一个中心化任务。然而，独立的MARL方法无法捕获全局信息，并且智能体之间的协作较差，而集中训练分散执行（CTDE）MARL方法则受到维度灾难的困扰。为了克服这些挑战，我们提出了一种中心化的单智能体强化学习（SARL）方法Triple-BERT，专门用于网约车平台上的大规模订单调度。我们的方法基于TD3的变体，通过将联合动作概率分解为单个司机动作概率的动作分解策略来解决巨大的动作空间。为了处理庞大的观察空间，我们引入了一种新颖的基于BERT的网络，其中参数重用减轻了参数随司机和订单数量增加而增长的问题，并且注意力机制有效地捕获了大量司机和订单之间复杂的相互关系。我们使用来自曼哈顿的真实网约车数据集验证了我们的方法。Triple-BERT比当前最先进的方法提高了约11.95％，其中已服务订单增加了4.26％，接送时间减少了22.25％。我们的代码、训练模型参数和处理后的数据可在https://github.com/RS2002/Triple-BERT公开获得。

## 🔬 方法详解

**问题定义**：论文旨在解决网约车平台订单调度问题，即如何高效地将乘客与司机进行匹配。现有MARL方法，如独立MARL和CTDE MARL，分别存在无法获取全局信息和维度灾难的问题，导致调度效率低下。

**核心思路**：论文的核心思路是将订单调度问题建模为中心化的单智能体强化学习问题，利用单智能体能够获取全局信息的优势，同时设计特定的网络结构来应对大规模的动作和观察空间。通过动作分解策略降低动作空间的维度，并使用基于BERT的网络来有效处理高维观察空间。

**技术框架**：Triple-BERT基于TD3算法框架。整体流程如下：首先，BERT网络对司机和订单信息进行编码，提取特征；然后，通过Actor网络输出每个司机的动作概率；接着，Critic网络评估当前状态-动作对的价值；最后，根据TD3算法进行策略更新。

**关键创新**：论文的关键创新在于提出了基于BERT的网络结构来处理大规模的观察空间。与传统方法相比，BERT网络能够有效地捕获司机和订单之间的复杂关系，并且通过参数重用降低了参数量，从而缓解了维度灾难。此外，动作分解策略也是一个重要的创新点，它将联合动作概率分解为单个司机动作概率，从而降低了动作空间的维度。

**关键设计**：BERT网络的输入包括司机和订单的特征信息，例如位置、时间、目的地等。BERT网络的输出作为Actor和Critic网络的输入。Actor网络采用多层感知机结构，输出每个司机的动作概率。Critic网络也采用多层感知机结构，输入包括状态和动作信息，输出状态-动作对的价值。损失函数采用TD3算法中的损失函数，包括Actor损失和Critic损失。

## 📊 实验亮点

实验结果表明，Triple-BERT在曼哈顿真实网约车数据集上取得了显著的性能提升。与当前最先进的方法相比，Triple-BERT的服务订单增加了4.26%，接送时间减少了22.25%，整体性能提升了约11.95%。这些数据表明，Triple-BERT能够有效地提高订单调度效率，改善用户体验。

## 🎯 应用场景

该研究成果可直接应用于网约车平台，提高订单调度效率，减少乘客等待时间，增加司机收入。此外，该方法也可推广到其他具有大规模状态和动作空间的调度问题，例如物流配送、智能仓储等领域，具有广泛的应用前景和实际价值。

## 📄 摘要（原文）

> On-demand ride-sharing platforms, such as Uber and Lyft, face the intricate real-time challenge of bundling and matching passengers-each with distinct origins and destinations-to available vehicles, all while navigating significant system uncertainties. Due to the extensive observation space arising from the large number of drivers and orders, order dispatching, though fundamentally a centralized task, is often addressed using Multi-Agent Reinforcement Learning (MARL). However, independent MARL methods fail to capture global information and exhibit poor cooperation among workers, while Centralized Training Decentralized Execution (CTDE) MARL methods suffer from the curse of dimensionality. To overcome these challenges, we propose Triple-BERT, a centralized Single Agent Reinforcement Learning (MARL) method designed specifically for large-scale order dispatching on ride-sharing platforms. Built on a variant TD3, our approach addresses the vast action space through an action decomposition strategy that breaks down the joint action probability into individual driver action probabilities. To handle the extensive observation space, we introduce a novel BERT-based network, where parameter reuse mitigates parameter growth as the number of drivers and orders increases, and the attention mechanism effectively captures the complex relationships among the large pool of driver and orders. We validate our method using a real-world ride-hailing dataset from Manhattan. Triple-BERT achieves approximately an 11.95% improvement over current state-of-the-art methods, with a 4.26% increase in served orders and a 22.25% reduction in pickup times. Our code, trained model parameters, and processed data are publicly available at the repository https://github.com/RS2002/Triple-BERT .

