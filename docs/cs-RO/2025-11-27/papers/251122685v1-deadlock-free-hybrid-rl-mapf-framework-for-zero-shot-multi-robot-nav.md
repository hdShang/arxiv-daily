---
layout: default
title: Deadlock-Free Hybrid RL-MAPF Framework for Zero-Shot Multi-Robot Navigation
---

# Deadlock-Free Hybrid RL-MAPF Framework for Zero-Shot Multi-Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22685" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22685v1</a>
  <a href="https://arxiv.org/pdf/2511.22685.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22685v1" onclick="toggleFavorite(this, '2511.22685v1', 'Deadlock-Free Hybrid RL-MAPF Framework for Zero-Shot Multi-Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyi Wang, Licheng Luo, Yiannis Kantaros, Bruno Sinopoli, Mingyu Cai

**分类**: cs.RO

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**提出一种混合RL-MAPF框架，用于零样本多机器人无死锁导航**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多机器人导航` `强化学习` `多智能体路径规划` `死锁避免` `零样本学习`

## 📋 核心要点

1. 现有基于强化学习的多机器人导航方法在复杂环境中泛化能力不足，容易出现死锁。
2. 该论文提出一种混合框架，结合RL反应式导航和按需MAPF，显式解决死锁问题。
3. 实验表明，该方法显著提升了任务完成率，减少了死锁和碰撞，实现了零样本性能。

## 📝 摘要（中文）

在复杂环境中，多机器人导航面临着反应式避障与长距离目标实现之间的平衡难题。尤其是在狭窄通道或封闭空间中，当强化学习（RL）控制策略遇到学习分布之外的新配置时，经常出现死锁，阻碍机器人到达目的地。现有的基于RL的方法在未见过的环境中泛化能力有限。我们提出了一种混合框架，该框架无缝集成了基于RL的反应式导航和按需多智能体路径规划（MAPF），以显式地解决拓扑死锁。我们的方法集成了一个安全层，该安全层监控智能体的进度以检测死锁，并在检测到死锁时触发受影响智能体的协调控制器。该框架通过MAPF构建全局可行轨迹，并调节航点进度以减少导航期间的智能体间冲突。在密集的多智能体基准测试中进行的大量评估表明，我们的方法将任务完成率从边缘成功提升到接近普遍成功，显着减少了死锁和碰撞。当与分层任务规划集成时，它可以实现异构机器人的协调导航，表明将反应式RL导航与选择性MAPF干预相结合可产生强大的零样本性能。

## 🔬 方法详解

**问题定义**：多机器人导航在复杂环境中容易出现死锁，尤其是在狭窄空间内。现有的基于强化学习的方法泛化能力有限，难以应对未见过的环境配置，导致任务完成率低，碰撞率高。

**核心思路**：核心思路是将基于强化学习的反应式导航与多智能体路径规划（MAPF）相结合。RL负责局部避障和导航，MAPF则在检测到死锁时介入，进行全局路径规划，从而避免死锁。这种混合方法旨在兼顾反应速度和全局规划能力。

**技术框架**：该框架包含三个主要模块：1) 基于RL的反应式导航器：负责机器人的局部运动控制。2) 死锁检测器：监控机器人的运动状态，判断是否发生死锁。3) MAPF协调控制器：当检测到死锁时，触发MAPF算法为受影响的机器人规划全局路径，引导它们脱离死锁。框架通过调节航点进度来减少机器人间的冲突。

**关键创新**：关键创新在于将RL和MAPF无缝集成，实现了一种按需的全局规划机制。与完全依赖RL或MAPF的方法相比，该方法能够在保证反应速度的同时，有效地解决死锁问题，提升了整体导航性能。此外，该方法实现了零样本性能，无需针对特定环境进行训练。

**关键设计**：死锁检测器通过监控机器人的运动速度和与其他机器人的距离来判断是否发生死锁。MAPF协调控制器使用A*算法或其他MAPF求解器来生成无碰撞的全局路径。RL导航器可以使用任何合适的强化学习算法，例如PPO或DDPG。框架通过调节航点进度来减少机器人间的冲突，具体的调节策略未知。

## 📊 实验亮点

实验结果表明，该方法在密集的多智能体基准测试中，将任务完成率从边缘成功提升到接近普遍成功，显著减少了死锁和碰撞。与现有的基于RL的方法相比，该方法在未见过的环境中表现出更强的泛化能力和鲁棒性。此外，该方法能够与分层任务规划集成，实现异构机器人的协调导航。

## 🎯 应用场景

该研究成果可应用于仓库自动化、物流配送、服务机器人等领域，尤其是在拥挤和复杂的环境中，例如大型仓库、医院、商场等。通过该方法，可以实现多机器人的高效、安全、可靠的协同导航，提高工作效率，降低运营成本，并提升用户体验。未来，该技术有望扩展到更多类型的机器人和更复杂的应用场景。

## 📄 摘要（原文）

> Multi-robot navigation in cluttered environments presents fundamental challenges in balancing reactive collision avoidance with long-range goal achievement. When navigating through narrow passages
>   or confined spaces, deadlocks frequently emerge that prevent agents from reaching their destinations, particularly when Reinforcement Learning (RL) control policies encounter novel configurations out of learning distribution. Existing RL-based approaches suffer from limited generalization capability in unseen environments. We propose a hybrid framework that seamlessly integrates RL-based reactive navigation with on-demand Multi-Agent Path Finding (MAPF) to explicitly resolve topological deadlocks. Our approach integrates a safety layer that monitors agent progress to detect deadlocks and, when detected, triggers a coordination controller for affected agents. The framework constructs globally feasible trajectories via MAPF and regulates waypoint progression to reduce inter-agent conflicts during navigation.
>   Extensive evaluation on dense multi-agent benchmarks shows that our method boosts task completion from marginal to near-universal success, markedly reducing deadlocks and collisions. When integrated with hierarchical task planning, it enables coordinated navigation for heterogeneous robots, demonstrating that coupling reactive RL navigation with selective MAPF intervention yields a robust, zero-shot performance.

