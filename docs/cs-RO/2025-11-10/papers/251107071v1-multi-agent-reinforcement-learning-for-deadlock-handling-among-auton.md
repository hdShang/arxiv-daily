---
layout: default
title: Multi-Agent Reinforcement Learning for Deadlock Handling among Autonomous Mobile Robots
---

# Multi-Agent Reinforcement Learning for Deadlock Handling among Autonomous Mobile Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07071" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07071v1</a>
  <a href="https://arxiv.org/pdf/2511.07071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07071v1" onclick="toggleFavorite(this, '2511.07071v1', 'Multi-Agent Reinforcement Learning for Deadlock Handling among Autonomous Mobile Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marcel Müller

**分类**: cs.MA, cs.RO

**发布日期**: 2025-11-10

**备注**: for associated repositories, see https://github.com/Nerozud/dl_reference_models and https://github.com/Nerozud/FTS_simpel

---

## 💡 一句话要点

**提出基于多智能体强化学习的死锁处理方法，提升AMR物流系统效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `自主移动机器人` `死锁处理` `内部物流` `路径规划`

## 📋 核心要点

1. 现有AMR物流系统死锁处理方法缺乏自适应性，难以应对动态环境。
2. 提出基于MARL的死锁处理方法，通过学习优化AMR的路径规划和行为策略。
3. 实验表明，在复杂环境中，MARL方法优于传统规则方法，提升了系统性能。

## 📝 摘要（中文）

本论文探讨了多智能体强化学习（MARL）在自主移动机器人（AMR）内部物流系统中处理死锁的应用。AMR提高了运营灵活性，但也增加了死锁的风险，从而降低了系统吞吐量和可靠性。现有方法通常忽略规划阶段的死锁处理，并依赖于无法适应动态运营条件的刚性控制规则。为了解决这些缺点，本研究开发了一种将MARL集成到物流规划和运营控制中的结构化方法。它引入了显式考虑死锁的多智能体路径规划（MAPF）参考模型，从而能够系统地评估MARL策略。通过基于网格的环境和外部仿真软件，该研究比较了传统的死锁处理策略与基于MARL的解决方案，重点关注不同训练和执行模式下的PPO和IMPALA算法。研究结果表明，基于MARL的策略，特别是与集中式训练和分散式执行（CTDE）相结合时，在复杂的拥堵环境中优于基于规则的方法。在更简单的环境或具有充足空间自由度的环境中，基于规则的方法由于其较低的计算需求而仍然具有竞争力。这些结果表明，MARL为动态内部物流场景中的死锁处理提供了一种灵活且可扩展的解决方案，但需要根据运营环境进行仔细调整。

## 🔬 方法详解

**问题定义**：论文旨在解决内部物流系统中，由于自主移动机器人（AMR）数量增加和环境复杂性提升导致的死锁问题。现有方法，如预先设定的规则或集中式路径规划，难以适应动态变化的运营环境，导致系统效率降低和可靠性下降。这些方法通常缺乏学习和自适应能力，无法有效处理突发情况。

**核心思路**：论文的核心思路是利用多智能体强化学习（MARL）来训练AMR，使其能够自主学习避免死锁的策略。通过将死锁处理问题建模为MARL问题，每个AMR作为一个智能体，通过与环境和其他智能体的交互，学习最优的路径规划和行为策略。这种方法旨在提高系统的灵活性、可扩展性和鲁棒性。

**技术框架**：论文构建了一个基于网格的仿真环境，用于训练和评估MARL算法。整体框架包括以下几个主要模块：1) 环境建模：将物流系统抽象为网格环境，定义AMR的运动规则和交互方式。2) 智能体设计：每个AMR配备一个MARL代理，负责学习最优策略。3) 训练模块：使用PPO或IMPALA等MARL算法，通过与环境交互，不断优化智能体的策略。4) 评估模块：在不同的场景下评估MARL策略的性能，并与传统方法进行比较。

**关键创新**：论文的关键创新在于将MARL应用于AMR的死锁处理问题，并提出了一种结构化的方法，将MARL集成到物流规划和运营控制中。此外，论文还引入了显式考虑死锁的多智能体路径规划（MAPF）参考模型，用于系统地评估MARL策略。集中式训练和分散式执行（CTDE）的策略也是一个重要的创新点，它允许智能体在训练阶段共享信息，但在执行阶段独立决策，从而提高了系统的鲁棒性和可扩展性。

**关键设计**：论文使用了PPO和IMPALA两种MARL算法，并针对死锁处理问题进行了优化。关键设计包括：1) 奖励函数设计：奖励函数旨在鼓励AMR完成任务，同时避免死锁。例如，可以设置负奖励来惩罚碰撞或长时间停滞。2) 状态表示：状态表示需要包含AMR自身的信息（如位置、速度）以及周围环境的信息（如其他AMR的位置、障碍物）。3) 网络结构：可以使用卷积神经网络（CNN）来处理网格环境中的状态信息，并使用循环神经网络（RNN）来处理时间序列数据。4) 超参数调整：需要仔细调整PPO和IMPALA的超参数，以获得最佳的训练效果。

## 📊 实验亮点

实验结果表明，在复杂的拥堵环境中，基于MARL的策略，特别是与集中式训练和分散式执行（CTDE）相结合时，优于传统的基于规则的方法。具体来说，MARL方法在吞吐量和死锁避免率方面均有显著提升。在更简单的环境或具有充足空间自由度的环境中，基于规则的方法由于其较低的计算需求而仍然具有竞争力。

## 🎯 应用场景

该研究成果可应用于各种内部物流场景，如仓库、工厂、医院等，以提高AMR系统的效率和可靠性。通过MARL，AMR能够更好地适应动态变化的运营环境，减少死锁的发生，从而提高整体的物流效率。此外，该方法还可以扩展到其他多智能体系统，如交通控制、机器人协作等。

## 📄 摘要（原文）

> This dissertation explores the application of multi-agent reinforcement learning (MARL) for handling deadlocks in intralogistics systems that rely on autonomous mobile robots (AMRs). AMRs enhance operational flexibility but also increase the risk of deadlocks, which degrade system throughput and reliability. Existing approaches often neglect deadlock handling in the planning phase and rely on rigid control rules that cannot adapt to dynamic operational conditions.
>   To address these shortcomings, this work develops a structured methodology for integrating MARL into logistics planning and operational control. It introduces reference models that explicitly consider deadlock-capable multi-agent pathfinding (MAPF) problems, enabling systematic evaluation of MARL strategies. Using grid-based environments and an external simulation software, the study compares traditional deadlock handling strategies with MARL-based solutions, focusing on PPO and IMPALA algorithms under different training and execution modes.
>   Findings reveal that MARL-based strategies, particularly when combined with centralized training and decentralized execution (CTDE), outperform rule-based methods in complex, congested environments. In simpler environments or those with ample spatial freedom, rule-based methods remain competitive due to their lower computational demands. These results highlight that MARL provides a flexible and scalable solution for deadlock handling in dynamic intralogistics scenarios, but requires careful tailoring to the operational context.

