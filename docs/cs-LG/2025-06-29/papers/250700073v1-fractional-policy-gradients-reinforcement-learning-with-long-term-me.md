---
layout: default
title: "Fractional Policy Gradients: Reinforcement Learning with Long-Term Memory"
---

# Fractional Policy Gradients: Reinforcement Learning with Long-Term Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00073" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00073v1</a>
  <a href="https://arxiv.org/pdf/2507.00073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00073v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00073v1', 'Fractional Policy Gradients: Reinforcement Learning with Long-Term Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Urvi Pawar, Kunal Telangi

**分类**: cs.LG, stat.ML

**发布日期**: 2025-06-29

**备注**: Submitted to Journal of Machine Learning Research (JMLR), June 2025. 24 pages, 3 figures. Under review

---

## 💡 一句话要点

**提出分数策略梯度方法以解决长期记忆强化学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `分数微积分` `长期记忆` `策略优化` `方差降低` `样本效率` `时间建模`

## 📋 核心要点

1. 现有的强化学习方法在长期时间建模上存在局限，尤其是在高方差和低效采样方面。
2. 本文提出的FPG框架通过引入分数微积分，重新定义策略梯度以捕捉长期时间相关性。
3. 实验结果表明，FPG在样本效率和方差方面显著优于现有的最先进方法，提升幅度达到35-68%和24-52%。

## 📝 摘要（中文）

本文提出了分数策略梯度（FPG）框架，结合分数微积分用于策略优化中的长期时间建模。标准的策略梯度方法受到马尔可夫假设的限制，表现出高方差和低效采样。通过使用Caputo分数导数重新构造梯度，FPG建立了状态转移之间的幂律时间相关性。我们开发了一种高效的递归计算技术，用于分数时间差错的计算，具有恒定的时间和内存需求。理论分析表明，FPG在保持收敛性的同时，实现了O(t^(-alpha))的渐近方差降低。实证验证显示，相较于最先进的基线，FPG在样本效率上提升了35-68%，方差降低了24-52%。该框架为利用长程依赖提供了数学基础，而无需额外的计算开销。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在长期记忆建模中的不足，特别是高方差和低效采样的问题。标准策略梯度方法依赖于马尔可夫假设，限制了其在复杂环境中的表现。

**核心思路**：FPG框架通过引入分数微积分，利用Caputo分数导数重新构造策略梯度，从而建立状态转移之间的幂律时间相关性。这种设计使得模型能够更好地捕捉长期依赖关系。

**技术框架**：FPG的整体架构包括状态表示、分数时间差错计算和策略优化三个主要模块。通过递归计算技术，FPG能够在恒定的时间和内存需求下高效地处理分数时间差错。

**关键创新**：FPG的核心创新在于将分数微积分应用于策略梯度方法，显著降低了方差并提高了样本效率。这一方法与传统的策略梯度方法在理论基础和计算效率上存在本质区别。

**关键设计**：在FPG中，关键参数包括分数阶数的选择和损失函数的设计。通过合理的网络结构和训练策略，FPG能够有效地学习长期依赖关系。具体的损失函数设计考虑了分数时间差错的计算，以确保模型的收敛性和稳定性。

## 📊 实验亮点

实验结果显示，FPG在样本效率上较最先进基线提升了35-68%，在方差方面降低了24-52%。这些结果表明，FPG在强化学习任务中具有显著的性能优势，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、金融预测和智能决策系统等。通过有效捕捉长期依赖关系，FPG能够在复杂环境中实现更高效的学习和决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We propose Fractional Policy Gradients (FPG), a reinforcement learning framework incorporating fractional calculus for long-term temporal modeling in policy optimization. Standard policy gradient approaches face limitations from Markovian assumptions, exhibiting high variance and inefficient sampling. By reformulating gradients using Caputo fractional derivatives, FPG establishes power-law temporal correlations between state transitions. We develop an efficient recursive computation technique for fractional temporal-difference errors with constant time and memory requirements. Theoretical analysis shows FPG achieves asymptotic variance reduction of order O(t^(-alpha)) versus standard policy gradients while preserving convergence. Empirical validation demonstrates 35-68% sample efficiency gains and 24-52% variance reduction versus state-of-the-art baselines. This framework provides a mathematically grounded approach for leveraging long-range dependencies without computational overhead.

