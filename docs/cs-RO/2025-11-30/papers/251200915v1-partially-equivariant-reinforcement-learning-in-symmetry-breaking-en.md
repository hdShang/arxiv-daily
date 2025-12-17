---
layout: default
title: Partially Equivariant Reinforcement Learning in Symmetry-Breaking Environments
---

# Partially Equivariant Reinforcement Learning in Symmetry-Breaking Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00915" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00915v1</a>
  <a href="https://arxiv.org/pdf/2512.00915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00915v1" onclick="toggleFavorite(this, '2512.00915v1', 'Partially Equivariant Reinforcement Learning in Symmetry-Breaking Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junwoo Chang, Minwoo Park, Joohwan Seo, Roberto Horowitz, Jongmin Lee, Jongeun Choi

**分类**: cs.LG, cs.RO

**发布日期**: 2025-11-30

**备注**: 27 pages, 10 figures

---

## 💡 一句话要点

**提出部分等变强化学习，解决对称破缺环境下的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `群对称性` `等变性` `对称破缺` `泛化能力`

## 📋 核心要点

1. 现实环境中的对称性通常是局部而非全局的，这导致传统群不变强化学习方法在对称破缺区域产生误差并扩散。
2. 论文提出部分群不变MDP (PI-MDP) 框架，根据对称性保持情况选择性地应用群不变或标准贝尔曼备份，减少误差传播。
3. 实验结果表明，提出的 PE-DQN 和 PE-SAC 算法在多个任务中显著优于基线方法，验证了选择性对称性利用的有效性。

## 📝 摘要（中文）

群对称性为强化学习(RL)提供了一种强大的归纳偏置，通过群不变马尔可夫决策过程(MDP)实现跨对称状态和动作的有效泛化。然而，现实环境几乎从未实现完全群不变的MDP；动力学、驱动限制和奖励设计通常会打破对称性，而且通常只是局部打破。在这种情况下，如果采用群不变的贝尔曼备份，局部对称性破缺会引入误差，并在整个状态-动作空间中传播，导致全局价值估计误差。为了解决这个问题，我们引入了部分群不变MDP(PI-MDP)，它根据对称性保持的位置选择性地应用群不变或标准贝尔曼备份。该框架减轻了局部对称性破缺带来的误差传播，同时保持了等变的优势，从而提高了样本效率和泛化能力。在此框架的基础上，我们提出了实用的RL算法——用于离散控制的Partially Equivariant (PE)-DQN和用于连续控制的PE-SAC——它们结合了等变的优势和对对称性破缺的鲁棒性。在Grid-World、运动和操作基准上的实验表明，PE-DQN和PE-SAC明显优于基线，突出了选择性对称性利用对于鲁棒和样本高效RL的重要性。

## 🔬 方法详解

**问题定义**：现有基于群对称性的强化学习方法依赖于完全群不变的MDP假设，但在实际环境中，由于动力学、动作限制或奖励函数的设计，对称性往往是局部破缺的。这种局部对称性破缺会导致价值估计误差在整个状态空间传播，降低算法的性能和泛化能力。

**核心思路**：论文的核心思想是只在对称性保持的区域利用群不变性，而在对称性破缺的区域使用标准的贝尔曼备份。通过这种选择性的对称性利用，可以避免误差从对称性破缺区域传播到整个状态空间，从而提高价值估计的准确性和算法的鲁棒性。

**技术框架**：论文提出了部分群不变MDP (PI-MDP) 框架。该框架包含两个关键部分：1) 对称性检测器，用于判断当前状态-动作对是否满足群不变性；2) 选择性贝尔曼备份，根据对称性检测器的结果，选择使用群不变贝尔曼备份或标准贝尔曼备份来更新价值函数。基于 PI-MDP 框架，论文进一步提出了 PE-DQN 和 PE-SAC 两种具体的算法，分别用于离散和连续控制任务。

**关键创新**：论文的关键创新在于提出了部分群不变MDP (PI-MDP) 的概念，并设计了相应的算法框架。与传统的群不变强化学习方法相比，PI-MDP 能够更好地适应实际环境中普遍存在的局部对称性破缺现象，从而提高算法的性能和泛化能力。

**关键设计**：PE-DQN 和 PE-SAC 算法的关键设计包括：1) 使用神经网络来近似对称性检测器，通过训练来学习状态-动作对的对称性；2) 设计合适的损失函数，鼓励对称性检测器输出准确的对称性判断结果；3) 在群不变贝尔曼备份中使用合适的群表示，以保证价值函数的等变性。

## 📊 实验亮点

实验结果表明，在 Grid-World、locomotion 和 manipulation 等多个基准测试中，PE-DQN 和 PE-SAC 算法均显著优于基线方法。例如，在 locomotion 任务中，PE-SAC 算法的性能比 SAC 算法提高了 20% 以上，证明了部分等变强化学习在对称破缺环境下的有效性。

## 🎯 应用场景

该研究成果可应用于机器人控制、游戏AI、自动驾驶等领域，尤其是在这些领域中存在部分对称性的场景。例如，在机器人操作任务中，机器人的某些关节可能具有旋转对称性，而其他关节则受到物理限制。通过利用部分等变强化学习，可以提高机器人在这些任务中的学习效率和泛化能力，从而降低开发成本和提高系统性能。

## 📄 摘要（原文）

> Group symmetries provide a powerful inductive bias for reinforcement learning (RL), enabling efficient generalization across symmetric states and actions via group-invariant Markov Decision Processes (MDPs). However, real-world environments almost never realize fully group-invariant MDPs; dynamics, actuation limits, and reward design usually break symmetries, often only locally. Under group-invariant Bellman backups for such cases, local symmetry-breaking introduces errors that propagate across the entire state-action space, resulting in global value estimation errors. To address this, we introduce Partially group-Invariant MDP (PI-MDP), which selectively applies group-invariant or standard Bellman backups depending on where symmetry holds. This framework mitigates error propagation from locally broken symmetries while maintaining the benefits of equivariance, thereby enhancing sample efficiency and generalizability. Building on this framework, we present practical RL algorithms -- Partially Equivariant (PE)-DQN for discrete control and PE-SAC for continuous control -- that combine the benefits of equivariance with robustness to symmetry-breaking. Experiments across Grid-World, locomotion, and manipulation benchmarks demonstrate that PE-DQN and PE-SAC significantly outperform baselines, highlighting the importance of selective symmetry exploitation for robust and sample-efficient RL.

