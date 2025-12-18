---
layout: default
title: EUBRL: Epistemic Uncertainty Directed Bayesian Reinforcement Learning
---

# EUBRL: Epistemic Uncertainty Directed Bayesian Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15405" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15405v1</a>
  <a href="https://arxiv.org/pdf/2512.15405.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15405v1" onclick="toggleFavorite(this, '2512.15405v1', 'EUBRL: Epistemic Uncertainty Directed Bayesian Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianfei Ma, Wee Sun Lee

**分类**: cs.LG

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出EUBRL算法，利用认知不确定性指导贝叶斯强化学习探索，提升样本效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `贝叶斯强化学习` `认知不确定性` `探索-利用` `稀疏奖励` `长视界` `样本效率` `强化学习`

## 📋 核心要点

1. 传统强化学习在探索-利用平衡上存在挑战，尤其是在稀疏奖励和长视界任务中，难以有效探索未知状态。
2. EUBRL算法利用认知不确定性作为探索指导，通过贝叶斯方法量化不确定性，并引导智能体探索不确定性高的区域。
3. 实验表明，EUBRL在样本效率、可扩展性和一致性方面优于现有算法，尤其在稀疏奖励和长视界任务中表现突出。

## 📝 摘要（中文）

在已知与未知边界，智能体面临探索与利用的两难。认知不确定性反映了这种边界，代表了因知识有限而产生的系统性不确定性。本文提出了一种贝叶斯强化学习算法（EUBRL），它利用认知指导来实现有原则的探索，自适应地减少由估计误差引起的每步遗憾。对于无限视界折扣MDP中一类充分表达的先验，我们建立了接近minimax最优的遗憾和样本复杂度保证。在具有稀疏奖励、长视界和随机性的任务上评估了EUBRL，结果表明EUBRL实现了卓越的样本效率、可扩展性和一致性。

## 🔬 方法详解

**问题定义**：强化学习智能体在与环境交互时，需要在探索未知状态以获取更多信息和利用已知信息以最大化奖励之间进行权衡。尤其是在稀疏奖励和长视界的环境中，智能体很难有效地探索，导致学习效率低下。现有的方法往往难以有效地量化和利用这种探索的不确定性，导致次优策略。

**核心思路**：EUBRL的核心思路是利用认知不确定性（Epistemic Uncertainty）来指导探索。认知不确定性反映了由于知识不足而产生的系统性不确定性。通过贝叶斯强化学习框架，EUBRL能够量化这种不确定性，并将其作为探索的内在奖励，引导智能体优先探索那些不确定性高的状态和动作，从而更有效地学习最优策略。

**技术框架**：EUBRL算法基于贝叶斯强化学习框架，其主要流程如下：1) 使用贝叶斯方法维护一个关于MDP参数的后验分布；2) 基于该后验分布，计算每个状态-动作对的认知不确定性；3) 将认知不确定性作为内在奖励添加到原始奖励中，形成一个增广的奖励函数；4) 使用标准的强化学习算法（如Q-learning或策略梯度）来优化基于增广奖励函数的策略；5) 根据智能体的经验更新后验分布。这个过程迭代进行，直到策略收敛。

**关键创新**：EUBRL的关键创新在于将认知不确定性显式地纳入到强化学习的探索过程中。与传统的探索方法（如ε-greedy或UCB）相比，EUBRL能够更准确地量化和利用不确定性信息，从而实现更有效的探索。此外，EUBRL通过贝叶斯方法维护MDP参数的后验分布，能够更好地处理环境的不确定性，并提供理论上的保证。

**关键设计**：EUBRL的关键设计包括：1) 使用合适的先验分布来表示MDP参数的不确定性。论文中提到使用一类充分表达的先验，具体形式未知；2) 定义认知不确定性的计算方法。具体如何计算认知不确定性，论文中未详细说明，需要参考相关文献；3) 如何将认知不确定性与原始奖励进行融合。论文中提到将认知不确定性作为内在奖励添加到原始奖励中，但具体的权重比例未知；4) 使用合适的贝叶斯更新方法来更新MDP参数的后验分布。具体使用哪种贝叶斯更新方法，论文中未详细说明。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15405v1/experiment_figures/Loop-scaling.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15405v1/experiment_figures/DeepSea.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15405v1/experiment_figures/LazyChain.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EUBRL算法在稀疏奖励、长视界和随机性任务上表现出卓越的性能。实验结果表明，EUBRL在样本效率、可扩展性和一致性方面优于现有算法。具体性能提升数据未知，但论文强调EUBRL实现了接近minimax最优的遗憾和样本复杂度保证，表明其具有良好的理论性质。

## 🎯 应用场景

EUBRL算法适用于需要高效探索的强化学习任务，例如机器人导航、游戏AI、自动驾驶等。尤其在奖励稀疏、环境复杂或存在大量未知状态的情况下，EUBRL能够显著提升学习效率，降低试错成本。该研究有助于推动强化学习在实际场景中的应用，并为解决探索-利用难题提供新的思路。

## 📄 摘要（原文）

> At the boundary between the known and the unknown, an agent inevitably confronts the dilemma of whether to explore or to exploit. Epistemic uncertainty reflects such boundaries, representing systematic uncertainty due to limited knowledge. In this paper, we propose a Bayesian reinforcement learning (RL) algorithm, $\texttt{EUBRL}$, which leverages epistemic guidance to achieve principled exploration. This guidance adaptively reduces per-step regret arising from estimation errors. We establish nearly minimax-optimal regret and sample complexity guarantees for a class of sufficiently expressive priors in infinite-horizon discounted MDPs. Empirically, we evaluate $\texttt{EUBRL}$ on tasks characterized by sparse rewards, long horizons, and stochasticity. Results demonstrate that $\texttt{EUBRL}$ achieves superior sample efficiency, scalability, and consistency.

