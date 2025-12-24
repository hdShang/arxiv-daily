---
layout: default
title: "BlackBoxToBlueprint: Extracting Interpretable Logic from Legacy Systems using Reinforcement Learning and Counterfactual Analysis"
---

# BlackBoxToBlueprint: Extracting Interpretable Logic from Legacy Systems using Reinforcement Learning and Counterfactual Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00180" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00180v1</a>
  <a href="https://arxiv.org/pdf/2507.00180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00180v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00180v1', 'BlackBoxToBlueprint: Extracting Interpretable Logic from Legacy Systems using Reinforcement Learning and Counterfactual Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vidhi Rathore

**分类**: cs.AI, cs.LG

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出一种新方法从遗留系统中提取可解释逻辑**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `遗留系统` `强化学习` `可解释性` `决策逻辑` `反事实分析` `软件现代化` `自动化测试`

## 📋 核心要点

1. 遗留系统现代化面临缺乏文档和理解复杂决策逻辑的挑战，传统方法无法有效捕捉系统意图。
2. 提出的管道利用强化学习代理探索输入空间，识别关键决策边界并提取可解释的决策逻辑。
3. 在三种不同复杂度的虚拟遗留系统上验证了该方法的有效性，提取的规则准确反映了系统核心逻辑。

## 📝 摘要（中文）

现代化遗留软件系统是一项关键但具有挑战性的任务，常因缺乏文档和对原系统复杂决策逻辑的理解而受阻。传统方法如行为克隆仅复制输入输出行为，而未能捕捉潜在意图。本文提出了一种新颖的管道，自动从被视为黑箱的遗留系统中提取可解释的决策逻辑。该方法利用强化学习（RL）代理探索输入空间，通过奖励导致系统输出显著变化的动作来识别关键决策边界。收集的反事实状态转变通过K-Means聚类，随后在这些聚类上训练决策树，以提取近似系统决策逻辑的人类可读规则。实验表明，该管道在三种不同复杂度的虚拟遗留系统上有效，提取的规则准确反映了核心逻辑，为遗留迁移中的规范生成和测试用例提供了有希望的基础。

## 🔬 方法详解

**问题定义**：本文旨在解决遗留软件系统现代化过程中缺乏文档和对复杂决策逻辑理解不足的问题。现有方法如行为克隆仅能复制输入输出行为，无法捕捉系统的真实意图，导致迁移过程中的困难。

**核心思路**：论文提出通过强化学习代理探索输入空间，识别关键决策边界。通过奖励机制鼓励代理在导致输出显著变化的状态转变上进行探索，从而提取出可解释的决策逻辑。

**技术框架**：整体流程包括：1) 强化学习代理探索输入空间，2) 收集反事实状态转变，3) 使用K-Means对状态转变进行聚类，4) 在聚类上训练决策树以提取可读规则。

**关键创新**：最重要的创新在于将强化学习与反事实分析结合，自动化提取遗留系统的决策逻辑。这一方法与传统的行为克隆方法本质上不同，后者无法捕捉系统的内在意图。

**关键设计**：在强化学习过程中，设计了特定的奖励机制以引导代理关注关键决策边界。聚类阶段采用K-Means算法，决策树的训练则使用标准的分类算法，确保提取的规则具有良好的可解释性。

## 📊 实验亮点

实验结果表明，强化学习代理成功聚焦于相关决策边界区域，提取的规则在三种虚拟遗留系统上准确反映了核心逻辑。具体而言，提取的规则在复杂度上与原系统的决策逻辑高度一致，为遗留系统的迁移提供了有效的支持。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、系统迁移和自动化测试等。通过提取可解释的决策逻辑，开发者可以更好地理解和维护遗留系统，进而提高系统的可用性和可维护性。这一方法为未来的遗留系统现代化提供了新的思路和工具。

## 📄 摘要（原文）

> Modernizing legacy software systems is a critical but challenging task, often hampered by a lack of documentation and understanding of the original system's intricate decision logic. Traditional approaches like behavioral cloning merely replicate input-output behavior without capturing the underlying intent. This paper proposes a novel pipeline to automatically extract interpretable decision logic from legacy systems treated as black boxes. The approach uses a Reinforcement Learning (RL) agent to explore the input space and identify critical decision boundaries by rewarding actions that cause meaningful changes in the system's output. These counterfactual state transitions, where the output changes, are collected and clustered using K-Means. Decision trees are then trained on these clusters to extract human-readable rules that approximate the system's decision logic near the identified boundaries. I demonstrated the pipeline's effectiveness on three dummy legacy systems with varying complexity, including threshold-based, combined-conditional, and non-linear range logic. Results show that the RL agent successfully focuses exploration on relevant boundary regions, and the extracted rules accurately reflect the core logic of the underlying dummy systems, providing a promising foundation for generating specifications and test cases during legacy migration.

