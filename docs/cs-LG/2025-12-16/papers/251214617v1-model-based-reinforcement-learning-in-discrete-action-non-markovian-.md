---
layout: default
title: Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes
---

# Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes

**arXiv**: [2512.14617v1](https://arxiv.org/abs/2512.14617) | [PDF](https://arxiv.org/pdf/2512.14617.pdf)

**作者**: Alessandro Trapasso, Luca Iocchi, Fabio Patrizi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 19 pages, 32 figures, includes appendix

---

## 💡 一句话要点

**提出QR-MAX算法，通过奖励机分解学习，解决离散动作非马尔可夫奖励决策过程的样本效率与最优性保证问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `非马尔可夫奖励决策过程` `基于模型强化学习` `奖励机` `样本效率` `PAC收敛` `连续状态空间` `SimHash离散化` `时间依赖性任务`

## 📋 核心要点

1. 核心问题：现有马尔可夫强化学习方法不适用于依赖历史的任务，非马尔可夫奖励决策过程缺乏最优性和样本效率的形式化保证。
2. 方法要点：提出QR-MAX算法，通过奖励机分解马尔可夫转移与非马尔可夫奖励，实现模型学习与奖励处理的分离。
3. 实验或效果：在复杂环境中，QR-MAX相比现有方法显著提升样本效率，增强策略最优性鲁棒性，并扩展到连续状态空间。

## 📝 摘要（中文）

许多实际决策问题涉及任务的成功依赖于整个系统历史，而非仅达到具有期望属性的状态。马尔可夫强化学习方法不适用于此类任务，而非马尔可夫奖励决策过程使智能体能够处理时间依赖性任务。这种方法长期以来缺乏对（近）最优性和样本效率的形式化保证。我们通过QR-MAX贡献于解决这两个问题，这是一种基于模型的新算法，用于离散非马尔可夫奖励决策过程，通过奖励机将马尔可夫转移学习与非马尔可夫奖励处理分解。据我们所知，这是首个基于模型的强化学习算法，利用这种分解实现多项式样本复杂度下收敛到ε-最优策略的PAC保证。然后，我们将QR-MAX扩展到连续状态空间，通过Bucket-QR-MAX，一种基于SimHash的离散化器，保持相同的分解结构，实现快速稳定学习，无需手动网格化或函数逼近。我们在复杂度递增的环境上实验比较我们的方法与现代最先进的基于模型强化学习方法，显示样本效率显著提升和寻找最优策略的鲁棒性增强。

## 🔬 方法详解

QR-MAX是一种基于模型的强化学习算法，专为离散动作非马尔可夫奖励决策过程设计。整体框架结合奖励机来分解学习过程：智能体学习马尔可夫状态转移模型，同时使用奖励机处理非马尔可夫奖励信号。关键技术创新点在于这种分解结构，允许独立优化转移学习和奖励处理，从而获得多项式样本复杂度的PAC收敛保证。与现有方法的主要区别在于，它首次在基于模型强化学习中实现这种分解，避免了传统方法对函数逼近或手动离散化的依赖，并通过Bucket-QR-MAX扩展支持连续状态空间，利用SimHash进行高效离散化。

## 📊 实验亮点

实验显示QR-MAX在样本效率上显著优于现代最先进的基于模型强化学习方法，在复杂环境中实现更快收敛和更高策略最优性，Bucket-QR-MAX在连续状态空间中保持稳定学习，无需手动调整。

## 🎯 应用场景

该研究适用于需要处理时间依赖性任务的领域，如机器人导航、自动驾驶、游戏AI和工业自动化，其中任务成功依赖于历史序列而非单一状态，可提升决策系统的效率和鲁棒性。

## 📄 摘要（原文）

> Many practical decision-making problems involve tasks whose success depends on the entire system history, rather than on achieving a state with desired properties. Markovian Reinforcement Learning (RL) approaches are not suitable for such tasks, while RL with non-Markovian reward decision processes (NMRDPs) enables agents to tackle temporal-dependency tasks. This approach has long been known to lack formal guarantees on both (near-)optimality and sample efficiency. We contribute to solving both issues with QR-MAX, a novel model-based algorithm for discrete NMRDPs that factorizes Markovian transition learning from non-Markovian reward handling via reward machines. To the best of our knowledge, this is the first model-based RL algorithm for discrete-action NMRDPs that exploits this factorization to obtain PAC convergence to $\varepsilon$-optimal policies with polynomial sample complexity. We then extend QR-MAX to continuous state spaces with Bucket-QR-MAX, a SimHash-based discretiser that preserves the same factorized structure and achieves fast and stable learning without manual gridding or function approximation. We experimentally compare our method with modern state-of-the-art model-based RL approaches on environments of increasing complexity, showing a significant improvement in sample efficiency and increased robustness in finding optimal policies.

