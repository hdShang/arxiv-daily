---
layout: default
title: Interaction-Aware Parameter Privacy-Preserving Data Sharing in Coupled Systems via Particle Filter Reinforcement Learning
---

# Interaction-Aware Parameter Privacy-Preserving Data Sharing in Coupled Systems via Particle Filter Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06122" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06122v1</a>
  <a href="https://arxiv.org/pdf/2505.06122.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06122v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06122v1', 'Interaction-Aware Parameter Privacy-Preserving Data Sharing in Coupled Systems via Particle Filter Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haokun Yu, Jingyuan Zhou, Kaidi Yang

**分类**: eess.SY

**发布日期**: 2025-05-09

**备注**: 21 pages, 8 figures, accepted at the 7th Annual Learning for Dynamics and Control (L4DC) Conference, 2025

---

## 💡 一句话要点

**提出交互感知的参数隐私保护数据共享方法以解决耦合系统问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `隐私保护` `数据共享` `耦合系统` `粒子滤波` `强化学习` `智能交通` `自动驾驶`

## 📋 核心要点

1. 核心问题：现有方法在耦合系统中难以同时满足数据共享与隐私保护的需求，存在隐私泄露风险。
2. 方法要点：提出了一种交互感知的隐私保护数据共享方法，通过优化互信息和控制性能的影响来生成失真数据。
3. 实验或效果：在混合自主车队场景中验证了方法的有效性，成功保护了敏感参数，且对燃油效率影响极小。

## 📝 摘要（中文）

本文解决了耦合系统中参数隐私保护的数据共享问题。在该场景中，数据提供者希望在共享数据的同时保护其敏感参数。共享数据不仅影响数据用户的决策，还通过系统交互影响数据提供者的操作。为平衡控制性能与隐私保护，提出了一种交互感知的隐私保护数据共享方法。该方法通过最小化互信息和失真数据对数据提供者控制性能的影响来生成失真数据，并将优化问题形式化为贝尔曼方程，利用粒子滤波强化学习方法求解。实验结果表明，该方法有效保护人类驾驶车辆的敏感驾驶行为参数，且对燃油效率的影响微乎其微。

## 🔬 方法详解

**问题定义**：本文旨在解决耦合系统中数据共享时的参数隐私保护问题。现有方法往往无法有效平衡数据用户的需求与数据提供者的隐私保护，导致敏感参数泄露的风险增加。

**核心思路**：提出的交互感知隐私保护数据共享方法通过生成失真数据来降低敏感参数的隐私泄露，同时考虑到数据用户与提供者之间的系统交互影响。该方法通过最小化互信息与控制性能损失的组合来实现。

**技术框架**：整体架构包括数据共享模块、隐私保护模块和优化求解模块。数据共享模块负责数据的初步处理，隐私保护模块通过优化算法生成失真数据，优化求解模块则利用粒子滤波强化学习方法解决贝尔曼方程。

**关键创新**：该方法的主要创新在于引入了交互感知机制，使得隐私保护与控制性能的优化能够同时进行，显著减少了历史依赖性，并有效处理连续状态空间的场景。

**关键设计**：在损失函数设计上，结合了互信息与控制性能损失，确保在保护隐私的同时不影响系统的整体性能。粒子滤波强化学习的应用使得优化过程更加高效，适应性更强。

## 📊 实验亮点

实验结果显示，提出的方法在混合自主车队场景中成功保护了人类驾驶车辆的敏感驾驶行为参数，且对燃油效率的影响几乎可以忽略不计。与现有强化学习方法相比，显著降低了历史依赖性，提高了在连续状态空间中的处理效率。

## 🎯 应用场景

该研究在智能交通系统、自动驾驶和数据隐私保护等领域具有广泛的应用潜力。通过有效保护敏感参数，能够提升人类驾驶车辆在混合自主环境中的安全性和隐私性，促进智能交通技术的进一步发展与应用。

## 📄 摘要（原文）

> This paper addresses the problem of parameter privacy-preserving data sharing in coupled systems, where a data provider shares data with a data user but wants to protect its sensitive parameters. The shared data affects not only the data user's decision-making but also the data provider's operations through system interactions. To trade off control performance and privacy, we propose an interaction-aware privacy-preserving data sharing approach. Our approach generates distorted data by minimizing a combination of (i) mutual information, quantifying privacy leakage of sensitive parameters, and (ii) the impact of distorted data on the data provider's control performance, considering the interactions between stakeholders. The optimization problem is formulated into a Bellman equation and solved by a particle filter reinforcement learning (RL)-based approach. Compared to existing RL-based methods, our formulation significantly reduces history dependency and efficiently handles scenarios with continuous state space. Validated in a mixed-autonomy platoon scenario, our method effectively protects sensitive driving behavior parameters of human-driven vehicles (HDVs) against inference attacks while maintaining negligible impact on fuel efficiency.

