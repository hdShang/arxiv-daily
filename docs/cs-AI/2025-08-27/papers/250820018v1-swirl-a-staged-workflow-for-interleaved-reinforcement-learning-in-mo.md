---
layout: default
title: "SWIRL: A Staged Workflow for Interleaved Reinforcement Learning in Mobile GUI Control"
---

# SWIRL: A Staged Workflow for Interleaved Reinforcement Learning in Mobile GUI Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20018" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20018v1</a>
  <a href="https://arxiv.org/pdf/2508.20018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20018v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20018v1', 'SWIRL: A Staged Workflow for Interleaved Reinforcement Learning in Mobile GUI Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quanfeng Lu, Zhantao Ma, Shuai Zhong, Jin Wang, Dahai Yu, Michael K. Ng, Ping Luo

**分类**: cs.AI, cs.CL, cs.CV, cs.MA

**发布日期**: 2025-08-27

**备注**: 28 pages, 12 figures

---

## 💡 一句话要点

**提出SWIRL以解决移动GUI控制中的多智能体强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动GUI控制` `多智能体系统` `强化学习` `视觉语言模型` `智能体协调` `数学推理` `实验验证`

## 📋 核心要点

1. 现有的单智能体方法在移动GUI控制中受到结构限制，无法有效处理复杂的界面操作。
2. SWIRL通过将多智能体强化学习转化为单智能体任务，逐个更新智能体，从而实现稳定训练和高效协调。
3. 实验结果表明，SWIRL在高层和低层GUI基准测试中表现优越，并在多智能体数学推理中展现出强大能力。

## 📝 摘要（中文）

随着大型视觉语言模型（LVLMs）和智能体系统的快速发展，移动GUI智能体的研究受到关注，然而现有的单智能体方法受到结构限制。尽管多智能体系统能够自然地解耦不同的能力，但多智能体强化学习（MARL）的效率问题和与现有LVLM架构的不兼容性仍然存在。为了解决这些挑战，本文提出了SWIRL，一个为多智能体系统设计的交错强化学习的分阶段工作流。SWIRL将MARL重新表述为一系列单智能体强化学习任务，逐个更新智能体，同时保持其他智能体固定。这种方法促进了稳定的训练和高效的协调。通过大量实验，SWIRL在高层和低层GUI基准测试中表现出优越的性能，并在多智能体数学推理中展现出强大的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决移动GUI控制中多智能体强化学习的效率问题，现有方法在处理复杂任务时存在结构限制和协调困难。

**核心思路**：SWIRL的核心思路是将多智能体强化学习转化为一系列单智能体任务，逐个更新智能体，保持其他智能体固定，从而实现稳定的训练过程。

**技术框架**：SWIRL的整体架构包括两个主要模块：Navigator和Interactor。Navigator负责将自然语言和屏幕上下文转化为结构化计划，而Interactor则将这些计划转化为可执行的原子动作。

**关键创新**：SWIRL的主要创新在于其将MARL重构为单智能体任务的方式，这种方法提高了训练的稳定性和效率，与传统的多智能体方法相比，能够更好地协调智能体之间的交互。

**关键设计**：SWIRL设计了逐步安全界限、跨轮单调改进定理和收益收敛保证等理论框架，确保了优化过程的稳健性和原则性。

## 📊 实验亮点

SWIRL在高层和低层GUI基准测试中表现出色，实验结果显示其性能优于现有基线，具体提升幅度达到XX%（具体数据未提供）。此外，SWIRL在多智能体数学推理任务中也展现了强大的能力，进一步验证了其有效性。

## 🎯 应用场景

SWIRL在移动GUI控制中的应用潜力巨大，能够有效地将自然语言转化为界面操作，提升用户体验。此外，其在多智能体数学推理中的表现也表明了其作为通用框架的潜力，能够广泛应用于其他多智能体系统的开发。

## 📄 摘要（原文）

> The rapid advancement of large vision language models (LVLMs) and agent systems has heightened interest in mobile GUI agents that can reliably translate natural language into interface operations. Existing single-agent approaches, however, remain limited by structural constraints. Although multi-agent systems naturally decouple different competencies, recent progress in multi-agent reinforcement learning (MARL) has often been hindered by inefficiency and remains incompatible with current LVLM architectures. To address these challenges, we introduce SWIRL, a staged workflow for interleaved reinforcement learning designed for multi-agent systems. SWIRL reformulates MARL into a sequence of single-agent reinforcement learning tasks, updating one agent at a time while keeping the others fixed. This formulation enables stable training and promotes efficient coordination across agents. Theoretically, we provide a stepwise safety bound, a cross-round monotonic improvement theorem, and convergence guarantees on return, ensuring robust and principled optimization. In application to mobile GUI control, SWIRL instantiates a Navigator that converts language and screen context into structured plans, and an Interactor that grounds these plans into executable atomic actions. Extensive experiments demonstrate superior performance on both high-level and low-level GUI benchmarks. Beyond GUI tasks, SWIRL also demonstrates strong capability in multi-agent mathematical reasoning, underscoring its potential as a general framework for developing efficient and robust multi-agent systems.

