---
layout: default
title: "Generalizing Beyond Suboptimality: Offline Reinforcement Learning Learns Effective Scheduling through Random Data"
---

# Generalizing Beyond Suboptimality: Offline Reinforcement Learning Learns Effective Scheduling through Random Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10303" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10303v1</a>
  <a href="https://arxiv.org/pdf/2509.10303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10303v1', 'Generalizing Beyond Suboptimality: Offline Reinforcement Learning Learns Effective Scheduling through Random Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jesse van Remmerden, Zaharah Bukhsh, Yingqian Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**提出CDQAC算法，通过离线强化学习从随机数据中学习高效作业调度策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `作业调度问题` `分位数Actor-Critic` `保守策略更新` `组合优化` `工业应用`

## 📋 核心要点

1. 在线强化学习方法在作业调度问题中需要大量与模拟环境的交互，且随机策略初始化导致样本效率低下。
2. CDQAC算法通过离线强化学习，直接从历史数据中学习调度策略，无需在线交互，并能从次优数据中提升。
3. 实验表明，CDQAC优于现有离线和在线强化学习方法，且样本效率高，在随机数据上训练效果更佳。

## 📝 摘要（中文）

本文针对Job-Shop调度问题(JSP)和柔性Job-Shop调度问题(FJSP)，提出了一种新的离线强化学习算法——保守离散分位数Actor-Critic (CDQAC)。该算法直接从历史数据中学习有效的调度策略，无需耗时的在线交互，并能从次优训练数据中进行改进。CDQAC将基于分位数的评论家与延迟策略更新相结合，估计每个机器-操作对的回报分布，而不是直接选择配对。实验结果表明，CDQAC能够从多样化的数据源中学习，始终优于原始数据生成启发式方法，并超越了最先进的离线和在线强化学习基线。此外，CDQAC具有很高的样本效率，仅需10-20个训练实例即可学习高质量策略。令人惊讶的是，CDQAC在随机启发式算法生成的数据上训练时，性能优于在遗传算法和优先级调度规则等更高质量数据上训练时的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决Job-Shop调度问题(JSP)和柔性Job-Shop调度问题(FJSP)。现有在线强化学习方法需要大量的环境交互，成本高昂，且模拟环境可能无法完全捕捉真实世界的复杂性。此外，随机策略初始化导致样本效率低下，收敛速度慢。

**核心思路**：论文的核心思路是利用离线强化学习，直接从历史数据中学习调度策略，避免在线交互的成本。通过保守策略更新，即使训练数据是次优的，也能学习到更优的策略。使用分位数Actor-Critic方法，学习回报的分布，而不是单一的期望值，从而更好地处理不确定性。

**技术框架**：CDQAC算法包含一个基于分位数的评论家和一个Actor网络。评论家网络用于估计每个机器-操作对的回报分布。Actor网络根据评论家网络的输出，选择最优的机器-操作对。算法采用延迟策略更新，以保证策略的稳定性。整体流程是：首先，使用历史数据训练评论家网络；然后，使用评论家网络指导Actor网络的训练；最后，使用训练好的Actor网络进行调度决策。

**关键创新**：CDQAC的关键创新在于结合了分位数Actor-Critic方法和保守策略更新，使其能够从次优的离线数据中学习到有效的调度策略。传统Actor-Critic方法通常学习期望回报，而CDQAC学习回报的分布，能够更好地处理调度问题中的不确定性。保守策略更新则避免了策略过度优化，提高了算法的稳定性和泛化能力。

**关键设计**：CDQAC使用分位数回归损失函数训练评论家网络，以学习回报分布。Actor网络使用softmax策略，选择具有最高回报的机器-操作对。保守策略更新通过限制策略的更新幅度，防止策略偏离训练数据过远。具体参数设置包括学习率、折扣因子、分位数数量等，这些参数需要根据具体问题进行调整。

## 📊 实验亮点

实验结果表明，CDQAC算法在JSP和FJSP问题上均优于现有的离线和在线强化学习基线。CDQAC仅需10-20个训练实例即可学习高质量策略，样本效率显著提高。更令人惊讶的是，CDQAC在随机启发式算法生成的数据上训练时，性能优于在遗传算法和优先级调度规则等更高质量数据上训练时的性能，这表明CDQAC具有很强的鲁棒性和泛化能力。

## 🎯 应用场景

CDQAC算法可广泛应用于工业制造、物流运输、云计算资源调度等领域。通过利用历史调度数据，企业可以快速部署高效的调度策略，提高生产效率，降低运营成本。该研究为解决实际生产中的复杂调度问题提供了一种新的思路和方法，具有重要的实际应用价值和推广前景。

## 📄 摘要（原文）

> The Job-Shop Scheduling Problem (JSP) and Flexible Job-Shop Scheduling Problem (FJSP), are canonical combinatorial optimization problems with wide-ranging applications in industrial operations. In recent years, many online reinforcement learning (RL) approaches have been proposed to learn constructive heuristics for JSP and FJSP. Although effective, these online RL methods require millions of interactions with simulated environments that may not capture real-world complexities, and their random policy initialization leads to poor sample efficiency. To address these limitations, we introduce Conservative Discrete Quantile Actor-Critic (CDQAC), a novel offline RL algorithm that learns effective scheduling policies directly from historical data, eliminating the need for costly online interactions, while maintaining the ability to improve upon suboptimal training data. CDQAC couples a quantile-based critic with a delayed policy update, estimating the return distribution of each machine-operation pair rather than selecting pairs outright. Our extensive experiments demonstrate CDQAC's remarkable ability to learn from diverse data sources. CDQAC consistently outperforms the original data-generating heuristics and surpasses state-of-the-art offline and online RL baselines. In addition, CDQAC is highly sample efficient, requiring only 10-20 training instances to learn high-quality policies. Surprisingly, we find that CDQAC performs better when trained on data generated by a random heuristic than when trained on higher-quality data from genetic algorithms and priority dispatching rules.

