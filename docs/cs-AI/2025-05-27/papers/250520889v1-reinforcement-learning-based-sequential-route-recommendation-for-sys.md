---
layout: default
title: Reinforcement Learning-based Sequential Route Recommendation for System-Optimal Traffic Assignment
---

# Reinforcement Learning-based Sequential Route Recommendation for System-Optimal Traffic Assignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20889" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20889v1</a>
  <a href="https://arxiv.org/pdf/2505.20889.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20889v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20889v1', 'Reinforcement Learning-based Sequential Route Recommendation for System-Optimal Traffic Assignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leizhen Wang, Peibo Duan, Cheng Lyu, Zhenliang Ma

**分类**: cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出基于强化学习的顺序路线推荐以解决系统最优交通分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `交通分配` `个性化推荐` `深度学习` `智能交通` `系统优化`

## 📋 核心要点

1. 现有的个性化路线推荐系统未能有效实现系统最优交通分配，导致整体交通效率低下。
2. 本文提出将静态系统最优交通分配问题转化为单代理深度强化学习任务，通过顺序推荐路线来优化整体旅行时间。
3. 实验结果显示，所提方法在Braess网络中收敛至理论最优解，在Ortuzar-Willumsen网络中偏差仅为0.35%。

## 📝 摘要（中文）

现代导航系统和共享出行平台越来越依赖个性化路线推荐来提升旅行体验和运营效率。然而，关键问题在于这些个性化的顺序路线决策是否能够共同实现系统最优交通分配。本文提出了一种学习框架，将静态系统最优交通分配问题重构为单代理深度强化学习任务。中心代理根据起点-终点需求的到达，顺序推荐路线以最小化总系统旅行时间。为提高学习效率和解决方案质量，本文开发了一种多阶段引导的深度Q学习算法，将传统交通分配方法的迭代结构融入强化学习训练过程中。实验结果表明，强化学习代理在Braess网络中收敛到理论的系统最优解，而在Ortuzar-Willumsen网络中仅有0.35%的偏差。

## 🔬 方法详解

**问题定义**：本文旨在解决个性化路线推荐如何实现系统最优交通分配的问题。现有方法往往无法有效整合个体决策与系统效率，导致整体交通流量不理想。

**核心思路**：论文的核心思路是将静态系统最优交通分配问题转化为单代理的深度强化学习任务，通过中心代理顺序推荐路线，以最小化系统的总旅行时间。这样的设计能够动态适应实时交通需求。

**技术框架**：整体架构包括一个中心代理，负责根据实时的起点-终点需求推荐路线。采用多阶段引导的深度Q学习算法，结合传统交通分配方法的迭代结构，提升学习效率和解决方案质量。

**关键创新**：最重要的技术创新在于将传统的交通分配方法与深度强化学习结合，形成了一种新的学习框架，使得个体的路线选择能够有效地与系统级效率相结合。

**关键设计**：在算法设计中，采用了多阶段引导的深度Q学习，设置了特定的损失函数以优化学习过程，并设计了SO-informed的路线动作集，以加快收敛速度和提升最终性能。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，所提强化学习代理在Braess网络中成功收敛至理论的系统最优解，而在Ortuzar-Willumsen网络中仅有0.35%的偏差，表明该方法在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、导航应用和共享出行平台。通过实现个性化的路线推荐与系统最优交通分配的结合，能够显著提升交通流量管理的效率，减少拥堵，提高用户出行体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Modern navigation systems and shared mobility platforms increasingly rely on personalized route recommendations to improve individual travel experience and operational efficiency. However, a key question remains: can such sequential, personalized routing decisions collectively lead to system-optimal (SO) traffic assignment? This paper addresses this question by proposing a learning-based framework that reformulates the static SO traffic assignment problem as a single-agent deep reinforcement learning (RL) task. A central agent sequentially recommends routes to travelers as origin-destination (OD) demands arrive, to minimize total system travel time. To enhance learning efficiency and solution quality, we develop an MSA-guided deep Q-learning algorithm that integrates the iterative structure of traditional traffic assignment methods into the RL training process. The proposed approach is evaluated on both the Braess and Ortuzar-Willumsen (OW) networks. Results show that the RL agent converges to the theoretical SO solution in the Braess network and achieves only a 0.35% deviation in the OW network. Further ablation studies demonstrate that the route action set's design significantly impacts convergence speed and final performance, with SO-informed route sets leading to faster learning and better outcomes. This work provides a theoretically grounded and practically relevant approach to bridging individual routing behavior with system-level efficiency through learning-based sequential assignment.

