---
layout: default
title: "Tracking World States with Language Models: State-Based Evaluation Using Chess"
---

# Tracking World States with Language Models: State-Based Evaluation Using Chess

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19851" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19851v1</a>
  <a href="https://arxiv.org/pdf/2508.19851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19851v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19851v1', 'Tracking World States with Language Models: State-Based Evaluation Using Chess')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Romain Harang, Jason Naradowsky, Yaswitha Gujju, Yusuke Miyao

**分类**: cs.AI

**发布日期**: 2025-08-27

**备注**: Spotlight presentation at ICML 2025 Workshop on Assessing World Models

---

## 💡 一句话要点

**提出一种状态基础评估框架以提升语言模型在棋类游戏中的表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `状态跟踪` `国际象棋` `模型评估` `语义保真度` `结构化环境` `深度学习`

## 📋 核心要点

1. 现有方法依赖模型特定的内部激活，限制了对语言模型的可解释性和普适性。
2. 本文提出了一种模型无关的状态基础评估框架，通过分析国际象棋的合法移动分布来评估语义保真度。
3. 实验结果显示，提出的评估指标能够有效捕捉LLMs在状态跟踪中的不足，揭示其在长序列中的局限性。

## 📝 摘要（中文）

大型语言模型（LLMs）在结构化领域展现出新兴能力，暗示它们可能隐含高保真度的世界模型表示。尽管探测技术在科学和游戏环境中显示出良好迹象，但依赖于模型特定的内部激活，限制了可解释性和普适性。本文提出了一种模型无关的状态基础评估框架，以国际象棋作为基准，评估LLMs是否保留结构化环境的语义。我们的方法分析下游合法移动分布（状态可供性），以估计预测与实际游戏状态之间的语义保真度。实验结果表明，我们的评估指标捕捉到了状态跟踪中的不足，突显了LLMs在长序列中保持一致内部模型的局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在结构化环境中状态跟踪的不足，现有方法的痛点在于缺乏可解释性和普适性。

**核心思路**：提出一种模型无关的评估框架，通过分析合法移动分布来评估模型对游戏状态的理解和保真度，旨在提供更具战略性和规则导向的评估方式。

**技术框架**：整体架构包括数据收集、状态分析和评估指标计算三个主要模块。首先收集国际象棋的游戏数据，然后分析合法移动的分布，最后计算预测状态与实际状态之间的语义保真度。

**关键创新**：最重要的技术创新在于提出了一种不依赖于模型内部激活的评估方法，使得评估过程更加透明和普适，能够广泛应用于各种符号环境。

**关键设计**：在评估过程中，采用了特定的损失函数来量化预测与实际状态之间的差异，并设计了适应不同游戏状态的参数设置，以确保评估的准确性和有效性。

## 📊 实验亮点

实验结果表明，提出的评估指标能够有效捕捉LLMs在状态跟踪中的不足，尤其是在长序列中，显示出与传统字符串基础指标相比，提升了对模型语义保真度的评估能力。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、教育工具和智能助手等。通过提供一种有效的评估框架，可以帮助开发者更好地理解和改进语言模型在复杂环境中的表现，从而提升其实际应用价值和用户体验。

## 📄 摘要（原文）

> Large Language Models (LLMs) exhibit emergent capabilities in structured domains, suggesting they may implicitly internalize high-fidelity representations of world models. While probing techniques have shown promising signs of this in scientific and game-based settings, they rely on model-specific internal activations, which limit interpretability and generalizability. In this work, we propose a model-agnostic, state-based evaluation framework using chess as a benchmark to assess whether LLMs preserve the semantics of structured environments. Our method analyzes the downstream legal move distributions (state affordances) to estimate semantic fidelity between predicted and actual game states. This approach offers a more meaningful evaluation than conventional string-based metrics by aligning more closely with the strategic and rule-governed nature of chess. Experimental results demonstrate that our metrics capture deficiencies in state-tracking, highlighting limitations of LLMs in maintaining coherent internal models over long sequences. Our framework provides a robust tool for evaluating structured reasoning in LLMs without requiring internal model access, and generalizes to a wide class of symbolic environments.

