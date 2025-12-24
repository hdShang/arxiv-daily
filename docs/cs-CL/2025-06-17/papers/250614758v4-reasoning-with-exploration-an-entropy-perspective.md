---
layout: default
title: "Reasoning with Exploration: An Entropy Perspective"
---

# Reasoning with Exploration: An Entropy Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14758" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14758v4</a>
  <a href="https://arxiv.org/pdf/2506.14758.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14758v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14758v4', 'Reasoning with Exploration: An Entropy Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daixuan Cheng, Shaohan Huang, Xuekai Zhu, Bo Dai, Wayne Xin Zhao, Zhenliang Zhang, Furu Wei

**分类**: cs.CL

**发布日期**: 2025-06-17 (更新: 2025-11-08)

**备注**: AAAI 2026 Conference

---

## 💡 一句话要点

**提出基于熵的探索方法以提升强化学习推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `推理能力` `探索与利用` `熵` `深度学习` `自然语言处理` `智能对话系统`

## 📋 核心要点

1. 现有方法在强化学习中多偏向利用，导致性能停滞，缺乏有效的探索机制。
2. 本文提出通过在优势函数中增加熵项来促进更长更深的推理链，从而增强探索能力。
3. 实验结果表明，该方法在Pass@K指标上显著提升，尤其在极大K值下表现优异。

## 📝 摘要（中文）

在强化学习中，平衡探索与利用是核心目标。尽管大型语言模型（LLM）推理能力有所提升，但现有方法多偏向利用，导致性能停滞。本文重新审视熵这一探索信号，探讨其与LLM探索性推理的关系。通过实证分析，发现高熵区域与三种探索性推理行为存在正相关。基于此，我们提出在标准强化学习中仅需一行代码的最小修改：在优势函数中增加基于熵的项。与传统最大熵方法不同，我们通过促进更长更深的推理链来鼓励探索。我们的方案在Pass@K指标上取得显著提升，推动了LLM推理的边界。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习中探索与利用的平衡问题，现有方法往往过于依赖利用，导致性能提升受限。

**核心思路**：我们提出通过在优势函数中增加熵的项来鼓励探索，特别是促进更长和更深的推理链，而非单纯增加不确定性。

**技术框架**：整体架构包括标准强化学习框架，主要模块为优势函数的修改，增加熵项后进行训练和评估。

**关键创新**：最重要的创新在于通过熵的引入，改变了探索的方式，强调推理链的深度和长度，而非仅仅是增加随机性。

**关键设计**：在优势函数中添加熵项的具体实现为一行代码，确保了方法的简洁性和易用性，同时在训练过程中保持了模型的稳定性。

## 📊 实验亮点

实验结果显示，所提方法在Pass@K指标上取得了显著提升，尤其在K值极大时，性能提升幅度超过了传统方法，展示了更强的推理能力和探索性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和自动推理等。通过提升LLM的推理能力，能够在更复杂的任务中实现更高的准确性和效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Balancing exploration and exploitation is a central goal in reinforcement learning (RL). Despite recent advances in enhancing large language model (LLM) reasoning, most methods lean toward exploitation, and increasingly encounter performance plateaus. In this work, we revisit entropy -- a signal of exploration in RL -- and examine its relationship to exploratory reasoning in LLMs. Through empirical analysis, we uncover positive correlations between high-entropy regions and three types of exploratory reasoning actions: (1) pivotal tokens that determine or connect logical steps, (2) reflective actions such as self-verification and correction, and (3) rare behaviors under-explored by the base LLMs. Motivated by this, we introduce a minimal modification to standard RL with only one line of code: augmenting the advantage function with an entropy-based term. Unlike traditional maximum-entropy methods which encourage exploration by promoting uncertainty, we encourage exploration by promoting longer and deeper reasoning chains. Notably, our method achieves significant gains on the Pass@K metric -- an upper-bound estimator of LLM reasoning capabilities -- even when evaluated with extremely large K values, pushing the boundaries of LLM reasoning.

