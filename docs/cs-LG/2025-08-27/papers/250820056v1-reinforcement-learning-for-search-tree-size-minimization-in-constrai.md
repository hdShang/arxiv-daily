---
layout: default
title: "Reinforcement Learning for Search Tree Size Minimization in Constraint Programming: New Results on Scheduling Benchmarks"
---

# Reinforcement Learning for Search Tree Size Minimization in Constraint Programming: New Results on Scheduling Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20056" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20056v1</a>
  <a href="https://arxiv.org/pdf/2508.20056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20056v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20056v1', 'Reinforcement Learning for Search Tree Size Minimization in Constraint Programming: New Results on Scheduling Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vilém Heinz, Petr Vilím, Zdeněk Hanzálek

**分类**: cs.LG

**发布日期**: 2025-08-27

**期刊**: Computers & Industrial Engineering, vol. 209, p. 111413, 2025

**DOI**: [10.1016/j.cie.2025.111413](https://doi.org/10.1016/j.cie.2025.111413)

---

## 💡 一句话要点

**基于强化学习的约束编程搜索树大小最小化方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `约束编程` `调度问题` `搜索树优化` `多臂老虎机` `失败导向搜索` `性能提升`

## 📋 核心要点

1. 现有的失败导向搜索算法在处理调度问题时，搜索树的大小往往导致效率低下。
2. 本文提出将多臂老虎机强化学习算法与FDS相结合，通过优化分支决策来减少搜索树的规模。
3. 实验结果表明，增强后的FDS在JSSP和RCPSP基准测试中显著提升了求解速度，并改善了现有的下界。

## 📝 摘要（中文）

失败导向搜索（FDS）是一种在约束编程中广泛应用的完整搜索算法，特别适用于调度问题。本文分析了FDS的特性，指出通过排名分支决策来最小化搜索树的大小与多臂老虎机（MAB）问题密切相关。基于这一洞察，本文将MAB强化学习算法应用于FDS，并进行了问题特定的改进和参数调优。在作业车间调度问题（JSSP）和资源约束项目调度问题（RCPSP）这两种基本调度问题上进行了评估，结果显示，增强后的FDS在JSSP上比原始实现快1.7倍，在RCPSP上快2.1倍，同时在JSSP和RCPSP基准测试中均显著超越了IBM CP Optimizer 22.1的现有最优FDS算法。

## 🔬 方法详解

**问题定义**：本文旨在解决约束编程中失败导向搜索算法在调度问题上效率低下的问题，尤其是搜索树的大小影响了算法的性能。

**核心思路**：通过将多臂老虎机强化学习算法应用于FDS，优化分支决策，从而有效减少搜索树的大小，提高搜索效率。

**技术框架**：整体架构包括FDS的基本框架，结合MAB算法进行分支决策的优化，并进行问题特定的参数调优。主要模块包括搜索树生成、分支决策优化和性能评估。

**关键创新**：将MAB强化学习算法与FDS结合，提出了一种新的搜索树优化策略，与传统方法相比，显著提高了调度问题的求解效率。

**关键设计**：在参数设置上，针对不同问题进行了细致的调优，损失函数设计考虑了搜索树的大小和求解时间，确保了算法的高效性。具体的网络结构和算法细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，增强后的FDS在作业车间调度问题（JSSP）上比原始实现快1.7倍，在资源约束项目调度问题（RCPSP）上快2.1倍。此外，增强后的FDS在JSSP和RCPSP基准测试中也超越了IBM CP Optimizer 22.1的现有最优FDS算法，表现出3.5倍和2.1倍的速度提升。

## 🎯 应用场景

该研究的潜在应用领域包括工业调度、项目管理和资源分配等场景，能够显著提高调度算法的效率，降低资源消耗，具有重要的实际价值和广泛的应用前景。未来，随着算法的进一步优化和推广，可能会在更多复杂的调度问题中发挥作用。

## 📄 摘要（原文）

> Failure-Directed Search (FDS) is a significant complete generic search algorithm used in Constraint Programming (CP) to efficiently explore the search space, proven particularly effective on scheduling problems. This paper analyzes FDS's properties, showing that minimizing the size of its search tree guided by ranked branching decisions is closely related to the Multi-armed bandit (MAB) problem. Building on this insight, MAB reinforcement learning algorithms are applied to FDS, extended with problem-specific refinements and parameter tuning, and evaluated on the two most fundamental scheduling problems, the Job Shop Scheduling Problem (JSSP) and Resource-Constrained Project Scheduling Problem (RCPSP). The resulting enhanced FDS, using the best extended MAB algorithm and configuration, performs 1.7 times faster on the JSSP and 2.1 times faster on the RCPSP benchmarks compared to the original implementation in a new solver called OptalCP, while also being 3.5 times faster on the JSSP and 2.1 times faster on the RCPSP benchmarks than the current state-of-the-art FDS algorithm in IBM CP Optimizer 22.1. Furthermore, using only a 900-second time limit per instance, the enhanced FDS improved the existing state-of-the-art lower bounds of 78 of 84 JSSP and 226 of 393 RCPSP standard open benchmark instances while also completely closing a few of them.

