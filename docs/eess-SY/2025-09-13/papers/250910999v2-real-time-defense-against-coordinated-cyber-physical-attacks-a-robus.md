---
layout: default
title: "Real-Time Defense Against Coordinated Cyber-Physical Attacks: A Robust Constrained Reinforcement Learning Approach"
---

# Real-Time Defense Against Coordinated Cyber-Physical Attacks: A Robust Constrained Reinforcement Learning Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10999" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10999v2</a>
  <a href="https://arxiv.org/pdf/2509.10999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10999v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10999v2', 'Real-Time Defense Against Coordinated Cyber-Physical Attacks: A Robust Constrained Reinforcement Learning Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saman Mazaheri Khamaneh, Tong Wu, Wei Sun, Cong Chen

**分类**: eess.SY, eess.SP

**发布日期**: 2025-09-13 (更新: 2025-09-16)

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出鲁棒约束强化学习框架，实时防御电力系统中的协同网络物理攻击。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `网络物理攻击` `鲁棒约束强化学习` `电力系统安全` `实时防御` `AC-OPF` `N-K攻击` `级联故障` `关键基础设施`

## 📋 核心要点

1. 现有电力系统安全方法难以高效识别最坏攻击场景并快速响应，易导致级联故障。
2. 提出三层鲁棒约束强化学习框架，无需预定义攻击模式，缓解各种运行条件下的攻击。
3. 实验表明，该策略能快速响应协同攻击，在0.21毫秒内恢复系统约束，提升系统弹性。

## 📝 摘要（中文）

现代电力系统面临日益复杂的网络物理攻击，这些攻击超出了传统的N-1安全准则。现有安全范式的瓶颈在于：高效识别最坏情况和快速协调防御响应受到计算密集性和时间延迟的限制，这可能导致级联故障的传播。本文提出了一种新颖的三层鲁棒约束强化学习(RCRL)框架，用于增强电力系统的鲁棒性。该框架通过AC-OPF公式生成多样化的系统状态，识别每个状态下的最坏情况N-K攻击场景，并训练策略来缓解所有运行条件下的这些场景，而无需预定义的攻击模式。该框架通过训练期间基于Beta混合投影的可行动作映射技术和部署期间的原始-对偶增广拉格朗日优化来解决约束满足问题。训练完成后，RCRL策略能够实时控制观察到的网络物理攻击。在IEEE基准系统上的验证表明，该方法对导致网络中广泛级联故障的协同N-K攻击有效。学习到的策略能够快速响应，在0.21毫秒的推理时间内将系统范围内的约束恢复到正常状态，从而为关键基础设施保护建立了卓越的弹性。

## 🔬 方法详解

**问题定义**：电力系统面临日益复杂的协同网络物理攻击，传统的N-1安全准则已不足以应对。现有方法在识别最坏情况攻击场景和协调防御响应方面存在计算瓶颈和时间延迟，容易导致级联故障，影响电力系统的稳定运行。因此，需要一种能够实时、鲁棒地防御此类攻击的方法。

**核心思路**：本文的核心思路是利用鲁棒约束强化学习（RCRL）来学习一种防御策略，该策略能够在各种运行条件下，针对最坏情况的N-K攻击做出快速响应。通过将攻击场景建模为不确定性集合，并利用强化学习算法来寻找在该集合下表现最佳的防御策略，从而提高系统的鲁棒性。同时，通过约束处理技术，确保防御策略满足电力系统的运行约束。

**技术框架**：该框架包含三个主要层次：1) 系统状态生成层：利用AC-OPF公式生成多样化的电力系统运行状态。2) 最坏情况攻击识别层：针对每个系统状态，识别出能够造成最大损害的N-K攻击场景。3) 防御策略学习层：利用RCRL算法，学习一种能够缓解这些攻击场景的防御策略。在部署阶段，使用原始-对偶增广拉格朗日优化来确保约束满足。

**关键创新**：该方法的主要创新在于：1) 提出了一种三层RCRL框架，能够有效地防御电力系统中的协同网络物理攻击。2) 采用鲁棒优化方法来处理攻击场景的不确定性，提高了防御策略的鲁棒性。3) 利用Beta-blending投影技术和原始-对偶增广拉格朗日优化来处理约束，确保防御策略的可行性。4) 无需预定义攻击模式，能够适应各种未知的攻击场景。

**关键设计**：在RCRL算法中，使用了深度神经网络来近似值函数和策略函数。损失函数包括强化学习的奖励函数和约束违反项。Beta-blending投影用于将动作映射到可行域内。原始-对偶增广拉格朗日优化用于在部署阶段确保约束满足。具体的网络结构和参数设置需要根据具体的电力系统进行调整。

## 📊 实验亮点

实验结果表明，该RCRL策略能够有效防御协同N-K攻击，并在0.21毫秒的推理时间内将系统约束恢复到正常状态。与传统的防御方法相比，该方法能够显著提高电力系统的鲁棒性和响应速度，有效防止级联故障的发生。

## 🎯 应用场景

该研究成果可应用于电力系统的实时安全防御，提高电力系统对网络物理攻击的抵抗能力，保障电力系统的稳定运行。此外，该方法也可推广到其他关键基础设施的安全防护领域，例如智能交通系统、水资源管理系统等，具有重要的实际应用价值和广泛的应用前景。

## 📄 摘要（原文）

> Modern power systems face increasing vulnerability to sophisticated cyber-physical attacks beyond traditional N-1 contingency frameworks. Existing security paradigms face a critical bottleneck: efficiently identifying worst-case scenarios and rapidly coordinating defensive responses are hindered by intensive computation and time delays, during which cascading failures can propagate. This paper presents a novel tri-level robust constrained reinforcement learning (RCRL) framework for robust power system security. The framework generates diverse system states through AC-OPF formulations, identifies worst-case N-K attack scenarios for each state, and trains policies to mitigate these scenarios across all operating conditions without requiring predefined attack patterns. The framework addresses constraint satisfaction through Beta-blending projection-based feasible action mapping techniques during training and primal-dual augmented Lagrangian optimization for deployment. Once trained, the RCRL policy learns how to control observed cyber-physical attacks in real time. Validation on IEEE benchmark systems demonstrates effectiveness against coordinated N-K attacks, causing widespread cascading failures throughout the network. The learned policy can successfully respond rapidly to recover system-wide constraints back to normal within 0.21 ms inference times, establishing superior resilience for critical infrastructure protection.

