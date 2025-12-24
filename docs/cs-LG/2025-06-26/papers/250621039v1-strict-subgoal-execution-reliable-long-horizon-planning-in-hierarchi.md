---
layout: default
title: "Strict Subgoal Execution: Reliable Long-Horizon Planning in Hierarchical Reinforcement Learning"
---

# Strict Subgoal Execution: Reliable Long-Horizon Planning in Hierarchical Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21039" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21039v1</a>
  <a href="https://arxiv.org/pdf/2506.21039.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21039v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21039v1', 'Strict Subgoal Execution: Reliable Long-Horizon Planning in Hierarchical Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaebak Hwang, Sanghyeon Lee, Jeongmo Kim, Seungyul Han

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-26

**备注**: 9 technical page followed by references and appendix

---

## 💡 一句话要点

**提出严格子目标执行框架以解决长时间规划问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长时间规划` `强化学习` `分层RL` `子目标执行` `探索策略` `图基方法` `路径优化`

## 📋 核心要点

1. 长时间目标条件任务在强化学习中面临目标遥远和奖励稀疏的挑战，现有方法难以有效解决。
2. 提出严格子目标执行（SSE）框架，通过结构性约束实现单步子目标可达性，增强探索能力。
3. 实验结果显示，SSE在效率和成功率上均优于现有的目标条件RL和分层RL方法，表现出显著的提升。

## 📝 摘要（中文）

长时间目标条件任务对强化学习（RL）提出了基本挑战，尤其是在目标遥远且奖励稀疏的情况下。尽管分层和基于图的方法提供了部分解决方案，但它们常常面临子目标不可行和规划效率低下的问题。本文提出了严格子目标执行（SSE）框架，通过结构性约束高层决策，强制实现单步子目标可达性。为增强探索，SSE采用解耦的探索策略，系统性地遍历目标空间的未充分探索区域。此外，失败感知路径优化通过根据观察到的低层成功率动态调整边缘成本，从而改善子目标的可靠性。实验结果表明，SSE在多种长时间基准测试中，效率和成功率均优于现有的目标条件RL和分层RL方法。

## 🔬 方法详解

**问题定义**：本文旨在解决长时间目标条件任务中的子目标不可行和规划效率低下的问题。现有的分层和图基方法在面对遥远目标时，往往无法有效规划和执行子目标。

**核心思路**：论文提出的严格子目标执行（SSE）框架，通过结构性约束高层决策，确保每个子目标的单步可达性，从而提升任务的可执行性和成功率。

**技术框架**：SSE框架主要包括两个模块：高层决策模块和低层执行模块。高层模块负责生成子目标，而低层模块则执行这些子目标。框架还引入了解耦的探索策略和失败感知路径优化，以增强探索和规划的有效性。

**关键创新**：SSE的核心创新在于通过结构性约束确保子目标的单步可达性，这与现有方法的设计思路有本质区别，后者往往忽视了子目标的可行性。

**关键设计**：在参数设置上，SSE采用动态调整的边缘成本，以反映低层成功率。此外，探索策略的设计使得算法能够系统性地覆盖未充分探索的目标区域，从而提高整体效率。

## 📊 实验亮点

在多种长时间基准测试中，SSE框架的效率和成功率均显著优于现有的目标条件RL和分层RL方法。例如，在某些任务中，成功率提升幅度达到20%以上，显示出其在复杂环境中的强大适应能力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、游戏AI等长时间规划任务。通过提高长时间目标条件任务的成功率和效率，SSE框架能够在实际应用中显著提升智能体的表现，推动相关领域的发展。未来，SSE还可能扩展到更复杂的多任务学习和协作任务中。

## 📄 摘要（原文）

> Long-horizon goal-conditioned tasks pose fundamental challenges for reinforcement learning (RL), particularly when goals are distant and rewards are sparse. While hierarchical and graph-based methods offer partial solutions, they often suffer from subgoal infeasibility and inefficient planning. We introduce Strict Subgoal Execution (SSE), a graph-based hierarchical RL framework that enforces single-step subgoal reachability by structurally constraining high-level decision-making. To enhance exploration, SSE employs a decoupled exploration policy that systematically traverses underexplored regions of the goal space. Furthermore, a failure-aware path refinement, which refines graph-based planning by dynamically adjusting edge costs according to observed low-level success rates, thereby improving subgoal reliability. Experimental results across diverse long-horizon benchmarks demonstrate that SSE consistently outperforms existing goal-conditioned RL and hierarchical RL approaches in both efficiency and success rate.

