---
layout: default
title: Automatic Curriculum Learning for Driving Scenarios: Towards Robust and Efficient Reinforcement Learning
---

# Automatic Curriculum Learning for Driving Scenarios: Towards Robust and Efficient Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08264" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08264v2</a>
  <a href="https://arxiv.org/pdf/2505.08264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08264v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08264v2', 'Automatic Curriculum Learning for Driving Scenarios: Towards Robust and Efficient Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Abouelazm, Tim Weinstein, Tim Joseph, Philip Schörner, J. Marius Zöllner

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-13 (更新: 2025-07-11)

**备注**: Accepted in the 36th IEEE Intelligent Vehicles Symposium (IV 2025)

---

## 💡 一句话要点

**提出自动课程学习框架以解决自主驾驶训练效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `强化学习` `课程学习` `场景生成` `训练效率` `泛化能力` `动态适应`

## 📋 核心要点

1. 现有的强化学习方法在固定场景下训练，导致代理的泛化能力不足，难以适应真实世界的复杂情况。
2. 本文提出的自动课程学习框架能够根据代理的学习能力动态生成驾驶场景，避免了专家设计的偏见和不灵活性。
3. 实验结果显示，该框架在不同交通密度下的成功率显著提高，并且训练效率得到改善，收敛速度加快。

## 📝 摘要（中文）

本文针对使用强化学习（RL）训练端到端自主驾驶代理所面临的挑战进行了探讨。现有的RL代理通常在固定场景下训练，限制了其泛化能力和实际部署效果。虽然领域随机化提供了一种可能的解决方案，但由于训练场景之间的高方差，常常导致训练效率低下和次优策略。为了解决这些问题，本文提出了一种自动课程学习框架，该框架根据代理的能力动态生成具有适应性复杂度的驾驶场景。与手动设计的课程不同，该框架通过一个“教师”自动生成和变异驾驶场景，基于代理当前策略的学习潜力，从而提高训练效率。实验结果表明，该方法在低交通密度和高交通密度下的成功率分别提高了9%和21%，并且收敛速度更快，训练步骤更少。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在固定场景下训练导致的泛化能力不足和训练效率低下的问题。现有方法在训练过程中缺乏灵活性，难以适应复杂的真实驾驶场景。

**核心思路**：提出了一种自动课程学习框架，该框架通过动态生成和调整驾驶场景的复杂度，依据代理的学习能力进行优化，从而提高训练效率和泛化能力。

**技术框架**：整体架构包括一个“教师”模块，该模块负责生成和变异驾驶场景，基于代理当前策略的学习潜力进行调整。框架还包含场景筛选机制，以排除代理已掌握或过于困难的场景。

**关键创新**：最重要的创新在于引入了自动生成和变异场景的“教师”机制，消除了手动设计带来的偏见，并提高了课程学习的可扩展性。与传统方法相比，该框架能够更有效地适应代理的学习进程。

**关键设计**：在设计中，采用了基于代理当前策略的学习潜力作为场景生成的依据，并设置了相应的参数以控制场景的复杂度和多样性。损失函数和网络结构的选择也经过优化，以支持高效的训练过程。

## 📊 实验亮点

实验结果表明，提出的自动课程学习框架在低交通密度下成功率提高了9%，在高交通密度下提高了21%。此外，该框架在训练步骤上也表现出更快的收敛速度，相较于基线方法显著提升了训练效率。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车的训练与开发，尤其是在复杂和动态的交通环境中。通过提高自主驾驶代理的训练效率和泛化能力，该框架能够加速自主驾驶技术的实际部署，提升道路安全性和驾驶体验。未来，该方法还可能扩展到其他需要动态适应的强化学习任务中。

## 📄 摘要（原文）

> This paper addresses the challenges of training end-to-end autonomous driving agents using Reinforcement Learning (RL). RL agents are typically trained in a fixed set of scenarios and nominal behavior of surrounding road users in simulations, limiting their generalization and real-life deployment. While domain randomization offers a potential solution by randomly sampling driving scenarios, it frequently results in inefficient training and sub-optimal policies due to the high variance among training scenarios. To address these limitations, we propose an automatic curriculum learning framework that dynamically generates driving scenarios with adaptive complexity based on the agent's evolving capabilities. Unlike manually designed curricula that introduce expert bias and lack scalability, our framework incorporates a ``teacher'' that automatically generates and mutates driving scenarios based on their learning potential -- an agent-centric metric derived from the agent's current policy -- eliminating the need for expert design. The framework enhances training efficiency by excluding scenarios the agent has mastered or finds too challenging. We evaluate our framework in a reinforcement learning setting where the agent learns a driving policy from camera images. Comparative results against baseline methods, including fixed scenario training and domain randomization, demonstrate that our approach leads to enhanced generalization, achieving higher success rates: +9% in low traffic density, +21% in high traffic density, and faster convergence with fewer training steps. Our findings highlight the potential of ACL in improving the robustness and efficiency of RL-based autonomous driving agents.

