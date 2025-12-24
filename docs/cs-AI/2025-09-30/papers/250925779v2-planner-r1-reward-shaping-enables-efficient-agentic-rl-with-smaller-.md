---
layout: default
title: "Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs"
---

# Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25779" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25779v2</a>
  <a href="https://arxiv.org/pdf/2509.25779.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25779v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25779v2', 'Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Zhu, Yanbin Jiang, Hejian Sang, Shao Tang, Qingquan Song, Biao He, Rohit Jain, Zhipeng Wang, Alborz Geramifard

**分类**: cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出Planner-R1以提升小型LLM在Agentic RL中的效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励塑造` `Agentic RL` `小型语言模型` `计算效率` `内存效率` `智能规划` `深度学习`

## 📋 核心要点

1. 现有方法在Agentic RL中对大型语言模型的依赖导致计算和内存效率低下。
2. 提出的Planner-R1通过奖励塑造技术，显著提升了小型模型在Agentic RL任务中的表现。
3. 实验结果显示，8B模型在效率和性能上均优于32B模型，且在多个任务上保持了良好的泛化能力。

## 📝 摘要（中文）

我们在TravelPlanner基准上研究了大型语言模型的Agentic RL。我们的方法Planner-R1在仅180个训练查询的情况下达到了56.9%的最终通过率，比GPT-5的21.2%基线提高了2.7倍，并在公共排行榜上取得了最强的Agentic结果。研究发现，小型模型（8B）对奖励塑造高度敏感：在密集的过程级信号下，它们的性能具有竞争力，同时在计算效率上比32B模型高出3.5倍，内存效率高出1.5倍。尽管较大模型在稀疏奖励下更为稳健，但它们从奖励塑造中获得的相对增益较小，且运行间方差较高。重要的是，这些提升并未以过拟合为代价，微调后的模型在多个领域外任务上大多保持或超越基线性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决在Agentic RL中使用大型语言模型时的计算和内存效率问题，现有方法往往依赖于更大的模型，导致资源消耗过高。

**核心思路**：论文提出的Planner-R1方法通过奖励塑造来提升小型模型的学习效率，使其在Agentic RL任务中表现出色。通过密集的过程级信号，小型模型能够在较少的训练查询下实现竞争力的性能。

**技术框架**：整体架构包括奖励塑造模块和模型训练模块。奖励塑造模块负责生成过程级信号，而模型训练模块则利用这些信号进行高效的学习。

**关键创新**：最重要的技术创新在于通过奖励塑造显著提升小型模型的学习动态，使其在计算和内存使用上更为高效。这一方法与传统依赖大型模型的方式形成鲜明对比。

**关键设计**：在参数设置上，使用了8B的小型模型，并通过密集的奖励信号进行训练。损失函数设计上，强调了过程级信号的引入，以增强模型的学习能力。

## 📊 实验亮点

实验结果显示，Planner-R1在TravelPlanner基准上达到了56.9%的最终通过率，比GPT-5的21.2%基线提高了2.7倍。8B模型在计算和内存效率上分别比32B模型高出3.5倍和1.5倍，且在多个领域外任务上保持了良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化规划和决策支持系统等。通过提升小型模型的效率，Planner-R1可以在资源受限的环境中实现更高效的Agentic RL应用，推动智能系统的普及与发展。

## 📄 摘要（原文）

> We investigated Agentic RL with large language models on the \textsc{TravelPlanner} benchmark. Our approach, \textsc{Planner-R1}, achieved a \textbf{56.9\%} final-pass rate with only 180 training queries, a $2.7\times$ improvement over GPT-5's $21.2\%$ baseline and the strongest agentic result on the public leaderboard. A central finding was that smaller models (8B) were highly responsive to reward shaping: with dense process-level signals, they reached competitive performance while being $3.5\times$ more compute-efficient and $1.5\times$ more memory-efficient than 32B models. Larger models were more robust under sparse rewards but exhibited smaller relative gains from shaping and higher variance across runs. While curriculum learning offered no significant benefit, shaped rewards consistently amplified learning dynamics, making 8B models the most efficient setting for agentic RL. Crucially, these gains did not come at the cost of overfitting: fine-tuned models mostly maintained or exceeded baseline performance on out-of-domain tasks, including \textsc{Multi-IF}, \textsc{NaturalPlan}, and $τ$-\textsc{Bench}. These results establish reward shaping as a decisive lever for scaling agentic RL, highlight the competitive strength of smaller models, and demonstrate that efficiency can be achieved without sacrificing generalization.

