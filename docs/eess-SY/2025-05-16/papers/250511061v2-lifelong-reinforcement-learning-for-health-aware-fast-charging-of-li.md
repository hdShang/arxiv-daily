---
layout: default
title: Lifelong reinforcement learning for health-aware fast charging of lithium-ion batteries
---

# Lifelong reinforcement learning for health-aware fast charging of lithium-ion batteries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11061" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11061v2</a>
  <a href="https://arxiv.org/pdf/2505.11061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11061v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11061v2', 'Lifelong reinforcement learning for health-aware fast charging of lithium-ion batteries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meng Yuan, Changfu Zou

**分类**: eess.SY

**发布日期**: 2025-05-16 (更新: 2025-07-06)

---

## 💡 一句话要点

**提出健康感知的快速充电策略以解决锂离子电池寿命问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `锂离子电池` `快速充电` `健康感知` `深度强化学习` `电池管理系统` `电池寿命` `充电策略`

## 📋 核心要点

1. 现有快速充电方法可能导致锂离子电池加速退化，影响其使用寿命。
2. 提出了一种健康感知的快速充电策略，通过映射阳极过电位与电池健康状态来优化充电过程。
3. 实验结果表明，TD3控制器在减少电池退化的同时，仍能保持竞争力的快速充电时间。

## 📝 摘要（中文）

锂离子电池的快速充电仍然是电动汽车和固定能源存储系统广泛应用的关键瓶颈，因不当设计的快速充电会加速电池退化并缩短使用寿命。本文提出了一种健康感知的快速充电策略，明确平衡充电速度与电池寿命。关键创新在于建立阳极过电位与电池健康状态（SoH）之间的映射，并在双延迟深度确定性策略梯度（TD3）框架中使用该映射来约束终端充电电压。通过引入SoH依赖的电压约束，所设计的深度学习方法有效减轻副反应并延长电池寿命。通过与传统的CC-CV及其变体进行生命周期模拟比较，TD3控制器在保持快速充电时间的同时减少了整体退化，展示了深度强化学习在先进电池管理系统中的实际可行性。

## 🔬 方法详解

**问题定义**：本文旨在解决锂离子电池快速充电过程中，因不当充电策略导致的电池退化和寿命缩短的问题。现有方法往往未能有效平衡充电速度与电池健康，造成电池性能下降。

**核心思路**：论文提出的健康感知快速充电策略，通过建立阳极过电位与电池健康状态（SoH）之间的映射，来约束充电电压，从而优化充电过程，延长电池寿命。

**技术框架**：整体架构基于双延迟深度确定性策略梯度（TD3）框架，主要模块包括SoH映射模块、充电电压约束模块和深度学习控制器。通过这些模块，系统能够实时调整充电策略以适应电池的健康状态。

**关键创新**：最重要的技术创新在于将电池健康状态与充电电压的动态映射结合，形成了一种新的充电策略。这一方法与传统的恒流-恒压（CC-CV）方法本质上不同，后者未能考虑电池的实时健康状态。

**关键设计**：在设计中，关键参数包括SoH的实时监测、阳极过电位的动态调整，以及损失函数的设计，确保在充电过程中有效减轻副反应，延长电池使用寿命。

## 📊 实验亮点

实验结果显示，TD3控制器在与传统CC-CV及其变体的生命周期模拟比较中，显著减少了电池的整体退化，充电时间仍保持在竞争力水平。这表明该方法在实际应用中具有良好的性能和可行性。

## 🎯 应用场景

该研究的潜在应用领域包括电动汽车和固定能源存储系统的电池管理。通过优化充电策略，不仅可以提高电池的使用效率，还能延长电池的整体寿命，具有重要的经济和环境价值。未来，该方法可能推动健康感知充电技术的广泛应用，促进可持续能源的发展。

## 📄 摘要（原文）

> Fast charging of lithium-ion batteries remains a critical bottleneck for widespread adoption of electric vehicles and stationary energy storage systems, as improperly designed fast charging can accelerate battery degradation and shorten lifespan. In this work, we address this challenge by proposing a health-aware fast charging strategy that explicitly balances charging speed and battery longevity across the entire service life. The key innovation lies in establishing a mapping between anode overpotential and the state of health (SoH) of battery, which is then used to constrain the terminal charging voltage in a twin delayed deep deterministic policy gradient (TD3) framework. By incorporating this SoH-dependent voltage constraint, our designed deep learning method mitigates side reactions and effectively extends battery life. To validate the proposed approach, a high-fidelity single particle model with electrolyte is implemented in the widely adopted PyBaMM simulation platform, capturing degradation phenomena at realistic scales. Comparative life-cycle simulations against conventional CC-CV, its variants, and constant current-constant overpotential methods show that the TD3-based controller reduces overall degradation while maintaining competitively fast charge times. These results demonstrate the practical viability of deep reinforcement learning for advanced battery management systems and pave the way for future explorations of health-aware, performance-optimized charging strategies.

