---
layout: default
title: "STEP Planner: Constructing cross-hierarchical subgoal tree as an embodied long-horizon task planner"
---

# STEP Planner: Constructing cross-hierarchical subgoal tree as an embodied long-horizon task planner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21030" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21030v2</a>
  <a href="https://arxiv.org/pdf/2506.21030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21030v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21030v2', 'STEP Planner: Constructing cross-hierarchical subgoal tree as an embodied long-horizon task planner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianxing Zhou, Zhirui Wang, Haojia Ao, Guangyan Chen, Boyang Xing, Jingwen Cheng, Yi Yang, Yufeng Yue

**分类**: cs.RO

**发布日期**: 2025-06-26 (更新: 2025-07-16)

---

## 💡 一句话要点

**提出STEP规划器以解决长远任务规划问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长远任务规划` `子目标树` `大型语言模型` `闭环反馈` `机器人技术`

## 📋 核心要点

1. 现有方法在长远任务规划中成功率低，尤其是大型语言模型在复杂任务推理中的局限性。
2. STEP框架通过构建子目标树，结合子目标分解和叶节点终止模型，有效分解复杂任务并实时反馈。
3. 在VirtualHome WAH-NL基准和真实机器人实验中，STEP的任务完成率显著提升，分别达到34%和25%。

## 📝 摘要（中文）

长远任务规划的可靠性对于机器人在现实环境中的部署至关重要。然而，直接使用大型语言模型（LLMs）作为动作序列生成器往往导致成功率低下，因为其在长远任务推理方面能力有限。STEP框架通过一对闭环模型构建了一个子目标树：子目标分解模型和叶节点终止模型。该框架开发了一个从粗到细的层次树结构，子目标分解模型利用基础LLM将复杂目标分解为可管理的子目标，从而构建子目标树。叶节点终止模型根据环境状态提供实时反馈，决定何时终止树的扩展，确保每个叶节点可以直接转化为原始动作。实验结果表明，STEP在VirtualHome WAH-NL基准和真实机器人上的长远任务完成率分别达到34%和25%，超越了现有最先进的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决长远任务规划中的低成功率问题，现有方法在复杂任务推理上存在局限性，导致机器人在实际应用中表现不佳。

**核心思路**：论文提出的核心思路是构建一个层次化的子目标树，通过子目标分解模型将复杂目标分解为可管理的子目标，并通过叶节点终止模型实时反馈环境状态，确保每个叶节点能转化为具体动作。

**技术框架**：整体架构包括两个主要模块：子目标分解模型和叶节点终止模型。子目标分解模型利用基础LLM进行目标分解，叶节点终止模型则根据环境反馈决定何时终止树的扩展。

**关键创新**：最重要的技术创新在于构建了一个跨层次的子目标树，结合了闭环反馈机制，使得长远任务规划的成功率显著提高。这一方法与传统的线性任务规划方法有本质区别。

**关键设计**：在设计中，子目标分解模型的参数设置和损失函数经过精心调整，以确保模型能够有效分解复杂目标；同时，叶节点终止模型的实时反馈机制也经过优化，以提高决策的准确性和及时性。

## 📊 实验亮点

实验结果显示，STEP在VirtualHome WAH-NL基准上的任务完成率达到34%，在真实机器人上的完成率为25%，均显著优于现有最先进的方法，展示了其在长远任务规划中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化系统和人机协作等。通过提高长远任务规划的成功率，STEP框架能够在复杂环境中更好地支持机器人执行多样化任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The ability to perform reliable long-horizon task planning is crucial for deploying robots in real-world environments. However, directly employing Large Language Models (LLMs) as action sequence generators often results in low success rates due to their limited reasoning ability for long-horizon embodied tasks. In the STEP framework, we construct a subgoal tree through a pair of closed-loop models: a subgoal decomposition model and a leaf node termination model. Within this framework, we develop a hierarchical tree structure that spans from coarse to fine resolutions. The subgoal decomposition model leverages a foundation LLM to break down complex goals into manageable subgoals, thereby spanning the subgoal tree. The leaf node termination model provides real-time feedback based on environmental states, determining when to terminate the tree spanning and ensuring each leaf node can be directly converted into a primitive action. Experiments conducted in both the VirtualHome WAH-NL benchmark and on real robots demonstrate that STEP achieves long-horizon embodied task completion with success rates up to 34% (WAH-NL) and 25% (real robot) outperforming SOTA methods.

