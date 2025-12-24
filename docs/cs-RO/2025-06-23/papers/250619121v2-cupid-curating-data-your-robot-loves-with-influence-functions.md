---
layout: default
title: "CUPID: Curating Data your Robot Loves with Influence Functions"
---

# CUPID: Curating Data your Robot Loves with Influence Functions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19121" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19121v2</a>
  <a href="https://arxiv.org/pdf/2506.19121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19121v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19121v2', 'CUPID: Curating Data your Robot Loves with Influence Functions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher Agia, Rohan Sinha, Jingyun Yang, Rika Antonova, Marco Pavone, Haruki Nishimura, Masha Itkina, Jeannette Bohg

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-23 (更新: 2025-09-23)

**备注**: Project page: https://cupid-curation.github.io. 27 pages, 15 figures. Accepted to the Conference on Robot Learning (CoRL) 2025

---

## 💡 一句话要点

**提出CUPID以解决机器人模仿学习中的数据质量问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人模仿学习` `数据策划` `影响函数` `策略优化` `闭环性能`

## 📋 核心要点

1. 现有的机器人模仿学习方法难以准确评估单个演示对策略性能的影响，导致数据质量不均。
2. CUPID通过影响函数理论来估计每个训练演示对策略预期回报的影响，从而优化数据选择。
3. 实验结果显示，使用少于33%的策划数据即可在模拟RoboMimic基准上实现最先进的扩散策略，硬件实验也取得类似效果。

## 📝 摘要（中文）

在机器人模仿学习中，策略性能与演示数据的质量和组成紧密相关。然而，如何准确理解单个演示对下游结果（如闭环任务成功或失败）的贡献仍然是一个持续的挑战。本文提出CUPID，一种基于新颖影响函数理论的机器人数据策划方法。CUPID通过评估每个训练演示对策略预期回报的影响，来对演示进行排名和选择，从而过滤掉有害的训练演示，并选择最能提升策略的新收集轨迹。大量的模拟和硬件实验表明，该方法能够有效识别驱动测试性能的数据。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人模仿学习中演示数据质量对策略性能影响评估的困难。现有方法往往无法准确识别哪些演示对任务成功有积极贡献，导致训练效果不佳。

**核心思路**：CUPID通过影响函数理论来量化每个训练演示对策略预期回报的影响，从而实现数据的有效筛选和优化。该方法的设计旨在提升策略的闭环性能，确保训练数据的高质量。

**技术框架**：CUPID的整体架构包括数据评估、影响计算、演示排名和选择等主要模块。首先，通过评估回合数据，计算每个演示的影响，然后根据影响力对演示进行排序，最后选择对策略性能提升最显著的演示进行训练。

**关键创新**：CUPID的核心创新在于引入影响函数理论来分析演示数据的贡献，这一方法与传统的随机选择或简单过滤方法有本质区别，能够更精确地识别有益数据。

**关键设计**：在实现过程中，CUPID采用了特定的损失函数来优化策略性能，并通过实验验证了不同参数设置对结果的影响，确保了方法的有效性和鲁棒性。实验中使用的网络结构经过精心设计，以适应不同类型的演示数据。

## 📊 实验亮点

实验结果表明，CUPID能够在模拟环境中使用少于33%的策划数据实现最先进的扩散策略，且在硬件实验中也取得了类似的性能提升。这表明该方法在数据选择和策略优化方面具有显著的效果。

## 🎯 应用场景

CUPID方法在机器人学习和自主系统中具有广泛的应用潜力，特别是在需要高质量演示数据的复杂任务中。其能够有效提升机器人在动态环境中的适应能力，未来可能在智能制造、服务机器人等领域发挥重要作用。

## 📄 摘要（原文）

> In robot imitation learning, policy performance is tightly coupled with the quality and composition of the demonstration data. Yet, developing a precise understanding of how individual demonstrations contribute to downstream outcomes - such as closed-loop task success or failure - remains a persistent challenge. We propose CUPID, a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies. Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return. This enables ranking and selection of demonstrations according to their impact on the policy's closed-loop performance. We use CUPID to curate data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy. Extensive simulated and hardware experiments show that our approach consistently identifies which data drives test-time performance. For example, training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Furthermore, hardware experiments show that our method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies. Videos and code are made available at: https://cupid-curation.github.io.

