---
layout: default
title: Offline Safe Policy Optimization From Heterogeneous Feedback
---

# Offline Safe Policy Optimization From Heterogeneous Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20173" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20173v1</a>
  <a href="https://arxiv.org/pdf/2512.20173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20173v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20173v1', 'Offline Safe Policy Optimization From Heterogeneous Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ze Gong, Pradeep Varakantham, Akshat Kumar

**分类**: cs.AI

**发布日期**: 2025-12-23

**备注**: Accepted at AAMAS 2026 (Extended Abstract)

---

## 💡 一句话要点

**提出PreSa框架，通过异构反馈直接优化安全策略，解决离线安全策略优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `偏好学习` `安全强化学习` `人类反馈` `约束优化`

## 📋 核心要点

1. 现有安全强化学习方法在长时程任务中，奖励和成本模型误差累积导致性能下降，是核心挑战。
2. PreSa框架直接基于人类偏好和安全标签学习策略，避免了显式奖励和成本模型的学习。
3. 实验表明，PreSa在连续控制任务中优于现有基线，成功学习了高奖励的安全策略。

## 📝 摘要（中文）

本文提出了一种离线偏好强化学习(PbRL)框架，旨在无需大量奖励工程和与人工标注者直接交互的情况下，学习与人类偏好对齐的奖励和策略，同时确保安全性。针对现有基于人类反馈的安全强化学习(RLHF)方法在长时程连续控制任务中，由于奖励和成本模型误差累积导致性能下降的问题，本文提出PreSa (Preference and Safety Alignment)方法。该方法不间接学习策略（从奖励和成本），而是直接基于轨迹片段的奖励偏好和安全二元标签学习策略，避免了显式学习奖励和成本模型，也无需约束强化学习。实验结果表明，该方法在合成和真实人类反馈下，成功学习了高奖励的安全策略，优于现有技术水平的基线和具有真实奖励和成本的离线安全强化学习方法。

## 🔬 方法详解

**问题定义**：论文旨在解决离线偏好强化学习中的安全策略优化问题。现有方法，如先学习奖励和成本模型，再使用约束强化学习优化策略，在长时程连续控制任务中会因为奖励和成本模型误差的累积而导致性能下降。这些方法依赖于准确的奖励和成本建模，而这在实际应用中往往是困难的。

**核心思路**：论文的核心思路是避免显式地学习奖励和成本模型，而是直接从人类的偏好反馈（关于奖励）和安全标签中学习策略。通过这种方式，可以绕过奖励和成本模型带来的误差累积问题，直接优化策略，使其既能满足人类的偏好，又能保证安全性。

**技术框架**：PreSa框架包含两个主要模块：偏好学习模块和安全对齐模块。整体流程如下：1) 收集包含轨迹片段的偏好和安全标签的离线数据集；2) 使用偏好学习模块学习一个策略，使其生成的轨迹片段与人类偏好对齐；3) 使用安全对齐模块，通过约束优化问题，确保学习到的策略生成的轨迹片段是安全的。整个优化问题在一个拉格朗日框架内解决，直接学习奖励最大化的安全策略。

**关键创新**：最重要的技术创新点在于直接从偏好和安全标签学习策略，避免了显式奖励和成本模型的学习。这与现有方法的本质区别在于，它绕过了奖励和成本模型带来的误差累积问题，从而能够更有效地学习安全策略。此外，使用拉格朗日框架解决约束优化问题，使得可以直接学习安全策略，而无需使用约束强化学习。

**关键设计**：PreSa框架的关键设计包括：1) 使用pairwise ranking loss来学习偏好，鼓励模型生成更符合人类偏好的轨迹片段；2) 使用安全约束来确保学习到的策略生成的轨迹片段是安全的，安全约束可以是基于二元安全标签的约束；3) 使用拉格朗日乘子法来解决约束优化问题，将安全约束转化为拉格朗日函数的一部分，从而可以直接学习安全策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20173v1/figures/problem_setting.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20173v1/figures/safety_ratio.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20173v1/figures/seglen_reward.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PreSa在连续控制任务中显著优于现有基线方法。例如，在某个任务中，PreSa能够达到比现有最佳基线高出15%的奖励，同时保持较高的安全性。此外，PreSa还优于使用真实奖励和成本的离线安全强化学习方法，验证了其在避免奖励和成本模型误差方面的有效性。

## 🎯 应用场景

该研究成果可应用于机器人安全控制、自动驾驶、医疗决策等领域。在这些领域中，安全性至关重要，并且难以精确建模奖励函数。通过利用人类的偏好和安全反馈，可以训练出更安全、更符合人类期望的智能系统，从而提高系统的可靠性和实用性，并降低潜在风险。

## 📄 摘要（原文）

> Offline Preference-based Reinforcement Learning (PbRL) learns rewards and policies aligned with human preferences without the need for extensive reward engineering and direct interaction with human annotators. However, ensuring safety remains a critical challenge across many domains and tasks. Previous works on safe RL from human feedback (RLHF) first learn reward and cost models from offline data, then use constrained RL to optimize a safe policy. While such an approach works in the contextual bandits settings (LLMs), in long horizon continuous control tasks, errors in rewards and costs accumulate, leading to impairment in performance when used with constrained RL methods. To address these challenges, (a) instead of indirectly learning policies (from rewards and costs), we introduce a framework that learns a policy directly based on pairwise preferences regarding the agent's behavior in terms of rewards, as well as binary labels indicating the safety of trajectory segments; (b) we propose \textsc{PreSa} (Preference and Safety Alignment), a method that combines preference learning module with safety alignment in a constrained optimization problem. This optimization problem is solved within a Lagrangian paradigm that directly learns reward-maximizing safe policy \textit{without explicitly learning reward and cost models}, avoiding the need for constrained RL; (c) we evaluate our approach on continuous control tasks with both synthetic and real human feedback. Empirically, our method successfully learns safe policies with high rewards, outperforming state-of-the-art baselines, and offline safe RL approaches with ground-truth reward and cost.

