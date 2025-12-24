---
layout: default
title: The Limits of Preference Data for Post-Training
---

# The Limits of Preference Data for Post-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19964" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19964v1</a>
  <a href="https://arxiv.org/pdf/2505.19964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19964v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19964v1', 'The Limits of Preference Data for Post-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Zhao, Jessica Dai, Pranjal Awasthi

**分类**: cs.LG, cs.AI, cs.CL, cs.GT

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**研究偏好数据对后训练优化的限制及其影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `偏好数据` `强化学习` `人类反馈` `投票理论` `序数反馈` `模型优化` `推理行为`

## 📋 核心要点

1. 现有方法在需要人类反馈的领域中，偏好数据限制了结果优化的有效性。
2. 论文提出通过投票理论形式化偏好数据的局限性，强调人类评分和算法创新的重要性。
3. 研究发现偏好数据对强化学习人类反馈（RLHF）在推理行为的引导上影响显著，抑制了其能力。

## 📝 摘要（中文）

近年来，强化学习在大语言模型中的应用取得了显著进展，尤其是在可自动验证结果的领域。然而，在需要人类反馈的领域，结果评估往往是定性的，存在多种成功的可能性。本文研究了偏好数据在结果优化中的根本限制，发现即使在理想化的条件下，使用序数反馈也可能无法获得近似最优解。通过投票理论的类比，本文指出需要更扎实的人类评分和算法创新，以扩展强化学习后训练的成功。

## 🔬 方法详解

**问题定义**：本文解决的问题是偏好数据在后训练优化中的局限性，现有方法在处理需要人类反馈的任务时，无法有效评估结果，导致优化效果不佳。

**核心思路**：论文的核心思路是通过投票理论形式化偏好数据的限制，指出即使在理想条件下，序数反馈也无法保证接近最优解，从而强调了人类评分的重要性。

**技术框架**：整体架构包括三个主要模块：1) 偏好数据收集，2) 结果评估与优化，3) 人类反馈整合。每个模块都旨在解决特定的优化挑战。

**关键创新**：最重要的技术创新在于将投票理论应用于偏好数据的分析，揭示了其在优化过程中的根本限制，这与传统的强化学习方法有本质区别。

**关键设计**：在设计中，论文强调了理想化偏好数据的特征，如无限、无噪声和在线收集，同时探讨了如何通过人类评分来补充序数反馈的不足。具体的参数设置和损失函数设计尚未详细说明，需进一步研究。

## 📊 实验亮点

实验结果表明，偏好数据的局限性显著抑制了强化学习人类反馈（RLHF）在推理行为引导上的能力，尤其是在复杂任务中，模型的表现未能达到预期的优化效果，强调了人类评分的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括需要人类反馈的复杂任务，如深度研究和旅行规划。通过改进人类反馈的收集和整合方式，能够提升模型在这些领域的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent progress in strengthening the capabilities of large language models has stemmed from applying reinforcement learning to domains with automatically verifiable outcomes. A key question is whether we can similarly use RL to optimize for outcomes in domains where evaluating outcomes inherently requires human feedback; for example, in tasks like deep research and trip planning, outcome evaluation is qualitative and there are many possible degrees of success. One attractive and scalable modality for collecting human feedback is preference data: ordinal rankings (pairwise or $k$-wise) that indicate, for $k$ given outcomes, which one is preferred. In this work, we study a critical roadblock: preference data fundamentally and significantly limits outcome-based optimization. Even with idealized preference data (infinite, noiseless, and online), the use of ordinal feedback can prevent obtaining even approximately optimal solutions. We formalize this impossibility using voting theory, drawing an analogy between how a model chooses to answer a query with how voters choose a candidate to elect. This indicates that grounded human scoring and algorithmic innovations are necessary for extending the success of RL post-training to domains demanding human feedback. We also explore why these limitations have disproportionately impacted RLHF when it comes to eliciting reasoning behaviors (e.g., backtracking) versus situations where RLHF has been historically successful (e.g., instruction-tuning and safety training), finding that the limitations of preference data primarily suppress RLHF's ability to elicit robust strategies -- a class that encompasses most reasoning behaviors.

