---
layout: default
title: "DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving"
---

# DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17940" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17940v1</a>
  <a href="https://arxiv.org/pdf/2509.17940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17940v1', 'DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuyao Shang, Yuntao Chen, Yuqi Wang, Yingyan Li, Zhaoxiang Zhang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-22

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**DriveDPO：面向端到端自动驾驶的安全DPO策略学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `端到端自动驾驶` `直接偏好优化` `安全策略学习` `模仿学习` `规则驱动` `轨迹优化` `NAVSIM` `强化学习`

## 📋 核心要点

1. 模仿学习在端到端自动驾驶中面临安全挑战，难以区分类人但潜在危险的轨迹。
2. DriveDPO通过提炼人类模仿和规则安全分数，进行直接策略优化，实现安全驾驶。
3. 在NAVSIM基准测试中，DriveDPO达到了90.0的PDMS，并在复杂场景中表现出更安全可靠的驾驶行为。

## 📝 摘要（中文）

端到端自动驾驶通过直接从原始感知输入预测未来轨迹取得了显著进展，绕过了传统的模块化流程。然而，主流的模仿学习方法存在严重的安全限制，因为它们无法区分看起来像人类但可能不安全的轨迹。一些最近的方法试图通过回归多个规则驱动的分数来解决这个问题，但将监督与策略优化分离，导致次优性能。为了应对这些挑战，我们提出了DriveDPO，一个安全直接偏好优化策略学习框架。首先，我们从人类模仿相似性和基于规则的安全分数中提炼出一个统一的策略分布，用于直接策略优化。此外，我们引入了一个迭代的直接偏好优化阶段，将其表述为轨迹级别的偏好对齐。在NAVSIM基准上的大量实验表明，DriveDPO实现了90.0的最新PDMS。此外，各种具有挑战性的场景中的定性结果突出了DriveDPO产生更安全和更可靠的驾驶行为的能力。

## 🔬 方法详解

**问题定义**：现有端到端自动驾驶方法，特别是基于模仿学习的方法，在安全性方面存在不足。它们难以区分模仿人类驾驶行为但实际上不安全的轨迹，导致潜在的安全风险。虽然一些方法尝试引入规则驱动的安全评分，但这些评分与策略优化过程是分离的，导致性能次优。

**核心思路**：DriveDPO的核心思路是将人类驾驶行为的相似性和规则驱动的安全评分结合起来，提炼出一个统一的策略分布，并使用直接偏好优化（Direct Preference Optimization, DPO）方法来优化策略。通过直接对轨迹级别的偏好进行对齐，避免了传统方法中监督信号与策略优化分离的问题。

**技术框架**：DriveDPO框架包含两个主要阶段。首先，从人类模仿相似性和规则安全分数中提炼出一个统一的策略分布。然后，使用迭代的DPO阶段，将策略与轨迹级别的偏好对齐。整个框架以端到端的方式进行训练，直接从原始感知输入预测未来轨迹。

**关键创新**：DriveDPO的关键创新在于使用安全直接偏好优化策略学习框架，将人类驾驶行为的模仿和规则驱动的安全约束集成到一个统一的优化过程中。通过直接优化策略以符合人类偏好和安全规则，避免了传统方法中监督信号与策略优化分离的问题，从而提高了驾驶的安全性。

**关键设计**：DriveDPO使用DPO损失函数来对齐轨迹级别的偏好。具体来说，它通过比较不同轨迹的得分，鼓励模型选择更安全、更符合人类驾驶习惯的轨迹。此外，DriveDPO采用迭代的优化策略，逐步提高策略的性能和安全性。具体的网络结构和参数设置在论文中进行了详细描述，以确保模型能够有效地学习到安全驾驶策略。

## 📊 实验亮点

DriveDPO在NAVSIM基准测试中取得了显著成果，PDMS（Percentage of Driving Miles Safely）达到了90.0，超越了现有技术水平。定性结果表明，DriveDPO在各种具有挑战性的场景中能够产生更安全、更可靠的驾驶行为，例如在交通拥堵、行人穿越和恶劣天气等情况下。

## 🎯 应用场景

DriveDPO技术可应用于各种自动驾驶场景，包括城市道路、高速公路和越野环境。该技术能够提高自动驾驶系统的安全性，减少事故风险，并提升用户体验。此外，DriveDPO还可以用于训练更安全、更可靠的机器人和无人机，具有广泛的应用前景。

## 📄 摘要（原文）

> End-to-end autonomous driving has substantially progressed by directly predicting future trajectories from raw perception inputs, which bypasses traditional modular pipelines. However, mainstream methods trained via imitation learning suffer from critical safety limitations, as they fail to distinguish between trajectories that appear human-like but are potentially unsafe. Some recent approaches attempt to address this by regressing multiple rule-driven scores but decoupling supervision from policy optimization, resulting in suboptimal performance. To tackle these challenges, we propose DriveDPO, a Safety Direct Preference Optimization Policy Learning framework. First, we distill a unified policy distribution from human imitation similarity and rule-based safety scores for direct policy optimization. Further, we introduce an iterative Direct Preference Optimization stage formulated as trajectory-level preference alignment. Extensive experiments on the NAVSIM benchmark demonstrate that DriveDPO achieves a new state-of-the-art PDMS of 90.0. Furthermore, qualitative results across diverse challenging scenarios highlight DriveDPO's ability to produce safer and more reliable driving behaviors.

