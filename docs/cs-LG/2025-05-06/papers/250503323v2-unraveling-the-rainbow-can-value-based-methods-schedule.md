---
layout: default
title: Unraveling the Rainbow: can value-based methods schedule?
---

# Unraveling the Rainbow: can value-based methods schedule?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03323" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03323v2</a>
  <a href="https://arxiv.org/pdf/2505.03323.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03323v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03323v2', 'Unraveling the Rainbow: can value-based methods schedule?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arthur Corrêa, Alexandre Jesus, Paulo Nascimento, Cristóvão Silva, Samuel Moniz

**分类**: cs.LG

**发布日期**: 2025-05-06 (更新: 2025-11-27)

**🔗 代码/项目**: [GITHUB](https://github.com/AJ-Correa/Unraveling-the-Rainbow)

---

## 💡 一句话要点

**提出基于价值的方法以解决作业调度问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `作业调度` `价值基算法` `策略梯度算法` `组合优化` `工业应用`

## 📋 核心要点

1. 现有的组合优化方法主要依赖策略梯度算法，忽视了价值基算法的潜力。
2. 论文提出通过深度强化学习中的价值基算法来解决作业调度问题，展示其在稳定性和泛化能力上的优势。
3. 实验结果显示，价值基算法在多个调度实例上表现出更低的方差和更好的收敛性，挑战了传统观点。

## 📝 摘要（中文）

本研究对多种深度强化学习算法在作业车间和灵活作业车间调度问题上的表现进行了广泛的实证研究。这两个问题是具有多种工业应用的基本挑战。尽管价值基算法在某些领域取得了显著成功，但组合优化领域主要偏向于策略梯度算法。我们的结果表明，价值基算法在方差和收敛稳定性方面表现更佳，并且在跨规模和跨分布的泛化能力上优于策略梯度算法。此外，算法的相对性能可能依赖于问题的结构特性，如灵活性和实例大小。我们的发现挑战了策略梯度算法在组合优化中优越性的普遍假设，表明价值基算法同样值得关注。

## 🔬 方法详解

**问题定义**：本论文旨在解决作业车间和灵活作业车间调度问题，这些问题在工业应用中具有重要意义。现有方法主要依赖策略梯度算法，导致对价值基算法的潜力认识不足。

**核心思路**：论文的核心思路是通过深度强化学习中的价值基算法，展示其在调度问题上的有效性，尤其是在稳定性和泛化能力方面的优势。

**技术框架**：整体架构包括数据预处理、模型训练和性能评估三个主要模块。首先，对调度实例进行特征提取，然后使用价值基算法进行训练，最后评估模型在不同规模和分布上的表现。

**关键创新**：最重要的技术创新点在于证明了价值基算法在组合优化问题上可以与策略梯度算法相媲美，甚至超越其性能，挑战了传统的算法优越性假设。

**关键设计**：在模型设计中，采用了特定的损失函数和网络结构，以优化价值基算法的表现，并进行了参数调优以提高收敛速度和稳定性。具体细节包括使用经验回放和目标网络等技术。

## 📊 实验亮点

实验结果显示，价值基算法在多个调度实例上表现出更低的方差和更好的收敛性，相比于策略梯度算法，价值基算法在跨规模和跨分布的泛化能力上有显著提升，挑战了传统观点。

## 🎯 应用场景

该研究的潜在应用领域包括制造业调度、物流优化和资源分配等多个工业场景。通过提高调度效率，企业可以降低成本、提高生产力，进而在竞争中获得优势。未来，价值基算法的进一步研究可能会推动更多复杂调度问题的解决。

## 📄 摘要（原文）

> In this work, we conduct an extensive empirical study of several deep reinforcement learning algorithms on two challenging combinatorial optimization problems: the job-shop and flexible job-shop scheduling problems, both fundamental challenges with multiple industrial applications. Broadly, deep reinforcement learning algorithms fall into two categories: policy-gradient and value-based. While value-based algorithms have achieved notable success in domains such as the Arcade Learning Environment, the combinatorial optimization community has predominantly favored policy-gradient algorithms, often overlooking the potential of value-based alternatives. From our results, value-based algorithms demonstrated a lower variance and a more stable convergence profile compared to policy-gradient ones. Moreover, they achieved superior cross-size and cross-distribution generalization, that is, effectively solving instances that are substantially larger or structurally distinct from those seen during training. Finally, our analysis also suggests that the relative performance of each category of algorithms may be dependent on structural properties of the problem, such as problem flexibility and instance size. Overall, our findings challenge the prevailing assumption that policy-gradient algorithms are inherently superior for combinatorial optimization. We show instead that value-based algorithms can match or even surpass the performance of policy-gradient algorithms, suggesting that they deserve greater attention from the combinatorial optimization community. Our code is openly available at: https://github.com/AJ-Correa/Unraveling-the-Rainbow

