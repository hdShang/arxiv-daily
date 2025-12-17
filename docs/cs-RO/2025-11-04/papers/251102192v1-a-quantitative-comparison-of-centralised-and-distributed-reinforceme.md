---
layout: default
title: A Quantitative Comparison of Centralised and Distributed Reinforcement Learning-Based Control for Soft Robotic Arms
---

# A Quantitative Comparison of Centralised and Distributed Reinforcement Learning-Based Control for Soft Robotic Arms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02192" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02192v1</a>
  <a href="https://arxiv.org/pdf/2511.02192.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02192v1" onclick="toggleFavorite(this, '2511.02192v1', 'A Quantitative Comparison of Centralised and Distributed Reinforcement Learning-Based Control for Soft Robotic Arms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linxin Hou, Qirui Wu, Zhihang Qin, Neil Banerjee, Yongxin Guo, Cecilia Laschi

**分类**: cs.RO

**发布日期**: 2025-11-04

**备注**: 7 pages, 4 figures, 2 tables, submitted to RoboSoft 2026

---

## 💡 一句话要点

**对比集中式与分布式强化学习控制软体机械臂，为软体机器人控制提供设计指导。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `软体机器人` `强化学习` `分布式控制` `集中式控制` `多智能体强化学习`

## 📋 核心要点

1. 软体机器人控制面临高维度、非线性等挑战，传统控制方法难以有效应对复杂环境。
2. 采用集中式和分布式多智能体强化学习，对比两种架构在软体机械臂控制中的性能差异。
3. 实验表明，分布式策略在高自由度下具有更高样本效率和鲁棒性，但集中式策略训练速度更快。

## 📝 摘要（中文）

本文对集中式和分布式多智能体强化学习(MARL)架构在控制软体机械臂方面的性能进行了定量比较，该软体机械臂在仿真环境中被建模为Cosserat杆。使用PyElastica和OpenAI Gym接口，我们在相同的计算资源下训练了全局近端策略优化(PPO)控制器和多智能体PPO(MAPPO)。两种方法都基于手臂具有n个可控部分。该研究系统地改变n，并评估手臂在三种场景中到达固定目标的能力：默认基线条件、从外部干扰中恢复以及适应执行器故障。用于评估的定量指标是平均动作幅度、平均最终距离、平均episode长度和成功率。结果表明，当可控部分数量n≤4时，分布式策略没有显著优势。在非常简单的系统(n≤2)中，集中式策略优于分布式策略。当n增加到4<n≤12时，分布式策略显示出更高的样本效率。在这些系统中，分布式策略在局部可观测性下提高了成功率、弹性和鲁棒性，并在相同样本量下实现了更快的收敛。然而，集中式策略在训练过程中实现了更高的时间效率，因为训练相同大小的样本花费的时间更少。这些发现突出了基于强化学习的软体机器人控制中集中式和分布式策略之间的权衡，并为未来软杆状机械手中的sim-to-real迁移提供了可操作的设计指导。

## 🔬 方法详解

**问题定义**：论文旨在解决软体机械臂的控制问题，特别是如何在集中式和分布式强化学习架构之间做出选择，以实现更好的控制性能。现有方法在处理高维度、复杂动态的软体机器人时存在局限性，需要探索更有效的控制策略。

**核心思路**：论文的核心思路是通过对比集中式和分布式强化学习方法在控制软体机械臂时的性能，揭示两种架构的优缺点，从而为软体机器人控制系统的设计提供指导。分布式方法通过局部观测和控制，有望提高鲁棒性和适应性。

**技术框架**：整体框架包括：1) 使用PyElastica对软体机械臂进行建模；2) 通过OpenAI Gym接口构建强化学习环境；3) 分别训练集中式PPO和分布式MAPPO控制器；4) 在不同场景下评估控制器的性能，包括基线条件、抗干扰和容错能力。

**关键创新**：论文的关键创新在于对集中式和分布式强化学习在软体机器人控制中的性能进行了定量比较，并分析了不同控制单元数量下两种架构的优劣。这为软体机器人控制策略的选择提供了理论依据和实验数据。

**关键设计**：论文的关键设计包括：1) 使用Cosserat杆模型模拟软体机械臂；2) 采用PPO和MAPPO算法进行训练；3) 通过平均动作幅度、平均最终距离、平均episode长度和成功率等指标评估性能；4) 系统地改变可控部分的数量n，以研究其对控制性能的影响。

## 📊 实验亮点

实验结果表明，当可控部分数量n≤4时，集中式策略在简单系统中表现更优。当4<n≤12时，分布式策略展现出更高的样本效率、成功率和鲁棒性。集中式策略训练速度更快，但分布式策略在复杂系统中具有优势，为软体机器人控制策略选择提供了依据。

## 🎯 应用场景

该研究成果可应用于医疗机器人、康复机器人、搜救机器人等领域，尤其是在需要高柔性和适应性的复杂环境中。通过选择合适的控制架构，可以提高软体机器人的操作精度、鲁棒性和安全性，从而更好地完成各种任务。

## 📄 摘要（原文）

> This paper presents a quantitative comparison between centralised and distributed multi-agent reinforcement learning (MARL) architectures for controlling a soft robotic arm modelled as a Cosserat rod in simulation. Using PyElastica and the OpenAI Gym interface, we train both a global Proximal Policy Optimisation (PPO) controller and a Multi-Agent PPO (MAPPO) under identical budgets. Both approaches are based on the arm having $n$ number of controlled sections. The study systematically varies $n$ and evaluates the performance of the arm to reach a fixed target in three scenarios: default baseline condition, recovery from external disturbance, and adaptation to actuator failure. Quantitative metrics used for the evaluation are mean action magnitude, mean final distance, mean episode length, and success rate. The results show that there are no significant benefits of the distributed policy when the number of controlled sections $n\le4$. In very simple systems, when $n\le2$, the centralised policy outperforms the distributed one. When $n$ increases to $4< n\le 12$, the distributed policy shows a high sample efficiency. In these systems, distributed policy promotes a stronger success rate, resilience, and robustness under local observability and yields faster convergence given the same sample size. However, centralised policies achieve much higher time efficiency during training as it takes much less time to train the same size of samples. These findings highlight the trade-offs between centralised and distributed policy in reinforcement learning-based control for soft robotic systems and provide actionable design guidance for future sim-to-real transfer in soft rod-like manipulators.

