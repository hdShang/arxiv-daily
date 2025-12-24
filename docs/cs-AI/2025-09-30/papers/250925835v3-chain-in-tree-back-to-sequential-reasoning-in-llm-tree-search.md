---
layout: default
title: "Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search"
---

# Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25835" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25835v3</a>
  <a href="https://arxiv.org/pdf/2509.25835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25835v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25835v3', 'Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinzhe Li

**分类**: cs.AI

**发布日期**: 2025-09-30 (更新: 2025-10-18)

**备注**: Under Review; Add codebase

**🔗 代码/项目**: [GITHUB](https://github.com/xinzhel/chain_in_tree)

---

## 💡 一句话要点

**Chain-in-Tree：通过动态分支策略提升LLM树搜索效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM树搜索` `长程推理` `分支必要性评估` `动态分支策略` `计算效率优化`

## 📋 核心要点

1. 现有LLM树搜索方法（LITS）虽然性能强大，但计算效率低下，速度远低于迭代方法。
2. Chain-in-Tree (CiT) 框架通过引入分支必要性评估，动态决定何时进行分支，减少不必要扩展。
3. 实验表明，CiT显著减少了token生成、模型调用和运行时间，同时保持或略微提升了准确率。

## 📝 摘要（中文）

本文提出Chain-in-Tree (CiT)，一个即插即用的框架，用于在LLM树搜索过程中动态决定何时进行分支，而非每一步都扩展。CiT引入轻量级的“分支必要性”（Branching Necessity, BN）评估方法：BN-DP（直接提示），利用辅助LLM判断分支需求；BN-SC（自洽性），通过聚类候选动作来评估一致性。集成到Tree of Thoughts、ReST-MCTS和RAP后，BN-DP在GSM8K和Math500上实现了75-85%的token生成、模型调用和运行时间减少，且通常精度损失可忽略不计或没有损失。BN-SC通常也能显著节省资源（高达80%），但在14个设置中的1-4个中表现出不稳定性，这是由一小部分产生极长推理步骤的例子引起的。理论证明BN-DP永远不会增加策略调用次数。论文发布了模块化的LITS实现和一个轻量级的CiT函数，适用于所有LITS变体。完整的代码库可在https://github.com/xinzhel/chain_in_tree公开获取。

## 🔬 方法详解

**问题定义**：现有基于LLM的树搜索方法，如Tree of Thoughts等，在每一步都进行分支扩展，导致计算量巨大，效率低下。尤其是在长程推理任务中，这种盲目扩展会浪费大量计算资源，成为实际应用的瓶颈。

**核心思路**：CiT的核心思想是并非每一步都需要进行分支，而是应该根据当前状态和潜在动作的价值，动态地决定是否需要进行分支。通过引入“分支必要性”评估，避免不必要的分支扩展，从而提高整体搜索效率。

**技术框架**：CiT是一个即插即用的框架，可以集成到现有的LITS方法中，如Tree of Thoughts、ReST-MCTS和RAP。其主要流程包括：1) 在每个搜索步骤中，首先进行分支必要性评估；2) 如果评估结果表明需要分支，则进行正常的动作采样和扩展；3) 如果评估结果表明不需要分支，则继续沿着当前路径进行推理。

**关键创新**：CiT的关键创新在于提出了两种轻量级的“分支必要性”（BN）评估方法：BN-DP（Direct Prompting）和BN-SC（Self-Consistency）。BN-DP利用辅助LLM直接判断是否需要分支，而BN-SC则通过聚类候选动作来评估一致性，从而间接判断分支的必要性。与现有方法在每一步都进行分支扩展不同，CiT只在必要时才进行分支，从而显著减少了计算量。

**关键设计**：BN-DP通过设计特定的prompt，让辅助LLM判断当前状态是否需要分支。BN-SC则首先采样多个候选动作，然后使用聚类算法（如K-means）将这些动作分组。如果大部分动作属于同一个簇，则认为当前状态不需要分支，因为模型已经找到了一个相对明确的方向。具体的聚类算法和参数设置需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，在GSM8K和Math500数据集上，集成BN-DP的CiT框架能够减少75-85%的token生成、模型调用和运行时间，同时保持或略微提升了准确率。BN-SC虽然通常也能显著节省资源（高达80%），但在少数情况下表现出不稳定性。这些结果表明，CiT是一种有效的LLM树搜索优化方法，能够显著提高推理效率。

## 🎯 应用场景

CiT框架可广泛应用于需要长程推理和规划的场景，例如数学问题求解、代码生成、游戏AI、机器人导航等。通过提高LLM树搜索的效率，CiT能够降低计算成本，并使得LLM能够在资源受限的环境中执行更复杂的任务。未来，CiT可以进一步扩展到其他类型的LLM推理方法中，并与其他优化技术相结合，以实现更高的效率和性能。

## 📄 摘要（原文）

> Test-time scaling improves large language models (LLMs) on long-horizon reasoning tasks by allocating more compute at inference. LLM Inference via Tree Search (LITS) methods achieve strong performance but are highly inefficient, often running an order of magnitude slower than iterative approaches. We propose Chain-in-Tree (CiT), a plug-in framework that decides when to branch during search rather than expanding at every step. CiT introduces lightweight Branching Necessity (BN) evaluations: BN-DP (Direct Prompting), where an auxiliary LLM judges branching needs, and BN-SC (Self-Consistency), which clusters candidate actions to assess agreement. Integrated into Tree of Thoughts, ReST-MCTS, and RAP, BN-DP achieves 75-85% reductions in token generation, model calls, and runtime on GSM8K and Math500, with often negligible or no accuracy loss. BN-SC typically yields substantial savings (up to 80%) generally but shows instability in 1-4 out of 14 settings, caused by a small subset of examples that produce extremely long reasoning steps. We theoretically prove that BN-DP never increases policy invocations and release both modular LITS implementations and a lightweight CiT function applicable across all LITS variants. The full codebase is publicly available at https://github.com/xinzhel/chain_in_tree.

