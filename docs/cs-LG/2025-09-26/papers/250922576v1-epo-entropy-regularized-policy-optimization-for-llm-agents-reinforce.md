---
layout: default
title: "EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning"
---

# EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22576" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22576v1</a>
  <a href="https://arxiv.org/pdf/2509.22576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22576v1', 'EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wujiang Xu, Wentian Zhao, Zhenting Wang, Yu-Jhe Li, Can Jin, Mingyu Jin, Kai Mei, Kun Wan, Dimitris N. Metaxas

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出EPO算法，解决LLM Agent在多轮稀疏奖励强化学习中的探索-利用崩溃问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `LLM Agent` `强化学习` `熵正则化` `多轮交互` `稀疏奖励` `策略优化` `探索-利用`

## 📋 核心要点

1. 多轮交互、稀疏奖励环境下训练LLM Agent面临探索-利用级联崩溃问题，早期策略过早收敛，后期熵正则化失效。
2. 提出熵正则化策略优化（EPO）框架，包含熵正则化、熵平滑正则化器和自适应阶段权重三个机制，平衡探索与利用。
3. 实验表明，EPO在ScienceWorld和ALFWorld等任务上显著提升了LLM Agent的性能，验证了其有效性。

## 📝 摘要（中文）

本文针对LLM Agent在多轮交互、稀疏奖励环境下的强化学习训练难题，指出了一种独特的失败模式：探索-利用级联崩溃。这种崩溃始于早期策略的过早收敛，由于稀疏反馈导致Agent陷入有缺陷的低熵策略。随后，Agent进入晚期策略崩溃，此时传统的熵正则化反而适得其反，促进了混乱的探索，破坏了训练的稳定性。为此，论文提出了熵正则化策略优化（EPO）框架，通过三个协同机制打破这种失败循环：(1) 在多轮设置中采用熵正则化以增强探索；(2) 熵平滑正则化器，将策略熵限制在历史平均值范围内，以防止突然波动；(3) 自适应的基于阶段的权重，平衡训练过程中的探索和利用。分析表明，EPO保证了单调递减的熵方差，同时保持收敛性。在ScienceWorld上，EPO实现了高达152%的性能提升，在ALFWorld上实现了高达19.8%的性能提升。这项工作表明，多轮稀疏奖励设置需要与传统强化学习根本不同的熵控制方法，这对LLM Agent训练具有广泛的影响。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM Agent在多轮交互、稀疏奖励环境下的强化学习训练问题。现有方法在处理此类问题时，容易出现“探索-利用级联崩溃”现象。具体来说，由于奖励稀疏，Agent在训练初期容易陷入次优策略并过早收敛（低熵），导致后续探索不足；而后期为了跳出局部最优，采用传统熵正则化又容易导致策略不稳定，甚至崩溃。

**核心思路**：论文的核心思路是通过更精细的熵控制来解决上述问题。具体而言，论文提出了一种新的熵正则化策略优化（EPO）框架，该框架包含三个关键组成部分：熵正则化、熵平滑正则化器和自适应阶段权重。通过这些组件的协同作用，EPO旨在平衡探索和利用，避免策略过早收敛和后期崩溃。

**技术框架**：EPO框架主要包含以下几个阶段：
1. **策略学习阶段**：使用强化学习算法（如Policy Optimization）更新LLM Agent的策略。
2. **熵正则化阶段**：在策略学习过程中，引入熵正则化项，鼓励Agent进行更广泛的探索。
3. **熵平滑阶段**：使用熵平滑正则化器，将策略熵限制在历史平均值范围内，防止策略熵的剧烈波动。
4. **自适应权重调整阶段**：根据训练的阶段，自适应地调整探索和利用的权重，以达到最佳的训练效果。

**关键创新**：论文的关键创新在于提出了一个综合的熵控制框架，该框架能够有效地解决LLM Agent在多轮交互、稀疏奖励环境下的强化学习训练问题。与传统方法相比，EPO不仅考虑了熵正则化，还引入了熵平滑正则化器和自适应阶段权重，从而实现了更精细的熵控制。

**关键设计**：
* **熵平滑正则化器**：该正则化器通过计算当前策略熵与历史平均熵之间的差异，并将其作为惩罚项添加到损失函数中，从而限制策略熵的波动。
* **自适应阶段权重**：该权重根据训练的阶段（早期、中期、晚期）自适应地调整探索和利用的权重。例如，在训练初期，可以增加探索的权重，以鼓励Agent进行更广泛的探索；在训练后期，可以增加利用的权重，以提高Agent的性能。

## 📊 实验亮点

实验结果表明，EPO算法在ScienceWorld和ALFWorld等任务上取得了显著的性能提升。具体而言，在ScienceWorld上，EPO算法实现了高达152%的性能提升；在ALFWorld上，EPO算法实现了高达19.8%的性能提升。这些结果表明，EPO算法能够有效地解决LLM Agent在多轮交互、稀疏奖励环境下的强化学习训练问题。

## 🎯 应用场景

该研究成果可应用于各种需要LLM Agent进行多轮交互、解决复杂任务的场景，例如游戏AI、智能客服、科学研究助手等。通过提高LLM Agent在复杂环境下的学习能力，可以显著提升其解决实际问题的能力，具有重要的应用价值和潜力。

## 📄 摘要（原文）

> Training LLM agents in multi-turn environments with sparse rewards, where completing a single task requires 30+ turns of interaction within an episode, presents a fundamental challenge for reinforcement learning. We identify a critical failure mode unique to this setting: the exploration-exploitation cascade failure. This cascade begins with early-stage policy premature convergence, where sparse feedback causes agents to commit to flawed, low-entropy strategies. Subsequently, agents enter late-stage policy collapse, where conventional entropy regularization becomes counterproductive, promoting chaotic exploration that destabilizes training. We propose Entropy-regularized Policy Optimization (EPO), a general framework that breaks this failure cycle through three synergistic mechanisms: (1) adopting entropy regularization in multi-turn settings to enhance exploration, (2) an entropy smoothing regularizer that bounds policy entropy within historical averages to prevent abrupt fluctuations, and (3) adaptive phase-based weighting that balances exploration and exploitation across training. Our analysis justifies that EPO guarantees monotonically decreasing entropy variance while maintaining convergence. EPO achieves up to 152% performance improvement on ScienceWorld and up to 19.8% on ALFWorld. Our work demonstrates that multi-turn sparse-reward settings require fundamentally different entropy control than traditional RL, with broad implications for LLM agent training.

